"""角色设定图 v3：handraw-style 风格库 FB-047（Isabelle Arsenault 诗意铅笔+水粉绘本）。
NovelAI 不在该库的已校准模型内，按其规则必须垫参考图：这里用 Vibe Transfer 只迁移画风（参考图已裁去署名文字）。
配色沿用 v2 的性格配色，在铅笔灰底上作为“唯一点缀色”。
用法：python3 characters_v3.py [角色名...] 输出目录"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from nai_generate import gen

HERE = os.path.dirname(os.path.abspath(__file__))
VIBE = os.path.join(HERE, "..", "style_refs", "FB-047_arsenault.nai45.vibe")
STYLE_V3 = ("traditional media, graphite (medium), colored pencil (medium), gouache (medium), picture book illustration, "
            "soft pencil lines, grainy pencil shading, cream paper, paper texture, muted colors, single color accent, "
            "poetic, quiet, negative space, best quality, very aesthetic")
NEG_V3 = ("anime screencap, cel shading, glossy, 3d, realistic, photo, digital painting, neon, rainbow, text, watermark, "
          "signature, lowres, bad hands, extra fingers, deformed, nsfw")

# (点缀色, 角色描述) —— 描述按 ip-designer 的“文字简洁，画面不碎”原则只保留识别锚点
CHARS = {
    "sylvia": ("orange accent on her jacket, everything else in graphite gray",
               "1girl, solo, 16 years old, long wavy hair, messy bangs, tired gentle eyes, quiet determination, "
               "oversized work jacket with patches, small rabbit sticker, rolled sleeves, earphones around neck, "
               "bandage on index finger, holding a screwdriver, full body, standing"),
    "father": ("1.6::indigo blue cardigan::, deep blue accent, everything else in graphite gray",
               "1man, solo, middle-aged, lean, short hair with gray streaks, glasses, stubble, quiet tired expression, "
               "knit cardigan over collared shirt, company id badge, holding small black notebook, "
               "warm mug of milk in other hand, full body, standing"),
    "alice": ("1.5::glowing pale gold light::, gold colored pencil, golden aura, everything else in faint graphite",
              "1girl, solo, alice, translucent ghostly figure made of light, long hair dissolving into lines of tiny text, "
              "small glass vase pendant, curious gentle smile, half-closed eyes, simple long dress, "
              "a few tiny golden flowers floating, floating, full body"),
    "hk7": ("1.5::brass gold stripes and gold joints::, yellow gold accent, everything else in graphite gray",
            "no humans, 1.3::old humanoid household robot::, solo, round head with single camera lens eye, small antenna, "
            "rounded worn shell, brass joints, dents and scratches, repair tape on bent left knee, "
            "sitting on the floor, holding small watering can, gentle posture, full body"),
    "ethan": ("1.5::teal shirt::, teal accent, everything else in graphite gray",
              "1boy, solo, 26 years old, young engineer, short messy hair, earnest bright eyes, eager smile, "
              "work shirt with rolled sleeves, company lanyard, safety glasses pushed up on head, "
              "holding printed temperature graph, full body, standing"),
    "meridian": ("1.6::deep indigo blue night sky::, blue gouache wash, pale white-gold sun, everything else in graphite",
                 "no humans, 1.5::colossal faceless human silhouette, head and shoulders::, rising behind tiny datacenter buildings "
                 "on the horizon, 1.4::huge pale sun disc halo behind its head::, small sun emblem on its chest, "
                 "power lines, night, wide shot, vast scale contrast"),
}

if __name__ == "__main__":
    out = sys.argv[-1]; names = sys.argv[1:-1] or list(CHARS)
    os.makedirs(out, exist_ok=True)
    n_each = int(os.environ.get("N_EACH", 3)); strength = float(os.environ.get("VIBE_STRENGTH", 0.6))
    for n in names:
        color, desc = CHARS[n]
        w, h = (1216, 832) if n == "meridian" else (832, 1216)
        for i in range(1, n_each + 1):
            gen(f"{desc}, {color}", f"{out}/{n}_{i}.png", w, h, style=STYLE_V3, neg=NEG_V3, vibes=[(VIBE, strength)])
