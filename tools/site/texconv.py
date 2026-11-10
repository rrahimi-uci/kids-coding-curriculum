"""LaTeX (kidscode class) -> web HTML for the course website.

The .tex files stay the single source of truth. This module converts one file
at a time:

  1. protect code listings, then strip comments (keeping `%% alt:` lines),
  2. replace figures (TikZ pictures and Scratch scripts) by tokens and hand
     them to figures.py, which renders each one to an SVG with LuaLaTeX,
  3. rewrite the course's own macros and environments into forms Pandoc
     understands (callouts, vocabulary, checkboxes, fill-in lines ...),
  4. run Pandoc (LaTeX -> HTML5), then
  5. post-process the HTML with BeautifulSoup: callout boxes, syntax
     highlighting (Pygments, so no JavaScript is needed), figure tags with
     alt text, accessible tables, ids and a table of contents.

Everything that cannot be converted faithfully is recorded in `Result.warnings`
so the build can report it.
"""
from __future__ import annotations

import html
import re
import subprocess
from dataclasses import dataclass, field

from bs4 import BeautifulSoup, NavigableString
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

# --------------------------------------------------------------------------- tables

CALLOUTS = {
    # env name: (css class, label shown when the env has no title)
    "tip": ("tip", "Tip"),
    "safety": ("safety", "Safety"),
    "reflection": ("reflection", "Reflect"),
    "core": ("core", "Core"),
    "challenge": ("challenge", "Challenge"),
    "creative": ("creative", "Creative"),
    "exercise": ("exercise", "Exercise"),
    "bughunt": ("bughunt", "Bug hunt"),
    "selfcheck": ("selfcheck", "Self-check"),
    "vocab": ("vocab", "New words"),
}
CALLOUT_LABELS = {
    "tip": "Tip", "safety": "Safety", "reflection": "Reflect", "core": "Core",
    "challenge": "Challenge", "creative": "Creative", "exercise": "Exercise",
    "bughunt": "Bug hunt", "selfcheck": "Self-check", "vocab": "New words",
}
SELFCHECK_TITLE = "Self-check: check off each box when it is true"

SYMBOLS = {
    "faStar": "\u2605", "faCheck": "\u2713", "faTimes": "\u2717",
    "faCat": "", "faMagic": "", "faImage": "", "faBullhorn": "", "faPlayCircle": "",
    "faPython": "", "faPalette": "",
}
INLINE_MATH = {
    r"\rightarrow": "\u2192", r"\leftarrow": "\u2190", r"\times": "\u00d7", r"\div": "\u00f7",
    r"\leq": "\u2264", r"\geq": "\u2265", r"\neq": "\u2260", r"\square": "\u2610",
    r"\ldots": "\u2026", r"\approx": "\u2248",
}
OKABE = {
    "kcorange": "#E69F00", "kcsky": "#56B4E9", "kcgreen": "#009E73", "kcyellow": "#F0E442",
    "kcblue": "#0072B2", "kcvermillion": "#D55E00", "kcpurple": "#CC79A7",
    "kcblack": "#000000", "kcgray": "#555555", "kcpaper": "#FFFFFF",
}
C_BLOCKS = {"blockrepeat", "blockinfloop", "blockif", "blockifelse", "blockuntil", "blockforever"}

# --------------------------------------------------------------------------- brace helpers


def match_brace(s: str, i: int) -> int:
    """Index of the `}` matching the `{` at s[i]; -1 if unbalanced."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def read_args(s: str, i: int, n: int) -> tuple[list[str], int]:
    """Read n brace arguments starting at s[i]; returns (args, index after last)."""
    args = []
    for _ in range(n):
        while i < len(s) and s[i] in " \t\n":
            i += 1
        if i >= len(s) or s[i] != "{":
            break
        j = match_brace(s, i)
        if j < 0:
            break
        args.append(s[i + 1 : j])
        i = j + 1
    return args, i


def replace_cmd(s: str, name: str, nargs: int, fn) -> str:
    """Replace every \\name{..}{..} using fn(*args); handles nested braces."""
    out, pos = [], 0
    pat = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z])")
    while True:
        m = pat.search(s, pos)
        if not m:
            out.append(s[pos:])
            break
        out.append(s[pos : m.start()])
        args, end = read_args(s, m.end(), nargs)
        if len(args) < nargs:
            out.append(s[m.start() : m.end()])
            pos = m.end()
            continue
        out.append(fn(*args))
        pos = end
    return "".join(out)


def strip_comments(s: str) -> str:
    out = []
    for line in s.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


# --------------------------------------------------------------------------- scratch alt text


def _clean_label(t: str) -> str:
    t = re.sub(r"\\greenflag", "green flag", t)
    t = re.sub(r"\\turnleft\{?\}?", "left", t)
    t = re.sub(r"\\turnright\{?\}?", "right", t)
    t = re.sub(r"\\(?:ovalnum|ovalvariable|ovalsensing|ovaloperator|ovalmoreblocks|booloperator|boolsensing|selectmenu)\{([^{}]*)\}",
               lambda m: m.group(1), t)
    for _ in range(3):
        t = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", lambda m: m.group(1), t)
    t = re.sub(r"\\[A-Za-z]+", "", t)
    t = t.replace("{", "").replace("}", "").replace("~", " ").replace("\\", "")
    t = re.sub(r"\$([^$]*)\$", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def scratch_alt(body: str) -> str:
    """Describe a Scratch script in words, block by block, keeping C-block nesting."""

    def seq(s: str) -> list[str]:
        items, i = [], 0
        pat = re.compile(r"\\(block[a-z]+|initmoreblocks|namemoreblocks)(?![A-Za-z])")
        while True:
            m = pat.search(s, i)
            if not m:
                break
            name = m.group(1)
            nargs = {"blockifelse": 3}.get(name, 2 if name in C_BLOCKS else 1)
            args, end = read_args(s, m.end(), nargs)
            if not args:
                i = m.end()
                continue
            label = _clean_label(args[0])
            if len(args) > 1:
                inner = "; ".join(seq(args[1]))
                label += f" [ {inner} ]"
                if len(args) > 2:
                    label += f" else [ {'; '.join(seq(args[2]))} ]"
            items.append(label)
            i = end
        return items

    parts = seq(body)
    text = "; ".join(p for p in parts if p)
    return ("Scratch script: " + text) if text else "Scratch script"


# --------------------------------------------------------------------------- result type


@dataclass
class Figure:
    token: str
    kind: str  # tikz | scratch
    source: str
    alt: str
    key: str = ""


@dataclass
class Result:
    html: str = ""
    meta: dict = field(default_factory=dict)  # week, title, big idea ...
    objectives: list[str] = field(default_factory=list)
    vocab: list[tuple[str, str]] = field(default_factory=list)
    toc: list[tuple[int, str, str]] = field(default_factory=list)  # (level, id, text)
    figures: list[Figure] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    exercise_links: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- preprocessing

CODE_ENVS = ("pycode", "outputcode", "shellcode")


def extract_code(s: str, store: list[tuple[str, str, str, str]]) -> str:
    """Pull code listings out first so later regexes cannot damage them."""
    pat = re.compile(r"\\begin\{(pycode|outputcode|shellcode|cs|sheetcode)\}(?:\[([^\]]*)\])?\n?(.*?)\\end\{\1\}", re.S)

    def sub(m):
        token = f"CODEBLOCKTOKEN{len(store):04d}X"
        kind = "pycode" if m.group(1) in ("cs", "sheetcode") else m.group(1)
        store.append((token, kind, m.group(2) or "", m.group(3).rstrip("\n")))
        return f"\n\n{token}\n\n"

    return pat.sub(sub, s)


def extract_figures(s: str, figs: list[Figure], file_label: str) -> str:
    """Replace tikzpicture / scratch environments by tokens; attach `%% alt:` text."""
    pat = re.compile(
        r"(?P<alt>^[ \t]*%%[ \t]*alt:[ \t]*(?P<alt_text>[^\n]*)$)"
        r"|(?P<fig>\\begin\{(?P<env>tikzpicture|scratch)\}.*?\\end\{(?P=env)\})",
        re.S | re.M,
    )
    out, pos, pending = [], 0, None
    for m in pat.finditer(s):
        out.append(s[pos : m.start()])
        pos = m.end()
        if m.group("alt") is not None:
            pending = m.group("alt_text").strip()
            continue
        src, env = m.group("fig"), m.group("env")
        token = f"FIGURETOKEN{len(figs):04d}X"
        if env == "scratch":
            alt = pending or scratch_alt(src)
        else:
            alt = pending or ""
        figs.append(Figure(token, "tikz" if env == "tikzpicture" else env, src, alt))
        pending = None
        out.append(token)
    out.append(s[pos:])
    return "".join(out)


def simple_math(s: str) -> str:
    s = re.sub(r"\$\s*(-?)(\d+(?:\.\d+)?)\s*\$", lambda m: ("\u2212" if m.group(1) else "") + m.group(2), s)
    s = re.sub(r"\$\s*(\\[a-z]+)\s*\$", lambda m: INLINE_MATH.get(m.group(1), m.group(0)), s)
    return s


def split_document(tex: str) -> str:
    """Standalone documents (project briefs, extras): keep the body and expand the file's own
    zero-argument macros (for example \\lvA or \\crccard) defined in its preamble."""
    if "\\begin{document}" not in tex:
        return tex
    pre, rest = tex.split("\\begin{document}", 1)
    body = rest.split("\\end{document}", 1)[0]
    macros: dict[str, str] = {}
    for m in re.finditer(r"\\newcommand\{\\([A-Za-z]+)\}\s*\{", pre):
        j = match_brace(pre, m.end() - 1)
        if j > 0:
            macros.setdefault(m.group(1), pre[m.end() : j])
    for _ in range(2):
        for name in sorted(macros, key=len, reverse=True):
            body = re.sub(r"\\" + name + r"(?![A-Za-z])\s?", lambda mm, v=macros[name]: v.replace("\\", "\\\\") if False else v, body)
    return body


def expand_sheet_macros(s: str) -> str:
    """Macros of the cheat sheets: inline Scratch blocks, command tables, category rows."""
    s = replace_cmd(s, "sbk", 1, lambda a: "\\begin{scratch}[scale=0.58]" + a + "\\end{scratch} ")
    s = replace_cmd(s, "cshead", 1, lambda a: "\n\n\\subsection{" + a + "}\n\n")
    s = replace_cmd(s, "cmdhead", 1, lambda a: "\n\n\\subsection{" + a + "}\n\n")
    s = replace_cmd(s, "cat", 4, lambda c, t, tip, blocks: "\n\n\\subsection{" + t + "}\n\n" + tip + "\n\n" + blocks + "\n\n")
    s = re.sub(r"\\begin\{cmdtable\}(?:\[[^\]]*\])?\{([^}]*)\}", lambda m: "\n\n\\subsection{" + m.group(1) + "}\n\n\\begin{tabular}{ll}\n", s)
    s = s.replace("\\end{cmdtable}", "\\end{tabular}\n")
    if "\\cat{" in s or "\\begin{longtable}" in s and "\\subsection{" in s:
        while True:  # the \\cat rows replace the table wrapper
            m = re.search(r"\\begin\{longtable\}", s)
            if not m:
                break
            _, end = read_args(s, m.end(), 1)
            s = s[: m.start()] + s[end:]
        s = s.replace("\\end{longtable}", "")
    s = re.sub(r"\\(begin|end)\{multicols\}(\{\d+\})?", "", s)
    s = replace_cmd(s, "scalebox", 2, lambda a, b: b)
    s = re.sub(r"\\(rowcolor|cellcolor|columncolor)(\[[^\]]*\])?\{[^}]*\}", "", s)
    s = re.sub(r"\\(needspace|columnbreak|pagebreak|allowbreak|raggedcolumns|nopagebreak)(\{[^}]*\})?", "", s)
    return s


def prepare(tex: str, file_label: str, week_hint: str = "") -> tuple[str, Result]:
    res = Result()
    code_store: list = []
    tex = split_document(tex)
    title = re.search(r"\\kctitle\{", tex)
    if title:
        args, end = read_args(tex, title.end() - 1, 2)
        if len(args) == 2:
            res.meta = {"title": args[0].strip(), "subtitle": args[1].strip()}
            tex = tex[: title.start()] + tex[end:]
    tex = expand_sheet_macros(tex)
    s = extract_code(tex, code_store)
    s = extract_figures(s, res.figures, file_label)
    s = strip_comments(s)

    # metadata banners
    m = re.search(r"\\(chapterweek|homeworkweek)\{([^}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}", s)
    if m:
        res.meta = {"week": m.group(2).strip(), "title": m.group(3).strip(), "idea": m.group(4).strip()}
        s = s[: m.start()] + s[m.end() :]
    s = s.replace(r"\namedateline", "")

    # plain formatting commands that mean nothing on the web
    s = re.sub(r"\\(small|large|Large|LARGE|huge|Huge|footnotesize|scriptsize|normalsize|centering|raggedright|"
               r"noindent|medskip|smallskip|bigskip|hfill|quad|qquad|clearpage|newpage|bfseries|ttfamily|itshape)(?![A-Za-z])", " ", s)
    s = re.sub(r"\\(hspace|vspace)\*?\{[^}]*\}", " ", s)
    s = re.sub(r"\\renewcommand\{\\arraystretch\}\{[^}]*\}", "", s)
    s = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}", "", s)
    s = re.sub(r"\\\\\[[^\]]*\]", r"\\\\", s)

    # icons / symbols
    for name, sym in SYMBOLS.items():
        s = re.sub(r"\\" + name + r"(?![A-Za-z])\s?", sym, s)
    s = re.sub(r"\\fa[A-Z][A-Za-z]*(\[[a-z]*\])?\s?", "", s)
    s = simple_math(s)
    s = re.sub(r"\\tickbox", "\u2610", s)
    s = re.sub(r"\\ldots", "\u2026", s)

    # inline macros -> markers resolved after Pandoc
    s = replace_cmd(s, "menu", 1, lambda a: f"\u27e6m\u27e7{a}\u27e6/m\u27e7")
    s = replace_cmd(s, "keys", 1, lambda a: f"\u27e6k\u27e7{a}\u27e6/k\u27e7")
    s = replace_cmd(s, "swatch", 1, lambda a: f"\u27e6sw:{a}\u27e7")
    def _tt(code: str) -> str:
        code = re.sub(r"([_#%&$])", r"\\\1", code.replace("\\_", "_"))
        return r"\texttt{" + code + "}"

    # "\_<name>" makes Pandoc swallow "<name>" as an HTML tag, so angle brackets inside \texttt become macros
    s = re.sub(r"\\texttt\{([^{}]*)\}",
               lambda m: "\\texttt{" + m.group(1).replace("<", "\\textless{}").replace(">", "\\textgreater{}") + "}", s)
    s = re.sub(r"\\py\|([^|\n]*)\|", lambda m: _tt(m.group(1)), s)
    s = replace_cmd(s, "py", 1, _tt)
    s = replace_cmd(s, "answerlines", 1, lambda a: f"\n\nLINESTOKEN{a.strip()}X\n\n")
    s = replace_cmd(s, "answerspace", 1, lambda a: "\n\nLINESTOKEN3X\n\n")
    s = re.sub(r"\\rule\{[^}]*\}\{[^}]*\}", "\u27e6blank\u27e7", s)
    s = replace_cmd(s, "fbox", 1, lambda a: a)
    s = replace_cmd(s, "makebox", 1, lambda a: a)

    # vocabulary: \begin{vocab} \vocabword{T}{D} ... -> description list
    s = replace_cmd(s, "vocabword", 2, lambda t, d: "\\item[" + t + "] " + d + "\n")
    s = re.sub(r"\\begin\{vocab\}", r"\\begin{vocab}\n\\begin{description}", s)
    s = re.sub(r"\\end\{vocab\}", r"\\end{description}\n\\end{vocab}", s)

    # self-check lists: wrap items in an itemize list
    for env in ("selfcheck", "checklist"):
        s = re.sub(r"\\begin\{" + env + r"\}", r"\\begin{" + env + r"}\n\\begin{itemize}", s)
        s = re.sub(r"\\end\{" + env + r"\}", r"\\end{itemize}\n\\end{" + env + "}", s)

    # callout titles: \begin{tip}[Title] -> div + marker line
    exercise_counter = [0]

    def begin_env(m):
        env, title = m.group(1), m.group(2)
        if env == "exercise":
            exercise_counter[0] += 1
            n = f"{res.meta.get('week', week_hint)}.{exercise_counter[0]}"
            title = f"{n}: {title}" if title else n
        if env == "selfcheck" and not title:
            title = SELFCHECK_TITLE
        if title:
            return f"\\begin{{{env}}}\n\nCALLOUTTITLEBEGIN {title} CALLOUTTITLEEND\n\n"
        return f"\\begin{{{env}}}\n"

    s = re.sub(r"\\begin\{(" + "|".join(CALLOUTS) + r")\}(?:\[((?:[^\[\]]|\[[^\]]*\])*)\])?", begin_env, s)
    s = re.sub(r"\\begin\{(itemize|enumerate)\}\[[^\]]*\]", r"\\begin{\1}", s)
    s = re.sub(r"\\begin\{minipage\}(\[[^\]]*\])?\{[^}]*\}", r"\\begin{minipage}", s)

    # restore code tokens as paragraphs (they are swapped for <pre> after Pandoc)
    res._code_store = code_store  # type: ignore[attr-defined]
    return s, res


# --------------------------------------------------------------------------- pandoc

_NOHL: list[str] = []


def no_highlight() -> list[str]:
    """Pandoc >= 3.8 renamed --no-highlight to --syntax-highlighting=none."""
    if not _NOHL:
        out = subprocess.run(["pandoc", "--version"], capture_output=True, text=True).stdout
        m = re.search(r"pandoc (\d+)\.(\d+)", out)
        new = bool(m) and (int(m.group(1)), int(m.group(2))) >= (3, 8)
        _NOHL.append("--syntax-highlighting=none" if new else "--no-highlight")
    return list(_NOHL)



def run_pandoc(tex: str) -> str:
    p = subprocess.run(
        ["pandoc", "-f", "latex", "-t", "html5", "--wrap=none", "--shift-heading-level-by=1",
         *no_highlight(), "--mathml"],
        input=tex, capture_output=True, text=True,
    )
    if p.returncode != 0:
        raise RuntimeError("pandoc failed: " + p.stderr[:400])
    return p.stdout


# --------------------------------------------------------------------------- post-processing

_FORMATTER = HtmlFormatter(nowrap=True, classprefix="tok-")


def highlight_python(code: str) -> str:
    return highlight(code, PythonLexer(), _FORMATTER).rstrip("\n")


def slugify(text: str) -> str:
    t = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return t or "section"


def post_process(raw_html: str, res: Result, fig_urls: dict[str, tuple[str, int, int]],
                 exercise_pages: dict[str, str]) -> str:
    soup = BeautifulSoup(raw_html, "lxml")
    body = soup.body or soup
    raw_code: dict[str, str] = {}

    # ---- code blocks
    def replace_token(token: str, make):
        """Swap a placeholder paragraph (or a bare table-cell string) for a new element."""
        for node in body.find_all(string=re.compile(re.escape(token))):
            holder = node.parent
            if holder.name == "p" and holder.get_text(strip=True) == token:
                holder.replace_with(make())
                return True
            if str(node).strip() == token:
                node.replace_with(make())
                return True
        return False

    for tok, kind, title, code in getattr(res, "_code_store", []):
        def make_code(kind=kind, title=title, code=code):
            wrap = soup.new_tag("div", attrs={"class": f"code-block code-{kind}"})
            if title:
                cap = soup.new_tag("p", attrs={"class": "code-title"})
                cap.string = title
                wrap.append(cap)
            pre = soup.new_tag("pre", attrs={"tabindex": "0"})
            c = soup.new_tag("code")
            if kind == "pycode":
                c["class"] = "language-python"
                # inserted as raw HTML after serialization: BeautifulSoup would collapse the indentation
                marker = f"HIGHLIGHTMARKER{len(raw_code)}X"
                raw_code[marker] = highlight_python(code)
                c.string = marker
            else:
                c.string = code
            pre.append(c)
            wrap.append(pre)
            return wrap

        if not replace_token(tok, make_code):
            res.warnings.append(f"code token {tok} not found in HTML")

    # ---- callouts
    for env, (cls, _) in CALLOUTS.items():
        for div in body.find_all("div", class_=env):
            first = div.find("p")
            title = ""
            if first and "CALLOUTTITLEBEGIN" in first.get_text():
                t = first.get_text()
                title = re.sub(r"\s+", " ", t.split("CALLOUTTITLEBEGIN", 1)[1].split("CALLOUTTITLEEND", 1)[0]).strip()
                first.decompose()
            div["class"] = ["callout", f"callout-{cls}"]
            div["role"] = "note"
            label = CALLOUT_LABELS[env]
            head = soup.new_tag("p", attrs={"class": "callout-title"})
            lab = soup.new_tag("span", attrs={"class": "callout-label"})
            lab.string = label
            head.append(lab)
            if title and title != label:
                tt = soup.new_tag("span", attrs={"class": "callout-heading"})
                # print edition: tick boxes; the web page is for reading, so the title asks the question instead
                tt.string = title.replace("check off each box when it is true", "read each line and ask: is it true for me?")
                head.append(tt)
            div.insert(0, head)
            if env == "vocab":
                for dl in div.find_all("dl"):
                    dl["class"] = "vocab-list"
                    for dt in dl.find_all("dt"):
                        dd = dt.find_next_sibling("dd")
                        res.vocab.append((dt.get_text(" ", strip=True),
                                          dd.get_text(" ", strip=True) if dd else ""))
    for div in body.find_all("div", class_="checklist"):
        div["class"] = ["checklist"]
    # Self-check and checklist items are ordinary list items: the page is for reading, not for ticking.
    for li in body.select(".callout-selfcheck li, .checklist li"):
        for p in li.find_all("p", recursive=False):
            p.unwrap()

    # ---- inline markers
    def rewrite_text(node):
        t = str(node)
        if not any(x in t for x in ("\u27e6", "LINESTOKEN")):
            return
        t = html.escape(t, quote=False)
        t = re.sub(r"\u27e6m\u27e7(.*?)\u27e6/m\u27e7", r'<span class="menu">\1</span>', t)
        t = re.sub(r"\u27e6k\u27e7(.*?)\u27e6/k\u27e7", r"<kbd>\1</kbd>", t)
        t = re.sub(r"\u27e6blank\u27e7", '<span class="blank"><span class="visually-hidden">(blank to fill in)</span></span>', t)

        def sw(m):
            col = OKABE.get(m.group(1), "#888")
            return f'<span class="swatch" style="background:{col}" title="{m.group(1)[2:]}"></span>'

        t = re.sub(r"\u27e6sw:([a-z]+)\u27e7", sw, t)
        node.replace_with(BeautifulSoup("<span>" + t + "</span>", "lxml").span)

    for node in list(body.find_all(string=True)):
        if isinstance(node, NavigableString):
            rewrite_text(node)
    for span in list(body.find_all("span")):
        if not span.attrs:
            span.unwrap()

    for p in list(body.find_all("p")):
        m = re.fullmatch(r"LINESTOKEN(\d+)X", p.get_text(strip=True))
        if m:
            d = soup.new_tag("div", attrs={"class": "write-lines", "data-lines": m.group(1), "aria-hidden": "true"})
            d["style"] = f"--lines:{m.group(1)}"
            p.replace_with(d)

    # ---- figures
    for fig in res.figures:
        url = fig_urls.get(fig.token)
        if not url:
            continue
        src, w, h = url
        scale = {"scratch": 1.75, "tikz": 1.4}.get(fig.kind, 1.0)  # PDF-size figures are small on screens
        w, h = round(w * scale), round(h * scale)
        img = soup.new_tag("img", attrs={"src": src, "alt": fig.alt, "width": str(w), "height": str(h),
                                         "loading": "lazy", "decoding": "async"})
        img["class"] = f"fig fig-{fig.kind}"
        placed = False
        for p in body.find_all("p"):
            if p.get_text(strip=True) == fig.token and not p.find("img"):
                f = soup.new_tag("figure", attrs={"class": f"figure figure-{fig.kind}"})
                f.append(img)
                p.replace_with(f)
                placed = True
                break
        if not placed:
            for node in body.find_all(string=re.compile(re.escape(fig.token))):
                parts = str(node).split(fig.token)
                new = BeautifulSoup("<span></span>", "lxml").span
                new.append(NavigableString(parts[0]))
                img["class"] = f"fig fig-{fig.kind} fig-inline"
                new.append(img)
                new.append(NavigableString(parts[1] if len(parts) > 1 else ""))
                node.replace_with(new)
                new.unwrap()
                placed = True
                break
        if not placed:
            res.warnings.append(f"figure token {fig.token} not placed")

    # ---- tables: scrollable, named, focusable region (WCAG)
    for tb in body.find_all("table"):
        for attr in ("style", "class"):
            tb.attrs.pop(attr, None)
        wrap = soup.new_tag("div", attrs={"class": "table-wrap", "tabindex": "0"})
        tb.wrap(wrap)
        for colgroup in tb.find_all("colgroup"):
            colgroup.decompose()
        for th in tb.find_all("th"):
            th.attrs.pop("style", None)
            th["scope"] = "col"
        for td in tb.find_all(["td"]):
            td.attrs.pop("style", None)
        if not tb.find("caption"):
            pass

    # ---- exercise folders become links
    for code in body.find_all("code"):
        txt = code.get_text(strip=True)
        m = re.fullmatch(r"(week\d\d)/((?:ex|hw)-[a-z0-9-]+)", txt)
        if m and txt in exercise_pages:
            a = soup.new_tag("a", href=exercise_pages[txt])
            code.wrap(a)
            res.exercise_links.append(txt)

    # ---- the self-check script is not published on the web: drop list items that depend on it
    for li in list(body.find_all("li")):
        if "check_my_work" in li.get_text():
            li.decompose()
            res.warnings.append("info: removed a self-check list item that mentions check_my_work.py")
    cleanup_selfcheck_sentences(body)

    # ---- ids and table of contents
    seen: set[str] = set()
    for el in body.find_all(["section", "div"], id=True):
        del el["id"]  # Pandoc copies a heading id onto wrapper elements: keep ids unique
    for h in body.find_all(["h2", "h3"]):
        text = h.get_text(" ", strip=True)
        sid = re.sub(r"[^A-Za-z0-9_-]+", "-", h.get("id") or slugify(text)).strip("-") or "section"
        if not sid[0].isalpha():
            sid = "s-" + sid
        base, k = sid, 2
        while sid in seen:
            sid = f"{base}-{k}"
            k += 1
        seen.add(sid)
        h["id"] = sid
        res.toc.append((int(h.name[1]), sid, text))

    # leftover tokens = something we failed to convert
    out = body.decode_contents()
    for marker, code_html in raw_code.items():
        out = out.replace(marker, code_html)
    for bad in ("CODEBLOCKTOKEN", "FIGURETOKEN", "CALLOUTTITLE", "LINESTOKEN"):
        if bad in out:
            res.warnings.append(f"unconverted token left in HTML: {bad}")
    for bad in ("\\begin", "\\end{", "\\texttt", "\\textbf", "\\enquote"):
        if bad in out:
            res.warnings.append(f"raw LaTeX left in HTML: {bad}")
    return out


_SELF_RE = [
    re.compile(r"\s*Check(?: your work)?:\s*open\s*check_my_work\.py\s*and press Run\.?", re.I),
    re.compile(r"\s*(?:Then|and then)?\s*run\s*check_my_work\.py\.?", re.I),
    re.compile(r"\s*(?:Then )?open\s*check_my_work\.py\s*and press Run\.?", re.I),
]


def cleanup_selfcheck_sentences(body) -> None:
    """check_my_work.py is not published (it needs the private tests); drop the sentence."""
    pat = re.compile(r"\s*(?:Then\s+)?(?:Check(?: your work)?:\s*)?(?:then\s+)?(?:open|run)\s*<code>check_my_work\.py</code>"
                     r"(?:\s*and press\s*(?:<strong>)?Run(?:</strong>)?)?\.?", re.I)
    for node in list(body.find_all(string=re.compile("check_my_work"))):
        p = node.find_parent(["p", "li"])
        if p is None:
            continue
        inner = p.decode_contents()
        new = pat.sub("", inner)
        if new != inner:
            p.clear()
            for child in list(BeautifulSoup(new, "html.parser").children):
                p.append(child)


# --------------------------------------------------------------------------- public entry point


def convert_file(path, level: int, fig_dir, fig_url_prefix: str, exercise_pages: dict[str, str] | None = None,
                 week_hint: str = "") -> Result:
    from pathlib import Path

    from . import figures

    tex = Path(path).read_text(encoding="utf-8")
    prepared, res = prepare(tex, str(path), week_hint)
    for f in res.figures:
        if f.kind == "tikz" and not f.alt:
            res.warnings.append(f"{Path(path).name}: TikZ figure without `%% alt:` text ({f.token})")
    fig_urls = figures.render(res.figures, level, Path(fig_dir), fig_url_prefix)
    raw = run_pandoc(prepared)
    res.html = post_process(raw, res, fig_urls, exercise_pages or {})
    return res
