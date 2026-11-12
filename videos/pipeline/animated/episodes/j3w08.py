"""Junior Level 3 Week 8: Colors and My Own Pattern (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/3-bridge-to-python/teaching-material/lessons/week08.tex: the color-by-code warm-up
(key card A, a remix, key card B with "purpel"), t.color and t.pensize as the twins of Scratch's pen
blocks, the recipe analogy, the Exercise 8.1 worked example (black becomes blue, pen size 1 becomes 5),
the "bleu" bug hunt with the real "bad color string" message, the Two-Color Flower starter and its
credit line (no finished answer shown), remix and credit, the color-hunt wiggle break, and `def` as a
My Block as a short stretch idea.

The course's headless turtle does not check color names, so the "bleu" panel runs `exec` code that
raises the same error the real turtle raises (turtle.py: TurtleGraphicsError("bad color string: ...")),
so the Shell shows the true last line a child sees in Thonny.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

START = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.pensize(1)
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()"""

BLUE = START.replace('"black"', '"blue"')
BLUE5 = BLUE.replace("pensize(1)", "pensize(5)")
BLEU = BLUE5.replace('"blue"', '"bleu"')

# What the real turtle does at line 4: it stops with TurtleGraphicsError (see the module docstring).
BLEU_RUN = """import turtle
t = turtle.Turtle()
t.shape("turtle")
class TurtleGraphicsError(Exception):
    pass
TurtleGraphicsError.__module__ = "turtle"
raise TurtleGraphicsError("bad color string: bleu")"""

TWO_LINES = """t.color("blue")
t.pensize(5)"""

FLOWER_VIEW = """# Made by: the Kids Coding course.
# Changed by: your nickname
...
t.color("purple")   # first color
...
t.color("purple")   # CHANGE ME"""

FLOWER_STARTER = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(8)
for i in range(3):
    t.color("purple")
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)
    t.color("purple")
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)
turtle.done()"""

DEF_VIEW = """def square():
    for side in range(4):
        t.forward(60)
        t.left(90)

square()"""

DEF_RUN = """import turtle
t = turtle.Turtle()
t.color("blue")
t.pensize(3)
""" + DEF_VIEW + "\nturtle.done()"

GRID_NUMBERS = ["1221", "2112", "2112", "1221"]
GRID_GOLD_BLUE = ["GBBG", "BGGB", "BGGB", "GBBG"]
GRID_GOLD_GREEN = ["GFFG", "FGGF", "FGGF", "GFFG"]
GRID_STOPPED = ["G11G", "1GG1", "1GG1", "G11G"]

EPISODE = Episode(level="j3", week=8, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j3-w08-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is my robot friend, Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello, coders!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, our programs drew in black, with a thin pen.", speaker=AIDEN, cue="last", pause=0.5),
        B("Today, we make them ours, with colors and thick lines!", speaker=AIDEN, cue="today", pause=0.5),
        B("We will change a program that already works.", speaker=AIDEN, cue="change", pause=0.5),
        B("Ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello"),
        A("turtle", code=START, x=1000, y=220, w=640, h=560, at="last", until="today", duration=2.0, world=160),
        A("turtle", code=BLUE5, x=1000, y=220, w=640, h=560, at="today", duration=2.0, world=160),
        A("banner", "MISSION: Colors and my own pattern", at="today"),
        A("chip", "Change a working program", at="change", x=1320, y=880, color="orange", size=44),
    )),
    # 2. warm-up: color by code ----------------------------------------------------------------------
    Scene("j3-w08-s02", setting="peach", beats=(
        B("Let's warm up with color by code.", speaker=AIDEN, cue="warm", pause=0.4),
        B("Here is a grid with a number in every square.", speaker=AIDEN, cue="grid", pause=0.5),
        B("And here is a tiny program, a color key. Every one is gold. Every two is blue.", speaker=AIDEN,
          cue="key", pause=0.5),
        B("Color it in, and a pattern appears!", speaker=AIDEN, cue="color", pause=0.8),
        B("Now let's change the program. Two is green now.", speaker=AIDEN, cue="change", pause=0.8),
        B("Same program, one change, a new picture!", speaker=AIDEN, cue="same", pause=0.6),
        B("Here is another key. It says two is purpel: P, U, R, P, E, L.", speaker=AIDEN, cue="purpel",
          pause=0.5),
        B("What will the computer do at number two?", speaker=AIDEN, cue="what", pause=3.0),
        B("It stops! It does not know purpel. Python is picky about color names too.", speaker=AIDEN,
          cue="stops", pause=0.8),
    ), actions=(
        A("grid", at="grid", x=220, y=240, cell=140,
          states=[("grid", GRID_NUMBERS), ("color", GRID_GOLD_BLUE), ("change@0.6", GRID_GOLD_GREEN),
                  ("purpel", GRID_NUMBERS), ("stops", GRID_STOPPED)]),
        A("chip", '1 = "gold"', at="key@0.4", until="purpel", x=1260, y=360, color="yellow", size=52),
        A("chip", '2 = "blue"', at="key@0.7", until="change@0.6", x=1260, y=500, color="sky", size=52),
        A("chip", '2 = "green"', at="change@0.6", until="purpel", x=1260, y=500, color="green", size=52),
        A("chip", "one change, a new picture", at="same", until="purpel", x=1260, y=680, color="white", size=42),
        A("chip", '1 = "gold"', at="purpel", x=1260, y=360, color="yellow", size=52),
        A("chip", '2 = "purpel"', at="purpel@0.3", x=1260, y=500, color="white", size=52),
        A("thought", "What happens at 2?", at="what$+0.2", until="stops", x=1260, y=720),
        A("badge", ok=False, at="stops", x=1560, y=500),
        A("chip", "Error! I don't know purpel", at="stops@0.3", x=1260, y=700, color="red", size=42),
        A("pixi", x=1720, y=960, s=0.5, ground=1030, beep="stops"),
    )),
    # 3. two new lines -------------------------------------------------------------------------------
    Scene("j3-w08-s03", setting="lavender", beats=(
        B("Now, two new Python lines.", speaker=AIDEN, cue="two", pause=0.4),
        B("T dot color, blue. It is like Scratch's set pen color block.", speaker=AIDEN, cue="color", pause=0.5),
        B("The color name goes inside quote marks.", speaker=AIDEN, cue="quotes", pause=0.6),
        B("T dot pen size, five. It is like the set pen size block.", speaker=AIDEN, cue="size", pause=0.5),
        B("A bigger number draws a thicker line.", speaker=AIDEN, cue="thicker", pause=0.6),
        B("Good colors to try: orange, blue, purple, green, gold and black.", speaker=AIDEN, cue="good",
          pause=0.5),
        B("Almost everyone can tell purple and gold apart.", speaker=AIDEN, cue="apart", pause=0.8),
    ), actions=(
        A("scratch", "Scratch", blocks=[("pen", "set pen color to [blue]"), ("pen", "set pen size to [5]")],
          x=100, y=220, w=760, h=380, scale=1.15, reveal=["color", "size"]),
        A("code", code=TWO_LINES, title="Python", x=1000, y=220, w=820, h=380, size=50, shell=False,
          reveal=["color@0.4", "size@0.4"], highlight=[(1, "quotes", "quotes$+0.3"), (2, "thicker", "thicker$")]),
        A("arrow", at="color@0.4", until="good", x1=880, y1=370, x2=980, y2=370, color="navy", width=8),
        A("arrow", at="size@0.4", until="good", x1=880, y1=460, x2=980, y2=460, color="navy", width=8),
        A("chip", '" " around the color name', at="quotes", until="size", x=960, y=720, color="yellow", size=46),
        A("chip", "bigger number = thicker line", at="thicker", until="good", x=960, y=720, color="sky", size=46),
        A("chip", "orange", at="good@0.2", x=330, y=720, color="orange", size=44),
        A("chip", "blue", at="good@0.3", x=590, y=720, color="sky", size=44),
        A("chip", "purple", at="good@0.4", x=830, y=720, color="purple", size=44),
        A("chip", "green", at="good@0.5", x=1080, y=720, color="green", size=44),
        A("chip", "gold", at="good@0.65", x=1310, y=720, color="yellow", size=44),
        A("chip", "black", at="good@0.8", x=1550, y=720, color="navy", size=44),
        A("chip", "purple + gold: easy to tell apart", at="apart", x=960, y=880, color="white", size=42),
    )),
    # 4. worked example: Color My Square ---------------------------------------------------------------
    Scene("j3-w08-s04", setting="mint", beats=(
        B("A working program is like a cake recipe that already tastes good.", speaker=AIDEN, cue="recipe",
          pause=0.5),
        B("Change one thing, and taste it. Then change the next thing.", speaker=AIDEN, cue="one", pause=0.6),
        B("Let's try it! It is Exercise 8.1, Color My Square.", speaker=AIDEN, cue="try", pause=0.4),
        B("First, we run it.", speaker=AIDEN, cue="run", pause=2.8),
        B("A thin black square.", speaker=AIDEN, cue="thin", pause=0.5),
        B("We change black to blue. We leave both quote marks where they are.", speaker=AIDEN, cue="blue",
          pause=0.5),
        B("Save, and Run.", speaker=AIDEN, cue="run2", pause=2.8),
        B("A blue square, and a blue turtle!", speaker=AIDEN, cue="bluesq", pause=0.8),
    ), actions=(
        A("aiden", x=360, y=1000, s=0.75, at="recipe", until="try", moods={"start": "happy"},
          point=("one", "one$")),
        A("chip", "A working program = a tasty recipe", at="recipe@0.3", until="one", x=1180, y=420, color="pink",
          size=46),
        A("cards", items=["Change one thing", "Run it and look", "Then the next change"], x=860, y=320, w=760,
          gap=130, reveal=["one", "one@0.4", "one@0.7"], at="one", until="try"),
        A("banner", "Exercise 8.1: Color My Square", at="try", color="green"),
        A("code", code=START, title="color_square.py", x=80, y=200, w=1060, h=640, size=40, shell=False, at="try",
          until="blue@0.5", run="run$", expect=[], highlight=[(4, "blue", "blue@0.5")]),
        A("code", code=BLUE, title="color_square.py", x=80, y=200, w=1060, h=640, size=40, shell=False,
          at="blue@0.5", run="run2$", expect=[], highlight=[(4, "blue@0.5", "bluesq$")]),
        A("turtle", code=START, x=1220, y=200, w=620, h=560, at="try", until="run2$", run="run$", duration=2.0,
          world=160),
        A("turtle", code=BLUE, x=1220, y=200, w=620, h=560, at="run2$", duration=2.0, world=160),
        A("chip", '"black" → "blue"', at="blue@0.5", until="bluesq", x=1530, y=880, color="sky", size=46),
        A("chip", "One change, then Run", at="bluesq", x=1530, y=880, color="green", size=44),
    )),
    # 5. predict: a thicker pen ---------------------------------------------------------------------------
    Scene("j3-w08-s05", setting="peach", beats=(
        B("Next, the pen size. We change one to five.", speaker=AIDEN, cue="five", pause=0.5),
        B("What do you think will happen?", speaker=AIDEN, cue="predict", pause=3.0),
        B("Save, and Run.", speaker=AIDEN, cue="run", pause=2.6),
        B("A thick blue square! One change, then Run. Then the next change.", speaker=AIDEN, cue="thick",
          pause=0.6),
        B("Thick and blue! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("code", code=BLUE5, title="color_square.py", x=80, y=200, w=1060, h=640, size=40, shell=False,
          run="run$", expect=[], highlight=[(5, "five@0.4", "thick$")]),
        A("turtle", code=BLUE, x=1220, y=200, w=620, h=560, until="run$", duration=0.1, world=160),
        A("chip", "pensize(1) → pensize(5)", at="five@0.4", until="predict$", x=1530, y=880, color="yellow",
          size=40),
        A("thought", "Thin or thick?", at="predict$+0.2", until="run", x=1530, y=880),
        A("turtle", code=BLUE5, x=1220, y=200, w=620, h=560, at="run$", duration=2.0, world=160),
        A("badge", ok=True, at="thick", x=1780, y=270),
        A("pixi", x=1720, y=980, s=0.45, at="pixi", ground=1040, beep="pixi"),
    )),
    # 6. bug hunt: a color name spelled wrong -------------------------------------------------------------
    Scene("j3-w08-s06", setting="mint", beats=(
        B("Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.4),
        B("Here is the same program, with one tiny change. The color says bleu: B, L, E, U.", speaker=AIDEN,
          cue="bleu", pause=0.5),
        B("Let's run it.", speaker=AIDEN, cue="run", pause=2.2),
        B("The turtle does not draw, and red text appears in the Shell.", speaker=AIDEN, cue="red", pause=0.5),
        B("Read the last line: bad color string, bleu.", speaker=AIDEN, cue="last", pause=0.5),
        B("Python says: I don't know a color called bleu.", speaker=AIDEN, cue="says", pause=0.5),
        B("Which line has the color? How do we fix it?", speaker=AIDEN, cue="which", pause=3.0),
        B("Line four! We spell it B, L, U, E, save, and run again.", speaker=AIDEN, cue="fix", pause=3.0),
        B("It works! Color names must be spelled right.", speaker=AIDEN, cue="works", pause=0.5),
        B("Bad color string? Not anymore!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The color typo", at="bug", color="navy"),
        A("code", code=BLEU, exec=BLEU_RUN, title="color_square.py", x=60, y=180, w=1160, h=820, size=38,
          shell_h=200, at="bleu", until="fix", run="run$", allow_error=True, error_line=4,
          expect=["turtle.TurtleGraphicsError: bad color string: bleu"],
          highlight=[(4, "bleu", "bleu$"), (4, "which$", "fix")]),
        A("code", code=BLUE5, title="color_square.py", x=60, y=180, w=1160, h=820, size=38, shell_h=200,
          at="fix", run="fix@0.8", expect=[], highlight=[(4, "fix", "fix@0.8")]),
        A("chip", "Expected: a blue square", at="run", until="red", x=1560, y=400, color="green", size=40),
        A("badge", ok=False, at="red", until="fix", x=1560, y=560),
        A("chip", "bad color string: bleu", at="last", until="fix", x=1560, y=400, color="red", size=40),
        A("chip", "I don't know bleu!", at="says", until="fix", x=1560, y=720, color="yellow", size=42),
        A("thought", "Which line?", at="which$+0.2", until="fix", x=1560, y=880),
        A("turtle", code=BLUE5, x=1280, y=200, w=580, h=500, at="fix@0.8", duration=2.0, world=160),
        A("badge", ok=True, at="works", x=1790, y=270),
        A("confetti", at="works", x=1570, y=450),
        A("chip", "Spell colors right", at="works", x=1570, y=820, color="green", size=44),
    )),
    # 7. the Two-Color Flower starter and its credit line ----------------------------------------------------
    Scene("j3-w08-s07", setting="lavender", beats=(
        B("Next comes Exercise 8.2, the Two-Color Flower.", speaker=AIDEN, cue="next", pause=0.4),
        B("The starter draws six purple squares, like the flower from last week.", speaker=AIDEN, cue="six",
          pause=0.6),
        B("You change the second color, so the squares take turns.", speaker=AIDEN, cue="second", pause=0.6),
        B("At the top is a credit line. Made by: the Kids Coding course. Changed by: your nickname.",
          speaker=AIDEN, cue="credit", pause=0.8),
    ), actions=(
        A("banner", "Exercise 8.2: Two-Color Flower", at="next", color="green"),
        A("code", code=FLOWER_VIEW, title="two_color_flower.py", x=60, y=200, w=1120, h=560, size=38,
          shell=False, at="next", highlight=[(6, "second", "second$+0.4"), (1, "credit", "credit@0.5"),
                                             (2, "credit@0.5", "end")]),
        A("turtle", code=FLOWER_STARTER, x=1240, y=200, w=600, h=560, at="six", duration=4.0, world=150),
        A("chip", "change the second color", at="second@0.4", until="credit", x=620, y=880, color="purple",
          size=44),
        A("chip", "Changed by: a nickname", at="credit@0.6", x=620, y=880, color="orange", size=44),
    )),
    # 8. remix and credit -------------------------------------------------------------------------------
    Scene("j3-w08-s08", setting="sky", beats=(
        B("Starting from someone's program and changing it is called a remix.", speaker=AIDEN, cue="remix",
          pause=0.4),
        B("Remixing is great! Programmers do it all the time.", speaker=AIDEN, cue="great", pause=0.5),
        B("But we always say whose idea we started from. That is called giving credit.", speaker=AIDEN,
          cue="credit", pause=0.6),
        B("Your friend Leo drew a cool flower, and you want to remix it. What do you do first?", speaker=AIDEN,
          cue="leo", pause=3.0),
        B("Ask Leo! Then write at the top: Idea from Leo.", speaker=AIDEN, cue="ask", pause=0.6),
        B("Use a nickname, never your real name, because files can travel.", speaker=AIDEN, cue="nick",
          pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "leo": "thinking", "ask": "happy"},
          chin=("leo", "ask")),
        A("chip", "remix = change someone's program", at="remix@0.4", until="leo", x=1060, y=320, color="purple",
          size=44),
        A("chip", "credit = say whose idea", at="credit@0.5", until="leo", x=1060, y=460, color="orange",
          size=44),
        A("thought", "What first?", at="leo$+0.2", until="ask", x=1060, y=420),
        A("icons", at="ask", until="nick", x=1060, y=420, gap=420,
          items=[("person", "Ask Leo", "ask"), ("file", "Idea from: Leo", "ask@0.5")]),
        A("icons", at="nick", x=1060, y=420, gap=420, crossed=[1],
          items=[("star", "Nickname", "nick@0.1"), ("person", "Real name", "nick@0.3")]),
    )),
    # 9. wiggle break: color hunt -------------------------------------------------------------------------
    Scene("j3-w08-s09", setting="workshop", beats=(
        B("Wiggle break! Let's play color hunt.", speaker=AIDEN, cue="wiggle", pause=0.4),
        B("When I call a color, run and touch something that color.", speaker=AIDEN, cue="rule", pause=0.5),
        B("Blue!", speaker=AIDEN, cue="c1", pause=3.0),
        B("Orange!", speaker=AIDEN, cue="c2", pause=3.0),
        B("G, R, E, N!", speaker=AIDEN, cue="c3", pause=0.6),
        B("Bad color string! Freeze!", speaker=PIXI, cue="err", pause=1.2),
        B("Great freezing, color hunters!", speaker=AIDEN, cue="done", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("wiggle", "rule"), ("done", "end")],
          moods={"start": "happy", "c3": "surprised", "done": "proud"}),
        A("pixi", x=640, y=760, beep="err", moods={"err": "surprised", "done": "happy"},
          path=[("c1", 640, 760), ("c1+1.4", 900, 760), ("c2", 900, 760), ("c2+1.4", 700, 760)]),
        A("chip", "WIGGLE BREAK: color hunt", at="wiggle", until="c1", x=1300, y=420, color="orange", size=48),
        A("bigtext", "blue!", at="c1", until="c2", x=1300, y=420, size=100, color="blue"),
        A("bigtext", "orange!", at="c2", until="c3", x=1300, y=420, size=100, color="orange"),
        A("bigtext", "G-R-E-N?", at="c3", until="done", x=1300, y=420, size=100, color="red"),
        A("chip", "Freeze!", at="err", until="done", x=1300, y=600, color="red", size=48),
        A("confetti", at="done", x=1200, y=420),
    )),
    # 10. stretch: def as a My Block --------------------------------------------------------------------------
    Scene("j3-w08-s10", setting="peach", beats=(
        B("Here is a stretch idea, for when you are ready.", speaker=AIDEN, cue="stretch", pause=0.4),
        B("Remember making a My Block called square in Scratch? Python has My Blocks too.", speaker=AIDEN,
          cue="remember", pause=0.5),
        B("Def square, with a colon, is like the pink define block.", speaker=AIDEN, cue="def", pause=0.5),
        B("The lines pushed in under it are what the block does.", speaker=AIDEN, cue="pushed", pause=0.5),
        B("And square, with brackets, uses the block.", speaker=AIDEN, cue="use", pause=0.5),
        B("That is Exercise 8.3, My Square Block.", speaker=AIDEN, cue="ex", pause=0.8),
    ), actions=(
        A("chip", "STRETCH IDEA", at="stretch", x=960, y=110, color="purple", size=46),
        A("scratch", "Scratch", blocks=[("myblocks", "define [square]"),
                                        ("control", "repeat [4]", [("motion", "move [60] steps"),
                                                                   ("motion", "turn ↺ [90] degrees")])],
          x=80, y=200, w=720, h=520, scale=1.0, at="remember"),
        A("code", code=DEF_VIEW, title="square_block.py", x=860, y=200, w=980, h=520, size=42, shell=False,
          at="def", highlight=[(1, "def", "def$+0.3"), (2, "pushed", "pushed$"), (3, "pushed", "pushed$"),
                               (4, "pushed", "pushed$"), (6, "use", "use$+0.3")]),
        A("chip", "def square(): = define square", at="def@0.5", until="use", x=960, y=840, color="pink",
          size=44),
        A("chip", "square() = use the block", at="use@0.4", until="ex", x=960, y=840, color="pink", size=44),
        A("chip", "Exercise 8.3: My Square Block (stretch)", at="ex", x=960, y=840, color="white", size=42),
    )),
    # 11. recap and next ---------------------------------------------------------------------------------------
    Scene("j3-w08-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Color!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Pen size!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Credit!", speaker=AIDEN, cue="w3", pause=1.2),
        B("Change one thing, then Run. Keep the quote marks, and spell colors right.", speaker=AIDEN,
          cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Color your square, make the Two-Color Flower, and try My Square Block if you are ready.",
          speaker=AIDEN, cue="next", pause=0.6),
        B("Next week is the project studio. You can choose a Scratch game or a Python postcard!", speaker=AIDEN,
          cue="preview", pause=0.5),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Color!", at="w1", until="w1>", y=560, size=90, color="blue"),
        A("bigtext", "Pen size!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Credit!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("chip", "One change, then Run", at="recap", until="turn", x=1200, y=520, color="orange", size=48),
        A("chip", '"blue" not "bleu"', at="recap@0.5", until="turn", x=1200, y=650, color="sky", size=46),
        A("banner", "NEXT: Color My Square and Two-Color Flower", at="turn", color="green"),
        A("cards", items=["Color My Square", "Two-Color Flower", "My Square Block (stretch)"], x=980, y=300,
          w=700, gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "Next week: Project Studio", at="preview", x=1330, y=760, color="yellow", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
