"""Scene pictures, narration providers, captions, and FFmpeg composition.

Providers are small functions behind two registries (`VISUAL_PROVIDERS`, `VOICE_PROVIDERS`), so a
new image or voice technology changes this file only. Paid results are cached under
`videos/.cache/` (git-ignored), keyed by everything that affects the output, so re-rendering a
reviewed episode never pays twice for the same picture or narration.
"""

from __future__ import annotations

import asyncio
import base64
from dataclasses import dataclass
import difflib
import functools
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import textwrap
from typing import Callable
import wave

from .models import Scene, Video

WIDTH = 1920
HEIGHT = 1080
FPS = 30
SPOKEN_WPM = 140
CAPTION_LINE = 42  # characters per caption line; two lines per cue
REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / "videos" / ".cache"

# Okabe-Ito based palette, the same family as every printed course document.
PALETTE = {
    "navy": "#15324A",
    "sky": "#56B4E9",
    "sky_light": "#DDF2FC",
    "orange": "#E69F00",
    "green": "#009E73",
    "cream": "#FFF8E7",
    "ink": "#17212B",
    "muted": "#4A5560",
}


def require_ffmpeg() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if not shutil.which(name)]
    if missing:
        raise RuntimeError(f"missing media tools: {', '.join(missing)}")


# --------------------------------------------------------------------------- fonts and layout
@functools.lru_cache(maxsize=None)
def _font_path(bold: bool) -> str | None:
    """The course font (Atkinson Hyperlegible Next) when TeX Live has it, else a system font."""
    name = "AtkinsonHyperlegibleNext-Bold.otf" if bold else "AtkinsonHyperlegibleNext-Regular.otf"
    if shutil.which("kpsewhich"):
        found = subprocess.run(["kpsewhich", name], capture_output=True, text=True).stdout.strip()
        if found and Path(found).is_file():
            return found
    fallbacks = (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Verdana.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    return next((path for path in fallbacks if Path(path).is_file()), None)


@functools.lru_cache(maxsize=None)
def _font(size: int, bold: bool = False):
    from PIL import ImageFont

    path = _font_path(bold)
    return ImageFont.truetype(path, size=size) if path else ImageFont.load_default(size=size)


FALLBACK_FONTS = (
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
)


@functools.lru_cache(maxsize=None)
def _fallback_font(size: int):
    from PIL import ImageFont

    path = next((path for path in FALLBACK_FONTS if Path(path).is_file()), None)
    return ImageFont.truetype(path, size=size) if path else None


def _glyph_signature(font, char: str) -> tuple:
    mask = font.getmask(char)
    return mask.size, bytes(mask)


@functools.lru_cache(maxsize=4096)
def _has_glyph(font, char: str) -> bool:
    """False when `font` would draw its missing-glyph box for `char` (e.g. → in Atkinson)."""
    if char.isspace():
        return True
    return _glyph_signature(font, char) != _glyph_signature(font, "\U0010FFFD")


def _runs(text: str, font) -> list[tuple[str, object]]:
    """Split text into runs drawn with the main font or, for missing symbols, the fallback."""
    fallback = _fallback_font(font.size)
    runs: list[tuple[str, object]] = []
    for char in text:
        use = font if fallback is None or _has_glyph(font, char) else fallback
        if runs and runs[-1][1] is use:
            runs[-1] = (runs[-1][0] + char, use)
        else:
            runs.append((char, use))
    return runs


def _text_width(draw, text: str, font) -> float:
    return sum(draw.textlength(run, font=run_font) for run, run_font in _runs(text, font))


def _draw_text(draw, xy: tuple[float, float], text: str, font, fill, anchor: str = "la") -> None:
    """Draw one line, switching to the fallback font only for characters the main font lacks."""
    x, y = xy
    ascent, descent = font.getmetrics()
    vertical = anchor[1] if len(anchor) == 2 else "a"
    # Every run shares the main font's baseline, so fallback symbols sit on the same line.
    baseline = {"a": y + ascent, "m": y + (ascent - descent) / 2, "s": y}.get(vertical, y + ascent)
    for run, run_font in _runs(text, font):
        draw.text((x, baseline), run, font=run_font, fill=fill, anchor="ls")
        x += draw.textlength(run, font=run_font)


def _wrap(draw, text: str, font, max_width: int) -> list[str]:
    """Greedy word wrap by rendered pixel width."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if not current or _text_width(draw, candidate, font) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _fit(draw, text: str, max_width: int, max_lines: int, sizes: tuple[int, ...], bold: bool = False):
    """Largest font size from `sizes` at which `text` wraps into `max_lines` lines."""
    for size in sizes:
        font = _font(size, bold)
        lines = _wrap(draw, text, font, max_width)
        if len(lines) <= max_lines:
            return font, lines
    font = _font(sizes[-1], bold)
    lines = _wrap(draw, text, font, max_width)
    return font, lines[: max_lines - 1] + [" ".join(lines[max_lines - 1 :])]


def _draw_chips(draw, items: tuple[str, ...], top: int, left: int, right: int, fill) -> None:
    """On-screen text as large rounded labels, two per row when they fit."""
    font = _font(40, bold=True)
    gap, height = 24, 84
    x, y = left, top
    for item in items:
        width = int(_text_width(draw, item, font)) + 72
        width = min(width, right - left)
        if x > left and x + width > right:
            x, y = left, y + height + gap
        draw.rounded_rectangle((x, y, x + width, y + height), 22, fill=fill)
        _draw_text(draw, (x + 36, y + height // 2), item, font, PALETTE["navy"], anchor="lm")
        x += width + gap


def _draw_footer(draw, note: str | None, box_fill=None) -> None:
    if not note:
        return
    font = _font(30, bold=True)
    width = int(_text_width(draw, note, font))
    x1, y1 = WIDTH - 90 - width - 40, HEIGHT - 135
    if box_fill:
        draw.rounded_rectangle((x1, y1, WIDTH - 90, y1 + 56), 14, fill=box_fill)
    _draw_text(draw, (x1 + 20, y1 + 28), note, font, PALETTE["navy"], anchor="lm")


def _header(video: Video, index: int, total: int) -> str:
    return f"KIDS CODING  •  WEEK {video.week}  •  SCENE {index} OF {total}"


def render_scene_card(
    video: Video,
    scene: Scene,
    destination: Path,
    index: int = 1,
    total: int = 1,
    footer_note: str | None = None,
) -> None:
    """Create an accessible, deterministic storyboard card (animatic frame) for one scene."""
    from PIL import Image, ImageDraw

    image = Image.new("RGB", (WIDTH, HEIGHT), PALETTE["cream"])
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((60, 60, WIDTH - 60, HEIGHT - 60), 42, fill="#FFFFFF", outline=PALETTE["navy"], width=8)
    draw.rounded_rectangle((60, 60, WIDTH - 60, 200), 42, fill=PALETTE["navy"])
    draw.rectangle((60, 160, WIDTH - 60, 200), fill=PALETTE["navy"])
    draw.text((120, 130), _header(video, index, total), font=_font(36, bold=True), fill="#FFFFFF", anchor="lm")

    left, right = 120, WIDTH - 120
    title_font, title_lines = _fit(draw, video.title, right - left, 1, (72, 64, 56), bold=True)
    _draw_text(draw, (left, 240), title_lines[0], title_font, PALETTE["ink"])
    _draw_text(draw, (left, 335), scene.purpose.upper(), _font(32, bold=True), PALETTE["green"])
    # A short orange rule plus the word label: purpose is never shown by color alone.
    draw.rectangle((left, 385, left + 140, 393), fill=PALETTE["orange"])

    visual_font, visual_lines = _fit(draw, scene.visual, right - left, 6, (40, 36, 32))
    line_height = visual_font.size + 14
    for number, line in enumerate(visual_lines):
        _draw_text(draw, (left, 425 + number * line_height), line, visual_font, PALETTE["muted"])
    _draw_chips(draw, scene.on_screen_text, 740, left, right, PALETTE["sky_light"])
    _draw_footer(draw, footer_note)
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination)


def overlay_scene_text(
    video: Video,
    scene: Scene,
    path: Path,
    index: int = 1,
    total: int = 1,
    footer_note: str | None = None,
) -> None:
    """Crop a generated background to 16:9 and add deterministic, readable labels."""
    from PIL import Image, ImageDraw, ImageOps

    background = Image.open(path).convert("RGB")
    image = ImageOps.fit(background, (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((55, 45, WIDTH - 55, 225), 36, fill=(21, 50, 74, 235))
    draw.text((105, 95), _header(video, index, total), font=_font(32, bold=True), fill="#FFFFFF", anchor="lm")
    title_font, title_lines = _fit(draw, video.title, WIDTH - 210, 1, (60, 52, 46), bold=True)
    _draw_text(draw, (105, 140), title_lines[0], title_font, "#FFFFFF")
    _draw_chips(draw, scene.on_screen_text, 760, 105, WIDTH - 105, (255, 255, 255, 240))
    _draw_footer(draw, footer_note, box_fill=(255, 255, 255, 240))
    image.save(path)


# --------------------------------------------------------------------------- cache
def _cached(kind: str, key: dict[str, object], suffix: str, destination: Path, produce: Callable[[Path], None]) -> None:
    """Copy a cached result to `destination`, or produce it once and keep a copy."""
    digest = hashlib.sha256(json.dumps(key, sort_keys=True).encode("utf-8")).hexdigest()[:32]
    cached = CACHE_DIR / kind / f"{digest}{suffix}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not cached.is_file():
        cached.parent.mkdir(parents=True, exist_ok=True)
        partial = cached.with_name(cached.name + ".partial")
        produce(partial)
        partial.replace(cached)
    shutil.copyfile(cached, destination)


# --------------------------------------------------------------------------- pictures
def generate_openai_illustration(scene: Scene, destination: Path) -> None:
    """Generate text-free background art; code and labels are overlaid afterwards."""
    model = os.getenv("VIDEO_IMAGE_MODEL", "gpt-image-2.5-flare")
    # GPT Image models accept WIDTHxHEIGHT sizes divisible by 16; 1536x864 is exactly 16:9.
    size = os.getenv("VIDEO_IMAGE_SIZE", "1536x864")
    quality = os.getenv("VIDEO_IMAGE_QUALITY", "medium")
    prompt = (
        "Create a clean 16:9 educational illustration for children in grades 4 and 5. "
        "Friendly modern flat vector style, generous empty space in the lower third, high contrast, "
        "no tiny details, no words, no letters, no numbers, no logos, no rendered user interface, "
        "no real people. Characters: Rose, a curious ten-year-old coder with long, straight (not curly) "
        "dark-brown hair with a center part, a light-blue headband and a purple long-sleeve top with lavender "
        "stripes across the top of the shirt and the upper sleeves only, and Pixi, a small round "
        f"friendly helper robot. Scene brief: {scene.visual}"
    )

    def produce(path: Path) -> None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is required for OpenAI illustrations")
        from openai import OpenAI

        # GPT Image models always return base64 data; `response_format` is not supported.
        result = OpenAI().images.generate(model=model, prompt=prompt, size=size, quality=quality,
                                          output_format="png", n=1)
        path.write_bytes(base64.b64decode(result.data[0].b64_json))

    _cached("images", {"model": model, "size": size, "quality": quality, "prompt": prompt}, ".png", destination, produce)


@dataclass(frozen=True)
class VisualProvider:
    paid: bool
    description: str


VISUAL_PROVIDERS = {
    "cards": VisualProvider(False, "deterministic storyboard cards (offline)"),
    "openai": VisualProvider(True, "OpenAI text-free illustrations with deterministic overlays"),
}


# --------------------------------------------------------------------------- narration
VOICE_STYLE = (
    "Warm, curious, encouraging teaching voice for children in grades 4 and 5 (ages nine to eleven). "
    "Speak clearly at about 140 words per minute. Sound friendly, never babyish. "
    "Pause briefly after questions and say code words plainly, without exaggeration."
)
READ_ALOUD = (
    "You are the narrator of a children's coding video. Read the user's text aloud exactly as "
    "written, word for word, without adding, removing or changing anything and without commentary. "
    + VOICE_STYLE
)


def synthesize_openai_speech(scene: Scene, destination: Path) -> None:
    """Legacy Speech API adapter. Its models shut down on 2027-01-06; prefer `openai-realtime`."""
    model = os.getenv("VIDEO_SPEECH_MODEL", "gpt-4o-mini-tts")
    voice = os.getenv("VIDEO_VOICE", "coral")

    def produce(path: Path) -> None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is required for OpenAI narration")
        from openai import OpenAI

        with OpenAI().audio.speech.with_streaming_response.create(
            model=model, voice=voice, input=scene.narration, instructions=VOICE_STYLE, response_format="mp3",
        ) as response:
            response.stream_to_file(path)

    _cached("speech", {"provider": "openai-speech", "model": model, "voice": voice,
                       "style": VOICE_STYLE, "text": scene.narration}, ".mp3", destination, produce)


def _normalized_words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("'", ""))


def transcript_similarity(expected: str, heard: str) -> float:
    return difflib.SequenceMatcher(None, _normalized_words(expected), _normalized_words(heard)).ratio()


async def _realtime_read_aloud(text: str, model: str, voice: str) -> tuple[bytes, str]:
    from openai import AsyncOpenAI

    pcm = bytearray()
    transcript: list[str] = []
    async with AsyncOpenAI().realtime.connect(model=model) as connection:
        await connection.session.update(session={
            "type": "realtime",
            "model": model,
            "instructions": READ_ALOUD,
            "output_modalities": ["audio"],
            "audio": {"output": {"voice": voice, "format": {"type": "audio/pcm", "rate": 24000}}},
        })
        await connection.conversation.item.create(item={
            "type": "message", "role": "user", "content": [{"type": "input_text", "text": text}],
        })
        await connection.response.create(response={"output_modalities": ["audio"]})
        async for event in connection:
            if event.type == "response.output_audio.delta":
                pcm.extend(base64.b64decode(event.delta))
            elif event.type == "response.output_audio_transcript.delta":
                transcript.append(event.delta)
            elif event.type == "error":
                raise RuntimeError(f"Realtime API error: {event.error.message}")
            elif event.type == "response.done":
                break
    return bytes(pcm), "".join(transcript)


def synthesize_openai_realtime(scene: Scene, destination: Path) -> None:
    """Realtime API narration (the documented replacement for the Speech API models).

    A conversational model can paraphrase, so the transcript of what it said is compared with
    the script; anything below VIDEO_MIN_TRANSCRIPT_MATCH (default 0.97) is rejected instead of
    being rendered with captions that no longer match the voice.
    """
    model = os.getenv("VIDEO_REALTIME_MODEL", "gpt-realtime-2.1-mini")
    voice = os.getenv("VIDEO_VOICE", "coral")
    threshold = float(os.getenv("VIDEO_MIN_TRANSCRIPT_MATCH", "0.97"))

    def produce(path: Path) -> None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is required for OpenAI narration")
        pcm, heard = asyncio.run(_realtime_read_aloud(scene.narration, model, voice))
        score = transcript_similarity(scene.narration, heard)
        if not pcm or score < threshold:
            raise RuntimeError(
                f"{scene.scene_id}: the voice did not read the script word for word "
                f"(match {score:.2f} < {threshold:.2f}); heard: {heard[:160]!r}"
            )
        with wave.open(str(path), "wb") as out:
            out.setnchannels(1)
            out.setsampwidth(2)
            out.setframerate(24000)
            out.writeframes(pcm)

    _cached("speech", {"provider": "openai-realtime", "model": model, "voice": voice,
                       "instructions": READ_ALOUD, "text": scene.narration}, ".wav", destination, produce)


def synthesize_macos_say(scene: Scene, destination: Path) -> None:
    """Free, offline draft narration with the macOS `say` command (for timing reviews)."""
    if not shutil.which("say"):
        raise RuntimeError("the macos-say voice needs macOS (the `say` command)")
    voice = os.getenv("VIDEO_SAY_VOICE", "Samantha")
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "narration.txt"
        script.write_text(scene.narration, encoding="utf-8")
        raw = Path(tmp) / "narration.aiff"
        subprocess.run(["say", "-v", voice, "-r", str(SPOKEN_WPM), "-f", str(script), "-o", str(raw)],
                       check=True, capture_output=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(raw, destination)


@dataclass(frozen=True)
class VoiceProvider:
    synthesize: Callable[[Scene, Path], None] | None
    suffix: str
    paid: bool
    disclosure: str


VOICE_PROVIDERS = {
    "openai-realtime": VoiceProvider(synthesize_openai_realtime, ".wav", True, "Narration uses an AI-generated voice"),
    "openai-speech": VoiceProvider(synthesize_openai_speech, ".mp3", True, "Narration uses an AI-generated voice"),
    "macos-say": VoiceProvider(synthesize_macos_say, ".aiff", False, "Draft narration: computer-generated voice"),
    "silent": VoiceProvider(None, "", False, "Draft animatic: no narration"),
}


def needs_approval(visual_provider: str, voice_provider: str) -> bool:
    """Paid providers need the explicit --approved flag; offline drafts do not."""
    return VISUAL_PROVIDERS[visual_provider].paid or VOICE_PROVIDERS[voice_provider].paid


# --------------------------------------------------------------------------- captions
def estimated_speech_seconds(scene: Scene) -> float:
    return scene.narration_words * 60 / SPOKEN_WPM


def _caption_wrap(text: str) -> list[str]:
    return textwrap.wrap(text, width=CAPTION_LINE, break_long_words=False, break_on_hyphens=False)


def caption_chunks(text: str, max_lines: int = 2) -> list[str]:
    """Split narration into cues: whole sentences where possible, at most two short lines each."""
    sentences = re.split(r"(?<=[.!?…])\s+", " ".join(text.split()))
    chunks: list[str] = []
    for sentence in filter(None, sentences):
        current = ""
        for word in sentence.split():
            candidate = f"{current} {word}".strip()
            if current and len(_caption_wrap(candidate)) > max_lines:
                chunks.append(current)
                current = word
            else:
                current = candidate
        if current:
            chunks.append(current)
    return chunks


def _cue_lines(chunk: str) -> str:
    return "\n".join(_caption_wrap(chunk))


def _timestamp(seconds: float, separator: str) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{separator}{millis:03d}"


def caption_cues(video: Video, speech_seconds: list[float] | None = None) -> list[tuple[float, float, str]]:
    """(start, end, text) cues. Each scene's cues share the time its narration is actually spoken
    (measured from the audio when available), in proportion to their length; captions then
    disappear during the silent pause at the end of the scene."""
    cues: list[tuple[float, float, str]] = []
    scene_start = 0.0
    for index, scene in enumerate(video.scenes):
        spoken = speech_seconds[index] if speech_seconds else estimated_speech_seconds(scene)
        spoken = min(max(spoken, 0.5), scene.duration_seconds)
        chunks = caption_chunks(scene.narration)
        total_chars = sum(len(chunk) for chunk in chunks) or 1
        at = scene_start
        for chunk in chunks:
            length = spoken * len(chunk) / total_chars
            end = min(at + max(length, 1.0), scene_start + scene.duration_seconds)
            cues.append((at, end, _cue_lines(chunk)))
            at += length
        scene_start += scene.duration_seconds
    return cues


def write_captions(video: Video, destination: Path, speech_seconds: list[float] | None = None) -> None:
    """Write SubRip captions (.srt)."""
    entries = [
        f"{number}\n{_timestamp(start, ',')} --> {_timestamp(end, ',')}\n{text}\n"
        for number, (start, end, text) in enumerate(caption_cues(video, speech_seconds), start=1)
    ]
    destination.write_text("\n".join(entries), encoding="utf-8")


def write_webvtt(video: Video, destination: Path, speech_seconds: list[float] | None = None) -> None:
    """Write WebVTT captions (.vtt) for web players."""
    entries = ["WEBVTT\n"] + [
        f"{_timestamp(start, '.')} --> {_timestamp(end, '.')}\n{text}\n"
        for start, end, text in caption_cues(video, speech_seconds)
    ]
    destination.write_text("\n".join(entries), encoding="utf-8")


# --------------------------------------------------------------------------- composition
def _media_duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(result.stdout.strip())


def _ffconcat_path(path: Path) -> str:
    return "file '" + str(path).replace("'", "'\\''") + "'"


def _ffmpeg(args: list[str]) -> None:
    result = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("ffmpeg failed: " + result.stderr.strip()[-600:])


def output_name(video: Video, voice_provider: str, level: int = 1) -> str:
    draft = "" if VOICE_PROVIDERS[voice_provider].paid else "-draft"
    return f"level{level}-week{video.week:02d}-{video.slug}{draft}"


def render_video(
    video: Video,
    output_dir: Path,
    visual_provider: str = "cards",
    voice_provider: str = "openai-realtime",
    level: int = 1,
) -> Path:
    """Render one episode to MP4 with a caption track and sidecar .srt/.vtt files."""
    if visual_provider not in VISUAL_PROVIDERS:
        raise ValueError(f"unknown visual provider: {visual_provider}")
    if voice_provider not in VOICE_PROVIDERS:
        raise ValueError(f"unknown voice provider: {voice_provider}")
    require_ffmpeg()
    voice = VOICE_PROVIDERS[voice_provider]
    work = output_dir / ".work" / output_name(video, voice_provider, level)
    work.mkdir(parents=True, exist_ok=True)
    concat_lines: list[str] = []
    speech_seconds: list[float] = []
    total = len(video.scenes)
    for index, scene in enumerate(video.scenes, start=1):
        image = work / f"scene-{index:02d}.png"
        clip = work / f"scene-{index:02d}.mp4"
        # The disclosure stays on the last scene (the end card) and is repeated in the metadata.
        note = voice.disclosure if index == total else None
        if visual_provider == "openai":
            generate_openai_illustration(scene, image)
            overlay_scene_text(video, scene, image, index, total, note)
        else:
            render_scene_card(video, scene, image, index, total, note)

        if voice.synthesize is None:
            audio_input = ["-f", "lavfi", "-t", str(scene.duration_seconds), "-i", "anullsrc=r=48000:cl=stereo"]
            speech_seconds.append(estimated_speech_seconds(scene))
        else:
            audio = work / f"scene-{index:02d}{voice.suffix}"
            voice.synthesize(scene, audio)
            seconds = _media_duration(audio)
            if seconds > scene.duration_seconds:
                raise RuntimeError(
                    f"{scene.scene_id}: narration is {seconds:.1f}s but the scene allows "
                    f"{scene.duration_seconds}s; shorten the script or extend the scene"
                )
            speech_seconds.append(seconds)
            audio_input = ["-i", str(audio)]
        _ffmpeg([
            "-loop", "1", "-framerate", str(FPS), "-i", str(image), *audio_input,
            "-t", str(scene.duration_seconds),
            "-vf", f"scale={WIDTH}:{HEIGHT},format=yuv420p", "-r", str(FPS),
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "medium", "-crf", "20",
            "-af", "apad", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
            str(clip),
        ])
        concat_lines.append(_ffconcat_path(clip))

    concat_file = work / "concat.txt"
    concat_file.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
    stem = output_name(video, voice_provider, level)
    captions = output_dir / f"{stem}.srt"
    write_captions(video, captions, speech_seconds)
    write_webvtt(video, output_dir / f"{stem}.vtt", speech_seconds)
    destination = output_dir / f"{stem}.mp4"
    _ffmpeg([
        "-f", "concat", "-safe", "0", "-i", str(concat_file), "-i", str(captions),
        "-map", "0:v", "-map", "0:a", "-map", "1:0",
        "-c:v", "copy", "-c:a", "copy", "-c:s", "mov_text",
        "-metadata", f"title=Kids Coding with Rose and Pixi – Level {level} Week {video.week}: {video.title}",
        "-metadata", f"comment={voice.disclosure}",
        "-metadata:s:s:0", "language=eng", "-movflags", "+faststart",
        str(destination),
    ])
    return destination
