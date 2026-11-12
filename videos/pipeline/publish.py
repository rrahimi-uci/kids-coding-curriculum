"""Make web copies of the rendered videos and publish them to the repository's `videos` release.

The website does not keep videos in git. It downloads them from the release when it is built
(tools/site/videos.py), so replacing a video means: render it, run `publish-videos --upload`, and the
next website build shows the new one. File names are stable (level1-week01.mp4), so links never change.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = REPO_ROOT / "videos" / "output"
WEB = OUTPUT / "web"
RELEASE_TAG = "videos"
MANIFEST = "videos.json"
POSTER_AT = 3.0  # seconds: the intro card with the logo, level, week and title
RENDERED = re.compile(r"^level(?P<level>[1-3])-week(?P<week>\d\d)-[a-z0-9-]+\.mp4$")


def stem(level: int, week: int) -> str:
    return f"level{level}-week{week:02d}"


def rendered_videos() -> dict[tuple[int, int], Path]:
    found = {}
    for path in sorted(OUTPUT.glob("level?-week??-*.mp4")):
        match = RENDERED.match(path.name)
        if match and not path.name.endswith(("-draft.mp4", "-preview.mp4")):
            found[(int(match["level"]), int(match["week"]))] = path
    return found


def _run(args: list[str]) -> str:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{args[0]} failed: {result.stderr.strip()[-500:]}")
    return result.stdout


def _seconds(path: Path) -> float:
    return float(_run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def make_web_copy(level: int, week: int, source: Path, name: str | None = None) -> dict:
    """720p H.264 + AAC with fast start, a poster frame and the WebVTT captions."""
    WEB.mkdir(parents=True, exist_ok=True)
    name = name or stem(level, week)
    mp4, jpg, vtt = WEB / f"{name}.mp4", WEB / f"{name}.jpg", WEB / f"{name}.vtt"
    _run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source), "-map", "0:v", "-map", "0:a",
          "-vf", "scale=1280:720:flags=lanczos", "-c:v", "libx264", "-preset", "slow", "-crf", "24",
          "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "112k", "-ac", "2", "-movflags", "+faststart", str(mp4)])
    _run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(POSTER_AT), "-i", str(source),
          "-frames:v", "1", "-vf", "scale=1280:720", "-q:v", "4", str(jpg)])
    captions = source.with_suffix(".vtt")
    if not captions.is_file():
        raise RuntimeError(f"{captions.name} is missing; render the episode again")
    shutil.copyfile(captions, vtt)
    return {"video": mp4.name, "poster": jpg.name, "captions": vtt.name, "seconds": round(_seconds(mp4), 1),
            "bytes": mp4.stat().st_size, "sha256": {p.name: _sha256(p) for p in (mp4, jpg, vtt)}}


def _fetch_release_manifest(destination: Path) -> None:
    """Start from the published list when there is no local one (a fresh clone), if gh can reach it."""
    if not shutil.which("gh"):
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "release", "download", RELEASE_TAG, "--pattern", MANIFEST, "--dir", str(destination.parent),
                    "--clobber"], capture_output=True)


def build_web_copies(wanted: set[tuple[int, int]] | None = None) -> dict:
    """Update the web copies (all, or only `wanted`) and rewrite the manifest."""
    manifest_path = WEB / MANIFEST
    if not manifest_path.is_file():
        _fetch_release_manifest(manifest_path)  # keep the entries of videos not re-made on this computer
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {"videos": {}}
    for (level, week), source in rendered_videos().items():
        if wanted is not None and (level, week) not in wanted:
            continue
        print(f"Level {level} week {week}: making the web copy…")
        manifest["videos"][f"{level}-{week}"] = make_web_copy(level, week, source)
    manifest["release"] = RELEASE_TAG
    WEB.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def upload(manifest: dict, wanted: set[tuple[int, int]] | None = None) -> None:
    """Create the `videos` release if needed and replace the changed files (gh CLI, your login)."""
    if not shutil.which("gh"):
        raise RuntimeError("the GitHub CLI (gh) is needed to upload; install it and run `gh auth login`")
    exists = subprocess.run(["gh", "release", "view", RELEASE_TAG], capture_output=True).returncode == 0
    if not exists:
        _run(["gh", "release", "create", RELEASE_TAG, "--title", "Teaching videos (website)", "--latest=false",
              "--notes", "Web copies of the animated teaching videos (720p, captions, posters). The website "
              "downloads these files when it is built. Narration uses AI-generated voices."])
    files = [WEB / MANIFEST]
    for key, entry in manifest["videos"].items():
        level, week = (int(part) for part in key.split("-"))
        if wanted is None or (level, week) in wanted:
            files += [WEB / entry["video"], WEB / entry["poster"], WEB / entry["captions"]]
    for start in range(0, len(files), 12):  # a few files per call keeps each upload short
        _run(["gh", "release", "upload", RELEASE_TAG, "--clobber", *map(str, files[start:start + 12])])
    print(f"Uploaded {len(files)} file(s) to the '{RELEASE_TAG}' release.")


# --------------------------------------------------------------------------- junior track
# Junior videos (Kids Coding Junior with Aiden and Pixi) live on the same release under their own list,
# junior-videos.json (keys "j1-2" = Junior Level 1 Week 2), so the main list videos.json is never touched.
JUNIOR_MANIFEST = "junior-videos.json"
JUNIOR_RENDERED = re.compile(r"^junior(?P<level>[1-3])-week(?P<week>\d\d)-[a-z0-9-]+\.mp4$")


def junior_rendered_videos() -> dict[tuple[int, int], Path]:
    found = {}
    for path in sorted(OUTPUT.glob("junior?-week??-*.mp4")):
        match = JUNIOR_RENDERED.match(path.name)
        if match and not path.name.endswith(("-draft.mp4", "-preview.mp4")):
            found[(int(match["level"]), int(match["week"]))] = path
    return found


def build_junior_web_copies(wanted: set[tuple[int, int]] | None = None) -> dict:
    """Web copies named junior1-week02.mp4 (and .jpg, .vtt) plus junior-videos.json."""
    manifest_path = WEB / JUNIOR_MANIFEST
    if not manifest_path.is_file() and shutil.which("gh"):
        WEB.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gh", "release", "download", RELEASE_TAG, "--pattern", JUNIOR_MANIFEST, "--dir", str(WEB),
                        "--clobber"], capture_output=True)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {"videos": {}}
    for (level, week), source in junior_rendered_videos().items():
        if wanted is not None and (level, week) not in wanted:
            continue
        print(f"Junior Level {level} week {week}: making the web copy…")
        manifest["videos"][f"j{level}-{week}"] = make_web_copy(level, week, source, name=f"junior{level}-week{week:02d}")
    manifest["release"] = RELEASE_TAG
    manifest["series"] = "Kids Coding Junior with Aiden and Pixi"
    WEB.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def upload_junior(manifest: dict, wanted: set[tuple[int, int]] | None = None) -> None:
    """Upload the junior web copies and junior-videos.json to the existing `videos` release."""
    if not shutil.which("gh"):
        raise RuntimeError("the GitHub CLI (gh) is needed to upload; install it and run `gh auth login`")
    if subprocess.run(["gh", "release", "view", RELEASE_TAG], capture_output=True).returncode != 0:
        raise RuntimeError(f"the '{RELEASE_TAG}' release does not exist yet; publish the main videos first")
    files = [WEB / JUNIOR_MANIFEST]
    for key, entry in manifest["videos"].items():
        level, week = int(key.split("-")[0][1:]), int(key.split("-")[1])
        if wanted is None or (level, week) in wanted:
            files += [WEB / entry["video"], WEB / entry["poster"], WEB / entry["captions"]]
    for start in range(0, len(files), 12):
        _run(["gh", "release", "upload", RELEASE_TAG, "--clobber", *map(str, files[start:start + 12])])
    print(f"Uploaded {len(files)} file(s) to the '{RELEASE_TAG}' release.")


def rebuild_site() -> None:
    """Start the Website workflow on main so the pages pick up the new files now."""
    _run(["gh", "workflow", "run", "site.yml", "--ref", "main"])
    print("Started the Website workflow on main; the new videos are live when it finishes.")
