"""Level 2 Week 10: Project Studio 1: Plan and Core (kit episode)."""

from ..kit_dsl import A, B, Episode, PIXEL, Scene

# ----------------------------------------------------------------------------- the lesson's skeleton, in steps
SKELETON_DATA = '''# My game - core loop skeleton (M2)
import turtle

SETTINGS = {"step": 20, "left_edge": -280,
            "right_edge": 280}
state = {"score": 0, "running": True}'''

SKELETON_BRAIN = '''def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

def next_x(x, direction):
    new_x = x + direction * SETTINGS["step"]
    return clamp(new_x, SETTINGS["left_edge"],
                 SETTINGS["right_edge"])'''

SKELETON_LOOP = '''def go_left():
    player.setx(next_x(player.xcor(), -1))

def go_right():
    player.setx(next_x(player.xcor(), 1))

def game_loop():
    if not state["running"]:
        return
    screen.update()
    screen.ontimer(game_loop, 50)'''

SKELETON_MAIN = '''if __name__ == "__main__":
    screen = turtle.Screen()
    screen.tracer(0)
    player = turtle.Turtle("square")
    player.penup()
    player.goto(0, -250)
    screen.listen()
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    game_loop()
    turtle.done()'''

FULL = "\n\n".join([SKELETON_DATA, SKELETON_BRAIN, SKELETON_LOOP, SKELETON_MAIN])

HALF_TYPED = '''# Comet Catch
def level_1():
def level_2(
def boss_battle
def rainbow_title'''


def clamp(value, low, high):
    return max(low, min(high, value))


# where the square is after each arrow press: right to the wall (it stops), then left to the other wall
PRESSES = [1] * 17 + [-1] * 31
SQUARE_XS = [0]
for step in PRESSES:
    SQUARE_XS.append(clamp(SQUARE_XS[-1] + step * 20, -280, 280))


def square_frame(x: int) -> str:
    return (
        "import turtle\n"
        "edge = turtle.Turtle()\n"
        "edge.hideturtle()\n"
        'edge.color("gray")\n'
        "for wall in (-300, 300):\n"
        "    edge.penup()\n"
        "    edge.goto(wall, -300)\n"
        "    edge.pendown()\n"
        "    edge.goto(wall, 300)\n"
        'player = turtle.Turtle("square")\n'
        "player.hideturtle()\n"
        "player.penup()\n"
        f"player.goto({x - 20}, -270)\n"
        'player.color("blue")\n'
        "player.begin_fill()\n"
        f"for corner in [({x + 20}, -270), ({x + 20}, -230), ({x - 20}, -230)]:\n"
        "    player.goto(corner)\n"
        "player.end_fill()\n"
    )


SLIDE_TIMES = ["press"] + [f"press@0.6+{0.1 * k:.1f}" for k in range(1, len(SQUARE_XS))]


def slide_frames():
    out = []
    for i, (x, when) in enumerate(zip(SQUARE_XS, SLIDE_TIMES)):
        end = SLIDE_TIMES[i + 1] if i + 1 < len(SLIDE_TIMES) else "end"
        out.append(A("turtle", code=square_frame(x), at=when, until=end, x=1170, y=170, w=690, h=560, world=320,
                     duration=0.01, cursor=False, title="mygame.py"))
    return out


ROAD = ["M1 Pitch + plan", "M2 Core loop", "M3 Data + tests", "M4 Polish", "Showcase"]

EPISODE = Episode(level=2, week=10, scenes=(
    Scene("l2-w10-s01", setting="workshop", lead_in=0.2, beats=(
        B("Hi, coders!", cue="hi", pause=0.3),
        B("Nova has a giant plan: Comet Catch, with ten levels, boss battles and a rainbow title screen.",
          cue="plan", pause=0.4),
        B("Nova starts typing everything at once.", cue="typing", pause=0.3),
        B("Pixel waits, and waits.", cue="waits", pause=0.5),
        B("‘Which part can I run today?’", speaker=PIXEL, cue="which", pause=0.1),
        B("asks Pixel.", cue="asks", pause=0.4),
        B("Hmm. Nothing yet!", cue="nothing", pause=0.5),
        B("Nobody can ride one perfect wheel.", cue="wheel", pause=0.4),
        B("So what should Nova build first?", cue="first", pause=2.4),
    ), actions=(
        A("nova", x=300, y=960, enter="left", wave="hi",
          moods={"plan": "happy", "nothing": "surprised", "first": "thinking"}, chin=("first", "end")),
        A("pixel", x=650, y=760, drop=True, moods={"waits": "thinking", "nothing": "confused", "first": "thinking"}),
        A("panel", "Comet Catch", at="plan", until="typing", x=1050, y=380, w=700,
          items=[("plan@0.45", "10 levels"), ("plan@0.6", "boss battles"), ("plan@0.8", "rainbow title screen")]),
        A("code", code=HALF_TYPED, title="comet_catch.py", allow_error=True, x=1000, y=400, w=820, h=360,
          shell=False, at="typing", until="wheel", type=("typing", "waits$")),
        A("icons", at="waits", until="nothing", x=1410, y=860, items=[("clock", "waiting…", "waits")]),
        A("chip", "not running yet", at="nothing", until="wheel", x=1410, y=830, color="red", size=44),
        A("icons", at="wheel", x=1400, y=520, items=[("gear", "one wheel", "wheel")]),
        A("banner", "STUDIO MISSION: Plan, then build", at="first"),
        A("chip", "What is the smallest version?", at="first@0.4", x=1000, y=260, color="yellow", size=44),
        A("thought", "", at="first$+0.3", until="end", x=640, y=440),
    )),
    Scene("l2-w10-s02", setting="sky", beats=(
        B("Build a skateboard first.", cue="skate", pause=0.2),
        B("It's tiny, but you can ride it.", cue="tiny", pause=0.3),
        B("In a project, the skateboard is the core loop: the smallest version that runs.", cue="core", pause=0.4),
        B("Before Python, we plan.", cue="plan", pause=0.2),
        B("Pseudocode is your program in plain words, one step per line.", cue="pseudo", pause=0.3),
        B("A flowchart draws the same steps: ovals for start and end, rectangles for steps, and diamonds for "
          "yes-or-no questions.", cue="flow", pause=0.4),
        B("Each line that does one job can become a function.", cue="job", pause=0.3),
        B("‘Move the player, but not off the screen’ becomes next x.", cue="move", pause=0.3),
        B("The position and the direction go in.", cue="in", pause=0.2),
        B("The new position comes out.", cue="out", pause=0.4),
        B("That's decomposition: breaking a big problem into small, named parts.", cue="decomp", pause=0.4),
        B("Your pitch and plan are Milestone M1.", cue="m1", pause=0.2),
        B("Your core loop is M2.", cue="m2", pause=0.8),
    ), actions=(
        A("listrow", at="skate", until="plan", x=960, y=420, cell=380, indexes=False,
          items=["skateboard", "scooter", "bike", "car"],
          highlight=[("skate", "core$", 0)]),
        A("chip", "every version works", at="tiny", until="plan", x=960, y=600, color="white", size=40),
        A("chip", "Core loop = the skateboard", at="core", until="plan", x=960, y=760, color="orange", size=48),
        # pseudocode and flowchart
        A("panel", "Pseudocode", at="pseudo", until="job", x=90, y=250, w=780, size=34,
          items=[("pseudo@0.3", "set up the screen, player, keys"), ("pseudo@0.55", "repeat every tick:"),
                 ("pseudo@0.8", "move, check, score")]),
        A("chip", "Start", at="flow@0.1", until="job", x=1250, y=240, color="white", size=40),
        A("arrow", at="flow@0.15", until="job", x1=1250, y1=285, x2=1250, y2=345, color="navy", width=8),
        A("panel", at="flow@0.35", until="job", x=1060, y=355, w=380, size=34,
          items=[("flow@0.35", "move everything")]),
        A("arrow", at="flow@0.5", until="job", x1=1250, y1=465, x2=1250, y2=515, color="navy", width=8),
        A("flow", at="flow@0.65", until="job", x=1250, y=590, items=["Touching?"], outcomes=["+1 point", "next tick"]),
        A("chip", "Oval start/end • Rectangle step", at="flow@0.4", until="job", x=480, y=700, color="sky",
          size=40),
        A("chip", "Diamond = yes/no question", at="flow@0.75", until="job", x=480, y=820, color="yellow", size=40),
        # one job -> one function
        A("chip", "one job → one function", at="job", until="move", x=960, y=480, color="orange", size=48),
        A("chip", "‘Move the player, but not off the screen’", at="move", until="m1", x=960, y=230, color="white",
          size=40),
        A("machine", "next_x", at="move@0.6", until="m1", x=960, y=520, items=[("in", "(0, 1)", "20")]),
        A("chip", "in: position, direction", at="in", until="m1", x=440, y=720, color="orange", size=36),
        A("chip", "out: new position", at="out", until="m1", x=1480, y=720, color="green", size=36),
        A("chip", "decomposition = small, named parts", at="decomp", until="m1", x=960, y=880, color="purple",
          size=42),
        # milestones
        A("roadmap", at="m1", x=260, y=500, w=1400, items=ROAD, current=[("m1", 0), ("m2", 1)]),
        A("chip", "M1 pitch + plan → M2 core loop", at="m2", x=960, y=780, color="green", size=46),
    )),
    Scene("l2-w10-s03", setting="lavender", beats=(
        B("Let's turn a plan into a walking skeleton.", cue="skeleton", pause=0.3),
        B("Nova saves a new file: mygame dot p y.", cue="save", pause=0.2),
        B("Never call it turtle dot p y!", cue="never", pause=0.5),
        B("First, two dictionaries.", cue="dicts", pause=0.2),
        B("SETTINGS holds numbers we might change, like a step of twenty.", cue="settings", pause=0.3),
        B("state holds things that change while playing, like the score.", cue="state", pause=0.4),
        B("Next, the brain: clamp and next x.", cue="brain", pause=0.3),
        B("No turtle at all, just values in and an answer out.", cue="values", pause=0.4),
        B("Then the key handlers and the game loop.", cue="handlers", pause=0.3),
        B("At its end: screen dot ontimer, game loop, fifty.", cue="ontimer", pause=0.2),
        B("Run me again in fifty milliseconds.", cue="again", pause=0.4),
        B("The start-up code goes at the bottom, under if name equals main.", cue="main", pause=0.4),
        B("Press Run, click the window, press the arrows.", cue="press", pause=0.3),
        B("The square slides and stops at the edges.", cue="slides", pause=0.4),
        B("That's M2!", cue="m2", pause=0.5),
        B("Art Studio teams build a menu loop, or a key that draws a new design.", cue="art", pause=0.8),
    ), actions=(
        A("icons", at="save", until="dicts", x=1510, y=380, gap=320, crossed=[1],
          items=[("file", "mygame.py", "save@0.4"), ("file", "turtle.py", "never")]),
        A("chip", "Never name it turtle.py", at="never@0.4", until="dicts", x=1510, y=640, color="red", size=42),
        A("code", code=SKELETON_DATA, title="mygame.py", x=50, y=170, w=1080, h=440, size=30, shell=False,
          at="save", until="brain", reveal=["save", "save", "dicts", "settings", "settings", "state"],
          highlight=[(4, "settings@0.3", "state"), (5, "settings@0.3", "state"), (6, "state@0.3", "brain")]),
        A("dict", "SETTINGS", at="settings", until="brain", x=1190, y=260, w=660,
          rows=[('"step"', 20), ('"left_edge"', -280), ('"right_edge"', 280)],
          highlight=[("settings@0.6", "state", '"step"')]),
        A("dict", "state", at="state", until="brain", x=1190, y=640, w=660,
          rows=[('"score"', 0), ('"running"', "True")]),
        A("chip", "SETTINGS + state dictionaries", at="state@0.6", until="brain", x=1520, y=920, color="orange",
          size=40),
        A("code", code=SKELETON_BRAIN, title="mygame.py", x=50, y=170, w=1080, h=600, size=30, shell=False,
          at="brain", until="handlers", highlight=[(1, "brain@0.4", "brain$"), (8, "brain$", "values$")]),
        A("icons", at="brain@0.3", until="handlers", x=1510, y=380, items=[("gear", "the brain", "brain@0.3")]),
        A("chip", "values in → answer out", at="values", until="handlers", x=1510, y=640, color="green", size=42),
        A("chip", "no turtle here", at="values@0.5", until="handlers", x=1510, y=760, color="white", size=38),
        A("code", code=SKELETON_LOOP, title="mygame.py", x=50, y=170, w=1080, h=600, size=30, shell=False,
          at="handlers", until="main", highlight=[(11, "ontimer", "main")]),
        A("chip", "Run me again in 50 ms", at="again", until="main", x=1510, y=500, color="yellow", size=42),
        A("code", code=SKELETON_MAIN, exec=FULL, title="mygame.py", x=50, y=170, w=1080, h=830, size=30,
          at="main", highlight=[(1, "main", "press")], run="press", expect=[]),
        A("chip", 'if __name__ == "__main__":', at="main@0.5", until="press", x=1510, y=500, color="sky", size=40),
        *slide_frames(),
        A("chip", "Right →", at="press@0.6", until="press@0.6+1.7", x=1510, y=800, color="navy", size=44),
        A("chip", "← Left", at="press@0.6+1.7", until="m2", x=1510, y=800, color="navy", size=44),
        A("chip", "stops at the edges", at="slides@0.5", until="art", x=1510, y=900, color="white", size=38),
        A("badge", ok=True, at="m2", until="art", x=1290, y=820),
        A("chip", "That's M2!", at="m2", until="art", x=1560, y=800, color="green", size=46),
        A("chip", "Art Studio: a menu loop", at="art", x=1510, y=800, color="purple", size=40),
        A("chip", "Draw • Save • Load • Quit", at="art@0.4", x=1510, y=910, color="white", size=38),
    )),
    Scene("l2-w10-s04", setting="mint", beats=(
        B("Time for a partner code review.", cue="review", pause=0.2),
        B("Swap seats.", cue="swap", pause=0.5),
        B("Pixel runs Nova's code and reads it with three questions.", cue="three", pause=0.3),
        B("One: does it run?", cue="one", pause=0.2),
        B("If there's red text, which line does the traceback point to?", cue="red", pause=0.4),
        B("Two: are the names clear?", cue="two", pause=0.2),
        B("next x tells you its job.", cue="nextx", pause=0.2),
        B("A function called thing two doesn't!", cue="thing2", pause=0.4),
        B("Three: does each function do one job, and are numbers you might change kept in the settings dictionary?",
          cue="job", pause=0.5),
        B("Pixel also hunts last week's classic bugs: parentheses after a handler in onkey, a missing listen, and a "
          "game loop that never sets its timer again.", cue="classic", pause=0.5),
        B("Then Pixel writes two stars and a wish.", cue="stars", pause=0.3),
        B("‘Star: next x says exactly what it does.", speaker=PIXEL, cue="star1", pause=0.2),
        B("Star: the square stops at the wall.", speaker=PIXEL, cue="star2", pause=0.2),
        B("Wish: could thing two get a name that tells its job?’", speaker=PIXEL, cue="wish", pause=0.4),
        B("Nova says thanks, and decides what to change.", cue="thanks", pause=0.8),
    ), actions=(
        A("banner", "PARTNER CODE REVIEW", at="review", color="navy"),
        A("chair", x=280, y=1000, s=0.8),
        A("chair", x=560, y=1000, s=0.8),
        A("nova", x=260, y=1000, s=0.65, path=[("swap", 260, 1000), ("swap+1.0", 560, 1000)],
          moods={"thing2": "thinking", "thanks": "happy"}, wave=("thanks", "end")),
        A("pixel", x=560, y=860, s=0.55, ground=990, path=[("swap", 560, 860), ("swap+1.0", 260, 860)],
          moods={"one": "thinking", "stars": "happy"}),
        A("chip", "Does it run? • Clear names? • One job?", at="three", until="classic", x=1250, y=220,
          color="yellow", size=40),
        A("cards", at="one", until="classic", x=800, y=340, w=900, gap=110,
          items=["Does it run?", "Clear names?", "One job each? Numbers in SETTINGS?"],
          reveal=["one", "two", "job"], active=[("one", "two"), ("two", "job"), ("job", "classic")]),
        A("chip", "traceback → which line?", at="red", until="two", x=1250, y=740, color="red", size=40),
        A("chip", "next_x", at="nextx", until="job", x=1000, y=740, color="green", size=42),
        A("badge", ok=True, at="nextx@0.5", until="job", x=1170, y=740),
        A("chip", "thing2", at="thing2", until="job", x=1420, y=740, color="white", size=42),
        A("thought", "?", at="thing2@0.5", until="job", x=1600, y=660),
        A("chip", 'SETTINGS["step"]', at="job@0.6", until="classic", x=1250, y=740, color="orange", size=40),
        A("chip", "Hunt: (), listen(), ontimer", at="classic", until="stars", x=1250, y=220, color="red", size=42),
        A("cards", at="classic", until="stars", x=800, y=340, w=900, gap=110, color="red",
          items=['onkey(go_left(), "Left")', "no screen.listen()", "no ontimer at the end of game_loop"],
          reveal=["classic@0.3", "classic@0.55", "classic@0.8"]),
        A("magnifier", at="classic@0.3", until="stars", s=0.6,
          path=[("classic@0.3", 1780, 340), ("classic@0.55", 1780, 450), ("classic@0.8", 1780, 560)]),
        A("panel", "Two stars and a wish", at="stars", x=800, y=230, w=980, size=36,
          items=[("star1", "Star: next_x says exactly what it does"), ("star2", "Star: the square stops at the wall"),
                 ("wish", "Wish: a name for thing2 that tells its job")]),
        A("icons", at="thanks", x=1050, y=730, items=[("heart", "thanks!", "thanks")]),
        A("chip", "The makers decide", at="thanks@0.4", x=1450, y=730, color="green", size=44),
    )),
    Scene("l2-w10-s05", setting="workshop", tail=0.8, beats=(
        B("Studio day complete!", cue="complete", pause=0.3),
        B("Let's remember.", cue="remember", pause=0.2),
        B("Plan with pseudocode or a flowchart.", cue="plan", pause=0.2),
        B("Break the plan into functions.", cue="break", pause=0.2),
        B("Build the skateboard, your core loop, before anything fancy.", cue="build", pause=0.4),
        B("Now, teamwork.", cue="team", pause=0.2),
        B("Write each function on a sticky note, and take turns choosing, like picking teams fairly.",
          cue="sticky", pause=0.3),
        B("Share the fun jobs and the boring ones, and swap the keyboard on time.", cue="share", pause=0.3),
        B("Put both nicknames in a comment on line one, and credit any code you remixed.", cue="names", pause=0.3),
        B("Using someone's idea is fine.", cue="fine", pause=0.2),
        B("Hiding it is not.", cue="hiding", pause=0.4),
        B("Your turn: make a paper prototype, finish your plan for M1, fill your task board, and build your core "
          "loop for M2.", cue="turn", pause=0.3),
        B("Small and working beats big and broken!", cue="small", pause=0.8),
    ), actions=(
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "remember"), ("small", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "pseudocode or flowchart", at="plan", until="team", x=1150, y=460, color="sky", size=44),
        A("chip", "→ functions", at="break", until="team", x=1150, y=590, color="orange", size=44),
        A("chip", "→ the skateboard first", at="build", until="team", x=1150, y=720, color="green", size=44),
        A("chip", "TO DO → DOING → DONE", at="sticky", until="names", x=1260, y=440, color="yellow", size=44),
        A("table", at="sticky@0.3", until="share", x=760, y=530, col_w=330, header=["TO DO", "DOING", "DONE"],
          rows=[["next_x", "", ""], ["game_loop", "", ""], ["show_score", "", ""]]),
        A("table", at="share", until="names", x=760, y=530, col_w=330, header=["TO DO", "DOING", "DONE"],
          rows=[["show_score", "game_loop", "next_x"], ["", "", ""], ["", "", ""]],
          highlight=[("share", "share+0.8", 0)]),
        A("code", code="# Made by Comet and Pixel\n# Movement code remixed from Dodge the Meteors", title="mygame.py",
          at="names", until="turn", x=740, y=300, w=1080, h=200, size=30, shell=False),
        A("chip", "Credit remixed code", at="names@0.6", until="turn", x=1270, y=600, color="orange", size=42),
        A("icons", at="fine", until="turn", x=1270, y=760, gap=340, crossed=[1],
          items=[("check", "use an idea", "fine"), ("magnifier", "hide it", "hiding")]),
        A("banner", "NEXT: Plan (M1) → Core loop (M2)", at="turn", color="green"),
        A("cards", at="turn", x=640, y=230, w=840, gap=105,
          items=["Make a paper prototype", "Finish your plan (M1)", "Fill your task board",
                 "Build your core loop (M2)"],
          reveal=["turn@0.15", "turn@0.35", "turn@0.6", "turn@0.85"]),
        A("roadmap", at="small", x=760, y=760, w=1000, items=ROAD, checks=[("small@0.3", 0), ("small@0.6", 1)]),
        A("confetti", at="small@0.7", x=1100, y=600),
    )),
))
