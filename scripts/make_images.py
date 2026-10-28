"""Convert the source photos in images/ into compressed WebP files in assets/img/.

Photos are cropped to the aspect ratio of the slot they fill on the page, so the
browser never has to crop them. Diagrams and drawings keep their own shape and
are letterboxed on white by the CSS instead. EXIF data (including GPS) is dropped.

Run from the repo root:  python scripts/make_images.py
"""
from pathlib import Path

from PIL import Image, ImageOps

SRC = Path("images")
OUT = Path("assets/img")

# output name: (source file, aspect ratio or None to keep shape, max width, vertical focus 0..1)
IMAGES = {
    "headshot":         ("Headshot.jpg", 4 / 5, 800, 0.5),
    "logo-miele":       ("Miele Logo.webp", 1, 160, 0.5),
    "logo-anthology":   ("Anthology Biotechnologies Logo.jpg", 1, 160, 0.5),
    "miele-sql":        ("Miele SQL Database Design.png", None, 1600, 0.5),
    "anth-gantry":      ("Fluorescence Gantry System- Anthology.jpg", 4 / 3, 900, 0.4),
    "anth-depositing":  ("Microfluidics Depositing Hardware - Anthology.jpg", 4 / 3, 900, 0.6),
    "gait-exploded":    ("GaitKeeper Exploded Drawing.jpg", None, 1200, 0.5),
    "gait-schematic":   ("GaitKeeper Schematic.png", None, 1600, 0.5),
    "gait-topview":     ("GaitKeeper Top View Drawing.jpg", None, 900, 0.5),
    "riscv-fpga":       ("FPGA Board Testing - RISCV.jpg", 16 / 9, 1200, 0.5),
    "riscv-datapath":   ("RISCV Datapath.png", None, 1200, 0.5),
    "ner-car":          ("Me in the car - NER.jpg", 3 / 2, 1200, 0.85),
    "ner-track":        ("IMG_9771.jpg", 1, 800, 0.75),
    "ner-flex-pcb":     ("FlexPCB Manufacturing - NER.jpg", 1, 800, 0.5),
    "ner-hv-front":     ("HV Plate Front.jpg", 1, 800, 0.5),
    "ner-hv-back":      ("HV Plate Back.jpg", 1, 800, 0.5),
}


def crop_to(im, ratio, focus_y):
    w, h = im.size
    if w / h > ratio:
        cw, ch = round(h * ratio), h
    else:
        cw, ch = w, round(w / ratio)
    x = (w - cw) // 2
    y = round((h - ch) * focus_y)
    return im.crop((x, y, x + cw, y + ch))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (src, ratio, max_w, focus_y) in IMAGES.items():
        im = ImageOps.exif_transpose(Image.open(SRC / src))
        im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
        if ratio:
            im = crop_to(im, ratio, focus_y)
        if im.width > max_w:
            im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        dest = OUT / f"{name}.webp"
        im.save(dest, "WEBP", quality=80, method=6)
        print(f"{dest}  {im.width}x{im.height}  {dest.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
