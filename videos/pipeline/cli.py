"""Command-line entry point for checking, regenerating, accepting, and rendering videos."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys

from .markdown import render_plan
from .models import load_series, validate_series
from .sources import changed_files, update_manifest_weeks, write_manifest

REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = REPO_ROOT / "videos" / "specs" / "level1.json"
PLAN_PATH = REPO_ROOT / "videos" / "video-plan-level1.md"
MANIFEST_PATH = REPO_ROOT / "videos" / "manifest-level1.json"
CANDIDATE_PATH = SPEC_PATH.with_suffix(".candidate.json")
OUTPUT_DIR = REPO_ROOT / "videos" / "output"
WEEKS = range(1, 13)


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _drift_report() -> list[str]:
    """One line per stale week, naming the files that changed."""
    if not MANIFEST_PATH.is_file():
        return ["manifest-level1.json is missing; run `accept --all` after reviewing the scripts"]
    try:
        changes = changed_files(REPO_ROOT, MANIFEST_PATH)
    except ValueError as exc:
        return [str(exc)]
    return [
        f"curriculum changed for week {week}: {', '.join(files)}"
        for week, files in changes.items()
    ]


def command_check(_: argparse.Namespace) -> int:
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    if not PLAN_PATH.is_file() or PLAN_PATH.read_text(encoding="utf-8") != render_plan(series):
        errors.append("video-plan-level1.md is not synchronized with the JSON spec (run `plan`)")
    drift = _drift_report()
    if errors or drift:
        print("Video quality gate failed:", file=sys.stderr)
        for line in errors + drift:
            print(f"- {line}", file=sys.stderr)
        if drift:
            print(
                "  Then either regenerate those weeks (`generate --week N`) or, if the script still "
                "matches the lesson, record that with `accept --week N`.",
                file=sys.stderr,
            )
        return 1
    print(
        f"Video quality gate passed: {len(series.videos)} scripts, "
        f"{sum(len(video.scenes) for video in series.videos)} scenes, no source drift."
    )
    return 0


def command_plan(_: argparse.Namespace) -> int:
    """Rewrite the readable plan from the JSON spec after a hand edit."""
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    PLAN_PATH.write_text(render_plan(series), encoding="utf-8")
    print(f"Wrote {PLAN_PATH.relative_to(REPO_ROOT)}")
    return 1 if errors else 0


def command_accept(args: argparse.Namespace) -> int:
    """Record that a teacher checked the scripts against the current lessons (no paid calls)."""
    if not args.all and not args.week:
        print("Name the reviewed weeks with --week N (repeatable) or pass --all.", file=sys.stderr)
        return 2
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    if errors:
        print("Fix the spec before accepting it:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if args.all:
        write_manifest(REPO_ROOT, MANIFEST_PATH)
        weeks = list(WEEKS)
    else:
        weeks = sorted(set(args.week))
        update_manifest_weeks(REPO_ROOT, MANIFEST_PATH, weeks)
    print(f"Recorded the current curriculum for week(s) {', '.join(map(str, weeks))}.")
    return 0


async def _generate(args: argparse.Namespace) -> int:
    from .agents_workflow import generate_video

    raw = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    current = {int(video["week"]): video for video in raw["videos"]}
    if args.week:
        weeks = sorted(set(args.week))
    elif MANIFEST_PATH.is_file():
        weeks = sorted(changed_files(REPO_ROOT, MANIFEST_PATH))
    else:
        weeks = list(WEEKS)
    if not weeks:
        print("No curriculum changes detected; all scripts are current.")
        return 0
    done: list[int] = []
    for week in weeks:
        print(f"Regenerating Level 1 week {week}...")
        try:
            current[week] = await generate_video(
                REPO_ROOT, week, current_video=current.get(week), max_revisions=args.max_revisions,
            )
        except Exception as exc:  # keep the weeks that already succeeded for review
            print(f"Week {week} failed: {exc}", file=sys.stderr)
            break
        done.append(week)
        raw["videos"] = [current[w] for w in WEEKS]
        _write_json(CANDIDATE_PATH, raw)
    if not done:
        return 1
    candidate = load_series(CANDIDATE_PATH)
    errors = validate_series(candidate, REPO_ROOT)
    if errors:
        print("Generated scripts failed deterministic checks:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"Candidate retained at {CANDIDATE_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    _write_json(SPEC_PATH, raw)
    PLAN_PATH.write_text(render_plan(candidate), encoding="utf-8")
    # Only the regenerated weeks are marked current; other stale weeks stay visible.
    update_manifest_weeks(REPO_ROOT, MANIFEST_PATH, done)
    CANDIDATE_PATH.unlink(missing_ok=True)
    print(f"Updated week(s) {', '.join(map(str, done))}; teacher review is still required.")
    return 0 if done == weeks else 1


def command_render(args: argparse.Namespace) -> int:
    from .media import needs_approval, render_video

    if needs_approval(args.visual_provider, args.voice_provider) and not args.approved:
        print(
            f"'{args.visual_provider}' pictures with '{args.voice_provider}' narration make paid API "
            "calls. Review the plan, then pass --approved. For a free offline draft, use "
            "--voice-provider macos-say (or silent) with the default cards.",
            file=sys.stderr,
        )
        return 2
    series = load_series(SPEC_PATH)
    errors = validate_series(series, REPO_ROOT)
    drift = _drift_report()
    if drift and not args.allow_stale:
        errors += drift + ["refusing to render scripts that may not match the lessons (or pass --allow-stale for a draft)"]
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    requested = set(args.week or WEEKS)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for video in series.videos:
        if video.week in requested:
            destination = render_video(
                video, OUTPUT_DIR, visual_provider=args.visual_provider, voice_provider=args.voice_provider,
            )
            print(destination.relative_to(REPO_ROOT))
    return 0


def build_parser() -> argparse.ArgumentParser:
    from .media import VISUAL_PROVIDERS, VOICE_PROVIDERS

    parser = argparse.ArgumentParser(prog="python -m videos.pipeline.cli", description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    check = subcommands.add_parser("check", help="validate scripts, the plan and curriculum fingerprints")
    check.set_defaults(handler=command_check)

    plan = subcommands.add_parser("plan", help="rewrite video-plan-level1.md from the JSON spec")
    plan.set_defaults(handler=command_plan)

    accept = subcommands.add_parser(
        "accept", help="record that the scripts still match the current lessons (after a teacher review)")
    accept.add_argument("--week", type=int, choices=WEEKS, action="append")
    accept.add_argument("--all", action="store_true")
    accept.set_defaults(handler=command_accept)

    generate = subcommands.add_parser("generate", help="regenerate stale scripts with agents (paid)")
    generate.add_argument("--week", type=int, choices=WEEKS, action="append")
    generate.add_argument("--max-revisions", type=int, default=2, choices=range(0, 5))
    generate.set_defaults(handler=lambda args: asyncio.run(_generate(args)))

    render = subcommands.add_parser("render", help="render reviewed scripts to captioned MP4")
    render.add_argument("--week", type=int, choices=WEEKS, action="append")
    render.add_argument("--approved", action="store_true", help="allow paid image or voice calls")
    render.add_argument("--allow-stale", action="store_true", help="render even if lessons changed (drafts only)")
    render.add_argument("--visual-provider", choices=sorted(VISUAL_PROVIDERS), default="cards")
    render.add_argument("--voice-provider", choices=sorted(VOICE_PROVIDERS), default="openai-realtime")
    render.set_defaults(handler=command_render)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
