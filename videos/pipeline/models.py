"""Data contracts and deterministic validation for Level 1 videos."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

MAX_VIDEO_SECONDS = 300
MIN_VIDEO_SECONDS = 180
WORDS_PER_MINUTE = 145


@dataclass(frozen=True)
class Scene:
    scene_id: str
    duration_seconds: int
    purpose: str
    narration: str
    visual: str
    on_screen_text: tuple[str, ...]
    production_notes: str

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
    source_files: tuple[str, ...]
    scenes: tuple[Scene, ...]

    @property
    def duration_seconds(self) -> int:
        return sum(scene.duration_seconds for scene in self.scenes)

    @property
    def narration_words(self) -> int:
        return sum(len(scene.narration.split()) for scene in self.scenes)

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

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Series":
        return cls(
            schema_version=int(value["schema_version"]),
            level=int(value["level"]),
            audience=str(value["audience"]),
            series_title=str(value["series_title"]),
            creative_direction=dict(value["creative_direction"]),
            videos=tuple(Video.from_dict(item) for item in value["videos"]),
        )


def load_series(path: Path) -> Series:
    return Series.from_dict(json.loads(path.read_text(encoding="utf-8")))


def validate_series(series: Series, repo_root: Path) -> list[str]:
    """Return human-readable errors; an empty list means the spec is shippable."""
    errors: list[str] = []
    if series.schema_version != 1:
        errors.append(f"unsupported schema_version {series.schema_version}")
    if series.level != 1:
        errors.append("the Level 1 pipeline received a different level")
    weeks = [video.week for video in series.videos]
    if weeks != list(range(1, 13)):
        errors.append(f"videos must cover weeks 1-12 in order; found {weeks}")

    scene_ids: set[str] = set()
    for video in series.videos:
        if not MIN_VIDEO_SECONDS <= video.duration_seconds <= MAX_VIDEO_SECONDS:
            errors.append(
                f"week {video.week}: duration {video.duration_seconds}s is outside "
                f"{MIN_VIDEO_SECONDS}-{MAX_VIDEO_SECONDS}s"
            )
        spoken_capacity = video.duration_seconds * WORDS_PER_MINUTE / 60
        if video.narration_words > spoken_capacity:
            errors.append(
                f"week {video.week}: {video.narration_words} narration words exceed "
                f"the {int(spoken_capacity)}-word timing budget"
            )
        if len(video.objectives) < 2:
            errors.append(f"week {video.week}: needs at least two instructional objectives")
        if len(video.scenes) < 4:
            errors.append(f"week {video.week}: needs at least four scenes")
        for source in video.source_files:
            if not (repo_root / source).is_file():
                errors.append(f"week {video.week}: missing source file {source}")
        for scene in video.scenes:
            if scene.scene_id in scene_ids:
                errors.append(f"duplicate scene id {scene.scene_id}")
            scene_ids.add(scene.scene_id)
            if scene.duration_seconds <= 0:
                errors.append(f"{scene.scene_id}: duration must be positive")
            if not scene.narration.strip() or not scene.visual.strip():
                errors.append(f"{scene.scene_id}: narration and visual are required")
            if not scene.on_screen_text:
                errors.append(f"{scene.scene_id}: needs readable on-screen text")
    return errors
