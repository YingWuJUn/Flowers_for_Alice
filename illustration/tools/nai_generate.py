import json, os, sys, io, zipfile, random, urllib.request
STYLE = "limited palette, orange theme, three-tone, flat color, high contrast, no gradients, cut-paper style, graphic shapes, sharp shadow shapes, cream white highlights, dark brown background, subtle dot pattern background, minimalist, clean silhouette, best quality, very aesthetic"
NEG = "gradient, realistic, 3d, photo, blurry, lineart heavy, sketch, extra colors, rainbow, neon, text, watermark, signature, lowres, bad hands, extra fingers, deformed, nsfw"
def gen(prompt, out, w=832, h=1216, seed=None, model="nai-diffusion-4-5-full"):
    seed = seed or random.randint(1, 2**32-1)
    full = prompt + ", " + STYLE
    body = {"input": full, "model": model, "action": "generate", "parameters": {
        "params_version": 3, "width": w, "height": h, "scale": 5, "sampler": "k_euler_ancestral",
        "steps": 28, "n_samples": 1, "ucPreset": 0, "qualityToggle": True, "seed": seed,
        "noise_schedule": "karras", "negative_prompt": NEG, "cfg_rescale": 0,
        "v4_prompt": {"caption": {"base_caption": full, "char_captions": []}, "use_coords": False, "use_order": True},
        "v4_negative_prompt": {"caption": {"base_caption": NEG, "char_captions": []}, "legacy_uc": False},
    }}
    req = urllib.request.Request("https://image.novelai.net/ai/generate-image", data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["NOVELAI_API_TOKEN"], "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36", "Origin": "https://novelai.net", "Referer": "https://novelai.net/"})
    try:
        data = urllib.request.urlopen(req, timeout=180).read()
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read()[:500]); return False
    z = zipfile.ZipFile(io.BytesIO(data))
    open(out, "wb").write(z.read(z.namelist()[0])); print("ok", out, seed); return True
if __name__ == "__main__":
    gen(sys.argv[1], sys.argv[2])
