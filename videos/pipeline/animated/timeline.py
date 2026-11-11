"""Beats, scene scripts and the audio-driven timeline (pure Python, no media dependencies).

An animated episode is written as beats: one sentence or phrase each, with a speaker, an
optional pause after it, and an optional cue name the drawing code can look up. The spoken
beats of a scene must add up to exactly that scene's narration in `videos/specs/level1.json`,
so the spec stays the single source of truth for what is said (and captioned).
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re

NARRATOR = "narrator"
ROSE = "rose"
PIXI = "pixi"
SPEAKERS = (NARRATOR, ROSE, PIXI)


@dataclass(frozen=True)
class Beat:
    text: str
    speaker: str = NARRATOR
    pause: float = 0.25  # seconds of silence after the beat
    cue: str = ""  # name the scene's drawing code uses to time an animation


@dataclass(frozen=True)
class SceneScript:
    scene_id: str
    beats: tuple[Beat, ...]
    lead_in: float = 0.6  # seconds before the first beat (scene settles, transition ends)
    tail: float = 1.2  # seconds after the last beat


def normalize(text: str) -> str:
    return " ".join(text.replace("’", "'").replace("‘", "'").split())


def joined_text(script: SceneScript) -> str:
    return normalize(" ".join(beat.text for beat in script.beats))


def check_against_spec(scripts: list[SceneScript], spec_video: dict) -> list[str]:
    """Errors when the beats no longer say exactly what the spec says."""
    errors = []
    scenes = {scene["scene_id"]: scene for scene in spec_video["scenes"]}
    if [script.scene_id for script in scripts] != list(scenes):
        errors.append(f"week {spec_video['week']}: animated scenes {[s.scene_id for s in scripts]} "
                      f"do not match the spec's {list(scenes)}")
    for script in scripts:
        scene = scenes.get(script.scene_id)
        if scene is None:
            continue
        if joined_text(script) != normalize(scene["narration"]):
            errors.append(f"{script.scene_id}: animated beats do not match the spec narration")
        for beat in script.beats:
            if beat.speaker not in SPEAKERS:
                errors.append(f"{script.scene_id}: unknown speaker {beat.speaker!r}")
    return errors


@dataclass
class BeatTiming:
    text: str
    speaker: str
    cue: str
    start: float
    end: float
    envelope: list[float] = field(default_factory=list)  # mouth-open values, one per video frame


@dataclass
class SceneTiming:
    scene_id: str
    start: float
    end: float
    beats: list[BeatTiming]

    @property
    def duration(self) -> float:
        return self.end - self.start

    def cue(self, name: str) -> BeatTiming:
        for beat in self.beats:
            if beat.cue == name:
                return beat
        raise KeyError(f"{self.scene_id}: no beat with cue {name!r}")

    def at(self, name: str) -> float:
        """Scene-local start time of the beat with this cue."""
        return self.cue(name).start - self.start

    def end_of(self, name: str) -> float:
        return self.cue(name).end - self.start

    def speaking(self, speaker: str, t_local: float, fps: int) -> float:
        """Mouth-open amount (0-1) for a character at scene-local time t."""
        t = self.start + t_local
        for beat in self.beats:
            if beat.speaker == speaker and beat.start <= t < beat.end and beat.envelope:
                index = int((t - beat.start) * fps)
                return beat.envelope[min(index, len(beat.envelope) - 1)]
        return 0.0


def build_timeline(scripts: list[SceneScript], durations: list[list[float]], intro: float,
                   outro: float, envelopes: list[list[list[float]]] | None = None) -> tuple[list[SceneTiming], float]:
    """Place every beat on one clock. `durations[s][b]` is the spoken length of beat b in scene s."""
    scenes: list[SceneTiming] = []
    clock = intro
    for s_index, script in enumerate(scripts):
        start = clock
        clock += script.lead_in
        beats = []
        for b_index, beat in enumerate(script.beats):
            length = durations[s_index][b_index]
            envelope = envelopes[s_index][b_index] if envelopes else []
            beats.append(BeatTiming(beat.text, beat.speaker, beat.cue, clock, clock + length, envelope))
            clock += length + beat.pause
        clock += script.tail
        scenes.append(SceneTiming(script.scene_id, start, clock, beats))
    return scenes, clock + outro


def caption_beats(scenes: list[SceneTiming]) -> list[tuple[float, float, str]]:
    """(start, end, text) for every spoken beat, in order."""
    return [(beat.start, beat.end, beat.text) for scene in scenes for beat in scene.beats]


_SPLIT = re.compile(r"(?<=[.!?…])\s+")


def sentences(text: str) -> list[str]:
    return [part for part in _SPLIT.split(normalize(text)) if part]
