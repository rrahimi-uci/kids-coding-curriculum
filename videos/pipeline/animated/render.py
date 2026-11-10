"""Render an animated episode: voices -> timeline -> audio mix -> frames (in parallel) -> MP4 + captions."""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
import dataclasses
import importlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from .timeline import BeatTiming, SceneTiming, build_timeline, check_against_spec

REPO_ROOT = Path(__file__).resolve().parents[3]
SPEC_PATH = REPO_ROOT / "videos" / "specs" / "level1.json"
TRANSITION = 0.55  # seconds of circular wipe between scenes


def episode_modules(week: int):
    script = importlib.import_module(f"videos.pipeline.animated.episodes.week{week:02d}_script")
    drawing = importlib.import_module(f"videos.pipeline.animated.episodes.week{week:02d}")
    return script, drawing


def available_weeks() -> list[int]:
    folder = Path(__file__).parent / "episodes"
    return sorted(int(p.stem[4:6]) for p in folder.glob("week[0-9][0-9].py"))


# --------------------------------------------------------------------------- frame drawing (runs in workers)
def _scene_at(scenes: list[SceneTiming], t: float) -> int:
    for index, scene in enumerate(scenes):
        if t < scene.end:
            return index
    return len(scenes) - 1


def draw_frame(drawing, scenes: list[SceneTiming], total: float, t: float):
    from . import engine, props

    surface, ctx = engine.new_frame()
    outro_start = scenes[-1].end

    def paint(slot: int, when: float) -> None:
        if slot < 0:
            drawing.intro(ctx, when, when)
        elif slot >= len(scenes):
            drawing.outro(ctx, when - outro_start, when)
        else:
            scene = scenes[slot]
            drawing.SCENES[slot](ctx, when - scene.start, scene, when)

    if t < scenes[0].start:
        slot = -1
    elif t >= outro_start:
        slot = len(scenes)
    else:
        slot = _scene_at(scenes, t)
    boundary = drawing.INTRO if slot == 0 else (scenes[slot].start if 0 < slot < len(scenes) else outro_start)
    if slot >= 0 and t - boundary < TRANSITION:
        # circular wipe: the previous picture keeps moving underneath, the new one grows from the middle
        paint(slot - 1, t)
        amount = engine.ease_in_out((t - boundary) / TRANSITION)
        ctx.save()
        props.iris(ctx, engine.W / 2, engine.H / 2, amount * math.hypot(engine.W, engine.H) / 2)
        paint(slot, t)
        ctx.restore()
        ctx.arc(engine.W / 2, engine.H / 2, max(amount * math.hypot(engine.W, engine.H) / 2, 0.1), 0, 2 * math.pi)
        engine.set_color(ctx, engine.C["white"], 0.9 * (1 - amount))
        ctx.set_line_width(18)
        ctx.stroke()
    else:
        paint(slot, t)
    return surface


def _load_scenes(data: list[dict]) -> list[SceneTiming]:
    return [SceneTiming(s["scene_id"], s["start"], s["end"], [BeatTiming(**b) for b in s["beats"]]) for s in data]


def _render_chunk(args: tuple) -> str:
    week, scene_data, total, first, last, out_path = args
    from . import engine

    _, drawing = episode_modules(week)
    scenes = _load_scenes(scene_data)
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra",
               "-s", f"{engine.W}x{engine.H}", "-r", str(engine.FPS), "-i", "-",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", out_path]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        for frame in range(first, last):
            surface = draw_frame(drawing, scenes, total, frame / engine.FPS)
            surface.flush()
            process.stdin.write(bytes(surface.get_data()))
    finally:
        process.stdin.close()
        process.wait()
    if process.returncode != 0:
        raise RuntimeError(f"ffmpeg failed while encoding frames {first}-{last}")
    return out_path


# --------------------------------------------------------------------------- captions
def _captions(scenes: list[SceneTiming]) -> list[tuple[float, float, str]]:
    from ..media import _cue_lines, caption_chunks

    cues = []
    for scene in scenes:
        for beat in scene.beats:
            chunks = caption_chunks(beat.text)
            total_chars = sum(len(c) for c in chunks) or 1
            at = beat.start
            for chunk in chunks:
                length = (beat.end - beat.start) * len(chunk) / total_chars
                cues.append((at, max(at + length, at + 0.9), _cue_lines(chunk)))
                at += length
    # never overlap the next cue
    fixed = []
    for i, (start, end, body) in enumerate(cues):
        if i + 1 < len(cues):
            end = min(end, cues[i + 1][0])
        fixed.append((start, end, body))
    return fixed


def _write_captions(cues, srt: Path, vtt: Path) -> None:
    from ..media import _timestamp

    srt.write_text("\n".join(f"{n}\n{_timestamp(a, ',')} --> {_timestamp(b, ',')}\n{body}\n"
                             for n, (a, b, body) in enumerate(cues, 1)), encoding="utf-8")
    vtt.write_text("WEBVTT\n\n" + "\n".join(f"{_timestamp(a, '.')} --> {_timestamp(b, '.')}\n{body}\n"
                                            for a, b, body in cues), encoding="utf-8")


# --------------------------------------------------------------------------- main entry
def render_episode(week: int, output_dir: Path, workers: int | None = None, preview: float | None = None) -> Path:
    """Render one animated episode. `preview` renders only the first N seconds (for quick checks)."""
    from . import audio, engine

    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required")
    script, drawing = episode_modules(week)
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    video = next(v for v in spec["videos"] if v["week"] == week)
    errors = check_against_spec(script.SCRIPTS, video)
    if errors:
        raise RuntimeError("; ".join(errors))

    # 1. voices: one line per beat, measured exactly
    durations, envelopes, signals = [], [], []
    for scene in script.SCRIPTS:
        durations.append([]), envelopes.append([]), signals.append([])
        for beat in scene.beats:
            signal = audio.speak(beat.text, beat.speaker)
            durations[-1].append(len(signal) / audio.SR)
            envelopes[-1].append(audio.mouth_envelope(signal, engine.FPS))
            signals[-1].append(signal)
    scenes, total = build_timeline(script.SCRIPTS, durations, drawing.INTRO, drawing.OUTRO, envelopes)

    # 2. audio: voices, effects, ducked music
    voice_events = [(beat.start, signals[s][b]) for s, scene in enumerate(scenes) for b, beat in enumerate(scene.beats)]
    sfx_events = [(0.15, "sparkle"), (drawing.INTRO - 0.4, "whoosh"), (scenes[-1].end, "chime")]
    for index, scene in enumerate(scenes):
        sfx_events += drawing.SFX[index](scene)
        if index > 0:
            sfx_events.append((scene.start, "whoosh"))
    length = min(total, preview) if preview else total
    stereo = audio.mix(total, voice_events, sfx_events, drawing.INTRO, scenes[-1].end)

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"level1-week{week:02d}-{video['slug']}" + ("-preview" if preview else "")
    work = Path(tempfile.mkdtemp(prefix=f"{stem}-", dir=output_dir))
    try:
        wav = work / "mix.wav"
        audio.write_wav(wav, stereo[: int(length * audio.SR)])

        # 3. frames, rendered in parallel chunks
        frames = int(math.ceil(length * engine.FPS))
        workers = workers or max(1, (os.cpu_count() or 2) - 1)
        size = math.ceil(frames / workers)
        scene_data = [dataclasses.asdict(s) for s in scenes]
        jobs = [(week, scene_data, total, start, min(start + size, frames), str(work / f"part{n:03d}.mp4"))
                for n, start in enumerate(range(0, frames, size))]
        with ProcessPoolExecutor(max_workers=workers) as pool:
            parts = list(pool.map(_render_chunk, jobs))
        listing = work / "parts.txt"
        listing.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")

        # 4. captions and the final file (loudness-normalized, captions as a selectable track)
        cues = [c for c in _captions(scenes) if c[0] < length]
        srt, vtt = output_dir / f"{stem}.srt", output_dir / f"{stem}.vtt"
        _write_captions(cues, srt, vtt)
        destination = output_dir / f"{stem}.mp4"
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(listing), "-i", str(wav), "-i", str(srt),
            "-map", "0:v", "-map", "1:a", "-map", "2:0", "-c:v", "copy",
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
            "-metadata", f"title=Code Quest Week {week}: {video['title']}",
            "-metadata", "comment=Narration uses AI-generated voices (Kokoro).",
            "-movflags", "+faststart", str(destination),
        ], check=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return destination


def still(week: int, seconds: list[float], out_dir: Path) -> list[Path]:
    """Render single frames (PNG) at given times, for visual review without encoding video."""
    from . import audio, engine

    script, drawing = episode_modules(week)
    durations, envelopes = [], []
    for scene in script.SCRIPTS:
        signals = [audio.speak(beat.text, beat.speaker) for beat in scene.beats]
        durations.append([len(s) / audio.SR for s in signals])
        envelopes.append([audio.mouth_envelope(s, engine.FPS) for s in signals])
    scenes, total = build_timeline(script.SCRIPTS, durations, drawing.INTRO, drawing.OUTRO, envelopes)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for value in seconds:
        surface = draw_frame(drawing, scenes, total, value)
        path = out_dir / f"week{week:02d}-{value:07.2f}.png"
        surface.write_to_png(str(path))
        paths.append(path)
    return paths


def timeline_summary(week: int) -> tuple[list[SceneTiming], float]:
    from . import audio, engine

    script, drawing = episode_modules(week)
    durations = [[len(audio.speak(b.text, b.speaker)) / audio.SR for b in s.beats] for s in script.SCRIPTS]
    return build_timeline(script.SCRIPTS, durations, drawing.INTRO, drawing.OUTRO)
