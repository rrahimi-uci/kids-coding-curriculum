#!/usr/bin/env python3
"""Generate the website data from the course sources.

    python3 -m tools.site.build [--levels 1 2 3] [--skip-pdfs]

Reads only what site/manifest.yml marks public; writes HTML fragments, JSON data, SVG figures and
downloads into site/src/generated/ and site/public/generated/ (both git-ignored). The Astro project in
site/ turns that into pages. See docs/SITE-DESIGN.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import glob
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from . import exercises as exmod
from . import extras as extmod
from . import parents as parentsmod
from . import pdfs, syllabus, texconv

ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / "site" / "src" / "generated"
PUB = ROOT / "site" / "public" / "generated"
BASE = "%BASE%"  # replaced by the Astro layer with the real base path


def load_manifest() -> dict:
    return yaml.safe_load((ROOT / "site" / "manifest.yml").read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def git_info() -> dict:
    def run(*a):
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()

    return {"commit": run("rev-parse", "--short", "HEAD") or "dev",
            "date": run("log", "-1", "--format=%cs") or dt.date.today().isoformat()}


def extract_objectives(html: str) -> tuple[list[str], str]:
    """Take the 'What you will learn' list out of the chapter body; returns (items, remaining html)."""
    soup = BeautifulSoup(html, "html.parser")
    for h in soup.find_all("h2"):
        if h.get_text(strip=True).lower().startswith("what you will"):
            nxt = h.find_next_sibling()
            ul = nxt.find("ul") if nxt is not None and nxt.name == "div" else nxt  # a checklist is wrapped in a div
            if ul is not None and ul.name == "ul":
                items = [re.sub(r"\s+", " ", li.get_text()).strip() for li in ul.find_all("li", recursive=False)]
                nxt.decompose()
                h.decompose()
                return items, str(soup)
    return [], html


def strip_vocab(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for d in soup.find_all("div", class_="callout-vocab"):
        d.decompose()
    return str(soup)


def plain(text: str) -> str:
    text = re.sub(r"\\texttt\{([^}]*)\}", r"\1", text)
    text = text.replace("---", "\u2014").replace("--", "\u2013").replace("\\&", "&")
    return re.sub(r"\\[A-Za-z]+\s?", "", text).strip()


def build_level(entry: dict, syl: dict, manifest: dict, args, warnings: list[str]) -> dict:
    n, d, slug = entry["number"], entry["dir"], entry["slug"]
    pub = manifest["public"]
    fig_dir = PUB / "fig" / slug
    fig_prefix = f"{BASE}generated/fig/{slug}"
    # --- exercises (public files only)
    ex_by_week: dict[int, list[dict]] = {}
    ex_pages: dict[str, str] = {}
    for dpath in sorted(glob.glob(str(ROOT / pub["exercise_dirs"].format(dir=d)))):
        dpath = Path(dpath)
        files = [f.name for f in dpath.iterdir() if any(fnmatch.fnmatch(f.name, pat) for pat in pub["exercise_files"])]
        ex = exmod.build_exercise(dpath, n, sorted(files), warnings)
        if not ex["hints"]:
            warnings.append(f"ERROR level {n}: exercise {ex['folder']} has no hints.md")
        ex_by_week.setdefault(ex["week"], []).append(ex)
        ex_pages[ex["folder"]] = f"{BASE}levels/{slug}/exercises/{ex['slug']}/"
        ex["url"] = ex_pages[ex["folder"]]
    # --- level documents (whole-level PDFs)
    level_dl: dict[str, dict] = {}
    if not args.skip_pdfs:
        pdf_map = pdfs.ensure_level_pdfs(d, ["student-workbook", "homework"])
        for stem, variants in pdf_map.items():
            for variant, src in variants.items():
                rel = f"downloads/{slug}/{slug}-{stem}{'-dyslexia' if variant == 'dyslexia' else ''}.pdf"
                dst = ROOT / "site" / "public" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                level_dl.setdefault(stem, {})[variant] = {"url": f"{BASE}{rel}", "kb": dst.stat().st_size // 1024}
    # --- weeks
    weeks = []
    syl_weeks = {w["n"]: w for w in syl[n]["weeks"]}
    for w in range(1, 13):
        nn = f"{w:02d}"
        wb = ROOT / pub["workbook"].format(dir=d).replace("week[0-9][0-9]", f"week{nn}")
        hw = ROOT / pub["homework"].format(dir=d).replace("week[0-9][0-9]", f"week{nn}")
        if not wb.exists():
            continue
        res = texconv.convert_file(wb, n, fig_dir, fig_prefix, ex_pages, week_hint=str(w))
        objectives, body = extract_objectives(res.html)
        body = strip_vocab(body)
        if not objectives:
            warnings.append(f"ERROR level {n} week {w}: no 'What you will learn' objectives found")
        warnings += [f"level {n} week {w}: {x}" for x in res.warnings]
        hw_html, hw_meta = "", {}
        if hw.exists():
            hres = texconv.convert_file(hw, n, fig_dir, fig_prefix, ex_pages, week_hint=str(w))
            hw_html, hw_meta = hres.html, hres.meta
            warnings += [f"level {n} week {w} homework: {x}" for x in hres.warnings]
        html_dir = GEN / "html" / slug
        html_dir.mkdir(parents=True, exist_ok=True)
        (html_dir / f"week-{nn}.html").write_text(body, encoding="utf-8")
        (html_dir / f"homework-{nn}.html").write_text(hw_html, encoding="utf-8")
        week_ex = sorted(ex_by_week.get(w, []), key=lambda e: (e["homework"], [int(x) for x in re.findall(r"\d+", e["number"])], e["folder"]))
        # downloads: week PDF + starter zip
        dl = {}
        if not args.skip_pdfs:
            rel = f"downloads/{slug}/week-{nn}.pdf"
            if pdfs.week_pdf(n, d, w, ROOT / "site" / "public" / rel, ROOT / "build" / "site-cache"):
                dl["pdf"] = {"url": f"{BASE}{rel}", "kb": (ROOT / "site" / "public" / rel).stat().st_size // 1024}
        zrel = f"downloads/{slug}/week-{nn}-starter-files.zip"
        starters = [e for e in week_ex if e["kind"] == "python"]
        if starters:
            zpath = ROOT / "site" / "public" / zrel
            zpath.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                for e in week_ex:
                    src_dir = ROOT / d / "exercises" / e["folder"]
                    z.writestr(f"{e['folder']}/README.md", e["readme_clean"])
                    for name in ["starter.py", *e["files"]]:
                        if (src_dir / name).exists():
                            z.write(src_dir / name, f"{e['folder']}/{name}")
            dl["starter"] = {"url": f"{BASE}{zrel}", "kb": max(1, zpath.stat().st_size // 1024)}
        sw = syl_weeks.get(w, {})
        weeks.append({
            "n": w, "slug": f"week-{nn}",
            "title": plain(res.meta.get("title") or ""), "idea": plain(res.meta.get("idea") or ""),
            "concepts": sw.get("concepts", ""), "unplugged": sw.get("unplugged", ""),
            "objectives": objectives, "vocab": [{"term": t, "def": df} for t, df in res.vocab],
            "toc": [{"level": lv, "id": i, "text": t} for lv, i, t in res.toc
                    if not t.lower().startswith("what you will")],
            "has_homework": bool(hw_html), "homework_title": plain(hw_meta.get("title", "")),
            "homework_note": plain(hw_meta.get("idea", "")),
            "exercises": [{k: e[k] for k in ("slug", "title", "number", "kind", "homework", "url")} for e in week_ex],
            "downloads": dl,
        })
    # exercise pages data
    for wk, exs in ex_by_week.items():
        for e in exs:
            e["url"] = ex_pages[e["folder"]]
            write_json(GEN / "exercises" / slug / f"{e['slug']}.json",
                       {k: v for k, v in e.items() if k != "readme_clean"})
            # raw starter files (only the public ones) for the download buttons
            out = ROOT / "site" / "public" / "downloads" / slug / "exercises" / e["slug"]
            src_dir = ROOT / d / "exercises" / e["folder"]
            for name in (["starter.py"] if e["kind"] == "python" else []) + list(e["files"]):
                out.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_dir / name, out / name)
    project = extmod.build_project(entry, manifest, GEN, fig_dir, warnings)
    extras = extmod.build_extras(entry, manifest, GEN, fig_dir, warnings)
    glossary = extras.pop("glossary")
    write_json(GEN / "glossary" / f"{slug}.json", glossary)
    extra_dl = extmod.level_pdfs(d, slug, ["project-brief", "cheat-sheet", "glossary", "parent-notes", "progress-tracker"],
                                 args.skip_pdfs)
    return {
        "number": n, "slug": slug, "dir": d, "name": syl[n]["name"], "languages": syl[n]["languages"],
        "tools": syl[n]["tools"], "goals": syl[n]["goals"], "project_title": syl[n]["project_title"],
        "project_html": syl[n]["project_html"], "published": entry["published"], "weeks": weeks,
        "project": project, "extras": extras, "glossary_count": len(glossary), "extra_downloads": extra_dl,
        "downloads": level_dl,
        "syllabus_weeks": [{"n": w["n"], "title": w["title"], "idea": w["idea"]} for w in syl[n]["weeks"]],
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", type=int, nargs="*", help="levels to convert (default: all published in manifest)")
    ap.add_argument("--skip-pdfs", action="store_true", help="do not build or copy PDF downloads")
    args = ap.parse_args(argv)
    manifest = load_manifest()
    syl = syllabus.parse()
    if GEN.exists():
        shutil.rmtree(GEN)
    GEN.mkdir(parents=True)
    (ROOT / "site" / "public" / "downloads").mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []
    levels = []
    for entry in manifest["levels"]:
        if args.levels is not None and entry["number"] not in args.levels:
            entry = dict(entry, published=False)
        elif args.levels is None and not entry["published"]:
            pass
        if entry["published"]:
            levels.append(build_level(entry, syl, manifest, args, warnings))
        else:
            n = entry["number"]
            levels.append({"number": n, "slug": entry["slug"], "dir": entry["dir"], "name": syl[n]["name"],
                           "languages": syl[n]["languages"], "tools": syl[n]["tools"], "goals": syl[n]["goals"],
                           "project_title": syl[n]["project_title"], "project_html": syl[n]["project_html"],
                           "published": False, "weeks": [], "downloads": {},
                           "syllabus_weeks": [{"n": w["n"], "title": w["title"], "idea": w["idea"]}
                                              for w in syl[n]["weeks"]]})
    write_json(GEN / "levels.json", levels)
    write_json(GEN / "resources.json", extmod.build_resources(manifest, GEN, warnings))
    parentsmod.build(manifest, GEN, PUB, warnings, skip_pdfs=args.skip_pdfs)
    info = git_info()
    version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else "0.0.0"
    changelog = ""
    if (ROOT / "CHANGELOG.md").exists():
        changelog = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none", "--shift-heading-level-by=2", "--id-prefix=changelog-"],
                                   input=(ROOT / "CHANGELOG.md").read_text(encoding="utf-8").split("\n", 1)[1],
                                   capture_output=True, text=True, check=True).stdout
    write_json(GEN / "site.json", {"version": version, "updated": info["date"], "commit": info["commit"],
                                   "changelog_html": changelog})
    errors = [w for w in warnings if w.startswith("ERROR") or "TikZ figure without" in w or "token" in w
              or "raw LaTeX" in w or "not placed" in w]
    infos = [w for w in warnings if w not in errors]
    print(f"site data built: {sum(len(l['weeks']) for l in levels)} week pages, "
          f"{sum(1 for _ in (GEN / 'exercises').rglob('*.json'))} exercise pages")
    from collections import Counter
    for msg, cnt in Counter(re.sub(r"^level \d week \d+( homework)?: ", "", w) for w in infos).items():
        print(f"  note: {msg} (x{cnt})")
    for w in errors:
        print("  PROBLEM:", w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
