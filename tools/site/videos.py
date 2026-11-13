"""Bring the teaching videos into the website build.

The videos are not kept in git. `python -m videos.pipeline.cli publish-videos --upload` puts web copies
(720p MP4, poster JPG, WebVTT captions) and a `videos.json` list on the repository's `videos` release; this
module copies them into site/public/videos/ while the site is built, so every page that has a video
shows it in the same place. When a video is replaced on the release, the next build shows the new one.

The junior track's videos ("Kids Coding Junior with Aiden and Pixi") are on the same release, listed in
their own `junior-videos.json` with the same shape and keys like "j1-2" (junior level 1, week 2). Each
list is read on its own: when one is missing, only its videos are left out.

Where the files come from (environment variable SITE_VIDEOS):
  unset          the `videos` release of this repository (GITHUB_REPOSITORY, or the default below)
  a folder path  a local folder with the same files, e.g. videos/output/web after publish-videos
  off            no videos (the pages are built without the player)

If the files cannot be fetched, the site is still built, without videos, and a note is printed.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "site" / "public" / "videos"
CACHE = ROOT / "build" / "site-cache" / "videos"
DEFAULT_REPO = "rrahimi-uci/kids-coding-curriculum"
RELEASE_TAG = "videos"
MANIFEST = "videos.json"
JUNIOR_MANIFEST = "junior-videos.json"
BASE = "%BASE%"
CUE_GAP = 1.6  # seconds of silence between captions that start a new paragraph in the transcript


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_name(destination.name + ".part")
    request = urllib.request.Request(url, headers={"User-Agent": "kids-coding-site-build"})
    with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as out:
        shutil.copyfileobj(response, out, 1 << 20)
    partial.replace(destination)


class _Source:
    """Reads files from a local folder or from the release, keeping a checksum-verified cache."""

    def __init__(self, setting: str):
        self.folder = Path(setting).expanduser() if setting else None
        if self.folder is not None and not self.folder.is_absolute():
            self.folder = ROOT / self.folder
        repo = os.environ.get("GITHUB_REPOSITORY") or DEFAULT_REPO
        self.base_url = f"https://github.com/{repo}/releases/download/{RELEASE_TAG}/"

    def describe(self) -> str:
        return str(self.folder) if self.folder else self.base_url

    def manifest(self, name: str = MANIFEST) -> dict:
        if self.folder:
            return json.loads((self.folder / name).read_text(encoding="utf-8"))
        target = CACHE / name
        _download(self.base_url + name, target)  # always fresh: it says which files changed
        return json.loads(target.read_text(encoding="utf-8"))

    def fetch(self, name: str, sha256: str | None) -> Path:
        if self.folder:
            path = self.folder / name
        else:
            path = CACHE / name
            if not (path.is_file() and sha256 and _sha256(path) == sha256):
                _download(self.base_url + name, path)
        if sha256 and _sha256(path) != sha256:
            raise ValueError(f"{name} does not match its checksum in its video list")
        return path


def _timestamp(value: str) -> float:
    hours, minutes, seconds = value.replace(",", ".").split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def transcript(vtt: str) -> list[str]:
    """The narration as paragraphs (a longer pause between captions starts a new paragraph)."""
    paragraphs: list[list[str]] = []
    last_end = None
    for block in re.split(r"\n\s*\n", vtt.replace("\r\n", "\n")):
        lines = [line.strip() for line in block.strip().splitlines()]
        timing = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if timing is None:
            continue
        start, end = (_timestamp(part.strip().split(" ")[0]) for part in lines[timing].split("-->"))
        words = re.sub(r"<[^>]+>", "", " ".join(lines[timing + 1:])).strip()
        if not words:
            continue
        if last_end is None or start - last_end > CUE_GAP:
            paragraphs.append([])
        paragraphs[-1].append(words)
        last_end = end
    return [" ".join(parts) for parts in paragraphs]


def level_key(part: str) -> int | str:
    """The level part of a video key: 1 for main-track level 1 ("1-2"), "j1" for junior level 1 ("j1-2")."""
    return int(part) if part.isdigit() else part


def collect(warnings: list[str], manifests: tuple[str, ...] = (MANIFEST,)) -> dict[tuple[int | str, int], dict]:
    """Copy the videos into site/public/videos/ and return the page data for each (level, week).

    The level is an int for the main track (videos.json) and the curriculum key, such as "j1", for the
    junior track (junior-videos.json)."""
    setting = os.environ.get("SITE_VIDEOS", "").strip()
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    if setting.lower() in {"off", "0", "no", "none"}:
        print("  videos: off (SITE_VIDEOS=off)")
        return {}
    source = _Source(setting)
    found: dict[tuple[int | str, int], dict] = {}
    for name in manifests:
        try:
            listing = source.manifest(name)
        except (OSError, urllib.error.URLError, ValueError) as exc:
            what = "none on the site" if name == MANIFEST else f"none from {name} on the site"
            warnings.append(f"videos: {what}, could not read {name} from {source.describe()} ({exc})")
            continue
        found.update(_collect_list(source, listing, warnings))
    total = sum(f.stat().st_size for f in PUBLIC.glob("*")) / 1e6 if PUBLIC.exists() else 0
    print(f"  videos: {len(found)} from {source.describe()} ({total:.0f} MB)")
    return found


def _collect_list(source: _Source, listing: dict, warnings: list[str]) -> dict[tuple[int | str, int], dict]:
    found: dict[tuple[int | str, int], dict] = {}
    for key, entry in sorted(listing.get("videos", {}).items()):
        lpart, wpart = key.rsplit("-", 1)
        level, week = level_key(lpart), int(wpart)
        sums = entry.get("sha256", {})
        try:
            files = {kind: source.fetch(entry[kind], sums.get(entry[kind])) for kind in ("video", "poster", "captions")}
        except (OSError, urllib.error.URLError, ValueError, KeyError) as exc:
            warnings.append(f"videos: level {level} week {week} left out ({exc})")
            continue
        PUBLIC.mkdir(parents=True, exist_ok=True)
        for path in files.values():
            shutil.copy2(path, PUBLIC / path.name)
        seconds = float(entry["seconds"])
        found[(level, week)] = {
            "src": f"{BASE}videos/{files['video'].name}",
            "poster": f"{BASE}videos/{files['poster'].name}",
            "captions": f"{BASE}videos/{files['captions'].name}",
            "seconds": round(seconds),
            "minutes": max(1, round(seconds / 60)),
            "mb": round(files["video"].stat().st_size / 1e6, 1),
            "transcript": transcript(files["captions"].read_text(encoding="utf-8")),
        }
    return found
