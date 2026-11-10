"""Offline contract tests for the Level 1 teaching-video pipeline."""

from __future__ import annotations

import json
from pathlib import Path

from videos.pipeline.markdown import render_plan
from videos.pipeline.media import write_captions
from videos.pipeline.models import MAX_VIDEO_SECONDS, load_series, validate_series
from videos.pipeline.sources import build_manifest, stale_weeks

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "videos" / "specs" / "level1.json"
PLAN = ROOT / "videos" / "video-plan-level1.md"
MANIFEST = ROOT / "videos" / "manifest-level1.json"


def test_level1_video_contract_is_complete_and_valid() -> None:
    series = load_series(SPEC)
    assert validate_series(series, ROOT) == []
    assert [video.week for video in series.videos] == list(range(1, 13))
    assert all(video.duration_seconds <= MAX_VIDEO_SECONDS for video in series.videos)
    assert all(video.misconception.strip() for video in series.videos)


def test_readable_plan_is_reproducible() -> None:
    series = load_series(SPEC)
    assert PLAN.read_text(encoding="utf-8") == render_plan(series)


def test_curriculum_manifest_has_no_drift() -> None:
    assert stale_weeks(ROOT, MANIFEST) == []
    tracked = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert tracked == build_manifest(ROOT)


def test_every_scene_has_accessible_text_and_production_direction() -> None:
    series = load_series(SPEC)
    for video in series.videos:
        for scene in video.scenes:
            assert scene.on_screen_text
            assert scene.visual.strip()
            assert scene.production_notes.strip()


def test_caption_track_uses_short_readable_cues(tmp_path: Path) -> None:
    video = load_series(SPEC).videos[0]
    destination = tmp_path / "week01.srt"
    write_captions(video, destination)
    cues = destination.read_text(encoding="utf-8").strip().split("\n\n")
    assert len(cues) > len(video.scenes)
    for cue in cues:
        lines = cue.splitlines()
        assert " --> " in lines[1]
        assert all(len(line) <= 42 for line in lines[2:])
