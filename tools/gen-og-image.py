#!/usr/bin/env python3
"""Generate the 1200x630 Open Graph image for mingw-w64.org.

Pillow-only (no cairosvg/rsvg). Reproduces the site's real branding:
the diamond logo pattern (rotated squares in #999 / #4d4d4d) from
web/logo.svg, on a white ground matching the site's light theme.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
OUT = "web/og-image.png"

# ---- background: white ground (site light theme) ----
img = Image.new("RGB", (W, H), "#ffffff")
d = ImageDraw.Draw(img)

# ---- diamond logo pattern (from web/logo.svg) ----
# logo.svg: 45deg-rotated squares, 32.529 units, colors #999 and #4d4d4d
# arranged in a 3x3-ish grid. We scale it up and tile it in the top-left.
S = 46          # square size (px)
GAP = 0
colors = [
    ["#999", "#4d4d4d", "#999"],
    ["#4d4d4d", "#999", "#4d4d4d"],
    ["#999", "#4d4d4d", "#999"],
]
ox, oy = 70, 70
for r, row in enumerate(colors):
    for c, col in enumerate(row):
        cx = ox + c * (S + GAP)
        cy = oy + r * (S + GAP)
        # draw a 45deg-rotated square centered at (cx, cy)
        half = S / 2 * math.sqrt(2)
        pts = []
        for ang in (45, 135, 225, 315):
            rad = math.radians(ang)
            pts.append((cx + half * math.cos(rad), cy + half * math.sin(rad)))
        d.polygon(pts, fill=col)

# ---- title ----
def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

f_title = font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 96)
f_sub = font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
f_tag = font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 34)

# title on the right of the diamond block
tx = 70 + 3 * S + 60
ty = 120
d.text((tx, ty), "mingw-w64", font=f_title, fill="#1c1b1e")

# subtitle
d.text((tx, ty + 130), "A complete runtime environment", font=f_sub, fill="#4d4d4d")
d.text((tx, ty + 185), "for GCC & LLVM on Windows", font=f_sub, fill="#4d4d4d")

# tagline / URL
d.text((tx, ty + 300), "32-bit (x86)  ·  64-bit (x64)  ·  ARM64", font=f_tag, fill="#999")
d.text((tx, ty + 360), "mingw-w64.org", font=f_tag, fill="#14213d")

img.save(OUT)
print("wrote", OUT, img.size)
