---
name: aditya-brand-voice
description: Rebuild an HTML page in Aditya's brand voice (calm, minimal, very large display type, one idea per screen, alternating dark and light sections, one orange accent, gentle fade-and-rise motion) while keeping every fact exactly as it is. Use only when the user explicitly asks for it by name, for example "/aditya-brand-voice", "rebuild this in my voice", "use my brand voice on this page".
disable-model-invocation: true
---

# Aditya's brand voice

Rebuild an HTML page so it carries Aditya's brand language, and change nothing but the language. The facts on the page are the user's career record; a number rounded up or a claim sharpened is a false statement on a public page, so the facts stay word for word and only the voice, type, space, colour and motion change.

The reference build is `v1-just-ask.html` (the portfolio, calm and minimal, dark and light chapters, one orange accent). If it is in the project, open it to see the voice in practice before you start. `references/design-tokens.md` holds the CSS and patterns taken from it.

## Inputs and output

- **Input:** an HTML page, or facts the user supplies in the message, files or a resume. HTML only; if the user hands you plain copy, say you build pages and ask for the page or facts.
- **Output:** one self-contained `.html` file (inline CSS and a little inline JS, no frameworks, no external fonts or libraries) saved next to the source.
- **Never overwrite.** Save under the new name the user gives. If they gave none, pick a clear new one (for example `v6-<source-name>.html`) and say so. The source file stays untouched because the user keeps earlier versions to compare.

## The voice

Calm and minimal. Say less; let space and scale carry the weight. No exclamation marks, no hype words ("world-class", "cutting-edge", "passionate"), no filler openings ("Welcome to…"). Plain, first-person statements of fact.

- **Headlines:** six words or fewer, a complete thought or a plain label, ending in a full stop ("Mainframe replacement.", "Where I work.", "Nike."). Count the words. A seventh word makes it a sentence, and the short length is the point.
- **Body and sub-lines:** calm, short, in the user's own words. Reuse the sentences from the source rather than paraphrasing them.
- **Eyebrows and meta lines** (roles, dates, places) stay exactly as written in small quiet type.

## Facts stay exact

This is the rule that matters most.

1. Copy every sentence, bullet, date, role, number, name and credential from the source verbatim. Layout may change; text inside the facts does not.
2. Keep the precision the source used. "~75%", "about $4B", "nearly 38%", "18+ years" and "more than" are part of the claim. Do not drop the "~", turn "18+" into "eighteen", or merge two numbers into one.
3. Do not invent anything: no new numbers, clients, quotes, awards, skills or dates. If a section needs something the source lacks, cut the section or leave an obvious `[add …]` marker.
4. Headlines and card titles are the one place wording may change, because the headline rule applies. Each must still be traceable to something on the source page. Do not let a headline claim more than its body does.
5. Contact details: carry over only what the source page already shows. Do not add an email address or phone number from other files, because a public page is a different audience from a CV.
6. Missing media: if the source references an image that is not there, keep the reference and let it hide itself (`onerror="this.remove()"`). Do not substitute a stock or generated picture.

## The design language

Read `references/design-tokens.md` for the exact tokens, then apply:

- **One idea per screen.** Each section fills the viewport and holds a single idea, with generous space. A group of items that belongs together (for example a set of results the user wants to compare) can share one screen as a quiet grid, as long as it fits without scrolling.
- **Type.** System font only. Very large display type for headlines and key numbers, calm body text, two weights (300 and 500). Tight tracking on display sizes.
- **Colour.** Alternate dark (`#0d0d0f`) and light (`#f5f2ee`) full-bleed sections, so never two of the same in a row. One accent, burnt orange `#d9480f`, used only on large type (key numbers, hover states) because it falls just under 4.5:1 contrast on the light background at small sizes. No second accent.
- **Motion.** A gentle fade and rise as elements scroll into view: small translate, slow ease, no bounce, no loops. Switch it off for `prefers-reduced-motion`, and keep content visible if JavaScript is off.
- **Navigation.** A minimal fixed bar that stays readable on both backgrounds, with a few text links.

## Workflow

1. **Read the source.** List every fact on it (sections, roles, dates, numbers, links). This list is what you check against at the end.
2. **Find the order of ideas.** Decide what each screen says, and what the headline for each is. Write the headlines first and count their words.
3. **Build** the single HTML file using the tokens and patterns.
4. **Verify.**
   - Run `python3 -I scripts/check_facts.py <source.html> <new.html>`. It reports any list item, paragraph or small line from the source that is not word for word in the new file. Anything it flags should be a deliberate headline or layout change, and nothing else.
   - If a browser is available (Playwright with Chromium), load the page at 1440×900, 1280×720 and 375×812. Confirm there is no horizontal scroll and that any section meant to fit one screen does. Check that headlines stay within three lines at phone width.
   - Confirm every headline is six words or fewer and ends in a full stop.
5. **Save and commit only if asked.** The user decides when to commit or push.

## What to tell the user

Keep the reply short:

1. The file path of the new page.
2. **Fact check:** say whether every fact matches the source word for word. List anything reworded (usually headlines) and anything left out.
3. **What changed:** two or three lines on the language changes (voice, type, space, colour, motion), with a real before-and-after from the page.
4. **Still missing:** anything the page is waiting for, such as a photo file, and anything you could not verify.
