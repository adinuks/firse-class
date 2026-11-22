# Design tokens and patterns

Use these as a starting kit. Adjust to the subject, but keep the proportions (the contrast between sizes is the style).

## Tokens

```css
:root{
  --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --black:#000; --ink:#1d1d1f; --grey:#6e6e73; --soft:#86868b;
  --paper:#fff; --mist:#f5f5f7; --night:#0b0b0c;
  --accent:#0071e3;            /* the only colour; links and the one primary action */
  --ease:cubic-bezier(.28,.11,.32,1);
  --pad:clamp(88px,14vw,160px);
}
```

System font stack only. Do not embed or link licensed Apple fonts. On Apple devices the stack renders as San Francisco; elsewhere it falls back gracefully.

## Type scale

| Role | Size | Weight | Tracking | Line height |
|---|---|---|---|---|
| Hero headline | `clamp(48px,9vw,112px)` | 600–700 | `-0.035em` | 1.02 |
| Section headline | `clamp(36px,6vw,72px)` | 600 | `-0.03em` | 1.05 |
| Sub-line | `clamp(20px,2.4vw,28px)` | 400 | `-0.01em` | 1.3, colour `--grey` |
| Body | `17–19px` | 400 | `0` | 1.5 |
| Eyebrow | `14–17px` | 600 | `0` | 1.2, colour `--accent` or `--grey` |
| Big number | `clamp(64px,12vw,160px)` | 700 | `-0.05em` | 1 |

Centre-align hero and section headlines. Left-align only for running text.

## Layout

- Content column max `980px`, hero text max `~12 words` wide per line. Sections are full-bleed, so the background runs edge to edge.
- Section padding `var(--pad)` top and bottom.
- Alternate section backgrounds: `--paper`, `--mist`, `--night` (white text on night). Never two of the same kind in a row.
- Grids of cards use `--mist` background, radius `28px`, padding `40px`, no borders or shadows. Two or three columns, collapsing to one under `~760px`.

## Components

- **Nav:** 48px tall, translucent (`rgba(255,255,255,.72)` plus `backdrop-filter:saturate(180%) blur(20px)`), small `12px` links, name left, one or two links right. No big buttons.
- **Primary CTA:** pill, `border-radius:980px`, accent background, white text, `17px`, padding `12px 22px`. Hover: slightly darker, no movement.
- **Secondary action:** plain accent text with a `›` after it. Underline on hover only.
- **Big-number block:** number in display size, caption beneath in `--grey` at body size. One or two per page.
- **Spec row:** small grey label above a large value, in a quiet grid. Use only for facts the user supplied.
- **Image slots:** if the user supplied an image, show it large with generous space and no frame. If not, don't fake one; use typography or an abstract soft gradient (`radial-gradient` from accent to transparent) at low contrast.

## Motion

```css
.rv{opacity:0;transform:translateY(32px) scale(.985);transition:opacity .9s var(--ease),transform .9s var(--ease)}
.rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}}
```

Trigger `.in` with a single `IntersectionObserver`. Provide a no-JS fallback (`.no-js .rv{opacity:1;transform:none}`). One entrance per element; no loops, parallax-jank, bounce or spinning things.

## Dark section detail

On `--night` sections, headline `#f5f5f7`, sub-line `#a1a1a6`, links `#2997ff`. A very faint top glow (`radial-gradient(ellipse at 50% 0%, rgba(41,151,255,.18), transparent 60%)`) adds depth without decoration.

## Before/after toggle (teaching mode)

A fixed pill at the top centre with two buttons switches a `data-mode="before|after"` attribute on `<body>`. Render both versions in the same file as two `<main>` blocks and show one at a time. The "Before" version should be recognisably ordinary: dense, many bullets, small type, boxed cards with borders, a default-blue rectangular button, feature-list copy. The "After" version uses everything above. Same facts, different language.

## Quality bar

- No horizontal scroll at 375px width.
- Hero headline stays within three lines at phone width.
- Text contrast is at least 4.5:1 on every background.
- Every interactive element is reachable and visible by keyboard.
