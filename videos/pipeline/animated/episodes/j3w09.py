"""Junior Level 3 Week 9: Project Studio, My Big Build (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/3-bridge-to-python/teaching-material/lessons/week09.tex and project/project-brief.tex:
choose path A (Scratch game or art app) or path B (Python postcard), the must-haves, the plan card
(Omar's planning example: house, roof, sun), the snowman analogy (one part at a time), the worked
example of Omar changing the starter postcard one line at a time (blue house, gold roof, sides of 120),
Leo's Flower Garden as the path A look, the partner check against the plan (this week's bug hunt: a
roof line that is not pushed in), acting out the plan card, and "Can everyone see it?" (the squint test).
No child's finished Big Build is shown: only the lesson's own planning and worked examples.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

# The working starter (project/starter/postcard.py) without its comments: an orange house, a purple roof.
POSTCARD = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.pensize(5)
t.color("orange")
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.color("purple")
for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()"""

BLUE_HOUSE = POSTCARD.replace('"orange"', '"blue"')
GOLD_ROOF = BLUE_HOUSE.replace('"purple"', '"gold"')
BIGGER = GOLD_ROOF.replace("t.forward(100)", "t.forward(120)")
LONELY_ROOF = BIGGER.replace("    t.left(120)", "t.left(120)")
THIN_YELLOW = POSTCARD.replace("t.pensize(5)", "t.pensize(1)").replace('"orange"', '"yellow"').replace(
    '"purple"', '"yellow"')

VIEW = """t.color("orange")
for i in range(4):
    t.forward(100)
    t.left(90)
...
t.color("purple")
for i in range(3):
    t.forward(100)
    t.left(120)"""

VIEW_BLUE = VIEW.replace('"orange"', '"blue"')
VIEW_GOLD = VIEW_BLUE.replace('"purple"', '"gold"')
VIEW_BIGGER = VIEW_GOLD.replace("t.forward(100)", "t.forward(120)")
VIEW_LONELY = VIEW_BIGGER.replace("    t.left(120)", "t.left(120)")

LEO = [("event", "when [space] key pressed"), ("motion", "go to [mouse-pointer]"), ("pen", "pen down"),
       ("control", "repeat [6]", [("control", "repeat [4]", [("motion", "move [30] steps"),
                                                             ("motion", "turn ↻ [90] degrees")]),
                                  ("motion", "turn ↻ [60] degrees")]),
       ("pen", "pen up"), ("variables", "change [flowers] by [1]")]

EPISODE = Episode(level="j3", week=9, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j3-w09-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi", pause=0.3),
        B("Beep boop! Hello, builders!", speaker=PIXI, cue="hello", pause=0.5),
        B("Today is a big day. You build your own big project: your Big Build!", speaker=NARRATOR, cue="big",
          pause=0.5),
        B("Builders draw a plan before they build a house. Coders do too.", speaker=NARRATOR, cue="plan",
          pause=0.5),
        B("First we plan. Then we build. Then we test.", speaker=NARRATOR, cue="pbt", pause=0.6),
        B("Let's go!", speaker=NARRATOR, cue="go", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("go", "end")],
          moods={"start": "happy", "big": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello"),
        A("banner", "MISSION: My Big Build", at="big"),
        A("cards", items=["Plan", "Build", "Test"], x=1000, y=320, w=520, gap=140,
          reveal=["pbt", "pbt@0.35", "pbt@0.7"], at="pbt"),
        A("chip", "Plan first, like real builders", at="plan@0.4", until="pbt", x=1260, y=420, color="yellow",
          size=44),
    )),
    # 2. choose a path --------------------------------------------------------------------------------
    Scene("j3-w09-s02", setting="peach", beats=(
        B("First, choose a path. Both are great!", speaker=NARRATOR, cue="choose", pause=0.4),
        B("Path A is Scratch: a game or an art app.", speaker=NARRATOR, cue="a", pause=0.5),
        B("Path B is Python: a turtle postcard picture.", speaker=NARRATOR, cue="b", pause=0.5),
        B("Can't choose? Ask yourself: do I want people to play it, or to look at it?", speaker=NARRATOR,
          cue="ask", pause=3.0),
        B("Play it? Pick Scratch. Look at it? Pick Python.", speaker=NARRATOR, cue="pick", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "ask": "thinking", "pick": "happy"},
          chin=("ask", "pick")),
        A("icons", at="a", x=1100, y=400, gap=560,
          items=[("game", "A: Scratch game or art app", "a"), ("laptop", "B: Python postcard", "b")]),
        A("thought", "Play it or look at it?", at="ask$+0.2", until="pick", x=1100, y=760),
        A("chip", "play it → Scratch", at="pick", x=820, y=760, color="orange", size=44),
        A("chip", "look at it → Python", at="pick@0.5", x=1380, y=760, color="sky", size=44),
    )),
    # 3. the must-haves -------------------------------------------------------------------------------
    Scene("j3-w09-s03", setting="lavender", beats=(
        B("Each path has must-haves.", speaker=NARRATOR, cue="must", pause=0.4),
        B("Scratch needs the green flag, a repeat inside a repeat or a My Block, and a score or a counter.",
          speaker=NARRATOR, cue="scratch", pause=0.6),
        B("Python needs a program that runs, a for loop, two colors, and a shape you changed.", speaker=NARRATOR,
          cue="python", pause=0.6),
        B("Both paths need a plan card, and a partner check.", speaker=NARRATOR, cue="both", pause=0.8),
    ), actions=(
        A("chip", "My must-haves", at="must", until="scratch", x=960, y=420, color="yellow", size=52),
        A("panel", "A: Scratch", at="scratch", x=100, y=200, w=820, size=34, color="orange",
          items=[("scratch@0.2", "green flag"), ("scratch@0.45", "repeat in a repeat, or a My Block"),
                 ("scratch@0.8", "a score or a counter")]),
        A("panel", "B: Python", at="python", x=1000, y=200, w=820, size=34, color="blue",
          items=[("python@0.15", "it runs"), ("python@0.35", "a for loop"), ("python@0.55", "two colors"),
                 ("python@0.8", "a shape I changed")]),
        A("chip", "Both: a plan card + a partner check", at="both", x=960, y=760, color="green", size=46),
        A("pixi", x=1720, y=980, s=0.5, at="both", ground=1040, beep="both"),
    )),
    # 4. the plan card: Omar's planning example ----------------------------------------------------------
    Scene("j3-w09-s04", setting="sky", beats=(
        B("Now, the plan card. Here is Omar's.", speaker=NARRATOR, cue="card", pause=0.4),
        B("He circled B, for Python.", speaker=NARRATOR, cue="circled", pause=0.4),
        B("He drew what it will look like: a house with a roof, and a sun.", speaker=NARRATOR, cue="drew",
          pause=0.5),
        B("He named three parts, in the order he will build them: the house, the roof, and a sun.",
          speaker=NARRATOR, cue="parts", pause=0.6),
        B("He checked his must-haves, and wrote whose idea he used: the starter program.", speaker=NARRATOR,
          cue="idea", pause=0.6),
        B("Keep it quick. A quick drawing is perfect!", speaker=NARRATOR, cue="quick", pause=0.5),
        B("Three parts is plenty. Extra ideas go on the back of the card, for later.", speaker=NARRATOR,
          cue="plenty", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "quick": "proud"}, point=("card", "card$")),
        A("panel", "Omar's plan card", at="card", x=620, y=170, w=880, size=36, color="green",
          items=[("circled", "Path: B, Python"), ("drew", "Drawing: a house, a roof, a sun"),
                 ("parts@0.45", "Part 1: the house"), ("parts@0.65", "Part 2: the roof"),
                 ("parts@0.85", "Part 3: a sun"), ("idea@0.6", "Idea from: the starter")]),
        A("chip", "A quick drawing is perfect!", at="quick", until="plenty", x=1060, y=880, color="yellow",
          size=44),
        A("chip", "3 parts is plenty • extras on the back", at="plenty", x=1060, y=880, color="sky", size=42),
    )),
    # 5. one part at a time: the snowman -----------------------------------------------------------------
    Scene("j3-w09-s05", setting="mint", beats=(
        B("We don't build the whole project at once.", speaker=NARRATOR, cue="whole", pause=0.4),
        B("It's like a snowman. You roll the bottom ball, and check that it stands.", speaker=NARRATOR,
          cue="snow", pause=0.5),
        B("Then the middle. Then the head.", speaker=NARRATOR, cue="middle", pause=0.6),
        B("Build one part. Test it. Check it off. Then the next part.", speaker=NARRATOR, cue="one", pause=0.6),
        B("If something breaks, we know where to look: in the part we just made.", speaker=NARRATOR,
          cue="breaks", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "breaks": "proud"}),
        A("chip", "Not all at once!", at="whole@0.3", until="snow", x=1080, y=420, color="orange", size=52),
        A("roadmap", at="snow", x=620, y=330, w=1000, items=["Bottom", "Middle", "Head"],
          checks=[("snow@0.8", 0), ("middle@0.3", 1), ("middle@0.8", 2)], until="one"),
        A("cards", items=["Build one part", "Test it", "Check it off"], x=700, y=300, w=760, gap=130,
          reveal=["one", "one@0.3", "one@0.55"], at="one",
          active=[("one", "one@0.3"), ("one@0.3", "one@0.55"), ("one@0.55", "breaks")]),
        A("chip", "A bug? Look in the newest part", at="breaks@0.3", x=1080, y=820, color="yellow", size=44),
    )),
    # 6. worked example: Omar's postcard, part by part ---------------------------------------------------
    Scene("j3-w09-s06", setting="mint", beats=(
        B("Let's watch Omar build, part by part.", speaker=NARRATOR, cue="watch", pause=0.4),
        B("First, he presses Run. The starter already works: an orange house with a purple roof.",
          speaker=NARRATOR, cue="run", pause=1.6),
        B("Part one, the house. He changes orange to blue, and keeps the quote marks.", speaker=NARRATOR,
          cue="p1", pause=0.5),
        B("Quick quiz! Omar changed one line. What should he do next?", speaker=NARRATOR, cue="quiz", pause=3.0),
        B("Press Run, and test it!", speaker=NARRATOR, cue="test", pause=2.4),
        B("A blue house! Check it off.", speaker=NARRATOR, cue="check", pause=0.5),
        B("Next, he changes purple to gold, and runs it again.", speaker=NARRATOR, cue="p2", pause=2.6),
        B("Then he makes the house bigger. He changes all three one hundreds to one hundred twenty.",
          speaker=NARRATOR, cue="p3", pause=2.8),
        B("A bigger house! He changed a shape. That is a must-have.", speaker=NARRATOR, cue="bigger", pause=0.5),
        B("Then he clicks Save. Save often, so the working version stays safe!", speaker=NARRATOR, cue="saved",
          pause=0.8),
    ), actions=(
        A("code", code=VIEW, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          until="p1@0.5", highlight=[(1, "p1", "p1@0.5")]),
        A("code", code=VIEW_BLUE, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          at="p1@0.5", until="p2", highlight=[(1, "p1@0.5", "check$")]),
        A("code", code=VIEW_GOLD, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          at="p2", until="p3@0.6", highlight=[(6, "p2", "p2$+1.0")]),
        A("code", code=VIEW_BIGGER, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          at="p3@0.6", highlight=[(3, "p3@0.6", "bigger$"), (8, "p3@0.6", "bigger$")]),
        A("turtle", code=POSTCARD, x=1220, y=180, w=620, h=640, at="watch", until="test$", run="run@0.5",
          duration=2.6, world=200),
        A("turtle", code=BLUE_HOUSE, x=1220, y=180, w=620, h=640, at="test$", until="p2$", duration=2.0,
          world=200),
        A("turtle", code=GOLD_ROOF, x=1220, y=180, w=620, h=640, at="p2$", until="p3$", duration=2.0, world=200),
        A("turtle", code=BIGGER, x=1220, y=180, w=620, h=640, at="p3$", duration=2.0, world=200),
        A("chip", "QUICK QUIZ: what next?", at="quiz", until="test", x=610, y=900, color="purple", size=44),
        A("thought", "What next?", at="quiz$+0.2", until="test", x=1530, y=920),
        A("chip", "Run and test!", at="test", until="check$", x=610, y=900, color="green", size=46),
        A("chip", "Part 1: the house ✓", at="check", until="p3", x=610, y=900, color="green", size=44),
        A("chip", "a shape I changed ✓", at="bigger", until="saved", x=610, y=900, color="orange", size=44),
        A("chip", "Save often!", at="saved", x=610, y=900, color="yellow", size=46),
    )),
    # 7. path A in one look: Leo's Flower Garden ---------------------------------------------------------
    Scene("j3-w09-s07", setting="lavender", beats=(
        B("On the Scratch path, here is Leo's Flower Garden.", speaker=NARRATOR, cue="leo", pause=0.4),
        B("Press the space key, and a flower of six squares appears at the mouse pointer.", speaker=NARRATOR,
          cue="space", pause=0.6),
        B("The flowers counter goes up by one, every time.", speaker=NARRATOR, cue="counter", pause=0.6),
        B("A repeat inside a repeat, and a counter. Both must-haves!", speaker=NARRATOR, cue="both", pause=0.8),
    ), actions=(
        A("scratch", "Leo's Flower Garden", blocks=LEO, x=80, y=150, w=980, h=880, scale=1.0, at="leo",
          highlight=[(3, "both", "both$+0.4"), (5, "counter", "counter$")]),
        A("stage", x=1140, y=240, w=700, h=500, at="leo", flag=False, sprite_scale=0.8,
          monitors=[("flowers", [("start", 0), ("space@0.6", 1), ("counter@0.5", 2)])],
          actions=[("space@0.3", "goto", 120, 60, 0.8), ("counter", "goto", -120, -40, 0.8)]),
        A("chip", "space key = a flower", at="space", until="both", x=1490, y=860, color="yellow", size=44),
        A("chip", "repeat in a repeat + counter", at="both", x=1490, y=860, color="orange", size=40),
    )),
    # 8. bug hunt: the partner check ---------------------------------------------------------------------
    Scene("j3-w09-s08", setting="mint", beats=(
        B("Now, the partner check. It is our bug hunt!", speaker=NARRATOR, cue="bug", pause=0.4),
        B("Swap seats. Your partner holds your plan card, presses Run, and checks each part.", speaker=NARRATOR,
          cue="swap", pause=0.5),
        B("Mei checks Omar's postcard. Part one, the house: matches!", speaker=NARRATOR, cue="house", pause=0.5),
        B("Part two, the roof: not yet!", speaker=NARRATOR, cue="roof", pause=0.5),
        B("Mei says it like a good bug report: I expected a roof, but it drew one long line.", speaker=NARRATOR,
          cue="report", pause=0.6),
        B("Can you see the bug?", speaker=NARRATOR, cue="see", pause=3.0),
        B("T dot left one hundred twenty is not pushed in, so it runs only once.", speaker=NARRATOR, cue="lonely",
          pause=0.6),
        B("Omar fixes it himself, with one press of Tab. The partner finds it. The owner fixes it.",
          speaker=NARRATOR, cue="fix", pause=2.8),
        B("A roof! Check it off.", speaker=NARRATOR, cue="roof2", pause=0.5),
        B("Matches! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The partner check", at="bug", color="navy"),
        A("code", code=VIEW_LONELY, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          at="swap", until="fix@0.6", highlight=[(9, "see$+1.0", "fix@0.6")]),
        A("code", code=VIEW_BIGGER, title="postcard_omar.py", x=60, y=180, w=1100, h=640, size=40, shell=False,
          at="fix@0.6", highlight=[(9, "fix@0.6", "roof2$")]),
        A("turtle", code=LONELY_ROOF, x=1220, y=180, w=620, h=640, at="swap", until="fix$", run="swap@0.6",
          duration=2.6, world=260),
        A("chip", "house: matches ✓", at="house@0.5", until="see", x=610, y=900, color="green", size=44),
        A("chip", "roof: not yet", at="roof", until="lonely", x=1530, y=900, color="red", size=44),
        A("chip", "I expected a roof, but…", at="report@0.4", until="see", x=610, y=900, color="yellow",
          size=44),
        A("thought", "Which line?", at="see$+0.2", until="lonely", x=610, y=910),
        A("chip", "not pushed in = runs once", at="lonely@0.3", until="roof2", x=610, y=900, color="red",
          size=44),
        A("turtle", code=BIGGER, x=1220, y=180, w=620, h=640, at="fix$", duration=2.0, world=260),
        A("badge", ok=True, at="roof2", x=1780, y=250),
        A("chip", "roof: matches ✓", at="roof2", x=1530, y=900, color="green", size=44),
    )),
    # 9. wiggle break: act out your plan card ----------------------------------------------------------------
    Scene("j3-w09-s09", setting="workshop", beats=(
        B("Wiggle break! Stand up and act out your plan card.", speaker=NARRATOR, cue="wiggle", pause=0.4),
        B("Part one: strike a pose!", speaker=NARRATOR, cue="p1", pause=2.2),
        B("Part two: make a move, and repeat it four times!", speaker=NARRATOR, cue="p2", pause=0.4),
        B("One, two, three, four!", speaker=PIXI, cue="count", pause=0.8),
        B("Part three: a big finish!", speaker=NARRATOR, cue="p3", pause=2.0),
        B("Ta-da! Great building, builders!", speaker=NARRATOR, cue="tada", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("p1", "p1$+1.0"), ("p3", "end")],
          moods={"start": "happy", "p1": "proud", "tada": "proud"}),
        A("pixi", x=640, y=760, beep="count", moods={"count": "happy"},
          path=[("count", 640, 760), ("count@0.25", 640, 700), ("count@0.5", 640, 760), ("count@0.75", 640, 700),
                ("count$", 640, 760)]),
        A("chip", "WIGGLE BREAK: act out your plan", at="wiggle", until="p1", x=1300, y=420, color="orange",
          size=46),
        A("bigtext", "Part 1: pose!", at="p1", until="p2", x=1300, y=420, size=90, color="green"),
        A("bigtext", "Part 2: move × 4", at="p2", until="p3", x=1300, y=420, size=90, color="blue"),
        A("bigtext", "Part 3: big finish!", at="p3", until="tada$", x=1300, y=420, size=84, color="purple"),
        A("confetti", at="tada", x=1250, y=420),
    )),
    # 10. can everyone see it? -----------------------------------------------------------------------------
    Scene("j3-w09-s10", setting="sky", beats=(
        B("Can everyone see your project?", speaker=NARRATOR, cue="see", pause=0.4),
        B("Some people see red and green as the same color. Some people need things big to see them.",
          speaker=NARRATOR, cue="some", pause=0.5),
        B("Try the squint test. Squint your eyes at this postcard. Can you still see every part?",
          speaker=NARRATOR, cue="squint", pause=3.0),
        B("The thin yellow lines almost disappear!", speaker=NARRATOR, cue="yellow", pause=0.5),
        B("Use thick lines, a pen size of five or more. Put dark next to light, like blue next to gold.",
          speaker=NARRATOR, cue="tips", pause=0.6),
        B("Don't use color alone, and make things big enough to see.", speaker=NARRATOR, cue="more", pause=0.5),
        B("And check that every plan card says whose idea you used, with nicknames only.", speaker=NARRATOR,
          cue="credit", pause=0.8),
    ), actions=(
        A("icons", at="see@0.3", until="squint", x=1060, y=420, gap=420,
          items=[("star", "Colors for everyone", "some@0.2"), ("magnifier", "Big enough to see", "some@0.6")]),
        A("turtle", code=THIN_YELLOW, x=120, y=200, w=640, h=600, at="squint", duration=2.0, world=200),
        A("thought", "Can you see it?", at="squint$+0.2", until="yellow", x=1300, y=420),
        A("badge", ok=False, at="yellow", x=700, y=260),
        A("turtle", code=GOLD_ROOF, x=1160, y=200, w=640, h=600, at="tips", duration=2.0, world=200),
        A("badge", ok=True, at="tips@0.6", x=1740, y=260),
        A("chip", "thick lines • dark next to light", at="tips@0.3", until="credit", x=960, y=900, color="green",
          size=44),
        A("chip", "not color alone • big enough", at="more", until="credit", x=960, y=1000, color="sky", size=40),
        A("chip", "Whose idea? Nicknames only", at="credit", x=960, y=920, color="orange", size=44),
        A("aiden", x=1300, y=1080, s=0.45, at="see", until="tips", moods={"squint": "thinking",
                                                                          "yellow": "surprised"}),
    )),
    # 11. recap and next ---------------------------------------------------------------------------------------
    Scene("j3-w09-s11", setting="workshop", tail=0.8, beats=(
        B("Say it with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Plan!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Build!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Test!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("Today: fill in your plan card, then make it work, one part at a time.", speaker=NARRATOR, cue="today",
          pause=0.5),
        B("Next week is the showcase!", speaker=NARRATOR, cue="showcase", pause=0.5),
        B("Now it's your turn, with a grown-up.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Make your plan card, build part by part, then do the partner check.", speaker=NARRATOR, cue="next",
          pause=0.6),
        B("And save often!", speaker=NARRATOR, cue="save", pause=0.5),
        B("See you next week. Happy coding!", speaker=NARRATOR, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Plan!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Build!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Test!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("roadmap", at="today", until="turn", x=820, y=420, w=860,
          items=["M1 Plan card", "M2 It works", "M3 Showcase"],
          current=[("today", 0), ("today@0.6", 1), ("showcase", 2)]),
        A("banner", "NEXT: Plan, build and check My Big Build", at="turn", color="green"),
        A("cards", items=["My plan card", "Build part by part", "Partner check"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "Save often!", at="save", x=1320, y=760, color="yellow", size=46),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
