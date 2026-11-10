"""Command-line entry point for checking, regenerating, and rendering videos."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys

from .markdown import render_plan
from .media import render_video
from .models import load_series, validate_series
from .sources import build_manifest, stale_weeks

REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = REPO_ROOT / "videos" / "specs" / "level1.json"
PLAN_PATH = REPO_ROOT / "videos" / "video-plan-level1.md"
MANIFEST_PATH = REPO_ROOT / "videos" / "manifest-level1.json"


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def command_check(_: argparse.Namespace) -> int:
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    expected_plan = render_plan(series)
    if not PLAN_PATH.is_file() or PLAN_PATH.read_text(encoding="utf-8") != expected_plan:
        errors.append("video-plan-level1.md is not synchronized with the JSON spec")
    if not MANIFEST_PATH.is_file():
        errors.append("manifest-level1.json is missing")
    else:
        changed = stale_weeks(REPO_ROOT, MANIFEST_PATH)
        if changed:
            errors.append(
                "curriculum changed for week(s) "
                + ", ".join(str(week) for week in changed)
                + "; regenerate those scripts"
            )
    if errors:
        print("Video quality gate failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"Video quality gate passed: {len(series.videos)} scripts, "
        f"{sum(len(video.scenes) for video in series.videos)} scenes, no source drift."
    )
    return 0


async def _generate(args: argparse.Namespace) -> int:
    from .agents_workflow import generate_video

    raw = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    current = {int(video["week"]): video for video in raw["videos"]}
    if args.week:
        weeks = sorted(set(args.week))
    elif MANIFEST_PATH.is_file():
        weeks = stale_weeks(REPO_ROOT, MANIFEST_PATH)
    else:
        weeks = list(range(1, 13))
    if not weeks:
        print("No curriculum changes detected; all scripts are current.")
        return 0
    for week in weeks:
        print(f"Regenerating Level 1 week {week}...")
        current[week] = await generate_video(
            REPO_ROOT,
            week,
            current_video=current.get(week),
            max_revisions=args.max_revisions,
        )
    raw["videos"] = [current[week] for week in range(1, 13)]
    candidate_path = SPEC_PATH.with_suffix(".candidate.json")
    _write_json(candidate_path, raw)
    candidate = load_series(candidate_path)
    errors = validate_series(candidate, REPO_ROOT)
    if errors:
        print("Generated scripts failed deterministic checks:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"Candidate retained at {candidate_path}", file=sys.stderr)
        return 1
    _write_json(SPEC_PATH, raw)
    PLAN_PATH.write_text(render_plan(candidate), encoding="utf-8")
    _write_json(MANIFEST_PATH, build_manifest(REPO_ROOT))
    candidate_path.unlink(missing_ok=True)
    print(f"Updated weeks {', '.join(map(str, weeks))}; teacher review is still required.")
    return 0


def command_render(args: argparse.Namespace) -> int:
    if not args.approved:
        print(
            "Rendering can make paid API calls. Review the plan, then pass --approved.",
            file=sys.stderr,
        )
        return 2
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    requested = set(args.week or range(1, 13))
    output = REPO_ROOT / "videos" / "output"
    output.mkdir(parents=True, exist_ok=True)
    for video in series.videos:
        if video.week in requested:
            destination = render_video(
                video,
                output,
                visual_provider=args.visual_provider,
                voice_provider=args.voice_provider,
            )
            print(destination.relative_to(REPO_ROOT))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    check = subcommands.add_parser("check", help="validate scripts and curriculum hashes")
    check.set_defaults(handler=command_check)

    generate = subcommands.add_parser("generate", help="regenerate stale scripts with agents")
    generate.add_argument("--week", type=int, choices=range(1, 13), action="append")
    generate.add_argument("--max-revisions", type=int, default=2, choices=range(0, 5))
    generate.set_defaults(handler=lambda args: asyncio.run(_generate(args)))

    render = subcommands.add_parser("render", help="render reviewed scripts to captioned MP4")
    render.add_argument("--week", type=int, choices=range(1, 13), action="append")
    render.add_argument("--approved", action="store_true")
    render.add_argument("--visual-provider", choices=("cards", "openai"), default="cards")
    render.add_argument("--voice-provider", choices=("openai-speech",), default="openai-speech")
    render.set_defaults(handler=command_render)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
