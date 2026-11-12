"""Which tracks and levels the course has, read from ``curriculum.json``.

Every tool and test that used to hard-code the three level folders or the
twelve weeks asks this module instead::

    import curriculum                       # with tools/ on sys.path
    for level in curriculum.levels():       # active levels of every track
        print(level.key, level.dir, level.week_names)

``levels()`` returns only *active* levels unless ``include_planned=True``:
a planned level is declared (so its folder, syllabus and key are reserved)
but has no lessons yet, so builds, the student copy and the quality gate
must not expect any.

Standard library only: the tests run on Thonny's Python 3.10 without extra
packages, and 3.10 has no ``tomllib``, hence JSON.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "curriculum.json"
STATUSES = ("active", "planned")


@dataclass(frozen=True)
class Level:
    track: str           # track id, e.g. "main" or "junior"
    key: str             # unique CLI key: "1", "2", "3", "j1", ...
    number: int          # level number inside its track (1, 2, 3)
    dir: str             # folder relative to the repository root
    title: str
    goal_prefix: str     # goal codes look like <prefix>.G1, e.g. L1.G1 or J1.G1
    weeks: int           # core weekly sessions
    buffers: int         # optional buffer sessions (buffer1, buffer2, ...)
    status: str          # "active" or "planned"
    syllabus: str        # the track's scope-and-sequence document

    @property
    def path(self) -> Path:
        return ROOT / self.dir

    @property
    def active(self) -> bool:
        return self.status == "active"

    @property
    def week_names(self) -> list[str]:
        return [f"week{n:02d}" for n in range(1, self.weeks + 1)]

    @property
    def buffer_names(self) -> list[str]:
        return [f"buffer{n}" for n in range(1, self.buffers + 1)]

    @property
    def session_names(self) -> list[str]:
        """All lesson files in teaching order: weeks, then buffers."""
        return self.week_names + self.buffer_names


@dataclass(frozen=True)
class Track:
    id: str
    title: str
    grades: str
    ages: str
    syllabus: str
    levels: tuple[Level, ...]


def load(config: Path = CONFIG) -> list[Track]:
    """Parse and validate the config; raise ValueError on any mistake."""
    data = json.loads(config.read_text(encoding="utf-8"))
    tracks, keys, dirs, errors = [], set(), set(), []
    for t in data["tracks"]:
        levels = []
        for raw in t["levels"]:
            level = Level(track=t["id"], syllabus=t["syllabus"], **raw)
            where = f"{t['id']}/{level.key}"
            if level.key in keys:
                errors.append(f"{where}: duplicate key")
            if level.dir in dirs:
                errors.append(f"{where}: duplicate dir {level.dir}")
            if level.status not in STATUSES:
                errors.append(f"{where}: status must be one of {STATUSES}")
            if not 1 <= level.weeks <= 20 or not 0 <= level.buffers <= 5:
                errors.append(f"{where}: weeks must be 1-20 and buffers 0-5")
            keys.add(level.key)
            dirs.add(level.dir)
            levels.append(level)
        tracks.append(Track(id=t["id"], title=t["title"], grades=t["grades"], ages=t["ages"],
                            syllabus=t["syllabus"], levels=tuple(levels)))
    if errors:
        raise ValueError("curriculum.json: " + "; ".join(errors))
    return tracks


def levels(track: str | None = None, *, include_planned: bool = False) -> list[Level]:
    """Levels in config order, optionally for one track; active only by default."""
    return [lv for t in load() if track in (None, t.id) for lv in t.levels
            if include_planned or lv.active]


def by_key(key: str) -> Level:
    for lv in levels(include_planned=True):
        if lv.key == key:
            return lv
    raise KeyError(f"no level with key {key!r} in curriculum.json")


def by_dir(folder: str) -> Level:
    for lv in levels(include_planned=True):
        if lv.dir == folder:
            return lv
    raise KeyError(f"no level with dir {folder!r} in curriculum.json")


def level_of(path: Path) -> Level:
    """The level a file inside the repository belongs to."""
    rel = path.resolve().relative_to(ROOT).as_posix() + "/"
    for lv in levels(include_planned=True):
        if rel.startswith(lv.dir + "/"):
            return lv
    raise KeyError(f"{path} is not inside any level folder")
