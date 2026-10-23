"""用 OpenAI 图像模型生成角色/场景图。
需要环境变量 OPENAI_API_KEY；模型名可用 OPENAI_IMAGE_MODEL 覆盖（默认 gpt-image-1）。
用法：
  python3 gpt_generate.py 角色名 输出目录 [--ref]     # --ref：以 characters/<角色>.png 为参考图重绘
"""
import base64, json, os, sys, urllib.request, uuid
sys.path.insert(0, os.path.dirname(__file__))
from characters_v2 import CHARS

MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
HERE = os.path.dirname(os.path.abspath(__file__))
STYLE = ("Illustration for a literary sci-fi novel. Flat-color cut-paper / layered paper style with halftone dot texture, "
         "sharp graphic shadow shapes, rich small details, limited palette. No text other than what is described, no watermark.")

def _post(url, body, content_type):
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"], "Content-Type": content_type})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=300).read())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read()[:800].decode(errors='replace')}")

def generate(prompt, out, size="1024x1536", ref=None):
    if ref:
        b = uuid.uuid4().hex; parts = []
        for k, v in (("model", MODEL), ("prompt", prompt), ("size", size), ("quality", "high")):
            parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="image[]"; filename="ref.png"\r\nContent-Type: image/png\r\n\r\n'.encode()
                     + open(ref, "rb").read() + b"\r\n")
        parts.append(f"--{b}--\r\n".encode())
        r = _post("https://api.openai.com/v1/images/edits", b"".join(parts), f"multipart/form-data; boundary={b}")
    else:
        r = _post("https://api.openai.com/v1/images/generations",
                  json.dumps({"model": MODEL, "prompt": prompt, "size": size, "quality": "high"}).encode(), "application/json")
    open(out, "wb").write(base64.b64decode(r["data"][0]["b64_json"])); print("ok", out)

if __name__ == "__main__":
    name, outdir = sys.argv[1], sys.argv[2]; use_ref = "--ref" in sys.argv
    os.makedirs(outdir, exist_ok=True)
    color, desc, bg = CHARS[name]
    prompt = f"{STYLE}\nCharacter design: {desc.replace('1.4::', '').replace('1.6::', '').replace('1.3::', '').replace('::', '')}.\nComposition: {bg}.\nColor palette: {color}."
    if use_ref:
        prompt = "Redraw this character with the same design, adding more detail. " + prompt
    size = "1536x1024" if name == "meridian" else "1024x1536"
    ref = os.path.join(HERE, "..", "characters", f"{name}.png") if use_ref else None
    generate(prompt, os.path.join(outdir, f"{name}_gpt.png"), size, ref)
