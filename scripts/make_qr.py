"""Generate the static contact QR codes in assets/qr/.

Reads SITE_URL, EMAIL and LINKEDIN from js/config.js so links live in one place.
Run from the repo root:  python scripts/make_qr.py
"""
import pathlib
import re

import segno

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = (ROOT / "js" / "config.js").read_text(encoding="utf-8")
OUT = ROOT / "assets" / "qr"

DARK = "#0c0d0f"
LIGHT = "#ECEAE6"


def config_value(key):
    match = re.search(rf'{key}:\s*"([^"]+)"', CONFIG)
    if not match:
        raise SystemExit(f"{key} not found in js/config.js")
    return match.group(1)


codes = {
    "email": "mailto:" + config_value("EMAIL"),
    "website": config_value("SITE_URL"),
    "linkedin": config_value("LINKEDIN"),
}

OUT.mkdir(parents=True, exist_ok=True)
for name, data in codes.items():
    qr = segno.make(data, error="m", micro=False)
    path = OUT / f"{name}.svg"
    qr.save(path, kind="svg", scale=10, border=4, dark=DARK, light=LIGHT,
            xmldecl=False, svgns=True, nl=False, omitsize=True)
    print(f"{path.relative_to(ROOT)}  <-  {data}")
