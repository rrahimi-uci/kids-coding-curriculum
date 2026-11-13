"""Voices, music, sound effects and the final mix for animated episodes.

- Voices: Kokoro-82M (Apache-2.0), an open neural text-to-speech model that runs locally and
  free. Each character has its own voice; Pixi gets a light robot effect.
- Music and sound effects are synthesized here from simple waveforms, so there is nothing to
  license and every render sounds the same.
- The music is ducked under the voices and the final mix is loudness-normalized when muxed.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import urllib.request

import numpy as np

from .speech import LEXICON, spoken_form  # noqa: F401  (re-exported for callers)
from .timeline import AIDEN, NARRATOR, ROSE, PIXI

SR = 48_000
REPO_ROOT = Path(__file__).resolve().parents[3]
MODEL_DIR = REPO_ROOT / "videos" / ".cache" / "models"
VOICE_CACHE = REPO_ROOT / "videos" / ".cache" / "voices"
MODEL_FILES = {
    "kokoro-v1.0.onnx": "7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5",
    "voices-v1.0.bin": "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d",
}
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/{name}"

# Voice casting: a warm, clear narrator; an energetic young inventor; a friendly robot.
# Aiden uses the same unprocessed narration voice as Grades 4-6. Pitch transformation made the
# younger-track voice noticeably less natural, even with a high-quality formant-preserving filter.
NARRATION_VOICE = {"voice": "af_heart", "speed": 0.94}
VOICES = {
    NARRATOR: NARRATION_VOICE,
    ROSE: {"voice": "af_bella", "speed": 1.02},
    PIXI: {"voice": "am_puck", "speed": 1.06, "robot": True},
    AIDEN: NARRATION_VOICE,
}

# --------------------------------------------------------------------------- model files
def fetch_models() -> None:
    """Download the Kokoro model files once and verify their SHA-256 checksums."""
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    for name, expected in MODEL_FILES.items():
        path = MODEL_DIR / name
        if path.is_file() and _sha256(path) == expected:
            continue
        partial = path.with_suffix(path.suffix + ".partial")
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(MODEL_URL.format(name=name), partial)
        if _sha256(partial) != expected:
            partial.unlink(missing_ok=True)
            raise RuntimeError(f"{name}: checksum mismatch; refusing to use the download")
        partial.replace(path)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


_KOKORO = None


def _kokoro():
    global _KOKORO
    if _KOKORO is None:
        missing = [name for name in MODEL_FILES if not (MODEL_DIR / name).is_file()]
        if missing:
            raise RuntimeError("Voice model missing; run `python -m videos.pipeline.cli fetch-voice` first")
        from kokoro_onnx import Kokoro

        _KOKORO = Kokoro(str(MODEL_DIR / "kokoro-v1.0.onnx"), str(MODEL_DIR / "voices-v1.0.bin"))
    return _KOKORO


# --------------------------------------------------------------------------- voices
def phonemes(text: str) -> str:
    """How the voice will pronounce a line (for checking code words without rendering)."""
    return _kokoro().tokenizer.phonemize(spoken_form(text), "en-us")


def upsample_2x(signal: np.ndarray) -> np.ndarray:
    """Band-limited 24 kHz -> 48 kHz resampling (spectral zero padding)."""
    spectrum = np.fft.rfft(signal)
    padded = np.zeros(len(signal) + 1, dtype=complex)
    padded[: len(spectrum)] = spectrum
    return np.fft.irfft(padded, n=len(signal) * 2) * 2


def robotize(signal: np.ndarray) -> np.ndarray:
    """A light, friendly robot color: gentle ring modulation plus a short metallic echo."""
    n = np.arange(len(signal)) / SR
    ring = signal * (0.75 + 0.25 * np.sin(2 * np.pi * 55 * n))
    echo = np.zeros_like(ring)
    delay = int(0.012 * SR)
    echo[delay:] = ring[:-delay] * 0.35
    return ring + echo


def speak(text: str, speaker: str) -> np.ndarray:
    """One line of speech at 48 kHz (cached by text, voice and settings)."""
    settings = VOICES[speaker]
    key = json.dumps({"text": spoken_form(text), **settings,
                      "model": MODEL_FILES["kokoro-v1.0.onnx"][:12]}, sort_keys=True)
    path = VOICE_CACHE / (hashlib.sha256(key.encode()).hexdigest()[:32] + ".npy")
    if path.is_file():
        return np.load(path)
    samples, rate = _kokoro().create(spoken_form(text), voice=settings["voice"], speed=settings["speed"],
                                     lang="en-us")
    signal = np.asarray(samples, dtype=np.float64)
    if rate == 24_000:
        signal = upsample_2x(signal)
    elif rate != SR:
        raise RuntimeError(f"unexpected voice sample rate {rate}")
    signal = _trim(signal)
    if settings.get("robot"):
        signal = robotize(signal)
    signal = signal / (np.max(np.abs(signal)) + 1e-9) * 0.85
    VOICE_CACHE.mkdir(parents=True, exist_ok=True)
    np.save(path, signal.astype(np.float32))
    return signal


def _trim(signal: np.ndarray, threshold: float = 0.01) -> np.ndarray:
    loud = np.nonzero(np.abs(signal) > threshold * np.max(np.abs(signal)))[0]
    if len(loud) == 0:
        return signal
    start = max(loud[0] - int(0.03 * SR), 0)
    end = min(loud[-1] + int(0.08 * SR), len(signal))
    return signal[start:end]


def mouth_envelope(signal: np.ndarray, fps: int) -> list[float]:
    """Mouth-open values (0-1), one per video frame, from the loudness of the voice."""
    hop = SR // fps
    frames = len(signal) // hop + 1
    padded = np.pad(signal, (0, frames * hop - len(signal)))
    rms = np.sqrt(np.mean(padded.reshape(frames, hop) ** 2, axis=1))
    level = np.clip(rms / (np.percentile(rms, 90) + 1e-9), 0, 1)
    smooth = np.convolve(level, [0.25, 0.5, 0.25], mode="same")
    return [round(float(v), 3) for v in smooth]


# --------------------------------------------------------------------------- synthesis helpers
def _t(seconds: float) -> np.ndarray:
    return np.arange(int(seconds * SR)) / SR


def _note_freq(name: str) -> float:
    names = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
    octave = int(name[-1])
    semitone = names[name[:-1]] + (octave + 1) * 12
    return 440.0 * 2 ** ((semitone - 69) / 12)


def _pluck(freq: float, seconds: float, decay: float = 0.35, bright: float = 0.25) -> np.ndarray:
    t = _t(seconds)
    env = np.exp(-t / decay) * np.minimum(1, t / 0.004)
    return env * (np.sin(2 * np.pi * freq * t) + bright * np.sin(2 * np.pi * 4 * freq * t) * np.exp(-t / 0.05))


def _pad_tone(freq: float, seconds: float) -> np.ndarray:
    t = _t(seconds)
    env = np.minimum(1, t / 0.5) * np.minimum(1, (seconds - t) / 0.6)
    tone = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * 2 * freq * t + 0.4)
    return env * tone * (1 + 0.05 * np.sin(2 * np.pi * 0.25 * t))


def _add(target: np.ndarray, sound: np.ndarray, at: float, gain: float) -> None:
    start = int(at * SR)
    if start >= len(target):
        return
    end = min(start + len(sound), len(target))
    target[start:end] += sound[: end - start] * gain


def _noise(seconds: float, seed: int) -> np.ndarray:
    return np.random.default_rng(seed).uniform(-1, 1, int(seconds * SR))


def _smooth(signal: np.ndarray, width: int) -> np.ndarray:
    kernel = np.ones(width) / width
    return np.convolve(signal, kernel, mode="same")


# --------------------------------------------------------------------------- music
PROGRESSION = [("C3", ["C4", "E4", "G4"]), ("A2", ["A3", "C4", "E4"]),
               ("F2", ["F3", "A3", "C4"]), ("G2", ["G3", "B3", "D4"])]


def music_bed(seconds: float, intro: float, outro_start: float, bpm: float = 100) -> np.ndarray:
    """Gentle, uplifting background music: soft pads, a marimba-like arpeggio, round bass, light shaker."""
    out = np.zeros(int(seconds * SR) + SR)
    beat = 60 / bpm
    bar = beat * 4
    bars = int(seconds / bar) + 1
    for b in range(bars):
        at = b * bar
        root, chord = PROGRESSION[b % len(PROGRESSION)]
        for name in chord:
            _add(out, _pad_tone(_note_freq(name), bar + 0.3), at, 0.035)
        for k, step in enumerate([0, 1, 2, 1, 0, 2, 1, 2]):  # eighth-note arpeggio, one octave up
            name = chord[step]
            freq = _note_freq(name) * 2
            _add(out, _pluck(freq, 0.6, decay=0.22), at + k * beat / 2, 0.055 if k % 2 == 0 else 0.04)
        for k in (0, 2):
            _add(out, _pluck(_note_freq(root), 1.2, decay=0.45, bright=0.05), at + k * beat, 0.11)
        for k in range(4):  # shaker on the off-beats
            hiss = _noise(0.06, seed=b * 4 + k)
            hiss = (hiss - _smooth(hiss, 12)) * np.exp(-_t(0.06) / 0.018)
            _add(out, hiss, at + k * beat + beat / 2, 0.025)
    # bright bell melody over the intro and the ending
    melody = ["E5", "G5", "C6", "B5", "G5", "A5", "G5", "E5"]
    for k, name in enumerate(melody):
        _add(out, _pluck(_note_freq(name), 1.2, decay=0.5, bright=0.4), 0.3 + k * beat / 2, 0.07)
        _add(out, _pluck(_note_freq(name), 1.2, decay=0.5, bright=0.4), outro_start + 0.2 + k * beat / 2, 0.06)
    final = outro_start + 0.2 + len(melody) * beat / 2
    for name in ("C4", "E4", "G4", "C5"):
        _add(out, _pad_tone(_note_freq(name), 3.0), final, 0.05)
    fade = np.ones_like(out)
    end = int(seconds * SR)
    fade[max(end - SR, 0) : end] = np.linspace(1, 0, end - max(end - SR, 0))
    fade[end:] = 0
    return (out * fade)[: int(seconds * SR)]


# --------------------------------------------------------------------------- sound effects
def sfx(name: str) -> np.ndarray:
    """Short, soft sound effects (all synthesized)."""
    if name == "pop":
        t = _t(0.12)
        freq = 700 * np.exp(-t * 18) + 220
        return np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t / 0.04)
    if name == "snap":
        click = _noise(0.02, 7) * np.exp(-_t(0.02) / 0.004)
        tone = np.sin(2 * np.pi * 1400 * _t(0.05)) * np.exp(-_t(0.05) / 0.012)
        out = np.zeros(len(tone))
        out[: len(click)] += click * 0.6
        return out + tone * 0.7
    if name == "whoosh":
        seconds = 0.55
        noise = _noise(seconds, 11)
        t = _t(seconds)
        out = np.zeros_like(noise)
        state = 0.0
        coeff = 0.02 + 0.25 * np.sin(np.pi * t / seconds) ** 2  # sweeping low-pass
        for i in range(len(noise)):  # small loop on 26k samples; fine
            state += coeff[i] * (noise[i] - state)
            out[i] = state
        return out * np.sin(np.pi * t / seconds) ** 2 * 3.0
    if name == "chime":
        out = np.zeros(int(1.4 * SR))
        for k, name_ in enumerate(("C6", "E6", "G6")):
            _add(out, _pluck(_note_freq(name_), 1.2, decay=0.45, bright=0.3), k * 0.09, 0.5)
        return out
    if name == "sparkle":
        out = np.zeros(int(0.9 * SR))
        rng = np.random.default_rng(5)
        for k in range(7):
            _add(out, _pluck(rng.uniform(1800, 3200), 0.3, decay=0.08, bright=0.1), k * 0.07, 0.35)
        return out
    if name == "beep_boop":
        out = np.zeros(int(0.45 * SR))
        for k, freq in enumerate((880, 660)):
            t = _t(0.14)
            tone = np.sign(np.sin(2 * np.pi * freq * t)) * 0.3 + np.sin(2 * np.pi * freq * t) * 0.7
            _add(out, tone * np.minimum(1, (0.14 - t) / 0.02) * np.minimum(1, t / 0.005), k * 0.18, 0.35)
        return out
    if name == "boing":
        t = _t(0.6)
        freq = 220 + 120 * np.sin(2 * np.pi * 7 * t) * np.exp(-t / 0.2) + 160 * t
        return np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t / 0.22)
    if name == "oops":  # gentle descending two notes, never a harsh buzzer
        out = np.zeros(int(0.8 * SR))
        _add(out, _pluck(_note_freq("E5"), 0.5, decay=0.18), 0.0, 0.6)
        _add(out, _pluck(_note_freq("C5"), 0.6, decay=0.22), 0.2, 0.6)
        return out
    if name == "tick":
        return np.sin(2 * np.pi * 2000 * _t(0.03)) * np.exp(-_t(0.03) / 0.006)
    if name == "door":
        out = sfx("whoosh") * 0.6
        chime = sfx("chime")
        result = np.zeros(max(len(out), len(chime) + int(0.2 * SR)))
        result[: len(out)] += out
        result[int(0.2 * SR) : int(0.2 * SR) + len(chime)] += chime
        return result
    if name == "zoom":
        t = _t(0.5)
        freq = 300 + 900 * t
        return np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.sin(np.pi * t / 0.5) * 0.6
    raise KeyError(f"unknown sound effect {name!r}")


SFX_GAIN = {"pop": 0.22, "snap": 0.3, "whoosh": 0.25, "chime": 0.3, "sparkle": 0.2, "beep_boop": 0.35,
            "boing": 0.25, "oops": 0.25, "tick": 0.15, "door": 0.3, "zoom": 0.18}


# --------------------------------------------------------------------------- mix
def mix(total: float, voice_events: list[tuple[float, np.ndarray]], sfx_events: list[tuple[float, str]],
        intro: float, outro_start: float) -> np.ndarray:
    """Voices on top, effects below, music ducked under speech; returns stereo float audio."""
    n = int(total * SR) + 1
    voice = np.zeros(n)
    for at, signal in voice_events:
        _add(voice, signal, at, 0.9)
    effects = np.zeros(n)
    for at, name in sfx_events:
        _add(effects, sfx(name), at, SFX_GAIN.get(name, 0.2))
    music = music_bed(total, intro, outro_start)[:n]
    music = np.pad(music, (0, n - len(music)))
    # ducking: music sits about 18 dB under the voice while anyone speaks, and rises gently between lines
    control_rate = 100
    hop = SR // control_rate
    blocks = n // hop + 1
    level = np.pad(np.abs(voice), (0, blocks * hop - n)).reshape(blocks, hop).max(axis=1)
    speaking = (level > 0.02).astype(float)
    target = np.where(speaking > 0, 0.30, 0.75)
    gain = np.empty_like(target)
    state = 0.75
    for i, value in enumerate(target):  # attack fast (80 ms), release slow (450 ms)
        rate = 1 / (0.08 * control_rate) if value < state else 1 / (0.45 * control_rate)
        state += (value - state) * rate
        gain[i] = state
    gain = np.interp(np.arange(n) / hop, np.arange(blocks), gain)
    full = voice + effects + music * gain
    full = np.tanh(full * 1.1) / np.tanh(1.1)  # soft limiter
    # tiny stereo width for music and effects; voices stay centered
    side = (effects * 0.15 + music * gain * 0.25)
    left = np.clip(full + side * 0.2, -1, 1)
    right = np.clip(full - side * 0.2, -1, 1)
    return np.stack([left, right], axis=1)


def write_wav(path: Path, stereo: np.ndarray) -> None:
    import soundfile

    soundfile.write(str(path), stereo.astype(np.float32), SR, subtype="PCM_24")
