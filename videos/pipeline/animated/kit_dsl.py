"""The episode data format for the animation kit (pure Python: no drawing libraries needed).

An episode is a list of scenes. Each scene has beats (what is said, by whom, with pauses and cue
names) and actions (what appears on screen, when). Actions are drawn in the order listed, so later
actions sit on top. See videos/pipeline/animated/KIT.md for every action and its options.

Time specs (strings) used by `at`, `until` and inside action options:
    "start" / "end"         the scene's first / last moment
    "cue"                   when the beat with that cue starts speaking
    "cue$"                  when that beat stops speaking
    "cue>"                  when the next beat starts (end of this beat's pause)
    "cue@0.5"               halfway through that beat's speech
    any of the above +/- N  e.g. "cue+1.2", "cue$-0.3", "end-2"
    a number                seconds from the scene start
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Any

from .timeline import NARRATOR, ROSE, PIXI, Beat, SceneScript, SceneTiming

B = Beat  # short alias for episode files
__all__ = ["A", "B", "Beat", "Episode", "Scene", "NARRATOR", "ROSE", "PIXI", "resolve_time", "ACTION_TYPES"]

ACTION_TYPES = {
    # characters and props
    "rose", "pixi", "cat", "grownup", "key", "door", "chair", "laptop", "pointer", "magnifier",
    # text and callouts
    "banner", "chip", "bigtext", "bubble", "thought", "panel", "cards", "icons", "arrow",
    # coding views
    "scratch", "stage", "code", "turtle", "terminal", "tests", "file",
    # diagrams
    "box", "listrow", "dict", "flow", "machine", "timeline", "bars", "grid", "scatter", "table", "tree",
    "stack", "queue", "roadmap",
    # feedback and sound
    "badge", "confetti", "sfx",
}
SETTINGS = {"workshop", "sky", "lavender", "mint", "peach", "night", "stage"}


@dataclass(frozen=True)
class A:
    """One on-screen action: A(kind, text?, at=..., until=..., **options)."""

    kind: str
    text: str = ""
    at: Any = "start"
    until: Any = "end"
    options: dict = field(default_factory=dict)

    def __init__(self, kind: str, text: str = "", at: Any = "start", until: Any = "end", **options: Any) -> None:
        object.__setattr__(self, "kind", kind)
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "at", at)
        object.__setattr__(self, "until", until)
        object.__setattr__(self, "options", options)

    def get(self, name: str, default: Any = None) -> Any:
        return self.options.get(name, default)


@dataclass(frozen=True)
class Scene:
    scene_id: str
    beats: tuple
    actions: tuple = ()
    setting: str = "sky"
    lead_in: float = 0.6
    tail: float = 1.2

    def script(self) -> SceneScript:
        return SceneScript(self.scene_id, tuple(self.beats), lead_in=self.lead_in, tail=self.tail)


@dataclass(frozen=True)
class Episode:
    level: int
    week: int
    scenes: tuple

    @property
    def scripts(self) -> list[SceneScript]:
        return [scene.script() for scene in self.scenes]


_SPEC = re.compile(r"^(?P<base>[A-Za-z_][\w]*|start|end)(?P<mod>[$>]|@(?P<frac>[0-9.]+))?(?P<off>[+-][0-9.]+)?$")


def resolve_time(spec: Any, sc: SceneTiming) -> float:
    """Scene-local seconds for a time spec (see the module docstring)."""
    if isinstance(spec, (int, float)):
        return float(spec)
    text = str(spec).replace(" ", "")
    match = _SPEC.match(text)
    if not match:
        raise ValueError(f"{sc.scene_id}: bad time spec {spec!r}")
    base, mod, frac, off = match.group("base"), match.group("mod"), match.group("frac"), match.group("off")
    if base == "start":
        value = 0.0
    elif base == "end":
        value = sc.duration
    else:
        beat_index = next((i for i, beat in enumerate(sc.beats) if beat.cue == base), None)
        if beat_index is None:
            raise ValueError(f"{sc.scene_id}: no beat with cue {base!r} (time spec {spec!r})")
        beat = sc.beats[beat_index]
        start, end = beat.start - sc.start, beat.end - sc.start
        if mod == "$":
            value = end
        elif mod == ">":
            value = (sc.beats[beat_index + 1].start - sc.start) if beat_index + 1 < len(sc.beats) else sc.duration
        elif frac is not None:
            value = start + float(frac) * (end - start)
        else:
            value = start
    return value + (float(off) if off else 0.0)


def time_specs(value: Any) -> list[Any]:
    """Every time spec mentioned inside an action option (for validation)."""
    found = []
    if isinstance(value, str) and _SPEC.match(value.replace(" ", "")):
        found.append(value)
    elif isinstance(value, (list, tuple)):
        for item in value:
            found += time_specs(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            found += time_specs(key) + time_specs(item)
    return found


TIME_OPTIONS = {"at", "until", "reveal", "active", "done", "highlight", "moods", "wave", "point", "chin", "path",
                "beep", "carrying", "talk", "values", "states", "run", "type", "error", "actions", "checks",
                "current", "token", "items_at", "query", "nearest", "commits", "lines", "swap", "reorder", "open",
                "look", "items"}
