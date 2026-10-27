"""Generate assets/img/og-image.png (1200x630 social preview) and apple-touch-icon.png.

Run from the repo root:  python scripts/make_og.py
Uses Windows system fonts as a stand-in for IBM Plex; swap the paths if needed.
"""
import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
FONTS = pathlib.Path("C:/Windows/Fonts")

BG, SURFACE, BORDER = "#0c0d0f", "#15171a", "#262a2f"
TEXT, MUTED, ACCENT, RED = "#ECEAE6", "#8D9199", "#EBA43A", "#E0473C"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def og_image():
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 6], fill=BORDER)
    d.rectangle([0, 0, 780, 6], fill=ACCENT)
    d.rectangle([774, 0, 780, 6], fill=RED)

    mono = font("consola.ttf", 26)
    d.text((80, 90), "pablo", font=mono, fill=TEXT)
    w = d.textlength("pablo", font=mono)
    d.text((80 + w, 90), ".", font=mono, fill=RED)
    d.text((80 + w + d.textlength(".", font=mono), 90), "sabater", font=mono, fill=TEXT)

    d.text((76, 190), "Pablo Sabater", font=font("segoeuib.ttf", 104), fill=TEXT)
    body = font("segoeui.ttf", 36)
    d.text((80, 340), "Electrical & computer engineer: high-voltage power", font=body, fill=MUTED)
    d.text((80, 388), "electronics, embedded systems, and PCBs.", font=body, fill=MUTED)

    badge = "Available July 2027 · Full-time"
    small = font("consola.ttf", 26)
    bw = d.textlength(badge, font=small)
    d.rounded_rectangle([80, 490, 80 + bw + 76, 548], radius=29, outline=ACCENT, width=2)
    d.ellipse([104, 513, 116, 525], fill=RED)
    d.text((132, 503), badge, font=small, fill=ACCENT)
    img.save(OUT / "og-image.png", optimize=True)


def touch_icon():
    img = Image.new("RGB", (180, 180), BG)
    d = ImageDraw.Draw(img)
    d.text((38, 18), "p", font=font("consolab.ttf", 120), fill=ACCENT)
    d.ellipse([118, 108, 146, 136], fill=RED)
    img.save(OUT / "apple-touch-icon.png", optimize=True)


OUT.mkdir(parents=True, exist_ok=True)
og_image()
touch_icon()
print("wrote assets/img/og-image.png and assets/img/apple-touch-icon.png")
