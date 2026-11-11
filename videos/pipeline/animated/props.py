"""Reusable props and on-screen elements for animated episodes."""

from __future__ import annotations

import math
import random

import cairo

from .engine import (
    C, H, W, appear, check_mark, circle, clamp, cross_mark, ease_out, ellipse, fill_rounded, glow, line,
    rounded_rect, set_color, star, text, text_size, vertical_gradient,
)


# --------------------------------------------------------------------------- backgrounds
def workshop(ctx: cairo.Context, t: float, floor_y: int = 780) -> None:
    """A warm, uncluttered workshop: wall, window, shelf with gears, pegboard, wooden floor."""
    vertical_gradient(ctx, 0, 0, W, floor_y, "#FFF4E2", "#FDE1C0")
    # window with sky
    fill_rounded(ctx, 1380, 120, 360, 260, 24, C["white"])
    vertical_gradient(ctx, 1396, 136, 328, 228, "#BFE6FA", "#E8F6FE")
    circle(ctx, 1640, 200, 34, "#FFE08A")
    for cx in (1460, 1520):
        circle(ctx, cx + 30 * math.sin(t * 0.05), 300, 28, C["white"], 0.9)
    line(ctx, 1560, 136, 1560, 364, C["white"], 12)
    line(ctx, 1396, 250, 1724, 250, C["white"], 12)
    # shelf with a gear and boxes
    fill_rounded(ctx, 160, 300, 420, 22, 8, C["wood"])
    _gear(ctx, 240, 250, 42, t * 0.4, C["sky"])
    fill_rounded(ctx, 320, 222, 90, 78, 10, C["orange_light"])
    fill_rounded(ctx, 430, 246, 110, 54, 10, C["green_light"])
    # pegboard with tools (simple shapes)
    fill_rounded(ctx, 700, 150, 420, 230, 20, "#F3D9B5")
    for gx in range(8):
        for gy in range(4):
            circle(ctx, 730 + gx * 52, 180 + gy * 52, 4, "#D9B78E")
    line(ctx, 790, 200, 790, 320, C["gray"], 12)
    circle(ctx, 790, 200, 18, C["gray"])
    fill_rounded(ctx, 880, 210, 30, 120, 10, C["vermillion"])
    _gear(ctx, 1020, 260, 36, -t * 0.5, C["orange"])
    # floor
    vertical_gradient(ctx, 0, floor_y, W, H - floor_y, C["floor"], C["floor_dark"])
    for x in range(0, W, 240):
        line(ctx, x, floor_y, x - 80, H, "#C9A47A", 3, 0.5)


def _gear(ctx, x, y, r, angle, color) -> None:
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    for i in range(8):
        ctx.save()
        ctx.rotate(i * math.pi / 4)
        fill_rounded(ctx, -r * 0.18, -r * 1.25, r * 0.36, r * 0.5, 4, color)
        ctx.restore()
    circle(ctx, 0, 0, r, color)
    circle(ctx, 0, 0, r * 0.4, "#FFF4E2")
    ctx.restore()


def soft_background(ctx: cairo.Context, top: str = "#EAF6FF", bottom: str = "#FFFFFF") -> None:
    vertical_gradient(ctx, 0, 0, W, H, top, bottom)


# --------------------------------------------------------------------------- objects
def key(ctx, x, y, s, t, glowing: bool = True, angle: float = 0.0) -> None:
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    ctx.scale(s, s)
    if glowing:
        glow(ctx, 0, 0, 70, C["gold"], 0.45 + 0.15 * math.sin(t * 6))
        for i in range(3):
            a = t * 2 + i * 2.1
            star(ctx, 46 * math.cos(a), 30 * math.sin(a), 6, C["white"], 0.9, rotation=t)
    circle(ctx, -26, 0, 22, C["gold"], stroke="#B8860B", width=4)
    circle(ctx, -26, 0, 9, "#FFF4E2")
    fill_rounded(ctx, -6, -7, 60, 14, 6, C["gold"], stroke="#B8860B", width=3)
    fill_rounded(ctx, 34, 4, 10, 16, 3, C["gold"])
    fill_rounded(ctx, 46, 4, 8, 12, 3, C["gold"])
    ctx.restore()


def door(ctx, x, y, w, h, t, opened: float = 0.0, locked: bool = True, label: str = "DOOR") -> None:
    """A wooden door with its bottom-left corner at (x, y). opened 0-1 swings it open with light."""
    fill_rounded(ctx, x - 16, y - h - 16, w + 32, h + 16, 18, C["wood_dark"])
    if opened > 0:
        glow(ctx, x + w / 2, y - h / 2, h * 0.8, "#FFF2B3", 0.8 * opened)
        fill_rounded(ctx, x, y - h, w, h, 10, "#FFF6CF")
    width = w * (1 - 0.82 * ease_out(opened))
    fill_rounded(ctx, x, y - h, width, h, 10, C["wood"])
    if width > w * 0.4:
        fill_rounded(ctx, x + width * 0.14, y - h + 30, width * 0.72, h * 0.36, 8, "#C98A52")
        fill_rounded(ctx, x + width * 0.14, y - h * 0.5, width * 0.72, h * 0.36, 8, "#C98A52")
        circle(ctx, x + width - 26, y - h * 0.48, 10, C["gold"])
        if locked:
            _padlock(ctx, x + width / 2, y - h * 0.62, 1.0)
    if label:
        fill_rounded(ctx, x + w / 2 - 70, y - h - 74, 140, 48, 12, C["navy"])
        text(ctx, label, x + w / 2, y - h - 50, 30, C["white"], bold=True)


def _padlock(ctx, x, y, s) -> None:
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(s, s)
    ctx.arc(0, -10, 18, math.pi, 0)
    set_color(ctx, C["gray"])
    ctx.set_line_width(8)
    ctx.stroke()
    fill_rounded(ctx, -26, -10, 52, 40, 8, C["gray"])
    circle(ctx, 0, 8, 6, C["ink"])
    ctx.restore()


def chair(ctx, x, y, s) -> None:
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(s, s)
    for lx in (-50, 44):
        fill_rounded(ctx, lx, -90, 12, 90, 5, C["wood_dark"])
    fill_rounded(ctx, -60, -104, 120, 22, 8, C["wood"])
    fill_rounded(ctx, 40, -230, 16, 130, 6, C["wood_dark"])
    fill_rounded(ctx, -10, -230, 66, 60, 10, C["wood"])
    ctx.restore()


# --------------------------------------------------------------------------- UI elements
def chip(ctx, x, y, label, t, start, color=C["sky_light"], ink=C["navy"], size=42, anchor="center") -> float:
    """A rounded label that pops in at `start`. Returns its width."""
    amount = appear(t, start)
    tw, th = text_size(label, size, bold=True)
    w, h = tw + 64, th + 26
    if amount <= 0:
        return w
    ctx.save()
    cx = x if anchor == "center" else x + w / 2
    ctx.translate(cx, y)
    ctx.scale(max(amount, 1e-3), max(amount, 1e-3))
    fill_rounded(ctx, -w / 2 + 4, -h / 2 + 6, w, h, h / 2, "#000000", 0.10)
    fill_rounded(ctx, -w / 2, -h / 2, w, h, h / 2, color)
    text(ctx, label, 0, 0, size, ink, bold=True)
    ctx.restore()
    return w


def title_banner(ctx, label, t, start, y=96, size=56, color=C["navy"]) -> None:
    amount = appear(t, start, 0.5)
    if amount <= 0:
        return
    tw, th = text_size(label, size, bold=True)
    w, h = tw + 90, th + 34
    ctx.save()
    ctx.translate(W / 2, y)
    ctx.scale(max(amount, 1e-3), max(amount, 1e-3))
    fill_rounded(ctx, -w / 2 + 6, -h / 2 + 8, w, h, 26, "#000000", 0.12)
    fill_rounded(ctx, -w / 2, -h / 2, w, h, 26, color)
    text(ctx, label, 0, 0, size, C["white"], bold=True)
    ctx.restore()


def speech_bubble(ctx, x, y, label, t, start, end=None, size=40, tail="down-left", max_width=520) -> None:
    """A speech bubble whose tail points at (x, y); it pops in at start and shrinks away at end."""
    amount = appear(t, start, 0.35)
    if end is not None and t > end:
        amount *= 1 - ease_out((t - end) / 0.25)
    if amount <= 0.01:
        return
    tw, th = text_size(label, size, bold=True, max_width=max_width)
    w, h = tw + 60, th + 40
    dx = {"down-left": 40, "down-right": -40 - w, "down": -w / 2}[tail]
    bx, by = x + dx, y - 40 - h
    bx = min(max(bx, 24), W - 24 - w)  # always keep the whole bubble on screen
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(amount, 1e-3), max(amount, 1e-3))
    ctx.translate(-x, -y)
    fill_rounded(ctx, bx + 4, by + 6, w, h, 28, "#000000", 0.10)
    rounded_rect(ctx, bx, by, w, h, 28)
    tail_x = min(max(x + (20 if tail == "down-left" else -20 if tail == "down-right" else 0), bx + 40), bx + w - 40)
    ctx.move_to(tail_x - 18, by + h - 2)
    ctx.line_to(x, y)
    ctx.line_to(tail_x + 22, by + h - 2)
    set_color(ctx, C["white"])
    ctx.fill_preserve()
    set_color(ctx, C["navy"])
    ctx.set_line_width(4)
    ctx.stroke()
    rounded_rect(ctx, bx, by, w, h, 28)
    set_color(ctx, C["white"])
    ctx.fill()
    text(ctx, label, bx + w / 2, by + h / 2, size, C["ink"], bold=True, max_width=max_width)
    ctx.restore()


def thought_bubble(ctx, x, y, t, start, end, label: str = "") -> None:
    """A thinking bubble with three animated dots (or a short label) during a pause."""
    if t < start or t > end + 0.3:
        return
    amount = appear(t, start, 0.4) * (1 - ease_out((t - end) / 0.3) if t > end else 1)
    if amount <= 0.01:  # a zero-size bubble would make cairo's matrix singular
        return
    width = max(300, text_size(label, 40, bold=True)[0] + 90) if label else 300
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(amount, 1e-3), max(amount, 1e-3))
    circle(ctx, -60, 90, 14, C["white"], stroke=C["navy"], width=3)
    circle(ctx, -30, 55, 22, C["white"], stroke=C["navy"], width=3)
    fill_rounded(ctx, -width / 2, -110, width, 140, 60, C["white"], stroke=C["navy"], width=4)
    if label:
        text(ctx, label, 0, -40, 40, C["navy"], bold=True)
    else:
        for i in range(3):
            bounce = max(0.0, math.sin((t - start) * 6 - i * 0.7)) * 14
            circle(ctx, -50 + i * 50, -40 - bounce, 16, C["sky"])
    ctx.restore()


def step_card(ctx, x, y, w, number: int, label: str, t, start, active: float = 0.0, done: bool = False,
              color=C["blue"], size=38) -> None:
    """A numbered instruction card. active 0-1 highlights it; done shows a check badge."""
    amount = appear(t, start)
    if amount <= 0:
        return
    h = 92
    ctx.save()
    ctx.translate(x + w / 2, y + h / 2)
    grow = 1 + 0.06 * active
    ctx.scale(max(amount * grow, 1e-3), max(amount * grow, 1e-3))
    if active > 0:
        fill_rounded(ctx, -w / 2 - 10, -h / 2 - 10, w + 20, h + 20, 30, C["yellow"], 0.35 * active)
    fill_rounded(ctx, -w / 2 + 4, -h / 2 + 6, w, h, 22, "#000000", 0.10)
    fill_rounded(ctx, -w / 2, -h / 2, w, h, 22, C["white"], stroke=C["yellow"] if active > 0.5 else C["navy"],
                 width=6 if active > 0.5 else 4)
    circle(ctx, -w / 2 + 50, 0, 30, color)
    text(ctx, str(number), -w / 2 + 50, 0, 36, C["white"], bold=True)
    text(ctx, label, -w / 2 + 96, 0, size, C["ink"], bold=True, anchor="left")
    if done:
        circle(ctx, w / 2 - 42, 0, 24, C["green"])
        check_mark(ctx, w / 2 - 42, 0, 34)
    ctx.restore()


def badge(ctx, x, y, r, ok: bool, t, start) -> None:
    amount = appear(t, start, 0.4)
    if amount <= 0:
        return
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(amount, 1e-3), max(amount, 1e-3))
    circle(ctx, 0, 0, r, C["green"] if ok else C["vermillion"])
    if ok:
        check_mark(ctx, 0, 0, r * 1.3, amount=clamp((t - start) / 0.4))
    else:
        cross_mark(ctx, 0, 0, r * 1.3)
    ctx.restore()


def confetti(ctx, x, y, t, start, count=40, spread=520, seed=3) -> None:
    if t < start or t > start + 2.4:
        return
    rng = random.Random(seed)
    k = t - start
    colors = [C["orange"], C["sky"], C["green"], C["yellow"], C["pink"], C["purple"]]
    for _ in range(count):
        angle = rng.uniform(-math.pi * 0.95, -math.pi * 0.05)
        speed = rng.uniform(300, 700)
        px = x + math.cos(angle) * speed * k * (spread / 520)
        py = y + math.sin(angle) * speed * k + 600 * k * k
        alpha = clamp(1.6 - k * 0.7)
        ctx.save()
        ctx.translate(px, py)
        ctx.rotate(k * rng.uniform(-8, 8))
        fill_rounded(ctx, -8, -4, 16, 8, 2, rng.choice(colors), alpha)
        ctx.restore()


def magnifier(ctx, x, y, s, t) -> None:
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(s, s)
    ctx.rotate(-0.5)
    line(ctx, 0, 60, 0, 150, C["wood_dark"], 26)
    circle(ctx, 0, 0, 62, C["sky_light"], 0.35)
    ctx.arc(0, 0, 62, 0, 2 * math.pi)
    set_color(ctx, C["navy"])
    ctx.set_line_width(14)
    ctx.stroke()
    ctx.arc(-18, -18, 32, math.pi * 1.05, math.pi * 1.45)
    set_color(ctx, C["white"], 0.9)
    ctx.set_line_width(8)
    ctx.stroke()
    ctx.restore()


def pointer_hand(ctx, x, y, s) -> None:
    """A hand whose index finger points left at (x, y) (for 'read the blocks with your finger')."""
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(s, s)
    fill_rounded(ctx, 0, -11, 80, 22, 11, C["skin"], stroke="#8A5534", width=3)  # index finger
    fill_rounded(ctx, 60, -34, 78, 70, 26, C["skin"], stroke="#8A5534", width=3)  # hand
    fill_rounded(ctx, 120, -26, 70, 54, 18, C["blue"])  # sleeve
    ctx.restore()


# --------------------------------------------------------------------------- block code (our own block style)
BLOCK_COLORS = {"event": (C["yellow"], "#C79A00"), "looks": ("#9966FF", "#774DCB"),
                "motion": ("#4C97FF", "#3373CC"), "sound": ("#CF63CF", "#BD42BD")}


def code_block(ctx, x, y, kind: str, parts: list[str], t: float = 0.0, highlight: float = 0.0, hat: bool = False,
               scale: float = 1.0) -> tuple[float, float]:
    """A snap-together code block at (x, y) (top-left). parts: words; '[..]' entries draw as white inputs.

    Returns (width, height) in unscaled units. hat=True draws an event 'hat' block.
    """
    fill, edge = BLOCK_COLORS[kind]
    size = 34
    widths = []
    for part in parts:
        label = part.strip("[]")
        tw, _ = text_size(label, size, bold=True)
        widths.append(tw + (36 if part.startswith("[") else 10))
    w = max(260, sum(widths) + 40 + 14 * len(parts))
    h = 76
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(scale, scale)
    if highlight > 0:
        fill_rounded(ctx, -12, -14, w + 24, h + 30, 22, C["yellow"], 0.45 * highlight)
    _block_path(ctx, w, h, hat)
    set_color(ctx, fill)
    ctx.fill_preserve()
    set_color(ctx, C["white"] if highlight > 0.5 else edge)
    ctx.set_line_width(6 if highlight > 0.5 else 3)
    ctx.stroke()
    cx = 24
    for part, pw in zip(parts, widths):
        label = part.strip("[]")
        if part == "{flag}":
            _flag(ctx, cx + 20, h / 2 + (6 if hat else 0))
            cx += 50
            continue
        if part.startswith("["):
            fill_rounded(ctx, cx, h / 2 - 24 + (6 if hat else 0), pw, 48, 24, C["white"])
            text(ctx, label, cx + pw / 2, h / 2 + (6 if hat else 0), size - 2, "#575E75", bold=True)
        else:
            text(ctx, label, cx, h / 2 + (6 if hat else 0), size, C["white"], bold=True, anchor="left")
        cx += pw + 14
    ctx.restore()
    return w, h


def _block_path(ctx, w, h, hat) -> None:
    r, notch_x, nw, nd = 10, 30, 44, 10
    ctx.new_path()
    if hat:
        ctx.move_to(0, 18)
        ctx.curve_to(40, -26, 120, -26, 160, 18)
        ctx.line_to(w - r, 18)
        ctx.arc(w - r, 18 + r, r, -math.pi / 2, 0)
    else:
        ctx.move_to(0, r)
        ctx.arc(r, r, r, math.pi, 3 * math.pi / 2)
        ctx.line_to(notch_x, 0)
        ctx.line_to(notch_x + 10, nd)
        ctx.line_to(notch_x + nw - 10, nd)
        ctx.line_to(notch_x + nw, 0)
        ctx.line_to(w - r, 0)
        ctx.arc(w - r, r, r, -math.pi / 2, 0)
    ctx.line_to(w, h - r)
    ctx.arc(w - r, h - r, r, 0, math.pi / 2)
    ctx.line_to(notch_x + nw, h)
    ctx.line_to(notch_x + nw - 10, h + nd)
    ctx.line_to(notch_x + 10, h + nd)
    ctx.line_to(notch_x, h)
    ctx.line_to(r, h)
    ctx.arc(r, h - r, r, math.pi / 2, math.pi)
    ctx.close_path()


def _flag(ctx, x, y) -> None:
    line(ctx, x - 12, y - 18, x - 12, y + 20, "#2E7D32", 5)
    ctx.move_to(x - 10, y - 18)
    ctx.curve_to(x, y - 26, x + 8, y - 8, x + 20, y - 16)
    ctx.line_to(x + 20, y + 2)
    ctx.curve_to(x + 8, y + 10, x, y - 8, x - 10, y)
    ctx.close_path()
    set_color(ctx, "#4CBF56")
    ctx.fill()


def green_flag_button(ctx, x, y, r, pressed: float = 0.0) -> None:
    circle(ctx, x, y + 4, r, "#000000", 0.12)
    circle(ctx, x, y + 3 * pressed, r, C["white"], stroke=C["navy"], width=4)
    _flag(ctx, x + 4, y + 3 * pressed)


# --------------------------------------------------------------------------- titles and transitions
SITE_URL = "https://rrahimi-uci.github.io/kids-coding-curriculum/"
SERIES = "Kids Coding"
SUBTITLE = "with Nova and Pixel"


def logo_mark(ctx, x, y, size, t: float = 9.0, start: float = 0.0) -> None:
    """The website's logo (site/src/layouts/Base.astro): three code bars and a chevron, in a 32-unit box.

    Drawn at (x, y) top-left, `size` pixels wide. The bars slide in one after another from `start`.
    """
    u = size / 32
    bars = ((3, 13, "#E69F00"), (12.5, 19, "#0072B2"), (22, 15, "#009E73"))
    for i, (by, bw, color) in enumerate(bars):
        k = ease_out(clamp((t - start - i * 0.12) / 0.35))
        if k > 0:
            fill_rounded(ctx, x + 2 * u, y + by * u, bw * u * k, 7 * u, 2.5 * u, color)
    k = ease_out(clamp((t - start - 0.4) / 0.35))
    if k > 0:
        ctx.move_to(x + 24 * u, y + 8 * u)
        ctx.line_to(x + (24 + 6 * k) * u, y + (8 + 8 * k) * u)
        if k > 0.5:
            ctx.line_to(x + 24 * u, y + (16 + 16 * (k - 0.5)) * u)
        set_color(ctx, "#D55E00")
        ctx.set_line_width(3 * u)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.stroke()


def logo(ctx, x, y, s, t, start) -> None:
    """The series logo: the website's mark and 'Kids Coding' wordmark, with 'with Nova and Pixel'."""
    amount = appear(t, start, 0.6)
    if amount <= 0:
        return
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(s * amount, 1e-3), max(s * amount, 1e-3))
    fill_rounded(ctx, -490, -150, 1000, 300, 70, "#000000", 0.14)
    fill_rounded(ctx, -500, -160, 1000, 300, 70, C["white"])
    logo_mark(ctx, -455, -110, 200, t, start + 0.2)
    text(ctx, SERIES, -215, -38, 118, C["ink"], bold=True, anchor="left")
    text(ctx, SUBTITLE, -212, 66, 48, "#0072B2", bold=True, anchor="left")
    ctx.restore()


def footer(ctx, width: int, height: int, band: int) -> None:
    """The bottom band shown in every video: the logo, the name and the website address."""
    ctx.rectangle(0, height - band, width, band)
    set_color(ctx, C["white"])
    ctx.fill()
    size = 26
    label = f"{SERIES} with Nova and Pixel  •  {SITE_URL}"
    tw, _ = text_size(label, size, bold=False)
    mark = 30
    total = mark + 14 + tw
    x0 = (width - total) / 2
    cy = height - band / 2
    logo_mark(ctx, x0, cy - mark / 2, mark)
    text(ctx, label, x0 + mark + 14, cy, size, "#3D4A57", anchor="left")


def iris(ctx, cx, cy, radius) -> None:
    """Clip to a circle (used for circular wipe transitions)."""
    ctx.new_path()
    ctx.arc(cx, cy, max(radius, 0.1), 0, 2 * math.pi)
    ctx.clip()
