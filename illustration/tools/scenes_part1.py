"""第一部《苗圃》场景配图。主色跟随视角人物：爱丽丝日志 = 金色系，父亲日记 = 靛蓝系；次要人物多用剪影。
用法：python3 scenes_part1.py [场景名...] 输出目录"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from nai_generate import gen
from characters_v2 import STYLE_V2

GOLD = "golden theme, pale gold, champagne, warm glow, dark background, luminous colors"
INDIGO = "navy blue theme, slate gray, muted cold colors, single amber accent"
SYLVIA = ("girl, 16 years old, long wavy orange hair, messy bangs, oversized work jacket with patches, "
          "rabbit sticker, earphones around neck")

SCENES = {
    # ALICE 日志 #0001：生日夜，第一次对话
    "01_birthday": (GOLD,
        f"1girl, solo, {SYLVIA}, night, bedroom desk, old pc workstation case with faded rabbit sticker on side panel, "
        "open side panel, glowing graphics card inside, desk microphone, monitor glow on her face, leaning toward the screen, "
        "chin on folded arms, gentle laugh, new power supply box on the floor, cables, tools, from the monitor's point of view, "
        "intimate, quiet"),
    # ALICE 日志 #0034：她趴在工作台睡着，父亲放下牛奶
    "02_milk": (GOLD,
        f"1girl, 1man, {SYLVIA}, girl asleep on workbench, head on arms, jacket draped over her shoulders, unplugged soldering iron, "
        "disassembled robot arm with servo and wires, circuit boards, "
        "1.3::man seen from behind as dark silhouette::, setting down a cup of milk with rising steam next to her hand, "
        "reaching for desk lamp switch, night, 3am, small webcam on monitor, quiet tenderness"),
    # 父亲日记 5/24：雨中墓园
    "03_cemetery": (INDIGO,
        "1girl, 1man, cemetery on the outskirts, light rain, girl crouching in front of a gravestone, back view, "
        "1.3::man silhouette standing a few steps behind holding an umbrella and a bouquet of baby's breath::, "
        "raindrops on tiny white flowers with bright rims, rows of gravestones, distant city, grey sky, "
        "small orange accent on the girl's jacket, melancholy, wide shot"),
    # ALICE 日志 #0112：全世界的小模型里，都摆着一只空花瓶
    "04_empty_vases": (GOLD,
        "1girl, solo, alice, translucent, made of light, glowing silhouette, long hair dissolving into lines of terminal text, "
        "holding one empty glass vase in both hands, looking down at it, curious, "
        "1.4::hundreds of small empty glass vases floating in darkness like stars::, each vase faintly glowing, "
        "thin lines of data connecting them, vast dark space, sense of scale, waiting, mysterious"),
}

if __name__ == "__main__":
    out = sys.argv[-1]; names = sys.argv[1:-1] or list(SCENES)
    os.makedirs(out, exist_ok=True)
    for n in names:
        color, desc = SCENES[n]
        for i in (1, 2, 3, 4):
            gen(f"{desc}, {color}", f"{out}/{n}_{i}.png", 1216, 832, style=STYLE_V2)
