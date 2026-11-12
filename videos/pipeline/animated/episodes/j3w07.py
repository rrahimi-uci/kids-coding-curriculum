"""Junior Level 3 Week 7: Repeat in Python (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/3-bridge-to-python/teaching-material/lessons/week07.tex: the "Indent the line-up" warm-up
(CLAP and STOMP inside the tape box, WAVE outside), the repeat twins (Scratch repeat 4 and
`for i in range(4):`), the colon and the four spaces (the mouth of the repeat, the Tab key), the
Exercise 7.1 worked example (range(2) becomes range(4)), the Lonely Turn bug hunt, a look at the
Python Flower starter (two squares; the six-square answer is never shown), asking for help well, and
the jump-clap-stretch wiggle break.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

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

LOOP_DONE = LOOP3 + "\nturtle.done()"

REPEAT2 = """import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(2):
    t.forward(100)
    t.left(90)
turtle.done()"""

REPEAT4 = REPEAT2.replace("range(2)", "range(4)")

LONELY = """import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(4):
    t.forward(80)
t.left(90)
turtle.done()"""

LONELY_FIXED = LONELY.replace("\nt.left(90)", "\n    t.left(90)")

FLOWER_PART = """for i in range(2):
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)"""

FLOWER_STARTER = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(8)
""" + FLOWER_PART + "\nturtle.done()"

MOVE = ("motion", "move [100] steps")
TURN = ("motion", "turn ↺ [90] degrees")
BIG = 1.25  # block scale: big enough for young eyes

EPISODE = Episode(level="j3", week=7, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j3-w07-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is my robot friend, Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello again, coders!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, our square needed eight lines: forward, left, forward, left, again and again.",
          speaker=AIDEN, cue="last", pause=0.5),
        B("In Scratch, we would use a repeat block. Python has a repeat too!", speaker=AIDEN, cue="repeat",
          pause=0.4),
        B("It is called for.", speaker=AIDEN, cue="for", pause=0.5),
        B("Can we make eight lines into three?", speaker=AIDEN, cue="q", pause=3.0),
        B("Yes, we can! Let's find out how.", speaker=AIDEN, cue="yes", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, enter="left", wave=[("hi", "hello"), ("yes", "end")],
          moods={"start": "happy", "q": "thinking", "yes": "proud"}, chin=("q", "yes")),
        A("pixi", x=600, y=760, drop=True, beep="hello"),
        A("code", code=EIGHT_LINES, title="square.py", x=900, y=200, w=840, h=580, size=36, shell=False,
          at="last", type=("last", "last$")),
        A("banner", "MISSION: Repeat in Python", at="repeat"),
        A("chip", "for = repeat", at="for", x=1320, y=880, color="orange", size=48),
        A("thought", "8 lines → 3?", at="q$+0.2", until="yes", x=700, y=330),
    )),
    # 2. warm-up: Indent the line-up -----------------------------------------------------------------
    Scene("j3-w07-s02", setting="peach", beats=(
        B("Let's warm up! Imagine a box on the floor, made of tape.", speaker=AIDEN, cue="box", pause=0.4),
        B("The box is the inside of a repeat. The card on top says: for i in range three.", speaker=AIDEN,
          cue="card", pause=0.5),
        B("Clap and Stomp stand inside the box. Wave stands outside, below it.", speaker=AIDEN, cue="inside",
          pause=0.5),
        B("Do it with me!", speaker=AIDEN, cue="doit", pause=0.3),
        B("Clap, stomp! Clap, stomp! Clap, stomp! Wave!", speaker=PIXI, cue="act", pause=0.8),
        B("Why did Wave happen only once?", speaker=AIDEN, cue="why", pause=3.0),
        B("Wave is not inside the box!", speaker=AIDEN, cue="notin", pause=0.5),
        B("Now Wave steps into the box. Clap, stomp, wave, three times!", speaker=AIDEN, cue="stepin",
          pause=1.2),
        B("In Python, the box is made of spaces.", speaker=AIDEN, cue="spaces", pause=0.8),
    ), actions=(
        A("aiden", x=220, y=1000, s=0.75, wave=[("act@0.85", "why"), ("stepin@0.6", "stepin$")],
          moods={"start": "happy", "why": "thinking", "notin": "happy"}, chin=("why", "notin")),
        A("pixi", x=1660, y=860, s=0.6, ground=1000, beep="act"),
        A("panel", "for i in range(3):", at="card", until="stepin", x=700, y=260, w=560, color="orange",
          items=[("inside", "CLAP"), ("inside@0.25", "STOMP")]),
        A("chip", "WAVE", at="inside@0.6", until="stepin", x=980, y=620, color="white", size=46),
        A("chip", "3 times", at="act@0.6", until="stepin", x=1420, y=380, color="orange", size=42),
        A("chip", "once", at="act@0.9", until="stepin", x=1420, y=620, color="sky", size=42),
        A("thought", "Why only once?", at="why$+0.2", until="notin", x=1000, y=820),
        A("panel", "for i in range(3):", at="stepin", x=700, y=260, w=560, color="orange",
          items=[("stepin", "CLAP"), ("stepin", "STOMP"), ("stepin@0.2", "WAVE")]),
        A("chip", "3 times", at="stepin@0.5", x=1420, y=420, color="orange", size=42),
        A("chip", "box = spaces", at="spaces", x=980, y=760, color="green", size=46),
    )),
    # 3. the repeat twins -----------------------------------------------------------------------------
    Scene("j3-w07-s03", setting="lavender", beats=(
        B("Here are the repeat twins.", speaker=AIDEN, cue="twins", pause=0.4),
        B("In Scratch: repeat four, with move and turn inside.", speaker=AIDEN, cue="scratch", pause=0.5),
        B("In Python: for i in range four, with a colon at the end.", speaker=AIDEN, cue="python", pause=0.5),
        B("For i in range four means: repeat four.", speaker=AIDEN, cue="means", pause=0.6),
        B("The i is only a name Python needs. We don't use it yet.", speaker=AIDEN, cue="i", pause=0.5),
        B("Eight lines last week. Three lines today!", speaker=AIDEN, cue="three", pause=0.5),
        B("Three lines! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Scratch", blocks=[("control", "repeat [4]", [MOVE, TURN])], x=100, y=220, w=780, h=480,
          scale=BIG, at="scratch"),
        A("code", code=LOOP3, title="Python", x=1000, y=220, w=820, h=420, size=46, shell=False, at="python",
          highlight=[(1, "means", "means$+0.3")]),
        A("arrow", at="python@0.5", until="i", x1=900, y1=380, x2=980, y2=380, color="navy", width=8),
        A("chip", "for i in range(4): = repeat 4", at="means", until="i", x=960, y=820, color="orange", size=46),
        A("chip", "i = a name Python needs", at="i", until="three", x=960, y=820, color="sky", size=46),
        A("chip", "8 lines → 3 lines!", at="three", x=960, y=820, color="green", size=48),
        A("pixi", x=1720, y=980, s=0.5, at="pixi", ground=1040, beep="pixi"),
    )),
    # 4. the colon and the four spaces ---------------------------------------------------------------
    Scene("j3-w07-s04", setting="sky", beats=(
        B("Now look closely at the end of the first line. A colon!", speaker=AIDEN, cue="colon", pause=0.4),
        B("The colon says: here comes the inside.", speaker=AIDEN, cue="here", pause=0.6),
        B("The lines under it are pushed in by four spaces. Pushed in means inside the repeat.", speaker=AIDEN,
          cue="pushed", pause=0.6),
        B("In Scratch, blocks sit in the orange mouth of the repeat. Python has no mouth, so we push the lines in "
          "with spaces.", speaker=AIDEN, cue="mouth", pause=0.6),
        B("To push a line in, click at the very start of the line, and press the Tab key once.", speaker=AIDEN,
          cue="tab", pause=0.5),
        B("Tab jumps four spaces!", speaker=PIXI, cue="jump", pause=0.8),
    ), actions=(
        A("code", code=LOOP3, title="square.py", x=100, y=200, w=1000, h=420, size=52, shell=False,
          highlight=[(1, "colon", "here$"), (2, "pushed", "mouth"), (3, "pushed", "mouth")]),
        A("chip", ":", at="colon@0.6", until="pushed", x=880, y=320, color="yellow", size=56),
        A("chip", ": = here comes the inside", at="here", until="tab", x=600, y=720, color="yellow", size=46),
        A("chip", "4 spaces", at="pushed@0.3", until="tab", x=300, y=550, color="orange", size=36),
        A("scratch", blocks=[("control", "repeat [4]", [MOVE, TURN])], x=1180, y=220, w=680, h=420, scale=1.0,
          at="mouth", until="tab", panel=False),
        A("chip", "pushed in = inside", at="pushed@0.5", until="tab", x=1520, y=720, color="orange", size=44),
        A("chip", "Tab key = 4 spaces", at="tab", x=1480, y=400, color="green", size=52),
        A("chip", "Click at the very start first", at="tab@0.3", x=600, y=720, color="sky", size=44),
        A("pixi", x=1720, y=960, s=0.5, at="tab", ground=1030, beep="jump"),
    )),
    # 5. worked example: Repeat 4 -----------------------------------------------------------------------
    Scene("j3-w07-s05", setting="mint", beats=(
        B("Let's try it in Thonny. It is Exercise 7.1, Repeat 4.", speaker=AIDEN, cue="try", pause=0.4),
        B("This program says for i in range two. Let's click Run.", speaker=AIDEN, cue="run", pause=2.4),
        B("How many sides did the turtle draw?", speaker=AIDEN, cue="how", pause=3.0),
        B("Only two! The repeat went round two times: one side and one quarter turn, each time.", speaker=AIDEN,
          cue="two", pause=0.6),
        B("We change two to four. We keep the colon!", speaker=AIDEN, cue="change", pause=0.4),
        B("Save, and Run.", speaker=AIDEN, cue="save", pause=3.0),
        B("A square! One side and one quarter turn, four times.", speaker=AIDEN, cue="square", pause=0.5),
        B("Beep! Square!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "Exercise 7.1: Repeat 4", at="try", color="green"),
        A("code", code=REPEAT2, title="repeat.py", x=80, y=200, w=1060, h=600, size=42, shell=False, at="try",
          until="change@0.5", run="run$", expect=[], highlight=[(4, "run", "run$"), (4, "change", "change@0.5")]),
        A("code", code=REPEAT4, title="repeat.py", x=80, y=200, w=1060, h=600, size=42, shell=False,
          at="change@0.5", run="save$", expect=[], highlight=[(4, "change@0.5", "save$")]),
        A("turtle", code=REPEAT2, x=1220, y=200, w=620, h=600, at="run", until="save$", run="run$", duration=1.6,
          world=220),
        A("thought", "How many sides?", at="how$+0.2", until="two", x=640, y=900),
        A("chip", "2 sides", at="two", until="change", x=640, y=900, color="orange", size=46),
        A("chip", "range(2) → range(4)", at="change@0.5", until="save$", x=640, y=900, color="yellow", size=46),
        A("turtle", code=REPEAT4, x=1220, y=200, w=620, h=600, at="save$", duration=2.4, world=220),
        A("badge", ok=True, at="square", x=1780, y=270),
        A("chip", "4 sides, 4 corners", at="square", x=640, y=900, color="green", size=46),
    )),
    # 6. quick quiz: inside or outside? -------------------------------------------------------------------
    Scene("j3-w07-s06", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("Look at the left edge of each line. Which lines are inside the repeat? Point to them!",
          speaker=AIDEN, cue="which", pause=3.2),
        B("The two lines that are pushed in: forward and left.", speaker=AIDEN, cue="answer", pause=0.6),
        B("Turtle dot done starts at the left edge. It is outside, so it runs only once, at the very end.",
          speaker=AIDEN, cue="done", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("code", code=LOOP_DONE, title="square.py", x=140, y=220, w=1040, h=480, size=50, shell=False,
          at="quiz", highlight=[(2, "answer", "done"), (3, "answer", "done"), (4, "done", "end")]),
        A("pointer", x=240, y=380, at="which", until="answer",
          path=[("which@0.3", 240, 380), ("which$", 240, 620)]),
        A("thought", "Inside or outside?", at="which$+0.2", until="answer", x=1500, y=420),
        A("chip", "pushed in = inside", at="answer", x=1500, y=420, color="orange", size=44),
        A("chip", "left edge = outside, runs once", at="done", x=660, y=860, color="sky", size=44),
        A("aiden", x=1500, y=1080, s=0.45, at="quiz", moods={"which": "thinking", "answer": "happy"},
          chin=("which", "answer")),
    )),
    # 7. bug hunt: the Lonely Turn -------------------------------------------------------------------------
    Scene("j3-w07-s07", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt! It is called The Lonely Turn.", speaker=AIDEN, cue="bug", pause=0.5),
        B("This program should draw a square. Let's run it.", speaker=AIDEN, cue="should", pause=3.0),
        B("Hmm. One long, straight line.", speaker=AIDEN, cue="hmm", pause=0.4),
        B("How many times did the turtle turn?", speaker=AIDEN, cue="how", pause=3.0),
        B("Only once, at the very end!", speaker=AIDEN, cue="once", pause=0.5),
        B("Which line is outside the box?", speaker=AIDEN, cue="which", pause=3.0),
        B("T dot left is not pushed in. It is like Wave in our warm-up, so it runs only once.", speaker=AIDEN,
          cue="left", pause=0.6),
        B("Let's click at the start of that line, and press Tab once.", speaker=AIDEN, cue="fix", pause=0.6),
        B("Save, and Run again.", speaker=AIDEN, cue="again", pause=3.2),
        B("A square! The turtle turns at every corner.", speaker=AIDEN, cue="square", pause=0.5),
        B("Bug fixed! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Lonely Turn", at="bug", color="navy"),
        A("code", code=LONELY, title="lonely_turn.py", x=60, y=200, w=1080, h=600, size=42, shell=False,
          at="should", until="fix@0.5", run="should$", expect=[],
          highlight=[(6, "which$+1.0", "fix@0.5")]),
        A("code", code=LONELY_FIXED, title="lonely_turn.py", x=60, y=200, w=1080, h=600, size=42, shell=False,
          at="fix@0.5", run="again$", expect=[], highlight=[(6, "fix@0.5", "again$+1.0")]),
        A("chip", "Expected: a square", at="should@0.5", until="how", x=1520, y=860, color="green", size=42),
        A("turtle", code=LONELY, x=1200, y=200, w=640, h=560, at="should", until="again$", run="should$",
          duration=2.4),
        A("badge", ok=False, at="hmm", until="again$", x=1780, y=270),
        A("thought", "How many turns?", at="how$+0.2", until="once", x=1520, y=880),
        A("chip", "1 turn", at="once", until="which", x=1520, y=860, color="orange", size=44),
        A("thought", "Which line?", at="which$+0.2", until="left", x=640, y=920),
        A("chip", "not pushed in = runs once", at="left@0.2", until="again", x=600, y=900, color="red", size=44),
        A("chip", "Tab key", at="fix@0.5", until="again$", x=1520, y=860, color="yellow", size=48),
        A("turtle", code=LONELY_FIXED, x=1200, y=200, w=640, h=560, at="again$", duration=2.4),
        A("badge", ok=True, at="square", x=1780, y=270),
        A("confetti", at="square", x=1520, y=480),
    )),
    # 8. a repeat inside a repeat: the Python Flower starter -------------------------------------------------
    Scene("j3-w07-s08", setting="lavender", beats=(
        B("Remember the flower from week one? A repeat inside a repeat.", speaker=AIDEN, cue="remember",
          pause=0.5),
        B("Here it is in Python. The outer repeat is at the left edge. It counts the squares.", speaker=AIDEN,
          cue="outer", pause=0.6),
        B("The inner repeat is pushed in. It draws one square.", speaker=AIDEN, cue="inner", pause=0.6),
        B("And t dot left sixty is pushed in once, not twice. So the turtle turns once after each square.",
          speaker=AIDEN, cue="sixty", pause=0.6),
        B("The starter draws two squares. In Exercise 7.3, you change one number to grow the whole flower!",
          speaker=AIDEN, cue="two", pause=0.8),
    ), actions=(
        A("code", code=FLOWER_PART, title="python_flower.py", x=80, y=200, w=1080, h=480, size=42, shell=False,
          at="remember", highlight=[(1, "outer", "inner"), (2, "inner", "sixty"), (3, "inner", "sixty"),
                                    (4, "inner", "sixty"), (5, "sixty", "two")]),
        A("chip", "outer: counts the squares", at="outer@0.4", until="inner", x=620, y=800, color="orange",
          size=44),
        A("chip", "inner: draws one square", at="inner@0.3", until="sixty", x=620, y=800, color="sky", size=44),
        A("chip", "one turn after each square", at="sixty@0.5", until="two", x=620, y=800, color="purple",
          size=44),
        A("turtle", code=FLOWER_STARTER, x=1240, y=200, w=600, h=560, at="two", duration=3.0, world=150),
        A("chip", "Exercise 7.3: Python Flower", at="two@0.4", x=620, y=800, color="green", size=44),
    )),
    # 9. asking for help well -----------------------------------------------------------------------------
    Scene("j3-w07-s09", setting="sky", beats=(
        B("When code does something strange, a good question gets help fast.", speaker=AIDEN, cue="strange",
          pause=0.4),
        B("Say two things: what I expected, and what happened.", speaker=AIDEN, cue="two", pause=0.5),
        B("Like this: I expected a square, but the turtle drew one long line and turned once.", speaker=AIDEN,
          cue="like", pause=0.6),
        B("Which is the better question? It's broken! Or: I expected a square, but I got a line?",
          speaker=AIDEN, cue="which", pause=3.0),
        B("The second one! Now a helper knows where to look.", speaker=AIDEN, cue="second", pause=0.5),
        B("Ask a grown-up you know. Never type your name or school into a website or a chatbot to get help.",
          speaker=AIDEN, cue="ask", pause=0.8),
    ), actions=(
        A("chip", "A good question gets help fast", at="strange@0.3", until="two", x=1140, y=420, color="yellow",
          size=46),
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "which": "thinking", "second": "happy"},
          chin=("which", "second")),
        A("cards", items=["What I expected", "What happened"], x=760, y=280, w=760, gap=130,
          reveal=["two@0.3", "two@0.6"], at="two", until="which",
          active=[("like", "like@0.5"), ("like@0.5", "like$")]),
        A("chip", "“It's broken!”", at="which@0.2", until="ask", x=1140, y=330, color="white", size=46),
        A("chip", "“I expected a square, but I got a line.”", at="which@0.5", until="ask", x=1140, y=500,
          color="white", size=40),
        A("thought", "Which one?", at="which$+0.2", until="second", x=1140, y=720),
        A("badge", ok=True, at="second", until="ask", x=1720, y=500),
        A("icons", at="ask", x=1140, y=440, gap=420, crossed=[1],
          items=[("grownup", "A grown-up you know", "ask"), ("laptop", "No names in a chatbot", "ask@0.5")]),
    )),
    # 10. wiggle break: repeat jump and clap ---------------------------------------------------------------
    Scene("j3-w07-s10", setting="workshop", beats=(
        B("Wiggle break! Stand up.", speaker=AIDEN, cue="wiggle", pause=0.4),
        B("Repeat four: jump, clap!", speaker=AIDEN, cue="rep", pause=0.3),
        B("One! Two! Three! Four!", speaker=PIXI, cue="count", pause=0.8),
        B("Outside the repeat: one big stretch!", speaker=AIDEN, cue="stretch", pause=2.0),
        B("Now push the stretch inside the repeat. Jump, clap, stretch, four times!", speaker=AIDEN,
          cue="inside", pause=5.0),
        B("Great moving, coders!", speaker=AIDEN, cue="great", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("rep", "count$"), ("inside", "inside$+5.0")],
          moods={"start": "happy", "great": "proud"}),
        A("pixi", x=620, y=760, beep="count", moods={"count": "happy"},
          path=[("count", 620, 760), ("count@0.25", 620, 700), ("count@0.5", 620, 760), ("count@0.75", 620, 700),
                ("count$", 620, 760)]),
        A("panel", "for i in range(4):", at="rep", until="inside", x=1000, y=260, w=560, color="orange",
          items=[("rep", "JUMP"), ("rep@0.3", "CLAP")]),
        A("chip", "STRETCH", at="stretch", until="inside", x=1280, y=620, color="white", size=46),
        A("panel", "for i in range(4):", at="inside", x=1000, y=260, w=560, color="orange",
          items=[("inside", "JUMP"), ("inside", "CLAP"), ("inside@0.2", "STRETCH")]),
        A("confetti", at="great", x=1280, y=420),
    )),
    # 11. recap and next ---------------------------------------------------------------------------------------
    Scene("j3-w07-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Colon!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Four spaces!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Inside!", speaker=AIDEN, cue="w3", pause=1.2),
        B("For i in range four means repeat four.", speaker=AIDEN, cue="recap", pause=0.4),
        B("Lines that are pushed in are inside the repeat. A line at the left edge runs only once.",
          speaker=AIDEN, cue="recap2", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Make Repeat 4, fix The Lonely Turn, then grow the Python Flower.", speaker=AIDEN, cue="next",
          pause=0.6),
        B("Remember: one press of Tab pushes a line in.", speaker=AIDEN, cue="remember", pause=0.5),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Colon!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Four spaces!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Inside!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("chip", "for i in range(4): = repeat 4", at="recap", until="turn", x=1200, y=520, color="orange",
          size=46),
        A("chip", "left edge = runs once", at="recap2", until="turn", x=1200, y=650, color="sky", size=46),
        A("banner", "NEXT: Repeat 4, Lonely Turn, Python Flower", at="turn", color="green"),
        A("cards", items=["Repeat 4", "The Lonely Turn", "Python Flower"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "Tab key = push a line in", at="remember", x=1320, y=760, color="yellow", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
