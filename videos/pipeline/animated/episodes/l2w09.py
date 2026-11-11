"""Level 2 Week 9: Event-Driven Games (kit episode)."""

from ..kit_dsl import A, B, Episode, Scene

# ----------------------------------------------------------------------------- turtle frames
# Key presses and timers do not fire in a video, so each game frame is its own small turtle
# program that sets up the scene exactly as try_keys.py would look at that moment. The player is
# the first turtle (drawn as the turtle cursor); the ball is drawn as a dot.


def marker(name: str, x: float, y: float, heading: float, size: float = 2.6) -> str:
    """Trace a filled turtle-cursor shape around (x, y) so the player is easy to see."""
    import math

    shape = [(16, 0), (-12, -11), (-6, 0), (-12, 11), (16, 0)]
    a = math.radians(heading)
    pts = [(round(x + size * (px * math.cos(a) - py * math.sin(a)), 1),
            round(y + size * (px * math.sin(a) + py * math.cos(a)), 1)) for px, py in shape]
    lines = [f"{name}.goto{pts[0]}", f'{name}.color("green")', f"{name}.begin_fill()"]
    lines += [f"{name}.goto{p}" for p in pts[1:]]
    lines += [f"{name}.end_fill()", f"{name}.goto({x}, {y})"]
    return "\n".join(lines) + "\n"


def game_frame(ball_y: int, player_x: int = 0) -> str:
    return (
        "import turtle\n"
        "screen = turtle.Screen()\n"
        'player = turtle.Turtle("turtle")\n'
        "player.penup()\n"
        + marker("player", player_x, 0, 0)
        + 'ball = turtle.Turtle("circle")\n'
        "ball.hideturtle()\n"
        "ball.penup()\n"
        f"ball.goto(0, {ball_y})\n"
        'ball.dot(30, "orange")\n'
    )


def spin_frame(spins: int) -> str:
    return (
        "import turtle\n"
        "screen = turtle.Screen()\n"
        'player = turtle.Turtle("turtle")\n'
        "player.penup()\n"
        + "player.left(90)\n" * spins
        + marker("player", 0, 0, 90 * spins, 3.2)
        + "label = turtle.Turtle()\n"
        "label.hideturtle()\n"
        "label.penup()\n"
        "label.goto(0, 150)\n"
        'label.write("Press r to spin", align="center")\n'
    )


def touch_frame(gap: int) -> str:
    return (
        "import turtle\n"
        "a = turtle.Turtle()\n"
        "a.hideturtle()\n"
        "a.penup()\n"
        f"a.goto({-gap / 2}, 0)\n"
        'a.dot(40, "orange")\n'
        "b = turtle.Turtle()\n"
        "b.hideturtle()\n"
        "b.penup()\n"
        f"b.goto({gap / 2}, 0)\n"
        'b.dot(40, "blue")\n'
        "distance = a.distance(b)\n"
        "a.goto(0, 60)\n"
        'a.write(round(distance), align="center")\n'
        "if distance < 30:\n"
        "    a.goto(0, -90)\n"
        '    a.write("touching!", align="center")\n'
    )


def frames(programs, times, x, y, w, h, world, until_last="end", **extra):
    """One turtle window per frame; each frame replaces the one before (the windows are opaque)."""
    out = []
    for i, (code, when) in enumerate(zip(programs, times)):
        end = times[i + 1] if i + 1 < len(times) else until_last
        extra.setdefault("cursor", False)
        out.append(A("turtle", code=code, at=when, until=end, x=x, y=y, w=w, h=h, world=world, duration=0.01,
                     **extra))
    return out


# the ball falls from 200 to -200 in steps of 5: 80 frames, then the timer stops
FALL_YS = [200 - 5 * k for k in range(1, 81)]
FALL_TIMES = [f"down+{0.12 * k:.2f}" for k in range(80)]

TRY_KEYS = '''def go_left():
    player.setx(player.xcor() - 20)

def go_right():
    player.setx(player.xcor() + 20)

def fall():
    ball.sety(ball.ycor() - 5)
    if ball.ycor() > -200:
        screen.ontimer(fall, 50)

screen.onkey(go_left, "Left")
screen.listen()'''

SPIN_SETUP = '''import turtle
screen = turtle.Screen()
player = turtle.Turtle("turtle")

def spin():
    player.left(90)
'''
SPIN_BUG = SPIN_SETUP + '''
screen.onkey(spin(), "r")
turtle.done()'''
SPIN_NO_LISTEN = SPIN_SETUP + '''
screen.onkey(spin, "r")
turtle.done()'''
SPIN_FIXED = SPIN_SETUP + '''
screen.onkey(spin, "r")
screen.listen()
turtle.done()'''

ARCADE = '''import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
for x, y in [(-120, 150), (40, 60), (150, 180)]:
    pen.goto(x, y)
    pen.dot(34, "orange")
pen.goto(-20, -160)
pen.color("blue")
pen.begin_fill()
for corner in [(20, -160), (20, -120), (-20, -120)]:
    pen.goto(corner)
pen.end_fill()
pen.goto(-190, 190)
pen.write("Score: 3")'''

FLOWER = '''import turtle
t = turtle.Turtle()
t.pensize(4)
t.color("purple")
for petal in range(6):
    t.circle(70)
    t.left(60)'''

EPISODE = Episode(level=2, week=9, scenes=(
    Scene("l2-w09-s01", setting="workshop", lead_in=0.2, beats=(
        B("Hi, coders!", cue="hi", pause=0.3),
        B("Pixel presses Run and taps the arrow keys.", cue="taps", pause=0.2),
        B("Left, left, right!", cue="keys", pause=0.3),
        B("Nothing moves.", cue="nothing", pause=0.5),
        B("Until now, our programs ran from top to bottom, then stopped.", cue="topdown", pause=0.3),
        B("But games are different.", cue="different", pause=0.2),
        B("Games wait: for a key press, or for a timer to ring.", cue="wait", pause=0.4),
        B("Today, Pixel learns to wait and react.", cue="today", pause=0.3),
        B("And your own final project begins!", cue="project", pause=1.2),
    ), actions=(
        A("nova", x=300, y=960, enter="left", wave="hi", moods={"nothing": "surprised", "today": "happy"}),
        A("pixel", x=620, y=760, drop=True, moods={"nothing": "confused", "today": "happy", "project": "proud"},
          beep=[("keys", "keys$")]),
        *frames([game_frame(200)], ["taps"], x=1240, y=220, w=580, h=500, world=260, until_last="different"),
        A("chip", "← Left", at="keys", until="keys@0.33", x=1530, y=820, color="navy", size=60),
        A("chip", "← Left", at="keys@0.33", until="keys@0.66", x=1530, y=820, color="navy", size=60),
        A("chip", "Right →", at="keys@0.66", until="topdown", x=1530, y=820, color="navy", size=60),
        A("sfx", "tick", at="keys"), A("sfx", "tick", at="keys@0.33"), A("sfx", "tick", at="keys@0.66"),
        A("chip", "Nothing moves", at="nothing", until="different", x=1530, y=930, color="white", size=38),
        A("cards", at="topdown", until="different", x=860, y=300, w=320, gap=100,
          items=["line 1", "line 2", "line 3", "stop"],
          reveal=["topdown@0.1", "topdown@0.3", "topdown@0.5", "topdown@0.8"]),
        A("icons", at="wait", until="project", x=1300, y=420, gap=340,
          items=[("key", "a key press", "wait@0.3"), ("clock", "a timer", "wait@0.7")]),
        A("chip", "Games wait for keys and timers", at="wait@0.5", x=1300, y=680, color="green", size=44),
        A("banner", "MISSION: Make the game react", at="today"),
        A("icons", at="project+0.5", x=1300, y=420, items=[("trophy", "Final Project", "project+0.5")]),
        A("sfx", "sparkle", at="project@0.5"),
    )),
    Scene("l2-w09-s02", setting="sky", beats=(
        B("Something that happens while a program runs, like a key press, is an event.", cue="event", pause=0.3),
        B("The function that answers it is a handler.", cue="handler", pause=0.4),
        B("Think of a doorbell.", cue="doorbell", pause=0.2),
        B("You don't stand by the door all day.", cue="stand", pause=0.2),
        B("The bell calls you!", cue="calls", pause=0.5),
        B("With screen.onkey, we connect go right to the Right key: when the Right arrow is pressed, Python calls go "
          "right.", cue="onkey",
          pause=0.4),
        B("But the bell only works when switched on.", cue="switched", pause=0.2),
        B("That's screen.listen.", cue="listen", pause=0.5),
        B("Turtle's kitchen timer is ontimer.", cue="ontimer", pause=0.2),
        B("It calls a function after some milliseconds.", cue="ms", pause=0.3),
        B("Our game loop does one frame, where everything moves a tiny bit, then sets the timer again.",
          cue="frame", pause=0.5),
        B("And two things are touching when the distance between them is small, like less than thirty steps.",
          cue="touch", pause=0.8),
    ), actions=(
        # event -> handler
        A("chip", "Right →", at="event@0.5", until="ontimer", x=280, y=300, color="navy", size=48),
        A("arrow", at="handler", until="ontimer", x1=430, y1=300, x2=700, y2=300, color="orange"),
        A("chip", "go_right()", at="handler@0.4", until="ontimer", x=880, y=300, color="yellow", size=44),
        A("chip", "Event → handler", at="handler@0.6", until="onkey", x=580, y=470, color="orange", size=46),
        A("door", "DOOR", at="doorbell", until="ontimer", x=1560, y=900),
        A("nova", x=1080, y=960, s=0.8, at="doorbell", until="ontimer",
          path=[("calls", 1080, 960), ("calls+0.9", 1300, 960)], moods={"stand": "thinking", "calls": "happy"}),
        A("chip", "ding dong!", at="calls", until="onkey", x=1560, y=420, color="yellow", size=44),
        A("sfx", "door", at="calls"),
        # onkey + listen
        A("code", code='screen.onkey(go_right, "Right")\nscreen.listen()', title="game.py", x=80, y=430, w=900,
          h=240, shell=False, at="onkey", until="ontimer", reveal=["onkey", "listen"],
          highlight=[(1, "onkey@0.3", "switched"), (2, "listen", "ontimer")]),
        A("box", "doorbell", x=1560, y=330, w=260, at="switched", until="ontimer", color="red",
          values=[("switched", "OFF"), ("listen", "ON")]),
        A("chip", "screen.listen() switches it on", at="listen@0.4", until="ontimer", x=530, y=770, color="green",
          size=42),
        # ontimer and frames
        A("icons", at="ontimer", until="touch", x=330, y=380, items=[("clock", "ontimer", "ontimer")]),
        A("chip", "after some milliseconds", at="ms", until="touch", x=330, y=620, color="sky", size=36),
        A("cards", at="frame", until="touch", x=700, y=300, w=1060, gap=120,
          items=["One frame: everything moves a tiny bit", "Set the timer again"],
          reveal=["frame@0.1", "frame@0.6"],
          active=[[("frame@0.2", "frame@0.5"), ("frame$", "frame>")], ("frame@0.6", "frame$")]),
        A("box", "frame", x=1230, y=640, w=260, at="frame", until="touch",
          values=[("frame", 1), ("frame@0.7", 2), ("frame$+0.2", 3)]),
        A("chip", "ontimer → the next frame", at="frame@0.7", until="touch", x=1230, y=860, color="green",
          size=44),
        # touching
        *frames([touch_frame(g) for g in (240, 160, 90, 28)], ["touch", "touch@0.3", "touch@0.55", "touch@0.8"],
                x=560, y=200, w=800, h=600, world=220, cursor=False),
        A("chip", "distance < 30 → touching!", at="touch$", x=960, y=900, color="orange", size=44),
    )),
    Scene("l2-w09-s03", setting="lavender", beats=(
        B("Let's watch a tiny game work.", cue="watch", pause=0.3),
        B("A ball starts at the top, and Nova's turtle waits in the middle.", cue="begin", pause=0.3),
        B("Handler one: go left, which moves x twenty steps left.", cue="left", pause=0.3),
        B("Handler two: go right, twenty steps right.", cue="right", pause=0.4),
        B("Then the frame function, called fall.", cue="fall", pause=0.2),
        B("The ball moves down five steps.", cue="down", pause=0.2),
        B("If it's still above minus two hundred, Nova calls screen.ontimer with fall and fifty.", cue="if", pause=0.3),
        B("That means: run fall again in fifty milliseconds.", cue="means", pause=0.3),
        B("A thousand milliseconds make one second, and a thousand divided by fifty is twenty.", cue="math"),
        B("So that's twenty frames every second!", cue="twenty", pause=0.4),
        B("Notice: no parentheses after fall or go left.", cue="notice", pause=0.3),
        B("We hand turtle the function, and turtle calls it later.", cue="hand", pause=0.4),
        B("Bigger games also keep their state, like the score, in a dictionary.", cue="state", pause=0.8),
    ), actions=(
        A("code", code=TRY_KEYS, title="try_keys.py", x=50, y=150, w=1040, h=660, size=29, shell=False, at="watch",
          reveal=["left", "left", "right", "right", "right", "fall", "fall", "down", "if", "if@0.5", "notice",
                  "notice", "notice"],
          highlight=[(2, "left@0.4", "right"), (5, "right@0.3", "fall"), (8, "down", "if"), (9, "if", "if@0.5"),
                     (10, "if@0.5", "math"), (10, "notice", "state"), (12, "notice", "state")]),
        *frames([game_frame(200), game_frame(200, -20), game_frame(200, 0)], ["begin", "left@0.5", "right@0.5"],
                x=1150, y=150, w=700, h=600, world=260, until_last="down"),
        *frames([game_frame(y) for y in FALL_YS], FALL_TIMES, x=1150, y=150, w=700, h=600, world=260),
        A("chip", "← Left", at="left@0.4", until="right", x=1500, y=830, color="navy", size=56),
        A("chip", "Right →", at="right@0.4", until="fall", x=1500, y=830, color="navy", size=56),
        A("box", "frame", x=1500, y=880, w=240, h=150, at="down", until="math",
          values=[(t, k + 1) for k, t in enumerate(FALL_TIMES)]),
        A("chip", "1000 ÷ 50 = 20 frames each second", at="math@0.5", until="state", x=1500, y=860, color="yellow",
          size=38),
        A("chip", "No () after the function name", at="notice@0.4", x=570, y=900, color="red", size=42),
        A("dict", "state", at="state@0.4", x=1180, y=850, w=640, rows=[('"score"', 0), ('"running"', "True")]),
    )),
    Scene("l2-w09-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Nova wants the turtle to spin when you press r.", cue="wants", pause=0.3),
        B("The spin function turns the turtle left ninety degrees.", cue="code", pause=0.2),
        B("Then screen.onkey connects spin, with parentheses after it, to the r key.", cue="onkey", pause=0.3),
        B("Pixel presses Run.", cue="run", pause=0.3),
        B("The turtle spins once, right at the start.", cue="once", pause=0.3),
        B("Then r does nothing, and there's no red error.", cue="nothing", pause=0.4),
        B("Detective steps!", cue="steps", pause=0.2),
        B("What did we expect? A spin on every press.", cue="expect", pause=0.3),
        B("What happened? One spin, then nothing.", cue="happened", pause=0.3),
        B("Read one line at a time.", cue="read", pause=0.2),
        B("Pause and point.", cue="pause", pause=4.0),
        B("Those parentheses call spin right now, only once, and hand onkey its answer, which is nothing.",
          cue="parens", pause=0.4),
        B("Nova removes them.", cue="removes", pause=0.3),
        B("Run again.", cue="again", pause=0.3),
        B("Still nothing!", cue="still", pause=0.5),
        B("Second clue: is the doorbell switched on?", cue="second", pause=0.3),
        B("There's no screen.listen.", cue="nolisten", pause=0.2),
        B("Nova adds it.", cue="adds", pause=0.3),
        B("Third clue: on a Mac, click the turtle window once so it hears the keys.", cue="third", pause=0.3),
        B("Spin, spin, spin!", cue="spin", pause=1.0),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", code=SPIN_BUG, title="spin.py", x=50, y=190, w=1010, h=780, size=30, at="wants", until="removes",
          reveal=["wants", "wants", "wants", "code", "code", "code", "onkey", "onkey", "onkey@0.6"],
          highlight=[(8, "read", "removes")], run="run", expect=[]),
        A("code", code=SPIN_NO_LISTEN, title="spin.py", x=50, y=190, w=1010, h=780, size=30, at="removes",
          until="adds", highlight=[(8, "removes", "again")], run="again", expect=[]),
        A("code", code=SPIN_FIXED, title="spin.py", x=50, y=190, w=1010, h=780, size=30, at="adds",
          highlight=[(9, "adds", "third")], run="third", expect=[]),
        *frames([spin_frame(0), spin_frame(1)], ["run", "run+0.5"], x=1120, y=190, w=660, h=480, world=200,
                until_last="spin"),
        *frames([spin_frame(n) for n in (2, 3, 4)], ["spin", "spin@0.4", "spin@0.8"], x=1120, y=190, w=660, h=480,
                world=200),
        A("chip", "press r", at="nothing", until="nothing@0.3", x=1450, y=760, color="navy", size=56),
        A("chip", "press r", at="nothing@0.35", until="nothing@0.65", x=1450, y=760, color="navy", size=56),
        A("chip", "press r", at="nothing@0.7", until="steps", x=1450, y=760, color="navy", size=56),
        A("sfx", "tick", at="nothing"), A("sfx", "tick", at="nothing@0.35"), A("sfx", "tick", at="nothing@0.7"),
        A("chip", "no red error", at="nothing@0.6", until="steps", x=1450, y=880, color="white", size=38),
        A("chip", "Expected: a spin on every press", at="expect", until="pause", x=1450, y=760, color="green",
          size=36),
        A("chip", "Happened: one spin, then nothing", at="happened", until="pause", x=1450, y=870, color="orange",
          size=36),
        A("thought", "Which line?", at="pause+0.3", until="pause>", x=1450, y=820),
        A("chip", 'onkey(spin(), "r") runs it once', at="parens", until="second", x=1450, y=760, color="red",
          size=38),
        A("chip", 'onkey(spin, "r") calls it later', at="removes", until="second", x=1450, y=870, color="green",
          size=38),
        A("badge", ok=False, at="still", until="adds", x=1760, y=980),
        A("chip", "Add screen.listen()", at="nolisten", x=1450, y=760, color="green", size=42),
        A("chip", "On a Mac: click the window first", at="third@0.3", x=1450, y=870, color="yellow", size=36),
        A("pointer", at="third@0.4", until="spin", path=[("third@0.4", 1700, 760), ("third@0.8", 1500, 520)]),
        A("sfx", "pop", at="third@0.85"),
        A("badge", ok=True, at="spin@0.9", x=1720, y=620),
        A("confetti", at="spin@0.9", x=1450, y=400),
    )),
    Scene("l2-w09-s05", setting="workshop", tail=0.8, beats=(
        B("You made Pixel react!", cue="react", pause=0.3),
        B("Let's remember.", cue="remember", pause=0.2),
        B("An event calls a handler.", cue="event", pause=0.2),
        B("onkey connects them, listen switches on the doorbell, and ontimer runs the next frame.", cue="onkey",
          pause=0.4),
        B("Now your final project begins!", cue="project", pause=0.3),
        B("Option A is an Arcade Game with keys, a timer and a score.", cue="optA", pause=0.3),
        B("Option B is an Art Studio that saves and loads designs.", cue="optB", pause=0.4),
        B("Want a picture or sound?", cue="want", pause=0.2),
        B("They belong to the people who made them.", cue="belong", pause=0.3),
        B("CC zero means anyone may use it.", cue="cc0", pause=0.2),
        B("CC BY means you may use it if you give credit, in a comment and on your title screen.", cue="ccby",
          pause=0.3),
        B("No license? Don't use it.", cue="nolicense", pause=0.5),
        B("Your turn: open Etch-a-Sketch.", cue="turn", pause=0.2),
        B("Press Run, click the window, and press Up.", cue="press", pause=0.2),
        B("Nothing yet!", cue="nothing", pause=0.3),
        B("Make the window listen, then add the other arrows.", cue="make", pause=0.3),
        B("No parentheses!", cue="noparens", pause=0.8),
    ), actions=(
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "remember"), ("noparens", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "event → handler", at="event", until="project", x=1150, y=460, color="orange", size=46),
        A("chip", "onkey • listen() • ontimer", at="onkey", until="project", x=1150, y=600, color="green", size=46),
        A("turtle", code=ARCADE, title="Option A", at="optA", until="want", x=740, y=250, w=500, h=460, world=220,
          duration=0.01, cursor=False),
        A("chip", "Option A: Arcade Game", at="optA", until="want", x=990, y=790, color="sky", size=40),
        A("turtle", code=FLOWER, title="Option B", at="optB", until="want", x=1320, y=250, w=500, h=460, world=170,
          duration=2.0),
        A("chip", "Option B: Art Studio", at="optB", until="want", x=1570, y=790, color="purple", size=40),
        A("icons", at="want+0.5", until="cc0", x=1250, y=440, gap=320,
          items=[("camera", "a picture", "want+0.5"), ("music", "a sound", "want+0.9")]),
        A("chip", "They belong to their makers", at="belong", until="cc0", x=1250, y=700, color="yellow", size=40),
        A("icons", at="cc0", until="turn", x=1250, y=400, gap=360, crossed=[2],
          items=[("check", "CC0: anyone", "cc0"), ("star", "CC BY: give credit", "ccby"),
                 ("cross", "no license", "nolicense")]),
        A("code", code="# Star sound by Mei (CC BY)", title="mygame.py", at="ccby@0.5", until="turn", x=780, y=620,
          w=940, h=150, shell=False),
        A("chip", "CC0 or CC BY + credit. No license? No.", at="nolicense@0.5", until="turn", x=1250, y=870,
          color="green", size=40),
        A("banner", "NEXT: Etch-a-Sketch", at="turn", color="green"),
        A("cards", at="turn", x=640, y=250, w=840, gap=110,
          items=["Open Etch-a-Sketch", "Run, click the window, press Up", "Make the window listen",
                 "Add the other arrows: no ()!"],
          reveal=["turn@0.2", "press", "make", "make@0.6"]),
        A("chip", "Nothing yet!", at="nothing", until="make", x=1650, y=740, color="yellow", size=40),
        A("chip", "No parentheses!", at="noparens", x=1060, y=780, color="red", size=48),
    )),
))
