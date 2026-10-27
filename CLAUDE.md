# Pablo Sabater — portfolio site

Personal portfolio for job interviews and recruiters. The design below was iterated and approved in a separate design conversation. Build it as specified; don't redesign. Ask before making visual changes that aren't requested.

## Project basics

- Owner: Pablo Sabater, ECE Honors student at Northeastern (graduating May 2027). Works on Windows in VS Code and previews with the Live Server extension.
- Repo: `pablosabaterlp.github.io`, deployed with GitHub Pages from `main`, folder `/` (root). Live at https://pablosabaterlp.github.io until a custom domain is added.
- Custom domain: not bought yet. Use `pablosabater.com` as a placeholder, defined in ONE place (a constant in `js/config.js`) so it's easy to change. When the domain is final, add a `CNAME` file and regenerate the website QR code.
- The repo is PUBLIC. Never commit private files. The resume source lives in `private/` (gitignored). Don't publish the phone number unless Pablo asks.
- Don't push to GitHub without Pablo's go-ahead. Make small, clearly described commits.

## Tech

- Plain HTML, CSS, and vanilla JavaScript. No frameworks, no build step, no npm dependencies for the site itself. It must work as-is through Live Server and on GitHub Pages.
- Suggested structure:

```
index.html
css/styles.css
js/config.js        site URL, email, LinkedIn, GitHub
js/i18n.js          English and Spanish strings (JS object, not fetched JSON)
js/main.js          language toggle, progress bar, active nav, mobile menu, QR switcher
assets/img/         photos (WebP, compressed), logos, headshot
assets/qr/          static QR SVGs
assets/Pablo-Sabater-Resume.pdf   download button target (public version, no phone number)
private/            gitignored; resume source and notes
scripts/            one-off helpers (e.g. QR generation), not loaded by the site
```

## Visual design (approved)

Dark theme only.

| Token | Hex | Use |
|---|---|---|
| bg | #0c0d0f | page background |
| surface | #15171a | cards, fact tiles |
| border | #262a2f | hairlines |
| text | #ECEAE6 | primary text |
| muted | #8D9199 | secondary text, labels |
| accent (azafrán) | #EBA43A | primary accent: badges, buttons, links, active states, highlighted tiles |
| red | #E0473C | sparing secondary highlights only |
| on-accent | #2a1a03 | text on azafrán buttons |

- Red is used only for: section numbers (01–06), the tip of the progress bar, the availability dot, the red dot in the logo, and key metrics inside bullets (e.g. "100+ hrs", "1%", "168-hr", "provisionally patented").
- No Spanish flag stripe (it was tried and removed).
- Fonts: IBM Plex Sans (body and headings) and IBM Plex Mono (small labels, dates, tags, coordinates), from Google Fonts with system fallbacks.
- Rounded corners: ~10–12px cards, ~6–8px buttons and tiles, pills for badges.

## Global elements

- Scroll progress bar: fixed at the very top, 3px tall. Azafrán fill that grows with scroll position, with a 6px red tip at the leading edge. Track is the border color.
- Desktop nav: left "pablo.sabater" (the dot is red); center numbered links `01 What I can do` through `06 Contact` (numbers red, labels muted); right an EN / ES pill. The current section's label turns primary color with an azafrán underline (IntersectionObserver).
- Mobile nav: hamburger menu on the left, the current section number and name in the center (e.g. "02 Experience"), EN/ES on the right.

## Page structure

### Hero

- Availability badge (azafrán outline pill, red dot): "Available July 2027 · Full-time".
- Name: Pablo Sabater (large).
- Pitch: "Electrical and computer engineer building high-voltage power electronics, embedded systems, and the PCBs that tie them together." (Pablo may reword.)
- Facts grid, 3 columns by 2 rows on desktop: Based in (Cambridge, MA) · From (Spain) · Focus (Power · Embedded · PCB) · Education (Northeastern ECE, Honors) · Graduating (May 2027) · Work authorization (highlighted with an azafrán border and label).
- Buttons: View experience ↓ (azafrán filled), Résumé (PDF download), and icon buttons for LinkedIn, GitHub, and email.
- Desktop: headshot on the right in a rounded rectangle with a 1px azafrán border. Directly UNDER the headshot, in mono muted text: "Cambridge, MA / 42.37°N 71.08°W / → from Spain" (arrow red).
- Mobile: circular headshot at the top, then badge, name, short pitch, and a 2-column facts grid reduced to Based in, From, and Work authorization (spanning both columns). NO coordinates on mobile.

### Sections (in this order)

| # | Nav label | Heading |
|---|---|---|
| 01 | What I can do | What I can do |
| 02 | Experience | Where I've contributed |
| 03 | Projects | What I build on my own time |
| 04 | Leadership | Head of Electrical Powertrain |
| 05 | Education | Northeastern University |
| 06 | Contact | Let's build something |

Each section starts with a small mono label like "01 / What I can do" (number in red), then the heading.

**01 What I can do**: A quick-scan overview for someone skimming. A compact grid of capability groups (Hardware, Software, Systems, Design), each with short tag chips taken from the resume skills. Keep it short; this is the 10-second summary, not an exhaustive list.

**02 Where I've contributed**: One card per role, showing logo, title, company, dates, location, 3–4 bullets (key metrics in red), a photo strip, and tech tags.
- Miele Technologies: R&D Electrical and Computer Engineer Co-op, Peabody, MA, 07/2026–present.
- Anthology Biotechnologies: Microfluidics Hardware Co-op, Cambridge, MA, 06/2025–12/2025.
- Desktop shows 2 columns; mobile shows a single column.

**03 What I build on my own time**: Project cards with a cover image, "PRJ / 01" label, status (Active in azafrán / Shipped in muted), title, a one-line description, and tags. Each card expands to show full detail and more photos.
- PRJ / 01 Gait Keeper: smart insole with real-time gait analysis (velostat/flex PCB array, ESP32, IMU over I2C, USB-C charging, Altium semi-rigid flex). Active, 05/2026–present.
- PRJ / 02 Single-cycle RISC-V CPU: SystemVerilog on a PYNQ FPGA in Vivado. Shipped, 01/2026–05/2026.
- More projects will be added later.

**04 Head of Electrical Powertrain**: Northeastern Electric Racing, 01/2024–present.
- Three stat tiles with azafrán numbers: "3+" PCBs brought up, "20+" design reviews led, "~20%" BMS reliability gain.
- Bullets: owning accumulator electrical design and pack sizing via MATLAB simulations of past competition data; leading the flex-PCB voltage/temperature sensing project and the BMS redesign; redesigned precharge/discharge from analog to digital around the ADBMS2950B.
- Photo collage: one wide image (car or accumulator) plus two smaller ones (PCB, team).

**05 Northeastern University**:
- BS Electrical and Computer Engineering, Honors Program. Boston, MA. Expected May 2027. GPA 3.75 (in azafrán).
- Honors chips (azafrán outline): Honors Scholarship, Dean's List ×5 (the ×5 in red), Honors Impact Badge, IEEE-Eta Kappa Nu.
- Selected coursework as tags; groups: Northeastern Electric Racing, Energy Efficient Circuits and Systems, IEEE-Eta Kappa Nu.

**06 Let's build something**:
- A "What I'm looking for" card with an azafrán border. The text is a placeholder for Pablo to write. Pablo may title this card "What I hope to contribute to"; ask him.
- Desktop: three QR tiles side by side (Email, Website, LinkedIn). Each tile is clickable and opens its link, shows the address underneath, and has its own full-width azafrán button ("Send email", "Open site", "Open LinkedIn").
- Mobile (important: Pablo shows this screen on his phone so people can scan it): a segmented control (Email | Website | LinkedIn) above ONE large QR code that fills most of the screen width on a light background, the address under it, then a full-width button that opens the same link. Swiping left and right also switches codes, with dot indicators below.
- `#contact` must work as a direct link that opens straight onto this section, so Pablo can save it to his phone's home screen.
- Footer: "© 2027 Pablo Sabater" with a red dot and Cambridge, MA.

## Bilingual (EN/ES)

- English by default. The toggle swaps all visible text using `data-i18n` keys and dictionaries in `js/i18n.js`.
- Remember the visitor's choice in localStorage (wrapped in try/catch). Update `<html lang>` and the page title when switching.
- Pablo is a native Spanish speaker and will refine the Spanish wording himself, so keep the strings easy to find and edit.

## QR codes

- Generate static SVGs into `assets/qr/` with a small script in `scripts/` (e.g. Python `segno`), run once and re-run when links change. Document the command in `scripts/README.md`.
- Email encodes `mailto:psabater05@icloud.com`. LinkedIn encodes `https://www.linkedin.com/in/pablosabaterlp/`. Website encodes the placeholder domain until it's final.
- Use dark modules on a light (#ECEAE6) background with a quiet zone, so phones can scan them from a dark screen.

## Work authorization wording (use exactly)

- Fact tile: "OPT + STEM OPT · no sponsorship"
- Fuller statement (contact or education section): "Eligible for up to 3 years of U.S. work authorization through F-1 OPT and the STEM OPT extension. No visa sponsorship required during this period."
- Pablo is confirming the final wording with Northeastern's Office of Global Services, so keep it in one easily editable string.

## Links

- Email: psabater05@icloud.com
- LinkedIn: https://www.linkedin.com/in/pablosabaterlp/
- GitHub: https://github.com/pablosabaterlp

## Images

- Until Pablo provides photos, use dashed-border placeholder boxes with a small "photo" label at the final aspect ratio.
- When photos arrive: convert to WebP, resize (max ~1600px wide, cover images smaller), write descriptive alt text, and use `loading="lazy"` below the hero.

## Quality floor

- Responsive from 360px phones to wide desktops. Test both layouts in Live Server and with the browser's device toolbar.
- Visible keyboard focus states, semantic headings, and alt text on every image.
- Respect `prefers-reduced-motion`. Keep motion minimal: the progress bar and expanding project cards, nothing decorative.
- Open Graph and Twitter meta tags plus a preview image, so shared links look good. Add a favicon.
- No layout shift from images (set width and height or aspect-ratio).
