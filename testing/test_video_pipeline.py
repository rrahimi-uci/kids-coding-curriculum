"""Offline contract tests for the Level 1 teaching-video pipeline (no API key, no network)."""

from __future__ import annotations

import dataclasses
import json
import re
from pathlib import Path

import pytest

from videos.pipeline import cli
from videos.pipeline.markdown import render_plan
from videos.pipeline.media import (
    caption_chunks,
    caption_cues,
    needs_approval,
    transcript_similarity,
    write_captions,
    write_webvtt,
)
from videos.pipeline.models import (
    MAX_ON_SCREEN_CHARS,
    MAX_VIDEO_SECONDS,
    load_series,
    scene_word_budget,
    validate_series,
    validate_video,
)
from videos.pipeline.sources import (
    build_manifest,
    changed_files,
    stale_weeks,
    update_manifest_weeks,
    week_sources,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "videos" / "specs" / "level1.json"
PLAN = ROOT / "videos" / "video-plan-level1.md"
MANIFEST = ROOT / "videos" / "manifest-level1.json"


@pytest.fixture(scope="module")
def series():
    return load_series(SPEC)


def _week(series, number):
    return next(video for video in series.videos if video.week == number)


# --------------------------------------------------------------------------- the tracked content
def test_level1_video_contract_is_complete_and_valid(series) -> None:
    assert validate_series(series, ROOT) == []
    assert [video.week for video in series.videos] == list(range(1, 13))
    assert all(video.duration_seconds <= MAX_VIDEO_SECONDS for video in series.videos)
    assert all(video.misconception.strip() for video in series.videos)


def test_readable_plan_is_reproducible(series) -> None:
    assert PLAN.read_text(encoding="utf-8") == render_plan(series)


def test_curriculum_manifest_has_no_drift() -> None:
    assert stale_weeks(ROOT, MANIFEST) == []
    tracked = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert tracked == build_manifest(ROOT)


def test_every_scene_has_accessible_text_and_production_direction(series) -> None:
    for video in series.videos:
        for scene in video.scenes:
            assert 1 <= len(scene.on_screen_text) <= 4
            assert all(len(item) <= MAX_ON_SCREEN_CHARS for item in scene.on_screen_text)
            assert scene.visual.strip()
            assert scene.production_notes.strip()
            assert scene.narration_words <= scene_word_budget(scene)


def test_audience_matches_the_grade_4_5_course(series) -> None:
    assert "Grades 4–5" in series.audience
    assert "ages 9–11" in series.audience


def test_every_video_hands_off_to_this_weeks_activity(series) -> None:
    for video in series.videos:
        activity = video.practice_activity
        assert (ROOT / activity).exists()
        assert any(path.startswith(activity) for path in week_sources(ROOT, video.week))


def test_python_episodes_use_the_course_turtle_pattern(series) -> None:
    """Course starters use `t = turtle.Turtle()` and `t.forward(...)`, never module-level calls."""
    for video in series.videos:
        if video.week < 7:
            continue
        for scene in video.scenes:
            for item in scene.on_screen_text:
                assert "turtle.forward" not in item and "turtle.left" not in item, scene.scene_id


# --------------------------------------------------------------------------- spoiler protection
def test_answers_and_tests_are_never_video_evidence() -> None:
    for week in range(1, 13):
        for path in week_sources(ROOT, week):
            name = Path(path).name
            assert name not in {"solution.py", "solution.md", "check_my_work.py"}, path
            assert not name.startswith("test_"), path


def test_validation_rejects_an_answer_file_as_evidence(series) -> None:
    video = _week(series, 7)
    leaked = dataclasses.replace(
        video, source_files=video.source_files + ("1-introduction/exercises/week07/ex-typo-hunt/solution.py",)
    )
    assert any("not one of this week's fingerprinted sources" in error for error in validate_video(leaked, ROOT))


# --------------------------------------------------------------------------- validation rules
def test_validation_catches_unreadable_and_overlong_scenes(series) -> None:
    video = _week(series, 2)
    scene = video.scenes[0]
    crowded = dataclasses.replace(scene, on_screen_text=("A", "B", "C", "D", "E"))
    long_text = dataclasses.replace(scene, on_screen_text=("x" * (MAX_ON_SCREEN_CHARS + 1),))
    wordy = dataclasses.replace(scene, narration="word " * (scene_word_budget(scene) + 1))
    for broken_scene, expected in ((crowded, "at most 4"), (long_text, "longer than"), (wordy, "word budget")):
        broken = dataclasses.replace(video, scenes=(broken_scene,) + video.scenes[1:])
        assert any(expected in error for error in validate_video(broken, ROOT)), expected


def test_validation_requires_a_real_practice_activity(series) -> None:
    video = _week(series, 3)
    missing = dataclasses.replace(video, practice_activity="")
    elsewhere = dataclasses.replace(video, practice_activity="1-introduction/exercises/week01/ex-hello-cat")
    assert any("practice_activity must name" in e for e in validate_video(missing, ROOT))
    assert any("not part of this week's material" in e for e in validate_video(elsewhere, ROOT))


# --------------------------------------------------------------------------- manifest workflow
def test_changed_files_names_the_file_that_changed(tmp_path: Path) -> None:
    manifest = build_manifest(ROOT)
    lesson = "1-introduction/teaching-material/lessons/week02.tex"
    manifest["weeks"]["2"]["files"][lesson] = "0" * 64
    manifest["weeks"]["2"]["digest"] = "stale"
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert changed_files(ROOT, path) == {2: [lesson]}


def test_accepting_one_week_keeps_other_weeks_stale(tmp_path: Path) -> None:
    manifest = build_manifest(ROOT)
    for week in ("3", "5"):
        manifest["weeks"][week]["digest"] = "stale"
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    update_manifest_weeks(ROOT, path, [5])
    assert stale_weeks(ROOT, path) == [3]


def test_old_manifest_format_asks_for_a_review(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({"schema_version": 1, "weeks": {}}), encoding="utf-8")
    with pytest.raises(ValueError, match="accept --all"):
        changed_files(ROOT, path)


# --------------------------------------------------------------------------- captions
def test_caption_track_uses_short_readable_cues(series, tmp_path: Path) -> None:
    video = series.videos[0]
    destination = tmp_path / "week01.srt"
    write_captions(video, destination)
    cues = destination.read_text(encoding="utf-8").strip().split("\n\n")
    assert len(cues) > len(video.scenes)
    for cue in cues:
        lines = cue.splitlines()
        assert " --> " in lines[1]
        assert 1 <= len(lines[2:]) <= 2
        assert all(len(line) <= 42 for line in lines[2:])


def test_captions_follow_the_measured_speech_and_stay_inside_each_scene(series) -> None:
    video = series.videos[0]
    spoken = [10.0] * len(video.scenes)
    cues = caption_cues(video, spoken)
    scene_start = 0.0
    words = []
    for scene in video.scenes:
        inside = [cue for cue in cues if scene_start <= cue[0] < scene_start + scene.duration_seconds]
        assert inside[-1][1] <= scene_start + spoken[0] + 1.0  # captions end when the voice stops
        words += " ".join(cue[2] for cue in inside).split()
        scene_start += scene.duration_seconds
    assert words == " ".join(scene.narration for scene in video.scenes).split()  # every word captioned once


def test_caption_chunks_prefer_sentence_boundaries() -> None:
    chunks = caption_chunks("Order matters. Change one thing, then test again and again until it works well.")
    assert chunks[0] == "Order matters."
    assert all(len(chunk) <= 84 for chunk in chunks)


def test_webvtt_file_is_valid(series, tmp_path: Path) -> None:
    destination = tmp_path / "week01.vtt"
    write_webvtt(series.videos[0], destination)
    text = destination.read_text(encoding="utf-8")
    assert text.startswith("WEBVTT\n")
    assert "00:00:00.000 --> " in text


# --------------------------------------------------------------------------- render gates
def test_only_paid_providers_need_approval() -> None:
    assert needs_approval("cards", "openai-realtime")
    assert needs_approval("openai", "silent")
    assert not needs_approval("cards", "macos-say")
    assert not needs_approval("cards", "silent")


def test_render_refuses_paid_calls_without_approval(capsys) -> None:
    assert cli.main(["render", "--week", "1"]) == 2
    assert "--approved" in capsys.readouterr().err


def test_transcript_check_rejects_a_paraphrased_read() -> None:
    script = "Order matters. Change one thing, then test again."
    assert transcript_similarity(script, "Order matters! Change one thing, then test again.") == 1.0
    assert transcript_similarity(script, "Sure! Here is a fun idea: just try lots of things.") < 0.5


# --------------------------------------------------------------------------- optional dependencies
def test_scene_cards_render_symbols_and_fit_the_frame(series, tmp_path: Path) -> None:
    pytest.importorskip("PIL")
    from PIL import Image

    from videos.pipeline import media

    video = _week(series, 11)
    scene = video.scenes[1]  # contains a check mark the course font does not have
    destination = tmp_path / "card.png"
    media.render_scene_card(video, scene, destination, 2, len(video.scenes), "Narration uses an AI-generated voice")
    with Image.open(destination) as image:
        assert image.size == (media.WIDTH, media.HEIGHT)
    font = media._font(40, bold=True)
    if media._fallback_font(40) is not None:
        assert len(media._runs("M1 Plan ✓", font)) == 2


def test_agent_drafts_keep_week_and_slug_stable(series) -> None:
    pytest.importorskip("pydantic")
    from videos.pipeline.agents_workflow import VideoDraft, _pin_identity

    current = json.loads(SPEC.read_text(encoding="utf-8"))["videos"][6]
    draft = VideoDraft.model_validate({**current, "week": 99, "slug": "renamed-by-the-model"})
    pinned = _pin_identity(draft, 7, current)
    assert (pinned.week, pinned.slug) == (7, current["slug"])


# --------------------------------------------------------------------------- animated episodes
def test_animated_beats_say_exactly_the_spec_narration() -> None:
    from videos.pipeline.animated.timeline import check_against_spec

    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    hand_made = sorted(int(p.stem[4:6]) for p in (ROOT / "videos/pipeline/animated/episodes").glob("week[0-9][0-9]_script.py"))
    assert 1 in hand_made
    for week in hand_made:
        script = __import__(f"videos.pipeline.animated.episodes.week{week:02d}_script", fromlist=["SCRIPTS"])
        video = next(v for v in spec["videos"] if v["week"] == week)
        assert check_against_spec(script.SCRIPTS, video) == []
        for scene in script.SCRIPTS:
            names = [beat.cue for beat in scene.beats]
            assert len(names) == len(set(names)), scene.scene_id


def test_animated_timeline_places_beats_in_order() -> None:
    from videos.pipeline.animated.timeline import Beat, SceneScript, build_timeline

    scripts = [SceneScript("w01-s01", (Beat("One.", cue="a", pause=0.5), Beat("Two.", cue="b")), lead_in=1.0, tail=2.0)]
    scenes, total = build_timeline(scripts, [[2.0, 3.0]], intro=4.0, outro=5.0)
    scene = scenes[0]
    assert (scene.start, scene.at("a"), scene.at("b"), scene.end_of("b")) == (4.0, 1.0, 3.5, 6.5)
    assert scene.end == 4.0 + 1.0 + 2.0 + 0.5 + 3.0 + 0.25 + 2.0
    assert total == scene.end + 5.0


def test_synthesized_music_and_effects_are_clean() -> None:
    np = pytest.importorskip("numpy")
    from videos.pipeline.animated import audio

    bed = audio.music_bed(12.0, intro=4.0, outro_start=8.0)
    assert len(bed) == 12 * audio.SR and np.isfinite(bed).all() and np.abs(bed).max() < 1.5
    for name in audio.SFX_GAIN:
        sound = audio.sfx(name)
        assert len(sound) > 0 and np.isfinite(sound).all(), name
    stereo = audio.mix(6.0, [(1.0, np.sin(np.linspace(0, 2000, audio.SR)) * 0.5)], [(0.5, "pop")], 1.0, 5.0)
    assert stereo.shape[1] == 2 and np.abs(stereo).max() <= 1.0


# --------------------------------------------------------------------------- all levels and kit episodes
def _spec_levels():
    return [level for level in (1, 2, 3) if (ROOT / "videos" / "specs" / f"level{level}.json").is_file()]


@pytest.mark.parametrize("level", _spec_levels())
def test_every_level_spec_is_valid_synced_and_current(level) -> None:
    spec = ROOT / "videos" / "specs" / f"level{level}.json"
    series = load_series(spec)
    assert series.level == level
    assert validate_series(series, ROOT, level) == []
    assert (ROOT / "videos" / f"video-plan-level{level}.md").read_text(encoding="utf-8") == render_plan(series)
    assert stale_weeks(ROOT, ROOT / "videos" / f"manifest-level{level}.json") == []


def _kit_episodes():
    from videos.pipeline.animated.episode_check import kit_episodes

    return kit_episodes()


@pytest.mark.parametrize("level_week", _kit_episodes(), ids=lambda lw: f"l{lw[0]}w{lw[1]:02d}")
def test_kit_episode_matches_spec_and_shows_real_code_output(level_week) -> None:
    from videos.pipeline.animated.episode_check import check_episode

    assert check_episode(*level_week) == []


def test_python_shown_in_videos_runs_with_the_course_turtle() -> None:
    from videos.pipeline.animated import pyrun

    result = pyrun.run("import turtle\nt = turtle.Turtle()\nfor i in range(3):\n    t.forward(50)\n    t.left(120)\n")
    assert [item[0] for item in result["draw"]] == ["line"] * 3 and result["error"] == ""
    shell = pyrun.shell_lines(pyrun.run('n = input("How many? ")\nprint(n + 1)', inputs=("4",)))
    assert shell == ["How many? 4", 'TypeError: can only concatenate str (not "int") to str']


def test_voice_reads_code_like_a_teacher_while_captions_keep_it_written() -> None:
    from videos.pipeline.animated.speech import spoken_form

    assert spoken_form("Nova saves self.height in stickers.txt and rocket.py.") == (
        "Nova saves self dot height in stickers dot T X T and rocket dot pie.")
    assert spoken_form("__init__ and git config --global user.name") == (
        "dunder init and git config dash dash global user dot name")
    assert spoken_form("my_shape and flag_drawing.py") == "my underscore shape and flag underscore drawing dot pie"
    assert spoken_form("screen.onkey and screen.ontimer, not a monkey") == (
        "screen dot on key and screen dot on timer, not a monkey")
    assert spoken_form("It is 2.5, then 3. Done… Next.") == "It is 2.5, then 3. Done… Next."  # numbers, sentences


@pytest.mark.parametrize("level", [1, 2, 3])
def test_narration_has_no_code_syntax_the_voice_would_read_badly(level) -> None:
    """Code is described in words; only names the voice can read (self.height, stickers.txt) are written as code."""
    series = load_series(ROOT / "videos" / "specs" / f"level{level}.json")
    awkward = re.compile(r"[\[\]{}=<>#`\\]|\w\((?!\))|\b\w+ of \d|\b(dot|underscore|dunder) [a-z]+\b")
    found = [f"week {video.week} {scene.scene_id}: {match.group(0)!r}"
             for video in series.videos for scene in video.scenes
             for match in awkward.finditer(scene.narration)]
    assert not found, "\n".join(found)
