"""Junior Level 3 Week 5: Play Day: Blocks to Words (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/3-bridge-to-python/teaching-material/lessons/week05.tex: Play Day, the blocks-to-words
card sort (move 100 steps / t.forward(100), turn left 90 / t.left(90), repeat 4 / for i in range(4):,
set pen color to blue / t.color("blue")), the "hello / hola" analogy, t as the turtle's name, the
Scratch square in Python words with the indent (shown, not typed; a sneak-peek turtle drawing), the
"be the Python turtle" wiggle break, leg 1 of the bug-hunt relay (Exercise 5.2: the turn inside the
inside repeat), legs 2 and 3 left for the children, the show-me checklist ("not yet" is fine), and
"What am I proud of so far?" with credit and nicknames on the Proud Wall.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
MOVE100 = ("motion", "move [100] steps")
LEFT90 = ("motion", "turn ↺ [90] degrees")
COLOR = ("pen", "set pen color to [blue]")
MOVE60 = ("motion", "move [60] steps")
RIGHT90 = ("motion", "turn ↻ [90] degrees")
ERASE = ("pen", "erase all")
PEN_DOWN = ("pen", "pen down")
BIG = 1.25  # block scale: big enough for young eyes
L = 80  # side of one window square on the stage (stage steps; the viewer sees no numbers)

TWINS = """t.color("blue")
for i in range(4):
    t.forward(100)
    t.left(90)"""

SNEAK_PEEK = """import turtle
t = turtle.Turtle()
t.pensize(4)
t.color("blue")
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()"""


def window_actions(cue: str, base: float) -> list:
    """The cat draws the window like Scratch does: down-right, down-left, up-left, up-right squares."""
    def at(offset):
        return f"{cue}+{base + offset:.2f}"
    return [(at(0.0), "draw", 4, L, 1.0, -90), (at(1.1), "goto", -L, 0, 0.3), (at(1.5), "draw", 4, L, 1.0, -90),
            (at(2.6), "draw", 4, L, 1.0, 90), (at(3.7), "goto", 0, 0, 0.3), (at(4.1), "draw", 4, L, 1.0, 90)]


EPISODE = Episode(level="j3", week=5, scenes=(
    # 1. hook: Play Day ---------------------------------------------------------------------------------
    Scene("j3-w05-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi", pause=0.3),
        B("Beep boop! Is it Play Day?", speaker=PIXI, cue="hello", pause=0.5),
        B("Yes! Today is Play Day!", speaker=NARRATOR, cue="play", pause=0.4),
        B("We practice everything from weeks one to four: patterns, plans, data, and how computers learn.",
          speaker=NARRATOR, cue="practice", pause=0.5),
        B("And there's something new. Every Scratch block has a word twin, in a coding language called Python!",
          speaker=NARRATOR, cue="new", pause=0.5),
        B("Are you ready? Let's go!", speaker=NARRATOR, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "new": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello", moods={"play": "happy"}),
        A("banner", "PLAY DAY!", at="play", until="new", color="orange"),
        A("cards", items=["Patterns", "Plans", "Data", "How computers learn"], x=1000, y=250, w=640, gap=115,
          reveal=["practice@0.35", "practice@0.5", "practice@0.65", "practice@0.85"], at="practice",
          until="new", color="sky"),
        A("banner", "MISSION: Find the word twins", at="new"),
        A("scratch", blocks=[MOVE100], x=1020, y=420, panel=False, scale=BIG, at="new@0.5"),
        A("chip", "t.forward(100)", at="new@0.75", x=1260, y=640, color="white", size=48),
    )),
    # 2. two languages, one idea --------------------------------------------------------------------------
    Scene("j3-w05-s02", setting="lavender", beats=(
        B("Python uses words instead of blocks.", speaker=NARRATOR, cue="words", pause=0.5),
        B("You can say hello in English, and hola in Spanish. Different words, same idea.", speaker=NARRATOR,
          cue="hola", pause=0.6),
        B("A Scratch block and its Python line are like that: two ways to tell the computer the same thing.",
          speaker=NARRATOR, cue="same", pause=0.6),
        B("Let's play the card sort, and find the twins!", speaker=NARRATOR, cue="sort", pause=0.5),
        B("Hola, twins! Beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("chip", "Python: words, not blocks", at="words@0.3", until="hola", x=960, y=480, color="sky", size=52),
        A("chip", "hello", at="hola@0.25", until="same", x=620, y=420, color="sky", size=60),
        A("chip", "hola", at="hola@0.55", until="same", x=1300, y=420, color="yellow", size=60),
        A("arrow", at="hola@0.6", until="same", x1=780, y1=420, x2=1150, y2=420, color="navy", width=8),
        A("chip", "Different words, same idea", at="hola@0.8", until="same", x=960, y=640, color="green",
          size=46),
        A("scratch", blocks=[MOVE100], x=360, y=380, panel=False, scale=BIG, at="same"),
        A("arrow", at="same@0.5", x1=1000, y1=430, x2=1180, y2=430, color="navy", width=8),
        A("chip", "t.forward(100)", at="same@0.5", x=1450, y=430, color="white", size=52),
        A("chip", "Two ways, same thing", at="same@0.8", x=960, y=660, color="green", size=46),
        A("pixi", x=960, y=960, s=0.5, at="sort", ground=1010, beep="pixi"),
    )),
    # 3. twin 1: forward, and t is the turtle --------------------------------------------------------------
    Scene("j3-w05-s03", setting="sky", beats=(
        B("Here's our first block: move one hundred steps.", speaker=NARRATOR, cue="move", pause=0.4),
        B("Which Python word sounds like moving ahead?", speaker=NARRATOR, cue="which", pause=3.0),
        B("Forward! Its twin is t.forward, with one hundred inside the brackets.", speaker=NARRATOR, cue="forward",
          pause=0.5),
        B("The same number, one hundred, is in both twins.", speaker=NARRATOR, cue="number", pause=0.5),
        B("And what is the t? It is not a typo. t is the name of our turtle, the one that will draw in Python.",
          speaker=NARRATOR, cue="t", pause=0.5),
        B("Every turtle line starts with it, like a name on a letter.", speaker=NARRATOR, cue="letter", pause=0.6),
    ), actions=(
        A("scratch", "Block card", blocks=[MOVE100], x=200, y=330, w=700, h=280, scale=BIG, at="move"),
        A("cards", items=["t.left(90)", "t.forward(100)", 'for i in range(4):'], x=1060, y=270, w=640, gap=125,
          at="which", until="t"),
        A("thought", "Moving ahead?", at="which$+0.2", until="forward", x=1500, y=780),
        A("chip", "t.forward(100)", at="forward@0.3", x=560, y=720, color="green", size=56),
        A("chip", "same number: 100", at="number", until="t", x=1380, y=760, color="yellow", size=44),
        A("chip", "t = our turtle's name", at="t@0.4", x=1380, y=380, color="orange", size=46),
        A("chip", "like a name on a letter", at="letter", x=1380, y=520, color="sky", size=42),
    )),
    # 4. twins 2 and 3: left and color --------------------------------------------------------------------------
    Scene("j3-w05-s04", setting="sky", beats=(
        B("Next block: turn left ninety degrees. Its twin is t.left, with ninety inside.", speaker=NARRATOR,
          cue="left", pause=0.6),
        B("Careful! t.forward and t.left both have a number. Which one moves, and which one turns?",
          speaker=NARRATOR, cue="careful", pause=2.8),
        B("Forward moves. Left turns!", speaker=NARRATOR, cue="answer", pause=0.6),
        B("Say it with me: forward moves, left turns!", speaker=NARRATOR, cue="sayit", pause=1.6),
        B("Now the green pen block: set pen color to blue.", speaker=NARRATOR, cue="pen", pause=0.4),
        B("Its twin is t.color, with blue inside quotation marks.", speaker=NARRATOR, cue="color", pause=0.6),
        B("Blue words, blue lines! Beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("scratch", blocks=[LEFT90], x=200, y=300, panel=False, scale=BIG, at="left"),
        A("arrow", at="left@0.6", x1=870, y1=345, x2=1060, y2=345, color="navy", width=8),
        A("chip", "t.left(90)", at="left@0.6", x=1300, y=345, color="white", size=52),
        A("chip", "forward = moves", at="answer", until="pen", x=760, y=760, color="sky", size=44),
        A("chip", "left = turns", at="answer@0.5", until="pen", x=1260, y=760, color="purple", size=44),
        A("thought", "Moves or turns?", at="careful$+0.2", until="answer", x=960, y=640),
        A("scratch", blocks=[COLOR], x=200, y=540, panel=False, scale=BIG, at="pen"),
        A("arrow", at="color@0.3", x1=870, y1=585, x2=1060, y2=585, color="navy", width=8),
        A("chip", 't.color("blue")', at="color@0.3", x=1330, y=585, color="white", size=52),
        A("chip", '" " around the color', at="color@0.7", x=1330, y=760, color="yellow", size=42),
        A("pixi", x=600, y=920, s=0.5, at="pixi", ground=990, beep="pixi"),
    )),
    # 5. quick quiz: the twin of repeat 4 -----------------------------------------------------------------------
    Scene("j3-w05-s05", setting="peach", beats=(
        B("Quick quiz!", speaker=NARRATOR, cue="quiz", pause=0.4),
        B("Here's the orange repeat four block. Which word card is its twin?", speaker=NARRATOR, cue="which",
          pause=3.2),
        B("For i in range four! It means: do this four times.", speaker=NARRATOR, cue="answer", pause=0.5),
        B("The four is the same as in the repeat block.", speaker=NARRATOR, cue="same", pause=0.6),
        B("Four times, beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Block card", blocks=[("control", "repeat [4]", [])], x=200, y=330, w=740, h=400,
          scale=BIG, at="which"),
        A("cards", items=["t.color(\"blue\")", "for i in range(4):", "t.forward(100)"], x=1060, y=280, w=680,
          gap=130, at="which", active=[None, ("answer", "end"), None]),
        A("thought", "Which twin?", at="which$+0.2", until="answer", x=1400, y=760),
        A("chip", "repeat 4 = for i in range(4):", at="answer@0.3", x=960, y=850, color="green", size=46),
        A("pixi", x=1680, y=900, s=0.5, at="pixi", ground=990, beep="pixi"),
    )),
    # 6. a whole Scratch square in Python words, and the indent ----------------------------------------------
    Scene("j3-w05-s06", setting="mint", beats=(
        B("Now let's turn a whole Scratch square into Python words.", speaker=NARRATOR, cue="whole", pause=0.4),
        B("Read the twins from the top. t.color, blue.", speaker=NARRATOR, cue="l1", pause=0.4),
        B("For i in range four.", speaker=NARRATOR, cue="l2", pause=0.4),
        B("t.forward, one hundred.", speaker=NARRATOR, cue="l3", pause=0.4),
        B("t.left, ninety.", speaker=NARRATOR, cue="l4", pause=0.6),
        B("In Scratch, the blocks inside the repeat sit in its mouth.", speaker=NARRATOR, cue="mouth", pause=0.4),
        B("In Python, the lines inside the loop move in a little. That little gap is called an indent.",
          speaker=NARRATOR, cue="indent", pause=0.5),
        B("Say it with me: indent!", speaker=NARRATOR, cue="sayit", pause=1.4),
        B("In week six, we type lines like these. Here's a sneak peek of what the turtle will draw!",
          speaker=NARRATOR, cue="peek", pause=3.4),
        B("A blue square, from Python words! Today we stay in Scratch.", speaker=NARRATOR, cue="square", pause=0.6),
        B("Same square, blocks or words! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "A square in Python words", at="whole", color="green"),
        A("scratch", "Scratch", blocks=[COLOR, ("control", "repeat [4]", [MOVE100, LEFT90])], x=130, y=260,
          w=860, h=560, scale=BIG, at="whole", until="peek",
          highlight=[(0, "l1", "l1>"), (1, "l2", "l2>"), (2, "l3", "l3>"), (3, "l4", "l4>"),
                     (1, "mouth", "mouth$")]),
        A("code", code=TWINS, title="Python words", x=1050, y=230, w=780, h=430, size=40, at="whole",
          reveal=["l1", "l2", "l3", "l4"],
          highlight=[(1, "l1", "l1>"), (2, "l2", "l2>"), (3, "l3", "l3>"), (4, "l4", "l4>"),
                     (3, "indent@0.3", "sayit$"), (4, "indent@0.3", "sayit$")]),
        A("chip", "inside the loop = moved in", at="indent@0.5", until="sayit", x=1440, y=880, color="yellow",
          size=40),
        A("bigtext", "Indent!", at="sayit", until="peek", x=1440, y=880, size=72, color="orange"),
        A("turtle", code=SNEAK_PEEK, title="Sneak peek: week 6", x=130, y=200, w=860, h=680, at="peek",
          run="peek@0.8", duration=2.6),
        A("chip", "Today: Scratch", at="square@0.6", x=1440, y=880, color="sky", size=44),
    )),
    # 7. wiggle break: be the Python turtle -------------------------------------------------------------------
    Scene("j3-w05-s07", setting="workshop", beats=(
        B("Wiggle break! Stand up and be the Python turtle.", speaker=NARRATOR, cue="wiggle", pause=0.4),
        B("t.forward, three: take three big steps!", speaker=NARRATOR, cue="f3", pause=2.2),
        B("t.left, ninety: a quarter turn left!", speaker=NARRATOR, cue="l90", pause=2.2),
        B("Now for i in range four, with forward and left inside. Walk a square!", speaker=NARRATOR, cue="square",
          pause=5.0),
        B("Did you end where you started? Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("f3", "end")], moods={"start": "happy", "square": "proud"}),
        A("pixi", x=600, y=760, beep="pixi", path=[("square+0.5", 600, 760), ("square+1.4", 760, 760),
                                                    ("square+2.3", 760, 700), ("square+3.2", 600, 700),
                                                    ("square+4.1", 600, 760)]),
        A("chip", "t.forward(3)", at="f3", until="f3>", x=1300, y=400, color="white", size=56),
        A("chip", "3 big steps!", at="f3@0.5", until="f3>", x=1300, y=540, color="sky", size=46),
        A("chip", "t.left(90)", at="l90", until="l90>", x=1300, y=400, color="white", size=56),
        A("chip", "a quarter turn left!", at="l90@0.5", until="l90>", x=1300, y=540, color="purple", size=46),
        A("code", code="for i in range(4):\n    t.forward(3)\n    t.left(90)", title="walk a square", x=960,
          y=280, w=720, h=360, size=40, at="square", shell=False),
        A("chip", "Walk a square!", at="square@0.6", x=1320, y=740, color="green", size=46),
    )),
    # 8. bug-hunt relay, leg 1: The Window --------------------------------------------------------------------
    Scene("j3-w05-s08", setting="mint", beats=(
        B("Time for the bug-hunt relay! Three broken projects, and a sticker for each fix.", speaker=NARRATOR,
          cue="relay", pause=0.5),
        B("Leg one: The Window. It should draw four squares.", speaker=NARRATOR, cue="leg1", pause=0.4),
        B("But watch. The cat goes back and forth on one line!", speaker=NARRATOR, cue="watch", pause=2.4),
        B("Look inside the inside repeat. What is wrong?", speaker=NARRATOR, cue="look", pause=3.2),
        B("There are two turns in there! The second turn belongs under the inside repeat, but still inside the "
          "outside repeat.", speaker=NARRATOR, cue="two", pause=0.5),
        B("Drag the bottom turn out, drop it in the right place, and test again!", speaker=NARRATOR, cue="fix",
          pause=5.2),
        B("A window! Sticker number one!", speaker=NARRATOR, cue="fixed", pause=0.4),
        B("Legs two and three are yours: The Magic Trick, and The Stuck Counter. Change one thing at a time!",
          speaker=NARRATOR, cue="yours", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The relay, leg 1", at="relay", color="navy"),
        A("scratch", "Leg 1: The Window",
          blocks=[FLAG, ERASE, PEN_DOWN, ("control", "repeat [4]", [("control", "repeat [4]",
                                                                    [MOVE60, RIGHT90, RIGHT90])])],
          x=130, y=250, w=860, h=800, scale=1.0, at="leg1", until="fix+0.4",
          highlight=[(4, "look", "two"), (7, "two", "fix+0.4")]),
        A("scratch", "Leg 1: The Window (fixed)",
          blocks=[FLAG, ERASE, PEN_DOWN, ("control", "repeat [4]", [("control", "repeat [4]", [MOVE60, RIGHT90]),
                                                                    RIGHT90])],
          x=130, y=250, w=860, h=800, scale=1.0, at="fix+0.4", highlight=[(7, "fix+0.4", "fix+1.6")]),
        A("sfx", "snap", at="fix+0.4"),
        A("stage", x=1080, y=230, w=760, h=520, at="leg1", until="fix+0.4", flag_at="watch@0.1",
          sprite_scale=0.5, actions=[("watch@0.2", "draw", 8, L, 2.4, 180)]),
        A("stage", x=1080, y=230, w=760, h=520, at="fix+0.4", flag_at="fix+0.7", sprite_scale=0.5,
          actions=window_actions("fix", 0.8)),
        A("chip", "Should do: 4 squares", at="leg1@0.5", until="look", x=1460, y=850, color="green", size=42),
        A("badge", ok=False, at="watch$", until="fix", x=1780, y=290),
        A("thought", "What is wrong?", at="look$+0.2", until="two", x=1460, y=850),
        A("chip", "Two turns: one too many inside", at="two", until="fix", x=1460, y=850, color="orange",
          size=36),
        A("badge", ok=True, at="fixed", x=1780, y=290),
        A("confetti", at="fixed", x=1460, y=480),
        A("icons", at="fixed@0.3", until="yours", x=1460, y=860, items=[("star", "Sticker 1!", "fixed@0.3")]),
        A("cards", items=["Leg 2: The Magic Trick", "Leg 3: The Stuck Counter"], x=1100, y=800, w=700, gap=110,
          reveal=["yours@0.25", "yours@0.5"], at="yours"),
    )),
    # 9. show me, and what am I proud of? --------------------------------------------------------------------
    Scene("j3-w05-s09", setting="workshop", beats=(
        B("While you play, your grown-up may ask: can you show me? That's not a test. Not yet is a fine answer!",
          speaker=NARRATOR, cue="showme", pause=0.6),
        B("We are halfway through Level 3. Think of everything you made: patterns, plans, graphs, the robot "
          "game, and bug fixes.", speaker=NARRATOR, cue="half", pause=0.5),
        B("What are you proud of so far?", speaker=NARRATOR, cue="proud", pause=3.0),
        B("Your grown-up writes it on Our Proud Wall, with your nickname.", speaker=NARRATOR, cue="wall", pause=0.5),
        B("Two rules for proud coders. My own work, or say whose idea it was: the flower idea came from Kai.",
          speaker=NARRATOR, cue="rule1", pause=0.5),
        B("And proud work stays safe: nicknames only, never a full name, school or address.", speaker=NARRATOR,
          cue="rule2", pause=0.6),
        B("I'm proud of my beeps!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "proud": "thinking", "wall": "proud"},
          chin=("proud", "wall")),
        A("pixi", x=600, y=760, beep="pixi", moods={"pixi": "proud"}),
        A("chip", "“Can you show me?”", at="showme@0.2", until="half", x=1260, y=330, color="sky", size=44),
        A("chip", "Not yet = fine!", at="showme@0.7", until="half", x=1260, y=460, color="green", size=46),
        A("cards", items=["Patterns", "Plans", "Graphs", "The robot game", "Bug fixes"], x=1000, y=250, w=560,
          gap=110, reveal=["half@0.45", "half@0.55", "half@0.65", "half@0.75", "half@0.9"], at="half",
          until="wall", color="sky"),
        A("thought", "I'm proud of…", at="proud$+0.2", until="wall", x=1700, y=420),
        A("panel", "Our Proud Wall", at="wall", until="rule1", x=1000, y=260, w=760, size=40, color="orange",
          items=[("wall@0.3", "Pixel Panda: my flower!"), ("wall@0.6", "Robo Kid: my bar graph")]),
        A("icons", at="rule1", x=1260, y=420, gap=340,
          items=[("star", "My own work", "rule1@0.3"), ("person", "Say whose idea", "rule1@0.6")]),
        A("chip", "Nicknames only", at="rule2", x=1260, y=720, color="green", size=46),
        A("icons", at="rule2@0.4", x=1260, y=880, gap=260, crossed=[0, 1, 2], size=28,
          items=[("person", "Full name", "rule2@0.4"), ("book", "School", "rule2@0.6"),
                 ("house", "Address", "rule2@0.8")]),
    )),
    # 10. recap and next -------------------------------------------------------------------------------
    Scene("j3-w05-s10", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Python!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Word twin!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Indent!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("Every Scratch block has a word twin in Python. The t is our turtle, and lines inside a loop are "
          "indented.", speaker=NARRATOR, cue="recap", pause=0.5),
        B("Now it's your turn, with a grown-up.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Match the word twins, run the bug-hunt relay, then plan and build My Best Pattern.", speaker=NARRATOR,
          cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=NARRATOR, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Python!", at="w1", until="w1>", y=560, size=90, color="blue"),
        A("bigtext", "Word twin!", at="w2", until="w2>", y=560, size=90, color="purple"),
        A("bigtext", "Indent!", at="w3", until="w3>", y=560, size=90, color="orange"),
        A("chip", "1 block = 1 word twin", at="recap", until="turn", x=1200, y=470, color="green", size=48),
        A("chip", "t = turtle • indent = inside", at="recap@0.5", until="turn", x=1200, y=600, color="yellow",
          size=44),
        A("banner", "NEXT: Blocks to Words and the relay", at="turn", color="green"),
        A("cards", items=["Match the word twins", "Run the bug-hunt relay", "Build My Best Pattern"], x=960,
          y=280, w=720, gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
