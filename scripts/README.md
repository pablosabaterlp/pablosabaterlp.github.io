# scripts

One-off helpers. Nothing here is loaded by the site.

## QR codes

```
python -m pip install segno
python scripts/make_qr.py
```

Writes `assets/qr/email.svg`, `website.svg` and `linkedin.svg` (dark modules on #ECEAE6, 4-module quiet zone).
Links are read from `js/config.js`; re-run whenever `SITE_URL`, `EMAIL` or `LINKEDIN` changes (e.g. once the custom domain is live).

## Social preview image

```
python scripts/make_og.py
```

Writes `assets/img/og-image.png` (1200×630), used by the Open Graph / Twitter meta tags. Requires Pillow.
