"""Data contracts and deterministic validation for Level 1 videos."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any

from .sources import week_sources

SCHEMA_VERSION = 2
MAX_VIDEO_SECONDS = 300
MIN_VIDEO_SECONDS = 180
MIN_SCENES = 4
MAX_SCENES = 7
# Narration pace used for the timing budget. The voice is asked for about 140 words per minute;
# the budget leaves room for the pause-and-predict moments every scene asks for.
WORDS_PER_MINUTE = 145
# Readability limits for text drawn on a 1920x1080 frame (large type, no tiny captions).
MAX_TITLE_CHARS = 36
MAX_ON_SCREEN_ITEMS = 4
MAX_ON_SCREEN_CHARS = 44
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# US spelling is enforced for every tracked file, this spec included, by testing/test_consistency.py.


@dataclass(frozen=True)
class Scene:
    scene_id: str
    duration_seconds: int
    purpose: str
    narration: str
    visual: str
    on_screen_text: tuple[str, ...]
    production_notes: str

    @property
    def narration_words(self) -> int:
        return len(self.narration.split())

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Scene":
        return cls(
            scene_id=str(value["scene_id"]),
            duration_seconds=int(value["duration_seconds"]),
            purpose=str(value["purpose"]),
            narration=str(value["narration"]),
            visual=str(value["visual"]),
            on_screen_text=tuple(str(item) for item in value["on_screen_text"]),
            production_notes=str(value["production_notes"]),
        )


@dataclass(frozen=True)
class Video:
    week: int
    slug: str
    title: str
    lesson_question: str
    objectives: tuple[str, ...]
    vocabulary: tuple[str, ...]
    misconception: str
    safety_and_citizenship: str
    lesson_handoff: str
    practice_activity: str
    source_files: tuple[str, ...]
    scenes: tuple[Scene, ...]

    @property
    def duration_seconds(self) -> int:
        return sum(scene.duration_seconds for scene in self.scenes)

    @property
    def narration_words(self) -> int:
        return sum(scene.narration_words for scene in self.scenes)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Video":
        return cls(
            week=int(value["week"]),
            slug=str(value["slug"]),
            title=str(value["title"]),
            lesson_question=str(value["lesson_question"]),
            objectives=tuple(str(item) for item in value["objectives"]),
            vocabulary=tuple(str(item) for item in value["vocabulary"]),
            misconception=str(value["misconception"]),
            safety_and_citizenship=str(value["safety_and_citizenship"]),
            lesson_handoff=str(value["lesson_handoff"]),
            practice_activity=str(value.get("practice_activity", "")),
            source_files=tuple(str(item) for item in value["source_files"]),
            scenes=tuple(Scene.from_dict(item) for item in value["scenes"]),
        )


@dataclass(frozen=True)
class Series:
    schema_version: int
    level: int
    audience: str
    series_title: str
    creative_direction: dict[str, Any]
    videos: tuple[Video, ...]
    plan_notes: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Series":
        return cls(
            schema_version=int(value["schema_version"]),
            level=int(value["level"]),
            audience=str(value["audience"]),
            series_title=str(value["series_title"]),
            creative_direction=dict(value["creative_direction"]),
            videos=tuple(Video.from_dict(item) for item in value["videos"]),
            plan_notes=tuple(str(item) for item in value.get("plan_notes", ())),
        )


def load_series(path: Path) -> Series:
    return Series.from_dict(json.loads(path.read_text(encoding="utf-8")))


def scene_word_budget(scene: Scene) -> int:
    return int(scene.duration_seconds * WORDS_PER_MINUTE / 60)


def scene_prefix(level: int, week: int) -> str:
    return f"w{week:02d}-" if level == 1 else f"l{level}-w{week:02d}-"


def validate_video(video: Video, repo_root: Path, level: int = 1) -> list[str]:
    """Deterministic checks for one episode; an empty list means it may ship to review."""
    errors: list[str] = []
    label = f"level {level} week {video.week}" if level != 1 else f"week {video.week}"
    if not SLUG_RE.match(video.slug):
        errors.append(f"{label}: slug '{video.slug}' must be lowercase words joined by hyphens")
    if len(video.title) > MAX_TITLE_CHARS:
        errors.append(f"{label}: title is {len(video.title)} characters; keep it to {MAX_TITLE_CHARS}")
    if not MIN_VIDEO_SECONDS <= video.duration_seconds <= MAX_VIDEO_SECONDS:
        errors.append(
            f"{label}: duration {video.duration_seconds}s is outside "
            f"{MIN_VIDEO_SECONDS}-{MAX_VIDEO_SECONDS}s"
        )
    if len(video.objectives) < 2:
        errors.append(f"{label}: needs at least two instructional objectives")
    if not MIN_SCENES <= len(video.scenes) <= MAX_SCENES:
        errors.append(f"{label}: needs {MIN_SCENES}-{MAX_SCENES} scenes, found {len(video.scenes)}")
    for field in ("lesson_question", "misconception", "safety_and_citizenship", "lesson_handoff"):
        if not str(getattr(video, field)).strip():
            errors.append(f"{label}: {field} is required")

    allowed_sources = set(week_sources(repo_root, video.week, level))
    if not video.source_files:
        errors.append(f"{label}: list the curriculum files the script is based on")
    for source in video.source_files:
        if not (repo_root / source).is_file():
            errors.append(f"{label}: missing source file {source}")
        elif source not in allowed_sources:
            errors.append(
                f"{label}: evidence {source} is not one of this week's fingerprinted sources "
                "(answers and tests are never evidence for a video)"
            )

    activity = video.practice_activity.rstrip("/")
    if not activity:
        errors.append(f"{label}: practice_activity must name the exercise or project file the video hands off to")
    elif not (repo_root / activity).exists():
        errors.append(f"{label}: practice_activity {activity} does not exist")
    elif not any(source == activity or source.startswith(activity + "/") for source in allowed_sources):
        errors.append(f"{label}: practice_activity {activity} is not part of this week's material")

    for scene in video.scenes:
        sid = scene.scene_id
        prefix = scene_prefix(level, video.week)
        if not sid.startswith(prefix):
            errors.append(f"{sid}: scene ids for this week start with '{prefix}'")
        if scene.duration_seconds <= 0:
            errors.append(f"{sid}: duration must be positive")
        if not scene.narration.strip() or not scene.visual.strip():
            errors.append(f"{sid}: narration and visual are required")
        if not scene.production_notes.strip():
            errors.append(f"{sid}: production notes are required")
        if scene.narration_words > scene_word_budget(scene):
            errors.append(
                f"{sid}: {scene.narration_words} narration words exceed the "
                f"{scene_word_budget(scene)}-word budget for {scene.duration_seconds}s"
            )
        if not scene.on_screen_text:
            errors.append(f"{sid}: needs readable on-screen text")
        if len(scene.on_screen_text) > MAX_ON_SCREEN_ITEMS:
            errors.append(f"{sid}: at most {MAX_ON_SCREEN_ITEMS} on-screen text items fit on screen")
        for item in scene.on_screen_text:
            if len(item) > MAX_ON_SCREEN_CHARS:
                errors.append(f"{sid}: on-screen text '{item}' is longer than {MAX_ON_SCREEN_CHARS} characters")
    return errors


def validate_series(series: Series, repo_root: Path, level: int | None = None) -> list[str]:
    """Return human-readable errors; an empty list means the spec is shippable."""
    errors: list[str] = []
    if series.schema_version != SCHEMA_VERSION:
        errors.append(f"unsupported schema_version {series.schema_version}; expected {SCHEMA_VERSION}")
    if level is not None and series.level != level:
        errors.append(f"expected a Level {level} spec, found Level {series.level}")
    if series.level not in (1, 2, 3):
        errors.append(f"unknown level {series.level}")
    weeks = [video.week for video in series.videos]
    if weeks != list(range(1, 13)):
        errors.append(f"videos must cover weeks 1-12 in order; found {weeks}")

    scene_ids: set[str] = set()
    slugs: set[str] = set()
    for video in series.videos:
        errors.extend(validate_video(video, repo_root, series.level))
        if video.slug in slugs:
            errors.append(f"duplicate slug {video.slug}")
        slugs.add(video.slug)
        for scene in video.scenes:
            if scene.scene_id in scene_ids:
                errors.append(f"duplicate scene id {scene.scene_id}")
            scene_ids.add(scene.scene_id)
    return errors
