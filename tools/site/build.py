#!/usr/bin/env python3
"""Generate the website data from the course sources.

    python3 -m tools.site.build [--levels 1 j1 ...] [--skip-pdfs]

Reads only what site/manifest.yml marks public; writes HTML fragments, JSON data, SVG figures and
downloads into site/src/generated/ and site/public/generated/ (both git-ignored), and copies the teaching
videos into site/public/videos/ (see tools/site/videos.py). The Astro project in
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
from . import videos as videomod
from tools import curriculum

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


def level_entry(item: dict) -> dict:
    """A manifest level plus what curriculum.json says about it: where it lives and its web paths.

    Both bands have a Level 1, 2 and 3, so pages and files are named by band: the level page is
    <band>/<slug>/ (grade-4-6/level-1/) and flat file names use the id (grade-4-6-level-1).
    """
    lv = curriculum.by_key(str(item["key"]))
    if item["dir"] != lv.dir:
        raise SystemExit(f"site/manifest.yml: level {lv.key} dir {item['dir']} != curriculum.json {lv.dir}")
    track = curriculum.track(lv.track)
    return {
        "key": lv.key, "track": lv.track, "number": lv.number, "dir": lv.dir, "band": lv.band,
        "band_title": track.band_title, "track_title": track.title, "slug": lv.slug,
        "path": f"{lv.band}/{lv.slug}", "id": f"{lv.band}-{lv.slug}", "weeks_planned": lv.weeks,
        "classopts": f"track={lv.track},level={lv.number}", "syllabus": lv.syllabus,
        "label": f"{track.band_title} level {lv.number}", "published": bool(item["published"]),
    }


def summary(entry: dict, syl: dict) -> dict:
    """The fields every level has, published or not (from curriculum.json and the track syllabus)."""
    sl = syl[entry["track"]][entry["number"]]
    keep = ("key", "track", "number", "dir", "band", "band_title", "track_title", "slug", "path", "id",
            "weeks_planned", "published")
    return {**{k: entry[k] for k in keep},
            "name": sl["name"], "languages": sl["languages"], "tools": sl["tools"], "goals": sl["goals"],
            "project_title": sl["project_title"], "project_html": sl["project_html"],
            "syllabus_weeks": [{"n": w["n"], "title": w["title"], "idea": w["idea"]} for w in sl["weeks"]]}


def build_level(entry: dict, syl: dict, manifest: dict, args, warnings: list[str]) -> dict:
    d, path, ident, label, opts = entry["dir"], entry["path"], entry["id"], entry["label"], entry["classopts"]
    pub = manifest["public"]
    fig_dir = PUB / "fig" / ident
    fig_prefix = f"{BASE}generated/fig/{ident}"
    dl_dir = ROOT / "site" / "public" / "downloads" / path
    # --- exercises (public files only)
    ex_by_week: dict[int, list[dict]] = {}
    ex_pages: dict[str, str] = {}
    for dpath in sorted(glob.glob(str(ROOT / pub["exercise_dirs"].format(dir=d)))):
        dpath = Path(dpath)
        files = [f.name for f in dpath.iterdir() if any(fnmatch.fnmatch(f.name, pat) for pat in pub["exercise_files"])]
        ex = exmod.build_exercise(dpath, entry["key"], sorted(files), warnings)
        if not ex["hints"]:
            warnings.append(f"ERROR {label}: exercise {ex['folder']} has no hints.md")
        ex_by_week.setdefault(ex["week"], []).append(ex)
        ex_pages[ex["folder"]] = f"{BASE}{path}/exercises/{ex['slug']}/"
        ex["url"] = ex_pages[ex["folder"]]
    # --- level documents (whole-level PDFs)
    level_dl: dict[str, dict] = {}
    if not args.skip_pdfs:
        pdf_map = pdfs.ensure_level_pdfs(d, ["student-workbook", "homework"])
        for stem, variants in pdf_map.items():
            for variant, src in variants.items():
                rel = f"downloads/{path}/{ident}-{stem}{'-dyslexia' if variant == 'dyslexia' else ''}.pdf"
                dst = ROOT / "site" / "public" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                level_dl.setdefault(stem, {})[variant] = {"url": f"{BASE}{rel}", "kb": dst.stat().st_size // 1024}
    # --- weeks
    weeks = []
    syl_weeks = {w["n"]: w for w in syl[entry["track"]][entry["number"]]["weeks"]}
    for w in range(1, entry["weeks_planned"] + 1):
        nn = f"{w:02d}"
        wb = ROOT / pub["workbook"].format(dir=d).replace("week[0-9][0-9]", f"week{nn}")
        hw = ROOT / pub["homework"].format(dir=d).replace("week[0-9][0-9]", f"week{nn}")
        if not wb.exists():
            continue
        res = texconv.convert_file(wb, opts, fig_dir, fig_prefix, ex_pages, week_hint=str(w))
        objectives, body = extract_objectives(res.html)
        body = strip_vocab(body)
        if not objectives:
            warnings.append(f"ERROR {label} week {w}: no 'What you will learn' objectives found")
        warnings += [f"{label} week {w}: {x}" for x in res.warnings]
        hw_html, hw_meta = "", {}
        if hw.exists():
            hres = texconv.convert_file(hw, opts, fig_dir, fig_prefix, ex_pages, week_hint=str(w))
            hw_html, hw_meta = hres.html, hres.meta
            warnings += [f"{label} week {w} homework: {x}" for x in hres.warnings]
        html_dir = GEN / "html" / path
        html_dir.mkdir(parents=True, exist_ok=True)
        (html_dir / f"week-{nn}.html").write_text(body, encoding="utf-8")
        (html_dir / f"homework-{nn}.html").write_text(hw_html, encoding="utf-8")
        week_ex = sorted(ex_by_week.get(w, []), key=lambda e: (e["homework"], [int(x) for x in re.findall(r"\d+", e["number"])], e["folder"]))
        # downloads: week PDF + starter zip
        dl = {}
        if not args.skip_pdfs:
            rel = f"downloads/{path}/week-{nn}.pdf"
            if pdfs.week_pdf(entry["key"], opts, d, w, ROOT / "site" / "public" / rel, ROOT / "build" / "site-cache"):
                dl["pdf"] = {"url": f"{BASE}{rel}", "kb": (ROOT / "site" / "public" / rel).stat().st_size // 1024}
        zrel = f"downloads/{path}/{ident}-week-{nn}-starter-files.zip"
        starters = [e for e in week_ex if e["kind"] == "python"]
        if starters:
            zpath = ROOT / "site" / "public" / zrel
            zpath.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                for e in week_ex:
                    src_dir = ROOT / d / "exercises" / e["folder"]
                    z.writestr(f"{e['folder']}/README.md", e["readme_clean"])
                    if e["kind"] == "python":
                        z.writestr(f"{e['folder']}/starter.py", e["starter"]["raw"])
                    for name in e["files"]:
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
            write_json(GEN / "exercises" / path / f"{e['slug']}.json",
                       {k: v for k, v in e.items() if k != "readme_clean"})
            # raw starter files (only the public ones) for the download buttons
            out = dl_dir / "exercises" / e["slug"]
            src_dir = ROOT / d / "exercises" / e["folder"]
            if e["kind"] == "python":
                out.mkdir(parents=True, exist_ok=True)
                (out / "starter.py").write_text(e["starter"]["raw"], encoding="utf-8")
            for name in e["files"]:
                out.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_dir / name, out / name)
    project = extmod.build_project(entry, manifest, GEN, fig_dir, warnings)
    extras = extmod.build_extras(entry, manifest, GEN, fig_dir, warnings)
    glossary = extras.pop("glossary")
    write_json(GEN / "glossary" / f"{ident}.json", glossary)
    extra_dl = extmod.level_pdfs(entry, ["project-brief", "cheat-sheet", "glossary", "parent-notes", "progress-tracker"],
                                 args.skip_pdfs)
    return {
        **summary(entry, syl), "weeks": weeks,
        "project": project, "extras": extras, "glossary_count": len(glossary), "extra_downloads": extra_dl,
        "downloads": level_dl,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", nargs="*", metavar="KEY",
                    help="curriculum.json level keys to convert, e.g. 1 j1 (default: all published in manifest)")
    ap.add_argument("--skip-pdfs", action="store_true", help="do not build or copy PDF downloads")
    args = ap.parse_args(argv)
    manifest = load_manifest()
    syl = {t.id: syllabus.parse(t.syllabus) for t in curriculum.tracks()}
    if GEN.exists():
        shutil.rmtree(GEN)
    GEN.mkdir(parents=True)
    downloads = ROOT / "site" / "public" / "downloads"
    if downloads.exists():  # files from an older layout must not linger in the published site
        shutil.rmtree(downloads)
    downloads.mkdir(parents=True)
    warnings: list[str] = []
    levels = []
    for item in manifest["levels"]:
        entry = level_entry(item)
        if args.levels is not None and entry["key"] not in args.levels:
            entry["published"] = False
        if entry["published"]:
            levels.append(build_level(entry, syl, manifest, args, warnings))
        else:
            levels.append({**summary(entry, syl), "weeks": [], "downloads": {}})
    videos = videomod.collect(warnings)
    for level in levels:
        for week in level["weeks"]:
            if (level["key"], week["n"]) in videos:
                week["video"] = videos[(level["key"], week["n"])]
    write_json(GEN / "levels.json", levels)
    write_json(GEN / "bands.json", [
        {"id": t.dir, "track": t.id, "title": t.title, "band_title": t.band_title,
         "grades": t.grades.replace("-", "–"), "ages": t.ages.replace("-", "–"),
         "levels": [lv["key"] for lv in levels if lv["track"] == t.id]}
        for t in curriculum.tracks()])
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
    for msg, cnt in Counter(re.sub(r"^Grades \S+ level \d week \d+( homework)?: ", "", w) for w in infos).items():
        print(f"  note: {msg} (x{cnt})")
    for w in errors:
        print("  PROBLEM:", w)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
