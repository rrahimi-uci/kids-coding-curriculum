"""Checks for kit episodes that need no drawing libraries (run by `make test` and `episode-check`).

1. The beats say exactly the spec narration (so captions and fact-checks stay valid).
2. Every action's `at`/`until` names a real cue (checked on an estimated timeline).
3. Every code panel that is run declares `expect=[...]`, and that equals what the code really prints
   (the snippet is executed with the course's headless turtle); turtle canvases run without errors.
With drawing libraries installed, `exercise_components` also draws every action at the start and end
of its window, which catches bad options and time specs inside actions.
"""

from __future__ import annotations

import importlib
import json
from pathlib import Path

from . import pyrun
from .kit_dsl import ACTION_TYPES, SETTINGS, Episode, resolve_time
from .timeline import build_timeline, check_against_spec

REPO_ROOT = Path(__file__).resolve().parents[3]
EPISODES = Path(__file__).parent / "episodes"


def kit_episodes() -> list[tuple]:
    found = [(int(p.stem[1]), int(p.stem[3:5])) for p in EPISODES.glob("l[1-3]w[0-9][0-9].py")]
    found += [(p.stem[:2], int(p.stem[3:5])) for p in EPISODES.glob("j[1-3]w[0-9][0-9].py")]  # junior
    return sorted(found, key=lambda e: (str(e[0]), e[1]))


def load(level: int, week: int) -> Episode:
    from .render import module_name

    return importlib.import_module(f"videos.pipeline.animated.episodes.{module_name(level, week)}").EPISODE


def spec_video(level: int, week: int) -> dict:
    from .render import spec_path

    spec = json.loads(spec_path(level).read_text(encoding="utf-8"))
    return next(v for v in spec["videos"] if v["week"] == week)


def estimated_timeline(episode: Episode):
    durations = [[max(0.6, len(beat.text.split()) / 150 * 60) for beat in scene.beats] for scene in episode.scenes]
    return build_timeline(episode.scripts, durations, 4.6, 5.0)[0]


def check_episode(level: int, week: int, run_code: bool = True) -> list[str]:
    errors: list[str] = []
    episode = load(level, week)
    if (episode.level, episode.week) != (level, week):
        errors.append(f"l{level}w{week:02d}: EPISODE says level {episode.level} week {episode.week}")
    errors += check_against_spec(episode.scripts, spec_video(level, week))
    timings = estimated_timeline(episode)
    for scene, sc in zip(episode.scenes, timings):
        if scene.setting not in SETTINGS:
            errors.append(f"{scene.scene_id}: unknown setting {scene.setting!r}")
        cues = [beat.cue for beat in scene.beats]
        if len(cues) != len(set(cues)) or not all(cues):
            errors.append(f"{scene.scene_id}: every beat needs a unique cue name")
        if {"start", "end"} & set(cues):
            errors.append(f"{scene.scene_id}: 'start' and 'end' are reserved time words; rename those cues")
        for action in scene.actions:
            label = f"{scene.scene_id} {action.kind}"
            if action.kind not in ACTION_TYPES:
                errors.append(f"{label}: unknown action kind")
                continue
            try:
                resolve_time(action.at, sc)
                resolve_time(action.until, sc)
            except ValueError as exc:
                errors.append(f"{label}: {exc}")
            if action.kind == "code":
                errors += _check_code_fits(label, action)
            if action.kind == "code" and run_code:
                errors += _check_code(label, action)
            if action.kind == "turtle" and run_code:
                result = pyrun.run(action.get("code", action.text), tuple(action.get("inputs", ())), action.get("seed", 1))
                if result["error"] and not action.get("allow_error"):
                    errors.append(f"{label}: turtle code raised {result['error']}")
                if not result["draw"]:
                    errors.append(f"{label}: turtle code draws nothing")
    return errors


def _check_code_fits(label: str, action) -> list[str]:
    """The editor shows only the lines that fit; never let a line silently disappear."""
    lines = action.get("code", action.text).strip("\n").split("\n")
    size = action.get("size", 34)
    show_shell = action.get("shell", action.get("run") is not None)
    shell_h = action.get("shell_h", 230) if show_shell else 0
    capacity = int((action.get("h", 720) - shell_h - 100) // (size * 1.45))
    if len(lines) > capacity:
        return [f"{label}: {len(lines)} code lines but only {capacity} fit; make the panel taller or the text smaller"]
    return []


def _check_code(label: str, action) -> list[str]:
    code = action.get("code", action.text).strip("\n")
    program = action.get("exec", code)
    try:
        compile(program, "main.py", "exec")
    except SyntaxError as exc:
        if not action.get("allow_error"):
            return [f"{label}: code does not compile ({exc.msg}, line {exc.lineno})"]
    if action.get("run") is None:
        return []
    if action.get("expect") is None:
        return [f"{label}: a code panel that is run must list expect=[...] (the Shell lines the video shows)"]
    result = pyrun.run(program, tuple(action.get("inputs", ())), action.get("seed", 1))
    actual = pyrun.shell_lines(result, action.get("traceback", False))
    if list(action.get("expect")) != actual:
        return [f"{label}: expect={list(action.get('expect'))!r} but the code really prints {actual!r}"]
    if result["error"] and not action.get("allow_error"):
        return [f"{label}: code raised {result['error']} (pass allow_error=True if the error is the lesson)"]
    return []


def exercise_components(level: int, week: int) -> list[str]:
    """Draw every action at the start and near the end of its window (needs cairo)."""
    from .engine import new_frame
    from .kit import COMPONENTS, D, setting

    errors = []
    episode = load(level, week)
    for scene, sc in zip(episode.scenes, estimated_timeline(episode)):
        _, ctx = new_frame()
        resolve = lambda spec, sc=sc: resolve_time(spec, sc)  # noqa: E731
        setting(ctx, scene.setting, 0.0)
        for action in scene.actions:
            try:
                t0, t1 = resolve(action.at), resolve(action.until)
                for t in sorted({t0 + 0.05, (t0 + t1) / 2, max(t0, t1 - 0.05)}):
                    COMPONENTS[action.kind](D(ctx, t, sc.start + t, sc, resolve), action, t0)
            except Exception as exc:  # report every broken action, not just the first
                errors.append(f"{scene.scene_id} {action.kind}: {type(exc).__name__}: {exc}")
    return errors
