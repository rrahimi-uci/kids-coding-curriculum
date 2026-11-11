"""Drawing primitives for animated episodes: cairo shapes, easing, and text in the course font.

Shapes are drawn with cairo (antialiased vector graphics). Text is rendered once with Pillow in
Atkinson Hyperlegible Next (the course font, with a symbol fallback) and cached as a cairo
surface, so every frame shows exactly the same crisp, readable letters.
"""

from __future__ import annotations

import functools
import math
from pathlib import Path

import cairo
import numpy as np

from .. import media

W, H, FPS = 1920, 1080, 30

# Bright, friendly colors built around the Okabe-Ito palette; meaning never relies on color alone.
C = {
    "ink": "#1B2A3A",
    "navy": "#15324A",
    "white": "#FFFFFF",
    "cream": "#FFF7E8",
    "peach": "#FFE3C7",
    "wall": "#FDEBD3",
    "floor": "#E7C9A2",
    "floor_dark": "#D4B188",
    "blue": "#2F80ED",
    "sky": "#56B4E9",
    "sky_light": "#DDF2FC",
    "orange": "#E69F00",
    "orange_light": "#FFD48A",
    "green": "#009E73",
    "green_light": "#C8F0E2",
    "yellow": "#F0C419",
    "vermillion": "#D55E00",
    "pink": "#F28CB1",
    "purple": "#8E6BD8",
    "gray": "#8A97A6",
    "gray_light": "#E9EEF3",
    "skin": "#B9784F",
    "hair": "#6B3F22",  # Rose's long brown hair (and eyebrows)
    "hair_shade": "#4F2D17",
    "hair_shine": "#94603A",
    "wood": "#B9773F",
    "wood_dark": "#8C5427",
    "gold": "#F5C542",
    "screen": "#14283C",
    "led": "#5DE4F5",
}


def safe_scale(ctx: cairo.Context, sx: float, sy: float | None = None) -> None:
    """ctx.scale that never makes a singular matrix (things grow from or shrink to nothing)."""
    sy = sx if sy is None else sy
    ctx.scale(math.copysign(max(abs(sx), 1e-3), sx), math.copysign(max(abs(sy), 1e-3), sy))


def rgb(color: str, alpha: float = 1.0) -> tuple[float, float, float, float]:
    color = color.lstrip("#")
    r, g, b = (int(color[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return r, g, b, alpha


def set_color(ctx: cairo.Context, color: str, alpha: float = 1.0) -> None:
    ctx.set_source_rgba(*rgb(color, alpha))


# --------------------------------------------------------------------------- easing and timing
def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def progress(t: float, start: float, duration: float) -> float:
    return clamp((t - start) / duration) if duration > 0 else float(t >= start)


def ease_in_out(x: float) -> float:
    x = clamp(x)
    return 4 * x * x * x if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def ease_out(x: float) -> float:
    x = clamp(x)
    return 1 - (1 - x) ** 3


def ease_out_back(x: float, overshoot: float = 1.7) -> float:
    """Pop-in with a gentle overshoot."""
    x = clamp(x)
    c3 = overshoot + 1
    return 1 + c3 * (x - 1) ** 3 + overshoot * (x - 1) ** 2


def lerp(a: float, b: float, x: float) -> float:
    return a + (b - a) * x


def appear(t: float, start: float, duration: float = 0.45) -> float:
    """0 before `start`, pops to 1 with an overshoot."""
    return ease_out_back(progress(t, start, duration)) if t >= start else 0.0


def fade(t: float, start: float, duration: float = 0.4) -> float:
    return ease_out(progress(t, start, duration))


def blink(t: float, seed: float = 0.0) -> float:
    """Eye openness (1 open, 0 closed) with a natural blink every few seconds."""
    period = 3.4 + (seed % 1.3)
    phase = (t + seed * 1.7) % period
    if phase < 0.14:
        return abs(phase - 0.07) / 0.07
    return 1.0


# --------------------------------------------------------------------------- shapes
def rounded_rect(ctx: cairo.Context, x: float, y: float, w: float, h: float, r: float) -> None:
    r = min(r, w / 2, h / 2)
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()


def fill_rounded(ctx, x, y, w, h, r, color, alpha=1.0, stroke: str | None = None, width: float = 0) -> None:
    rounded_rect(ctx, x, y, w, h, r)
    set_color(ctx, color, alpha)
    if stroke:
        ctx.fill_preserve()
        set_color(ctx, stroke, alpha)
        ctx.set_line_width(width)
        ctx.stroke()
    else:
        ctx.fill()


def circle(ctx, x, y, r, color, alpha=1.0, stroke: str | None = None, width: float = 0) -> None:
    ctx.new_sub_path()
    ctx.arc(x, y, max(r, 0.01), 0, 2 * math.pi)
    set_color(ctx, color, alpha)
    if stroke:
        ctx.fill_preserve()
        set_color(ctx, stroke, alpha)
        ctx.set_line_width(width)
        ctx.stroke()
    else:
        ctx.fill()


def ellipse(ctx, x, y, rx, ry, color, alpha=1.0) -> None:
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, max(rx, 0.01), max(ry, 0.01))
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    set_color(ctx, color, alpha)
    ctx.fill()


def line(ctx, x1, y1, x2, y2, color, width, alpha=1.0, cap=cairo.LINE_CAP_ROUND) -> None:
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    set_color(ctx, color, alpha)
    ctx.set_line_width(width)
    ctx.set_line_cap(cap)
    ctx.stroke()


def shadow(ctx, x, y, rx, ry, alpha=0.18) -> None:
    ellipse(ctx, x, y, rx, ry, "#000000", alpha)


def check_mark(ctx, x, y, size, color="#FFFFFF", width=None, amount=1.0) -> None:
    """A drawn check mark (not a font glyph) that can animate in with `amount`."""
    points = [(-0.42, 0.02), (-0.12, 0.32), (0.45, -0.32)]
    pts = [(x + px * size, y + py * size) for px, py in points]
    ctx.move_to(*pts[0])
    first = math.dist(pts[0], pts[1])
    total = first + math.dist(pts[1], pts[2])
    target = total * clamp(amount)
    if target <= first:
        f = target / first
        ctx.line_to(lerp(pts[0][0], pts[1][0], f), lerp(pts[0][1], pts[1][1], f))
    else:
        ctx.line_to(*pts[1])
        f = (target - first) / (total - first)
        ctx.line_to(lerp(pts[1][0], pts[2][0], f), lerp(pts[1][1], pts[2][1], f))
    set_color(ctx, color)
    ctx.set_line_width(width or size * 0.16)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()


def cross_mark(ctx, x, y, size, color="#FFFFFF", width=None) -> None:
    s = size * 0.36
    line(ctx, x - s, y - s, x + s, y + s, color, width or size * 0.16)
    line(ctx, x - s, y + s, x + s, y - s, color, width or size * 0.16)


def star(ctx, x, y, r, color, alpha=1.0, points=5, rotation=0.0) -> None:
    ctx.new_path()
    for i in range(points * 2):
        radius = r if i % 2 == 0 else r * 0.45
        angle = rotation - math.pi / 2 + i * math.pi / points
        ctx.line_to(x + radius * math.cos(angle), y + radius * math.sin(angle))
    ctx.close_path()
    set_color(ctx, color, alpha)
    ctx.fill()


def glow(ctx, x, y, r, color, alpha=0.6) -> None:
    gradient = cairo.RadialGradient(x, y, 0, x, y, r)
    gradient.add_color_stop_rgba(0, *rgb(color, alpha))
    gradient.add_color_stop_rgba(1, *rgb(color, 0))
    ctx.set_source(gradient)
    ctx.arc(x, y, r, 0, 2 * math.pi)
    ctx.fill()


def vertical_gradient(ctx, x, y, w, h, top: str, bottom: str) -> None:
    gradient = cairo.LinearGradient(0, y, 0, y + h)
    gradient.add_color_stop_rgb(0, *rgb(top)[:3])
    gradient.add_color_stop_rgb(1, *rgb(bottom)[:3])
    ctx.set_source(gradient)
    ctx.rectangle(x, y, w, h)
    ctx.fill()


# --------------------------------------------------------------------------- text
@functools.lru_cache(maxsize=None)
def mono_font(size: int, bold: bool = False):
    """The course's code font (Atkinson Hyperlegible Mono), falling back to Menlo."""
    import shutil
    import subprocess

    from PIL import ImageFont

    name = "AtkinsonHyperlegibleMono-Bold.otf" if bold else "AtkinsonHyperlegibleMono-Regular.otf"
    path = None
    if shutil.which("kpsewhich"):
        path = subprocess.run(["kpsewhich", name], capture_output=True, text=True).stdout.strip() or None
    for candidate in (path, "/System/Library/Fonts/Menlo.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"):
        if candidate and Path(candidate).is_file():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default(size=size)


def mono_width(size: int) -> float:
    return mono_font(size).getlength("M")


@functools.lru_cache(maxsize=4096)
def _text_surface(text: str, size: int, color: str, bold: bool, max_width: int, align: str, spacing: float,
                  mono: bool = False):
    """Render text with Pillow in the course font and convert it to a premultiplied cairo surface."""
    from PIL import Image, ImageDraw

    font = mono_font(size, bold) if mono else media._font(size, bold)
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    lines = media._wrap(probe, text, font, max_width) if max_width else [text]
    ascent, descent = font.getmetrics()
    line_height = int((ascent + descent) * spacing)
    width = max(int(media._text_width(probe, ln, font)) for ln in lines) + 8
    height = line_height * len(lines) + 8
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fill = tuple(int(c * 255) for c in rgb(color)[:3]) + (255,)
    for number, ln in enumerate(lines):
        line_width = media._text_width(draw, ln, font)
        x = {"left": 4, "center": (width - line_width) / 2, "right": width - line_width - 4}[align]
        media._draw_text(draw, (x, 4 + number * line_height), ln, font, fill)
    rgba = np.asarray(image, dtype=np.float32) / 255.0
    alpha = rgba[..., 3:4]
    premultiplied = np.concatenate([rgba[..., 2:3] * alpha, rgba[..., 1:2] * alpha, rgba[..., 0:1] * alpha, alpha], axis=2)
    data = bytearray((premultiplied * 255 + 0.5).astype(np.uint8).tobytes())
    stride = cairo.ImageSurface.format_stride_for_width(cairo.FORMAT_ARGB32, width)
    if stride != width * 4:  # pad rows to cairo's stride
        rows = [bytes(data[r * width * 4 : (r + 1) * width * 4]).ljust(stride, b"\0") for r in range(height)]
        data = bytearray(b"".join(rows))
    surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, width, height, stride)
    return surface, data, width, height  # keep `data` alive with the surface


def text_size(text: str, size: int, bold: bool = False, max_width: int = 0, spacing: float = 1.15,
              mono: bool = False) -> tuple[int, int]:
    _, _, width, height = _text_surface(text, size, "#000000", bold, max_width, "left", spacing, mono)
    return width, height


def text(ctx, value: str, x: float, y: float, size: int, color: str = C["ink"], bold: bool = False,
         anchor: str = "center", alpha: float = 1.0, scale: float = 1.0, max_width: int = 0,
         align: str = "center", spacing: float = 1.15, mono: bool = False) -> tuple[int, int]:
    """Draw text. `anchor` is center, left (x is the left edge, y the middle) or topleft."""
    surface, _, width, height = _text_surface(value, size, color, bold, max_width, align, spacing, mono)
    if alpha <= 0 or scale < 0.02:
        return width, height
    xx, yx, xy, yy, _, _ = ctx.get_matrix()
    if abs(xx * yy - xy * yx) < 1e-3:  # an element scaled to (almost) nothing: drawing would fail
        return width, height
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, scale, scale)
    offset = {"center": (-width / 2, -height / 2), "left": (0, -height / 2), "topleft": (0, 0)}[anchor]
    ctx.set_source_surface(surface, *offset)
    ctx.paint_with_alpha(clamp(alpha))
    ctx.restore()
    return width, height


# --------------------------------------------------------------------------- frames
def new_frame() -> tuple[cairo.ImageSurface, cairo.Context]:
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surface)
    ctx.set_antialias(cairo.ANTIALIAS_BEST)
    return surface, ctx


def scaled(ctx, x: float, y: float, s: float):
    """Context manager: draw around (x, y) at scale s."""
    class _Scope:
        def __enter__(self_inner):
            ctx.save()
            ctx.translate(x, y)
            safe_scale(ctx, s, s)
            return ctx

        def __exit__(self_inner, *exc):
            ctx.restore()
            return False

    return _Scope()
