"""Level 1 Week 8: Loops in Python (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, Scene

MOVE = ("motion", "move [100] steps")
TURN = ("motion", "turn ↺ [90] degrees")

EIGHT_LINES = """t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)"""

LOOP3 = """for i in range(4):
    t.forward(100)
    t.left(90)"""

SQUARE = """import turtle
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()"""

TRIANGLE = SQUARE.replace("range(4)", "range(3)").replace("left(90)", "left(120)")

NESTED_PREVIEW = """for color in PALETTE:
    t.color(color)
    for side in range(4):
        t.forward(100)
        t.left(90)
    ..."""

# The finished picture only (the canvas hides this code; the exercise's answer is never shown as code).
FLOWER_DRAWING = """import turtle
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]
t = turtle.Turtle()
t.pensize(3)
for color in PALETTE:
    t.color(color)
    for side in range(4):
        t.forward(100)
        t.left(90)
    t.left(45)
turtle.done()"""

BUG_RANGE = TRIANGLE.replace("range(3)", "range(2)")
BUG_INDENT = TRIANGLE.replace("    t.left(120)", "t.left(120)")
MISMATCH = """for i in range(3):
    t.forward(100)
      t.left(120)"""

PALETTE_CODES = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

EPISODE = Episode(level=1, week=8, scenes=(
    Scene("w08-s01", setting="workshop", lead_in=0.2, beats=(
        B("Welcome back to Kids Coding!", cue="welcome", pause=0.3),
        B("Pixel types forward and left, four times, to draw a square.", cue="types", pause=0.3),
        B("‘This feels familiar,’", speaker=NOVA, cue="familiar", pause=0.1),
        B("Nova says.", cue="says"),
        B("‘We used a Scratch repeat block for this!’", speaker=NOVA, cue="scratch", pause=0.3),
        B("Python can loop too.", cue="loop"),
        B("But instead of a block's colored border, spaces show which instructions repeat.", cue="spaces",
          pause=0.3),
        B("Can we shrink eight lines into three?", cue="question", pause=2.8),
    ), actions=(
        A("nova", x=300, y=960, enter="left", wave="welcome", moods={"familiar": "happy", "question": "thinking"},
          chin=("question", "end"), look={"types": 0.6}),
        A("pixel", x=620, y=760, drop=True, beep=("types", "types$"), moods={"question": "thinking"}),
        A("banner", "MISSION: Make repetition shorter", at="types"),
        A("code", title="square.py", code=EIGHT_LINES, x=930, y=180, w=850, h=520, shell=False, at="types",
          type=("types", "types$+0.4"), until="question$",
          highlight=[(1, "familiar", "says>"), (2, "familiar", "says>"), (3, "says>", "scratch@0.5"),
                     (4, "says>", "scratch@0.5"), (5, "scratch@0.5", "scratch$"), (6, "scratch@0.5", "scratch$"),
                     (7, "scratch$", "loop"), (8, "scratch$", "loop")]),
        A("bubble", "This feels familiar!", who="nova", x=300, y=960, at="familiar", until="scratch"),
        A("bubble", "We used a repeat block!", who="nova", x=300, y=960, at="scratch", until="loop$"),
        A("scratch", blocks=[("control", "repeat [4]", [MOVE, TURN])], x=1060, y=705, scale=0.8, panel=False,
          at="scratch", until="question"),
        A("chip", "In Python, spaces can show a group", at="spaces", until="end", x=1320, y=990, color="yellow",
          size=40),
        A("thought", "", at="question$+0.2", until="end", x=500, y=330),
        A("code", title="loop.py", code=LOOP3, x=930, y=300, w=850, h=300, shell=False, at="question$+1.2"),
        A("chip", "8 lines → 3 lines", at="question$+1.6", x=1320, y=680, color="green", size=40),
    )),
    Scene("w08-s02", setting="sky", beats=(
        B("Read this line: for i in range four, colon.", cue="line", pause=0.4),
        B("It means: repeat the pushed-in lines four times.", cue="means", pause=0.3),
        B("The colon says a group is coming.", cue="colon", pause=0.3),
        B("Every line inside starts with the same four spaces.", cue="spaces", pause=0.2),
        B("That's called indentation.", cue="indent", pause=0.4),
        B("Thonny helps: after a colon, press Return, and it pushes the next line in for you.", cue="thonny",
          pause=0.4),
        B("Range four gives four numbers: zero, one, two, three.", cue="numbers", pause=0.4),
        B("Python starts counting at zero, but there are still four numbers, so the loop runs four times.",
          cue="still", pause=0.4),
        B("The i keeps count, even when our drawing doesn't use it.", cue="count", pause=0.6),
    ), actions=(
        A("chip", "for i in range(4):", at="line", x=960, y=110, color="navy", size=50),
        A("code", title="loop.py", code="for i in range(4):\n    print(i)", x=120, y=230, w=900, h=700,
          shell_h=300, reveal=["line", "means"], run="numbers@0.3", expect=["0", "1", "2", "3"],
          highlight=[(1, "line", "means"), (2, "means", "colon"), (1, "colon", "spaces"), (2, "spaces", "thonny")]),
        A("arrow", "indentation", at="indent", until="numbers", x1=560, y1=640, x2=270, y2=425, color="blue", size=36),
        A("chip", "colon → a group follows", at="colon", until="numbers", x=1450, y=330, color="orange"),
        A("chip", "4 spaces → inside the loop", at="spaces", until="numbers", x=1450, y=450, color="green"),
        A("chip", "Return after : → Thonny pushes in", at="thonny", until="numbers", x=1450, y=570, color="sky",
          size=38),
        A("listrow", "range(4)", at="numbers+0.35", x=1450, y=440, cell=140, indexes=False,
          states=[("numbers", []), ("numbers@0.5", [0]), ("numbers@0.65", [0, 1]), ("numbers@0.8", [0, 1, 2]),
                  ("numbers@0.92", [0, 1, 2, 3])],
          highlight=[("count", "count+0.6", 0), ("count+0.6", "count+1.2", 1), ("count+1.2", "count+1.8", 2),
                     ("count+1.8", "end", 3)]),
        A("chip", "range(4) → 0, 1, 2, 3 = 4 times", at="still@0.4", x=1450, y=620, color="yellow", size=40),
        A("box", "i", at="count", x=1450, y=860, values=[("count", 0), ("count+0.6", 1), ("count+1.2", 2),
                                                          ("count+1.8", 3)]),
    )),
    Scene("w08-s03", setting="lavender", beats=(
        B("For a square, put t dot forward one hundred and t dot left ninety inside range four.", cue="square",
          pause=0.3),
        B("The secret shape rule is back: repeats equal sides, and the turn equals three hundred sixty divided by "
          "sides.", cue="rule", pause=0.4),
        B("A triangle repeats three times and turns one hundred twenty.", cue="triangle", pause=0.6),
        B("A loop can even hold another loop.", cue="nested", pause=0.2),
        B("That's a nested loop.", cue="called", pause=0.4),
        B("In Square Flower, the outer loop takes one color at a time from a list called PALETTE, and the inner "
          "loop draws a whole square.", cue="flower", pause=0.4),
        B("The inner lines get eight spaces: four, then four more.", cue="eight", pause=0.8),
    ), actions=(
        A("code", title="square.py", code=SQUARE, x=120, y=200, w=900, h=560, shell=False,
          type=("square", "square$"), until="triangle",
          highlight=[(4, "square@0.75", "square$+0.3"), (5, "square@0.2", "square@0.5"),
                     (6, "square@0.5", "square@0.75"), (4, "rule@0.2", "rule@0.5"), (6, "rule@0.6", "rule$")]),
        A("turtle", code=SQUARE, x=1160, y=200, w=640, h=560, at="square", run="square$", duration=2.6,
          until="triangle"),
        A("chip", "repeats = sides", at="rule@0.2", until="nested", x=570, y=850, color="orange", size=44),
        A("chip", "turn = 360 ÷ sides", at="rule@0.6", until="nested", x=570, y=960, color="green", size=44),
        A("code", title="triangle.py", code=TRIANGLE, x=120, y=200, w=900, h=560, shell=False, at="triangle",
          until="nested", highlight=[(4, "triangle@0.2", "triangle@0.6"), (6, "triangle@0.6", "nested")]),
        A("turtle", code=TRIANGLE, x=1160, y=200, w=640, h=560, at="triangle", run="triangle+0.3", duration=2.2,
          until="nested"),
        A("chip", "3 sides → turn 120°", at="triangle@0.6", until="nested", x=1480, y=850, color="sky", size=40),
        A("chip", "Nested loop = a loop inside a loop", at="nested", x=960, y=110, color="orange", size=44),
        A("listrow", "PALETTE", at="flower", x=960, y=330, cell=200, indexes=False, items=PALETTE_CODES,
          highlight=[("flower@0.15", "flower@0.3", 0), ("flower@0.3", "flower@0.45", 1),
                     ("flower@0.45", "flower@0.6", 2), ("flower@0.6", "flower$", 3)]),
        A("code", title="square_flower.py", code=NESTED_PREVIEW, x=120, y=480, w=1000, h=420, shell=False,
          at="nested+0.35", highlight=[(1, "flower@0.1", "flower@0.55"), (3, "flower@0.6", "flower$"),
                                  (4, "eight", "end"), (5, "eight", "end")]),
        A("chip", "outer loop", at="flower@0.1", x=960, y=592, color="orange", size=32),
        A("chip", "inner loop", at="flower@0.6", x=960, y=690, color="green", size=32),
        A("turtle", code=FLOWER_DRAWING, x=1200, y=480, w=600, h=420, at="flower", run="flower@0.2",
          duration=6.0, title="Square Flower (preview)"),
        A("chip", "8 spaces: four, then four more", at="eight", x=620, y=975, color="yellow", size=40),
    )),
    Scene("w08-s04", setting="mint", beats=(
        B("Time for a bug hunt!", cue="bug", pause=0.3),
        B("Nova wants a triangle, but the turtle draws only two sides.", cue="two", pause=0.4),
        B("Count the trips: the code says range two.", cue="trips", pause=0.4),
        B("That's an off-by-one bug: the loop runs one time too few.", cue="offby", pause=2.4),
        B("A triangle has three sides, so change two to three, and test.", cue="fix1", pause=2.0),
        B("Next, Nova's triangle is one long straight line!", cue="line", pause=0.4),
        B("Look at the spaces.", cue="look", pause=2.4),
        B("t dot left one hundred twenty isn't pushed in, so it's outside the loop, and it turns only once, at "
          "the end.", cue="outside", pause=0.4),
        B("Push it in four spaces, under t dot forward, and test.", cue="fix2", pause=2.0),
        B("If the spaces don't match, Python shows a red IndentationError.", cue="error", pause=0.6),
        B("Pause before each repair: what evidence tells us which one thing to change?", cue="pause", pause=3.0),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        # clue 1: off by one
        A("code", title="triangle.py", code=BUG_RANGE, x=120, y=200, w=900, h=560, shell=False, at="two",
          until="fix1", highlight=[(4, "trips", "fix1")]),
        A("turtle", code=BUG_RANGE, x=1160, y=200, w=640, h=560, at="two", run="two@0.3", duration=1.8,
          until="fix1"),
        A("code", title="triangle.py", code=TRIANGLE, x=120, y=200, w=900, h=560, shell=False, at="fix1",
          until="line", highlight=[(4, "fix1@0.5", "fix1$+1.0")]),
        A("turtle", code=TRIANGLE, x=1160, y=200, w=640, h=560, at="fix1", run="fix1$", duration=1.8,
          until="line"),
        A("chip", "Clue 1: loop runs one time too few", at="offby", until="line", x=580, y=860, color="yellow",
          size=40),
        A("thought", "Which number?", at="offby$+0.2", until="fix1", x=1480, y=900),
        A("badge", ok=False, at="two@0.7", until="fix1", x=1720, y=310),
        A("badge", ok=True, at="fix1$+1.8", until="line", x=1720, y=310),
        # clue 2: a line outside the loop
        A("code", title="triangle.py", code=BUG_INDENT, x=120, y=200, w=900, h=560, shell=False, at="line",
          until="fix2", highlight=[(6, "look", "fix2"), (5, "look", "look$")]),
        A("turtle", code=BUG_INDENT, x=1160, y=200, w=640, h=560, at="line", run="line@0.3", duration=2.0,
          until="fix2"),
        A("code", title="triangle.py", code=TRIANGLE, x=120, y=200, w=900, h=560, shell=False, at="fix2",
          highlight=[(6, "fix2@0.3", "fix2$+1.0")]),
        A("turtle", code=TRIANGLE, x=1160, y=200, w=640, h=560, at="fix2", run="fix2$", duration=1.8,
          until="error"),
        A("chip", "Clue 2: a line outside the loop", at="outside", until="pause", x=580, y=860, color="yellow",
          size=40),
        A("thought", "Spaces?", at="look$+0.2", until="outside", x=1480, y=900),
        A("badge", ok=False, at="line@0.7", until="fix2", x=1720, y=310),
        A("badge", ok=True, at="fix2$+1.8", until="error", x=1720, y=310),
        A("confetti", at="fix2$+1.8", x=1480, y=420),
        # spaces that do not match
        A("code", title="oops.py", code=MISMATCH, x=1100, y=220, w=760, h=480, size=30, at="error", run="error@0.5",
          allow_error=True, error_line=3, expect=["IndentationError: unexpected indent"]),
        A("chip", "Use evidence. Fix one thing. Test.", at="pause", x=580, y=860, color="green", size=40),
        A("thought", "", at="pause$+0.2", until="end", x=1480, y=870),
        A("nova", x=1040, y=1065, s=0.5, moods={"two": "confused", "fix1$+1.8": "happy", "line": "surprised",
                                                "look": "thinking", "fix2$+1.8": "proud"}),
    )),
    Scene("w08-s05", setting="workshop", tail=0.8, beats=(
        B("Python loops are ready!", cue="ready", pause=0.4),
        B("A for loop repeats the pushed-in lines.", cue="forloop", pause=0.2),
        B("Range sets how many times, the colon starts the group, and four matching spaces show what belongs "
          "inside.", cue="parts", pause=0.4),
        B("Stuck?", cue="stuck", pause=0.3),
        B("Try three before me: read the red message, check the workbook, and ask your partner.", cue="three",
          pause=0.3),
        B("Then use the help sentence, like Nova:", cue="sentence", pause=0.1),
        B("‘I expected a triangle, but a straight line happened. I tried counting the spaces.’", speaker=NOVA,
          cue="help", pause=0.4),
        B("Now build Loop Square, then write a square loop and a hexagon loop for Polygon Party.", cue="next",
          pause=0.3),
        B("Predict the shape before you press Run.", cue="predict", pause=0.4),
        B("Happy coding!", cue="happy", pause=0.4),
    ), actions=(
        A("door", "DOOR 8", x=1560, y=920, open="ready"),
        A("nova", x=260, y=1010, s=0.72, wave=[("ready", "forloop"), ("happy", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("code", title="loop.py", code=LOOP3, x=640, y=200, w=760, h=300, shell=False, at="forloop",
          until="stuck", highlight=[(1, "parts", "parts@0.25"), (1, "parts@0.25", "parts@0.5"),
                                    (2, "parts@0.55", "parts$"), (3, "parts@0.55", "parts$")]),
        A("chip", "range • colon • 4 spaces", at="parts", until="stuck", x=1020, y=580, color="orange", size=44),
        A("icons", at="three", until="sentence", x=1000, y=320, gap=300,
          items=[("warning", "Red message", "three@0.3"), ("book", "Workbook", "three@0.55"),
                 ("person", "Partner", "three@0.8")]),
        A("chip", "I expected… but… happened. I tried…", at="sentence", until="next", x=1060, y=280,
          color="yellow", size=44),
        A("bubble", "I expected a triangle, but a straight line happened. I tried counting the spaces.", x=330,
          y=700, at="help", until="next", max_width=560, size=36),
        A("banner", "NEXT: Loop Square + Polygon Party", at="next", color="green"),
        A("cards", at="next", x=620, y=230, w=700, gap=110,
          items=["Build Loop Square", "Polygon Party: a square loop", "Polygon Party: a hexagon loop",
                 "Predict before Run"],
          reveal=["next@0.1", "next@0.6", "next@0.8", "predict"]),
        A("chip", "Happy coding!", at="happy", x=960, y=780, color="orange", size=48),
    )),
))
