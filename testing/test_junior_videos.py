"""Junior teaching videos (Aiden and Pixi, Grades 2-3).

For the junior track the episode files (videos/pipeline/animated/episodes/j{L}w{WW}.py) are the
source; `python -m videos.pipeline.cli junior-spec --level L` writes videos/specs/junior{L}.json from
them. These checks keep the two in step, keep Aiden as the host, keep every episode in the junior
length budget, and keep what children see and hear inside Grade 2-3 math.
"""

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
EPISODES = ROOT / "videos" / "pipeline" / "animated" / "episodes"
JUNIOR = sorted(EPISODES.glob("j[1-3]w[0-9][0-9].py"))


def _episode(path):
    import importlib

    return importlib.import_module(f"videos.pipeline.animated.episodes.{path.stem}").EPISODE


@pytest.mark.parametrize("level", sorted({int(p.stem[1]) for p in JUNIOR}))
def test_junior_spec_is_written_from_the_episodes(level):
    from videos.pipeline.cli import build_junior_spec

    spec = ROOT / "videos" / "specs" / f"junior{level}.json"
    assert spec.is_file(), f"run: python -m videos.pipeline.cli junior-spec --level {level}"
    assert json.loads(spec.read_text(encoding="utf-8")) == build_junior_spec(level), \
        f"{spec.name} is stale; run: python -m videos.pipeline.cli junior-spec --level {level}"


@pytest.mark.parametrize("path", JUNIOR, ids=lambda p: p.stem)
def test_aiden_hosts_every_junior_episode(path):
    from videos.pipeline.animated.timeline import AIDEN, ROSE

    episode = _episode(path)
    assert episode.level == path.stem[:2] and episode.week == int(path.stem[3:5])
    beats = [b for script in episode.scripts for b in script.beats]
    words = {speaker: sum(len(b.text.split()) for b in beats if b.speaker == speaker) for speaker in {b.speaker for b in beats}}
    total = sum(words.values())
    assert words.get(ROSE, 0) == 0, "Rose belongs to the main track; the junior host is Aiden"
    assert words.get(AIDEN, 0) >= 0.7 * total, f"Aiden should say most of the episode ({words})"
    assert not any(a.kind == "rose" for sc in episode.scenes for a in sc.actions)
    assert 600 <= total <= 950, f"a junior episode has about 650-850 spoken words, this one has {total}"


MATH = [
    (re.compile(r"(?:(?<=[\s(\[])|^)[-−]\d"), "a negative number"),
    (re.compile(r"\b[xy]:\s*-?\d"), "an x/y position"),
    (re.compile(r"360\s*(?:÷|/|divided)", re.I), "360 divided by sides"),
    (re.compile(r"\bminus\b|\bnegative\b", re.I), "a negative number in speech"),
]


@pytest.mark.parametrize("path", JUNIOR, ids=lambda p: p.stem)
def test_junior_episode_stays_in_grade_2_3_math(path):
    episode = _episode(path)
    seen = [b.text for script in episode.scripts for b in script.beats]
    for scene in episode.scenes:
        for action in scene.actions:
            seen += [action.text] if action.text else []
            for block in _blocks(action.get("blocks", [])):
                seen.append(block)
    bad = [f"{why}: {text[:70]}" for text in seen for pattern, why in MATH if pattern.search(text)]
    assert not bad, "\n".join(bad)


def _blocks(blocks):
    for block in blocks:
        yield block[1]
        for inner in block[2:]:
            if isinstance(inner, (list, tuple)):
                yield from _blocks(inner)


def test_aiden_uses_the_high_quality_grades_4_6_narration_voice():
    pytest.importorskip("numpy")
    from videos.pipeline.animated.audio import VOICES
    from videos.pipeline.animated.timeline import AIDEN, NARRATOR

    assert VOICES[AIDEN] == VOICES[NARRATOR]
    assert "pitch" not in VOICES[AIDEN], "pitch processing reduces the natural voice quality"


def test_grade_bands_have_separate_generated_video_folders():
    from videos.pipeline.cli import output_dir

    assert output_dir("j1").parts[-2:] == ("output", "grades-2-3")
    assert output_dir(1).parts[-2:] == ("output", "grades-4-6")
    assert output_dir("j1") != output_dir(1)


@pytest.mark.parametrize("path", JUNIOR, ids=lambda p: p.stem)
def test_junior_episode_fits_its_time(path):
    """5-7 minutes, measured with the real voices (skipped when the voice model is not installed)."""
    pytest.importorskip("kokoro_onnx")
    from videos.pipeline.animated import audio

    if any(not (audio.MODEL_DIR / name).is_file() for name in audio.MODEL_FILES):
        pytest.skip("voice model not installed (python -m videos.pipeline.cli fetch-voice)")
    from videos.pipeline.animated.render import timeline_summary

    _, total = timeline_summary(int(path.stem[3:5]), path.stem[:2])
    assert 300 <= total <= 430, f"{path.stem} runs {total:.0f} s; junior episodes run 5-7 minutes"
