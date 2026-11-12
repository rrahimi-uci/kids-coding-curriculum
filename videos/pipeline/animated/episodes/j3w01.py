"""Junior Level 3 Week 1: Patterns in Patterns (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/3-bridge-to-python/teaching-material/lessons/week01.tex: Aiden welcomes the children
back and opens Level 3, the clap-pattern warm-up (REPEAT 3 of clap, clap, stomp inside REPEAT 2 with a
jump), the nested repeat and the nesting-dolls analogy, Exercise 1.1 The Window built step by step,
the "square" My Block and the Square Flower with the turn from the turn card, a prediction quiz,
Exercise 1.3 The One-Square Flower (bug hunt), and "my own pattern, not a copy" (giving credit).

Kit notes: the stage's `draw` always starts heading right, so the window's four squares are drawn
with short `goto` hops between them; the stage cannot draw a rotated square, so the flower is drawn
on a plain drawing canvas (the `turtle` view with its own title and no cursor).
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
MOVE = ("motion", "move [60] steps")
TURN = ("motion", "turn ↻ [90] degrees")
TURN60 = ("motion", "turn ↻ [60] degrees")
ERASE = ("pen", "erase all")
PEN_DOWN = ("pen", "pen down")
PEN_UP = ("pen", "pen up")
SQUARE = ("control", "repeat [4]", [MOVE, TURN])
WINDOW = [("control", "repeat [4]", [SQUARE, TURN]), PEN_UP]  # the repeats of The Window
BIG = 1.25  # block scale: big enough for young eyes
L = 80  # side of one window square on the stage (stage steps; the viewer sees no numbers)

FLOWER = """import turtle
t = turtle.Turtle()
t.color("blue")
t.pensize(4)
for i in range(6):
    for j in range(4):
        t.forward(60)
        t.right(90)
    t.right(60)
turtle.done()"""


def window_actions(cue: str, base: float, squares: int = 4) -> list:
    """The cat draws the window like Scratch does: down-right, down-left, up-left, up-right squares."""
    def at(offset):
        return f"{cue}+{base + offset:.2f}"
    steps = [(at(0.0), "draw", 4, L, 1.2, -90), (at(1.3), "goto", -L, 0, 0.3),
             (at(1.7), "draw", 4, L, 1.2, -90), (at(3.0), "draw", 4, L, 1.2, 90),
             (at(4.3), "goto", 0, 0, 0.3), (at(4.7), "draw", 4, L, 1.2, 90)]
    return steps[:3] if squares == 2 else steps


EPISODE = Episode(level="j3", week=1, scenes=(
    # 1. hook: welcome to Level 3 ---------------------------------------------------------------------
    Scene("j3-w01-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is Pixi. Welcome back to Level 3!", speaker=AIDEN, cue="hi",
          pause=0.4),
        B("Beep boop! Welcome back, coders!", speaker=PIXI, cue="hello", pause=0.5),
        B("You are real coders now. You made games with scores, messages and My Blocks.", speaker=AIDEN,
          cue="coders", pause=0.5),
        B("In Level 3, we make art with patterns, plan on paper, collect data, and find out how computers "
          "learn.", speaker=AIDEN, cue="level", pause=0.5),
        B("And then, we write real code with words, in a language called Python!", speaker=AIDEN, cue="python",
          pause=0.5),
        B("Today's mission: a pattern inside a pattern.", speaker=AIDEN, cue="mission", pause=0.4),
        B("Are you ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "python": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello"),
        A("chip", "Games • Scores • Messages • My Blocks", at="coders", until="level", x=1300, y=300,
          color="orange", size=40),
        A("cards", items=["Patterns", "Plans", "Data", "How computers learn", "Python"], x=1000, y=230, w=640,
          gap=112, reveal=["level@0.1", "level@0.3", "level@0.5", "level@0.75", "python@0.6"], at="level",
          until="mission", color="sky"),
        A("banner", "MISSION: A pattern inside a pattern", at="mission"),
        A("turtle", code=FLOWER, title="Square Flower", cursor=False, x=1080, y=250, w=640, h=560,
          at="mission", run="mission@0.3", duration=3.0),
    )),
    # 2. warm-up: clap patterns ------------------------------------------------------------------------
    Scene("j3-w01-s02", setting="workshop", beats=(
        B("Let's warm up with a clap pattern!", speaker=AIDEN, cue="warm", pause=0.4),
        B("Inside a REPEAT 3 card, we put three cards: clap, clap, stomp.", speaker=AIDEN, cue="cards",
          pause=0.5),
        B("Do it with me! Clap, clap, stomp! Clap, clap, stomp! Clap, clap, stomp!", speaker=AIDEN, cue="clap",
          pause=0.8),
        B("Now watch. We put the whole REPEAT 3 card, and a JUMP card, inside a big REPEAT 2 card.",
          speaker=AIDEN, cue="watch", pause=0.5),
        B("How many stomps will we do now?", speaker=AIDEN, cue="how", pause=3.0),
        B("Three and three make six stomps! And two jumps.", speaker=AIDEN, cue="six", pause=0.5),
        B("The inside pattern runs all the way through, every time the outside pattern goes round.",
          speaker=AIDEN, cue="inside", pause=0.6),
        B("Clap, clap, beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("aiden", x=260, y=980, s=0.8, wave=("clap", "watch"), moods={"how": "thinking", "six": "happy"},
          chin=("how", "six")),
        A("pixi", x=520, y=780, s=0.7, ground=960, beep="pixi"),
        A("scratch", "Clap cards", blocks=[("control", "REPEAT [3]", [("sound", "CLAP"), ("sound", "CLAP"),
                                                                   ("motion", "STOMP")])],
          x=800, y=280, w=640, h=560, scale=BIG, at="cards", until="watch",
          reveal=["cards", "cards@0.6", "cards@0.7", "cards@0.85"],
          highlight=[(1, "clap@0.22", "clap@0.3"), (2, "clap@0.3", "clap@0.38"), (3, "clap@0.38", "clap@0.48"),
                     (1, "clap@0.48", "clap@0.56"), (2, "clap@0.56", "clap@0.64"), (3, "clap@0.64", "clap@0.74"),
                     (1, "clap@0.74", "clap@0.82"), (2, "clap@0.82", "clap@0.9"), (3, "clap@0.9", "clap$")]),
        A("scratch", "Clap cards", blocks=[("control", "REPEAT [2]", [
            ("control", "REPEAT [3]", [("sound", "CLAP"), ("sound", "CLAP"), ("motion", "STOMP")]),
            ("looks", "JUMP")])],
          x=760, y=250, w=640, h=760, scale=1.15, at="watch",
          reveal=["watch", "watch", "watch", "watch", "watch", "watch@0.45"],
          highlight=[(0, "watch@0.7", "watch$"), (4, "six", "six@0.6"), (5, "six@0.6", "six$"),
                     (1, "inside@0.15", "inside@0.5"), (0, "inside@0.5", "inside$")]),
        A("thought", "How many stomps?", at="how$+0.2", until="six", x=1640, y=330),
        A("chip", "3 + 3 = 6 stomps", at="six", x=1640, y=360, color="sky", size=44),
        A("chip", "2 jumps", at="six@0.6", x=1640, y=480, color="purple", size=44),
        A("chip", "Inside runs every time", at="inside", x=1630, y=640, color="yellow", size=36),
    )),
    # 3. the nested repeat --------------------------------------------------------------------------
    Scene("j3-w01-s03", setting="sky", beats=(
        B("Remember Level 1? The cat drew a square: repeat four, move, then a quarter turn.", speaker=AIDEN,
          cue="remember", pause=0.5),
        B("Today, we put that whole square inside another repeat.", speaker=AIDEN, cue="today", pause=0.5),
        B("A repeat inside a repeat is called a nested repeat.", speaker=AIDEN, cue="called", pause=0.5),
        B("Say it with me: nested repeat!", speaker=AIDEN, cue="sayit", pause=1.4),
        B("It's like nesting dolls: a small doll sits inside a bigger doll.", speaker=AIDEN,
          cue="dolls", pause=0.5),
        B("Every time the big repeat goes round once, the small repeat does all of its turns.", speaker=AIDEN,
          cue="every", pause=0.6),
        B("Small patterns make big patterns!", speaker=PIXI, cue="small", pause=0.6),
    ), actions=(
        A("scratch", "A square", blocks=[SQUARE], x=200, y=280, w=820, h=480, scale=BIG, at="remember",
          until="today"),
        A("scratch", "A nested repeat", blocks=[("control", "repeat [4]", [SQUARE, TURN])], x=200, y=290, w=820,
          h=720, scale=BIG, at="today", reveal=["today@0.6", "today", "today", "today", "today@0.6"],
          highlight=[(1, "called", "called@0.5"), (0, "called@0.5", "called$"), (0, "every", "every@0.5"),
                     (1, "every@0.5", "every$")]),
        A("chip", "quarter turn = 90", at="remember@0.6", until="today", x=1440, y=420, color="sky", size=44),
        A("chip", "outside repeat", at="called@0.5", until="sayit", x=1440, y=330, color="orange", size=44),
        A("chip", "inside repeat", at="called", until="sayit", x=1440, y=450, color="yellow", size=44),
        A("bigtext", "Nested repeat!", at="sayit", until="dolls", x=1440, y=420, size=80, color="orange"),
        A("chip", "Like nesting dolls", at="dolls", x=1440, y=330, color="pink", size=44),
        A("chip", "Big repeat: once round", at="every", x=1440, y=470, color="orange", size=40),
        A("chip", "Small repeat: all its turns", at="every@0.5", x=1440, y=590, color="yellow", size=40),
        A("pixi", x=1480, y=900, s=0.55, at="small", ground=980, beep="small"),
    )),
    # 4. The Window, part 1: getting ready -----------------------------------------------------------
    Scene("j3-w01-s04", setting="mint", beats=(
        B("Let's build The Window together.", speaker=AIDEN, cue="build", pause=0.4),
        B("First, we need the green Pen blocks: click Add Extension, and pick Pen.",
          speaker=AIDEN, cue="ext", pause=0.6),
        B("Yellow Events: drag in when green flag clicked.", speaker=AIDEN, cue="events", pause=0.6),
        B("Purple Looks: snap on set size, and change it to forty, so the cat is small.", speaker=AIDEN,
          cue="looks", pause=0.6),
        B("Blue Motion: point in direction ninety, so the cat faces right.", speaker=AIDEN, cue="motion",
          pause=0.6),
        B("Green Pen: erase all, then pen down.", speaker=AIDEN, cue="pen", pause=0.6),
        B("Pen down, ready to draw! Beep!", speaker=PIXI, cue="ready", pause=0.6),
    ), actions=(
        A("banner", "Exercise 1.1: The Window", at="build", color="green"),
        A("scratch", "The Window", blocks=[FLAG, ("looks", "set size to [100] %"), ("motion", "point in direction [90]"),
                                           ERASE, PEN_DOWN],
          x=130, y=260, w=860, h=600, scale=BIG, reveal=["events", "looks", "motion", "pen", "pen@0.6"],
          edits=[("looks@0.75", 1, "set size to [40] %")]),
        A("chip", "Add Extension → Pen", at="ext", until="ext>", x=1460, y=870, color="green", size=44),
        A("chip", "Events: yellow", at="events", until="events>", x=1460, y=870, color="yellow", size=44),
        A("chip", "Looks: purple", at="looks", until="looks>", x=1460, y=870, color="purple", size=44),
        A("chip", "Motion: blue", at="motion", until="motion>", x=1460, y=870, color="sky", size=44),
        A("chip", "Pen: green", at="pen", until="end", x=1460, y=870, color="green", size=44),
        A("stage", x=1080, y=230, w=760, h=520, at="build", until="looks@0.8", sprite_scale=1.0),
        A("stage", x=1080, y=230, w=760, h=520, at="looks@0.8", sprite_scale=0.5),
    )),
    # 5. The Window, part 2: the repeats ---------------------------------------------------------------
    Scene("j3-w01-s05", setting="mint", beats=(
        B("Now orange Control. Snap on a repeat, and change it to four. This is the outside repeat.",
          speaker=AIDEN, cue="outside", pause=0.6),
        B("Drag a second repeat inside it, and change it to four too. This is the inside repeat.",
          speaker=AIDEN, cue="inside", pause=0.6),
        B("Blue Motion: move sixty steps and turn ninety degrees go in the inside repeat. That's one square!",
          speaker=AIDEN, cue="square", pause=0.6),
        B("Then one more turn ninety, under the inside repeat, but still inside the outside repeat.",
          speaker=AIDEN, cue="turn", pause=0.6),
        B("Last, green Pen: pen up at the bottom.", speaker=AIDEN, cue="penup", pause=0.5),
        B("Drag the cat to the middle, and click the green flag!", speaker=AIDEN, cue="click", pause=6.6),
        B("Four squares that touch at the corner. A window!", speaker=AIDEN, cue="window", pause=0.4),
        B("Beep! I see a window!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "The Window (after pen down)",
          blocks=[("control", "repeat [10]", [("control", "repeat [10]", [MOVE, TURN]), TURN]), PEN_UP],
          x=130, y=200, w=860, h=830, scale=BIG,
          reveal=["outside", "inside", "square@0.3", "square@0.5", "turn", "penup"],
          edits=[("outside@0.5", 0, "repeat [4]"), ("inside@0.55", 1, "repeat [4]")],
          highlight=[(0, "outside@0.75", "outside$"), (1, "inside@0.75", "inside$"), (4, "turn", "turn$"),
                     (0, "click+0.5", "click+6.4")]),
        A("chip", "Control: orange", at="outside", until="square", x=1460, y=870, color="orange", size=44),
        A("chip", "Motion: blue", at="square", until="penup", x=1460, y=870, color="sky", size=44),
        A("chip", "Pen: green", at="penup", until="click", x=1460, y=870, color="green", size=44),
        A("stage", x=1080, y=200, w=760, h=540, at="outside", flag_at="click@0.6", sprite_scale=0.5, pen="#1F6FD1",
          actions=window_actions("click", 0.6)),
        A("chip", "4 squares = a window!", at="window", x=1460, y=870, color="green", size=44),
        A("badge", ok=True, at="window", x=1780, y=300),
        A("confetti", at="window", x=1460, y=470),
    )),
    # 6. a "square" My Block and the Square Flower --------------------------------------------------------
    Scene("j3-w01-s06", setting="lavender", beats=(
        B("Now let's turn our squares into a flower!", speaker=AIDEN, cue="flower", pause=0.4),
        B("Pink-red My Blocks: click Make a Block, and type square.", speaker=AIDEN, cue="make", pause=0.5),
        B("Under define square, snap the square repeat: repeat four, move sixty steps, turn ninety.",
          speaker=AIDEN, cue="define", pause=0.6),
        B("Now square is a brand-new block!", speaker=AIDEN, cue="newblock", pause=0.5),
        B("How far do we turn between squares? Let's read the turn card.", speaker=AIDEN, cue="card", pause=0.4),
        B("Square: ninety, a quarter turn. Triangle: one hundred twenty. Hexagon, six sides: sixty.",
          speaker=AIDEN, cue="read", pause=0.6),
        B("Six squares, like the six sides of a hexagon, so we turn sixty.", speaker=AIDEN,
          cue="six", pause=0.5),
        B("Under pen down, snap repeat six, with square and turn sixty inside.", speaker=AIDEN, cue="script",
          pause=0.5),
        B("Click the green flag!", speaker=AIDEN, cue="go", pause=4.0),
        B("The My Block hides the inside repeat, but it is still a repeat inside a repeat.", speaker=AIDEN,
          cue="hides", pause=0.6),
    ), actions=(
        A("banner", "Exercise 1.2: Square Flower", at="flower", color="green"),
        A("scratch", "My Block", blocks=[("myblocks", "define [square]"), SQUARE], x=130, y=270, w=860, h=560,
          scale=BIG, at="make", until="script", reveal=["make@0.6", "define@0.3", "define@0.5", "define@0.7"]),
        A("chip", "My Blocks: pink-red", at="make", until="newblock", x=1460, y=870, color="pink", size=44),
        A("scratch", blocks=[("myblocks", "square")], x=1240, y=420, panel=False, scale=1.4, at="newblock",
          until="card"),
        A("chip", "a brand-new block!", at="newblock@0.3", until="card", x=1460, y=620, color="pink", size=42),
        A("panel", "Turn card", at="card", until="go", x=1080, y=260, w=760, size=40,
          items=[("read@0.05", "Square: 90 (quarter turn)"), ("read@0.4", "Triangle: 120"),
                 ("read@0.7", "Hexagon (6 sides): 60")]),
        A("chip", "6 squares: turn 60", at="six@0.5", until="go", x=1460, y=720, color="orange", size=44),
        A("scratch", "Square Flower (after pen down)",
          blocks=[PEN_DOWN, ("control", "repeat [6]", [("myblocks", "square"), TURN60]), PEN_UP],
          x=130, y=270, w=860, h=680, scale=BIG, at="script", reveal=["script", "script@0.3", "script@0.5",
                                                                        "script@0.7", "script@0.9"],
          highlight=[(1, "go+0.4", "go$+3.8")]),
        A("turtle", code=FLOWER, title="Square Flower", cursor=False, x=1080, y=230, w=760, h=600, at="go",
          run="go+0.4", duration=3.4),
        A("chip", "Still a repeat inside a repeat", at="hides", x=1460, y=920, color="yellow", size=38),
    )),
    # 7. quick quiz: change the outside repeat -----------------------------------------------------------
    Scene("j3-w01-s07", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("Here is The Window again. What if we change the outside repeat from four to two?", speaker=AIDEN,
          cue="look", pause=0.4),
        B("How many squares will the cat draw?", speaker=AIDEN, cue="how", pause=3.2),
        B("Two squares! The inside repeat draws one square, and the outside repeat says how many times.",
          speaker=AIDEN, cue="two", pause=0.5),
        B("Let's test it.", speaker=AIDEN, cue="test", pause=3.2),
        B("Beep! Two squares!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "The Window", blocks=WINDOW, x=130, y=220, w=860, h=800, scale=BIG, at="quiz",
          edits=[("look@0.8", 0, "repeat [2]")],
          highlight=[(0, "look@0.6", "how$"), (1, "two@0.2", "two@0.6"), (0, "two@0.6", "two$")]),
        A("thought", "How many squares?", at="how$+0.2", until="two", x=1460, y=420),
        A("chip", "Outside repeat 2 = 2 squares", at="two@0.6", until="test", x=1460, y=870, color="orange",
          size=40),
        A("stage", x=1080, y=220, w=760, h=520, at="test", flag_at="test@0.3", sprite_scale=0.5, pen="#1F6FD1",
          actions=window_actions("test", 0.4, squares=2)),
        A("badge", ok=True, at="pixi", x=1780, y=300),
    )),
    # 8. bug hunt: The One-Square Flower --------------------------------------------------------------
    Scene("j3-w01-s08", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.5),
        B("Priya wanted a flower of six squares, but her cat draws only one square.", speaker=AIDEN, cue="priya",
          pause=0.6),
        B("Look at her script. The repeat six holds only the turn.", speaker=AIDEN, cue="look", pause=0.5),
        B("And the square repeat sits under it, not inside it.", speaker=AIDEN, cue="under", pause=0.5),
        B("Watch. The cat spins round six times, but spinning on the spot draws no line. Then it draws one square.",
          speaker=AIDEN, cue="watch", pause=0.8),
        B("Which repeat should be inside which?", speaker=AIDEN, cue="which", pause=3.2),
        B("The square repeat goes inside the repeat six, above the turn!", speaker=AIDEN, cue="fix", pause=0.4),
        B("Like a clap card outside the REPEAT card, it only happens once.", speaker=AIDEN, cue="clap",
          pause=0.5),
        B("Let's drag it up into the mouth of repeat six, and test again.", speaker=AIDEN, cue="drag", pause=4.0),
        B("Six squares. A flower! We fixed the bug!", speaker=AIDEN, cue="fixed", pause=0.4),
        B("Beep beep! Bug fixed!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The One-Square Flower", at="bug", color="navy"),
        A("scratch", "Priya's script", blocks=[FLAG, ERASE, PEN_DOWN, ("control", "repeat [6]", [TURN60]), SQUARE],
          x=130, y=250, w=860, h=810, scale=1.0, at="priya", until="drag+0.4",
          highlight=[(3, "look", "under"), (4, "look@0.5", "under"), (5, "under", "watch"),
                     (3, "watch+0.3", "watch+2.6"), (5, "watch+2.6", "watch$"), (5, "fix", "drag+0.4")]),
        A("scratch", "Priya's script (fixed)",
          blocks=[FLAG, ERASE, PEN_DOWN, ("control", "repeat [6]", [SQUARE, TURN60])],
          x=130, y=250, w=860, h=810, scale=1.0, at="drag+0.4", highlight=[(4, "drag+0.4", "drag+1.8")]),
        A("sfx", "snap", at="drag+0.4"),
        A("stage", x=1080, y=230, w=760, h=520, at="priya", until="drag+0.4", flag_at="watch@0.1",
          sprite_scale=0.5, pen="#1F6FD1",
          actions=[("watch+0.3", "turn", 60, 0.35), ("watch+0.68", "turn", 60, 0.35),
                   ("watch+1.06", "turn", 60, 0.35), ("watch+1.44", "turn", 60, 0.35),
                   ("watch+1.82", "turn", 60, 0.35), ("watch+2.2", "turn", 60, 0.35),
                   ("watch+2.6", "draw", 4, L, 1.2, -90)]),
        A("sfx", "whoosh", at="watch+0.3"),
        A("chip", "Spin, spin… no line!", at="watch+0.3", until="which", x=1460, y=850, color="orange", size=42),
        A("badge", ok=False, at="watch$", until="drag", x=1780, y=290),
        A("thought", "Which goes inside?", at="which$+0.2", until="fix", x=1460, y=850),
        A("chip", "Square repeat: inside repeat 6", at="fix", until="clap", x=1460, y=850, color="green", size=38),
        A("chip", "Outside the card = only once", at="clap", until="drag$", x=1460, y=850, color="yellow",
          size=38),
        A("turtle", code=FLOWER, title="Priya's flower (fixed)", cursor=False, x=1080, y=230, w=760, h=560,
          at="drag+0.4", run="drag+0.8", duration=3.0),
        A("badge", ok=True, at="fixed", x=1780, y=290),
        A("confetti", at="fixed", x=1460, y=500),
    )),
    # 9. my own pattern, not a copy (credit) + wiggle break -------------------------------------------------
    Scene("j3-w01-s09", setting="workshop", beats=(
        B("Your pattern is yours. You pick the numbers and the colors.", speaker=AIDEN, cue="yours", pause=0.5),
        B("If you see a pattern you love, you can learn from it. Then change it, to make it your own.",
          speaker=AIDEN, cue="love", pause=0.5),
        B("And say whose idea it was: I got the rainbow idea from Mei. That's called giving credit.",
          speaker=AIDEN, cue="say", pause=0.6),
        B("Sam copies Kai's flower, and says he made it all by himself. What could Sam say instead?",
          speaker=AIDEN, cue="sam", pause=3.0),
        B("He could say: I started from Kai's flower, and I changed the colors.", speaker=AIDEN, cue="could",
          pause=0.5),
        B("Now stand up for a wiggle break! Do our nested clap pattern, faster and faster!", speaker=AIDEN,
          cue="wiggle", pause=2.4),
        B("Clap, clap, stomp, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("wiggle", "end")], moods={"start": "happy", "sam": "thinking",
                                                                  "could": "happy", "wiggle": "proud"},
          chin=("sam", "could")),
        A("pixi", x=600, y=760, beep="pixi", moods={"wiggle": "happy"}),
        A("icons", at="yours", until="sam", x=1260, y=380, gap=290,
          items=[("star", "My own pattern", "yours@0.3"), ("heart", "Learn, then change", "love@0.6"),
                 ("person", "Say whose idea", "say@0.2")]),
        A("chip", "“I got the rainbow idea from Mei.”", at="say@0.3", until="sam", x=1260, y=640, color="yellow",
          size=36),
        A("chip", "Giving credit", at="say@0.75", until="sam", x=1260, y=760, color="green", size=44),
        A("thought", "What could Sam say?", at="sam$+0.2", until="could", x=1260, y=420),
        A("chip", "“I started from Kai's flower.”", at="could", until="wiggle", x=1260, y=460, color="green",
          size=40),
        A("chip", "“I changed the colors.”", at="could@0.6", until="wiggle", x=1260, y=580, color="green",
          size=40),
        A("bigtext", "Clap, clap, stomp!", at="wiggle@0.4", x=1260, y=500, size=72, color="orange"),
    )),
    # 10. recap and next -------------------------------------------------------------------------------
    Scene("j3-w01-s10", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Nested repeat!", speaker=AIDEN, cue="w1", pause=1.2),
        B("My Block!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Credit!", speaker=AIDEN, cue="w3", pause=1.2),
        B("A repeat inside a repeat makes amazing art.", speaker=AIDEN, cue="recap", pause=0.5),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Build The Window and the Square Flower, then fix the One-Square Flower.", speaker=AIDEN, cue="next",
          pause=0.5),
        B("Then change the numbers and colors to make a pattern of your own.", speaker=AIDEN, cue="own",
          pause=0.5),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Nested repeat!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "My Block!", at="w2", until="w2>", y=560, size=90, color="pink"),
        A("bigtext", "Credit!", at="w3", until="w3>", y=560, size=90, color="green"),
        A("chip", "A repeat inside a repeat", at="recap", until="turn", x=1200, y=470, color="orange", size=48),
        A("chip", "Inside: all the way, every time", at="recap@0.4", until="turn", x=1200, y=600, color="yellow",
          size=42),
        A("banner", "NEXT: The Window and the Square Flower", at="turn", color="green"),
        A("cards", items=["Build The Window", "Build the Square Flower", "Fix the One-Square Flower",
                          "Make your own pattern"], x=960, y=250, w=720, gap=115,
          reveal=["next@0.1", "next@0.4", "next@0.7", "own"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
