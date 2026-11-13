"""The Kids Coding characters, drawn as simple vector shapes so they animate smoothly.

Rose: a ten-year-old inventor (an original cartoon). Long, straight dark-brown hair with a center
part, falling just past the shoulders; a light-blue headband; a purple long-sleeve top with lavender
stripes across the top of the shirt and the upper sleeves (the lower part stays plain).
Pixi: a palm-sized hovering helper robot with an LED face.
Both blink, bob gently while idle, and change expression; Rose's mouth follows the voice.

Rose is deliberately built from bold, rounded shapes rather than tiny details.  That keeps her
face recognisable in a 1280x720 video, in a small contact-sheet thumbnail, and when a child sees
her beside a code example.
"""

from __future__ import annotations

import math

import cairo

from .engine import C, blink, vertical_gradient, safe_scale, circle, clamp, ellipse, fill_rounded, glow, line, rounded_rect, set_color, shadow

# Moods: "happy", "talk", "surprised", "confused", "proud", "thinking", "worried"

# Rose's colors (the purple top keeps strong contrast with the warm workshop backgrounds).
ROSE = {
    "skin": "#E7AE85",
    "skin_shade": "#D2946C",
    "hair": "#3A2418",
    "hair_mid": "#4E3122",
    "hair_shine": "#7A5038",
    "band": "#6FAEE8",
    "band_dark": "#4C8FD0",
    "top": "#8B5CD6",
    "top_dark": "#7044BE",
    "stripe": "#D3BFF5",
    "pants": "#2C3E66",
    "eye": "#5B3520",
    "brow": "#2E1C12",
    "lip": "#D46A80",
    "mouth": "#7A2436",
}
# Rose's proportions: LIFT lengthens the legs and raises everything above them; TORSO lengthens the top.
# Together they make her about 470 px tall at s=1. Speech bubbles sit ROSE_HEAD_TOP above her feet.
LIFT, TORSO = 40, 15
ROSE_HEAD_TOP = 510


def _path(ctx, pts):
    """pts: start point then cubic segments ((c1x, c1y, c2x, c2y, x, y), ...)."""
    ctx.new_path()
    ctx.move_to(*pts[0])
    for seg in pts[1:]:
        if len(seg) == 2:
            ctx.line_to(*seg)
        else:
            ctx.curve_to(*seg)
    ctx.close_path()


def _fill(ctx, color, alpha=1.0):
    set_color(ctx, color, alpha)
    ctx.fill()


def draw_rose(ctx: cairo.Context, x: float, y: float, s: float, t: float, mood: str = "happy",
              talk: float = 0.0, wave: float = 0.0, point: float = 0.0, look: float = 0.0,
              hand_on_chin: float = 0.0) -> None:
    """Rose standing with feet at (x, y). s=1 is about 470 px tall.

    wave: 0-1 waving right arm; point: 0-1 right arm stretched out; look: -1 (left) .. 1 (right);
    hand_on_chin: 0-1 thinking pose with the left hand.
    """
    bob = math.sin(t * 2.2) * 3
    sway = math.sin(t * 1.7) * 2.5  # hair tips sway gently
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, s, s)
    shadow(ctx, 0, 0, 95, 16)
    # legs and shoes
    for side in (-1, 1):
        fill_rounded(ctx, side * 26 - 18, -120 - LIFT, 36, 112 + LIFT, 16, ROSE["pants"])
        fill_rounded(ctx, side * 30 - 30, -20, 60, 24, 12, C["white"], stroke=C["navy"], width=4)
        line(ctx, side * 30 - 22, -12, side * 30 + 22, -12, ROSE["top"], 4)  # shoe stripe matches the top
    ctx.translate(0, bob - LIFT)
    hx, hy = look * 6, -350
    # hair behind the body (the long back layer)
    _hair_back(ctx, hx, hy, sway)
    # body: purple long-sleeve top
    fill_rounded(ctx, -78, -270, 156, 170 + TORSO, 48, ROSE["top"])
    # stripes across the top of the shirt only (the lower part stays plain)
    ctx.save()
    rounded_rect(ctx, -78, -270, 156, 170 + TORSO, 48)
    ctx.clip()
    for i in range(3):
        ctx.rectangle(-80, -252 + i * 22, 160, 11)
        _fill(ctx, ROSE["stripe"])
    ctx.restore()
    line(ctx, -60, -108 + TORSO, 60, -108 + TORSO, ROSE["top_dark"], 5)  # hem
    # neck and a round neckline
    fill_rounded(ctx, hx - 20, hy + 62, 40, 50, 14, ROSE["skin_shade"])
    ctx.save()
    ctx.rectangle(-60, -272, 120, 30)
    ctx.clip()
    ellipse(ctx, hx * 0.5, -270, 30, 18, ROSE["skin_shade"])
    ctx.restore()
    ctx.new_sub_path()
    ctx.arc(hx * 0.5, -270, 31, math.radians(10), math.radians(170))
    set_color(ctx, ROSE["top_dark"])
    ctx.set_line_width(5)
    ctx.stroke()
    # head
    _face_shape(ctx, hx, hy)
    _hair_front(ctx, hx, hy, sway)
    _headband(ctx, hx, hy)
    _face(ctx, hx, hy, t, mood, talk, look)
    # arms last, in front of the hair: left (thinking pose bends to the chin), right (idle, wave or point)
    _arm(ctx, -70, -250, angle=_lerp(100, -14, hand_on_chin), bend=hand_on_chin)
    if point > 0:
        angle = _lerp(80, -12 + 3 * math.sin(t * 3), point)
    else:
        angle = _lerp(80, -55 + 22 * math.sin(t * 10), wave)
    _arm(ctx, 70, -250, angle=angle, bend=0.0)
    ctx.restore()


def _lerp(a, b, x):
    return a + (b - a) * clamp(x)


def _arm(ctx, sx, sy, angle, bend):
    """A sleeve from the shoulder at (sx, sy), angle in degrees (0 = right, 90 = down), striped near the top."""
    rad = math.radians(angle)
    length = 128 - 74 * bend  # the thinking pose rests the hand under the chin
    dx, dy = math.cos(rad), math.sin(rad)
    ex, ey = sx + length * dx, sy + length * dy
    line(ctx, sx, sy, ex, ey, ROSE["top"], 34)
    for a, b in ((0.16, 0.25), (0.34, 0.43), (0.52, 0.61)):
        line(ctx, sx + a * length * dx, sy + a * length * dy, sx + b * length * dx, sy + b * length * dy,
             ROSE["stripe"], 34, cap=cairo.LINE_CAP_BUTT)
    line(ctx, sx + 0.86 * length * dx, sy + 0.86 * length * dy, ex, ey, ROSE["top_dark"], 34, cap=cairo.LINE_CAP_BUTT)  # cuff
    circle(ctx, ex + 8 * dx, ey + 8 * dy, 19, ROSE["skin"])


def _hair_back(ctx, hx, hy, sway):
    """The long back layer: a dome behind the head and straight lengths down past the shoulders."""
    tip = hy + 150
    _path(ctx, [(hx, hy - 104),
                (hx + 70, hy - 104, hx + 106, hy - 60, hx + 106, hy + 20),
                (hx + 106, hy + 100, hx + 108 + sway, hy + 120, hx + 104 + sway, tip),
                (hx + 60, tip + 6),
                (hx - 60, tip + 6),
                (hx - 104 + sway, tip),
                (hx - 108 + sway, hy + 120, hx - 106, hy + 100, hx - 106, hy + 20),
                (hx - 106, hy - 60, hx - 70, hy - 104, hx, hy - 104)])
    _fill(ctx, ROSE["hair"])


def _face_shape(ctx, hx, hy):
    # A slightly wider, softer face reads more clearly at the small scale used in lesson scenes.
    _path(ctx, [(hx, hy - 86),
                (hx + 58, hy - 86, hx + 84, hy - 48, hx + 84, hy + 2),
                (hx + 84, hy + 56, hx + 46, hy + 94, hx, hy + 96),
                (hx - 46, hy + 94, hx - 84, hy + 56, hx - 84, hy + 2),
                (hx - 84, hy - 48, hx - 58, hy - 86, hx, hy - 86)])
    _fill(ctx, ROSE["skin"])


def _hair_front(ctx, hx, hy, sway):
    """Center part, hair swept to both sides over the temples, and long locks in front of the shoulders."""
    for side in (-1, 1):
        # top: from the part line, over the crown, down the side of the face
        _path(ctx, [(hx + side * 2, hy - 98),
                    (hx + side * 64, hy - 104, hx + side * 100, hy - 60, hx + side * 98, hy + 10),
                    (hx + side * 96, hy + 60, hx + side * 90, hy + 110, hx + side * 84, hy + 130),
                    (hx + side * 74, hy + 80, hx + side * 72, hy + 20, hx + side * 66, hy - 18),
                    (hx + side * 52, hy - 54, hx + side * 26, hy - 70, hx + side * 2, hy - 74)])
        _fill(ctx, ROSE["hair"])
        # the lock that falls in front of the shoulder to the chest (straight, tapered ends)
        tip_y = hy + 152
        _path(ctx, [(hx + side * 70, hy + 40),
                    (hx + side * 98, hy + 60, hx + side * 102, hy + 110, hx + side * (100 + sway), tip_y),
                    (hx + side * (92 + sway), tip_y - 18),
                    (hx + side * (80 + sway), tip_y + 4),
                    (hx + side * (68 + sway), tip_y - 22),
                    (hx + side * 64, hy + 120, hx + side * 60, hy + 80, hx + side * 70, hy + 40)])
        _fill(ctx, ROSE["hair"])
        # straight strand lines and a soft shine
        for k, top in ((84, hy + 56), (94, hy + 76)):
            line(ctx, hx + side * k, top, hx + side * (k + 4 + sway * 0.5), tip_y - 24, ROSE["hair_mid"], 3)
        ctx.new_path()
        ctx.move_to(hx + side * 14, hy - 92)
        ctx.curve_to(hx + side * 50, hy - 94, hx + side * 74, hy - 70, hx + side * 82, hy - 36)
        set_color(ctx, ROSE["hair_shine"], 0.8)
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()


def _headband(ctx, hx, hy):
    ctx.new_path()
    ctx.arc(hx, hy + 14, 96, math.radians(198), math.radians(342))
    set_color(ctx, ROSE["band"])
    ctx.set_line_width(17)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()
    ctx.new_path()
    ctx.arc(hx, hy + 14, 102, math.radians(215), math.radians(325))
    set_color(ctx, ROSE["band_dark"], 0.6)
    ctx.set_line_width(3)
    ctx.stroke()
    # Two small end tabs make the headband legible in profile and give the character a
    # distinctive, friendly silhouette without adding a texture-heavy accessory.
    for side in (-1, 1):
        fill_rounded(ctx, hx + side * 91 - 7, hy + 12, 14, 23, 6, ROSE["band_dark"])


def _face(ctx, hx, hy, t, mood, talk, look):
    open_amount = blink(t, seed=0.3)
    if mood == "surprised":
        open_amount = 1.0
    eye_y = hy + 6
    for side in (-1, 1):
        ex = hx + side * 32
        eh = 20 * open_amount + (4 if mood == "surprised" else 0)
        if open_amount > 0.25:
            ellipse(ctx, ex, eye_y, 18, max(eh, 1.5), C["white"])
            ix = ex + look * 5
            circle(ctx, ix, eye_y + 1, 13, ROSE["eye"])
            circle(ctx, ix, eye_y + 1, 6.5, "#1A0E08")
            circle(ctx, ix + 4.5, eye_y - 4.5, 4, C["white"])
            circle(ctx, ix - 4, eye_y + 5, 1.8, C["white"], 0.8)
            # upper lash line with a little flick at the outer corner
            ctx.new_path()
            ctx.move_to(ex - 17, eye_y - 2)
            ctx.curve_to(ex - 10, eye_y - eh - 2, ex + 10, eye_y - eh - 2, ex + 17, eye_y - 2)
            set_color(ctx, ROSE["brow"])
            ctx.set_line_width(4.5)
            ctx.set_line_cap(cairo.LINE_CAP_ROUND)
            ctx.stroke()
            line(ctx, ex + side * 16, eye_y - 4, ex + side * 22, eye_y - 9, ROSE["brow"], 4)
        else:  # closed: a soft curved line
            ctx.new_path()
            ctx.move_to(ex - 15, eye_y)
            ctx.curve_to(ex - 6, eye_y + 6, ex + 6, eye_y + 6, ex + 15, eye_y)
            set_color(ctx, ROSE["brow"])
            ctx.set_line_width(4)
            ctx.stroke()
        # eyebrows
        lift = {"surprised": -10, "worried": -4, "confused": -8 if side > 0 else 0, "thinking": -6}.get(mood, 0)
        tilt = {"worried": 5 * side, "confused": -5 * side if side > 0 else 0}.get(mood, 0)
        by = eye_y - 30 + lift
        ctx.new_path()
        ctx.move_to(ex - 17, by + 4 + tilt)
        ctx.curve_to(ex - 6, by - 4, ex + 6, by - 4, ex + 18, by + 3 - tilt)
        set_color(ctx, ROSE["brow"])
        ctx.set_line_width(6)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
    # nose
    ctx.new_path()
    ctx.move_to(hx + look * 4 - 6, hy + 34)
    ctx.curve_to(hx + look * 4 - 2, hy + 40, hx + look * 4 + 4, hy + 40, hx + look * 4 + 7, hy + 34)
    set_color(ctx, ROSE["skin_shade"])
    ctx.set_line_width(4)
    ctx.stroke()
    # cheeks
    circle(ctx, hx - 54, hy + 36, 15, "#F28CA0", 0.38)
    circle(ctx, hx + 54, hy + 36, 15, "#F28CA0", 0.38)
    # mouth
    my = hy + 56
    if talk > 0.05:
        ellipse(ctx, hx, my, 15 + 4 * talk, 4 + 14 * talk, ROSE["mouth"])
        ellipse(ctx, hx, my + 3 + 7 * talk, 8, 3 + 3 * talk, "#EE8A9A")
    elif mood == "surprised":
        ellipse(ctx, hx, my + 2, 10, 12, ROSE["mouth"])
    elif mood in ("confused", "worried", "thinking"):
        ctx.new_path()
        ctx.move_to(hx - 14, my + 3)
        ctx.curve_to(hx - 5, my - 3, hx + 5, my + 6, hx + 14, my)
        set_color(ctx, ROSE["mouth"])
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
    else:  # happy / proud: soft pink lips in a closed smile
        width = 22 if mood == "proud" else 19
        ctx.new_path()
        ctx.move_to(hx - width, my - 5)
        ctx.curve_to(hx - width / 2, my + 10, hx + width / 2, my + 10, hx + width, my - 5)
        ctx.curve_to(hx + width / 2, my + 3, hx - width / 2, my + 3, hx - width, my - 5)
        _fill(ctx, ROSE["lip"])
        ctx.new_path()
        ctx.move_to(hx - width, my - 5)
        ctx.curve_to(hx - width / 2, my + 4, hx + width / 2, my + 4, hx + width, my - 5)
        set_color(ctx, ROSE["mouth"])
        ctx.set_line_width(3.5)
        ctx.stroke()


def draw_pixi(ctx: cairo.Context, x: float, y: float, s: float, t: float, mood: str = "happy",
               carrying: bool = False, facing: float = 0.0, beep: float = 0.0, ground: float | None = None) -> None:
    """Pixi hovering with the bottom of its body near (x, y). s=1 is about 230 px tall.

    beep: 0-1 flashes the antenna and widens the eyes (use while Pixi beeps or speaks).
    ground: y of the floor for the shadow (defaults to just below Pixi).
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
    _pixi_face(ctx, t, mood, beep)
    ctx.restore()


def _pixi_face(ctx, t, mood, beep) -> None:
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



# ---------------------------------------------------------------------------------------------
# Aiden: the junior videos' on-screen scientist and builder, an eight-year-old coder drawn from the
# approved character sheet: a round friendly face, short brown hair with a soft dome, a short spiky
# fringe and a shine on top, big brown eyes, light-brown brows, a little hook nose, pink cheeks, an
# open smile, and a red hoodie (hood behind the neck, white drawstrings, a front pocket, ribbed cuffs).
AIDEN = {
    "skin": "#F4C69F",
    "skin_shade": "#E6AD84",
    "ear": "#EDB68C",
    "ear_in": "#CC8E64",
    "hair": "#865529",
    "hair_dark": "#6E4320",
    "hair_shine": "#B9875A",
    "shirt": "#D8352F",
    "shirt_dark": "#B32A27",
    "collar": "#9E2322",
    "string": "#F5EDE6",
    "pants": "#3B4254",
    "iris": "#7A4A26",
    "pupil": "#24140A",
    "lid": "#2A1A10",
    "brow": "#8B5A36",
    "nose": "#C98A62",
    "cheek": "#F2A08C",
    "mouth": "#8E3B32",
    "tongue": "#E7837A",
}
AIDEN_LIFT, AIDEN_TORSO = 18, 6
# Speech bubbles sit AIDEN_HEAD_TOP above his feet (s=1).
AIDEN_HEAD_TOP = 520


def draw_aiden(ctx: cairo.Context, x: float, y: float, s: float, t: float, mood: str = "happy",
               talk: float = 0.0, wave: float = 0.0, point: float = 0.0, look: float = 0.0,
               hand_on_chin: float = 0.0) -> None:
    """Aiden standing with feet at (x, y). s=1 is about 480 px tall. Same poses as draw_rose."""
    bob = math.sin(t * 2.4) * 3
    ctx.save()
    ctx.translate(x, y)
    safe_scale(ctx, s, s)
    shadow(ctx, 0, 0, 90, 15)
    for side in (-1, 1):  # legs and sneakers
        fill_rounded(ctx, side * 25 - 17, -116 - AIDEN_LIFT, 34, 108 + AIDEN_LIFT, 15, AIDEN["pants"])
        fill_rounded(ctx, side * 29 - 29, -20, 58, 24, 12, C["white"], stroke=C["navy"], width=4)
        line(ctx, side * 29 - 20, -12, side * 29 + 20, -12, AIDEN["shirt"], 4)
    ctx.translate(0, bob - AIDEN_LIFT)
    hx, hy = look * 5, -370
    # the hood lies behind the neck and shoulders
    _path(ctx, [(-70, -262), (-78, -312, -40, -330, 0, -330), (40, -330, 78, -312, 70, -262)])
    _fill(ctx, AIDEN["collar"])
    _path(ctx, [(-58, -264), (-62, -304, -32, -318, 0, -318), (32, -318, 62, -304, 58, -264)])
    _fill(ctx, AIDEN["shirt_dark"])
    # hoodie body: rounded shoulders, a little darker toward the ribbed hem, two soft fold lines
    fill_rounded(ctx, -82, -266, 164, 160 + AIDEN_TORSO, 52, AIDEN["shirt"])
    ctx.save()
    rounded_rect(ctx, -82, -266, 164, 160 + AIDEN_TORSO, 52)
    ctx.clip()
    vertical_gradient(ctx, -84, -230, 168, 140, AIDEN["shirt"], AIDEN["shirt_dark"])
    ctx.restore()
    for side in (-1, 1):
        line(ctx, side * 50, -236, side * 54, -150, AIDEN["shirt_dark"], 3, 0.7)
    # front pocket and the ribbed hem band
    fill_rounded(ctx, -46, -176, 92, 52, 16, AIDEN["shirt_dark"])
    line(ctx, -44, -176, 44, -176, AIDEN["collar"], 3, 0.6)
    ctx.save()
    rounded_rect(ctx, -82, -266, 164, 160 + AIDEN_TORSO, 52)
    ctx.clip()
    ctx.rectangle(-84, -122 + AIDEN_TORSO, 168, 22)
    _fill(ctx, AIDEN["collar"])
    ctx.restore()
    # neck and the hood's crossover neckline
    fill_rounded(ctx, hx - 22, hy + 70, 44, 50, 14, AIDEN["skin_shade"])
    ctx.new_path()
    ctx.move_to(hx * 0.4 - 34, -272)
    ctx.curve_to(hx * 0.4 - 26, -240, hx * 0.4 + 26, -240, hx * 0.4 + 34, -272)
    set_color(ctx, AIDEN["collar"])
    ctx.set_line_width(12)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()
    # two drawstrings with little tips
    for side in (-1, 1):
        sx = hx * 0.4 + side * 14
        line(ctx, sx, -250, sx + side * 2, -204, AIDEN["string"], 4)
        fill_rounded(ctx, sx + side * 2 - 3, -206, 6, 10, 3, AIDEN["string"])
    # ears
    for side in (-1, 1):
        ellipse(ctx, hx + side * 80, hy + 12, 13, 18, AIDEN["ear"])
        ellipse(ctx, hx + side * 81, hy + 12, 6, 10, AIDEN["ear_in"], 0.55)
    # face: wide forehead, round cheeks and chin
    _path(ctx, [(hx, hy - 78),
                (hx + 58, hy - 78, hx + 82, hy - 40, hx + 80, hy + 10),
                (hx + 78, hy + 58, hx + 46, hy + 92, hx, hy + 94),
                (hx - 46, hy + 92, hx - 78, hy + 58, hx - 80, hy + 10),
                (hx - 82, hy - 40, hx - 58, hy - 78, hx, hy - 78)])
    _fill(ctx, AIDEN["skin"])
    _aiden_hair(ctx, hx, hy)
    _aiden_face(ctx, hx, hy, t, mood, talk, look)
    # arms: short blue sleeves, then bare forearms
    _aiden_arm(ctx, -72, -246, angle=_lerp(100, -14, hand_on_chin), bend=hand_on_chin)
    if point > 0:
        angle = _lerp(80, -12 + 3 * math.sin(t * 3), point)
    else:
        angle = _lerp(80, -55 + 22 * math.sin(t * 10), wave)
    _aiden_arm(ctx, 72, -246, angle=angle, bend=0.0)
    ctx.restore()


def _aiden_arm(ctx, sx, sy, angle, bend):
    rad = math.radians(angle)
    length = 124 - 72 * bend
    dx, dy = math.cos(rad), math.sin(rad)
    ex, ey = sx + length * dx, sy + length * dy
    line(ctx, sx, sy, ex, ey, AIDEN["shirt"], 36)  # long hoodie sleeve
    line(ctx, sx + 0.86 * length * dx, sy + 0.86 * length * dy, ex, ey, AIDEN["collar"], 36,
         cap=cairo.LINE_CAP_BUTT)  # ribbed cuff
    circle(ctx, ex + 9 * dx, ey + 9 * dy, 18, AIDEN["skin"])


def _aiden_hair(ctx, hx, hy):
    """A soft dome over the top of the head, sides down to just above the ears, a short spiky
    fringe across the forehead, and a light shine near the top."""
    top = hy - 122
    fringe = [(-76, -38), (-62, -50), (-48, -36), (-32, -49), (-16, -37), (0, -50), (16, -37),
              (32, -49), (48, -36), (62, -50), (76, -38)]
    pts = [(hx - 100, hy + 6), (hx - 114, hy - 42, hx - 100, top + 4, hx, top),
           (hx + 100, top + 4, hx + 114, hy - 42, hx + 100, hy + 6),
           (hx + 86, hy + 2), (hx + 80, hy - 30)]
    for fx, fy in reversed(fringe):
        pts.append((hx + fx, hy + fy))
    pts.append((hx - 80, hy - 30))
    pts.append((hx - 86, hy + 2))
    _path(ctx, pts)
    _fill(ctx, AIDEN["hair"])
    # soft strokes into the fringe tufts, and the shine
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for fx, fy in fringe[1::2]:
        line(ctx, hx + fx * 0.9, hy - 74, hx + fx, hy + fy + 6, AIDEN["hair_dark"], 3, 0.5)
    ctx.new_path()
    ctx.move_to(hx - 46, top + 22)
    ctx.curve_to(hx - 20, top + 12, hx + 22, top + 12, hx + 46, top + 22)
    set_color(ctx, AIDEN["hair_shine"], 0.9)
    ctx.set_line_width(7)
    ctx.stroke()


def _aiden_face(ctx, hx, hy, t, mood, talk, look):
    open_amount = blink(t, seed=0.7)
    if mood == "surprised":
        open_amount = 1.0
    eye_y = hy + 6
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for side in (-1, 1):
        ex = hx + side * 30
        if open_amount > 0.25:
            eh = 14 * open_amount + (2 if mood == "surprised" else 0)
            ellipse(ctx, ex, eye_y, 15, max(eh, 1.5), C["white"])
            ix = ex + look * 4
            circle(ctx, ix, eye_y + 1, 10, AIDEN["iris"])
            circle(ctx, ix, eye_y + 1, 5, AIDEN["pupil"])
            circle(ctx, ix + 3.5, eye_y - 3, 3, C["white"])
            # thick upper lid with a little flick at the outer corner
            ctx.new_path()
            ctx.move_to(ex - 16, eye_y + 1)
            ctx.curve_to(ex - 9, eye_y - eh - 3, ex + 9, eye_y - eh - 3, ex + 16, eye_y + 1)
            set_color(ctx, AIDEN["lid"])
            ctx.set_line_width(4)
            ctx.stroke()
        else:
            ctx.new_path()
            ctx.move_to(ex - 15, eye_y)
            ctx.curve_to(ex - 6, eye_y + 6, ex + 6, eye_y + 6, ex + 15, eye_y)
            set_color(ctx, AIDEN["lid"])
            ctx.set_line_width(4)
            ctx.stroke()
        lift = {"surprised": -8, "worried": -3, "confused": -7 if side > 0 else 0, "thinking": -5}.get(mood, 0)
        tilt = {"worried": 5 * side, "confused": -5 * side if side > 0 else 0}.get(mood, 0)
        by = eye_y - 26 + lift
        ctx.new_path()
        ctx.move_to(ex - 16, by + 4 + tilt)
        ctx.curve_to(ex - 6, by - 4, ex + 6, by - 4, ex + 17, by + 2 - tilt)
        set_color(ctx, AIDEN["brow"])
        ctx.set_line_width(6)
        ctx.stroke()
    # a little hook nose
    nx = hx + look * 4
    ctx.new_path()
    ctx.move_to(nx - 2, hy + 18)
    ctx.curve_to(nx - 6, hy + 30, nx - 6, hy + 38, nx + 2, hy + 38)
    ctx.curve_to(nx + 6, hy + 38, nx + 6, hy + 34, nx + 4, hy + 32)
    set_color(ctx, AIDEN["nose"])
    ctx.set_line_width(3.5)
    ctx.stroke()
    ellipse(ctx, hx - 48, hy + 36, 15, 10, AIDEN["cheek"], 0.6)
    ellipse(ctx, hx + 48, hy + 36, 15, 10, AIDEN["cheek"], 0.6)
    my = hy + 52
    if talk > 0.05:
        ellipse(ctx, hx, my + 4, 16 + 4 * talk, 5 + 13 * talk, AIDEN["mouth"])
        ellipse(ctx, hx, my + 8 + 7 * talk, 9, 3 + 3 * talk, AIDEN["tongue"])
        fill_rounded(ctx, hx - 11, my - 1 - 8 * talk, 22, 5, 2, C["white"])
    elif mood == "surprised":
        ellipse(ctx, hx, my + 4, 10, 12, AIDEN["mouth"])
    elif mood in ("confused", "worried", "thinking"):
        ctx.new_path()
        ctx.move_to(hx - 14, my + 4)
        ctx.curve_to(hx - 5, my - 1, hx + 5, my + 7, hx + 14, my + 2)
        set_color(ctx, AIDEN["mouth"])
        ctx.set_line_width(4.5)
        ctx.stroke()
    else:  # the open smile from the character sheet: a crescent with a row of teeth
        w = 24 if mood == "proud" else 21
        ctx.new_path()
        ctx.move_to(hx - w, my)
        ctx.curve_to(hx - w / 2, my + 14, hx + w / 2, my + 14, hx + w, my)
        ctx.curve_to(hx + w / 2, my + 5, hx - w / 2, my + 5, hx - w, my)
        _fill(ctx, C["white"])
        ctx.new_path()
        ctx.move_to(hx - w - 3, my - 3)
        ctx.curve_to(hx - w / 2, my + 15, hx + w / 2, my + 15, hx + w + 3, my - 3)
        set_color(ctx, AIDEN["mouth"])
        ctx.set_line_width(3.5)
        ctx.stroke()
        ctx.new_path()
        ctx.move_to(hx - w + 2, my + 1)
        ctx.curve_to(hx - w / 2, my + 6, hx + w / 2, my + 6, hx + w - 2, my + 1)
        set_color(ctx, AIDEN["mouth"], 0.6)
        ctx.set_line_width(1.5)
        ctx.stroke()


__all__ = ["draw_rose", "draw_aiden", "draw_pixi", "draw_cat", "draw_grown_up", "rounded_rect"]
