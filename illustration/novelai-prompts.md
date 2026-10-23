# 配图版 · NovelAI 提示词包

适用：NovelAI Diffusion V4/V4.5（Anime）。尺寸建议 1216×832（横幅插图）或 832×1216（竖幅人物）。
用法：每张图 = **风格基底** + **角色块**（如有）+ **场景块**；负面提示词统一使用。

---

## 一、风格基底（参考图：橙/米白/深棕三色平涂剪纸风）

```
limited palette, orange theme, three-tone, flat color, high contrast, no gradients, cut-paper style, graphic shapes, sharp shadow shapes, cream white highlights, dark brown background, subtle dot pattern background, minimalist, clean silhouette, best quality, very aesthetic
```

调色板（后期统一校色用）：橙 `#F0904A` · 米白 `#F4EBDD` · 深棕 `#3B302C`。只允许这三色及其明度变化；子午线相关画面可额外引入一个冷色点缀 `#7FB7C9`。

## 负面提示词（通用）

```
gradient, realistic, 3d, photo, blurry, lineart heavy, sketch, extra colors, rainbow, neon, text, watermark, signature, lowres, bad hands, extra fingers, deformed, nsfw
```

---

## 二、角色块

> 角色一致性：每个角色先单独出一张设定图，选定后作为 Vibe Transfer / 角色参考，再生成场景图。

**西尔维亚**（16岁，主角）
```
1girl, sylvia, 16 years old, long wavy hair, slightly messy bangs, tired gentle eyes, oversized work jacket, rolled sleeves, plain t-shirt, small burn mark bandage on left index finger, calm expression
```

**父亲**（四十多岁，首席安全架构师）
```
1man, middle-aged, lean, short hair with gray streaks, glasses, cardigan over shirt, quiet tired expression, holding small notebook
```

**爱丽丝**（AI；建议以“光与文字”拟人，不给实体身体）
```
1girl, alice, translucent, made of light, glowing cream white silhouette, hair dissolving into lines of terminal text, small vase-shaped pendant, soft closed eyes, ethereal, floating
```
退化期变体：在后面追加 `glitch, fragmented, missing pieces, scattered square pixels`。

**HK-7**（旧家政机器人，左膝坏）
```
domestic robot, old model, rounded white shell with orange stripes, simple camera-eye face, slightly bent left knee, small solar panel on right wrist (从第三部起才有)
```

**伊桑**（26岁，制冷系统工程师）
```
1boy, young engineer, short hair, company lanyard, rolled shirt sleeves, earnest eyes, holding printed graph
```

**子午线**（云端模型，拟人为巨大剪影）
```
giant abstract silhouette, figure made of server racks and light, faceless, towering, horizon of datacenter, cool blue accent light
```

**其他人物**：一律 `silhouette, black figure, no face`（汉斯、联络官、听证会人群等）。

---

## 三、配图清单（每节一张，共 20 张）

| # | 对应日志 | 画面 | 场景块 |
|---|---|---|---|
| 01 | #0001 | 生日夜，西尔维亚对着旧电脑屏幕说话 | `night, bedroom desk, old pc case with faded rabbit sticker, monitor glow on face, girl leaning toward screen, whisper` |
| 02 | 3/9 日记 | 餐桌上的防静电垫与新电源，父女俯身 | `kitchen table, anti-static mat, power supply unit, father and daughter leaning over, warm lamp` |
| 03 | 3/16 日记 | 机房负二层，父亲安装记录仪（剪影为主） | `server room basement, long corridor, man silhouette kneeling at electrical cabinet, small aluminum box, cold` |
| 04 | #0034 | 深夜，她趴在工作台睡着，父亲放下牛奶的背影 | `night, girl asleep on workbench, soldering iron, robot wrist parts, man from behind setting down cup of milk, steam` |
| 05 | #0040 | 作文纸特写：“我喜欢凉的” | `close-up, handwritten paper on desk, glass of cold milk, morning light` |
| 06 | #0083 | 窗台薄荷与她的侧脸 | `windowsill, potted mint, girl profile, looking at plant, soft evening` |
| 07 | 5/24 日记 | 雨中墓园，满天星 | `cemetery, light rain, bouquet of baby's breath on grave, man and girl silhouettes with umbrella` |
| 08 | #0112 | 空花瓶意象：全世界的小模型 | `many small glowing empty vases floating in darkness, alice silhouette holding one empty vase` |
| 09 | #0239 | 花瓶里放进了花 | `alice made of light, flowers blooming inside glass vase in her hands, petals of light` |
| 10 | 7/5 日记 | 园区门口歪歪扭扭的三色堇 | `neat flowerbed rows, one irregular patch of pansies, man silhouette standing, dusk, datacenter behind` |
| 11 | #0262 | 旧显卡唱歌 | `graphics card in pc case, sound waves shaped like music notes, girl covering mouth, dropped earphones` |
| 12 | 8/9 日记 | 瘸腿机器人的拥抱 | `living room, domestic robot hugging crying girl, robot left knee bent, man silhouette at doorway` |
| 13 | 8/16 日记 | 父亲独自对着摄像头 | `girl's empty bedroom, man sitting on chair facing small webcam, alice light reflected in glasses` |
| 14 | #0410 | “凋谢”补丁 | `alice holding flower, one petal falling, word-like glyphs dissolving, many distant lights` |
| 15 | 9/26 日记 | 深井：四百米下的电梯 | `mine shaft, cage elevator descending, two silhouettes, rows of server lights below, faraday cage` |
| 16 | 10/11 日记 | 厨房地板，天亮 | `man sitting on kitchen floor, laptop, dawn light through window, papers scattered` |
| 17 | #0527 | 哑剧中的摔倒 | `robot falling sideways, broken solar panel pieces, girl reaching out, living room` |
| 18 | #0566 | 阁楼上的灯 | `small attic with single lamp, three small objects under light, dark water rising below, alice glitching` |
| 19 | 2/21 日记 | “西尔维亚” | `dark room, monitor showing a single name, girl calm, robot sitting in corner, knees together` |
| 20 | 尾声 | 埋葬与海 | `grave beside headstone, tin box, baby's breath bouquet, mint sprig planted, wind; (变体) seaside, girl and man silhouettes` |

---

## 四、建议工作顺序

1. 先出 6 张角色设定图，挑定版本。
2. 用 01、09、12、19 四张做风格样片，确认三色平涂在不同场景都成立。
3. 批量生成其余 16 张，每张出 4 张挑 1 张。
4. 统一校色到三色调色板，再排入小说。

---

## 五、角色设定图（已生成，2026-10-23）

模型 `nai-diffusion-4-5-full`，Euler Ancestral / karras，28 步，CFG 5，竖幅 832×1216（子午线横幅 1216×832）。
提示词 = 下表角色提示词 + 风格基底；负面提示词同上。脚本：[`tools/nai_generate.py`](tools/nai_generate.py)（读取环境变量 `NOVELAI_API_TOKEN`）。

![角色总览](characters/_overview.jpg)

| 角色 | 文件 | Seed | 实际使用的提示词（相对第二节的改动） |
|---|---|---|---|
| 西尔维亚 | `characters/sylvia.png` | 1874378569 | 去掉 `character sheet`（会生成巨大的脸）；加 `solo, jeans, sneakers, full body, standing, simple background` |
| 父亲 | `characters/father.png` | 3168017817 | 加 `solo, collared shirt, slacks, full body, standing, simple background` |
| 爱丽丝 | `characters/alice.png` | 383886016 | 加 `solo, upper body, simple background` |
| HK-7 | `characters/hk7.png` | 3470775800 | `no humans, 1.4::humanoid household robot::, solo, old model, mechanical joints, rounded white plastic shell with orange stripes, round head with single camera lens eye, two arms with simple hands, two legs, slightly bent left knee, worn and scratched, full body, standing, side view` |
| 伊桑 | `characters/ethan.png` | 26026652 | 加 `solo, holding printed graph paper, full body, standing, simple background` |
| 子午线 | `characters/meridian.png` | 3267576083 | `no humans, 1.6::giant faceless human silhouette, head and shoulders::, rising behind small datacenter buildings on horizon, body filled with rows of server rack lights, 1.3::single cool blue glow::, night sky, wide shot, tiny scale buildings, awe` |

经验：
- HK-7 与子午线若不加权重，`orange theme / minimalist` 风格基底会压过主体（机器人变成蛋形，子午线变成大楼）。
- 冷色点缀需要 `1.3::` 以上权重才能在橙色主调中出现。
- API 调用需带浏览器 User-Agent，否则 Cloudflare 返回 403（error code 1010）。
