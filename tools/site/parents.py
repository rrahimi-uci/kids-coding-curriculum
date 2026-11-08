"""Parent pages: research evidence, slide gallery, FAQ and family information.

Everything is generated from parents/main.tex (frames, sources, speaker-note paragraphs and the
questions-and-answers), parents/content/shared.tex (course facts) and parents/references.bib.
Slide images are rendered from the built deck PDF.
"""
from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from pathlib import Path

from PIL import Image

from .texconv import match_brace, no_highlight, read_args

ROOT = Path(__file__).resolve().parents[2]
BASE = "%BASE%"


# --------------------------------------------------------------------------- helpers
def pandoc_html(tex: str, fmt: str = "latex") -> str:
    p = subprocess.run(["pandoc", "-f", fmt, "-t", "html5", "--wrap=none", *no_highlight()],
                       input=tex, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("pandoc failed: " + p.stderr[:300])
    return p.stdout.strip()


def parse_newcommands(text: str) -> dict[str, str]:
    macros = {}
    for m in re.finditer(r"\\newcommand\{\\([A-Za-z]+)\}", text):
        args, _ = read_args(text, m.end(), 1)
        if args:
            macros[m.group(1)] = args[0]
    return macros


def expand_macros(s: str, macros: dict[str, str]) -> str:
    for _ in range(3):
        for name in sorted(macros, key=len, reverse=True):
            s = re.sub(r"\\" + name + r"(?![A-Za-z])\s?", lambda m, v=macros[name]: v.replace("\\", "\\\\") if False else v, s)
    return s


# --------------------------------------------------------------------------- bibliography
def load_bib(bib_path: Path) -> dict[str, dict]:
    p = subprocess.run(["pandoc", str(bib_path), "-f", "biblatex", "-t", "csljson"], capture_output=True, text=True)
    items = json.loads(p.stdout)
    return {it["id"]: it for it in items}


def _names(it: dict) -> list[str]:
    out = []
    for a in it.get("author", []):
        out.append(a.get("literal") or a.get("family", ""))
    return out


def short_cite(it: dict) -> tuple[str, str]:
    """(author text, year) as in APA in-text citations."""
    names = _names(it)
    if len(names) == 1:
        a = names[0]
    elif len(names) == 2:
        a = f"{names[0]} & {names[1]}"
    else:
        a = f"{names[0]} et al."
    year = str(it.get("issued", {}).get("date-parts", [[""]])[0][0])
    return a, year


def apa_reference(it: dict) -> str:
    names = []
    for a in it.get("author", []):
        if a.get("literal"):
            names.append(a["literal"])
        else:
            given = " ".join(f"{g[0]}." for g in re.split(r"[ \-]+", a.get("given", "")) if g)
            names.append(f"{a.get('family', '')}, {given}")
    if len(names) > 2:
        auth = ", ".join(names[:-1]) + ", & " + names[-1]
    else:
        auth = " & ".join(names)
    year = short_cite(it)[1]
    title = html.escape(it.get("title", "")).rstrip(".")
    cont = html.escape(it.get("container-title", ""))
    vol, iss, pages = it.get("volume", ""), it.get("issue", ""), it.get("page", "")
    t = it.get("type", "")
    s = f"{html.escape(auth)} ({year}). "
    if t in ("article-journal", "paper-conference", "chapter") and cont:
        s += f"{title}. <em>{cont}</em>"
        if vol:
            s += f", <em>{html.escape(str(vol))}</em>"
            if iss:
                s += f"({html.escape(str(iss))})"
        if pages:
            s += f", {html.escape(pages.replace('--', '\u2013'))}"
        s += "."
    elif t == "book":
        s += f"<em>{title}</em>. {html.escape(it.get('publisher', ''))}."
    else:
        s += f"<em>{title}</em>."
        if it.get("publisher"):
            s += f" {html.escape(it['publisher'])}."
    link = ""
    if it.get("DOI"):
        link = f"https://doi.org/{it['DOI']}"
    elif it.get("URL"):
        link = it["URL"]
    if link:
        s += f' <a href="{html.escape(link)}">{html.escape(link)}</a>'
    return s


def resolve_cites(text: str, bib: dict[str, dict]) -> str:
    """Replace the citation markers with links to the reference list."""

    def link(key: str, mode: str, first: bool = True) -> str:
        it = bib.get(key.strip())
        if not it:
            return html.escape(key)
        a, y = short_cite(it)
        label = f"{html.escape(a)} ({y})" if mode == "t" else f"{html.escape(a)}, {y}"
        return f'<a class="cite" href="{BASE}parents/research/#ref-{key.strip()}">{label}</a>'

    def sub(m):
        mode, keys = m.group(1), m.group(2).split(",")
        parts = [link(k, mode) for k in keys]
        if mode == "p":
            return "(" + "; ".join(parts) + ")"
        return "; ".join(parts)

    return re.sub(r"\u27e6cite:([tp]):([^\u27e7]*)\u27e7", sub, text)


def tex_fragment_to_html(tex: str, macros: dict[str, str], bib: dict[str, dict]) -> str:
    tex = tex.strip()
    tex = re.sub(r"\\textcite\{([^}]*)\}", lambda m: f"\u27e6cite:t:{m.group(1)}\u27e7", tex)
    tex = re.sub(r"\\parencite\{([^}]*)\}", lambda m: f"\u27e6cite:p:{m.group(1)}\u27e7", tex)
    tex = expand_macros(tex, macros)
    tex = tex.replace("\\textperiodcentered", "\u00b7")
    tex = re.sub(r"\\(quad|qquad|enspace|medskip|smallskip|par)(?![A-Za-z])", " ", tex)
    return resolve_cites(pandoc_html(tex), bib)


# --------------------------------------------------------------------------- frames
FRAME_RE = re.compile(r"\\begin\{frame\}(?:\[[^\]]*\])?(?:\{((?:[^{}]|\{[^{}]*\})*)\})?(.*?)\\end\{frame\}", re.S)


def split_items(doc: str):
    """Yield ('kicker', text) | ('frame', title, body) | ('section', title) in document order."""
    # drop the \levelslide definition (it opens a frame without closing it)
    i = doc.find("\\newcommand{\\levelslide}")
    if i >= 0:
        _, end = read_args(doc, doc.find("[9]", i) + 3, 1)
        doc = doc[:i] + doc[end:]
    # expand \levelslide invocations into ordinary frames (title + the arguments as body)
    out, pos = [], 0
    for m in re.finditer(r"\\levelslide(?![A-Za-z])", doc):
        args, end = read_args(doc, m.end(), 9)
        out.append(doc[pos : m.start()])
        out.append("\\begin{frame}{Level %s: %s}%s" % (args[0], args[1], "\n".join(args[3:9])))
        pos = end
    out.append(doc[pos:])
    doc = "".join(out)
    pat = re.compile(r"\\kicker\{([^}]*)\}|\\sectionslide\{[^}]*\}\{([^}]*)\}\{[^}]*\}|\\begin\{frame\}")
    pos = 0
    for m in pat.finditer(doc):
        if m.start() < pos:
            continue
        if m.group(1) is not None:
            yield ("kicker", m.group(1))
            pos = m.end()
        elif m.group(2) is not None:
            yield ("section", m.group(2))
            pos = m.end()
        else:
            fm = FRAME_RE.match(doc, m.start())
            if fm:
                yield ("frame", (fm.group(1) or "").strip(), fm.group(2))
                pos = fm.end()


def cmd_args(body: str, name: str, n: int) -> list[str] | None:
    m = re.search(r"\\" + name + r"(?![A-Za-z])", body)
    if not m:
        return None
    args, _ = read_args(body, m.end(), n)
    return args if len(args) == n else None


def build(manifest: dict, gen: Path, pub: Path, warnings: list[str], skip_pdfs: bool = False) -> None:
    pp = manifest["public"]["parents"]
    src = (ROOT / pp["source"]).read_text(encoding="utf-8")
    shared = (ROOT / pp["shared"]).read_text(encoding="utf-8")
    macros = parse_newcommands(shared)
    bib = load_bib(ROOT / pp["bib"])
    deck = ROOT / pp["deck"]
    if not deck.exists():
        subprocess.run(["make", "-C", str(ROOT / "parents"), "deck", "handout"], check=True, capture_output=True)
    handout = ROOT / pp["handout"]
    if not handout.exists():
        subprocess.run(["make", "-C", str(ROOT / "parents"), "handout"], check=True, capture_output=True)

    doc = src[src.index("\\begin{document}") + len("\\begin{document}") : src.index("\\end{document}")]
    doc = re.sub(r"(?m)^\s*%.*$", "", doc)
    kicker, slides, page = "", [], 0
    appendix = False
    for item in split_items(doc):
        if item[0] == "kicker":
            kicker = item[1]
            continue
        if item[0] == "section":
            page += 1
            appendix = True
            slides.append({"n": page, "title": item[1], "kicker": "", "section": True, "appendix": True})
            continue
        _, title, body = item
        page += 1
        title = title or "Why Coding?"
        title = expand_macros(title, macros)
        is_refs = title == "References"
        notes = cmd_args(body, "kcnotes", 3)
        source = cmd_args(body, "source", 1)
        s = {
            "n": page, "title": pandoc_html(title).replace("<p>", "").replace("</p>", "") if "\\" in title else title,
            "kicker": kicker if not appendix else "Appendix", "section": False, "appendix": appendix,
            "refs": is_refs,
            "source": tex_fragment_to_html(source[0], macros, bib) if source else "",
            "say": tex_fragment_to_html(notes[0], macros, bib) if notes and notes[0].strip() else "",
            "plain": tex_fragment_to_html(notes[1], macros, bib) if notes and notes[1].strip() else "",
            "qa": [],
        }
        if notes and notes[2].strip():
            for m in re.finditer(r"\\qa(?![A-Za-z])", notes[2]):
                qa, _ = read_args(notes[2], m.end(), 2)
                if len(qa) == 2:
                    s["qa"].append({"q": tex_fragment_to_html(qa[0], macros, bib).replace("<p>", "").replace("</p>", ""),
                                    "a": tex_fragment_to_html(qa[1], macros, bib).replace("<p>", "").replace("</p>", "")})
        slides.append(s)
        if is_refs:
            break
    # ------------------------------------------------------------------ slide images (from the built deck PDF)
    sd = pub / "slides"
    sd.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "build" / "site-cache" / "slides"
    tmp.mkdir(parents=True, exist_ok=True)
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(deck)], capture_output=True, text=True).stdout).group(1))
    subprocess.run(["pdftoppm", "-r", "96", "-png", str(deck), str(tmp / "s")], check=True)
    for s in slides:
        n = s["n"]
        files = sorted(tmp.glob("s-*.png"))
        png = tmp / f"s-{n:02d}.png" if (tmp / f"s-{n:02d}.png").exists() else files[n - 1]
        dst = sd / f"slide-{n:02d}.webp"
        Image.open(png).convert("RGB").save(dst, "WEBP", quality=82, method=6)
        txt = subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout", str(deck), "-"],
                             capture_output=True, text=True).stdout
        txt = re.sub(r"\s+", " ", txt).strip()
        txt = re.sub(r"\s*Kids Coding \| \d+\s*$", "", txt)
        s["image"] = f"{BASE}generated/slides/slide-{n:02d}.webp"
        s["alt"] = f"Slide {n}: " + (txt[:380].rsplit(" ", 1)[0] + "\u2026" if len(txt) > 380 else txt)
        s["w"], s["h"] = 1280, 720
    shutil.rmtree(tmp, ignore_errors=True)
    # ------------------------------------------------------------------ downloads
    dl = ROOT / "site" / "public" / "downloads" / "parents"
    dl.mkdir(parents=True, exist_ok=True)
    shutil.copy2(deck, dl / "why-coding-parent-deck.pdf")
    shutil.copy2(handout, dl / "why-coding-parent-handout.pdf")
    # ------------------------------------------------------------------ references, facts, lists
    refs = [{"key": k, "html": apa_reference(bib[k]), "sort": (short_cite(bib[k])[0].lower(), short_cite(bib[k])[1])}
            for k in bib]
    refs.sort(key=lambda r: r["sort"])
    used = set(re.findall(r"#ref-([A-Za-z0-9]+)", json.dumps(slides)))

    def lst(name: str) -> str:
        items = macros.get(name, "")
        return tex_fragment_to_html("\\begin{itemize}" + items + "\\end{itemize}", macros, bib)

    facts = {k: tex_fragment_to_html(macros[k], macros, bib).replace("<p>", "").replace("</p>", "")
             for k in ("LevelWeeks", "TotalWeeks", "SessionLength", "GroupSize", "Homework", "Equipment")}
    data = {
        "slides": slides, "references": [{"key": r["key"], "html": r["html"]} for r in refs],
        "facts": facts, "help_html": lst("HelpItems"), "safety_html": lst("SafetyItems"),
        "pdf": {"deck": {"url": f"{BASE}downloads/parents/why-coding-parent-deck.pdf",
                         "kb": (dl / "why-coding-parent-deck.pdf").stat().st_size // 1024},
                "handout": {"url": f"{BASE}downloads/parents/why-coding-parent-handout.pdf",
                            "kb": (dl / "why-coding-parent-handout.pdf").stat().st_size // 1024}},
        "pages": pages,
    }
    (gen).mkdir(parents=True, exist_ok=True)
    (gen / "parents.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
