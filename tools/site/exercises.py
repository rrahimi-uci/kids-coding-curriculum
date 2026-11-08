"""Exercise pages: README + starter code + hints, rendered from the source folders.

Only files tagged public in site/manifest.yml are read: README.md, starter.py,
hints.md and the data files the starter needs. Solutions, tests and the
self-check script are never opened by this module.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup
from .texconv import no_highlight
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

ROOT = Path(__file__).resolve().parents[2]
_FMT = HtmlFormatter(nowrap=True, classprefix="tok-")


def md_to_html(md: str) -> str:
    p = subprocess.run(["pandoc", "-f", "gfm+task_lists", "-t", "html5", "--wrap=none", *no_highlight(),
                        "--shift-heading-level-by=0"], input=md, capture_output=True, text=True, check=True)
    return p.stdout


def read_hints(path: Path) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    hints = []
    for m in re.finditer(r"^## (Hint \d+): (.*?)\n(.*?)(?=^## Hint|\Z)", text, re.S | re.M):
        body = md_to_html(m.group(3).strip())
        hints.append({"label": m.group(1), "title": m.group(2).strip(), "html": body})
    return hints


def clean_readme_md(md: str) -> str:
    """The README as published: paragraphs about the self-check script (not published) are removed."""
    paras = re.split(r"\n[ \t]*\n", md)
    keep = [p for p in paras if not ("check_my_work" in p and re.search(r"check your work", p, re.I))]
    return "\n\n".join(keep) + ("\n" if md.endswith("\n") else "")


WEB_NOTE = ("> **On this website:** the automatic self-check files that come with the course folder are not "
            "published here. Work from the steps and the hints, and check your work by running your program.\n\n")


def web_starter(code: str) -> str:
    """The starter as published: comments that point to the unpublished self-check script are reworded."""
    code = re.sub(r"then open check_my_work\.py and press Run\.", "then press Run and see if it does what the README says.", code)
    code = re.sub(r"then run check_my_work\.py\.", "then run it again to check.", code)
    code = re.sub(r"Open check_my_work\.py and press Run: the tests tell you", "Run it and look closely: the program shows you", code)
    return code


def convert_readme(md: str, warnings: list[str]) -> tuple[str, str, str]:
    """Return (number, title, body_html) for an exercise README."""
    lines = md.splitlines()
    number, title = "", ""
    m = re.match(r"#\s+(?:Exercise|Homework)\s+([\d.]+)\s*[\-–—]\s*(.*)", lines[0])
    if m:
        number, title = m.group(1), m.group(2).strip()
        lines = lines[1:]
    else:
        title = re.sub(r"^#\s+", "", lines[0]).strip()
        lines = lines[1:]
    body = "\n".join(lines)
    # self-check script is not published (it needs the private tests)
    new = clean_readme_md(body)
    if "check_my_work" in new:  # steps that depend on the self-check files: tell the child why they are missing
        new = WEB_NOTE + new
    if new != body:
        warnings.append("info: removed the 'Check your work: check_my_work.py' paragraph from an exercise page")
    html = md_to_html(new)
    soup = BeautifulSoup(html, "html.parser")
    # interactive, labeled checkboxes for the checklist
    for li in soup.find_all("li"):
        inp = li.find("input", attrs={"type": "checkbox"})
        if inp:
            inp.attrs.pop("disabled", None)
            li["class"] = "check-item"
            if inp.find_parent("label") is None:  # Pandoc already wraps task-list items in a label
                label = soup.new_tag("label")
                for child in list(li.children):
                    label.append(child.extract())
                li.append(label)
    for h in soup.find_all(["h2", "h3"]):
        h["id"] = re.sub(r"[^a-z0-9]+", "-", h.get_text().lower()).strip("-")
    for code in soup.find_all("code"):
        pass
    return number, title, str(soup)


def build_exercise(dir_: Path, level: int, files_ok: list[str], warnings: list[str]) -> dict:
    week = dir_.parent.name
    slug = f"{week}-{dir_.name}"
    readme = (dir_ / "README.md").read_text(encoding="utf-8")
    number, title, body = convert_readme(readme, warnings)
    kind = "python" if (dir_ / "starter.py").exists() else "scratch"
    data = {
        "slug": slug, "folder": f"{week}/{dir_.name}", "week": int(week.replace("week", "")),
        "level": level, "kind": kind, "homework": dir_.name.startswith("hw-"),
        "number": number, "title": title, "body": body,
        "hints": read_hints(dir_ / "hints.md"),
        "starter": None, "files": [], "readme_clean": clean_readme_md(readme),
    }
    if kind == "python":
        code = web_starter((dir_ / "starter.py").read_text(encoding="utf-8"))
        data["starter"] = {"name": "starter.py", "raw": code,
                           "html": highlight(code, PythonLexer(), _FMT).rstrip("\n")}
    for name in files_ok:
        if name in ("README.md", "starter.py", "hints.md"):
            continue
        if (dir_ / name).exists():
            data["files"].append(name)
    return data
