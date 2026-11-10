"""Deterministic cards, optional OpenAI media, captions, and FFmpeg composition."""

from __future__ import annotations

import base64
import os
from pathlib import Path
import shutil
import subprocess
import textwrap
import warnings

from .models import Scene, Video

WIDTH = 1920
HEIGHT = 1080
PALETTE = {
    "navy": "#15324A",
    "sky": "#56B4E9",
    "orange": "#E69F00",
    "green": "#009E73",
    "cream": "#FFF8E7",
    "ink": "#17212B",
}


def require_ffmpeg() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if not shutil.which(name)]
    if missing:
        raise RuntimeError(f"missing media tools: {', '.join(missing)}")


def _font(size: int):
    from PIL import ImageFont

    candidates = (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Verdana.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default(size=size)


def render_scene_card(
    video: Video,
    scene: Scene,
    destination: Path,
    disclose_ai_voice: bool = False,
) -> None:
    """Create an accessible deterministic storyboard card for one scene."""
    from PIL import Image, ImageDraw

    image = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["cream"])
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((70, 70, WIDTH - 70, HEIGHT - 70), 42, fill="#FFFFFF", outline=PALETTE["navy"], width=8)
    draw.rounded_rectangle((70, 70, WIDTH - 70, 225), 42, fill=PALETTE["navy"])
    draw.text((125, 105), f"CODE QUEST • WEEK {video.week}", font=_font(38), fill="#FFFFFF")
    draw.text((125, 275), video.title, font=_font(68), fill=PALETTE["ink"])
    wrapped = textwrap.wrap(scene.visual, width=58)[:5]
    draw.multiline_text((125, 405), "\n".join(wrapped), font=_font(38), fill=PALETTE["ink"], spacing=18)
    y = 760
    for item in scene.on_screen_text[:3]:
        draw.rounded_rectangle((125, y, WIDTH - 125, y + 72), 18, fill="#DDF2FC")
        draw.text((160, y + 14), item, font=_font(32), fill=PALETTE["navy"])
        y += 88
    if disclose_ai_voice:
        draw.text(
            (WIDTH - 630, HEIGHT - 52),
            "Narration uses an AI-generated voice",
            font=_font(24),
            fill=PALETTE["navy"],
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination)


def generate_openai_illustration(scene: Scene, destination: Path) -> None:
    """Generate text-free background art; code and labels are overlaid later."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for OpenAI illustrations")
    from openai import OpenAI

    model = os.getenv("VIDEO_IMAGE_MODEL", "gpt-image-2.5-flare")
    prompt = (
        "Create a clean 16:9 educational illustration for children ages 10-11. "
        "Friendly modern vector style, generous empty space, high contrast, no tiny details, "
        "no words, no letters, no numbers, no logos, no rendered user interface. "
        f"Scene brief: {scene.visual}"
    )
    result = OpenAI().images.generate(
        model=model,
        prompt=prompt,
        size="1536x1024",
        response_format="b64_json",
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(base64.b64decode(result.data[0].b64_json))


def overlay_scene_text(
    video: Video,
    scene: Scene,
    path: Path,
    disclose_ai_voice: bool = False,
) -> None:
    """Crop a generated background to 16:9 and add deterministic readable labels."""
    from PIL import Image, ImageDraw, ImageOps

    background = Image.open(path).convert("RGB")
    image = ImageOps.fit(background, (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((55, 45, WIDTH - 55, 215), 36, fill=(21, 50, 74, 235))
    draw.text((105, 78), f"CODE QUEST • WEEK {video.week}", font=_font(34), fill="#FFFFFF")
    draw.text((105, 130), video.title, font=_font(50), fill="#FFFFFF")
    y = 780
    for item in scene.on_screen_text[:3]:
        draw.rounded_rectangle((105, y, WIDTH - 105, y + 72), 18, fill=(255, 255, 255, 235))
        draw.text((140, y + 14), item, font=_font(32), fill=PALETTE["navy"])
        y += 84
    if disclose_ai_voice:
        draw.rounded_rectangle(
            (WIDTH - 690, HEIGHT - 65, WIDTH - 40, HEIGHT - 20),
            14,
            fill=(255, 255, 255, 235),
        )
        draw.text(
            (WIDTH - 660, HEIGHT - 58),
            "Narration uses an AI-generated voice",
            font=_font(24),
            fill=PALETTE["navy"],
        )
    image.save(path)


def synthesize_openai_speech(scene: Scene, destination: Path) -> None:
    """Temporary Speech API adapter, isolated for the documented 2027 migration."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for OpenAI narration")
    warnings.warn(
        "The current OpenAI Speech API models retire on 2027-01-06; migrate this adapter "
        "to Realtime voice before that date.",
        FutureWarning,
        stacklevel=2,
    )
    from openai import OpenAI

    destination.parent.mkdir(parents=True, exist_ok=True)
    with OpenAI().audio.speech.with_streaming_response.create(
        model=os.getenv("VIDEO_SPEECH_MODEL", "gpt-4o-mini-tts"),
        voice=os.getenv("VIDEO_VOICE", "coral"),
        input=scene.narration,
        instructions=(
            "Warm, curious, encouraging teaching voice for children ages ten to eleven. "
            "Speak clearly at about 140 words per minute. Sound friendly, never babyish. "
            "Pause briefly after questions and emphasize code words without exaggeration."
        ),
        response_format="mp3",
    ) as response:
        response.stream_to_file(destination)


def _srt_time(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def write_captions(video: Video, destination: Path) -> None:
    elapsed = 0.0
    entries: list[str] = []
    cue = 1
    for scene in video.scenes:
        words = scene.narration.split()
        chunks = [words[index : index + 8] for index in range(0, len(words), 8)]
        cue_seconds = scene.duration_seconds / len(chunks)
        for chunk in chunks:
            start = elapsed
            elapsed += cue_seconds
            wrapped = "\n".join(textwrap.wrap(" ".join(chunk), width=42))
            entries.append(
                f"{cue}\n{_srt_time(start)} --> {_srt_time(elapsed)}\n{wrapped}\n"
            )
            cue += 1
    destination.write_text("\n".join(entries), encoding="utf-8")


def _media_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def _ffconcat_path(path: Path) -> str:
    return "file '" + str(path).replace("'", "'\\''") + "'"


def render_video(
    video: Video,
    output_dir: Path,
    visual_provider: str = "cards",
    voice_provider: str = "openai-speech",
) -> Path:
    """Render an approved video and return its MP4 path."""
    require_ffmpeg()
    work = output_dir / ".work" / f"week{video.week:02d}"
    work.mkdir(parents=True, exist_ok=True)
    concat_lines: list[str] = []
    for index, scene in enumerate(video.scenes, start=1):
        image = work / f"scene-{index:02d}.png"
        audio = work / f"scene-{index:02d}.mp3"
        clip = work / f"scene-{index:02d}.mp4"
        if visual_provider == "openai":
            generate_openai_illustration(scene, image)
            overlay_scene_text(
                video,
                scene,
                image,
                disclose_ai_voice=index == len(video.scenes),
            )
        elif visual_provider == "cards":
            render_scene_card(
                video,
                scene,
                image,
                disclose_ai_voice=index == len(video.scenes),
            )
        else:
            raise ValueError(f"unknown visual provider: {visual_provider}")
        if voice_provider != "openai-speech":
            raise ValueError(f"unknown voice provider: {voice_provider}")
        synthesize_openai_speech(scene, audio)
        audio_seconds = _media_duration(audio)
        if audio_seconds > scene.duration_seconds:
            raise RuntimeError(
                f"{scene.scene_id}: narration is {audio_seconds:.1f}s but the scene allows "
                f"{scene.duration_seconds}s; shorten the script or extend the scene"
            )
        subprocess.run(
            [
                "ffmpeg", "-y", "-loop", "1", "-i", str(image), "-i", str(audio),
                "-t", str(scene.duration_seconds),
                "-vf", "scale=1920:1080,format=yuv420p",
                "-af", f"apad=pad_dur={scene.duration_seconds}",
                "-c:v", "libx264", "-c:a", "aac", str(clip),
            ],
            check=True,
            capture_output=True,
        )
        concat_lines.append(_ffconcat_path(clip))
    concat_file = work / "concat.txt"
    concat_file.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
    captions = work / "captions.srt"
    write_captions(video, captions)
    destination = output_dir / f"level1-week{video.week:02d}-{video.slug}.mp4"
    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
            "-i", str(captions), "-map", "0:v", "-map", "0:a", "-map", "1:0",
            "-c:v", "copy", "-c:a", "copy", "-c:s", "mov_text",
            "-metadata:s:s:0", "language=eng", str(destination),
        ],
        check=True,
        capture_output=True,
    )
    return destination
