"""Junior Level 3 Week 6: Hello, Python! (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/3-bridge-to-python/teaching-material/lessons/week06.tex: the "Python is picky" warm-up
cards, a tour of Thonny in simple mode (Run, Stop, Editor, Shell, turtle window), the word twins of
the move and turn blocks, the Hello, Turtle! worked example (50 becomes 150), the typo hunt with
Thonny's real red text (t.forwad), the picky-robot wiggle break, and saving files with clear names.
Exercise 6.2 (Finish the Square) is named but never shown solved.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

HELLO = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.forward(50)
t.left(90)
turtle.done()"""

HELLO_150 = HELLO.replace("t.forward(50)", "t.forward(150)")

BUGGY = HELLO.replace("t.forward(50)", "t.forwad(100)")
FIXED = HELLO.replace("t.forward(50)", "t.forward(100)")

TWINS = """t.forward(100)
t.left(90)"""

MOVE = ("motion", "move [100] steps")
TURN = ("motion", "turn ↺ [90] degrees")
BIG = 1.25  # block scale: big enough for young eyes

EPISODE = Episode(level="j3", week=6, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j3-w06-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is my robot friend, Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello, coders!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, every Scratch block found its word twin.", speaker=AIDEN, cue="last", pause=0.5),
        B("Today, we use the words for real, in Python!", speaker=AIDEN, cue="today", pause=0.5),
        B("Scratch blocks can never be spelled wrong. Words can.", speaker=AIDEN, cue="spell", pause=0.4),
        B("And Python is very picky about spelling.", speaker=AIDEN, cue="picky", pause=0.5),
        B("Are you ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello"),
        A("scratch", blocks=[MOVE], x=900, y=330, w=520, h=150, panel=False, scale=BIG, at="last"),
        A("arrow", at="last@0.5", x1=1180, y1=440, x2=1180, y2=560, color="navy", width=8),
        A("chip", "t.forward(100)", at="last@0.7", x=1180, y=630, color="sky", size=48),
        A("banner", "MISSION: Hello, Python!", at="today"),
        A("chip", "Python is picky!", at="picky", x=1180, y=800, color="orange", size=48),
    )),
    # 2. warm-up: Python is picky ---------------------------------------------------------------------
    Scene("j3-w06-s02", setting="peach", beats=(
        B("Let's warm up with a game called Python is picky.", speaker=AIDEN, cue="game", pause=0.5),
        B("Here are two lines. One is right, and one has a tiny mistake.", speaker=AIDEN, cue="two", pause=0.5),
        B("Can you spot the difference?", speaker=AIDEN, cue="spot", pause=3.0),
        B("Yes! The second one is missing an r. Python does not know forwad.", speaker=AIDEN, cue="r",
          pause=0.6),
        B("Here is another one. Look closely.", speaker=AIDEN, cue="another", pause=0.4),
        B("What is different this time?", speaker=AIDEN, cue="diff", pause=3.0),
        B("A capital L! These Python words use small letters.", speaker=AIDEN, cue="capital", pause=0.5),
        B("Great detective eyes! Programmers do this every day.", speaker=AIDEN, cue="eyes", pause=0.4),
        B("Beep! Picky, picky, picky!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"spot": "thinking", "r": "happy", "diff": "thinking",
                                               "capital": "happy", "eyes": "proud"},
          chin=[("spot", "r"), ("diff", "capital")]),
        A("pixi", x=1720, y=880, s=0.55, ground=980, beep="pixi"),
        A("chip", "t.forward(100)", at="two@0.3", until="another", x=1000, y=360, color="white", size=56),
        A("chip", "t.forwad(100)", at="two@0.6", until="another", x=1000, y=560, color="white", size=56),
        A("thought", "What is different?", at="spot$+0.2", until="r", x=1480, y=300),
        A("badge", ok=True, at="r", until="another", x=1340, y=360),
        A("badge", ok=False, at="r", until="another", x=1340, y=560),
        A("chip", "missing r", at="r@0.3", until="another", x=1000, y=740, color="red", size=44),
        A("chip", "t.left(90)", at="another", x=1000, y=360, color="white", size=56),
        A("chip", "t.Left(90)", at="another@0.5", x=1000, y=560, color="white", size=56),
        A("thought", "Look closely!", at="diff$+0.2", until="capital", x=1480, y=300),
        A("badge", ok=True, at="capital", x=1300, y=360),
        A("badge", ok=False, at="capital", x=1300, y=560),
        A("chip", "small letters", at="capital@0.4", x=1000, y=740, color="green", size=44),
        A("magnifier", x=700, y=560, at="two", until="r", path=[("spot", 700, 560), ("spot$+2.4", 1120, 560)]),
        A("magnifier", x=700, y=560, at="another@0.5", until="capital", path=[("diff", 700, 560), ("diff$+2.4", 900, 560)]),
    )),
    # 3. meet Thonny ---------------------------------------------------------------------------------
    Scene("j3-w06-s03", setting="sky", beats=(
        B("This is Thonny, the app where we write Python.", speaker=AIDEN, cue="thonny", pause=0.5),
        B("It is in simple mode, so it shows big buttons with words under them.", speaker=AIDEN, cue="simple",
          pause=0.5),
        B("The green Run button is our green flag.", speaker=AIDEN, cue="run", pause=0.5),
        B("The red Stop button stops the program. If anything gets stuck, click Stop. Nothing breaks.",
          speaker=AIDEN, cue="stop", pause=0.6),
        B("The big white part is the Editor. Our program lives here.", speaker=AIDEN, cue="editor", pause=0.5),
        B("The part at the bottom is the Shell. Python talks back there.", speaker=AIDEN, cue="shell", pause=0.5),
        B("And the turtle window is our stage. The turtle is our sprite!", speaker=AIDEN, cue="stage", pause=0.5),
        B("Its pen is already down, so it draws wherever it walks.", speaker=AIDEN, cue="pen", pause=0.6),
        B("Can you point to the Run button?", speaker=AIDEN, cue="point", pause=3.0),
        B("There it is, at the top! Green, like the green flag.", speaker=AIDEN, cue="there", pause=0.8),
    ), actions=(
        A("code", code=HELLO, title="hello.py", x=80, y=170, w=1000, h=780, size=40, at="thonny",
          run="stage@0.3", expect=[]),
        A("chip", "Simple mode: big buttons", at="simple", until="run", x=1480, y=212, color="white", size=42),
        A("chip", "Run = green flag", at="run", until="stop$", x=1480, y=212, color="green", size=46),
        A("arrow", at="run@0.3", until="stop$", x1=1250, y1=212, x2=1070, y2=212, color="navy", width=8),
        A("chip", "Stop = nothing breaks", at="stop", until="stop$", x=1480, y=330, color="red", size=42),
        A("chip", "Editor: my program", at="editor", until="stage", x=1480, y=450, color="sky", size=44),
        A("arrow", at="editor@0.3", until="stage", x1=1250, y1=450, x2=1000, y2=450, color="navy", width=8),
        A("chip", "Shell: Python talks back", at="shell", until="stage", x=1480, y=840, color="yellow", size=42),
        A("arrow", at="shell@0.3", until="stage", x1=1230, y1=840, x2=1000, y2=840, color="navy", width=8),
        A("turtle", code=HELLO, x=1160, y=300, w=660, h=500, at="stage", run="stage@0.3", duration=2.0,
          until="point"),
        A("chip", "turtle = our sprite", at="stage@0.5", until="point", x=1490, y=880, color="orange", size=44),
        A("thought", "Where is Run?", at="point$+0.2", until="there", x=1480, y=520),
        A("pointer", x=1480, y=520, at="there", path=[("there", 1480, 520), ("there+1.0", 1030, 220)]),
        A("chip", "Run = green flag", at="there", x=1480, y=760, color="green", size=46),
    )),
    # 4. word twins ----------------------------------------------------------------------------------
    Scene("j3-w06-s04", setting="lavender", beats=(
        B("Every turtle line has a Scratch twin.", speaker=AIDEN, cue="twins", pause=0.5),
        B("Move one hundred steps is t dot forward, one hundred.", speaker=AIDEN, cue="move", pause=0.6),
        B("The number in the brackets is like the white oval in Scratch.", speaker=AIDEN, cue="oval", pause=0.6),
        B("Turn left ninety degrees is t dot left, ninety. That is a quarter turn.", speaker=AIDEN, cue="turn",
          pause=0.6),
        B("Small letters, a dot, and both brackets. Python needs every one.", speaker=AIDEN, cue="need",
          pause=0.6),
        B("Twins! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Scratch", blocks=[MOVE, TURN], x=100, y=230, w=760, h=420, scale=BIG,
          reveal=["move", "turn"]),
        A("code", code=TWINS, title="Python", x=1040, y=230, w=780, h=420, size=48, shell=False,
          reveal=["move@0.5", "turn@0.6"], highlight=[(1, "oval", "oval$")]),
        A("arrow", at="move@0.4", until="turn", x1=880, y1=420, x2=1020, y2=420, color="navy", width=8),
        A("arrow", at="turn@0.5", until="need", x1=880, y1=520, x2=1020, y2=520, color="navy", width=8),
        A("chip", "( ) = the white oval", at="oval", until="turn", x=960, y=780, color="yellow", size=46),
        A("chip", "quarter turn = 90", at="turn@0.6", until="need", x=960, y=780, color="sky", size=46),
        A("chip", "small letters • a dot • ( )", at="need", x=960, y=780, color="orange", size=46),
        A("pixi", x=1720, y=980, s=0.5, at="need", ground=1040, beep="pixi"),
    )),
    # 5. worked example: Hello, Turtle! ------------------------------------------------------------
    Scene("j3-w06-s05", setting="mint", beats=(
        B("Let's run our first program. It is Exercise 6.1, Hello, Turtle!", speaker=AIDEN, cue="first",
          pause=0.5),
        B("We read it from top to bottom.", speaker=AIDEN, cue="read", pause=0.4),
        B("Get the turtle toolbox.", speaker=AIDEN, cue="l1", pause=0.4),
        B("Make a turtle called t.", speaker=AIDEN, cue="l2", pause=0.4),
        B("Show it as a turtle.", speaker=AIDEN, cue="l3", pause=0.4),
        B("Walk forward fifty.", speaker=AIDEN, cue="l4", pause=0.4),
        B("Make a quarter turn to the left.", speaker=AIDEN, cue="l5", pause=0.4),
        B("Keep the window open.", speaker=AIDEN, cue="l6", pause=0.5),
        B("Now, click Run!", speaker=AIDEN, cue="click", pause=3.0),
        B("The turtle draws a short line, then turns to look up.", speaker=AIDEN, cue="short", pause=0.5),
        B("No turtle window? It is hiding behind Thonny. Click the Python icon in the Dock.", speaker=AIDEN,
          cue="hide", pause=0.8),
    ), actions=(
        A("banner", "Exercise 6.1: Hello, Turtle!", at="first", color="green"),
        A("code", code=HELLO, title="hello.py", x=80, y=200, w=1040, h=560, size=42, shell=False,
          reveal=["l1", "l2", "l3", "l4", "l5", "l6"], run="click@0.4", expect=[],
          highlight=[(1, "l1", "l1$"), (2, "l2", "l2$"), (3, "l3", "l3$"), (4, "l4", "l4$"), (5, "l5", "l5$"),
                     (6, "l6", "l6$"), (4, "click@0.4", "click@0.4+1.2"), (5, "click@0.4+1.2", "click@0.4+2.0")]),
        A("turtle", code=HELLO, x=1200, y=200, w=640, h=560, at="first", run="click@0.4", duration=2.0),
        A("chip", "Run = green flag", at="click", until="short$", x=600, y=880, color="green", size=46),
        A("chip", "Hiding? Click Python in the Dock", at="hide", x=960, y=880, color="yellow", size=42),
    )),
    # 6. change one number (predict) --------------------------------------------------------------------
    Scene("j3-w06-s06", setting="peach", beats=(
        B("Now let's change one number.", speaker=AIDEN, cue="change", pause=0.4),
        B("We change fifty to one hundred fifty. We keep the brackets!", speaker=AIDEN, cue="fifty", pause=0.5),
        B("Then we click Save, and Run.", speaker=AIDEN, cue="save", pause=0.4),
        B("What do you think will happen?", speaker=AIDEN, cue="predict", pause=3.0),
        B("Same program, longer line! We changed the white oval.", speaker=AIDEN, cue="longer", pause=0.6),
        B("Longer line, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("code", code=HELLO, title="hello.py", x=80, y=200, w=1040, h=560, size=42, shell=False,
          until="fifty@0.6", highlight=[(4, "change", "fifty@0.6")]),
        A("code", code=HELLO_150, title="hello.py", x=80, y=200, w=1040, h=560, size=42, shell=False,
          at="fifty@0.6", run="longer", expect=[], highlight=[(4, "fifty@0.6", "longer$")]),
        A("turtle", code=HELLO, x=1200, y=200, w=640, h=560, at="start", until="longer", duration=0.1,
          world=260),
        A("turtle", code=HELLO_150, x=1200, y=200, w=640, h=560, at="longer", duration=2.0, world=260),
        A("chip", "50 → 150", at="fifty@0.6", until="predict", x=600, y=880, color="orange", size=48),
        A("thought", "Longer or shorter?", at="predict$+0.2", until="longer", x=600, y=900),
        A("chip", "Same program, longer line!", at="longer", x=600, y=880, color="green", size=46),
        A("pixi", x=1720, y=960, s=0.5, at="pixi", ground=1030, beep="pixi"),
    )),
    # 7. quick quiz: Editor or Shell? -----------------------------------------------------------------
    Scene("j3-w06-s07", setting="sky", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("Where do we type our program? In the big Editor at the top, or in the Shell at the bottom?",
          speaker=AIDEN, cue="where", pause=3.2),
        B("In the Editor! The Shell runs one line and then forgets it.", speaker=AIDEN, cue="editor", pause=0.5),
        B("Programs live in the big white part.", speaker=AIDEN, cue="live", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("code", code=HELLO, title="hello.py", x=120, y=200, w=1000, h=780, size=40, at="quiz", run="quiz",
          expect=[]),
        A("chip", "A: the Editor (top)", at="where@0.3", x=1480, y=420, color="sky", size=44),
        A("chip", "B: the Shell (bottom)", at="where@0.6", x=1480, y=800, color="yellow", size=44),
        A("thought", "A or B?", at="where$+0.2", until="editor", x=1480, y=610),
        A("badge", ok=True, at="editor", x=1760, y=320),
        A("arrow", at="editor@0.3", x1=1240, y1=420, x2=1000, y2=420, color="navy", width=8),
        A("aiden", x=1480, y=1080, s=0.45, at="quiz", moods={"where": "thinking", "editor": "happy"},
          chin=("where", "editor")),
    )),
    # 8. bug hunt: the typo -----------------------------------------------------------------------------
    Scene("j3-w06-s08", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.5),
        B("Ada typed this program. She expected a line.", speaker=AIDEN, cue="ada", pause=0.5),
        B("But the turtle does not move, and red text appears in the Shell.", speaker=AIDEN, cue="red",
          pause=0.8),
        B("Don't worry. Red text means Python is confused, and it tells us where to look.", speaker=AIDEN,
          cue="worry", pause=0.5),
        B("First, find the line number. It says line four.", speaker=AIDEN, cue="line", pause=0.6),
        B("Then read the last line: the Turtle has no attribute forwad.", speaker=AIDEN, cue="last", pause=0.5),
        B("That means: I don't know a word called forwad. It even asks: did you mean forward?", speaker=AIDEN,
          cue="means", pause=0.6),
        B("Can you find the typo on line four?", speaker=AIDEN, cue="find", pause=3.0),
        B("A missing r! We put the r back, save, and run again.", speaker=AIDEN, cue="fix", pause=3.0),
        B("It works! The turtle draws a line and turns.", speaker=AIDEN, cue="works", pause=0.5),
        B("Bugs are normal. Reading the red text is a superpower!", speaker=AIDEN, cue="super", pause=0.5),
        B("Super detective!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The typo", at="bug", color="navy"),
        A("code", code=BUGGY, traceback=True, title="ada.py", x=60, y=180, w=1200, h=820, size=40, shell_h=330,
          at="ada", until="fix", run="red@0.2", allow_error=True, error_line=4,
          expect=["Traceback (most recent call last):", '  File "main.py", line 4, in <module>', "    t.forwad(100)",
                  "AttributeError: 'Turtle' object has no attribute 'forwad'. Did you mean: 'forward'?"],
          highlight=[(4, "line", "last"), (4, "find", "fix")]),
        A("code", code=FIXED, title="ada.py", x=60, y=180, w=1200, h=820, size=40, shell_h=330, at="fix",
          run="fix@0.8", expect=[], highlight=[(4, "fix", "fix@0.8")]),
        A("chip", "Expected: a line", at="ada@0.5", until="worry", x=1580, y=400, color="green", size=42),
        A("badge", ok=False, at="red+1.6", until="fix", x=1580, y=560),
        A("chip", "line 4", at="line", until="fix", x=850, y=473, color="orange", size=40),
        A("chip", "no attribute 'forwad'", at="last", until="fix", x=1580, y=400, color="red", size=38),
        A("chip", "Did you mean: 'forward'?", at="means@0.5", until="fix", x=1580, y=700, color="yellow", size=36),
        A("thought", "Which letter?", at="find$+0.2", until="fix", x=1580, y=880),
        A("turtle", code=FIXED, x=1300, y=200, w=560, h=480, at="fix@0.8", duration=1.6),
        A("badge", ok=True, at="works", x=1780, y=270),
        A("confetti", at="works", x=1580, y=440),
        A("chip", "Red text = a clue!", at="super", x=1580, y=820, color="green", size=44),
    )),
    # 9. wiggle break: the picky robot --------------------------------------------------------------------
    Scene("j3-w06-s09", setting="workshop", beats=(
        B("Wiggle break! Stand up. You are a picky robot.", speaker=AIDEN, cue="wiggle", pause=0.5),
        B("Move only when the word is spelled right. If it is wrong, freeze and say: Error!", speaker=AIDEN,
          cue="rule", pause=0.6),
        B("Ready? Forward three!", speaker=AIDEN, cue="c1", pause=2.2),
        B("Left!", speaker=AIDEN, cue="c2", pause=1.6),
        B("Forwad two!", speaker=AIDEN, cue="c3", pause=1.0),
        B("Error! Error!", speaker=PIXI, cue="err", pause=1.2),
        B("Great freezing! Now, forward two!", speaker=AIDEN, cue="c4", pause=2.0),
        B("Super picky robots!", speaker=AIDEN, cue="done", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("wiggle", "rule"), ("done", "end")],
          moods={"start": "happy", "c3": "surprised", "c4": "happy", "done": "proud"}),
        A("pixi", x=640, y=760, beep="err", moods={"err": "surprised", "c4": "happy"},
          path=[("c1", 640, 760), ("c1+1.5", 900, 760), ("c4", 900, 760), ("c4+1.5", 1100, 760)]),
        A("chip", "WIGGLE BREAK: the picky robot", at="wiggle", until="c1", x=1300, y=420, color="orange", size=48),
        A("chip", "Wrong word? Freeze!", at="rule@0.5", until="c1", x=1300, y=560, color="red", size=44),
        A("bigtext", "forward 3", at="c1", until="c2", x=1300, y=420, size=90, color="green"),
        A("bigtext", "left", at="c2", until="c3", x=1300, y=420, size=90, color="green"),
        A("bigtext", "forwad 2", at="c3", until="c4", x=1300, y=420, size=90, color="red"),
        A("chip", "Error! Freeze!", at="err", until="c4", x=1300, y=600, color="red", size=48),
        A("bigtext", "forward 2", at="c4", until="done", x=1300, y=420, size=90, color="green"),
        A("confetti", at="done", x=1200, y=420),
    )),
    # 10. saving files with clear names ---------------------------------------------------------------
    Scene("j3-w06-s10", setting="lavender", beats=(
        B("In Python, every program is saved as its own file.", speaker=AIDEN, cue="file", pause=0.4),
        B("A good name helps us find it again.", speaker=AIDEN, cue="find", pause=0.5),
        B("Rule one: the name says what it is. Square dot py, not untitled dot py.", speaker=AIDEN, cue="r1",
          pause=0.5),
        B("Use small letters, and an underscore instead of a space.", speaker=AIDEN, cue="small", pause=0.6),
        B("Rule two: add your nickname, never your real name. Files can travel to other computers.",
          speaker=AIDEN, cue="r2", pause=0.6),
        B("Rule three: never call a file turtle dot py. Python would open your file instead of the real turtle!",
          speaker=AIDEN, cue="r3", pause=0.6),
        B("Our files stay on our own Mac. Nothing is uploaded.", speaker=AIDEN, cue="stay", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "r3": "surprised", "stay": "proud"},
          point=("r1", "r1$")),
        A("icons", at="file", until="r1", x=1060, y=440, gap=420,
          items=[("file", "One program = one file", "file@0.2"), ("magnifier", "Easy to find", "find")]),
        A("icons", at="r1", until="r2", x=1060, y=420, gap=420, crossed=[1],
          items=[("file", "square.py", "r1@0.4"), ("file", "untitled.py", "r1@0.7")]),
        A("chip", "small letters and _", at="small", until="r2", x=1060, y=760, color="sky", size=46),
        A("icons", at="r2", until="stay", x=1060, y=420, gap=420, crossed=[1],
          items=[("person", "kai_square.py", "r2@0.2"), ("file", "turtle.py", "r3@0.3")]),
        A("chip", "nicknames only", at="r2@0.4", until="stay", x=1060, y=760, color="green", size=46),
        A("icons", at="stay", x=1060, y=440, gap=420,
          items=[("laptop", "Stays on our Mac", "stay"), ("lock", "Nothing uploaded", "stay@0.5")]),
    )),
    # 11. recap and next -----------------------------------------------------------------------------------
    Scene("j3-w06-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Thonny!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Run!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Typo!", speaker=AIDEN, cue="w3", pause=1.2),
        B("We write in the Editor, click Run, and read the Shell.", speaker=AIDEN, cue="recap", pause=0.4),
        B("A typo stops Python, and the red text tells us where to look.", speaker=AIDEN, cue="recap2",
          pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Run Hello, Turtle! Then finish the square. Then be a typo detective.", speaker=AIDEN, cue="next",
          pause=0.6),
        B("Remember: small letters, a dot, and both brackets.", speaker=AIDEN, cue="remember", pause=0.5),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Thonny!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Run!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Typo!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("chip", "Editor • Run • Shell", at="recap", until="turn", x=1200, y=520, color="orange", size=48),
        A("chip", "Red text = where to look", at="recap2", until="turn", x=1200, y=650, color="yellow", size=46),
        A("banner", "NEXT: Hello, Turtle! and Typo Detective", at="turn", color="green"),
        A("cards", items=["Hello, Turtle!", "Finish the Square", "Typo Detective"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "small letters • a dot • ( )", at="remember", x=1320, y=760, color="sky", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
