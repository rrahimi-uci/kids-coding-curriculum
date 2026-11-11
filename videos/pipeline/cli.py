"""Command-line entry point for checking, regenerating, accepting, and rendering videos (all levels)."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys

from .markdown import render_plan
from .models import Video, load_series, validate_series, validate_video
from .sources import changed_files, update_manifest_weeks, write_manifest

REPO_ROOT = Path(__file__).resolve().parents[2]
VIDEOS = REPO_ROOT / "videos"
OUTPUT_DIR = VIDEOS / "output"
WEEKS = range(1, 13)
LEVELS = (1, 2, 3)


def spec_path(level: int) -> Path:
    return VIDEOS / "specs" / f"level{level}.json"


def plan_path(level: int) -> Path:
    return VIDEOS / f"video-plan-level{level}.md"


def manifest_path(level: int) -> Path:
    return VIDEOS / f"manifest-level{level}.json"


def candidate_path(level: int) -> Path:
    return spec_path(level).with_suffix(".candidate.json")


def existing_levels() -> list[int]:
    return [level for level in LEVELS if spec_path(level).is_file()]


def _levels(args: argparse.Namespace) -> list[int]:
    return [args.level] if getattr(args, "level", None) else existing_levels()


# Kept for callers that only know Level 1.
SPEC_PATH, PLAN_PATH, MANIFEST_PATH = spec_path(1), plan_path(1), manifest_path(1)


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _drift_report(level: int = 1) -> list[str]:
    """One line per stale week, naming the files that changed."""
    path = manifest_path(level)
    if not path.is_file():
        return [f"{path.name} is missing; run `accept --level {level} --all` after reviewing the scripts"]
    try:
        changes = changed_files(REPO_ROOT, path)
    except ValueError as exc:
        return [str(exc)]
    return [f"level {level}: curriculum changed for week {week}: {', '.join(files)}" for week, files in changes.items()]


def command_check(args: argparse.Namespace) -> int:
    errors, drift, summary = [], [], []
    for level in _levels(args):
        series = load_series(spec_path(level))
        errors += validate_series(series, REPO_ROOT, level)
        if not plan_path(level).is_file() or plan_path(level).read_text(encoding="utf-8") != render_plan(series):
            errors.append(f"{plan_path(level).name} is not synchronized with the JSON spec (run `plan --level {level}`)")
        drift += _drift_report(level)
        summary.append(f"Level {level}: {len(series.videos)} scripts, {sum(len(v.scenes) for v in series.videos)} scenes")
    if errors or drift:
        print("Video quality gate failed:", file=sys.stderr)
        for line in errors + drift:
            print(f"- {line}", file=sys.stderr)
        if drift:
            print("  Then either regenerate those weeks (`generate --level L --week N`) or, if the script still "
                  "matches the lesson, record that with `accept --level L --week N`.", file=sys.stderr)
        return 1
    print("Video quality gate passed: " + "; ".join(summary) + "; no source drift.")
    return 0


def command_plan(args: argparse.Namespace) -> int:
    """Rewrite the readable plan from the JSON spec after a hand edit."""
    status = 0
    for level in _levels(args):
        series = load_series(spec_path(level))
        errors = validate_series(series, REPO_ROOT, level)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        plan_path(level).write_text(render_plan(series), encoding="utf-8")
        print(f"Wrote {plan_path(level).relative_to(REPO_ROOT)}")
        status = status or (1 if errors else 0)
    return status


def command_validate_draft(args: argparse.Namespace) -> int:
    """Validate draft videos (a JSON list of video objects, or a spec) without needing all 12 weeks."""
    raw = json.loads(Path(args.path).read_text(encoding="utf-8"))
    videos = raw["videos"] if isinstance(raw, dict) else raw
    errors = []
    for item in videos:
        try:
            errors += validate_video(Video.from_dict(item), REPO_ROOT, args.level)
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"week {item.get('week', '?')}: malformed video object ({exc!r})")
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    print(f"{len(videos)} draft video(s): {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


def command_accept(args: argparse.Namespace) -> int:
    """Record that a teacher checked the scripts against the current lessons (no paid calls)."""
    if not args.all and not args.week:
        print("Name the reviewed weeks with --week N (repeatable) or pass --all.", file=sys.stderr)
        return 2
    level = args.level or 1
    series = load_series(spec_path(level))
    errors = validate_series(series, REPO_ROOT, level)
    if errors:
        print("Fix the spec before accepting it:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if args.all:
        write_manifest(REPO_ROOT, manifest_path(level), level)
        weeks = list(WEEKS)
    else:
        weeks = sorted(set(args.week))
        update_manifest_weeks(REPO_ROOT, manifest_path(level), weeks, level)
    print(f"Recorded the current Level {level} curriculum for week(s) {', '.join(map(str, weeks))}.")
    return 0


async def _generate(args: argparse.Namespace) -> int:
    from .agents_workflow import generate_video

    level = args.level or 1
    spec, manifest, candidate = spec_path(level), manifest_path(level), candidate_path(level)
    raw = json.loads(spec.read_text(encoding="utf-8"))
    current = {int(video["week"]): video for video in raw["videos"]}
    if args.week:
        weeks = sorted(set(args.week))
    elif manifest.is_file():
        weeks = sorted(changed_files(REPO_ROOT, manifest))
    else:
        weeks = list(WEEKS)
    if not weeks:
        print("No curriculum changes detected; all scripts are current.")
        return 0
    done: list[int] = []
    for week in weeks:
        print(f"Regenerating Level {level} week {week}...")
        try:
            current[week] = await generate_video(
                REPO_ROOT, week, current_video=current.get(week), max_revisions=args.max_revisions, level=level,
            )
        except Exception as exc:  # keep the weeks that already succeeded for review
            print(f"Week {week} failed: {exc}", file=sys.stderr)
            break
        done.append(week)
        raw["videos"] = [current[w] for w in WEEKS]
        _write_json(candidate, raw)
    if not done:
        return 1
    series = load_series(candidate)
    errors = validate_series(series, REPO_ROOT, level)
    if errors:
        print("Generated scripts failed deterministic checks:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"Candidate retained at {candidate.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    _write_json(spec, raw)
    plan_path(level).write_text(render_plan(series), encoding="utf-8")
    update_manifest_weeks(REPO_ROOT, manifest, done, level)
    candidate.unlink(missing_ok=True)
    print(f"Updated week(s) {', '.join(map(str, done))}; teacher review is still required.")
    return 0 if done == weeks else 1


def command_render(args: argparse.Namespace) -> int:
    from .media import needs_approval, render_video

    if needs_approval(args.visual_provider, args.voice_provider) and not args.approved:
        print(
            f"'{args.visual_provider}' pictures with '{args.voice_provider}' narration make paid API "
            "calls. Review the plan, then pass --approved. For a free offline draft, use "
            "--voice-provider macos-say (or silent) with the default cards, or the `animate` command.",
            file=sys.stderr,
        )
        return 2
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for level in _levels(args):
        series = load_series(spec_path(level))
        errors = validate_series(series, REPO_ROOT, level)
        drift = _drift_report(level)
        if drift and not args.allow_stale:
            errors += drift + ["refusing to render scripts that may not match the lessons (or pass --allow-stale)"]
        if errors:
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        requested = set(args.week or WEEKS)
        for video in series.videos:
            if video.week in requested:
                destination = render_video(video, OUTPUT_DIR, visual_provider=args.visual_provider,
                                           voice_provider=args.voice_provider, level=level)
                print(destination.relative_to(REPO_ROOT))
    return 0


def command_fetch_voice(_: argparse.Namespace) -> int:
    """Download the free local neural voice model (Kokoro, Apache-2.0) and verify its checksums."""
    from .animated.audio import fetch_models

    fetch_models()
    print("Voice model ready in videos/.cache/models/")
    return 0


def command_animate(args: argparse.Namespace) -> int:
    """Render fully animated episodes with natural local voices, music and sound effects (free)."""
    try:
        from .animated.render import available_episodes, render_episode
    except ImportError as exc:
        print(f"Animated episodes need the extra packages in videos/requirements-animate.txt ({exc})", file=sys.stderr)
        return 2
    wanted = [(level, week) for level, week in available_episodes()
              if (not args.level or level == args.level) and (not args.week or week in args.week)]
    if not wanted:
        print(f"No animated episode matches; available: {available_episodes()}", file=sys.stderr)
        return 2
    for level in sorted({level for level, _ in wanted}):
        drift = _drift_report(level)
        if drift and not args.allow_stale:
            for line in drift + ["refusing to animate scripts that may not match the lessons (or pass --allow-stale)"]:
                print(f"- {line}", file=sys.stderr)
            return 1
    failed = []
    for level, week in wanted:
        try:
            destination = render_episode(week, OUTPUT_DIR, workers=args.workers, preview=args.preview, level=level)
        except Exception as exc:  # keep rendering the others; report every failure at the end
            failed.append(f"level {level} week {week}: {exc}")
            print(f"FAILED level {level} week {week}: {exc}", file=sys.stderr)
            continue
        print(destination.relative_to(REPO_ROOT))
    if failed:
        print(f"{len(failed)} episode(s) failed:", file=sys.stderr)
        for line in failed:
            print(f"- {line}", file=sys.stderr)
        return 1
    return 0


def command_apply_narration(args: argparse.Namespace) -> int:
    """Apply {scene_id: narration} (or {scene_id: {"narration": ..., "duration_seconds": ...}}) to a spec.

    Safe when several authors run it at once: the spec is locked while it is read and rewritten.
    """
    import fcntl

    changes = json.loads(Path(args.path).read_text(encoding="utf-8"))
    spec = spec_path(args.level)
    with open(spec, "r+", encoding="utf-8") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        raw = json.loads(handle.read())
        touched = set()
        for video in raw["videos"]:
            for scene in video["scenes"]:
                change = changes.get(scene["scene_id"])
                if change is None:
                    continue
                if isinstance(change, str):
                    change = {"narration": change}
                for key in ("narration", "duration_seconds", "on_screen_text", "visual", "production_notes"):
                    if key in change:
                        scene[key] = change[key]
                touched.add(video["week"])
        missing = set(changes) - {s["scene_id"] for v in raw["videos"] for s in v["scenes"]}
        if missing:
            print(f"Unknown scene ids: {sorted(missing)}", file=sys.stderr)
            return 1
        errors = []
        for video in raw["videos"]:
            if video["week"] in touched:
                errors += validate_video(Video.from_dict(video), REPO_ROOT, args.level)
        if errors:
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            print("Not applied.", file=sys.stderr)
            return 1
        handle.seek(0)
        handle.write(json.dumps(raw, indent=2, ensure_ascii=False) + "\n")
        handle.truncate()
        plan_path(args.level).write_text(render_plan(load_series(spec)), encoding="utf-8")
        fcntl.flock(handle, fcntl.LOCK_UN)
    print(f"Applied {len(changes)} scene change(s) to Level {args.level} week(s) {sorted(touched)}.")
    return 0


def command_episode_check(args: argparse.Namespace) -> int:
    """Check kit episodes: beats = spec narration, cues exist, code panels show the true output."""
    from .animated.episode_check import check_episode, exercise_components, kit_episodes

    wanted = [(lvl, wk) for lvl, wk in kit_episodes()
              if (not args.level or lvl == args.level) and (not args.week or wk in args.week)]
    errors = []
    for level, week in wanted:
        errors += check_episode(level, week)
        try:
            errors += exercise_components(level, week)
        except ImportError:
            pass  # drawing libraries not installed: the data checks above still ran
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    print(f"{len(wanted)} kit episode(s): {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


def command_contact_sheet(args: argparse.Namespace) -> int:
    """Render a grid of still frames (real voice timing) so an author can look at a whole episode."""
    from PIL import Image, ImageDraw

    from .animated.render import still, timeline_summary

    scenes, _ = timeline_summary(args.week, args.level)
    times = []
    for scene in scenes:
        for k in range(args.per_scene):
            times.append(round(scene.start + (k + 0.6) / args.per_scene * scene.duration, 2))
    folder = OUTPUT_DIR / "sheets" / f"l{args.level}w{args.week:02d}"
    shutil_paths = still(args.week, times, folder, level=args.level)
    w, h = 640, 360
    cols = args.per_scene
    rows = (len(shutil_paths) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), "white")
    for i, path in enumerate(shutil_paths):
        sheet.paste(Image.open(path).resize((w, h)), ((i % cols) * w, (i // cols) * h))
        ImageDraw.Draw(sheet).text(((i % cols) * w + 8, (i // cols) * h + 6), f"{times[i]:.1f}s", fill="red")
    out = OUTPUT_DIR / "sheets" / f"l{args.level}w{args.week:02d}-sheet.png"
    sheet.save(out)
    print(out.relative_to(REPO_ROOT))
    return 0


def command_publish_videos(args: argparse.Namespace) -> int:
    """Make the website copies of rendered videos and (with --upload) replace them on the `videos` release."""
    from . import publish

    rendered = publish.rendered_videos()
    wanted = {key for key in rendered
              if (not args.level or key[0] == args.level) and (not args.week or key[1] in args.week)}
    if not wanted:
        print("No rendered video matches; run `animate` first.", file=sys.stderr)
        return 2
    try:
        manifest = publish.build_web_copies(wanted)
        print(f"Web copies are in {publish.WEB.relative_to(REPO_ROOT)}/ "
              f"(preview the site with SITE_VIDEOS={publish.WEB.relative_to(REPO_ROOT)} make site)")
        if args.upload:
            publish.upload(manifest, wanted)
            if args.rebuild_site:
                publish.rebuild_site()
    except RuntimeError as exc:
        print(f"publish-videos: {exc}", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    from .media import VISUAL_PROVIDERS, VOICE_PROVIDERS

    parser = argparse.ArgumentParser(prog="python -m videos.pipeline.cli", description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    def level_arg(sub, default_note="all levels with a spec"):
        sub.add_argument("--level", type=int, choices=LEVELS, help=f"course level (default: {default_note})")

    check = subcommands.add_parser("check", help="validate scripts, plans and curriculum fingerprints")
    level_arg(check)
    check.set_defaults(handler=command_check)

    plan = subcommands.add_parser("plan", help="rewrite video-plan-levelN.md from the JSON spec")
    level_arg(plan)
    plan.set_defaults(handler=command_plan)

    draft = subcommands.add_parser("validate-draft", help="validate draft video objects for one level")
    draft.add_argument("path")
    draft.add_argument("--level", type=int, choices=LEVELS, required=True)
    draft.set_defaults(handler=command_validate_draft)

    accept = subcommands.add_parser(
        "accept", help="record that the scripts still match the current lessons (after a teacher review)")
    level_arg(accept, "1")
    accept.add_argument("--week", type=int, choices=WEEKS, action="append")
    accept.add_argument("--all", action="store_true")
    accept.set_defaults(handler=command_accept)

    generate = subcommands.add_parser("generate", help="regenerate stale scripts with agents (paid)")
    level_arg(generate, "1")
    generate.add_argument("--week", type=int, choices=WEEKS, action="append")
    generate.add_argument("--max-revisions", type=int, default=2, choices=range(0, 5))
    generate.set_defaults(handler=lambda args: asyncio.run(_generate(args)))

    render = subcommands.add_parser("render", help="render reviewed scripts to captioned MP4 (storyboard style)")
    level_arg(render)
    render.add_argument("--week", type=int, choices=WEEKS, action="append")
    render.add_argument("--approved", action="store_true", help="allow paid image or voice calls")
    render.add_argument("--allow-stale", action="store_true", help="render even if lessons changed (drafts only)")
    render.add_argument("--visual-provider", choices=sorted(VISUAL_PROVIDERS), default="cards")
    render.add_argument("--voice-provider", choices=sorted(VOICE_PROVIDERS), default="openai-realtime")
    render.set_defaults(handler=command_render)

    animate = subcommands.add_parser(
        "animate", help="render fully animated episodes with natural local voices, music and effects (free)")
    level_arg(animate)
    animate.add_argument("--week", type=int, choices=WEEKS, action="append")
    animate.add_argument("--workers", type=int, help="parallel frame renderers (default: CPU count - 1)")
    animate.add_argument("--preview", type=float, help="render only the first N seconds")
    animate.add_argument("--allow-stale", action="store_true")
    animate.set_defaults(handler=command_animate)

    publish = subcommands.add_parser(
        "publish-videos", help="make 720p website copies and (with --upload) replace them on the `videos` release")
    level_arg(publish)
    publish.add_argument("--week", type=int, choices=WEEKS, action="append")
    publish.add_argument("--upload", action="store_true", help="upload to the GitHub release (needs gh and a login)")
    publish.add_argument("--rebuild-site", action="store_true", help="after uploading, start the Website workflow")
    publish.set_defaults(handler=command_publish_videos)

    narration = subcommands.add_parser("apply-narration", help="apply narration edits to a spec (locked, validated)")
    narration.add_argument("path")
    narration.add_argument("--level", type=int, choices=LEVELS, required=True)
    narration.set_defaults(handler=command_apply_narration)

    echeck = subcommands.add_parser("episode-check", help="check kit episodes (script, cues, real code output)")
    level_arg(echeck)
    echeck.add_argument("--week", type=int, choices=WEEKS, action="append")
    echeck.set_defaults(handler=command_episode_check)

    sheet = subcommands.add_parser("contact-sheet", help="render a grid of stills for one episode")
    sheet.add_argument("--level", type=int, choices=LEVELS, required=True)
    sheet.add_argument("--week", type=int, choices=WEEKS, required=True)
    sheet.add_argument("--per-scene", type=int, default=4)
    sheet.set_defaults(handler=command_contact_sheet)

    fetch = subcommands.add_parser("fetch-voice", help="download the local neural voice model once")
    fetch.set_defaults(handler=command_fetch_voice)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
