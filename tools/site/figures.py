"""Render the TikZ pictures and Scratch scripts of the course to SVG.

Each figure is compiled with LuaLaTeX using the course's own class
(shared/latex/kidscode.cls), so it looks exactly like the PDF. Results are
cached by a hash of the figure source, so a rebuild only recompiles figures
that changed.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLASS_DIR = ROOT / "shared" / "latex"

PREAMBLE = r"""\documentclass[%(classopts)s]{kidscode}
\pagestyle{empty}
\newsavebox{\figbox}
\newcommand{\figpage}[1]{\savebox{\figbox}{#1}%%
  \pagewidth=\dimexpr\wd\figbox+2pt\relax \pageheight=\dimexpr\ht\figbox+\dp\figbox+2pt\relax
  \shipout\vbox{\kern-1in\hbox{\kern-1in\kern1pt\raise1pt\box\figbox}}}
%(preamble)s
\begin{document}
"""


def fig_key(kind: str, source: str, classopts: str, preamble: str = "") -> str:
    return hashlib.sha1(f"{kind}|{classopts}|{preamble}|{source}".encode()).hexdigest()[:12]


def svg_size(path: Path) -> tuple[int, int]:
    head = path.read_text(encoding="utf-8", errors="ignore")[:600]
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', head)
    if m:
        return round(float(m.group(1))), round(float(m.group(2)))
    return 400, 300


def render(figs, classopts: str, out_dir: Path, url_prefix: str, preamble: str = "") -> dict[str, tuple[str, int, int]]:
    """figs: list of objects with .token .kind .source ; returns token -> (url, w, h).

    classopts are the kidscode class options of the level, e.g. "track=junior,level=1", so a figure
    uses the same colors and fonts as in that level's PDF. preamble holds definitions from the source
    document's own preamble that its figures use (its color names, for example)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    result: dict[str, tuple[str, int, int]] = {}
    todo: list[tuple[str, object]] = []
    for f in figs:
        f.key = fig_key(f.kind, f.source, classopts, preamble)
        svg = out_dir / f"{f.key}.svg"
        if svg.exists():
            w, h = svg_size(svg)
            result[f.token] = (f"{url_prefix}/{f.key}.svg", w, h)
        else:
            todo.append((f.key, f))
    uniq: dict[str, object] = {}
    for key, f in todo:
        uniq.setdefault(key, f)
    if not uniq:
        return result
    with tempfile.TemporaryDirectory(prefix="figs-") as tmp:
        tmpd = Path(tmp)
        body = [PREAMBLE % {"classopts": classopts, "preamble": preamble}]
        order = list(uniq)
        for key in order:
            body.append("\\figpage{" + uniq[key].source + "}\n")
        body.append("\\end{document}\n")
        (tmpd / "figs.tex").write_text("".join(body), encoding="utf-8")
        env = dict(os.environ, TEXINPUTS=f"{CLASS_DIR}//:" + os.environ.get("TEXINPUTS", ""))
        p = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "figs.tex"],
                           cwd=tmpd, env=env, capture_output=True, text=True)
        if p.returncode != 0:
            log = (tmpd / "figs.log").read_text(errors="ignore") if (tmpd / "figs.log").exists() else p.stdout
            raise RuntimeError("figure compile failed:\n" + "\n".join(
                l for l in log.splitlines() if l.startswith("!") or "figs.tex:" in l)[:1500])
        for i, key in enumerate(order, start=1):
            svg = out_dir / f"{key}.svg"
            subprocess.run(["pdftocairo", "-svg", "-f", str(i), "-l", str(i), str(tmpd / "figs.pdf"), str(svg)],
                           check=True)
    for key, f in todo:
        svg = out_dir / f"{key}.svg"
        w, h = svg_size(svg)
        result[f.token] = (f"{url_prefix}/{key}.svg", w, h)
    return result
