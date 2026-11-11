"""Week 1 animation: 'Robots Need Exact Instructions'.

Every scene is a function of scene-local time t, timed by the beat cues in week01_script.py, so
pictures always land on the words that explain them.
"""

from __future__ import annotations

import math

from .. import props as P
from ..characters import ROSE_HEAD_TOP, draw_cat, draw_grown_up, draw_rose, draw_pixi
from ..engine import (
    C, FPS, H, W, appear, circle, clamp, ease_in_out, ease_out, fade, fill_rounded, glow, lerp, line,
    progress, set_color, star, text, vertical_gradient,
)
from ..timeline import ROSE, SceneTiming
from .week01_script import SCRIPTS

TITLE = "Robots Need Exact Instructions"
WEEK = 1


def _w(sc: SceneTiming, cue: str) -> tuple[float, float]:
    """(start, end) of a beat's window: from its first word to the next beat's first word."""
    start = sc.at(cue)
    names = [b.cue for b in sc.beats]
    i = names.index(cue)
    end = (sc.beats[i + 1].start - sc.start) if i + 1 < len(names) else sc.duration
    return start, end


def _f(sc: SceneTiming, cue: str, frac: float) -> float:
    """A moment `frac` of the way through a spoken beat."""
    return sc.at(cue) + frac * (sc.end_of(cue) - sc.at(cue))


def _tick_cues(start: float, end: float) -> list[float]:
    return [start + 0.4 + k for k in range(int(end - start - 0.4))]


# =============================================================================== scene 1
DOOR_X, FLOOR_Y = 1520, 900
CHAIR_X = 980


def scene1(ctx, t: float, sc: SceneTiming, gt: float) -> None:
    P.workshop(ctx, gt, floor_y=780)
    P.door(ctx, DOOR_X, FLOOR_Y, 230, 400, gt, locked=True)
    P.chair(ctx, CHAIR_X, FLOOR_Y, 1.0)
    # Rose slides in while waving
    rose_x = lerp(-200, 360, ease_out(progress(t, 0.0, 0.9)))
    mood, point, chin = "happy", 0.0, 0.0
    if t >= sc.at("take"):
        point = ease_out(progress(t, sc.at("take"), 0.3)) * (1 - progress(t, sc.at("zoom") + 0.6, 0.4))
    if t >= sc.at("exactly"):
        mood = "surprised"
    if t >= sc.at("notexact"):
        mood, chin = "thinking", ease_out(progress(t, sc.at("notexact"), 0.4))
    talk = sc.speaking(ROSE, t, FPS)
    wave = 1.0 if t < sc.end_of("meet") else 0.0
    draw_rose(ctx, rose_x, FLOOR_Y + 10, 1.0, gt, mood="talk" if talk > 0.05 else mood, talk=talk,
              wave=wave, point=point, look=0.6 if t > sc.at("zoom") else 0.2, hand_on_chin=chin)
    # Pixi drops in, carries the key, zooms to the chair, beeps proudly
    zoom_start, zoom_end = sc.at("zoom"), sc.end_of("zoom")
    px = lerp(640, CHAIR_X - 150, ease_in_out(progress(t, zoom_start + 0.2, zoom_end - zoom_start - 0.6)))
    drop = ease_out(progress(t, _f(sc, "meet", 0.45), 0.6))
    py = lerp(-260, 690, drop)
    pixi_mood = "happy"
    beep = 0.0
    if sc.at("beep") <= t < sc.end_of("beep") + 0.2:
        beep, pixi_mood = 1.0, "proud"
    elif t >= sc.end_of("beep") + 0.2:
        pixi_mood = "proud"
    carrying = sc.at("task") + 0.8 <= t < zoom_end - 0.3
    draw_pixi(ctx, px, py, 0.95, gt, mood=pixi_mood, carrying=carrying, beep=beep, ground=FLOOR_Y)
    # the glowing key: appears, floats to Pixi, rides along, then lands on the chair
    if t >= sc.at("task"):
        appear_amount = appear(t, sc.at("task"), 0.4)
        if t < sc.at("task") + 0.8:
            kx, ky = lerp(rose_x + 140, px, progress(t, sc.at("task") + 0.3, 0.5)), 560
        elif carrying:
            kx, ky = px, py - 115 + math.sin(gt * 3.1) * 7
        else:
            landing = ease_out(progress(t, zoom_end - 0.3, 0.4))
            kx, ky = lerp(px, CHAIR_X, landing), lerp(py - 115, FLOOR_Y - 128, landing)
        P.key(ctx, kx, ky, 1.1 * appear_amount, gt, glowing=True)
    # name tags
    P.chip(ctx, 360, FLOOR_Y + 70, "Rose", t, _f(sc, "meet", 0.05), color=C["white"], size=36)
    if t < zoom_start:
        P.chip(ctx, 640, FLOOR_Y + 70, "Pixi", t, _f(sc, "meet", 0.45), color=C["white"], size=36)
    # Rose's line and the mission
    P.speech_bubble(ctx, rose_x + 70, FLOOR_Y + 10 - ROSE_HEAD_TOP, "Take it over there!", t, sc.at("take"), sc.at("zoom") + 0.6)
    P.title_banner(ctx, "MISSION: Deliver the key", t, sc.at("task"), y=90)
    if t >= sc.at("exactly"):
        for i, dx in enumerate((-40, 20, 70)):
            amount = appear(t, sc.at("exactly") + i * 0.12, 0.3)
            text(ctx, "?", rose_x + dx, FLOOR_Y - 600 - 10 * math.sin(gt * 4 + i), 70, C["vermillion"], bold=True,
                 scale=amount, alpha=1 - progress(t, sc.at("question"), 0.3))
    q_start, q_end = _w(sc, "question")
    P.chip(ctx, W / 2, 205, "Pause: What exact steps would you give?", t, q_start, color=C["yellow"], size=40)
    P.thought_bubble(ctx, rose_x + 330, FLOOR_Y - 560, t, q_start + 0.8, q_end - 0.1)


def sfx1(sc: SceneTiming) -> list[tuple[float, str]]:
    a = sc.start
    events = [(a + 0.05, "whoosh"), (a + _f(sc, "meet", 0.45), "boing"), (a + sc.at("task"), "sparkle"),
              (a + sc.at("take"), "pop"), (a + sc.at("zoom") + 0.2, "zoom"), (a + sc.end_of("zoom") - 0.2, "pop"),
              (a + sc.at("beep") - 0.05, "beep_boop"), (a + sc.at("exactly"), "oops"), (a + sc.at("question"), "pop")]
    q_start, q_end = _w(sc, "question")
    events += [(a + k, "tick") for k in _tick_cues(sc.end_of("question"), q_end)]
    return events


# =============================================================================== scene 2
TILE, GX, GY, COLS, ROWS = 140, 150, 300, 5, 4


def _tile(col: float, row: float) -> tuple[float, float]:
    return GX + col * TILE + TILE / 2, GY + row * TILE + TILE / 2


PATH_OK = [((0, 3), 0), ((0, 0), 0), ((0, 0), 90), ((2, 0), 90)]  # (tile, heading in degrees: 0 = up, 90 = right)


def _pixi_on_grid(ctx, t, gt, col, row, heading, carrying, mood="happy", beep=0.0):
    x, y = _tile(col, row)
    # heading arrow under Pixi shows which way is "forward"
    ctx.save()
    ctx.translate(x, y + 30)
    ctx.rotate(math.radians(heading))
    ctx.move_to(0, -62)
    ctx.line_to(22, -30)
    ctx.line_to(-22, -30)
    ctx.close_path()
    set_color(ctx, C["orange"])
    ctx.fill()
    ctx.restore()
    draw_pixi(ctx, x, y + 40, 0.42, gt, mood=mood, carrying=carrying, beep=beep, ground=y + 58)
    if carrying:
        P.key(ctx, x, y - 22, 0.5, gt, glowing=False)


def _grid(ctx, door_open: float, door_ok: float, t, gt, key_at=None) -> None:
    fill_rounded(ctx, GX - 24, GY - 24, COLS * TILE + 48, ROWS * TILE + 48, 30, "#F1D9B8")
    for c in range(COLS):
        for r in range(ROWS):
            color = "#FBEBD5" if (c + r) % 2 == 0 else "#F3DDBF"
            fill_rounded(ctx, GX + c * TILE + 4, GY + r * TILE + 4, TILE - 8, TILE - 8, 14, color)
    text(ctx, "START", *_tile(0, 3.38), 26, C["gray"], bold=True)
    # the door on the right of tile (3, 0)
    dx, dy = _tile(3, 0)
    fill_rounded(ctx, dx - 50, dy - 64, 100, 128, 14, C["wood_dark"])
    fill_rounded(ctx, dx - 40, dy - 54, 80 * (1 - 0.7 * door_open), 108, 10, C["wood"])
    if door_open > 0:
        glow(ctx, dx, dy, 120, "#FFF2B3", 0.7 * door_open)
    text(ctx, "DOOR", dx, dy + 92, 28, C["navy"], bold=True)
    if key_at is not None:
        P.key(ctx, *key_at, 0.55, gt, glowing=False)


def _cards_positions(order: list[int]) -> dict[int, float]:
    return {step: 300 + slot * 118 for slot, step in enumerate(order)}


STEP_LABELS = {1: "Move forward 3", 2: "Turn right", 3: "Move forward 2", 4: "Put the key down"}


def scene2(ctx, t: float, sc: SceneTiming, gt: float) -> None:
    vertical_gradient(ctx, 0, 0, W, H, "#E8F5FF", "#FFF8EC")
    try_t = sc.at("try")
    intro_out = progress(t, try_t - 0.3, 0.5)
    # --- part A: computers are like Pixi (before "Let's try one")
    if intro_out < 1:
        alpha = 1 - intro_out
        ctx.save()
        ctx.push_group()
        draw_pixi(ctx, 620, 720, 1.1, gt, mood="confused" if t >= sc.at("mind") else "happy", ground=860)
        # a friendly laptop = Pixi
        lx, ly = 1180, 560
        laptop = appear(t, _f(sc, "secret", 0.4))
        if laptop > 0:
            ctx.save()
            ctx.translate(lx, ly)
            ctx.scale(laptop, laptop)
            fill_rounded(ctx, -170, -150, 340, 220, 20, C["navy"])
            fill_rounded(ctx, -150, -130, 300, 180, 12, C["sky_light"])
            for i in range(3):
                line(ctx, -110, -90 + i * 40, 60 - i * 30, -90 + i * 40, C["blue"], 12)
            fill_rounded(ctx, -220, 70, 440, 34, 14, C["gray"])
            ctx.restore()
            text(ctx, "=", 900, 560, 110, C["navy"], bold=True, scale=laptop)
        if t >= sc.at("mind"):
            P.thought_bubble(ctx, 860, 340, t, sc.at("mind"), sc.at("algo") + 0.2, label="???")
        if t < sc.at("algo_def"):
            P.chip(ctx, W / 2, 140, "Fast • Helpful • Not a mind reader", t, sc.at("mind"), size=40)
        ctx.pop_group_to_source()
        ctx.paint_with_alpha(alpha)
        ctx.restore()
    # definitions stay on screen at the top
    if t >= sc.at("algo_def"):
        P.chip(ctx, 560, 120, "Algorithm = exact steps", t, sc.at("algo_def"), color=C["orange_light"], size=44)
    if t >= sc.at("seq_def"):
        P.chip(ctx, 1290, 120, "Sequence = the order", t, sc.at("seq_def"), color=C["green_light"], size=44)
    if t < try_t - 0.3:
        return
    # --- part B: the grid run
    grid_in = ease_out(progress(t, try_t - 0.3, 0.6))
    ctx.save()
    ctx.translate(0, (1 - grid_in) * 60)
    swap_t, swap_end = _w(sc, "swap")
    order = [1, 2, 3, 4]
    reorder = ease_in_out(progress(t, swap_t + 0.2, 0.7))
    pos_a, pos_b = _cards_positions([1, 2, 3, 4]), _cards_positions([4, 1, 2, 3])
    # where is Pixi?
    s1, s1e = _w(sc, "s1")
    s2, s2e = _w(sc, "s2")
    s3, s3e = _w(sc, "s3")
    s4, s4e = _w(sc, "s4")
    col, row, heading, carrying, key_at, door_open, mood = 0, 3, 0, True, None, 0.0, "happy"
    if t < swap_t + 0.9:
        row = lerp(3, 0, ease_in_out(progress(t, s1 + 0.3, s1e - s1 - 0.4)))
        heading = lerp(0, 90, ease_in_out(progress(t, s2 + 0.3, 0.6)))
        col = lerp(0, 2, ease_in_out(progress(t, s3 + 0.3, s3e - s3 - 0.4)))
        if t >= s4 + 0.6:
            carrying = False
            landing = ease_out(progress(t, s4 + 0.6, 0.4))
            kx, ky = _tile(2.55, 0)
            key_at = (lerp(_tile(2, 0)[0], kx, landing), ky)
            door_open = ease_out(progress(t, s4 + 1.1, 0.6))
            mood = "proud"
    else:
        # wrong order: the key goes down first, at the start
        run0 = swap_t + 1.1
        heading = 0
        key_at = _tile(0.0, 3.0)
        carrying = False
        row = lerp(3, 0, ease_in_out(progress(t, run0 + 0.5, 0.8)))
        heading = lerp(0, 90, ease_in_out(progress(t, run0 + 1.4, 0.3)))
        col = lerp(0, 2, ease_in_out(progress(t, run0 + 1.8, 0.6)))
        mood = "confused" if t > run0 + 2.4 else "happy"
    _grid(ctx, door_open, 0, t, gt, key_at=key_at)
    _pixi_on_grid(ctx, t, gt, col, row, heading, carrying, mood=mood)
    # the four step cards
    current = None
    for cue, step in (("s1", 1), ("s2", 2), ("s3", 3), ("s4", 4)):
        a, b = _w(sc, cue)
        if a <= t < b and t < swap_t:
            current = step
    for step in order:
        y = lerp(pos_a[step], pos_b[step], reorder)
        start = sc.at(f"s{step}")
        active = 1.0 if current == step else 0.0
        done = t >= _w(sc, f"s{step}")[1] - 0.2 and t < swap_t
        P.step_card(ctx, 1040, y, 720, step, STEP_LABELS[step], t, start, active=active, done=done)
    if t >= sc.at("worked") and t < swap_t:
        P.badge(ctx, _tile(3, 0)[0], _tile(3, 0)[1] - 110, 40, True, t, sc.at("worked") - 0.2)
        P.confetti(ctx, _tile(3, 0)[0], _tile(3, 0)[1], t, sc.at("worked"))
    if t >= swap_t + 3.4:
        P.badge(ctx, _tile(3, 0)[0], _tile(3, 0)[1] - 110, 40, False, t, swap_t + 3.4)
    ctx.restore()
    # Rose cheers "It worked!" from the corner
    rose_in = appear(t, sc.at("worked") - 0.3) * (1 - progress(t, swap_t, 0.4))
    if rose_in > 0:
        talk = sc.speaking(ROSE, t, FPS)
        draw_rose(ctx, 1700, 1180 - 230 * rose_in, 0.55, gt, mood="talk" if talk > 0.05 else "happy", talk=talk, wave=1.0)
    if t >= sc.at("different"):
        P.chip(ctx, 1400, 860, "Same steps + new order = new result", t, sc.at("different"), color=C["white"], size=36)
    if t >= sc.at("matters"):
        amount = appear(t, sc.at("matters"), 0.5)
        ctx.save()
        ctx.translate(W / 2, 980)
        ctx.scale(amount, amount)
        fill_rounded(ctx, -330, -60, 660, 120, 60, C["vermillion"])
        text(ctx, "Order matters!", 0, 0, 64, C["white"], bold=True)
        ctx.restore()


def sfx2(sc: SceneTiming) -> list[tuple[float, str]]:
    a = sc.start
    swap_t, _ = _w(sc, "swap")
    events = [(a + _f(sc, "secret", 0.4), "pop"), (a + sc.at("mind"), "boing"), (a + sc.at("algo_def"), "pop"),
              (a + sc.at("seq_def"), "pop"), (a + sc.at("try") - 0.3, "whoosh")]
    for cue in ("s1", "s2", "s3", "s4"):
        events.append((a + sc.at(cue), "pop"))
    events += [(a + sc.at("s4") + 1.1, "door"), (a + sc.at("worked"), "chime"), (a + swap_t + 0.2, "whoosh"),
               (a + swap_t + 1.1, "snap"), (a + swap_t + 3.4, "oops"), (a + sc.at("matters"), "sparkle")]
    return events


# =============================================================================== scene 3
WIN = (120, 150, 1680, 820)  # editor window x, y, w, h
CODE_X, CODE_Y = 560, 330
STAGE = (1240, 300, 500, 380)


def _editor(ctx, t, sc, gt, highlight: str = "") -> None:
    x, y, w, h = WIN
    fill_rounded(ctx, x + 8, y + 12, w, h, 30, "#000000", 0.12)
    fill_rounded(ctx, x, y, w, h, 30, C["white"], stroke=C["navy"], width=5)
    fill_rounded(ctx, x, y, w, 80, 30, C["navy"])
    ctx.rectangle(x, y + 50, w, 30)
    set_color(ctx, C["navy"])
    ctx.fill()
    text(ctx, "Scratch (offline app)", x + 40, y + 42, 34, C["white"], bold=True, anchor="left")
    # block categories (word + color dot, never color alone)
    cats = [("Motion", "#4C97FF"), ("Looks", "#9966FF"), ("Sound", "#CF63CF"), ("Events", C["yellow"]),
            ("Control", "#FFAB19")]
    for i, (name, color) in enumerate(cats):
        cy = y + 140 + i * 92
        circle(ctx, x + 70, cy, 26, color)
        text(ctx, name, x + 110, cy, 32, C["ink"], bold=True, anchor="left")
    if highlight == "cats":
        fill_rounded(ctx, x + 24, y + 96, 300, 470, 22, C["yellow"], 0.25, stroke=C["orange"], width=6)
    # code area
    fill_rounded(ctx, CODE_X - 30, y + 100, 640, h - 130, 20, "#F4F6FA",
                 stroke=C["yellow"] if highlight == "code" else None, width=8)
    for gx in range(CODE_X, CODE_X + 600, 40):
        for gy in range(y + 120, y + h - 40, 40):
            circle(ctx, gx, gy, 2, "#D5DBE5")
    # stage
    sx, sy, sw, sh = STAGE
    fill_rounded(ctx, sx - 10, sy - 10, sw + 20, sh + 20, 24, C["yellow"] if highlight == "stage" else C["gray_light"])
    vertical_gradient(ctx, sx, sy, sw, sh, "#DFF3FF", "#FFFFFF")
    fill_rounded(ctx, sx, sy + sh - 70, sw, 70, 0, "#BFE3B4")


def scene3(ctx, t: float, sc: SceneTiming, gt: float) -> None:
    vertical_gradient(ctx, 0, 0, W, H, "#F0EAFF", "#FFF8EC")
    zoom = ease_out(progress(t, 0, 0.7))
    ctx.save()
    ctx.translate(W / 2, H / 2)
    ctx.scale(0.85 + 0.15 * zoom, 0.85 + 0.15 * zoom)
    ctx.translate(-W / 2, -H / 2)
    highlight = ""
    if _w(sc, "stage")[0] <= t < _w(sc, "stage")[1]:
        highlight = "stage"
    elif sc.at("code") <= t < _f(sc, "code", 0.45):
        highlight = "cats"
    elif _f(sc, "code", 0.45) <= t < _w(sc, "code")[1]:
        highlight = "code"
    _editor(ctx, t, sc, gt, highlight)
    sx, sy, sw, sh = STAGE
    # green flag button above the stage
    run_t = sc.at("run")
    pressed = 1.0 if run_t <= t < run_t + 0.25 else 0.0
    flag_pulse = 1 + 0.12 * math.sin(gt * 8) if _w(sc, "flag")[0] <= t < _w(sc, "flag")[1] else 1
    ctx.save()
    ctx.translate(sx + 50, sy - 50)
    ctx.scale(flag_pulse, flag_pulse)
    P.green_flag_button(ctx, 0, 0, 34, pressed)
    ctx.restore()
    # the cat: speaks, then moves ten steps
    say_start, move_start = run_t + 0.4, run_t + 2.4
    cat_x = sx + 170 + 90 * ease_in_out(progress(t, move_start, 0.7))
    sprite_bounce = 1 + 0.08 * math.sin(progress(t, sc.at("sprite"), 0.8) * math.pi) if t >= sc.at("sprite") else 1
    draw_cat(ctx, cat_x, sy + sh - 30, 0.85 * sprite_bounce, gt, talking=say_start <= t < move_start)
    P.speech_bubble(ctx, cat_x + 30, sy + sh - 230, "Hello, coder!", t, say_start, move_start, size=32, max_width=300)
    # blocks fly in and snap
    blocks = [("b1", "event", ["when", "{flag}", "clicked"], True), ("b2", "looks", ["say", "[Hello, coder!]", "for", "[2]", "seconds"], False),
              ("b3", "motion", ["move", "[10]", "steps"], False)]
    y = CODE_Y
    for index, (cue, kind, parts, hat) in enumerate(blocks):
        start = sc.at(cue)
        if t >= start:
            fly = ease_out(progress(t, start, 0.5))
            bx = lerp(170, CODE_X, fly)
            by = lerp(WIN[1] + 140, y, fly)
            highlight_amount = 0.0
            if index == 0 and run_t <= t < say_start:
                highlight_amount = 1.0
            if index == 1 and say_start <= t < move_start:
                highlight_amount = 1.0
            if index == 2 and move_start <= t < move_start + 0.9:
                highlight_amount = 1.0
            P.code_block(ctx, bx, by, kind, parts, highlight=highlight_amount, hat=hat, scale=0.88)
        y += 76 if hat else 70
    # top-to-bottom arrow
    if t >= sc.at("topdown"):
        amount = progress(t, sc.at("topdown"), 0.9)
        ax = CODE_X + 620
        line(ctx, ax, CODE_Y + 10, ax, CODE_Y + 10 + 220 * ease_out(amount), C["vermillion"], 12)
        if amount > 0.95:
            ctx.move_to(ax - 22, CODE_Y + 210)
            ctx.line_to(ax + 22, CODE_Y + 210)
            ctx.line_to(ax, CODE_Y + 246)
            ctx.close_path()
            set_color(ctx, C["vermillion"])
            ctx.fill()
    ctx.restore()
    # labels (spec on-screen text), placed where they point
    if t < sc.at("code"):
        P.chip(ctx, sx + 190, 120, "Stage = action area", t, sc.at("stage"), color=C["orange_light"], size=38)
    if t < sc.at("code"):
        P.chip(ctx, sx + 160, 1000, "Sprite = character or object", t, sc.at("sprite"), color=C["green_light"], size=38)
    if sc.at("code") <= t < sc.at("b1"):
        P.chip(ctx, 880, 1000, "Code area: snap blocks into a script", t, sc.at("code"), size=38)
    if sc.at("topdown") <= t < sc.at("run"):
        P.chip(ctx, 880, 1000, "Read blocks top → bottom", t, sc.at("topdown"), color=C["yellow"], size=40)
    first_start, first_end = _w(sc, "first")
    P.thought_bubble(ctx, cat_x + 180, sy + 40, t, first_start + 0.5, first_end - 0.1, label="Speak or move?")
    if t >= run_t + 3.3:
        P.badge(ctx, 1600, 900, 46, True, t, run_t + 3.3)


def sfx3(sc: SceneTiming) -> list[tuple[float, str]]:
    a = sc.start
    events = [(a + 0.05, "whoosh"), (a + sc.at("stage"), "pop"), (a + sc.at("sprite"), "boing"),
              (a + sc.at("code"), "pop"), (a + sc.at("flag"), "pop")]
    for cue in ("b1", "b2", "b3"):
        events.append((a + sc.at(cue) + 0.45, "snap"))
    first_start, first_end = _w(sc, "first")
    events += [(a + k, "tick") for k in _tick_cues(sc.end_of("first"), first_end)]
    run_t = sc.at("run")
    events += [(a + run_t, "pop"), (a + run_t + 2.4, "zoom"), (a + run_t + 3.3, "chime")]
    return events


# =============================================================================== scene 4
def scene4(ctx, t: float, sc: SceneTiming, gt: float) -> None:
    vertical_gradient(ctx, 0, 0, W, H, "#EAF7F1", "#FFF8EC")
    banner = appear(t, 0.1, 0.5) * (1 - progress(t, sc.at("builds"), 0.4))
    if banner > 0:
        ctx.save()
        ctx.translate(W / 2, H / 2 - 40)
        ctx.scale(banner * 1.4, banner * 1.4)
        fill_rounded(ctx, -330, -90, 660, 180, 50, C["navy"])
        text(ctx, "BUG HUNT!", 40, 0, 96, C["yellow"], bold=True)
        P.magnifier(ctx, -220, -10, 0.7, gt)
        ctx.restore()
    if t < sc.at("builds") - 0.1:
        return
    show = ease_out(progress(t, sc.at("builds") - 0.1, 0.6))
    ctx.save()
    ctx.translate(0, (1 - show) * 80)
    # code panel on the left
    fill_rounded(ctx, 100, 200, 820, 520, 30, C["white"], stroke=C["navy"], width=5)
    text(ctx, "Rose's script", 140, 250, 36, C["navy"], bold=True, anchor="left")
    move_t = sc.at("move")
    swap = ease_in_out(progress(t, move_t + 0.2, 0.8))
    slot = lambda i: 400 + i * 80  # noqa: E731
    thanks_y = lerp(slot(0), slot(1), swap)
    welcome_y = lerp(slot(1), slot(0), swap)
    lift = math.sin(swap * math.pi) * 40
    # when the script runs: before the fix and after it
    run1 = sc.at("blocks") + 0.2
    run2 = sc.at("works") - 1.4  # the fixed script runs just before Rose says it works
    blocks_cue_end = _w(sc, "blocks")[1]
    hl_thanks = hl_welcome = 0.0
    bubble = None
    if run1 <= t < run1 + 1.6:
        hl_thanks, bubble = 1.0, ("Thanks for watching!", run1, run1 + 1.6)
    elif run1 + 1.6 <= t < run1 + 3.4:
        hl_welcome, bubble = 1.0, ("Welcome to my show!", run1 + 1.6, run1 + 3.4)
    if run2 <= t < run2 + 1.5:
        hl_welcome, bubble = 1.0, ("Welcome to my show!", run2, run2 + 1.5)
    elif run2 + 1.5 <= t < run2 + 3.0:
        hl_thanks, bubble = 1.0, ("Thanks for watching!", run2 + 1.5, run2 + 3.0)
    # reading with a finger (detective step three)
    d3, d3_end = _w(sc, "d3")
    if d3 <= t < d3_end:
        k = (t - d3) / (d3_end - d3)
        reading = min(int(k * 3), 2)
        if reading == 1:
            hl_thanks = 0.6
        elif reading == 2:
            hl_welcome = 0.6
        P.pointer_hand(ctx, 720, 320 + reading * 80 + 38, 1.0)
    which, which_end = sc.at("which"), _w(sc, "pause")[1]
    pulse = (0.5 + 0.5 * math.sin(gt * 6)) if which <= t < which_end else 0.0
    P.code_block(ctx, 160, 320, "event", ["when", "{flag}", "clicked"], hat=True, highlight=1.0 if run1 - 0.2 <= t < run1 or run2 - 0.2 <= t < run2 else 0.0)
    P.code_block(ctx, 160 + (lift if swap < 1 else 0) * 0.3, thanks_y, "looks", ["say", "[Thanks for watching!]"], highlight=max(hl_thanks, pulse))
    P.code_block(ctx, 160 - (lift if swap < 1 else 0) * 0.3, welcome_y, "looks", ["say", "[Welcome to my show!]"], highlight=max(hl_welcome, pulse))
    # the little stage on the right
    stage_x, stage_y, stage_w, stage_h = 1020, 190, 800, 330
    fill_rounded(ctx, stage_x, stage_y, stage_w, stage_h, 30, "#3B2A4A")
    fill_rounded(ctx, stage_x + 20, stage_y + 20, stage_w - 40, stage_h - 40, 20, "#FFF1D6")
    for side in (0, 1):  # curtains
        cx = stage_x + 20 + side * (stage_w - 140)
        fill_rounded(ctx, cx, stage_y + 20, 100, stage_h - 40, 20, C["vermillion"])
    fill_rounded(ctx, stage_x + 20, stage_y + stage_h - 70, stage_w - 40, 50, 10, C["wood"])
    pixi_mood = "happy"
    if blocks_cue_end - 2.0 <= t < sc.at("works") - 1.4 and not bubble:
        pixi_mood = "confused"
    draw_pixi(ctx, stage_x + stage_w / 2, stage_y + stage_h - 90, 0.62, gt, mood=pixi_mood,
               beep=1.0 if bubble else 0.0, ground=stage_y + stage_h - 60)
    if bubble:
        P.speech_bubble(ctx, stage_x + stage_w / 2, stage_y + 150, bubble[0], t, bubble[1], bubble[2] - 0.15,
                        size=34, tail="down")
    ctx.restore()
    # Rose reacts at the bottom left
    talk = sc.speaking(ROSE, t, FPS)
    mood = "happy"
    if sc.at("backwards") - 0.6 <= t < sc.at("right"):
        mood = "confused"
    if t >= sc.at("works") - 0.2:
        mood = "proud"
    draw_rose(ctx, 300, 1075, 0.62, gt, mood="talk" if talk > 0.05 else mood, talk=talk,
              hand_on_chin=1.0 if mood == "confused" else 0.0, wave=1.0 if t >= sc.at("works") else 0.0)
    # detective steps (two columns under the stage)
    labels = ["What did we expect?", "What happened?", "Read one block at a time", "Change one thing. Test."]
    for i, label in enumerate(labels):
        cue = f"d{i + 1}"
        a, b = _w(sc, cue)
        active = 1.0 if a <= t < b else 0.0
        if t < sc.at("works") - 1.6:
            P.step_card(ctx, 980, 555 + i * 100, 860, i + 1, label, t, a, active=active, color=C["green"], size=34)
    pause_t, pause_end = _w(sc, "pause")
    P.thought_bubble(ctx, 620, 860, t, pause_t + 0.4, pause_end - 0.1, label="Which two swap?")
    if t >= sc.at("works") - 1.4 + 3.0:
        P.badge(ctx, 1420, 760, 56, True, t, sc.at("works") + 1.6)
        P.confetti(ctx, 1420, 700, t, sc.at("works") + 1.6)
    if t >= sc.at("clue"):
        amount = appear(t, sc.at("clue"), 0.5)
        ctx.save()
        ctx.translate(1380, 980)
        ctx.scale(amount, amount)
        fill_rounded(ctx, -460, -54, 920, 108, 54, C["navy"])
        text(ctx, "A bug is a clue, not a reason to quit.", 0, 0, 40, C["white"], bold=True)
        ctx.restore()


def sfx4(sc: SceneTiming) -> list[tuple[float, str]]:
    a = sc.start
    run1 = sc.at("blocks") + 0.2
    run2 = sc.at("works") - 1.4
    events = [(a + 0.1, "boing"), (a + sc.at("builds") - 0.1, "whoosh"), (a + run1, "pop"), (a + run1 + 1.6, "pop"),
              (a + sc.at("backwards") - 0.4, "oops")]
    for i in range(4):
        events.append((a + sc.at(f"d{i + 1}"), "pop"))
    pause_t, pause_end = _w(sc, "pause")
    events += [(a + k, "tick") for k in _tick_cues(sc.end_of("pause"), pause_end)]
    events += [(a + sc.at("move") + 0.2, "whoosh"), (a + sc.at("move") + 1.0, "snap"), (a + run2, "pop"),
               (a + run2 + 1.5, "pop"), (a + sc.at("works") + 1.6, "chime"), (a + sc.at("clue"), "sparkle")]
    return events


# =============================================================================== scene 5
def scene5(ctx, t: float, sc: SceneTiming, gt: float) -> None:
    P.workshop(ctx, gt, floor_y=800)
    opened = ease_out(progress(t, 0.3, 1.2))
    P.door(ctx, 1520, 920, 230, 400, gt, opened=opened, locked=opened < 0.2, label="DOOR 1")
    if opened > 0.5:
        for i in range(6):
            a = gt * 1.5 + i
            star(ctx, 1635 + 180 * math.cos(a), 700 + 120 * math.sin(a), 10, C["yellow"], 0.8, rotation=gt)
    talk = sc.speaking(ROSE, t, FPS)
    cheer = t < sc.at("remember") or t >= sc.at("happy")
    draw_rose(ctx, 260, 1010, 0.72, gt, mood="proud" if cheer else "happy", wave=1.0 if cheer else 0.0, talk=talk)
    draw_pixi(ctx, 470, 860, 0.62, gt, mood="proud" if cheer else "happy", ground=1000)
    # recap chips
    r_items = [("r1", "Exact steps = algorithm", C["orange_light"]), ("r2", "Order = sequence", C["green_light"]),
               ("r3", "Top → bottom", C["sky_light"])]
    recap_out = progress(t, sc.at("nick") - 0.4, 0.4)
    if recap_out < 1:
        for i, (cue, label, color) in enumerate(r_items):
            ctx.save()
            ctx.translate(0, -recap_out * 40)
            P.chip(ctx, 900, 260 + i * 130, label, t, sc.at(cue), color=color, size=46)
            ctx.restore()
        if t >= sc.at("remember"):
            P.title_banner(ctx, "Let's remember", t, sc.at("remember"), y=110)
    # privacy: nickname yes, personal details no
    priv_in, priv_out = sc.at("nick"), sc.at("next") - 0.3
    if priv_in <= t < priv_out + 0.4:
        alpha = 1 - progress(t, priv_out, 0.4)
        ctx.save()
        ctx.push_group()
        card = appear(t, priv_in)
        ctx.save()
        ctx.translate(900, 300)
        ctx.scale(card, card)
        fill_rounded(ctx, -260, -90, 520, 180, 30, C["white"], stroke=C["green"], width=6)
        draw_pixi(ctx, -170, 40, 0.38, gt, mood="happy", ground=60)
        text(ctx, "StarCoder", 40, -20, 54, C["navy"], bold=True)
        text(ctx, "my coding nickname", 40, 40, 30, C["green"], bold=True)
        ctx.restore()
        P.badge(ctx, 1140, 230, 30, True, t, priv_in + 0.5)
        never = ["Full name", "School", "Address", "Birthday", "Photos"]
        for i, label in enumerate(never):
            start = _f(sc, "never", 0.1 + i * 0.17)
            x = 640 + (i % 3) * 300
            y = 500 + (i // 3) * 110
            width = P.chip(ctx, x, y, label, t, start, color=C["white"], ink=C["ink"], size=38)
            if t >= start + 0.25:
                amount = ease_out(progress(t, start + 0.25, 0.25))
                half = width / 2 - 18
                line(ctx, x - half, y, x - half + 2 * half * amount, y, C["vermillion"], 9)
        P.chip(ctx, 900, 760, "Offline app • No account", t, sc.at("offline"), color=C["sky_light"], size=40)
        if t >= sc.at("grownup"):
            gin = appear(t, sc.at("grownup"))
            draw_grown_up(ctx, 1290, 1000, 0.75 * gin, gt)
            P.chip(ctx, 1290, 1040, "Stop • Get a grown-up", t, sc.at("grownup") + 0.3, color=C["yellow"], size=36)
        ctx.pop_group_to_source()
        ctx.paint_with_alpha(alpha)
        ctx.restore()
    # next activity: Hello, Cat!
    if t >= sc.at("next"):
        P.title_banner(ctx, "NEXT: Hello, Cat!", t, sc.at("next"), y=110, color=C["green"])
        steps = ["Say hello", "Walk", "Meow", "Say bye"]
        steps_t = sc.at("steps")
        first_t, first_end = _w(sc, "firstlast")
        for i, label in enumerate(steps):
            start = _f(sc, "steps", 0.15 + i * 0.2)
            active = 1.0 if first_t <= t < first_end and i in (0, 3) else 0.0
            P.step_card(ctx, 700, 230 + i * 112, 620, i + 1, label, t, start, active=active, color=C["purple"])
        draw_cat(ctx, 1150, 780, 0.7 * appear(t, sc.at("next")), gt, talking=steps_t <= t < sc.end_of("steps"))
        if t >= sc.at("click"):
            P.green_flag_button(ctx, 1010, 720, 40, 1.0 if sc.at("click") <= t < sc.at("click") + 0.3 else 0.0)
        if first_t <= t < first_end:
            P.chip(ctx, 1010, 900, "First? Last?", t, first_t + 0.2, color=C["yellow"], size=40)
    if t >= sc.at("happy"):
        P.chip(ctx, 1010, 900, "Happy coding!", t, sc.at("happy"), color=C["orange_light"], size=48)


def sfx5(sc: SceneTiming) -> list[tuple[float, str]]:
    a = sc.start
    events = [(a + 0.3, "door"), (a + sc.at("remember"), "pop")]
    for cue in ("r1", "r2", "r3"):
        events.append((a + sc.at(cue), "pop"))
    events += [(a + sc.at("nick"), "pop"), (a + sc.at("nick") + 0.5, "chime")]
    for i in range(5):
        events.append((a + _f(sc, "never", 0.1 + i * 0.17) + 0.25, "tick"))
    events += [(a + sc.at("offline"), "pop"), (a + sc.at("grownup"), "pop"), (a + sc.at("next"), "sparkle"),
               (a + sc.at("click"), "pop"), (a + sc.at("happy"), "chime")]
    for i in range(4):
        events.append((a + _f(sc, "steps", 0.15 + i * 0.2), "pop"))
    return events


# =============================================================================== intro and outro
INTRO, OUTRO = 4.6, 5.0


def intro(ctx, t: float, gt: float) -> None:
    vertical_gradient(ctx, 0, 0, W, H, "#18324B", "#25507A")
    for i in range(40):
        x = (i * 397) % W
        y = (i * 211) % H
        star(ctx, x, y, 4 + (i % 3) * 2, C["white"], 0.25 + 0.25 * math.sin(gt * 2 + i), rotation=gt * 0.3)
    P.logo(ctx, W / 2, H / 2 - 80, 1.0, t, 0.2)
    sub = fade(t, 1.6, 0.5)
    if sub > 0:
        fill_rounded(ctx, W / 2 - 520, H / 2 + 150, 1040, 110, 55, C["white"], sub)
        text(ctx, f"Week {WEEK}: {TITLE}", W / 2, H / 2 + 205, 52, C["navy"], bold=True, alpha=sub)
    draw_pixi(ctx, 260, 980 + 40 * (1 - ease_out(progress(t, 0.6, 0.8))), 0.6, gt, mood="happy", ground=1040)
    draw_rose(ctx, 1660, 1110 - 120 * ease_out(progress(t, 0.9, 0.8)), 0.6, gt, mood="happy", wave=1.0)


def outro(ctx, t: float, gt: float) -> None:
    vertical_gradient(ctx, 0, 0, W, H, "#18324B", "#25507A")
    P.logo(ctx, W / 2, 360, 0.75, t, 0.0)
    a = fade(t, 0.4)
    text(ctx, "See you next time!", W / 2, 640, 56, C["white"], bold=True, alpha=a)
    text(ctx, "Narration uses AI-generated voices.", W / 2, 790, 38, C["led"], bold=True, alpha=a)
    text(ctx, "Kids Coding • Level 1 • Grades 4–5", W / 2, 860, 32, "#C9D6E3", alpha=a)
    draw_pixi(ctx, 300, 980, 0.55, gt, mood="proud", ground=1040)
    draw_rose(ctx, 1640, 1080, 0.55, gt, mood="happy", wave=1.0)


SCENES = [scene1, scene2, scene3, scene4, scene5]
SFX = [sfx1, sfx2, sfx3, sfx4, sfx5]
