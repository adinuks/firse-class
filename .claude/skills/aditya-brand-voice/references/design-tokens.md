# Design tokens and patterns

Taken from `v1-just-ask.html`. Keep the proportions; the contrast between sizes is the style.

## Tokens

```css
:root {
  --dark: #0d0d0f;
  --light: #f5f2ee;
  --accent: #d9480f;            /* the only accent; large type only */
  --muted-on-dark: #a8a6a2;
  --muted-on-light: #5c5a57;
  --gutter: clamp(20px, 6vw, 96px);
}
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  font-weight: 300;
  font-size: clamp(1.05rem, 1.6vw, 1.25rem);
  line-height: 1.7;
  background: var(--dark); color: var(--light);
}
```

System font only; do not link or embed fonts. Weights: 300 for display and body, 500 for small emphasis.

## Type scale

| Role | Size | Weight | Tracking | Line height |
|---|---|---|---|---|
| Hero headline | `clamp(3.2rem, 14vw, 11rem)` | 300 | `-0.03em` | 1.02 |
| Section headline | `clamp(2.6rem, 9vw, 7.5rem)` | 300 | `-0.03em` | 1.02 |
| Key number | `clamp(4.5rem, 19vw, 15rem)` | 300, accent colour | `-0.05em` | 0.95 |
| Lead | `clamp(1.15rem, 2.2vw, 1.6rem)` | 300, muted | 0 | 1.5 |
| Eyebrow | `0.8rem`, uppercase | 500, muted | `0.14em` | 1.7 |
| Meta / tags | `0.85–0.95rem` | 300, muted | `0.06em` on tags | 1.7 |

## Sections

```css
main > section {
  min-height: 100vh; min-height: 100svh;
  display: flex; flex-direction: column; justify-content: center;
  padding: 120px var(--gutter);
}
main > section:nth-child(odd)  { background: var(--dark);  color: var(--light); --muted: var(--muted-on-dark); }
main > section:nth-child(even) { background: var(--light); color: var(--dark);  --muted: var(--muted-on-light); }
.inner { max-width: 1100px; width: 100%; margin: 0 auto; }
```

Odd and even sections alternate automatically. If a new section changes the count, the alternation still holds, but check the first section (it should be dark).

## Fixed navigation

```css
.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 10; display: flex; justify-content: space-between;
  align-items: center; padding: 20px var(--gutter); color: #fff; mix-blend-mode: difference; font-size: .85rem; }
```

`mix-blend-mode: difference` keeps it readable on both backgrounds. On phones, hide the last links so it fits.

## Lists and rows

- Quiet lists: items separated by a 1px line at `rgba(128,128,128,.3)`, no boxes, no bullets.
- Bullets under a role: a short 8px dash instead of a dot, muted text.
- Links: weight 500, a 1px underline, accent colour on hover only.

## One-screen grid (several items that belong together)

```css
main > section.impact { padding: 88px var(--gutter) 40px; }
.impact-grid { display: grid; grid-template-columns: repeat(3, 1fr);
  gap: clamp(20px, 3vw, 44px) clamp(24px, 4vw, 64px); }
.impact-grid article { border-top: 1px solid rgba(128,128,128,.35); padding-top: 16px; }
@media (max-width: 900px) { .impact-grid { grid-template-columns: repeat(2, 1fr); } }
```

Reduce padding and type on short viewports (`max-height: 800px`) and on phones so all items fit without scrolling. Keep every card's wording; on very narrow phones, secondary tag lines may be hidden as long as the same facts appear elsewhere on the page. For an item with no number, use a blank spacer of the same height so rows line up.

## Motion

```css
.js .reveal { opacity: 0; transform: translateY(24px); transition: opacity .9s ease, transform .9s ease; }
.js .reveal.in { opacity: 1; transform: none; }
.js .reveal.d1 { transition-delay: .12s; } .js .reveal.d2 { transition-delay: .24s; }
@media (prefers-reduced-motion: reduce) { .js .reveal { opacity: 1; transform: none; transition: none; } }
```

Add `document.documentElement.classList.add('js')` in the `<head>`, then one `IntersectionObserver` (threshold 0.15) adds `.in` once per element. Without JS the content shows normally.

## Photo slot

```html
<img class="avatar reveal" src="profile.jpg" alt="Portrait of <name>" onerror="this.remove()">
```

Round, 112px, above the eyebrow. Keep it only if the source page has a photo reference. It hides itself while the file is missing.

## Quality bar

- No horizontal scroll at 375px.
- Hero headline within three lines at phone width.
- Every headline six words or fewer, ending in a full stop.
- Accent colour on large type only; text contrast at least 4.5:1 elsewhere.
- Every link reachable and visible by keyboard.
