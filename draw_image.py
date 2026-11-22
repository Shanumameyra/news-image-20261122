# draw_image.py — draws the news-image-20261122 entry: a one-page front page
# summing up the world news of Sunday 22 November 2026.
# Original work, drawn with PIL from the news research in NOTES.md.
# Output: entry.png, 1024x1024, flat infographic style, legible at small sizes.

import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (16, 35, 63)
PAPER = (246, 241, 231)
CARD = (255, 255, 255)
INK = (16, 35, 63)
GREY = (71, 84, 103)
GOLD = (201, 162, 39)
BORDER = (217, 210, 192)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def fit_lines(draw, text, max_w, max_lines, start_size, min_size, path=FONT_B):
    """Largest font size (<= start_size, >= min_size) whose wrap fits max_lines."""
    for size in range(start_size, min_size - 1, -1):
        fnt = font(path, size)
        lines = wrap(draw, text, fnt, max_w)
        if len(lines) <= max_lines:
            return fnt, lines
    fnt = font(path, min_size)
    return fnt, wrap(draw, text, fnt, max_w)

def glyph(draw, kind, cx, cy, r, color):
    """Draw a small white glyph centred at (cx, cy) with radius r."""
    u = r  # unit
    if kind == "flame":
        pts = [(-0.05, -0.62), (0.30, -0.28), (0.48, 0.08), (0.34, 0.52),
               (0.0, 0.62), (-0.34, 0.52), (-0.48, 0.08), (-0.28, -0.30)]
        draw.polygon([(cx + x * u, cy + y * u) for x, y in pts], fill=color)
    elif kind == "star":
        pts = []
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            rr = 0.62 * u if i % 2 == 0 else 0.28 * u
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=color)
    elif kind == "globe":
        draw.ellipse([cx - 0.55 * u, cy - 0.55 * u, cx + 0.55 * u, cy + 0.55 * u],
                     outline=color, width=4)
        draw.line([cx - 0.52 * u, cy, cx + 0.52 * u, cy], fill=color, width=3)
        draw.line([cx, cy - 0.55 * u, cx, cy + 0.55 * u], fill=color, width=3)
    elif kind == "chart":
        pts = [(-0.55, -0.30), (-0.28, -0.02), (-0.02, -0.25), (0.22, 0.05), (0.48, 0.38)]
        xy = [(cx + x * u, cy + y * u) for x, y in pts]
        draw.line(xy, fill=color, width=5, joint="curve")
        ex, ey = cx + 0.48 * u, cy + 0.38 * u
        draw.polygon([(ex, ey), (ex - 0.22 * u, ey), (ex, ey - 0.22 * u)], fill=color)
    elif kind == "keyhole":
        draw.ellipse([cx - 0.24 * u, cy - 0.42 * u, cx + 0.24 * u, cy + 0.06 * u], fill=color)
        draw.polygon([(cx - 0.14 * u, cy - 0.02 * u), (cx + 0.14 * u, cy - 0.02 * u),
                      (cx + 0.07 * u, cy + 0.55 * u), (cx - 0.07 * u, cy + 0.55 * u)], fill=color)
    elif kind == "burst":
        pts = []
        for i in range(16):
            ang = -math.pi / 2 + i * math.pi / 8
            rr = 0.62 * u if i % 2 == 0 else 0.26 * u
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=color)
    elif kind == "scales":
        draw.line([cx, cy - 0.5 * u, cx, cy + 0.5 * u], fill=color, width=4)
        draw.line([cx - 0.5 * u, cy - 0.38 * u, cx + 0.5 * u, cy - 0.38 * u], fill=color, width=4)
        for sx in (-0.42, 0.42):
            draw.line([cx + sx * u, cy - 0.38 * u, cx + sx * u, cy - 0.05 * u], fill=color, width=3)
            draw.polygon([(cx + (sx - 0.16) * u, cy - 0.05 * u), (cx + (sx + 0.16) * u, cy - 0.05 * u),
                          (cx + sx * u, cy + 0.28 * u)], fill=color)
        draw.line([cx - 0.3 * u, cy + 0.55 * u, cx + 0.3 * u, cy + 0.55 * u], fill=color, width=4)
    elif kind == "boat":
        draw.polygon([(cx - 0.55 * u, cy - 0.05 * u), (cx + 0.55 * u, cy - 0.05 * u),
                      (cx + 0.38 * u, cy + 0.42 * u), (cx - 0.38 * u, cy + 0.42 * u)], fill=color)
        draw.line([cx, cy - 0.05 * u, cx, cy - 0.58 * u], fill=color, width=4)
        draw.polygon([(cx, cy - 0.58 * u), (cx, cy - 0.08 * u), (cx + 0.38 * u, cy - 0.08 * u)],
                     fill=color)
    elif kind == "flag":
        draw.line([cx - 0.32 * u, cy - 0.58 * u, cx - 0.32 * u, cy + 0.58 * u], fill=color, width=4)
        draw.polygon([(cx - 0.32 * u, cy - 0.58 * u), (cx + 0.5 * u, cy - 0.58 * u),
                      (cx + 0.32 * u, cy - 0.32 * u), (cx + 0.5 * u, cy - 0.06 * u),
                      (cx - 0.32 * u, cy - 0.06 * u)], fill=color)
    elif kind == "drop":
        draw.ellipse([cx - 0.42 * u, cy - 0.12 * u, cx + 0.42 * u, cy + 0.58 * u], fill=color)
        draw.polygon([(cx - 0.42 * u, cy - 0.08 * u), (cx + 0.42 * u, cy - 0.08 * u),
                      (cx, cy - 0.62 * u)], fill=color)

# --- stories: (tag, colour, glyph, headline, sub) ---
# Headlines kept short so each fits 2 lines; subs fit 2 lines in the tile.
STORIES = [
    ("MIDDLE EAST", (180, 35, 24), "drop",
     "Iran strikes Bahrain as tankers are hit in the Strait of Hormuz",
     "Bahrain says a civilian site was struck; two tankers hit near the strait."),
    ("MEXICO", (53, 56, 205), "star",
     "Mexico captures 'El Chapo Isidro'",
     "Cartel boss held; 11 killed in the raid."),
    ("CLIMATE", (6, 118, 71), "globe",
     "COP31 deadlocked over fossil fuels",
     "Climate summit in Antalya runs into overtime."),
    ("MARKETS", (181, 71, 8), "chart",
     "AI sell-off pushes US stocks into correction",
     "S&P 500 falls 3.7%; Japan's Nikkei drops 5.1%."),
    ("CYBER", (105, 65, 198), "keyhole",
     "FBI crime database hacked",
     "FBI probes a breach of its national records."),
    ("UKRAINE", (23, 92, 211), "burst",
     "Russia hits Zelenskyy's hometown",
     "Kryvyi Rih strike kills 2, wounds dozens."),
    ("WORLD COURT", (14, 116, 144), "scales",
     "UN court: Myanmar committed genocide",
     "Judges rule on the Rohingya; sanctions urged."),
    ("NIGERIA", (71, 84, 103), "boat",
     "Nigeria boat capsizes; 24 dead",
     "Boat carrying mourners sinks in the south."),
    ("INDONESIA", (196, 50, 10), "flame",
     "Indonesia factory fire; 36 missing",
     "Candy plant blaze in Banten kills 3."),
    ("SOUTH KOREA", (192, 16, 72), "flag",
     "South Korea education minister resigns",
     "He quits over an exam-cheating scandal."),
]

LEAD = STORIES[0]
GRID = STORIES[1:]

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# --- header band ---
d.rectangle([0, 0, W, 120], fill=NAVY)
d.rectangle([0, 120, W, 124], fill=GOLD)
title_f = font(FONT_B, 68)
d.text((24, 24), "WORLD NEWS", font=title_f, fill=(255, 255, 255))
date_f1 = font(FONT_B, 32)
date_f2 = font(FONT_B, 28)
d.text((W - 24 - d.textlength("SUNDAY", font=date_f1), 20), "SUNDAY", font=date_f1, fill=(255, 255, 255))
d.text((W - 24 - d.textlength("22 NOVEMBER 2026", font=date_f2), 60), "22 NOVEMBER 2026",
       font=date_f2, fill=(255, 255, 255))

# --- lead card ---
LX, LY, LW, LH = 24, 136, 976, 186
d.rounded_rectangle([LX, LY, LX + LW, LY + LH], radius=14, fill=CARD, outline=BORDER, width=2)
tag_f = font(FONT_B, 21)
tag_txt = "LEAD STORY"
tw = d.textlength(tag_txt, font=tag_f)
d.rounded_rectangle([LX + 18, LY + 14, LX + 18 + tw + 24, LY + 14 + 34], radius=8, fill=LEAD[1])
d.text((LX + 30, LY + 19), tag_txt, font=tag_f, fill=(255, 255, 255))
hl_f, hl_lines = fit_lines(d, LEAD[3], LW - 36, 2, 40, 30)
y = LY + 54
for ln in hl_lines:
    d.text((LX + 18, y), ln, font=hl_f, fill=INK)
    y += hl_f.size + 6
sub_f, sub_lines = fit_lines(d, LEAD[4], LW - 36, 2, 26, 22, FONT_R)
for ln in sub_lines:
    d.text((LX + 18, y), ln, font=sub_f, fill=GREY)
    y += sub_f.size + 5
assert y <= LY + LH - 6, f"lead overflow: {y} > {LY + LH - 6}"

# --- grid 3x3 ---
GX, GY = 24, 334
GW, GH, GAP = 317, 192, 12
for i, (tag, col, gk, head, sub) in enumerate(GRID):
    r, c = divmod(i, 3)
    x = GX + c * (GW + GAP)
    y = GY + r * (GH + GAP)
    d.rounded_rectangle([x, y, x + GW, y + GH], radius=14, fill=CARD, outline=BORDER, width=2)
    icx, icy, ir = x + 16 + 21, y + 14 + 21, 21
    d.ellipse([icx - ir, icy - ir, icx + ir, icy + ir], fill=col)
    glyph(d, gk, icx, icy, 15, (255, 255, 255))
    tg_f = font(FONT_B, 20)
    d.text((x + 16 + 52, y + 14 + 9), tag, font=tg_f, fill=col)
    hf, hl = fit_lines(d, head, GW - 32, 2, 28, 22)
    assert len(hl) <= 2, f"tile {tag}: headline {len(hl)} lines: {hl}"
    yy = y + 14 + 50
    for ln in hl:
        d.text((x + 16, yy), ln, font=hf, fill=INK)
        yy += hf.size + 4
    sf, sl = fit_lines(d, sub, GW - 32, 2, 21, 18, FONT_R)
    assert len(sl) <= 2, f"tile {tag}: sub {len(sl)} lines: {sl}"
    yy += 4
    for ln in sl:
        d.text((x + 16, yy), ln, font=sf, fill=GREY)
        yy += sf.size + 4
    assert yy <= y + GH - 8, f"tile {tag}: content bottom {yy} > {y + GH - 8}"

# --- footer band ---
d.rectangle([0, 946, W, 1000], fill=NAVY)
ft_f = font(FONT_B, 20)
ft = "SUNDAY 22 NOVEMBER 2026  •  THE DAY'S MOST CONSEQUENTIAL STORIES"
fw = d.textlength(ft, font=ft_f)
assert fw <= W - 24, f"footer too wide: {fw}"
d.text(((W - fw) / 2, 946 + 16), ft, font=ft_f, fill=(255, 255, 255))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
print("all layout assertions passed")
