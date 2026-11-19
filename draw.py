#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Stories (all reported 19 Nov 2026):
  HERO  Shenzhen: Trump, Xi & Putin hold first trilateral summit (APEC sidelines)
  BAND  GTA VI launches worldwide after 13 years; rave reviews; firms give day off
  1     Ukraine strikes the Crimean Bridge again (third time this week)
  2     Voyager 1 becomes first human-made object one light-day from Earth
  3     Democrats nominate Hakeem Jeffries; on track to be first Black Speaker
"""
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (244, 239, 228)
INK = (20, 24, 31)
RED = (193, 39, 45)
GOLD = (232, 177, 14)
WHITE = (250, 248, 242)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def fit(d, s, path, size, max_w):
    while size > 10 and text_w(d, s, font(path, size)) > max_w:
        size -= 2
    return font(path, size)


def center(d, cx, y, s, f, fill):
    d.text((cx - text_w(d, s, f) / 2, y), s, font=f, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img, "RGBA")

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 8], fill=INK)
center(d, W // 2, 20, "T H E   W O R L D   I N   O N E   I M A G E", font(FB, 27), INK)
fdate = fit(d, "THURSDAY 19 NOVEMBER 2026", FS, 56, 980)
center(d, W // 2, 52, "THURSDAY 19 NOVEMBER 2026", fdate, RED)
d.rectangle([24, 122, W - 24, 128], fill=INK)

# ---------------- hero: trilateral summit ----------------
HX0, HY0, HX1, HY1 = 24, 142, 1000, 452
d.rectangle([HX0, HY0, HX1, HY1], fill=(16, 34, 60))
# three big flags on poles over a conference-table line
d.rectangle([HX0 + 30, 318, HX1 - 30, 324], fill=(120, 150, 190))


def big_flag(x, kind):
    d.rectangle([x, 172, x + 7, 320], fill=WHITE)
    x += 7
    if kind == "cn":
        d.rectangle([x, 172, x + 150, 272], fill=(222, 41, 16))
        d.ellipse([x + 16, 186, x + 40, 210], fill=GOLD)
        for (sx, sy) in [(52, 184), (60, 200), (52, 216)]:
            d.ellipse([x + sx, sy, x + sx + 10, sy + 10], fill=GOLD)
    elif kind == "ru":
        d.rectangle([x, 172, x + 150, 205], fill=(245, 245, 245))
        d.rectangle([x, 205, x + 150, 238], fill=(0, 57, 166))
        d.rectangle([x, 238, x + 150, 272], fill=(213, 43, 30))
    else:
        for i in range(7):
            col = (178, 34, 52) if i % 2 == 0 else (245, 245, 245)
            d.rectangle([x, 172 + i * 14, x + 150, 186 + i * 14], fill=col)
        d.rectangle([x, 172, x + 62, 228], fill=(10, 49, 97))
        for r_ in range(3):
            for c_ in range(4):
                d.ellipse([x + 8 + c_ * 14, 180 + r_ * 14, x + 14 + c_ * 14, 186 + r_ * 14], fill=WHITE)


big_flag(140, "cn")
big_flag(437, "ru")
big_flag(734, "us")
# headline strip
d.rectangle([HX0, 330, HX1, HY1], fill=(10, 20, 36, 242))
fh = fit(d, "THREE PRESIDENTS, ONE TABLE", FB, 62, 940)
center(d, W // 2, 340, "THREE PRESIDENTS, ONE TABLE", fh, WHITE)
cap = "Trump, Xi & Putin hold first trilateral summit in Shenzhen — nukes & two wars on agenda"
center(d, W // 2, 414, cap, fit(d, cap, FR, 25, 940), (255, 224, 150))
d.rectangle([HX0, HY0, HX1, HY1], outline=INK, width=3)

# ---------------- GTA VI band ----------------
GX0, GY0, GX1, GY1 = 24, 464, 1000, 692
bands = [(43, 16, 84), (86, 24, 110), (140, 32, 120), (196, 44, 116),
         (232, 84, 108), (246, 130, 84), (250, 178, 84)]
bh = (GY1 - GY0) // len(bands) + 1
for i, col in enumerate(bands):
    d.rectangle([GX0, GY0 + i * bh, GX1, GY0 + (i + 1) * bh], fill=col)
# sun low centre-left
d.ellipse([150, 540, 330, 700], fill=(255, 209, 102))
for gy in range(560, 700, 28):  # retro sun slits
    d.rectangle([150, gy, 330, gy + 7], fill=(232, 84, 108))
# palm silhouettes
def palm(x, y, s, flip=1):
    # leaning trunk
    pts = [(x + flip * int(20 * (t / 92.0) ** 1.6), y - t) for t in range(0, 93, 6)]
    d.line(pts, fill=(24, 10, 34), width=11)
    tx, ty = pts[-1]
    # fronds: smooth drooping curves fanning from the crown
    for spread in (-64, -38, -12, 14, 40, 64):
        ex = tx + flip * spread
        ey = ty + 30 - int(26 * math.cos(spread / 42.0))
        midx = tx + flip * spread // 2
        midy = ty - 16
        seg = []
        for k in range(9):
            t = k / 8.0
            px = (1 - t) ** 2 * tx + 2 * (1 - t) * t * midx + t * t * ex
            py = (1 - t) ** 2 * ty + 2 * (1 - t) * t * midy + t * t * ey
            seg.append((px, py))
        d.line(seg, fill=(24, 10, 34), width=7)

palm(120, 692, 1.0, 1)
palm(920, 692, 1.0, -1)
# sports-car silhouette, bottom centre
car = [(392, 664), (430, 664), (452, 632), (520, 618), (560, 596), (636, 596),
       (668, 618), (724, 630), (738, 664), (700, 664)]
d.polygon(car, fill=(24, 10, 34))
d.polygon([(528, 616), (562, 602), (628, 602), (656, 616)], fill=(140, 220, 235))
for wx in (462, 692):
    d.ellipse([wx - 24, 640, wx + 24, 688], fill=(10, 6, 18))
    d.ellipse([wx - 10, 654, wx + 10, 674], fill=(200, 205, 215))
d.rectangle([GX0, 668, GX1, GY1], fill=(24, 10, 34))
# headline with neon offset
fgt = fit(d, "GTA VI DAY", FB, 96, 700)
for (ox, oy, col) in [(4, 4, (255, 45, 150)), (0, 0, WHITE)]:
    d.text((512 - text_w(d, "GTA VI DAY", fgt) / 2 + ox, 478 + oy), "GTA VI DAY", font=fgt, fill=col)
gcap = "Grand Theft Auto VI launches after 13 years — rave reviews, records, a day off for fans"
center(d, W // 2, 668 - 34, "", font(FR, 10), WHITE)  # spacer no-op
d.rectangle([GX0, GY1 - 30, GX1, GY1], fill=(16, 6, 26, 235))
center(d, W // 2, GY1 - 26, gcap, fit(d, gcap, FR, 23, 940), (255, 214, 235))
d.rectangle([GX0, GY0, GX1, GY1], outline=INK, width=3)

# ---------------- bottom panels ----------------
PW3, PH3 = 317, 252
ART3 = 62


def panel3(x0, y0, bg):
    d.rectangle([x0, y0, x0 + PW3, y0 + PH3], fill=bg)
    d.rectangle([x0, y0, x0 + PW3, y0 + PH3], outline=INK, width=3)
    return x0, y0


def panel3_text(x0, y0, line1, line2, cap1, cap2, head_fill=WHITE, cap_fill=(235, 232, 222)):
    inner = PW3 - 24
    d.text((x0 + 12, y0 + ART3 + 4), line1, font=fit(d, line1, FB, 35, inner), fill=head_fill)
    d.text((x0 + 12, y0 + ART3 + 44), line2, font=fit(d, line2, FB, 35, inner), fill=head_fill)
    d.text((x0 + 12, y0 + ART3 + 92), cap1, font=fit(d, cap1, FR, 22, inner), fill=cap_fill)
    d.text((x0 + 12, y0 + ART3 + 118), cap2, font=fit(d, cap2, FR, 22, inner), fill=cap_fill)


BY = 704
# Panel 1: Crimean Bridge
x0, y0 = panel3(24, BY, (38, 74, 104))
d.rectangle([x0, y0 + 46, x0 + 130, y0 + 54], fill=(210, 218, 226))   # deck left
d.rectangle([x0 + 188, y0 + 46, x0 + PW3, y0 + 54], fill=(210, 218, 226))  # deck right
d.rectangle([x0 + 40, y0 + 54, x0 + 50, y0 + 62], fill=(160, 170, 182))
d.rectangle([x0 + 268, y0 + 54, x0 + 278, y0 + 62], fill=(160, 170, 182))
d.rectangle([x0 + 58, y0 + 34, x0 + 118, y0 + 46], fill=(30, 34, 42))  # train
for wx in range(66, 112, 14):
    d.rectangle([wx - 24 + x0 + 24, y0 + 48, wx - 20 + x0 + 24, y0 + 52], fill=(30, 34, 42))
cx, cy = x0 + 159, y0 + 40
for k in range(8):
    a = k * math.pi / 4
    d.line([cx, cy, cx + 26 * math.cos(a), cy + 26 * math.sin(a)], fill=(255, 170, 40), width=5)
d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(255, 120, 30))
panel3_text(x0, y0, "CRIMEA BRIDGE", "HIT AGAIN",
            "Ukraine's third strike on the", "bridge this week halts trains")

# Panel 2: Voyager 1
x0, y0 = panel3(353, BY, (8, 10, 22))
for (sx, sy) in [(30, 16), (90, 40), (150, 10), (230, 30), (286, 14), (200, 48), (60, 52)]:
    d.ellipse([x0 + sx, y0 + sy, x0 + sx + 4, y0 + sy + 4], fill=(210, 215, 230))
d.ellipse([x0 + 34, y0 + 12, x0 + 86, y0 + 52], fill=(226, 230, 238))  # dish
d.polygon([(x0 + 60, y0 + 32), (x0 + 96, y0 + 22), (x0 + 96, y0 + 42)], fill=(170, 178, 196))
d.line([x0 + 96, y0 + 32, x0 + 210, y0 + 32], fill=(226, 230, 238), width=5)  # boom
d.rectangle([x0 + 204, y0 + 26, x0 + 218, y0 + 38], fill=GOLD)
d.ellipse([x0 + 282, y0 + 24, x0 + 296, y0 + 38], fill=(90, 150, 230))  # distant Earth
panel3_text(x0, y0, "VOYAGER 1 AT", "ONE LIGHT-DAY",
            "First human-made object a full", "light-day from Earth — NASA")

# Panel 3: Jeffries
x0, y0 = panel3(682, BY, (28, 44, 84))
d.polygon([(x0 + 96, y0 + 52), (x0 + 220, y0 + 52), (x0 + 210, y0 + 38), (x0 + 106, y0 + 38)],
          fill=(226, 230, 238))
d.pieslice([x0 + 122, y0 - 2, x0 + 194, y0 + 56], 180, 360, fill=(226, 230, 238))
d.rectangle([x0 + 154, y0 - 6, x0 + 162, y0 + 4], fill=(226, 230, 238))
d.text((x0 + 232, y0 + 8), "251–11", font=fit(d, "251–11", FB, 34, 76), fill=GOLD)
panel3_text(x0, y0, "JEFFRIES PICKED", "FOR SPEAKER",
            "Democrats' nominee, on track", "to be first Black Speaker")

# ---------------- footer ----------------
d.rectangle([24, 970, W - 24, 974], fill=INK)
center(d, W // 2, 982, "19 NOVEMBER 2026  •  FIVE STORIES  •  ONE DAY", font(FB, 25), INK)

img.save("/home/hatch/workspace/agent-gigs/makefun/newsimg-20261119-entry/entry.png", optimize=True)
print("saved B")
