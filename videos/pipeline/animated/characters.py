"""The Kids Coding characters, drawn as simple vector shapes so they animate smoothly.

Nova: a ten-year-old inventor with workshop goggles (no gendered features or pronouns).
Pixel: a palm-sized hovering helper robot with an LED face.
Both blink, bob gently while idle, and change expression; Nova's mouth follows the voice.
"""

from __future__ import annotations

import math

import cairo

from .engine import C, blink, safe_scale, circle, clamp, ellipse, fill_rounded, glow, line, rounded_rect, set_color, shadow

# Moods: "happy", "talk", "surprised", "confused", "proud", "thinking", "worried"


def draw_nova(ctx: cairo.Context, x: float, y: float, s: float, t: float, mood: str = "happy",
              talk: float = 0.0, wave: float = 0.0, point: float = 0.0, look: float = 0.0,
              hand_on_chin: float = 0.0) -> None:
    """Nova standing with feet at (x, y). s=1 is about 430 px tall.

    wave: 0-1 waving right arm; point: 0-1 right arm stretched out; look: -1 (left) .. 1 (right);
    hand_on_chin: 0-1 thinking pose with the left hand.
    """
    bob = math.sin(t * 2.2) * 3
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, s, s)
    shadow(ctx, 0, 0, 95, 16)
    # legs and shoes
    for side in (-1, 1):
        fill_rounded(ctx, side * 26 - 18, -120, 36, 112, 16, "#2C3E66")
        fill_rounded(ctx, side * 30 - 30, -20, 60, 24, 12, C["white"], stroke=C["navy"], width=4)
    ctx.translate(0, bob)
    # left arm (thinking pose bends to the chin)
    _arm(ctx, -70, -250, angle=lerp_angle(100, -35, hand_on_chin), bend=hand_on_chin)
    # body: hoodie
    fill_rounded(ctx, -78, -270, 156, 170, 48, C["blue"])
    fill_rounded(ctx, -40, -190, 80, 46, 18, "#2670D4")  # pocket
    line(ctx, -14, -268, -18, -222, C["white"], 6)  # hoodie strings
    line(ctx, 14, -268, 18, -222, C["white"], 6)
    # right arm: idle, waving or pointing
    # 0 degrees points right, 90 points down (screen coordinates)
    if point > 0:
        angle = lerp_angle(80, -12 + 3 * math.sin(t * 3), point)
    else:
        angle = lerp_angle(80, -55 + 22 * math.sin(t * 10), wave)
    _arm(ctx, 70, -250, angle=angle, bend=0.0, right=True)
    # head
    hx, hy = look * 6, -350
    circle(ctx, hx, hy, 84, C["skin"])
    # ears
    circle(ctx, hx - 82, hy + 8, 16, C["skin"])
    circle(ctx, hx + 82, hy + 8, 16, C["skin"])
    # hair: short curls
    for cx, cy, r in ((-60, -40, 34), (-30, -66, 38), (8, -74, 40), (46, -62, 36), (70, -34, 28), (-76, -10, 22)):
        circle(ctx, hx + cx, hy + cy, r, C["hair"])
    # goggles on the forehead (the inventor's signature)
    line(ctx, hx - 84, hy - 30, hx + 84, hy - 30, C["orange"], 12)
    for gx in (-30, 30):
        circle(ctx, hx + gx, hy - 32, 22, C["orange"])
        circle(ctx, hx + gx, hy - 32, 15, C["sky_light"])
        circle(ctx, hx + gx - 5, hy - 37, 4, C["white"])
    _face(ctx, hx, hy, t, mood, talk, look)
    ctx.restore()


def lerp_angle(a: float, b: float, x: float) -> float:
    return a + (b - a) * clamp(x)


def _arm(ctx, sx, sy, angle: float, bend: float, right: bool = False) -> None:
    """An arm from the shoulder at (sx, sy); angle in degrees (0 = right, 90 = down)."""
    rad = math.radians(angle)
    length = 120 - 45 * bend
    ex, ey = sx + length * math.cos(rad), sy + length * math.sin(rad)
    line(ctx, sx, sy, ex, ey, C["blue"], 34)
    circle(ctx, ex, ey, 19, C["skin"])


def _face(ctx, hx, hy, t, mood, talk, look) -> None:
    open_amount = blink(t, seed=0.3)
    if mood == "surprised":
        open_amount = 1.0
    eye_y = hy + 8
    for side in (-1, 1):
        ex = hx + side * 30
        eh = 17 * open_amount + (4 if mood == "surprised" else 0)
        ellipse(ctx, ex, eye_y, 14, max(eh, 1.5), C["white"])
        if open_amount > 0.25:
            circle(ctx, ex + look * 5, eye_y + 2, 9, C["ink"])
            circle(ctx, ex + look * 5 + 3, eye_y - 2, 3, C["white"])
        # eyebrows
        lift = {"surprised": -12, "worried": -4, "confused": -8 if side > 0 else 0, "thinking": -6}.get(mood, 0)
        tilt = {"worried": 6 * side, "confused": -6 * side if side > 0 else 0}.get(mood, 0)
        line(ctx, ex - 14, eye_y - 26 + lift + tilt, ex + 14, eye_y - 26 + lift - tilt, C["hair"], 6)
    # cheeks
    circle(ctx, hx - 52, hy + 34, 12, C["pink"], 0.45)
    circle(ctx, hx + 52, hy + 34, 12, C["pink"], 0.45)
    # mouth
    my = hy + 46
    if talk > 0.05:
        ellipse(ctx, hx, my, 16 + 4 * talk, 4 + 16 * talk, "#5A1E1E")
        ellipse(ctx, hx, my + 4 + 8 * talk, 9, 3 + 4 * talk, "#E86A6A")
    elif mood == "surprised":
        ellipse(ctx, hx, my + 2, 11, 13, "#5A1E1E")
    elif mood in ("confused", "worried", "thinking"):
        ctx.move_to(hx - 16, my + 4)
        ctx.curve_to(hx - 6, my - 4, hx + 6, my + 8, hx + 16, my)
        set_color(ctx, "#5A1E1E")
        ctx.set_line_width(6)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
    else:  # happy / proud
        width = 26 if mood == "proud" else 22
        ctx.move_to(hx - width, my - 6)
        ctx.curve_to(hx - width / 2, my + 14, hx + width / 2, my + 14, hx + width, my - 6)
        set_color(ctx, "#5A1E1E")
        ctx.set_line_width(6)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()


def draw_pixel(ctx: cairo.Context, x: float, y: float, s: float, t: float, mood: str = "happy",
               carrying: bool = False, facing: float = 0.0, beep: float = 0.0, ground: float | None = None) -> None:
    """Pixel hovering with the bottom of its body near (x, y). s=1 is about 230 px tall.

    beep: 0-1 flashes the antenna and widens the eyes (use while Pixel beeps or speaks).
    ground: y of the floor for the shadow (defaults to just below Pixel).
    """
    hover = math.sin(t * 3.1) * 7
    floor = (ground if ground is not None else y + 40)
    shadow(ctx, x, floor, 70 * s * (1 - hover / 80), 13 * s, 0.16)
    ctx.save()
    ctx.translate(x, y + hover)
    safe_scale(ctx, s, s)
    ctx.rotate(math.radians(facing * 6))
    # thruster glow
    glow(ctx, 0, 8, 46, C["led"], 0.35 + 0.2 * math.sin(t * 9))
    # antenna
    line(ctx, 0, -200, 0, -232, C["gray"], 7)
    pulse = 0.5 + 0.5 * math.sin(t * 5) if beep <= 0 else 1.0
    glow(ctx, 0, -240, 34, C["orange"], 0.25 + 0.5 * max(beep, pulse * 0.4))
    circle(ctx, 0, -240, 12, C["orange"])
    # arms
    for side in (-1, 1):
        reach = 26 if carrying else 0
        line(ctx, side * 78, -98, side * (100 - reach * 0.6), -60 - reach, C["gray"], 16)
        circle(ctx, side * (100 - reach * 0.6), -60 - reach, 14, C["gray_light"], stroke=C["gray"], width=4)
    # body
    fill_rounded(ctx, -84, -200, 168, 196, 56, C["white"], stroke=C["navy"], width=7)
    fill_rounded(ctx, -64, -176, 128, 98, 28, C["screen"])
    # belly light strip
    for i, color in enumerate((C["green"], C["yellow"], C["sky"])):
        circle(ctx, -24 + i * 24, -42, 7, color)
    _pixel_face(ctx, t, mood, beep)
    ctx.restore()


def _pixel_face(ctx, t, mood, beep) -> None:
    eye_y = -132
    color = C["led"]
    open_amount = blink(t, seed=1.9)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    if mood in ("happy", "proud") and beep <= 0.2:
        for side in (-1, 1):  # ^ ^ eyes
            ctx.move_to(side * 28 - 14, eye_y + 6)
            ctx.line_to(side * 28, eye_y - 8)
            ctx.line_to(side * 28 + 14, eye_y + 6)
            set_color(ctx, color)
            ctx.set_line_width(8)
            ctx.stroke()
    elif mood == "surprised" or beep > 0.2:
        for side in (-1, 1):
            circle(ctx, side * 28, eye_y, 14 + 3 * beep, color)
    elif mood == "confused":
        fill_rounded(ctx, -40, eye_y - 12 * open_amount, 22, max(24 * open_amount, 3), 8, color)
        fill_rounded(ctx, 20, eye_y - 4, 22, 8, 4, color)
    elif mood == "thinking":
        for side in (-1, 1):
            fill_rounded(ctx, side * 28 - 11, eye_y - 14, 22, max(16 * open_amount, 3), 8, color)
    else:
        for side in (-1, 1):
            fill_rounded(ctx, side * 28 - 11, eye_y - 12 * open_amount, 22, max(24 * open_amount, 3), 8, color)
    # mouth
    if mood == "confused":
        line(ctx, -14, -100, 14, -104, color, 5)
    elif mood == "surprised" or beep > 0.2:
        circle(ctx, 0, -100, 7, color)
    else:
        ctx.move_to(-16, -104)
        ctx.curve_to(-8, -94, 8, -94, 16, -104)
        set_color(ctx, color)
        ctx.set_line_width(5)
        ctx.stroke()


def draw_cat(ctx: cairo.Context, x: float, y: float, s: float, t: float, talking: bool = False) -> None:
    """A friendly gray-blue cartoon cat sprite (our own design) standing at (x, y)."""
    bob = math.sin(t * 2.6) * 2
    ctx.save()
    ctx.translate(x, y + bob)
    safe_scale(ctx, s, s)
    shadow(ctx, 0, 6, 60, 10)
    body, stripe = "#7D93B2", "#5E7595"
    # tail
    ctx.move_to(48, -40)
    ctx.curve_to(110, -50, 100, -130, 70 + 8 * math.sin(t * 3), -140)
    set_color(ctx, body)
    ctx.set_line_width(16)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()
    fill_rounded(ctx, -50, -100, 100, 100, 40, body)
    for i in range(3):
        line(ctx, -20 + i * 20, -96, -14 + i * 20, -76, stripe, 6)
    # head
    for side in (-1, 1):  # ears
        ctx.move_to(side * 20, -170)
        ctx.line_to(side * 52, -214)
        ctx.line_to(side * 60, -160)
        ctx.close_path()
        set_color(ctx, body)
        ctx.fill()
    circle(ctx, 0, -150, 58, body)
    open_amount = blink(t, seed=2.7)
    for side in (-1, 1):
        ellipse(ctx, side * 22, -156, 9, max(12 * open_amount, 1.5), C["ink"])
    ellipse(ctx, 0, -136, 7, 5, C["pink"])
    if talking:
        ellipse(ctx, 0, -120, 9, 7 + 3 * math.sin(t * 18), "#5A1E1E")
    else:
        line(ctx, -10, -122, 0, -118, C["ink"], 4)
        line(ctx, 0, -118, 10, -122, C["ink"], 4)
    for side in (-1, 1):  # whiskers
        line(ctx, side * 18, -130, side * 56, -136, C["ink"], 2.5, 0.6)
        line(ctx, side * 18, -126, side * 56, -122, C["ink"], 2.5, 0.6)
    ctx.restore()


def draw_grown_up(ctx: cairo.Context, x: float, y: float, s: float, t: float) -> None:
    """A friendly adult silhouette icon (used for 'get a grown-up')."""
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, s, s)
    fill_rounded(ctx, -60, -170, 120, 170, 50, C["green"])
    circle(ctx, 0, -215, 52, "#9C6B4A")
    circle(ctx, -18, -222, 6, C["ink"])
    circle(ctx, 18, -222, 6, C["ink"])
    ctx.move_to(-18, -196)
    ctx.curve_to(-8, -184, 8, -184, 18, -196)
    set_color(ctx, C["ink"])
    ctx.set_line_width(5)
    ctx.stroke()
    ctx.restore()


__all__ = ["draw_nova", "draw_pixel", "draw_cat", "draw_grown_up", "rounded_rect"]
