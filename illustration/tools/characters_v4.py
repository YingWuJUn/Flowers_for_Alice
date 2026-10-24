"""角色设定图 v4：在 v3（handraw-style FB-047 绘本画风 + Vibe Transfer）基础上，
把提示词改写为标准 Danbooru 标签。标签用 danbooru-diffusion-prompt-builder（https://github.com/wfjsw/danbooru-diffusion-prompt-builder）
的标签库核对，data/danbooru_tags_zh.json 是从中导出的 {标签: [中文名, 分类, 帖子数]}。
用法：python3 characters_v4.py [角色名...] 输出目录      python3 characters_v4.py --check   # 列出每个标签是否在标签库中
"""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(__file__))
from nai_generate import gen

HERE = os.path.dirname(os.path.abspath(__file__))
VIBE = os.path.join(HERE, "..", "style_refs", "FB-047_arsenault.nai45.vibe")
# spot color = 黑白画中的少量颜色，正好对应“铅笔灰底 + 单一点缀色”
STYLE_V4 = ("traditional media, graphite (medium), colored pencil (medium), watercolor pencil (medium), hatching (texture), "
            "1.3::spot color::, limited palette, muted color, negative space, simple background, masterpiece, best quality")
# 标签库中 NovelAI 预设“Low Quality + Bad Anatomy”，另加画风排除项
NEG_V4 = ("lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, "
          "low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, "
          "3d, realistic, photo, anime screencap, colorful, multicolored")

CHARS = {
    # 元气少女版：去掉 tired / determined，换成咧嘴笑、虎牙、呆毛、动态姿势
    "sylvia": "1girl, solo, teenage, long hair, wavy hair, messy hair, ahoge, bangs, bright pupils, sparkling eyes, "
              ":d, grin, fang, blush, happy, looking at viewer, leaning forward, ;d, v, "
              "1.4::orange jacket::, oversized clothes, open jacket, sleeves pushed up, headphones around neck, "
              "bandaged hands, holding screwdriver, patch, badge, jeans, sneakers, motion lines, full body",
    "father": "1boy, solo, mature male, middle-aged, grey hair, streaked hair, short hair, glasses, facial hair, stubble, tired, serious, "
              "1.5::blue cardigan::, collared shirt, lanyard, id card, holding notebook, holding mug, milk, full body, standing",
    "alice":  "1girl, solo, ghost, transparent, glowing, 1.4::yellow theme::, golden light, long hair, floating hair, light smile, "
              "half-closed eyes, white dress, pendant, vase, petals, flower, floating, full body",
    # 金发试验版：在上一版基础上只加金发
    "alice_blonde": "1girl, solo, ghost, transparent, glowing, 1.4::yellow theme::, golden light, 1.4::blonde hair::, long hair, "
                    "floating hair, light smile, half-closed eyes, white dress, pendant, vase, petals, flower, floating, full body",
    "hk7":    "no humans, solo, 1.4::humanoid robot::, old, damaged, round head, one-eyed, camera, antenna, "
              "1.4::gold trim::, yellow stripes, mechanical joints, bandaged leg, sitting, holding watering can, full body",
    "ethan":  "1boy, solo, young man, short hair, messy hair, black hair, smile, open mouth, "
              "1.4::aqua shirt::, collared shirt, sleeves rolled up, lanyard, id card, goggles on head, "
              "holding paper, chart, full body, standing",
    "meridian": "no humans, 1.6::colossal faceless human silhouette, head and shoulders::, silhouette, faceless, 1.4::white sun::, halo, sun symbol, "
                "1.7::dark blue night sky::, blue theme, starry sky, power lines, building, cityscape, horizon, wide shot",
}

def check():
    idx = json.load(open(os.path.join(HERE, "data", "danbooru_tags_zh.json")))
    for name, prompt in [("STYLE", STYLE_V4)] + list(CHARS.items()):
        tags = [re.sub(r"\d\.\d::|::", "", t).strip() for t in prompt.split(",")]
        print(f"[{name}]", "  ".join(f"{t}({idx[t][0]})" if t in idx else f"{t}(?)" for t in tags if t))

if __name__ == "__main__":
    if "--check" in sys.argv: check(); sys.exit()
    out = sys.argv[-1]; names = sys.argv[1:-1] or list(CHARS)
    os.makedirs(out, exist_ok=True)
    n_each = int(os.environ.get("N_EACH", 3)); strength = float(os.environ.get("VIBE_STRENGTH", 0.5))
    for n in names:
        w, h = (1216, 832) if n == "meridian" else (832, 1216)
        for i in range(1, n_each + 1):
            gen(CHARS[n], f"{out}/{n}_{i}.png", w, h, style=STYLE_V4, neg=NEG_V4, vibes=[(VIBE, strength)])
