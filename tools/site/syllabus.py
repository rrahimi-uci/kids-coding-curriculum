"""Read a track's syllabus (docs/SYLLABUS.md, docs/JUNIOR-SYLLABUS.md) into data for the level and curriculum pages.

Both files use the same layout: one `## Level N — Name (languages)` section per level with a goals table,
a weeks table, the final project paragraph and an assessments paragraph.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def md_inline(text: str) -> str:
    """Convert a short markdown fragment to inline HTML with Pandoc."""
    p = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"], input=text,
                       capture_output=True, text=True, check=True)
    out = p.stdout.strip()
    return re.sub(r"^<p>(.*)</p>$", r"\1", out, flags=re.S)


def parse_table(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows[1:]  # drop header


def parse(path: str | Path = "docs/SYLLABUS.md") -> dict[int, dict]:
    """Levels of one track's syllabus, keyed by level number (1, 2, 3)."""
    s = (ROOT / path).read_text(encoding="utf-8")
    levels: dict[int, dict] = {}
    parts = re.split(r"(?m)^## (Level (\d) — .*)$", s)
    # parts: [pre, heading, num, body, heading, num, body ...]
    for i in range(1, len(parts), 3):
        heading, num, body = parts[i], int(parts[i + 1]), parts[i + 2]
        name = re.match(r"Level \d — (.+?)(?:\s*\(|$)", heading).group(1).strip()
        lang = re.search(r"\((.*)\)", heading)
        tools = re.search(r"\*\*Tools:\*\*(.*?)(?=\n\n)", body, re.S)
        goals_blk = re.search(r"### Level \d goals\n(.*?)(?=\n### )", body, re.S).group(1)
        weeks_blk = re.search(r"### Level \d weeks\n(.*?)(?=\n\*\*Level \d final project)", body, re.S).group(1)
        proj = re.search(r"(\*\*Level \d final project.*?)(?=\n\n\*\*Assessments)", body, re.S).group(1)
        goals = [{"code": r[0], "text": md_inline(r[1])} for r in parse_table(goals_blk)]
        weeks = []
        for r in parse_table(weeks_blk):
            weeks.append({"n": int(r[0]), "title": md_inline(r[1]), "idea": md_inline(r[2]),
                          "concepts": md_inline(r[3]), "unplugged": md_inline(r[4]), "bughunt": md_inline(r[5]),
                          "citizenship": md_inline(r[6])})
        # The reference solution is teacher-only: never describe it on the public site.
        proj = re.sub(r"Reference\s+solution:\s*\*[^*]+\*\s*\((?:[^()]|\([^()]*\))*\)\.?\s*", "", proj)
        pt = re.match(r"\*\*Level \d final project — “(.*?)”\.?\*\*", proj)
        levels[num] = {
            "number": num, "name": name, "languages": lang.group(1) if lang else "",
            "tools": md_inline(re.sub(r"\s+", " ", tools.group(1)).strip()) if tools else "",
            "goals": goals, "weeks": weeks,
            "project_title": pt.group(1) if pt else "",
            "project_html": md_inline(re.sub(r"\s+", " ", proj)),
        }
    return levels


if __name__ == "__main__":
    import json
    import sys
    d = parse(*sys.argv[1:2])
    for n, v in d.items():
        print(n, v["name"], len(v["goals"]), len(v["weeks"]), v["project_title"])
