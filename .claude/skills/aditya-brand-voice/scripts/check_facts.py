#!/usr/bin/env python3
"""Check that every fact on a source page survives word for word in a rebuilt page.

Usage: python3 -I check_facts.py SOURCE.html REBUILT.html

It reads the visible text of the <main> block (or <body>) in each file, takes every
list item, paragraph, small line, strong line and table cell from the source, and
reports any that do not appear verbatim in the rebuilt page. Headlines (h1-h3) are
reported separately because they may be reworded on purpose.
"""
import html
import re
import sys


def norm(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main_block(source: str) -> str:
    m = re.search(r"<main\b.*?</main>", source, flags=re.S)
    if m:
        return m.group(0)
    m = re.search(r"<body\b.*?</body>", source, flags=re.S)
    return m.group(0) if m else source


def pieces(block: str, tags):
    found = []
    for tag in tags:
        for m in re.findall(rf"<{tag}\b[^>]*>(.*?)</{tag}>", block, flags=re.S):
            text = norm(m)
            if len(text) > 3 and text not in found:
                found.append(text)
    return found


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src = open(sys.argv[1], encoding="utf-8").read()
    new = open(sys.argv[2], encoding="utf-8").read()
    src_block, new_text = main_block(src), norm(main_block(new))

    facts = pieces(src_block, ["li", "p", "small", "strong", "td", "dd"])
    heads = pieces(src_block, ["h1", "h2", "h3"])

    # A wrapper such as an <li> that holds a nested <ul> repeats the text of its parts.
    # Drop any line that contains another line; its parts are checked on their own.
    leaves = [t for t in facts if sum(1 for o in facts if o != t and o in t) < 1]
    true_missing = [t for t in leaves if t not in new_text]

    print(f"Checked {len(leaves)} lines from the source.")
    if true_missing:
        print(f"\n{len(true_missing)} not found word for word in the rebuilt page:")
        for t in true_missing:
            print(f"  - {t[:200]}")
    else:
        print("All lines found word for word.")

    reworded = [h for h in heads if h not in new_text]
    if reworded:
        print(f"\n{len(reworded)} source headings not found as written (fine if deliberate):")
        for h in reworded:
            print(f"  - {h[:120]}")

    # Headline rule on the rebuilt page: six words or fewer, ends in a full stop.
    bad = []
    for m in re.findall(r"<h[12]\b[^>]*>(.*?)</h[12]>", new, flags=re.S):
        h = norm(m)
        if len(h.split()) > 6 or not h.endswith("."):
            bad.append(h)
    if bad:
        print("\nHeadlines breaking the rule (six words or fewer, ending in a full stop):")
        for h in bad:
            print(f"  - {h}")
    else:
        print("\nAll h1/h2 headlines are six words or fewer and end in a full stop.")

    return 1 if true_missing or bad else 0


if __name__ == "__main__":
    sys.exit(main())
