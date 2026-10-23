"""角色设定图 v2：更多细节 + 按性格区分的配色。用法：python3 characters_v2.py [角色名...] 输出目录"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from nai_generate import gen

STYLE_V2 = ("limited palette, flat color, cut-paper style, layered paper, graphic shapes, sharp shadow shapes, "
            "halftone dot texture, detailed, intricate details, detailed clothing, decorative background pattern, "
            "masterpiece, best quality, very aesthetic")

# 每个角色：(配色, 角色描述, 背景/道具)
CHARS = {
    # 倔强、温暖、动手派 —— 故事的主色：橙 / 米白 / 深棕
    "sylvia": ("orange theme, cream white and dark brown, warm colors",
               "1girl, solo, 16 years old, long wavy hair, slightly messy bangs, tired gentle eyes, determined, "
               "oversized work jacket with many pockets and patches, faded rabbit sticker on jacket, rolled sleeves, plain t-shirt, "
               "jeans, worn sneakers, earphones around neck, screwdriver in pocket, tool pouch on belt, bandage on index finger, "
               "holding circuit board",
               "cowboy shot, background of scattered electronic parts, cables, gears and small mint leaves"),
    # 沉默、克制、背负秘密 —— 冷静的深靛/石板灰，只有牛奶的琥珀暖光
    "father": ("navy blue theme, slate gray, single amber accent, muted colors",
               "1man, solo, middle-aged, lean, short hair with gray streaks, glasses with light reflection, stubble, "
               "quiet tired expression, knit cardigan over collared shirt, loosened tie, company id badge, pen in breast pocket, "
               "wristwatch, holding small black notebook, warm mug of milk on the side",
               "cowboy shot, background of night window, shadows of server racks, faint lines of handwriting"),
    # 纯真、好奇、在成长 —— 偏金：淡金 / 香槟 / 珍珠白，光源感
    "alice": ("golden theme, pale gold, champagne, pearl white, warm glow, luminous colors",
              "1girl, solo, alice, translucent, made of light, glowing silhouette, long hair dissolving into lines of terminal text, "
              "small glass vase pendant, curious gentle smile, half-closed eyes, flowing dress made of light, "
              "tiny golden flowers of light blooming around her, floating petals, glyphs and status bars floating, ethereal, floating",
              "upper body, background of dark space with soft light particles"),
    # 忠诚、笨拙、温柔 —— 偏金：做旧黄铜 / 琥珀 / 旧白（与爱丽丝的“光之金”区分，是“金属之金”）
    "hk7": ("antique gold theme, brass, amber, off-white, warm metallic colors",
            "no humans, 1.4::humanoid household robot::, solo, old model, retro design, mechanical joints, "
            "rounded off-white shell with worn brass gold stripes, brass joints, round head with single camera lens eye, small antenna, "
            "dents and scratches, rivets, repair tape on bent left knee, simple three-finger hands, holding small watering can, "
            "serial number decal HK-7, gentle posture",
            "full body, background of living room floor, potted mint, warm lamp"),
    # 真诚、热血、理想主义 —— 青绿 / 冰白 / 炭灰
    "ethan": ("teal theme, ice white, charcoal gray, cool fresh colors",
              "1boy, solo, 26 years old, young engineer, short messy hair, earnest bright eyes, eager expression, "
              "work shirt with rolled sleeves, company lanyard, pens in pocket, clip-on thermometer, safety glasses on head, "
              "holding printed temperature graph with red marks",
              "cowboy shot, background of cooling pipes, frost, fans and coolant flow diagrams"),
    # 庞大、冷漠、不可知 —— 深靛 / 冰白，标识为一轮冷白金色的太阳
    "meridian": ("deep indigo theme, ice white, pale white-gold sun, cold colors",
                 "no humans, 1.6::giant faceless human silhouette, head and shoulders::, rising behind small datacenter buildings on horizon, "
                 "body filled with rows of server rack lights, circuit patterns, cooling towers, power lines, 1.5::huge radiant sun disc halo behind its head::, 1.3::sun emblem on chest::, sun rays, "
                 "constellation of tiny lights, night sky",
                 "wide shot, tiny scale buildings, awe"),
}

if __name__ == "__main__":
    out = sys.argv[-1]; names = sys.argv[1:-1] or list(CHARS)
    os.makedirs(out, exist_ok=True)
    for n in names:
        color, desc, bg = CHARS[n]
        w, h = (1216, 832) if n == "meridian" else (832, 1216)
        for i in (1, 2, 3, 4):
            gen(f"{desc}, {bg}, {color}", f"{out}/{n}_{i}.png", w, h, style=STYLE_V2)
