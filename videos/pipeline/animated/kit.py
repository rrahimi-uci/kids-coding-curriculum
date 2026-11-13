"""The animation kit: draws any episode written in the kit_dsl data format.

Each action kind has one drawing function (`COMPONENTS[kind]`). They all share the same look as the
hand-made Week 1 episode (same characters, palette, fonts, props and transitions) so every video in
the series feels like one show. Code panels and turtle canvases run the real code (pyrun) and show
its true output.
"""

from __future__ import annotations

import functools
import math
import re
from types import SimpleNamespace

from . import props as P
from . import pyrun
from .characters import AIDEN_HEAD_TOP, ROSE_HEAD_TOP, draw_aiden, draw_cat, draw_grown_up, draw_rose, draw_pixi
from .engine import (
    safe_scale,
    C, FPS, H, W, appear, check_mark, circle, clamp, cross_mark, ease_in_out, ease_out, ellipse, fade,
    fill_rounded, glow, lerp, line, mono_width, progress, rounded_rect, set_color, star, text, text_size,
    vertical_gradient,
)
from .kit_dsl import A, Episode, resolve_time
from .timeline import AIDEN, ROSE, PIXI, SceneTiming

COLORS = {"blue": C["blue"], "sky": C["sky_light"], "orange": C["orange_light"], "green": C["green_light"],
          "yellow": C["yellow"], "white": C["white"], "navy": C["navy"], "pink": "#FBD3E2", "purple": "#E3D8FB",
          "red": "#F9C9B6", "gray": C["gray_light"]}
INK = {"navy": C["white"], "blue": C["white"]}
STRONG = {"navy": C["navy"], "green": C["green"], "orange": "#C77700", "blue": C["blue"], "red": C["vermillion"],
          "purple": "#6B4FC2", "pink": "#C2185B"}


def color(name: str | None, default: str = "sky") -> str:
    name = name or default
    return COLORS.get(name, name)


# =============================================================================== drawing context
class D:
    """Everything a component needs for one frame."""

    def __init__(self, ctx, t: float, gt: float, sc: SceneTiming, resolve):
        self.ctx, self.t, self.gt, self.sc = ctx, t, gt, sc
        self.T = resolve

    def windows(self, value) -> list[tuple[float, float]]:
        """A list of (from, to) windows from: a cue, a (from, to) pair, or a list of either."""
        if value is None:
            return []
        if isinstance(value, (str, int, float)):
            # a bare cue lasts until the next beat starts; any other single time lasts one second
            if isinstance(value, str) and re.fullmatch(r"[A-Za-z_]\w*", value) and value not in ("start", "end"):
                return [(self.T(value), self.T(value + ">"))]
            return [(self.T(value), self.T(value) + 1.0)]
        if isinstance(value, tuple) and len(value) == 2 and not isinstance(value[0], (list, tuple)):
            return [(self.T(value[0]), self.T(value[1]))]
        result = []
        for item in value:
            result += self.windows(item)
        return result

    def within(self, value) -> float:
        """1 inside any window (with a short ease in and out), else 0."""
        best = 0.0
        for start, end in self.windows(value):
            if start <= self.t <= end:
                best = max(best, min(1.0, (self.t - start) / 0.25, (end - self.t) / 0.25 + 0.0001))
        return clamp(best)

    @staticmethod
    def _entries(pairs):
        """(time, value) pairs from a dict or a list of (time, value...) tuples; extra parts become a tuple."""
        items = list(pairs.items()) if isinstance(pairs, dict) else list(pairs)
        return [(item[0], item[1] if len(item) == 2 else tuple(item[1:])) for item in items]

    def keyed(self, pairs, default=None):
        """Latest value from {time: value} or [(time, value)] whose time has passed."""
        if pairs is None:
            return default
        current = default
        for when, value in sorted(((self.T(w), v) for w, v in self._entries(pairs)), key=lambda p: p[0]):
            if self.t >= when:
                current = value
        return current

    def keyed_with_time(self, pairs):
        current, since = None, -1.0
        for when, value in sorted(((self.T(w), v) for w, v in self._entries(pairs)), key=lambda p: p[0]):
            if self.t >= when:
                current, since = value, when
        return current, since

    def path(self, keyframes, default_xy):
        """Position along [(time, x, y), ...] with eased moves between keyframes."""
        if not keyframes:
            return default_xy
        frames = sorted(((self.T(k[0]), k[1], k[2]) for k in keyframes), key=lambda f: f[0])
        x, y = default_xy
        previous = (0.0, x, y)
        for when, fx, fy in frames:
            if self.t < when:
                duration = max(0.35, min(1.2, when - previous[0])) if previous[0] < when else 0.6
                start = when - duration
                k = ease_in_out(progress(self.t, start, duration))
                return lerp(previous[1], fx, k), lerp(previous[2], fy, k)
            previous = (when, fx, fy)
        return previous[1], previous[2]


def _pop(d: D, x: float, y: float, start: float, draw, duration: float = 0.4) -> None:
    amount = appear(d.t, start, duration)
    if amount <= 0:
        return
    ctx = d.ctx
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, max(amount, 1e-3), max(amount, 1e-3))
    draw()
    ctx.restore()


# =============================================================================== characters and props
def c_rose(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 300), a.get("y", 960)))
    enter = a.get("enter")
    if enter:
        k = ease_out(progress(d.t, t0, 0.9))
        x = lerp(-250 if enter == "left" else W + 250, x, k)
    talk = d.sc.speaking(ROSE, d.t, FPS)
    mood = d.keyed(a.get("moods"), "happy")
    draw_rose(d.ctx, x, y, a.get("s", 1.0), d.gt, mood="talk" if talk > 0.05 else mood, talk=talk,
              wave=d.within(a.get("wave")), point=d.within(a.get("point")),
              look=float(d.keyed(a.get("look"), 0.2)), hand_on_chin=d.within(a.get("chin")))
    if a.get("label"):
        P.chip(d.ctx, x, y + 70 * a.get("s", 1.0), a.get("label"), d.t, t0 + 0.3, color=C["white"], size=34)


def c_aiden(d: D, a: A, t0: float) -> None:
    """Aiden, the junior host: the same poses and options as Rose."""
    x, y = d.path(a.get("path"), (a.get("x", 300), a.get("y", 960)))
    enter = a.get("enter")
    if enter:
        k = ease_out(progress(d.t, t0, 0.9))
        x = lerp(-250 if enter == "left" else W + 250, x, k)
    talk = d.sc.speaking(AIDEN, d.t, FPS)
    mood = d.keyed(a.get("moods"), "happy")
    draw_aiden(d.ctx, x, y, a.get("s", 1.0), d.gt, mood="talk" if talk > 0.05 else mood, talk=talk,
               wave=d.within(a.get("wave")), point=d.within(a.get("point")),
               look=float(d.keyed(a.get("look"), 0.2)), hand_on_chin=d.within(a.get("chin")))
    if a.get("label"):
        P.chip(d.ctx, x, y + 70 * a.get("s", 1.0), a.get("label"), d.t, t0 + 0.3, color=C["white"], size=34)


def c_pixi(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 700), a.get("y", 820)))
    if a.get("drop", False):
        y = lerp(-280, y, ease_out(progress(d.t, t0, 0.7)))
    speaking = any(b.speaker == PIXI and b.start <= d.sc.start + d.t < b.end for b in d.sc.beats)
    beep = 1.0 if speaking or d.within(a.get("beep")) > 0.5 else 0.0
    draw_pixi(d.ctx, x, y, a.get("s", 0.9), d.gt, mood=d.keyed(a.get("moods"), "happy"),
               carrying=d.within(a.get("carrying")) > 0.5, beep=beep,
               ground=a.get("ground", y + 40 * a.get("s", 0.9) / 0.9 + 100 * a.get("s", 0.9)))
    if a.get("label"):
        P.chip(d.ctx, x, a.get("ground", y + 160) + 60, a.get("label"), d.t, t0 + 0.3, color=C["white"], size=34)


def c_cat(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 1500), a.get("y", 960)))
    draw_cat(d.ctx, x, y, a.get("s", 0.9) * appear(d.t, t0, 0.4), d.gt, talking=d.within(a.get("talk")) > 0.5)


def c_grownup(d: D, a: A, t0: float) -> None:
    draw_grown_up(d.ctx, a.get("x", 1500), a.get("y", 960), a.get("s", 0.8) * appear(d.t, t0), d.gt)


def c_key(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 960), a.get("y", 540)))
    P.key(d.ctx, x, y, a.get("s", 1.0) * appear(d.t, t0), d.gt, glowing=a.get("glow", True))


def c_door(d: D, a: A, t0: float) -> None:
    opened = ease_out(progress(d.t, d.T(a.get("open")), 1.0)) if a.get("open") is not None else 0.0
    P.door(d.ctx, a.get("x", 1520), a.get("y", 900), a.get("w", 230), a.get("h", 400), d.gt, opened=opened,
           locked=a.get("locked", True) and opened < 0.2, label=a.text or "DOOR")


def c_chair(d: D, a: A, t0: float) -> None:
    P.chair(d.ctx, a.get("x", 980), a.get("y", 900), a.get("s", 1.0))


def c_laptop(d: D, a: A, t0: float) -> None:
    def draw():
        ctx = d.ctx
        fill_rounded(ctx, -170, -150, 340, 220, 20, C["navy"])
        fill_rounded(ctx, -150, -130, 300, 180, 12, C["sky_light"])
        for i in range(3):
            line(ctx, -110, -90 + i * 40, 60 - i * 30, -90 + i * 40, C["blue"], 12)
        fill_rounded(ctx, -220, 70, 440, 34, 14, C["gray"])
    d.ctx.save()
    d.ctx.translate(a.get("x", 960), a.get("y", 540))
    safe_scale(d.ctx, a.get("s", 1.0), a.get("s", 1.0))
    _pop(d, 0, 0, t0, draw)
    d.ctx.restore()


def c_pointer(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 960), a.get("y", 540)))
    P.pointer_hand(d.ctx, x, y, a.get("s", 1.0) * appear(d.t, t0, 0.3))


def c_magnifier(d: D, a: A, t0: float) -> None:
    x, y = d.path(a.get("path"), (a.get("x", 960), a.get("y", 540)))
    P.magnifier(d.ctx, x, y, a.get("s", 0.8) * appear(d.t, t0, 0.3), d.gt)


# =============================================================================== text and callouts
def c_banner(d: D, a: A, t0: float) -> None:
    P.title_banner(d.ctx, a.text, d.t, t0, y=a.get("y", 96), size=a.get("size", 56),
                   color=STRONG.get(a.get("color") or "navy", a.get("color") or C["navy"]))


def c_chip(d: D, a: A, t0: float) -> None:
    fill = color(a.get("color"))
    P.chip(d.ctx, a.get("x", W / 2), a.get("y", 200), a.text, d.t, t0, color=fill, ink=INK.get(a.get("color"), C["navy"]),
           size=a.get("size", 42))


def c_bigtext(d: D, a: A, t0: float) -> None:
    def draw():
        tw, th = text_size(a.text, a.get("size", 64), bold=True)
        fill_rounded(d.ctx, -tw / 2 - 50, -th / 2 - 22, tw + 100, th + 44, (th + 44) / 2,
                     STRONG.get(a.get("color") or "red", a.get("color") or C["vermillion"]))
        text(d.ctx, a.text, 0, 0, a.get("size", 64), C["white"], bold=True)
    _pop(d, a.get("x", W / 2), a.get("y", 960), t0, draw, 0.5)


def c_bubble(d: D, a: A, t0: float) -> None:
    t1 = d.T(a.until)
    anchors = {"rose": (a.get("x", 300) + 70, a.get("y", 960) - ROSE_HEAD_TOP),
               "aiden": (a.get("x", 300) + 70, a.get("y", 960) - AIDEN_HEAD_TOP * a.get("s", 1.0)), "pixi": (a.get("x", 700), a.get("y", 820) - 250),
               "cat": (a.get("x", 1500) + 20, a.get("y", 960) - 230)}
    x, y = anchors.get(a.get("who"), (a.get("x", 960), a.get("y", 500)))
    P.speech_bubble(d.ctx, x, y, a.text, d.t, t0, t1 - 0.25, size=a.get("size", 38), tail=a.get("tail", "down-left"),
                    max_width=a.get("max_width", 520))


def c_thought(d: D, a: A, t0: float) -> None:
    P.thought_bubble(d.ctx, a.get("x", 960), a.get("y", 300), d.t, t0, d.T(a.until) - 0.1, label=a.text)


def c_panel(d: D, a: A, t0: float) -> None:
    """A titled card with bullet lines that appear at their own times: items=[(time, text), ...]."""
    x, y, w = a.get("x", 1100), a.get("y", 260), a.get("w", 700)
    items = a.get("items", [])
    size = a.get("size", 38)
    line_h = size * 1.7
    h = 110 + line_h * len(items) if a.text else 40 + line_h * len(items)

    def draw():
        fill_rounded(d.ctx, 6, 8, w, h, 30, "#000000", 0.10)
        fill_rounded(d.ctx, 0, 0, w, h, 30, C["white"], stroke=color(a.get("color"), "navy"), width=5)
        top = 30
        if a.text:
            text(d.ctx, a.text, 40, 55, 42, C["navy"], bold=True, anchor="left")
            top = 100
        for i, item in enumerate(items):
            when, label = item if isinstance(item, (list, tuple)) else ("start", item)
            k = appear(d.t, d.T(when), 0.35)
            if k > 0:
                cy = top + i * line_h + line_h / 2
                circle(d.ctx, 50, cy, 9 * k, color(a.get("color"), "navy") if a.get("color") not in (None, "sky") else C["navy"])
                text(d.ctx, label, 80, cy, size, C["ink"], bold=True, anchor="left", alpha=k, max_width=w - 110, align="left")
    d.ctx.save()
    d.ctx.translate(x, y)
    k = appear(d.t, t0, 0.4)
    d.ctx.translate(w / 2, h / 2)
    safe_scale(d.ctx, max(k, 1e-3), max(k, 1e-3))
    d.ctx.translate(-w / 2, -h / 2)
    if k > 0:
        draw()
    d.ctx.restore()


def c_cards(d: D, a: A, t0: float) -> None:
    """Numbered step cards: items=[...], reveal=[time per item], active=[window per item], done=[time per item]."""
    items = a.get("items", [])
    x, y, w = a.get("x", 1040), a.get("y", 300), a.get("w", 720)
    gap = a.get("gap", 112)
    reveal = a.get("reveal") or [a.at] * len(items)
    active = a.get("active") or [None] * len(items)
    done = a.get("done") or [None] * len(items)
    order = list(range(len(items)))
    new_order, move = None, 0.0
    if a.get("reorder"):
        when, new_order = a.get("reorder")
        move = ease_in_out(progress(d.t, d.T(when), 0.7))
    for i in order:
        slot = i
        if new_order is not None:
            slot = lerp(i, new_order.index(i), move)
        cy = y + slot * gap
        is_done = done[i] is not None and d.t >= d.T(done[i])
        P.step_card(d.ctx, x, cy, w, a.get("numbers", list(range(1, len(items) + 1)))[i], items[i], d.t, d.T(reveal[i]),
                    active=d.within(active[i]) if active[i] is not None else 0.0, done=is_done,
                    color=color(a.get("color"), C["blue"]) if a.get("color") else C["blue"], size=a.get("size", 38))


ICONS = {}


def _icon(name):
    def register(fn):
        ICONS[name] = fn
        return fn
    return register


@_icon("lock")
def _i_lock(ctx):
    P._padlock(ctx, 0, 0, 2.0)


@_icon("check")
def _i_check(ctx):
    circle(ctx, 0, 0, 50, C["green"])
    check_mark(ctx, 0, 0, 70)


@_icon("cross")
def _i_cross(ctx):
    circle(ctx, 0, 0, 50, C["vermillion"])
    cross_mark(ctx, 0, 0, 70)


@_icon("star")
def _i_star(ctx):
    star(ctx, 0, 0, 52, C["yellow"])


@_icon("heart")
def _i_heart(ctx):
    ctx.move_to(0, 40)
    ctx.curve_to(-70, -10, -40, -60, 0, -25)
    ctx.curve_to(40, -60, 70, -10, 0, 40)
    set_color(ctx, C["pink"])
    ctx.fill()


@_icon("person")
def _i_person(ctx):
    circle(ctx, 0, -28, 22, C["gray"])
    fill_rounded(ctx, -32, 0, 64, 52, 24, C["gray"])


@_icon("laptop")
def _i_laptop(ctx):
    fill_rounded(ctx, -50, -40, 100, 64, 8, C["navy"])
    fill_rounded(ctx, -42, -32, 84, 48, 5, C["sky_light"])
    fill_rounded(ctx, -64, 24, 128, 14, 6, C["gray"])


@_icon("wifi_off")
def _i_wifi_off(ctx):
    for r in (20, 38, 56):
        ctx.arc(0, 30, r, math.pi * 1.25, math.pi * 1.75)
        set_color(ctx, C["gray"])
        ctx.set_line_width(9)
        ctx.stroke()
    line(ctx, -50, -30, 50, 40, C["vermillion"], 10)


@_icon("file")
def _i_file(ctx):
    fill_rounded(ctx, -40, -52, 80, 104, 10, C["white"], stroke=C["navy"], width=5)
    for i in range(4):
        line(ctx, -24, -28 + i * 18, 24, -28 + i * 18, C["gray"], 5)


@_icon("camera")
def _i_camera(ctx):
    fill_rounded(ctx, -55, -30, 110, 70, 14, C["navy"])
    circle(ctx, 0, 5, 22, C["sky_light"])
    fill_rounded(ctx, -20, -44, 40, 18, 6, C["navy"])


@_icon("gear")
def _i_gear(ctx):
    P._gear(ctx, 0, 0, 34, 0.0, C["orange"])


@_icon("clock")
def _i_clock(ctx):
    circle(ctx, 0, 0, 48, C["white"], stroke=C["navy"], width=6)
    line(ctx, 0, 0, 0, -30, C["navy"], 6)
    line(ctx, 0, 0, 22, 8, C["navy"], 6)


@_icon("trophy")
def _i_trophy(ctx):
    fill_rounded(ctx, -34, -46, 68, 56, 20, C["gold"])
    fill_rounded(ctx, -8, 8, 16, 26, 4, C["gold"])
    fill_rounded(ctx, -30, 32, 60, 14, 5, C["wood"])


@_icon("magnifier")
def _i_magnifier(ctx):
    P.magnifier(ctx, -8, -8, 0.45, 0.0)


@_icon("warning")
def _i_warning(ctx):
    ctx.move_to(0, -50)
    ctx.line_to(52, 40)
    ctx.line_to(-52, 40)
    ctx.close_path()
    set_color(ctx, C["yellow"])
    ctx.fill()
    text(ctx, "!", 0, 10, 56, C["ink"], bold=True)


@_icon("grownup")
def _i_grownup(ctx):
    draw_grown_up(ctx, 0, 55, 0.42, 0.0)


@_icon("house")
def _i_house(ctx):
    ctx.move_to(-50, -5)
    ctx.line_to(0, -50)
    ctx.line_to(50, -5)
    ctx.close_path()
    set_color(ctx, C["vermillion"])
    ctx.fill()
    fill_rounded(ctx, -38, -6, 76, 54, 6, C["orange_light"])


@_icon("book")
def _i_book(ctx):
    fill_rounded(ctx, -50, -38, 100, 76, 10, C["blue"])
    line(ctx, 0, -38, 0, 38, C["white"], 5)


@_icon("key")
def _i_key(ctx):
    P.key(ctx, 6, 0, 0.9, 0.0, glowing=False)


@_icon("game")
def _i_game(ctx):
    fill_rounded(ctx, -60, -32, 120, 64, 30, C["purple"])
    circle(ctx, -28, 0, 9, C["white"])
    circle(ctx, 30, -8, 7, C["yellow"])
    circle(ctx, 30, 10, 7, C["green"])


@_icon("music")
def _i_music(ctx):
    line(ctx, 10, -40, 10, 28, C["navy"], 7)
    ellipse(ctx, -4, 30, 18, 13, C["navy"])
    line(ctx, 10, -40, 38, -30, C["navy"], 7)


def c_icons(d: D, a: A, t0: float) -> None:
    """A row of labeled icons: items=[(icon, label, time?), ...]; crossed=[indexes] draws a strike."""
    items = a.get("items", [])
    x, y, gap = a.get("x", W / 2), a.get("y", 540), a.get("gap", 250)
    left = x - gap * (len(items) - 1) / 2
    for i, item in enumerate(items):
        name, label = item[0], item[1]
        when = item[2] if len(item) > 2 else t0
        cx = left + i * gap
        start = d.T(when)
        k = appear(d.t, start, 0.4)
        if k <= 0:
            continue
        ctx = d.ctx
        ctx.save()
        ctx.translate(cx, y)
        safe_scale(ctx, max(k, 1e-3), max(k, 1e-3))
        circle(ctx, 0, 0, 78, C["white"], stroke=C["navy"], width=4)
        ICONS.get(name, _i_star)(ctx)
        ctx.restore()
        text(ctx, label, cx, y + 118, a.get("size", 34), C["ink"], bold=True, alpha=k, max_width=gap - 20)
        if i in a.get("crossed", []) and d.t > start + 0.35:
            amount = ease_out(progress(d.t, start + 0.35, 0.25))
            line(ctx, cx - 70, y - 70, cx - 70 + 140 * amount, y - 70 + 140 * amount, C["vermillion"], 12)


def c_arrow(d: D, a: A, t0: float) -> None:
    x1, y1, x2, y2 = a.get("x1", 800), a.get("y1", 540), a.get("x2", 1100), a.get("y2", 540)
    k = ease_out(progress(d.t, t0, a.get("duration", 0.6)))
    if k <= 0:
        return
    ex, ey = lerp(x1, x2, k), lerp(y1, y2, k)
    col = color(a.get("color"), C["vermillion"])
    line(d.ctx, x1, y1, ex, ey, col, a.get("width", 12))
    if k > 0.9:
        angle = math.atan2(y2 - y1, x2 - x1)
        ctx = d.ctx
        ctx.move_to(x2 + 8 * math.cos(angle), y2 + 8 * math.sin(angle))
        ctx.line_to(x2 - 34 * math.cos(angle - 0.5), y2 - 34 * math.sin(angle - 0.5))
        ctx.line_to(x2 - 34 * math.cos(angle + 0.5), y2 - 34 * math.sin(angle + 0.5))
        ctx.close_path()
        set_color(ctx, col)
        ctx.fill()
    if a.text:
        angle = math.atan2(y2 - y1, x2 - x1)
        offset = 44 + text_size(a.text, a.get("size", 32), bold=True)[0] / 2 * abs(math.sin(angle))
        nx, ny = math.sin(angle), -math.cos(angle)  # a normal to the arrow
        if ny > 0 or (abs(ny) < 1e-6 and nx < 0):  # always label on the upper (or right) side
            nx, ny = -nx, -ny
        lx = (x1 + x2) / 2 + offset * nx
        ly = (y1 + y2) / 2 + offset * ny
        text(d.ctx, a.text, lx, ly, a.get("size", 32), col if col != C["white"] else C["ink"], bold=True, alpha=k)


# =============================================================================== Scratch blocks and stage
EXTRA_BLOCK_COLORS = {"control": ("#FFAB19", "#CF8B17"), "sensing": ("#5CB1D6", "#2E8EB8"),
                      "operators": ("#59C059", "#389438"), "variables": ("#FF8C1A", "#DB6E00"),
                      "pen": ("#0FBD8C", "#0B8E69"), "myblocks": ("#FF6680", "#FF3355")}
P.BLOCK_COLORS.update(EXTRA_BLOCK_COLORS)
_PART = re.compile(r"(\[[^\]]*\]|<[^>]*>|\{flag\})")


def _parts(text_value: str) -> list[str]:
    parts = []
    for chunk in _PART.split(text_value):
        if not chunk.strip():
            continue
        if _PART.fullmatch(chunk):
            parts.append(chunk if not chunk.startswith("<") else "[" + chunk[1:-1] + "]")
        else:
            parts.extend(chunk.split())
    return parts


def _block_height(entry) -> float:
    kind, label = entry[0], entry[1]
    if kind == "control" and len(entry) >= 3:
        inner = sum(_block_height(e) for e in entry[2]) or 60
        extra = 0
        if len(entry) >= 4:
            extra = 56 + (sum(_block_height(e) for e in entry[3]) or 60)
        return 76 + inner + 46 + extra
    return 76


def _draw_stack(d: D, entries, x, y, scale, reveal_times, highlight, index_offset=0, offsets=None) -> int:
    """Draw blocks top to bottom; returns how many blocks were drawn (for numbering)."""
    ctx = d.ctx
    index = index_offset
    cursor = y
    for entry in entries:
        kind, label = entry[0], entry[1]
        start = reveal_times[index] if index < len(reveal_times) else reveal_times[-1]
        fly = ease_out(progress(d.t, start, 0.5))
        dy = offsets.get(index, 0.0) if offsets else 0.0
        hl = 0.0
        for item in highlight:
            hi, frm, to = item
            if hi == index and d.T(frm) <= d.t < d.T(to):
                hl = 1.0
        if d.t >= start:
            bx = lerp(x - 300, x, fly)
            alpha_y = cursor + dy
            if kind == "control" and len(entry) >= 3:
                inner_h = sum(_block_height(e) for e in entry[2]) or 60
                else_h = (sum(_block_height(e) for e in entry[3]) or 60) if len(entry) >= 4 else 0
                fill, edge = P.BLOCK_COLORS["control"]
                label_w = sum(text_size(part.strip("[]"), 34, bold=True)[0] + (50 if part.startswith("[") else 6)
                              for part in _parts(label))
                total_w = max(520, label_w + 60)
                ctx.save()
                ctx.translate(bx, alpha_y)
                safe_scale(ctx, scale, scale)
                if hl:
                    fill_rounded(ctx, -12, -14, total_w + 24, _block_height(entry) + 28, 22, C["yellow"], 0.45)
                fill_rounded(ctx, 0, 0, total_w, 76, 12, fill, stroke=edge, width=3)
                fill_rounded(ctx, 0, 60, 40, inner_h + 30, 0, fill)
                arm_y = 76 + inner_h
                if len(entry) >= 4:
                    fill_rounded(ctx, 0, arm_y, total_w * 0.6, 56, 10, fill, stroke=edge, width=3)
                    text(ctx, "else", 24, arm_y + 28, 34, C["white"], bold=True, anchor="left")
                    fill_rounded(ctx, 0, arm_y + 40, 40, else_h + 30, 0, fill)
                    arm_y += 56 + else_h
                fill_rounded(ctx, 0, arm_y, total_w * 0.6, 46, 10, fill, stroke=edge, width=3)
                cx = 24
                for part in _parts(label):
                    if part.startswith("["):
                        tw, _ = text_size(part[1:-1], 32, bold=True)
                        fill_rounded(ctx, cx, 14, tw + 36, 48, 24, C["white"])
                        text(ctx, part[1:-1], cx + (tw + 36) / 2, 38, 30, "#575E75", bold=True)
                        cx += tw + 50
                    else:
                        text(ctx, part, cx, 38, 34, C["white"], bold=True, anchor="left")
                        cx += text_size(part, 34, bold=True)[0] + 6
                ctx.restore()
                index = _draw_stack(d, entry[2], x + 40 * scale, alpha_y + 76 * scale, scale, reveal_times, highlight,
                                    index + 1, offsets)
                if len(entry) >= 4:
                    index = _draw_stack(d, entry[3], x + 40 * scale, alpha_y + (76 + inner_h + 56) * scale, scale,
                                        reveal_times, highlight, index, offsets)
            else:
                P.code_block(ctx, bx, alpha_y, kind, _parts(label), highlight=hl,
                             hat=kind == "event" and label.lower().startswith("when") and entry is entries[0] and index_offset == 0,
                             scale=scale)
                index += 1
        else:
            index += 1 + (_count(entry[2]) + (_count(entry[3]) if len(entry) >= 4 else 0) if kind == "control" and len(entry) >= 3 else 0)
        cursor += _block_height(entry) * scale
    return index


def _apply_edits(entries, edits):
    """Replace the text of blocks (flat drawing-order index) for edits that have happened."""
    counter = [0]
    table = dict(edits)

    def walk(items):
        out = []
        for entry in items:
            index = counter[0]
            counter[0] += 1
            label = table.get(index, entry[1])
            if entry[0] == "control" and len(entry) >= 3:
                inner = walk(entry[2])
                rest = (walk(entry[3]),) if len(entry) >= 4 else ()
                out.append((entry[0], label, inner, *rest))
            else:
                out.append((entry[0], label))
        return out

    return walk(entries)


def _count(entries) -> int:
    return sum(1 + (_count(e[2]) + (_count(e[3]) if len(e) >= 4 else 0) if e[0] == "control" and len(e) >= 3 else 0)
               for e in entries)


def c_scratch(d: D, a: A, t0: float) -> None:
    """A block stack: blocks=[(kind, text), ("control", "repeat [4]", [inner...]), ...].

    reveal: one time per block in drawing order (default: all at `at`); highlight: [(index, from, to)];
    swap: (time, i, j) swaps two top-level blocks; edits: [(time, index, "new text")] changes a block.
    """
    blocks = a.get("blocks", [])
    edits = [(d.T(when), index, new) for when, index, new in a.get("edits", [])]
    if edits:
        blocks = _apply_edits(blocks, [(index, new) for when, index, new in edits if d.t >= when])
    total = _count(blocks)
    reveal = [d.T(r) for r in (a.get("reveal") or [a.at] * total)]
    if len(reveal) < total:
        reveal += [reveal[-1]] * (total - len(reveal))
    entries = list(blocks)
    offsets = {}
    if a.get("swap"):
        when, i, j = a.get("swap")
        k = ease_in_out(progress(d.t, d.T(when), 0.8))
        hi, hj = _block_height(entries[i]) * a.get("scale", 0.9), _block_height(entries[j]) * a.get("scale", 0.9)
        if k >= 1:
            entries[i], entries[j] = entries[j], entries[i]
        else:
            offsets = {i: k * hj if i < j else -k * hj, j: -k * hi if i < j else k * hi}
    if a.get("panel", True):
        fill_rounded(d.ctx, a.get("x", 200) - 40, a.get("y", 300) - 70, a.get("w", 760), a.get("h", 520), 26,
                     C["white"], stroke=C["navy"], width=4)
        if a.text:
            text(d.ctx, a.text, a.get("x", 200) - 10, a.get("y", 300) - 36, 32, C["navy"], bold=True, anchor="left")
    _draw_stack(d, entries, a.get("x", 200), a.get("y", 300) + (20 if a.text else 0), a.get("scale", 0.9), reveal,
                a.get("highlight", []), 0, offsets)


SPRITES = {}


def _sprite(name):
    def register(fn):
        SPRITES[name] = fn
        return fn
    return register


@_sprite("banana")
def _s_banana(ctx, x, y, s, gt, talking):
    """A banana (Mei's Banana Drop game in Junior Level 2)."""
    ctx.save()
    ctx.translate(x, y - 45 * s)
    safe_scale(ctx, s, s)
    ctx.move_to(-58, -26)
    ctx.curve_to(-46, 38, 46, 38, 58, -26)
    ctx.curve_to(30, 8, -30, 8, -58, -26)
    ctx.close_path()
    set_color(ctx, "#F7D038")
    ctx.fill_preserve()
    set_color(ctx, "#B88A12")
    ctx.set_line_width(4)
    ctx.stroke()
    ctx.rectangle(54, -38, 10, 16)
    set_color(ctx, "#7A5A1E")
    ctx.fill()
    ctx.restore()


@_sprite("cat")
def _s_cat(ctx, x, y, s, gt, talking):
    draw_cat(ctx, x, y, s, gt, talking=talking)


@_sprite("pixi")
def _s_pixi(ctx, x, y, s, gt, talking):
    draw_pixi(ctx, x, y - 40 * s, s * 0.7, gt, mood="happy", beep=1.0 if talking else 0.0, ground=y)


@_sprite("ghost")
def _s_ghost(ctx, x, y, s, gt, talking):
    ctx.save()
    ctx.translate(x, y - 20 + 6 * math.sin(gt * 3))
    safe_scale(ctx, s, s)
    ctx.move_to(-60, 0)
    ctx.line_to(-60, -110)
    ctx.arc(0, -110, 60, math.pi, 0)
    ctx.line_to(60, 0)
    for i in range(4):
        ctx.line_to(60 - 30 * (i + 0.5), -18)
        ctx.line_to(60 - 30 * (i + 1), 0)
    set_color(ctx, C["white"])
    ctx.fill_preserve()
    set_color(ctx, C["navy"])
    ctx.set_line_width(4)
    ctx.stroke()
    circle(ctx, -20, -110, 9, C["ink"])
    circle(ctx, 20, -110, 9, C["ink"])
    ellipse(ctx, 0, -84, 10, 7 + (4 if talking else 0), C["ink"])
    ctx.restore()


@_sprite("apple")
def _s_apple(ctx, x, y, s, gt, talking):
    circle(ctx, x, y - 40 * s, 40 * s, "#E8443A")
    line(ctx, x, y - 80 * s, x + 8 * s, y - 100 * s, C["wood_dark"], 6 * s)
    ellipse(ctx, x + 22 * s, y - 92 * s, 16 * s, 8 * s, C["green"])


@_sprite("bowl")
def _s_bowl(ctx, x, y, s, gt, talking):
    ctx.move_to(x - 90 * s, y - 60 * s)
    ctx.curve_to(x - 80 * s, y + 10 * s, x + 80 * s, y + 10 * s, x + 90 * s, y - 60 * s)
    ctx.close_path()
    set_color(ctx, C["blue"])
    ctx.fill()


@_sprite("star")
def _s_star(ctx, x, y, s, gt, talking):
    star(ctx, x, y - 50 * s, 50 * s, C["yellow"], rotation=gt * 0.5)


@_sprite("balloon")
def _s_balloon(ctx, x, y, s, gt, talking):
    line(ctx, x, y - 60 * s, x, y + 20 * s, C["gray"], 3)
    ellipse(ctx, x, y - 110 * s, 48 * s, 60 * s, "#E8443A")


def c_stage(d: D, a: A, t0: float) -> None:
    """A Scratch-style stage. actions=[(time, "say", text, seconds) | (time, "move", dx, seconds) |
    (time, "goto", x, y, seconds) | (time, "draw", sides, length, seconds[, turn]) | (time, "clear") |
    (time, "turn", degrees, seconds) | (time, "hide") | (time, "show")]; monitors=[(name, [(time, value), ...])]; sprite="cat" (or pixi, ghost,
    apple, bowl, star, balloon); extra=[(sprite, x, y)] for other sprites (stage coordinates).
    """
    x, y, w, h = a.get("x", 1180), a.get("y", 260), a.get("w", 620), a.get("h", 460)
    ctx = d.ctx
    k = appear(d.t, t0, 0.4)
    if k <= 0:
        return
    fill_rounded(ctx, x - 10, y - 10, w + 20, h + 20, 24, C["gray_light"])
    vertical_gradient(ctx, x, y, w, h, a.get("sky", "#DFF3FF"), "#FFFFFF")
    ctx.rectangle(x, y + h - 60, w, 60)
    set_color(ctx, "#BFE3B4")
    ctx.fill()
    if a.get("flag", True):
        flag_t = a.get("flag_at")
        pressed = 1.0 if flag_t is not None and d.T(flag_t) <= d.t < d.T(flag_t) + 0.25 else 0.0
        P.green_flag_button(ctx, x + 40, y - 52, 30, pressed)
    # sprite state from actions
    sx, sy = a.get("sprite_x", 0.0), a.get("sprite_y", 0.0)  # stage coords: (0, 0) is the middle
    heading = 90.0
    visible = True
    pen_points = []
    bubble = None
    for act in a.get("actions", []):
        when, verb = d.T(act[0]), act[1]
        if d.t < when:
            continue
        if verb == "say":
            seconds = act[3] if len(act) > 3 else 2.0
            if d.t < when + seconds:
                bubble = (act[2], when, when + seconds)
        elif verb == "move":
            seconds = act[3] if len(act) > 3 else 0.6
            k2 = ease_in_out(progress(d.t, when, seconds))
            sx += act[2] * k2 * math.sin(math.radians(heading))
            sy += act[2] * k2 * math.cos(math.radians(heading))
        elif verb == "turn":
            seconds = act[3] if len(act) > 3 else 0.4
            heading += act[2] * ease_in_out(progress(d.t, when, seconds))
        elif verb == "goto":
            seconds = act[4] if len(act) > 4 else 0.6
            k2 = ease_in_out(progress(d.t, when, seconds))
            sx, sy = lerp(sx, act[2], k2), lerp(sy, act[3], k2)
        elif verb == "clear":
            pen_points = []
        elif verb == "draw":
            sides, length = act[2], act[3]
            seconds = act[4] if len(act) > 4 else 2.0
            turn = act[5] if len(act) > 5 else 360 / sides
            total = sides * length
            done = total * progress(d.t, when, seconds)
            px, py, hd = sx, sy, 0.0
            pts = [(px, py)]
            for _ in range(sides):
                seg = min(length, done)
                if seg <= 0:
                    break
                px += seg * math.cos(math.radians(hd))
                py += seg * math.sin(math.radians(hd))
                pts.append((px, py))
                done -= seg
                if seg < length:
                    break
                hd += turn
            pen_points.append(pts)
            sx, sy = px, py
        elif verb == "hide":
            visible = False
        elif verb == "show":
            visible = True
    scale = w / 480
    def to_screen(px, py):
        return x + w / 2 + px * scale, y + h / 2 - py * scale
    for pts in pen_points:
        if len(pts) > 1:
            ctx.move_to(*to_screen(*pts[0]))
            for p in pts[1:]:
                ctx.line_to(*to_screen(*p))
            set_color(ctx, a.get("pen", C["blue"]))
            ctx.set_line_width(6)
            ctx.stroke()
    for extra in a.get("extra", []):
        ex, ey = to_screen(extra[1], extra[2])
        SPRITES.get(extra[0], _s_star)(ctx, ex, ey + 40, a.get("sprite_scale", 0.6) * 0.8, d.gt, False)
    cx, cy = to_screen(sx, sy)
    if visible:
        SPRITES.get(a.get("sprite", "cat"), _s_cat)(ctx, cx, cy + 50, a.get("sprite_scale", 0.6), d.gt, bubble is not None)
    if bubble:
        P.speech_bubble(ctx, min(cx + 30, x + w - 60), cy - 90, bubble[0], d.t, bubble[1], bubble[2] - 0.15, size=30,
                        max_width=320, tail="down")
    for i, (name, values) in enumerate(a.get("monitors", [])):
        value = d.keyed(values, "")
        fill_rounded(ctx, x + 16, y + 16 + i * 52, 200, 44, 10, C["white"], stroke=C["gray"], width=2)
        text(ctx, name, x + 30, y + 38 + i * 52, 26, C["ink"], bold=True, anchor="left")
        fill_rounded(ctx, x + 130, y + 24 + i * 52, 72, 28, 14, "#FF8C1A")
        text(ctx, str(value), x + 166, y + 38 + i * 52, 22, C["white"], bold=True)


# =============================================================================== Python code (runs for real)
KEYWORDS = {"def", "return", "for", "in", "if", "elif", "else", "while", "import", "from", "class", "True", "False",
            "None", "and", "or", "not", "break", "continue", "with", "as", "try", "except", "pass", "lambda", "is",
            "global", "yield", "assert", "finally", "raise", "del"}
BUILTINS = {"print", "input", "int", "str", "float", "len", "range", "open", "sorted", "list", "dict", "set", "sum",
            "min", "max", "abs", "round", "enumerate", "type", "bool", "super", "isinstance", "zip", "reversed"}
TOKEN_RE = re.compile(r"(#.*$)|(\"[^\"]*\"?|'[^']*'?)|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|(.)")
SYNTAX = {"comment": "#8A97A6", "string": "#2E8B57", "number": "#B35C00", "keyword": "#7B3FC6",
          "builtin": "#1F6FD1", "name": "#1B2A3A", "punct": "#1B2A3A", "self": "#C2185B"}


def tokens(source_line: str) -> list[tuple[str, str]]:
    result = []
    for match in TOKEN_RE.finditer(source_line):
        comment, string, number, name, space, other = match.groups()
        if comment:
            result.append((comment, "comment"))
        elif string:
            result.append((string, "string"))
        elif number:
            result.append((number, "number"))
        elif name:
            kind = ("keyword" if name in KEYWORDS else "builtin" if name in BUILTINS else
                    "self" if name == "self" else "name")
            result.append((name, kind))
        elif space:
            result.append((space, "space"))
        else:
            result.append((other, "punct"))
    return result


def _code_lines(a: A) -> list[str]:
    return a.get("code", a.text).strip("\n").split("\n")


@functools.lru_cache(maxsize=256)
def _run_cached(code: str, inputs: tuple, seed: int) -> dict:
    return pyrun.run(code, inputs, seed)


def code_result(a: A) -> dict:
    lines = _code_lines(a)
    program = a.get("exec", "\n".join(lines))
    return _run_cached(program, tuple(a.get("inputs", ())), a.get("seed", 1))


def c_code(d: D, a: A, t0: float) -> None:
    """A Thonny-style editor (and Shell) showing real code: code="...", title="main.py".

    type: (from, to) types the code character by character (default: shown at `at`);
    reveal: one time per line instead; highlight: [(line_number, from, to)]; run: time when Run is
    pressed (Shell shows the true output; inputs=[...] answers input()); error_line: line number to
    underline when the run raises an error; traceback=True shows the whole traceback (file, line number,
    source line, error) as Thonny does; shell=False hides the Shell. expect=[...] lists the Shell
    lines the episode relies on (tests check them against the real run).
    """
    ctx = d.ctx
    x, y, w, h = a.get("x", 120), a.get("y", 180), a.get("w", 1000), a.get("h", 720)
    size = a.get("size", 34)
    lines = _code_lines(a)
    k = appear(d.t, t0, 0.4)
    if k <= 0:
        return
    show_shell = a.get("shell", a.get("run") is not None)
    shell_h = a.get("shell_h", 230) if show_shell else 0
    fill_rounded(ctx, x + 8, y + 12, w, h, 26, "#000000", 0.12)
    fill_rounded(ctx, x, y, w, h, 26, C["white"], stroke=C["navy"], width=4)
    fill_rounded(ctx, x, y, w, 64, 26, C["navy"])
    ctx.rectangle(x, y + 40, w, 24)
    set_color(ctx, C["navy"])
    ctx.fill()
    text(ctx, f"Thonny  •  {a.get('title', 'main.py')}", x + 28, y + 33, 28, C["white"], bold=True, anchor="left")
    run_t = d.T(a.get("run")) if a.get("run") is not None else None
    # Run button
    pressed = run_t is not None and run_t <= d.t < run_t + 0.3
    circle(ctx, x + w - 60, y + 32, 22 - 3 * pressed, "#4CAF50")
    ctx.move_to(x + w - 68, y + 20)
    ctx.line_to(x + w - 48, y + 32)
    ctx.line_to(x + w - 68, y + 44)
    ctx.close_path()
    set_color(ctx, C["white"])
    ctx.fill()
    # editor
    line_h = size * 1.45
    top = y + 90
    cw = mono_width(size)
    typed_chars = None
    if a.get("type"):
        frm, to = a.get("type")
        total = sum(len(ln) + 1 for ln in lines)
        typed_chars = int(total * progress(d.t, d.T(frm), max(0.1, d.T(to) - d.T(frm))))
    reveal = a.get("reveal")
    used = 0
    for number, source in enumerate(lines, start=1):
        ly = top + (number - 1) * line_h
        if ly + line_h > y + h - shell_h - 10:
            break
        visible_text = source
        if reveal is not None:
            if number - 1 < len(reveal) and d.t < d.T(reveal[number - 1]):
                continue
        if typed_chars is not None:
            remaining = typed_chars - used
            used += len(source) + 1
            if remaining <= 0:
                break
            visible_text = source[: max(0, remaining)]
        for hl_line, frm, to in a.get("highlight", []):
            if hl_line == number and d.T(frm) <= d.t < d.T(to):
                fill_rounded(ctx, x + 70, ly - 4, w - 90, line_h, 10, C["yellow"], 0.45)
        text(ctx, str(number), x + 50, ly + line_h / 2, size - 8, C["gray"], mono=True)
        cx = x + 90
        for token_text, kind in tokens(visible_text):
            if kind != "space":
                text(ctx, token_text, cx, ly + line_h / 2, size, SYNTAX.get(kind, C["ink"]), anchor="left", mono=True,
                     bold=kind in ("keyword",))
            cx += cw * len(token_text)
        if typed_chars is not None and used >= typed_chars and (int(d.gt * 2) % 2 == 0):
            line(ctx, cx + 2, ly + 4, cx + 2, ly + line_h - 4, C["ink"], 3)
    # Shell
    if show_shell:
        sy = y + h - shell_h
        line(ctx, x, sy, x + w, sy, C["navy"], 3, cap=0)
        text(ctx, "Shell", x + 28, sy + 28, 26, C["gray"], bold=True, anchor="left")
        if run_t is not None and d.t >= run_t:
            result = code_result(a)
            output = pyrun.shell_lines(result, a.get("traceback", False))
            n_error = len(output) - len(result["stdout"].splitlines())
            shown = [">>> %Run " + a.get("title", "main.py")] + output
            error_from = len(shown) - n_error
            steps = int((d.t - run_t) / a.get("line_delay", 0.45)) + 1
            max_lines = int((shell_h - 50) / (size * 1.25))
            visible = shown[: steps]
            visible = visible[-max_lines:]
            first_visible = len(shown[: steps]) - len(visible)
            for i, out in enumerate(visible):
                is_error = bool(result["error"]) and first_visible + i >= error_from
                fit = int(min(size - 4, (w - 80) / (max(len(out), 1) * 0.62)))  # shrink long lines to fit
                text(ctx, out, x + 40, sy + 64 + i * size * 1.2, max(fit, 16),
                     C["vermillion"] if is_error else (C["gray"] if out.startswith(">>>") else C["ink"]),
                     anchor="left", mono=True, bold=is_error)
            if result["error"] and a.get("error_line") and steps >= len(shown):
                el = a.get("error_line")
                ly = top + (el - 1) * line_h + line_h - 6
                ctx.move_to(x + 90, ly)
                for i in range(int((w - 140) / 16)):
                    ctx.line_to(x + 98 + i * 16, ly + (5 if i % 2 == 0 else -1))
                set_color(ctx, C["vermillion"])
                ctx.set_line_width(3)
                ctx.stroke()


# =============================================================================== turtle canvas (runs for real)
TURTLE_COLORS = {"black": "#1B2A3A", "red": "#E8443A", "blue": "#2F80ED", "green": "#009E73", "orange": "#E69F00",
                 "purple": "#8E6BD8", "yellow": "#F0C419", "pink": "#F28CB1", "brown": "#8C5427", "gray": "#8A97A6",
                 "white": "#FFFFFF", "gold": "#F5C542", "navy": "#15324A", "skyblue": "#56B4E9",
                 "lightblue": "#ADD8E6", "darkgreen": "#006400", "violet": "#8E6BD8", "cyan": "#56B4E9"}


def turtle_color(value: str) -> str:
    value = str(value).strip()
    if value.startswith("#") and len(value) in (4, 7):
        return value if len(value) == 7 else "#" + "".join(ch * 2 for ch in value[1:])
    if value.startswith("(") and value.endswith(")"):
        try:
            parts = [float(p) for p in value[1:-1].split(",")]
            if all(p <= 1 for p in parts):
                parts = [p * 255 for p in parts]
            return "#%02X%02X%02X" % tuple(int(p) for p in parts[:3])
        except ValueError:
            pass
    return TURTLE_COLORS.get(value.lower(), C["navy"])


def c_turtle(d: D, a: A, t0: float) -> None:
    """A turtle window that draws what the code really draws: code="...", at=start, duration=seconds."""
    ctx = d.ctx
    x, y, w, h = a.get("x", 1180), a.get("y", 200), a.get("w", 640), a.get("h", 640)
    k = appear(d.t, t0, 0.4)
    if k <= 0:
        return
    result = _run_cached(a.get("code", a.text), tuple(a.get("inputs", ())), a.get("seed", 1))
    fill_rounded(ctx, x + 8, y + 12, w, h, 22, "#000000", 0.12)
    fill_rounded(ctx, x, y, w, h, 22, C["white"], stroke=C["navy"], width=4)
    fill_rounded(ctx, x, y, w, 56, 22, C["gray_light"])
    text(ctx, a.get("title", "Python Turtle Graphics"), x + 24, y + 28, 24, C["ink"], bold=True, anchor="left")
    bg = turtle_color(result.get("bg", "white")) if result.get("bg") not in (None, "white") else C["white"]
    ctx.save()
    rounded_rect(ctx, x + 4, y + 56, w - 8, h - 60, 18)
    ctx.clip()
    ctx.rectangle(x, y + 56, w, h - 56)
    set_color(ctx, bg)
    ctx.fill()
    draw = result["draw"]
    if a.get("world"):
        world = a.get("world")  # half-width of the visible turtle world
    else:  # zoom so the whole drawing fits with a margin
        coords = [abs(v) for it in draw if it[0] == "line" for v in it[1:5]]
        coords += [abs(v) for it in draw if it[0] in ("dot",) for v in it[1:3]]
        coords += [abs(v) for it in draw if it[0] == "fill" for pt in it[2] for v in pt]
        world = min(420.0, max(150.0, (max(coords) if coords else 200.0) * 1.6))
    scale = min(w, h - 60) / (2 * world)
    ox, oy = x + w / 2, y + 56 + (h - 60) / 2

    def screen(px, py):
        return ox + px * scale, oy - py * scale

    seglen = [math.dist((it[1], it[2]), (it[3], it[4])) if it[0] == "line" else 0.0 for it in draw]
    total = sum(seglen) or 1.0
    start_draw = d.T(a.get("run", a.at))
    duration = a.get("duration", 3.0)
    budget = total * progress(d.t, start_draw, duration) if d.t >= start_draw else -1
    finished = d.t >= start_draw + duration
    head = None
    for item, length in zip(draw, seglen):
        if budget < 0:
            break
        if item[0] == "line":
            portion = 1.0 if budget >= length else (budget / length if length else 1.0)
            x1, y1 = screen(item[1], item[2])
            x2, y2 = screen(lerp(item[1], item[3], portion), lerp(item[2], item[4], portion))
            line(ctx, x1, y1, x2, y2, turtle_color(item[5]), max(2.5, item[6] * scale * 1.5))
            head = (x2, y2, math.atan2(y2 - y1, x2 - x1))
            budget -= length
            if portion < 1:
                break
        elif item[0] == "dot":
            sx, sy = screen(item[1], item[2])
            circle(ctx, sx, sy, max(3, item[3] * scale / 2), turtle_color(item[4]))
        elif item[0] == "fill":
            pts = [screen(px, py) for px, py in item[2]]
            if len(pts) > 2:
                ctx.move_to(*pts[0])
                for p in pts[1:]:
                    ctx.line_to(*p)
                ctx.close_path()
                set_color(ctx, turtle_color(item[1]), 0.85)
                ctx.fill()
        elif item[0] == "text":
            sx, sy = screen(item[2], item[3])
            text(ctx, item[1], sx, sy - 14, 28, C["ink"], bold=True,
                 anchor="left" if item[4] == "left" else "center")
    if a.get("cursor", True):
        if finished and result["turtles"]:  # finished: show where the turtle really ends up
            tx, ty, th = result["turtles"][0]
            head = (*screen(tx, ty), -math.radians(th))
        if head is None and result["turtles"]:
            tx, ty, th = result["turtles"][0]
            head = (*screen(0, 0), 0.0) if budget < total else (*screen(tx, ty), -math.radians(th))
        if head is not None:
            hx, hy, angle = head
            ctx.save()
            ctx.translate(hx, hy)
            ctx.rotate(angle)
            ctx.move_to(16, 0)
            ctx.line_to(-12, -11)
            ctx.line_to(-6, 0)
            ctx.line_to(-12, 11)
            ctx.close_path()
            set_color(ctx, C["green"])
            ctx.fill()
            ctx.restore()
    ctx.restore()


# =============================================================================== terminal, tests, file
def c_terminal(d: D, a: A, t0: float) -> None:
    """A Terminal: lines=[(time, text, "cmd"|"out"), ...]; commands are typed, outputs appear."""
    ctx = d.ctx
    x, y, w, h = a.get("x", 120), a.get("y", 200), a.get("w", 1000), a.get("h", 600)
    if appear(d.t, t0, 0.4) <= 0:
        return
    fill_rounded(ctx, x + 8, y + 12, w, h, 22, "#000000", 0.14)
    fill_rounded(ctx, x, y, w, h, 22, "#1E2A36")
    for i, col in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
        circle(ctx, x + 34 + i * 30, y + 30, 9, col)
    text(ctx, a.get("title", "Terminal"), x + w / 2, y + 30, 24, "#AFC2D4", bold=True)
    size = a.get("size", 32)
    row = 0
    for item in a.get("lines", []):
        when, value, kind = item[0], item[1], item[2] if len(item) > 2 else "out"
        start = d.T(when)
        if d.t < start:
            continue
        shown = value
        if kind == "cmd":
            chars = int(len(value) * progress(d.t, start, max(0.4, len(value) * 0.045)))
            shown = "$ " + value[:chars]
        ty = y + 80 + row * size * 1.35
        if ty > y + h - 30:
            break
        text(ctx, shown, x + 30, ty, size, "#7EE787" if kind == "cmd" else "#E6EDF3", anchor="left", mono=True,
             bold=kind == "cmd")
        row += 1


def c_tests(d: D, a: A, t0: float) -> None:
    """pytest-style results: items=[(time, "test_name", passed), ...] with PASSED/FAILED words and colors."""
    ctx = d.ctx
    x, y, w = a.get("x", 1060), a.get("y", 260), a.get("w", 760)
    items = a.get("items", [])
    if appear(d.t, t0, 0.4) <= 0:
        return
    h = 100 + 70 * len(items)
    fill_rounded(ctx, x, y, w, h, 24, C["white"], stroke=C["navy"], width=4)
    text(ctx, a.text or "pytest", x + 30, y + 46, 34, C["navy"], bold=True, anchor="left")
    for i, (when, name, passed) in enumerate(items):
        start = d.T(when)
        k = appear(d.t, start, 0.3)
        if k <= 0:
            continue
        cy = y + 110 + i * 70
        circle(ctx, x + 50, cy, 22 * k, C["green"] if passed else C["vermillion"])
        (check_mark if passed else cross_mark)(ctx, x + 50, cy, 30 * k)
        text(ctx, name, x + 90, cy, 30, C["ink"], anchor="left", mono=True, alpha=k)
        text(ctx, "PASSED" if passed else "FAILED", x + w - 30 - 70, cy, 30,
             C["green"] if passed else C["vermillion"], bold=True, alpha=k)


def c_file(d: D, a: A, t0: float) -> None:
    """A text file: name, lines states=[(time, [line, ...]), ...] (or lines=[...])."""
    ctx = d.ctx
    x, y, w, h = a.get("x", 1240), a.get("y", 240), a.get("w", 520), a.get("h", 520)
    k = appear(d.t, t0, 0.4)
    if k <= 0:
        return
    content = d.keyed(a.get("states"), a.get("lines", [])) or []
    ctx.save()
    ctx.translate(x + w / 2, y + h / 2)
    safe_scale(ctx, max(k, 1e-3), max(k, 1e-3))
    ctx.translate(-w / 2, -h / 2)
    fill_rounded(ctx, 8, 10, w, h, 18, "#000000", 0.10)
    ctx.move_to(0, 0)
    ctx.line_to(w - 70, 0)
    ctx.line_to(w, 70)
    ctx.line_to(w, h)
    ctx.line_to(0, h)
    ctx.close_path()
    set_color(ctx, C["white"])
    ctx.fill_preserve()
    set_color(ctx, C["navy"])
    ctx.set_line_width(4)
    ctx.stroke()
    text(ctx, a.text or "data.txt", 30, 44, 32, C["navy"], bold=True, anchor="left")
    for i, value in enumerate(content[:9]):
        text(ctx, value, 30, 110 + i * 46, 30, C["ink"], anchor="left", mono=True)
    ctx.restore()


# =============================================================================== diagrams
def c_box(d: D, a: A, t0: float) -> None:
    """A labeled variable box whose value changes: values=[(time, value), ...]."""
    value, since = d.keyed_with_time(a.get("values", [(a.at, a.get("value", ""))]))
    def draw():
        w, h = a.get("w", 260), a.get("h", 170)
        fill_rounded(d.ctx, -w / 2 + 6, -h / 2 + 8, w, h, 24, "#000000", 0.10)
        fill_rounded(d.ctx, -w / 2, -h / 2, w, h, 24, color(a.get("color"), "orange"), stroke=C["navy"], width=4)
        fill_rounded(d.ctx, -w / 2 + 20, -h / 2 - 26, w - 40, 52, 18, C["navy"])
        text(d.ctx, a.text, 0, -h / 2, 30, C["white"], bold=True, mono=a.get("mono", True))
        if value is not None:
            pop = 1 + 0.25 * max(0.0, 1 - (d.t - since) / 0.3) if since >= 0 else 1
            d.ctx.save()
            d.ctx.translate(0, 18)
            safe_scale(d.ctx, pop, pop)
            text(d.ctx, str(value), 0, 0, a.get("size", 52), C["ink"], bold=True, mono=True)
            d.ctx.restore()
    _pop(d, a.get("x", 960), a.get("y", 540), t0, draw)


def c_listrow(d: D, a: A, t0: float) -> None:
    """A list as a row of boxes with index numbers: items=[...] or states=[(time, [...])]; highlight=[(from, to, index)]."""
    items = d.keyed(a.get("states"), a.get("items", [])) or []
    cell = a.get("cell", 170)
    x, y = a.get("x", 960), a.get("y", 540)
    left = x - cell * len(items) / 2
    ctx = d.ctx
    k = appear(d.t, t0, 0.4)
    if k <= 0:
        return
    if a.text:
        text(ctx, a.text, left, y - 110, 38, C["navy"], bold=True, anchor="left", mono=True)
    for i, item in enumerate(items):
        cx = left + i * cell
        hl = any(d.T(frm) <= d.t < d.T(to) and idx == i for frm, to, idx in a.get("highlight", []))
        fill_rounded(ctx, cx + 6, y - 60, cell - 12, 120, 18, C["yellow"] if hl else color(a.get("color"), "sky"),
                     stroke=C["navy"], width=6 if hl else 4)
        label = str(item)
        fit = int(min(a.get("size", 36), (cell - 28) / (max(len(label), 1) * 0.62)))
        text(ctx, label, cx + cell / 2, y, max(fit, 16), C["ink"], bold=True, mono=True)
        if a.get("indexes", True):
            text(ctx, str(i), cx + cell / 2, y + 92, 32, C["vermillion"], bold=True, mono=True)
    if a.get("indexes", True) and items:
        text(ctx, "index", left - 20, y + 92, 28, C["vermillion"], bold=True, anchor="center")


def c_dict(d: D, a: A, t0: float) -> None:
    """A dictionary as key → value cards: rows=[(key, value), ...] or states=[(time, rows)]; highlight=[(from, to, key)]."""
    rows = d.keyed(a.get("states"), a.get("rows", [])) or []
    x, y, w = a.get("x", 1100), a.get("y", 260), a.get("w", 680)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    if a.text:
        text(ctx, a.text, x, y - 40, 38, C["navy"], bold=True, anchor="left", mono=True)
    for i, (key, value) in enumerate(rows):
        cy = y + i * 96
        hl = any(d.T(frm) <= d.t < d.T(to) and k2 == key for frm, to, k2 in a.get("highlight", []))
        fill_rounded(ctx, x, cy, w * 0.45, 76, 18, C["yellow"] if hl else C["orange_light"], stroke=C["navy"], width=4)
        text(ctx, str(key), x + w * 0.225, cy + 38, 32, C["ink"], bold=True, mono=True, max_width=int(w * 0.42))
        line(ctx, x + w * 0.47, cy + 38, x + w * 0.53, cy + 38, C["navy"], 6)
        fill_rounded(ctx, x + w * 0.55, cy, w * 0.45, 76, 18, C["green_light"], stroke=C["navy"], width=4)
        text(ctx, str(value), x + w * 0.775, cy + 38, 32, C["ink"], bold=True, mono=True, max_width=int(w * 0.42))


def c_flow(d: D, a: A, t0: float) -> None:
    """An if/elif/else chain: items=["size > 100?", "size > 50?"], outcomes=["big", "medium", "small"],
    token=[(time, label, outcome_index), ...] moves a token down the chain to the chosen outcome."""
    items, outcomes = a.get("items", []), a.get("outcomes", [])
    x, y, gap = a.get("x", 700), a.get("y", 260), a.get("gap", 190)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    for i, question in enumerate(items):
        cy = y + i * gap
        tw, _ = text_size(question, 34, bold=True, mono=True)
        half = tw / 2 + 60
        ctx.move_to(x - half, cy)
        ctx.line_to(x, cy - 60)
        ctx.line_to(x + half, cy)
        ctx.line_to(x, cy + 60)
        ctx.close_path()
        set_color(ctx, C["sky_light"])
        ctx.fill_preserve()
        set_color(ctx, C["navy"])
        ctx.set_line_width(4)
        ctx.stroke()
        text(ctx, question, x, cy, 34, C["ink"], bold=True, mono=True)
        line(ctx, x + half, cy, x + half + 120, cy, C["green"], 6)
        text(ctx, "yes", x + half + 60, cy - 26, 26, C["green"], bold=True)
        fill_rounded(ctx, x + half + 120, cy - 40, 240, 80, 20, C["green_light"], stroke=C["green"], width=4)
        text(ctx, outcomes[i] if i < len(outcomes) else "", x + half + 240, cy, 32, C["ink"], bold=True)
        if i + 1 <= len(items):
            line(ctx, x, cy + 60, x, cy + gap - 60 if i + 1 < len(items) else cy + gap - 40, C["vermillion"], 6)
            text(ctx, "no", x - 34, cy + 95, 26, C["vermillion"], bold=True)
    if len(outcomes) > len(items):
        cy = y + len(items) * gap
        fill_rounded(ctx, x - 140, cy - 40, 280, 80, 20, C["orange_light"], stroke=C["orange"], width=4)
        text(ctx, outcomes[-1], x, cy, 32, C["ink"], bold=True)
    current, since = d.keyed_with_time(a.get("token", []))
    if current:
        label, outcome = current[0], current[1]
        k = ease_in_out(progress(d.t, since, 1.2))
        stops = [(x, y + i * gap) for i in range(min(outcome + 1, len(items)))]
        if outcome < len(items):
            tw, _ = text_size(items[outcome], 34, bold=True, mono=True)
            end = (x + tw / 2 + 240 + 60, y + outcome * gap)
        else:
            end = (x, y + len(items) * gap)
        path_pts = [(x, y - 120)] + stops + [end]
        seg = k * (len(path_pts) - 1)
        i = min(int(seg), len(path_pts) - 2)
        f = seg - i
        tx = lerp(path_pts[i][0], path_pts[i + 1][0], f)
        ty = lerp(path_pts[i][1], path_pts[i + 1][1], f)
        circle(ctx, tx, ty - 50, 34, C["yellow"], stroke=C["navy"], width=4)
        text(ctx, str(label), tx, ty - 50, 28, C["ink"], bold=True, mono=True)


def c_machine(d: D, a: A, t0: float) -> None:
    """A function machine: items=[(time, input, output), ...] slides an input card in and an output card out."""
    x, y = a.get("x", 960), a.get("y", 520)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    fill_rounded(ctx, x - 180, y - 120, 360, 240, 36, C["purple"], stroke=C["navy"], width=5)
    _gear_spin = d.gt * 2
    P._gear(ctx, x - 120, y - 70, 26, _gear_spin, C["yellow"])
    P._gear(ctx, x + 120, y - 70, 26, -_gear_spin, C["yellow"])
    text(ctx, a.text or "function", x, y + 10, 40, C["white"], bold=True, mono=True)
    current, since = d.keyed_with_time(a.get("items", []))
    if current:
        value_in, value_out = current[0], current[1]
        k = progress(d.t, since, 1.6)
        if k < 0.5:
            cx = lerp(x - 520, x - 200, ease_out(k * 2))
            fill_rounded(ctx, cx - 90, y - 45, 180, 90, 20, C["orange_light"], stroke=C["navy"], width=4)
            text(ctx, str(value_in), cx, y, 36, C["ink"], bold=True, mono=True)
        else:
            cx = lerp(x + 200, x + 520, ease_out((k - 0.5) * 2))
            fill_rounded(ctx, cx - 90, y - 45, 180, 90, 20, C["green_light"], stroke=C["navy"], width=4)
            text(ctx, str(value_out), cx, y, 36, C["ink"], bold=True, mono=True)
        text(ctx, "in", x - 520, y + 90, 30, C["gray"], bold=True)
        text(ctx, "out", x + 520, y + 90, 30, C["gray"], bold=True)


def c_timeline(d: D, a: A, t0: float) -> None:
    """A git history: commits=[(time, "message"), ...] as dots on a line; head label on the newest."""
    commits = a.get("commits", [])
    x, y, w = a.get("x", 200), a.get("y", 540), a.get("w", 1500)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    shown = [(d.T(when), msg) for when, msg in commits if d.t >= d.T(when)]
    gap = w / max(len(commits), 1)
    if len(shown) > 1:
        grow = ease_out(progress(d.t, shown[-1][0], 0.4))
        line(ctx, x, y, x + gap * (len(shown) - 2 + grow), y, C["navy"], 8)
    for i, (when, msg) in enumerate(shown):
        cx = x + i * gap
        k = appear(d.t, when, 0.4)
        circle(ctx, cx, y, 30 * k, C["orange"], stroke=C["navy"], width=5)
        text(ctx, msg, cx, y + (80 if i % 2 == 0 else -80), 28, C["ink"], bold=True, alpha=k, max_width=int(gap + 120))
    if shown and a.get("head", True):
        cx = x + (len(shown) - 1) * gap
        fill_rounded(ctx, cx - 50, y - 170 if (len(shown) - 1) % 2 == 0 else y + 120, 100, 44, 14, C["green"])
        text(ctx, "HEAD", cx, (y - 148) if (len(shown) - 1) % 2 == 0 else y + 142, 24, C["white"], bold=True)


def c_bars(d: D, a: A, t0: float) -> None:
    """Bars for sorting or charts: states=[(time, [values])], labels=[...], highlight=[(from, to, [indexes])]."""
    values = d.keyed(a.get("states"), a.get("values", [])) or []
    x, y, w, h = a.get("x", 300), a.get("y", 300), a.get("w", 1300), a.get("h", 520)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0 or not values:
        return
    top = max(max(values), 1)
    bw = w / len(values)
    labels = a.get("labels") or []
    for i, value in enumerate(values):
        hl = any(d.T(frm) <= d.t < d.T(to) and i in idx for frm, to, idx in a.get("highlight", []))
        bh = h * value / top
        fill_rounded(ctx, x + i * bw + 10, y + h - bh, bw - 20, bh, 12, C["yellow"] if hl else C["sky"],
                     stroke=C["navy"], width=4)
        text(ctx, str(value), x + i * bw + bw / 2, y + h - bh - 30, 32, C["ink"], bold=True)
        if i < len(labels):
            text(ctx, str(labels[i]), x + i * bw + bw / 2, y + h + 36, 28, C["ink"], bold=True, max_width=int(bw - 6))
    line(ctx, x, y + h, x + w, y + h, C["navy"], 5)


GRID_COLORS = {"#": C["navy"], ".": C["white"], " ": C["white"], "S": C["green_light"], "G": C["yellow"],
               "R": "#F4A6A0", "B": C["sky"], "O": C["orange_light"], "P": "#E3D8FB", "X": C["vermillion"],
               "F": C["green"], "W": C["sky_light"]}


def c_grid(d: D, a: A, t0: float) -> None:
    """A grid of cells: rows=["#..#", ...] or states=[(time, rows)]; marks=[(time, row, col, "label")]."""
    rows = d.keyed(a.get("states"), a.get("rows", [])) or []
    cell = a.get("cell", 90)
    x, y = a.get("x", 300), a.get("y", 220)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            fill_rounded(ctx, x + c * cell + 3, y + r * cell + 3, cell - 6, cell - 6, 10, GRID_COLORS.get(ch, C["white"]),
                         stroke=C["gray"], width=2)
            if ch.isdigit() or (ch.isalpha() and ch not in GRID_COLORS):
                text(ctx, ch, x + c * cell + cell / 2, y + r * cell + cell / 2, int(cell * 0.45), C["ink"], bold=True)
    for mark in a.get("marks", []):
        when, r, c, label = mark
        if d.t >= d.T(when):
            k = appear(d.t, d.T(when), 0.3)
            text(ctx, str(label), x + c * cell + cell / 2, y + r * cell + cell / 2, int(cell * 0.5), C["ink"], bold=True,
                 scale=k)
    walker = d.path(a.get("walker"), tuple(a.get("walker")[0][1:3])) if a.get("walker") else None
    if walker:
        wc, wr = walker
        draw_pixi(ctx, x + wc * cell + cell / 2, y + wr * cell + cell * 0.8, cell / 260, d.gt, mood="happy",
                   ground=y + wr * cell + cell * 0.9)


def c_scatter(d: D, a: A, t0: float) -> None:
    """A feature chart: points=[(fx, fy, "label", "color"), ...], axes=("x name", "y name"), query=(time, fx, fy),
    nearest=(time, index) circles the closest example and draws the steps (gap + gap) path."""
    x, y, w, h = a.get("x", 260), a.get("y", 180), a.get("w", 900), a.get("h", 700)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    span = a.get("span", 10)
    fill_rounded(ctx, x, y, w, h, 20, C["white"], stroke=C["navy"], width=4)
    def at(fx, fy):
        return x + 60 + (w - 100) * fx / span, y + h - 60 - (h - 100) * fy / span
    line(ctx, x + 60, y + h - 60, x + w - 30, y + h - 60, C["navy"], 4)
    line(ctx, x + 60, y + h - 60, x + 60, y + 30, C["navy"], 4)
    axes = a.get("axes", ("", ""))
    text(ctx, axes[0], x + w / 2, y + h - 22, 28, C["ink"], bold=True)
    ctx.save()
    ctx.translate(x + 24, y + h / 2)
    ctx.rotate(-math.pi / 2)
    text(ctx, axes[1], 0, 0, 28, C["ink"], bold=True)
    ctx.restore()
    for i, point in enumerate(a.get("points", [])):
        fx, fy, label = point[0], point[1], point[2]
        px, py = at(fx, fy)
        circle(ctx, px, py, 18, color(point[3], C["sky"]) if len(point) > 3 else C["sky"], stroke=C["navy"], width=3)
        text(ctx, label, px, py - 36, 24, C["ink"], bold=True)
    query = a.get("query")
    if query and d.t >= d.T(query[0]):
        qx, qy = at(query[1], query[2])
        star(ctx, qx, qy, 26 * appear(d.t, d.T(query[0])), C["vermillion"])
        nearest = a.get("nearest")
        if nearest and d.t >= d.T(nearest[0]):
            point = a.get("points")[nearest[1]]
            px, py = at(point[0], point[1])
            k = ease_out(progress(d.t, d.T(nearest[0]), 1.0))
            corner_x = lerp(qx, px, min(1.0, k * 2))
            line(ctx, qx, qy, corner_x, qy, C["orange"], 6)
            if k > 0.5:
                line(ctx, px, qy, px, lerp(qy, py, (k - 0.5) * 2), C["orange"], 6)
            if k >= 1:
                ctx.arc(px, py, 34, 0, 2 * math.pi)
                set_color(ctx, C["green"])
                ctx.set_line_width(6)
                ctx.stroke()


def c_table(d: D, a: A, t0: float) -> None:
    """A small table (CSV rows): header=[...], rows=[[...], ...], highlight=[(from, to, row_index)]."""
    header, rows = a.get("header", []), a.get("rows", [])
    x, y, cw, rh = a.get("x", 200), a.get("y", 260), a.get("col_w", 230), a.get("row_h", 70)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    if a.text:
        text(ctx, a.text, x, y - 40, 34, C["navy"], bold=True, anchor="left", mono=True)
    for c, name in enumerate(header):
        fill_rounded(ctx, x + c * cw, y, cw - 6, rh - 6, 10, C["navy"])
        text(ctx, str(name), x + c * cw + cw / 2, y + rh / 2 - 3, 28, C["white"], bold=True, mono=True)
    for r, row in enumerate(rows):
        reveal = a.get("reveal")
        if reveal and r < len(reveal) and d.t < d.T(reveal[r]):
            continue
        hl = any(d.T(frm) <= d.t < d.T(to) and idx == r for frm, to, idx in a.get("highlight", []))
        for c, value in enumerate(row):
            fill_rounded(ctx, x + c * cw, y + (r + 1) * rh, cw - 6, rh - 6, 10,
                         C["yellow"] if hl else (C["white"] if r % 2 == 0 else C["gray_light"]), stroke=C["gray"], width=2)
            text(ctx, str(value), x + c * cw + cw / 2, y + (r + 1) * rh + rh / 2 - 3, 28, C["ink"], mono=True)


def c_tree(d: D, a: A, t0: float) -> None:
    """Class boxes in a family tree: nodes=[(name, parent_or_None, ["line", ...], time), ...]."""
    nodes = a.get("nodes", [])
    x, y = a.get("x", 960), a.get("y", 220)
    ctx = d.ctx
    levels = {}
    for name, parent, *_ in nodes:
        levels[name] = 0 if parent is None else levels.get(parent, 0) + 1
    by_level = {}
    for name, parent, *_ in nodes:
        by_level.setdefault(levels[name], []).append(name)
    bodies = {name: body for name, parent, body, *_ in nodes}
    pos = {}
    for lvl, names in by_level.items():
        gap = a.get("gap", 460)
        for i, name in enumerate(names):
            pos[name] = (x + (i - (len(names) - 1) / 2) * gap, y + lvl * a.get("level_gap", 300))
    for name, parent, body, *rest in nodes:
        when = rest[0] if rest else a.at
        if d.t < d.T(when):
            continue
        k = appear(d.t, d.T(when))
        nx, ny = pos[name]
        if parent and parent in pos:
            px, py = pos[parent]
            parent_h = 70 + 44 * len(bodies.get(parent, []))
            line(ctx, px, py + parent_h, nx, ny - 4, C["navy"], 5, alpha=k)
        bw = a.get("w", 380)
        bh = 70 + 44 * len(body)
        ctx.save()
        ctx.translate(nx, ny + bh / 2)
        safe_scale(ctx, max(k, 1e-3), max(k, 1e-3))
        fill_rounded(ctx, -bw / 2, -bh / 2, bw, bh, 18, C["white"], stroke=C["navy"], width=4)
        fill_rounded(ctx, -bw / 2, -bh / 2, bw, 60, 18, C["purple"])
        text(ctx, name, 0, -bh / 2 + 30, 32, C["white"], bold=True, mono=True)
        for i, item in enumerate(body):
            text(ctx, item, -bw / 2 + 24, -bh / 2 + 88 + i * 44, 26, C["ink"], anchor="left", mono=True)
        ctx.restore()


def c_stack(d: D, a: A, t0: float) -> None:
    """A stack of plates: states=[(time, [bottom, ..., top])]."""
    items = d.keyed(a.get("states"), a.get("items", [])) or []
    x, y = a.get("x", 960), a.get("y", 820)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    if a.text:
        text(ctx, a.text, x, y + 60, 34, C["navy"], bold=True)
    for i, item in enumerate(items):
        cy = y - i * 76
        fill_rounded(ctx, x - 170, cy - 64, 340, 64, 30, C["sky_light"] if i % 2 == 0 else C["orange_light"],
                     stroke=C["navy"], width=4)
        text(ctx, str(item), x, cy - 32, 30, C["ink"], bold=True)
    if items:
        text(ctx, "top", x + 230, y - (len(items) - 1) * 76 - 32, 28, C["vermillion"], bold=True)


def c_queue(d: D, a: A, t0: float) -> None:
    """A queue (line of turns): states=[(time, [front, ..., back])]."""
    items = d.keyed(a.get("states"), a.get("items", [])) or []
    x, y, gap = a.get("x", 400), a.get("y", 560), a.get("gap", 210)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    if a.text:
        text(ctx, a.text, x, y - 150, 34, C["navy"], bold=True, anchor="left")
    for i, item in enumerate(items):
        cx = x + i * gap
        fill_rounded(ctx, cx, y - 60, gap - 30, 120, 24, C["green_light"] if i == 0 else C["sky_light"],
                     stroke=C["navy"], width=4)
        text(ctx, str(item), cx + (gap - 30) / 2, y, 30, C["ink"], bold=True, max_width=gap - 40)
    if items:
        text(ctx, "front", x + (gap - 30) / 2, y + 100, 28, C["green"], bold=True)
        text(ctx, "back", x + (len(items) - 1) * gap + (gap - 30) / 2, y + 100, 28, C["vermillion"], bold=True)


def c_roadmap(d: D, a: A, t0: float) -> None:
    """Project milestones: items=["M1 Plan", ...], checks=[(time, index)], current=[(time, index)]."""
    items = a.get("items", [])
    x, y, w = a.get("x", 220), a.get("y", 520), a.get("w", 1480)
    ctx = d.ctx
    if appear(d.t, t0, 0.4) <= 0:
        return
    gap = w / max(len(items) - 1, 1)
    line(ctx, x, y, x + w, y, C["gray"], 14)
    checked = {idx for when, idx in a.get("checks", []) if d.t >= d.T(when)}
    current = d.keyed(a.get("current"), None)
    for i, label in enumerate(items):
        cx = x + i * gap
        is_now = current == i
        circle(ctx, cx, y, 46 if is_now else 38, C["green"] if i in checked else (C["yellow"] if is_now else C["white"]),
               stroke=C["navy"], width=5)
        if i in checked:
            check_mark(ctx, cx, y, 50)
        text(ctx, label, cx, y + 90, 32, C["ink"], bold=True, max_width=int(gap - 10))


# =============================================================================== feedback and sound
def c_badge(d: D, a: A, t0: float) -> None:
    P.badge(d.ctx, a.get("x", 1600), a.get("y", 300), a.get("r", 48), a.get("ok", True), d.t, t0)


def c_confetti(d: D, a: A, t0: float) -> None:
    P.confetti(d.ctx, a.get("x", W / 2), a.get("y", 500), d.t, t0)


def c_sfx(d: D, a: A, t0: float) -> None:
    return None


COMPONENTS = {name[2:]: fn for name, fn in list(globals().items()) if name.startswith("c_") and callable(fn)}

# default sound for each kind when it appears (authors can add explicit A("sfx", "name", at=...))
DEFAULT_SFX = {"chip": "pop", "banner": "pop", "bigtext": "sparkle", "bubble": "pop", "panel": "pop", "cards": None,
               "icons": None, "scratch": None, "badge": None, "confetti": "sparkle", "box": "pop", "listrow": "pop",
               "dict": "pop", "flow": "pop", "machine": "pop", "timeline": None, "bars": "pop", "grid": "pop",
               "scatter": "pop", "table": "pop", "tree": None, "stack": "pop", "queue": "pop", "roadmap": "pop",
               "tests": None, "file": "pop", "terminal": "pop", "code": "pop", "turtle": "pop", "stage": "pop",
               "laptop": "pop", "key": "sparkle", "grownup": "pop", "cat": "pop"}


# =============================================================================== settings, intro and outro
GRADIENTS = {"sky": ("#E8F5FF", "#FFF8EC"), "lavender": ("#F0EAFF", "#FFF8EC"), "mint": ("#EAF7F1", "#FFF8EC"),
             "peach": ("#FFF1E3", "#FFF8EC"), "night": ("#18324B", "#25507A"), "stage": ("#2C2240", "#4A3A66")}


def setting(ctx, name: str, gt: float) -> None:
    if name == "workshop":
        P.workshop(ctx, gt, floor_y=800)
    else:
        top, bottom = GRADIENTS.get(name, GRADIENTS["sky"])
        vertical_gradient(ctx, 0, 0, W, H, top, bottom)


def is_junior(level) -> bool:
    return isinstance(level, str) and level.startswith("j")


def level_label(level) -> str:
    return f"Junior Level {level[1:]}" if is_junior(level) else f"Level {level}"


def make_intro(level, week: int, title: str):
    host = draw_aiden if is_junior(level) else draw_rose

    def intro(ctx, t, gt):
        vertical_gradient(ctx, 0, 0, W, H, "#18324B", "#25507A")
        for i in range(40):
            star(ctx, (i * 397) % W, (i * 211) % H, 4 + (i % 3) * 2, C["white"], 0.25 + 0.25 * math.sin(gt * 2 + i),
                 rotation=gt * 0.3)
        P.logo(ctx, W / 2, H / 2 - 80, 1.0, t, 0.2)
        sub = fade(t, 1.6, 0.5)
        if sub > 0:
            label = f"{level_label(level)} • Week {week}: {title}"
            tw, _ = text_size(label, 50, bold=True)
            fill_rounded(ctx, W / 2 - tw / 2 - 50, H / 2 + 150, tw + 100, 110, 55, C["white"], sub)
            text(ctx, label, W / 2, H / 2 + 205, 50, C["navy"], bold=True, alpha=sub)
        draw_pixi(ctx, 260, 980 + 40 * (1 - ease_out(progress(t, 0.6, 0.8))), 0.6, gt, mood="happy", ground=1040)
        host(ctx, 1660, 1110 - 120 * ease_out(progress(t, 0.9, 0.8)), 0.6, gt, mood="happy", wave=1.0)
    return intro


def make_outro(level):
    host = draw_aiden if is_junior(level) else draw_rose
    grades = "Grades 2–3" if is_junior(level) else "Grades 4–6"

    def outro(ctx, t, gt):
        vertical_gradient(ctx, 0, 0, W, H, "#18324B", "#25507A")
        P.logo(ctx, W / 2, 360, 0.75, t, 0.0)
        a = fade(t, 0.4)
        text(ctx, "See you next time!", W / 2, 640, 56, C["white"], bold=True, alpha=a)
        text(ctx, "Narration uses AI-generated voices.", W / 2, 790, 38, C["led"], bold=True, alpha=a)
        text(ctx, f"Kids Coding • {level_label(level)} • {grades}", W / 2, 860, 32, "#C9D6E3", alpha=a)
        draw_pixi(ctx, 300, 980, 0.55, gt, mood="proud", ground=1040)
        host(ctx, 1640, 1080, 0.55, gt, mood="happy", wave=1.0)
    return outro


# =============================================================================== compile an episode
FADE_OUT = 0.2  # seconds an action takes to disappear after its `until`
def compile_episode(episode: Episode, title: str):
    """Turn episode data into the (script, drawing) pair the renderer expects."""
    scenes = list(episode.scenes)

    def make_scene(scene):
        def draw(ctx, t, sc, gt):
            resolve = functools.lru_cache(maxsize=None)(lambda spec: resolve_time(spec, sc))
            setting(ctx, scene.setting, gt)
            d = D(ctx, t, gt, sc, resolve)
            for action in scene.actions:
                t0 = resolve(action.at)
                t1 = resolve(action.until)
                if t < t0 - 0.001 or t > t1 + FADE_OUT:
                    continue
                fn = COMPONENTS.get(action.kind)
                if fn is None:
                    raise ValueError(f"{scene.scene_id}: unknown action kind {action.kind!r}")
                if t > t1:  # fade out after `until`
                    ctx.push_group()
                    fn(d, action, t0)
                    ctx.pop_group_to_source()
                    ctx.paint_with_alpha(1 - (t - t1) / FADE_OUT)
                else:
                    fn(d, action, t0)
        return draw

    def make_sfx(scene):
        def sfx(sc):
            events = []
            resolve = lambda spec: resolve_time(spec, sc)  # noqa: E731
            for action in scene.actions:
                start = sc.start + resolve(action.at)
                if action.kind == "sfx":
                    events.append((start, action.text))
                    continue
                name = DEFAULT_SFX.get(action.kind)
                if action.kind == "badge":
                    name = "chime" if action.get("ok", True) else "oops"
                if name and resolve(action.at) > 0.05:
                    events.append((start, name))
                if action.kind == "cards":
                    for when in action.get("reveal") or []:
                        events.append((sc.start + resolve(when), "pop"))
                if action.kind == "scratch":
                    for when in action.get("reveal") or []:
                        events.append((sc.start + resolve(when) + 0.45, "snap"))
                    if action.get("swap"):
                        events.append((sc.start + resolve(action.get("swap")[0]), "whoosh"))
                if action.kind == "code" and action.get("run") is not None:
                    events.append((sc.start + resolve(action.get("run")), "pop"))
                if action.kind == "turtle":
                    events.append((sc.start + resolve(action.get("run", action.at)), "zoom"))
                if action.kind == "icons":
                    for item in action.get("items", []):
                        if len(item) > 2:
                            events.append((sc.start + resolve(item[2]), "pop"))
                if action.kind == "tests":
                    for when, _, passed in action.get("items", []):
                        events.append((sc.start + resolve(when), "chime" if passed else "oops"))
                if action.kind == "timeline":
                    for when, _ in action.get("commits", []):
                        events.append((sc.start + resolve(when), "snap"))
                if action.kind in ("rose", "aiden") and action.get("enter"):
                    events.append((start, "whoosh"))
                if action.kind == "pixi" and action.get("drop"):
                    events.append((start + 0.5, "boing"))
            # questions with a long pause get a soft ticking clock
            for beat, nxt in zip(sc.beats, sc.beats[1:] + [None]):
                end_of_pause = nxt.start if nxt else sc.end
                if beat.text.strip().endswith("?") and end_of_pause - beat.end >= 2.0:
                    events += [(beat.end + 0.4 + k, "tick") for k in range(int(end_of_pause - beat.end - 0.4))]
            return events
        return sfx

    script = SimpleNamespace(SCRIPTS=episode.scripts)
    drawing = SimpleNamespace(
        SCENES=[make_scene(s) for s in scenes], SFX=[make_sfx(s) for s in scenes], INTRO=4.6, OUTRO=5.0,
        intro=make_intro(episode.level, episode.week, title), outro=make_outro(episode.level),
        TITLE=title, WEEK=episode.week,
    )
    return script, drawing
