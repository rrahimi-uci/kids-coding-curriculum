#!/usr/bin/env python3
"""Content quality gates for the website (standard library only).

    python3 -m tools.site.check_content [site/dist]

* every lesson (week) page has a non-empty "What you will learn" list,
* every <img> has a non-empty alt text (and TikZ/Scratch figures have a descriptive one),
* every exercise page has at least three hints,
* every page has exactly one <h1> and a lang attribute,
* Python code blocks keep their indentation (a line ending in a colon is followed by an indented line).
"""
from __future__ import annotations

import html as htmlmod
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs: list[dict] = []
        self.h1 = 0
        self.lang = False
        self.objectives_li = 0
        self.hints = 0
        self._in_obj = False
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.imgs.append(a)
        if tag == "div" and "objectives" in (a.get("class") or "").split():
            self._in_obj = True
            self._depth = 1
        elif self._in_obj and tag == "div":
            self._depth += 1
        if self._in_obj and tag == "li":
            self.objectives_li += 1
        if tag == "details" and "hint" in (a.get("class") or "").split():
            self.hints += 1

    def handle_endtag(self, tag):
        if self._in_obj and tag == "div":
            self._depth -= 1
            if self._depth == 0:
                self._in_obj = False


HEADER = re.compile(r"^\s*(def|class|if|elif|else|for|while|try|except|finally|with)\b.*:\s*(#.*)?$")


def broken_indentation(raw: str) -> str | None:
    """First Python block in the page whose indentation was lost, or None."""
    for m in re.finditer(r'<code class="language-python"[^>]*>(.*?)</code>', raw, re.S):
        text = htmlmod.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
        lines = [ln for ln in text.split("\n") if ln.strip() and not ln.strip().startswith("#")]
        for a, b in zip(lines, lines[1:]):
            if HEADER.match(a) and len(b) - len(b.lstrip()) <= len(a) - len(a.lstrip()):
                return a.strip()[:50]
    return None


def main(argv=None) -> int:
    dist = Path((argv or sys.argv[1:] or [str(ROOT / "site" / "dist")])[0])
    problems: list[str] = []
    pages = 0
    for f in sorted(dist.rglob("index.html")) + sorted(dist.glob("*.html")):
        rel = f.relative_to(dist).as_posix()
        if rel.startswith("pagefind/"):
            continue
        p = Page()
        raw = f.read_text(encoding="utf-8")
        p.feed(raw)
        bad = broken_indentation(raw)
        if bad:
            problems.append(f"{rel}: Python code lost its indentation after '{bad}'")
        pages += 1
        if not p.lang:
            problems.append(f"{rel}: <html> has no lang attribute")
        if rel != "404.html" and p.h1 != 1:
            problems.append(f"{rel}: expected exactly one <h1>, found {p.h1}")
        for im in p.imgs:
            if "alt" not in im or im["alt"] is None:
                problems.append(f"{rel}: image without alt attribute: {im.get('src')}")
            elif not im["alt"].strip():
                problems.append(f"{rel}: image with empty alt text: {im.get('src')}")
            elif "fig" in (im.get("class") or "") and len(im["alt"].strip()) < 12:
                problems.append(f"{rel}: figure alt text too short: {im.get('src')}")
        parts = rel.split("/")
        if len(parts) == 4 and parts[0] == "levels" and parts[2].startswith("week-"):
            if p.objectives_li == 0:
                problems.append(f"{rel}: lesson page has no learning objectives")
        if len(parts) == 5 and parts[0] == "levels" and parts[2] == "exercises":
            if p.hints < 3:
                problems.append(f"{rel}: exercise has {p.hints} hints (need at least 3)")
    print(f"content check: {pages} pages inspected", file=sys.stderr)
    if problems:
        print("CONTENT CHECK FAILED:")
        for x in problems[:60]:
            print("  -", x)
        return 1
    print("content check passed: objectives, alt text, hints and headings are all present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
