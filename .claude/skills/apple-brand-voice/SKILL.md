---
name: apple-brand-voice
description: Rebuild a page, deck or piece of copy in an Apple-inspired brand language — minimal, product-first, cinematic type, huge whitespace, and punchy short-sentence copywriting — and explain what changed and why so it can be taught. Use only when the user explicitly asks for it (for example "/apple-brand-voice", "make this Apple-style", "Apple-like brand language", "show my student what changing brand language means").
disable-model-invocation: true
---

# Apple-inspired brand language

Turn whatever the user gives you (a topic, a rough page, existing copy, a product, a person) into a front-end page that *feels* like Apple's brand language, with copy that hits in a breath. Then show what changed, because the point is often to teach: a brand language is a set of consistent choices (voice, type, space, colour, motion, rhythm), and swapping them changes how the same facts feel.

This is inspiration, not impersonation. Match the principles. Never use Apple's logo, product names, trademarks or actual slogans, never claim to be Apple, and never copy their copy. Everything on the page belongs to the user's subject, and the brand is never used on it to describe the style (a real client or partner name from the user's own material is fine).

## How to work

1. **Find the one idea.** Ask what the single thing is that the audience should remember. If the user gave a topic only, pick the strongest idea yourself and say so. A page with three ideas has none.
2. **Write the copy first.** Read `references/copy-playbook.md`. Draft headlines, sub-lines and CTAs before any HTML, because the layout exists to give each line room to land. Every claim must come from material the user gave you. Do not invent numbers, quotes or features. If a section needs a proof point you don't have, cut the section or leave an obvious `[add number]` marker.
3. **Build the page.** Read `references/design-tokens.md` and use its tokens and patterns. One self-contained HTML file (inline CSS, tiny inline JS), no frameworks, works on a phone, respects `prefers-reduced-motion`.
4. **Verify.** Open it in the browser pane or take a screenshot if tools allow. Check that the hero headline fits on one to three lines at phone width, nothing overflows, and every section has exactly one job.
5. **Explain the shift.** Finish with a short "Brand language shift" note (format below). If the user is teaching, also build the before/after toggle described below.

## The brand language in one paragraph

Confident, quiet, specific. Say less, and make every word carry weight. Show one thing at a time at enormous size, surround it with space, and let contrast (dark/light, big/small, long pause/short line) do the persuading. Never shout; the scale does that. Benefits before specs, people before parts, and a number is always better than an adjective.

## Rules that matter most (and why)

- **One idea per screen.** Attention is the scarcest thing on the page; splitting it makes both halves weaker.
- **Headlines are short declaratives of six words or fewer, ending in a full stop. Treat six as a hard limit.** Count the words before you finish; if a headline runs seven, cut it, because the length is what makes it punchy. Sub-lines and body can run longer. The full stop reads as certainty.
- **Keep every claim as exact as the source.** "More than two decades" becomes "20+ years", never "Twenty years", because rounding down turns a floor into a claim of precision the user didn't make. Do the same for "over", "at least" and similar words.
- **Never use the brand's name to describe the page or its style, anywhere on the page or in its copy, including footers and disclaimers.** The page belongs to the user's subject. Put any "inspired by" note in your reply to the user, not in the file. The exception is a real fact from the user's own material: if the brand (or any company) is genuinely one of their clients, employers or partners, list it like any other name.
- **Big type, tight tracking, few weights.** Display text uses a heavy-ish weight with negative letter-spacing; body text is calm and grey. The size jump between the two is the hierarchy.
- **Space is the luxury signal.** Section padding is generous (think 120px+ on desktop). If it feels too empty, it's probably right.
- **Alternate full-bleed backgrounds** (near-black, off-white, soft grey) to pace the scroll like chapters. One accent colour only, used for links and the single primary action.
- **Product (or idea) as hero.** If there is an image, it is large and alone. If there is no image, make the headline and one big number the hero. Never fake product shots.
- **Motion is a whisper.** Fade-and-rise on scroll, easing that decelerates, nothing bouncing. Motion explains, never decorates.
- **Plain, human words.** No jargon, hedging, exclamation marks, or stacked superlatives ("revolutionary, world-class, cutting-edge"). Replace with a concrete fact.

## Output

Save the page as `<name>.html` next to the user's other files (ask only if the location is genuinely unclear; never overwrite an existing file, pick a new name). Give the file link and the shift note, nothing more.

### Brand language shift note (always include)

A compact table, then two lines on what to try next:

| Dimension | Before (typical) | After (this brand language) | Why it works |
|---|---|---|---|
| Voice | … | … | … |
| Headline | … | … | … |
| Type | … | … | … |
| Space | … | … | … |
| Colour | … | … | … |
| Motion | … | … | … |

Use real examples from the user's own content in the Before/After cells (an actual old line next to its rewrite), not generic descriptions. Keep it to six rows.

### Teaching mode

When the user mentions a student, class, lesson, workshop, "show the difference", or "before and after", also make the page a before/after demo: the same content with a pill toggle at the top (`Before` / `After`). "Before" is deliberately ordinary brand language (busy layout, feature-list copy, generic blue buttons, crowded spacing); "After" is the Apple-inspired version. Both must contain the same facts so the only thing changing is the language. Add three small numbered annotation chips on the After view pointing at copy, type and space, each one sentence long.

## When the input is only copy

If the user gives only text, return the rewritten copy first (headline, sub-line, three supporting lines, CTA), with the shift note's Voice and Headline rows, and offer the page. Don't build HTML they didn't ask for.
