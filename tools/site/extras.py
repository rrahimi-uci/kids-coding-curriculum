"""Projects, cheat sheets, glossaries, parent notes and resource guides for the website.

All of these are student- or family-facing sources listed as public in site/manifest.yml. The
project *starter* folders are published (templates the child edits); the reference solutions,
teacher guides and assessments are never touched.
"""
from __future__ import annotations

import fnmatch
import glob
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

from . import pdfs, texconv
from .exercises import md_to_html
from .texconv import match_brace, read_args

ROOT = Path(__file__).resolve().parents[2]
BASE = "%BASE%"
_FMT = HtmlFormatter(nowrap=True, classprefix="tok-")


# ------------------------------------------------------------------------------------ pdf helpers
def level_pdfs(entry: dict, stems: list[str], skip: bool) -> dict:
    """Copy whole-level PDFs to downloads/<band>/<level>/<id>-<stem>.pdf, e.g. grade-2-3-level-1-glossary.pdf."""
    out: dict[str, dict] = {}
    if skip:
        return out
    pdf_map = pdfs.ensure_level_pdfs(entry["dir"], stems)
    for stem, variants in pdf_map.items():
        for variant, src in variants.items():
            rel = f"downloads/{entry['path']}/{entry['id']}-{stem}{'-dyslexia' if variant == 'dyslexia' else ''}.pdf"
            dst = ROOT / "site" / "public" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            out.setdefault(stem, {})[variant] = {"url": f"{BASE}{rel}", "kb": dst.stat().st_size // 1024}
    return out


# ------------------------------------------------------------------------------------ glossary
def _inline(tex_list: list[str]) -> list[str]:
    """Convert LaTeX fragments to inline HTML with one Pandoc call."""
    if not tex_list:
        return []
    doc = "\\begin{description}\n" + "\n".join(f"\\item[K{i}] {t}" for i, t in enumerate(tex_list)) + "\n\\end{description}"
    doc = re.sub(r"\\(small|footnotesize|normalsize)\b", "", doc)
    doc = re.sub(r"\\texttt\{", r"\\texttt{", doc)
    p = subprocess.run(["pandoc", "-f", "latex", "-t", "html5", "--wrap=none", "--mathml"], input=doc,
                       capture_output=True, text=True)
    soup = BeautifulSoup(p.stdout, "html.parser")
    out = []
    for i in range(len(tex_list)):
        dt = soup.find("dt", string=f"K{i}")
        dd = dt.find_next_sibling("dd") if dt else None
        html = dd.decode_contents() if dd else ""
        html = re.sub(r"^\s*<p>(.*)</p>\s*$", r"\1", html, flags=re.S).strip()
        out.append(html)
    return out


def parse_glossary(tex_path: Path) -> list[dict]:
    s = tex_path.read_text(encoding="utf-8")
    s = s.split("\\begin{document}", 1)[1]
    items: list[tuple[str, str, str, str]] = []  # term, where, meaning, example (all LaTeX)
    # Level 1: \gl{term}{where}{meaning}{example}
    for m in re.finditer(r"\\gl(?![A-Za-z])", s):
        a, _ = read_args(s, m.end(), 4)
        if len(a) == 4:
            items.append((a[0], a[1], a[2], a[3]))
    # Levels 2 and 3: \term{term}{meaning}{week}
    for m in re.finditer(r"\\term(?![A-Za-z])", s):
        a, _ = read_args(s, m.end(), 3)
        if len(a) == 3:
            items.append((a[0], "W" + a[2].strip() if a[2].strip() else "", a[1], ""))
    # Level 3 also has \item[term] meaning (week N) lines
    for m in re.finditer(r"\\item\[([^\]]+)\]\s*(.*?)\s*\{\\small\\color\{kcgray\}\(week (\d+)\)\}", s):
        items.append((m.group(1), "W" + m.group(3), m.group(2), ""))
    terms = _inline([i[0] for i in items])
    means = _inline([i[2] for i in items])
    exs = _inline([i[3] for i in items if i[3].strip()])
    out, k = [], 0
    for (t, where, _, ex), term_html, mean_html in zip(items, terms, means):
        example = ""
        if ex.strip():
            example = exs[k]
            k += 1
        plain = re.sub(r"<[^>]+>", "", term_html)
        out.append({"term": term_html, "key": plain.lower().strip(" `\"'"), "where": where, "meaning": mean_html,
                    "example": example})
    out.sort(key=lambda e: e["key"])
    return out


# ------------------------------------------------------------------------------------ project
def _highlight(code: str) -> str:
    return highlight(code, PythonLexer(), _FMT).rstrip("\n")


def build_project(entry: dict, manifest: dict, gen: Path, fig_dir: Path, warnings: list[str]) -> dict | None:
    pub = manifest["public"]
    d, path, ident, label = entry["dir"], entry["path"], entry["id"], entry["label"]
    brief = ROOT / pub["project_brief"].format(dir=d)
    if not brief.exists():
        return None
    res = texconv.convert_file(brief, entry["classopts"], fig_dir, f"{BASE}generated/fig/{ident}", {})
    warnings += [f"{label} project brief: {w}" for w in res.warnings]
    html_dir = gen / "html" / path
    html_dir.mkdir(parents=True, exist_ok=True)
    (html_dir / "project.html").write_text(res.html, encoding="utf-8")
    toc = [{"level": lv, "id": i, "text": t} for lv, i, t in res.toc]
    # starter folder (templates only); some levels (Scratch projects) have none
    sdir = ROOT / pub["project_starter_dir"].format(dir=d)
    dest = ROOT / "site" / "public" / "downloads" / path / "project-starter"
    if dest.exists():
        shutil.rmtree(dest)
    if not sdir.is_dir():
        return {"title": texconv_title(res), "toc": toc, "starter_readme": "", "starter_files": [], "zip": None}
    files, readme_html = [], ""
    zpath = ROOT / "site" / "public" / "downloads" / path / f"{ident}-project-starter-files.zip"
    zpath.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(sdir.rglob("*")):
            if not f.is_file() or "__pycache__" in f.parts or f.suffix in (".pyc",):
                continue
            rel = f.relative_to(sdir).as_posix()
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest / rel)
            z.write(f, f"project-starter/{rel}")
            if f.name == "README.md":
                readme_html = md_to_html(f.read_text(encoding="utf-8"))
                continue
            if f.suffix == ".py":
                code = f.read_text(encoding="utf-8")
                files.append({"name": rel, "html": _highlight(code), "url": f"{BASE}downloads/{path}/project-starter/{rel}"})
            else:
                files.append({"name": rel, "html": "", "url": f"{BASE}downloads/{path}/project-starter/{rel}"})
    # the README's own level-1 heading becomes the page section title
    soup = BeautifulSoup(readme_html, "html.parser")
    for h in soup.find_all(["h1", "h2", "h3"]):
        h.name = "h3" if h.name in ("h1", "h2") else "h4"
        h["id"] = "starter-" + re.sub(r"[^a-z0-9]+", "-", h.get_text().lower()).strip("-")
    for li in soup.find_all("li"):
        inp = li.find("input", attrs={"type": "checkbox"})
        if inp:
            inp.attrs.pop("disabled", None)
            li["class"] = "check-item"
            if inp.find_parent("label") is None:
                label = soup.new_tag("label")
                for ch in list(li.children):
                    label.append(ch.extract())
                li.append(label)
    return {
        "title": texconv_title(res), "toc": toc,
        "starter_readme": str(soup), "starter_files": files,
        "zip": {"url": f"{BASE}downloads/{path}/{ident}-project-starter-files.zip", "kb": max(1, zpath.stat().st_size // 1024)},
    }


def texconv_title(res) -> str:
    return re.sub(r"\\[A-Za-z]+\s*", "", res.meta.get("title", "Project brief"))


# ------------------------------------------------------------------------------------ extras
def build_extras(entry: dict, manifest: dict, gen: Path, fig_dir: Path, warnings: list[str]) -> dict:
    pub = manifest["public"]
    d, ident, label = entry["dir"], entry["id"], entry["label"]
    out: dict = {}
    html_dir = gen / "html" / entry["path"]
    html_dir.mkdir(parents=True, exist_ok=True)
    for key, name in (("cheat_sheet", "cheat-sheet"), ("parent_notes", "parent-notes")):
        path = ROOT / pub[key].format(dir=d)
        res = texconv.convert_file(path, entry["classopts"], fig_dir, f"{BASE}generated/fig/{ident}", {})
        warnings += [f"{label} {name}: {w}" for w in res.warnings]
        (html_dir / f"{name}.html").write_text(res.html, encoding="utf-8")
        out[key] = {"title": res.meta.get("title", name), "subtitle": res.meta.get("subtitle", ""),
                    "toc": [{"level": lv, "id": i, "text": t} for lv, i, t in res.toc if lv == 2 or key == "cheat_sheet"]}
    out["glossary"] = parse_glossary(ROOT / pub["glossary"].format(dir=d))
    return out


# ------------------------------------------------------------------------------------ resources
def build_resources(manifest: dict, gen: Path, warnings: list[str]) -> list[dict]:
    out = []
    script = ROOT / manifest["public"]["install_script"]
    dest = ROOT / "site" / "public" / "downloads" / script.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(script, dest)
    for f in sorted(glob.glob(str(ROOT / manifest["public"]["resources"]))):
        md = Path(f).read_text(encoding="utf-8")
        if "{{INSTALL_SCRIPT}}" in md:  # the install script is shown on the page and offered as a download
            script = (ROOT / manifest["public"]["install_script"]).read_text(encoding="utf-8")
            md = md.replace("{{INSTALL_SCRIPT}}", "```bash\n" + script.rstrip("\n") + "\n```")
        title = re.match(r"#\s+(.*)", md).group(1).strip()
        body = md.split("\n", 1)[1]
        p = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none", *texconv.no_highlight(),
                            "--shift-heading-level-by=0"], input=body, capture_output=True, text=True, check=True)
        soup = BeautifulSoup(p.stdout, "html.parser")
        toc = []
        for h in soup.find_all("h2"):
            toc.append({"id": h.get("id", ""), "text": h.get_text(" ", strip=True)})
        for pre in soup.find_all("pre"):
            code = pre.find("code")
            pre["tabindex"] = "0"
            # one-line commands wrap instead of scrolling sideways, so a parent sees the whole line they paste
            single = len(pre.get_text().strip().splitlines()) == 1
            wrap = soup.new_tag("div", attrs={"class": "code-block code-command" if single else "code-block"})
            pre.wrap(wrap)
        for a in soup.find_all("a", href=True):
            if a["href"].startswith("../"):
                a["href"] = BASE + "resources/" + a["href"][3:]
        slug = Path(f).stem
        (gen / "html" / "resources").mkdir(parents=True, exist_ok=True)
        (gen / "html" / "resources" / f"{slug}.html").write_text(str(soup), encoding="utf-8")
        out.append({"slug": slug, "title": title, "toc": toc})
    return out
