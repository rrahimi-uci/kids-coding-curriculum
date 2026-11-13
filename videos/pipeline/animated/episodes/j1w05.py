"""Junior Level 1 Week 5: Play Day and Show Me (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/1-little-robots/teaching-material/lessons/week05.tex: Play Day, an arrow-maze challenge
card on the floor grid (our own card, not the workbook's Exercise 5.1 maze), a quick quiz on turning on
the spot, the detective steps and the doctor's check-up, the worked example (the wrong sound: Pop
instead of Meow), the bug-hunt relay (Exercise 5.2) with Leg 1 The Quiet Cat solved as the example and
Legs 2 and 3 left for the child with the lesson's hint ladder, Exercise 5.3 My Best Show (the
workbook's idea script) and saying what a script does, what makes a project fun for everyone, the
robot freeze dance, and the recap.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
SAYHI = ("looks", "say [Hi!] for [2] seconds")
MEOW = ("sound", "play sound [Meow] until done")
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage

# ------------------------------------------------------------------------------------------- helpers
STEP = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
RIGHT = {"up": "right", "right": "down", "down": "left", "left": "up"}
LEFT = {v: k for k, v in RIGHT.items()}


def _t(base: str, offset: float) -> str:
    return f"{base}+{offset:.2f}"


def facing(gx, gy, cell, col, row, way, at, until):
    """A short orange arrow that pokes out of the robot's square: the way the robot faces."""
    cx, cy = gx + col * cell + cell / 2, gy + row * cell + cell / 2
    dx, dy = STEP[way]
    return A("arrow", at=at, until=until, x1=cx + dx * cell * 0.30, y1=cy + dy * cell * 0.30,
             x2=cx + dx * cell * 0.84, y2=cy + dy * cell * 0.84, color="#E8590C", width=14, duration=0.25)


def walk(gx, gy, cell, steps, col, row, way, shown_from, until, move=0.8):
    """Walker keyframes and facing arrows for a row of cards: steps=[(base cue, offset, card)]."""
    path, arrows = [(shown_from, col, row)], []
    for base, offset, card in steps:
        arrows.append(facing(gx, gy, cell, col, row, way, shown_from, _t(base, offset)))
        if card == "FORWARD":
            dc, dr = STEP[way]
            path.append((_t(base, offset), col, row))
            col, row = col + dc, row + dr
            path.append((_t(base, offset + move), col, row))
            shown_from = _t(base, offset + move)
        else:
            way = RIGHT[way] if card == "TURN RIGHT" else LEFT[way]
            shown_from = _t(base, offset + 0.3)
    arrows.append(facing(gx, gy, cell, col, row, way, shown_from, until))
    return path, arrows


# Our own challenge card: a tree straight ahead of the robot, the star up and to the right.
MX, MY, MCELL = 1080, 250, 170
MAZE = [".G.", "F..", "S.."]
MAZE_MARKS = [("start", 0, 1, "★"), ("start", 1, 0, "♣")]
ROUTE = ["TURN RIGHT", "FORWARD", "TURN LEFT", "FORWARD", "FORWARD"]
ROUTE_STEPS = [("walk", 0.6 + 1.2 * i, card) for i, card in enumerate(ROUTE)]
S3_PATH, S3_ARROWS = walk(MX, MY, MCELL, ROUTE_STEPS, 0, 2, "up", "start", "end")

SHOW = [FLAG, ("looks", "say [Watch me!] for [2] seconds"),
        ("control", "repeat [4]", [("looks", "next costume"), ("motion", "move [10] steps"),
                                   ("control", "wait [1] seconds")]),
        ("looks", "say [Ta-da!] for [2] seconds")]

EPISODE = Episode(level="j1", week=5, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w05-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi", pause=0.3),
        B("Play Day! Beep beep, hooray!", speaker=PIXI, cue="hooray", pause=0.5),
        B("Today, we practice everything we know: steps in order, repeat, and fixing bugs.", speaker=NARRATOR,
          cue="practice", pause=0.5),
        B("Then you make your very best show, and show a grown-up what you can do.", speaker=NARRATOR, cue="show",
          pause=0.5),
        B("It is not a test. It is play! Let's go!", speaker=NARRATOR, cue="go", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hooray"), ("go", "end")],
          moods={"start": "happy", "show": "proud"}),
        A("pixi", x=640, y=760, at="hi@0.5", drop=True),
        A("banner", "MISSION: Play Day!", at="hooray"),
        A("icons", at="practice", until="go", x=1320, y=470, gap=300,
          items=[("check", "Steps in order", "practice@0.5"), ("gear", "Repeat", "practice@0.7"),
                 ("magnifier", "Fixing bugs", "practice@0.85")]),
        A("chip", "Not a test. It is play!", at="go", x=1320, y=520, color="green", size=52),
    )),
    # 2. arrow maze: the challenge card -------------------------------------------------------------
    Scene("j1-w05-s02", setting="sky", beats=(
        B("First, an arrow maze! Remember our robot cards from week one?", speaker=NARRATOR, cue="maze", pause=0.5),
        B("FORWARD is one square ahead. TURN LEFT and TURN RIGHT are a quarter turn, on the spot.",
          speaker=NARRATOR, cue="cards", pause=0.6),
        B("Here is a challenge card. Pixi starts here, facing up. There is the star.", speaker=NARRATOR,
          cue="card", pause=0.5),
        B("And this is a tree. Robots cannot walk on trees!", speaker=NARRATOR, cue="tree", pause=0.6),
        B("Which cards will take Pixi to the star?", speaker=NARRATOR, cue="which", pause=3.2),
    ), actions=(
        A("cards", items=["FORWARD", "TURN LEFT", "TURN RIGHT"], x=150, y=300, w=500, gap=140, size=44,
          at="maze", until="card", reveal=["maze@0.5", "cards@0.5", "cards@0.6"]),
        A("chip", "a quarter turn, on the spot", at="cards@0.5", until="card", x=400, y=800, color="orange",
          size=40),
        A("grid", x=MX, y=MY, cell=MCELL, rows=MAZE, marks=MAZE_MARKS, at="card", walker=[("card", 0, 2)]),
        facing(MX, MY, MCELL, 0, 2, "up", "card@0.4", "end"),
        A("chip", "tree: no walking here!", at="tree", x=1335, y=900, color="green", size=44),
        A("thought", "Which cards?", at="which$+0.2", until="end", x=500, y=560),
        A("aiden", x=230, y=1080, s=0.5, at="card", moods={"start": "happy", "which": "thinking"},
          chin=("which", "end")),
    )),
    # 3. arrow maze: walk it ---------------------------------------------------------------------------
    Scene("j1-w05-s03", setting="sky", beats=(
        B("Let's try: TURN RIGHT, FORWARD, TURN LEFT, FORWARD, FORWARD.", speaker=NARRATOR, cue="plan", pause=0.6),
        B("Pixi walks the cards, one at a time.", speaker=NARRATOR, cue="walk", pause=6.4),
        B("Pixi is on the star, and did not step on the tree!", speaker=NARRATOR, cue="star", pause=0.4),
        B("Beep! Star reached!", speaker=PIXI, cue="beep", pause=0.5),
        B("If your robot misses, find the wrong card, and change only that one.", speaker=NARRATOR, cue="miss",
          pause=0.8),
    ), actions=(
        A("cards", items=ROUTE, x=150, y=240, w=480, gap=118, size=40,
          reveal=["plan@0.1", "plan@0.3", "plan@0.5", "plan@0.7", "plan@0.85"],
          active=[(_t(b, o), _t(b, o + 1.2)) for b, o, _ in ROUTE_STEPS],
          done=[_t(b, o + 1.0) for b, o, _ in ROUTE_STEPS]),
        A("grid", x=MX, y=MY, cell=MCELL, rows=MAZE, marks=MAZE_MARKS, walker=S3_PATH),
        *S3_ARROWS,
        A("badge", ok=True, at="star", x=1780, y=240),
        A("confetti", at="star", x=1330, y=480),
        A("chip", "Change only the wrong card", at="miss", x=1335, y=900, color="yellow", size=42),
    )),
    # 4. quick quiz: does a turn move the robot? ----------------------------------------------------
    Scene("j1-w05-s04", setting="peach", beats=(
        B("Quick quiz!", speaker=NARRATOR, cue="quiz", pause=0.4),
        B("Pixi is facing up. The next card says TURN RIGHT.", speaker=NARRATOR, cue="facing", pause=0.5),
        B("Will Pixi move to a new square?", speaker=NARRATOR, cue="move", pause=3.2),
        B("No! Pixi turns a quarter turn, on the spot.", speaker=NARRATOR, cue="no", pause=0.6),
        B("The feet stay in the same square. Only FORWARD moves to a new square.", speaker=NARRATOR, cue="feet",
          pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("cards", items=["TURN RIGHT"], x=150, y=420, w=500, size=46, at="facing@0.6",
          active=[("no", "feet")]),
        A("grid", x=MX, y=MY, cell=MCELL, rows=["...", "...", "..."], walker=[("start", 1, 1)]),
        facing(MX, MY, MCELL, 1, 1, "up", "start", "no+0.3"),
        facing(MX, MY, MCELL, 1, 1, "right", "no+0.6", "end"),
        A("thought", "New square?", at="move$+0.2", until="no", x=1335, y=900),
        A("chip", "A turn is on the spot", at="no@0.5", x=1335, y=900, color="orange", size=46),
        A("aiden", x=230, y=1080, s=0.5, moods={"move": "thinking", "no": "happy"}, chin=("move", "no")),
    )),
    # 5. detective steps and the doctor -------------------------------------------------------------
    Scene("j1-w05-s05", setting="lavender", beats=(
        B("Next, bugs! Remember our detective steps?", speaker=NARRATOR, cue="steps", pause=0.4),
        B("Test: click the flag and watch. Look: what did we want, and what happened? Change one thing, then "
          "test again.", speaker=NARRATOR, cue="three", pause=0.6),
        B("It's like a doctor's check-up. A doctor does not guess.", speaker=NARRATOR, cue="doctor", pause=0.4),
        B("They look, they listen, they try one thing, and they check again.", speaker=NARRATOR, cue="check",
          pause=0.6),
        B("Bug detectives do the same!", speaker=PIXI, cue="same", pause=0.8),
    ), actions=(
        A("cards", items=["Test", "Look", "Change one thing"], x=200, y=300, w=620, gap=150, size=48,
          color="green", reveal=["three", "three@0.25", "three@0.6"],
          active=[("three", "three@0.25"), ("three@0.25", "three@0.6"), ("three@0.6", "three$")]),
        A("chip", "A doctor does not guess", at="doctor@0.5", x=1360, y=300, color="sky", size=46),
        A("icons", at="check", x=1360, y=560, gap=260,
          items=[("magnifier", "Look", "check@0.1"), ("music", "Listen", "check@0.3"),
                 ("check", "Check again", "check@0.7")]),
        A("pixi", x=1360, y=930, s=0.5, at="same", ground=1010),
        A("aiden", x=200, y=1080, s=0.5, moods={"start": "happy", "same": "proud"}, wave=("steps", "steps$")),
    )),
    # 6. worked example: the wrong sound --------------------------------------------------------------
    Scene("j1-w05-s06", setting="mint", beats=(
        B("Watch me fix a tiny bug. I want my cat to meow.", speaker=NARRATOR, cue="want", pause=0.5),
        B("Yellow Events: when green flag clicked. Pink Sound: play sound Meow until done. But I pick Pop in "
          "the list, on purpose.", speaker=NARRATOR, cue="build", pause=0.6),
        B("Test!", speaker=NARRATOR, cue="test", pause=1.8),
        B("Look: I wanted a meow. I heard a pop! The sound block is the clue.", speaker=NARRATOR, cue="look",
          pause=0.6),
        B("Change one thing: click the little arrow in the sound block, and pick Meow.", speaker=NARRATOR,
          cue="change", pause=0.6),
        B("Test again!", speaker=NARRATOR, cue="again", pause=2.0),
        B("Meow! Bug fixed. That is how the relay works.", speaker=NARRATOR, cue="fixed", pause=0.8),
    ), actions=(
        A("scratch", "The wrong sound", blocks=[FLAG, ("sound", "play sound [Pop] until done")], x=130, y=280,
          w=900, h=380, scale=BIG, reveal=["build@0.15", "build@0.4"],
          edits=[("change@0.8", 1, "play sound [Meow] until done")],
          highlight=[(1, "look@0.6", "look$+0.4"), (1, "change", "change$+0.4")]),
        A("chip", "Sound: pink", at="build@0.3", until="test", x=580, y=800, color="pink", size=44),
        A("stage", x=1100, y=230, w=700, h=480, flag_at="again+0.3", sprite_scale=CAT,
          actions=[("test+0.4", "say", "Pop!", 1.0), ("again+0.4", "say", "Meow!", 1.4)]),
        A("sfx", "pop", at="test+0.4"),
        A("badge", ok=False, at="look", until="again", x=1760, y=290),
        A("chip", "wanted: meow • heard: pop", at="look", until="again", x=1450, y=860, color="red", size=40),
        A("badge", ok=True, at="fixed", x=1760, y=290),
        A("confetti", at="fixed", x=1450, y=470),
        A("chip", "Bug fixed!", at="fixed", x=1450, y=860, color="green", size=48),
    )),
    # 7. the bug-hunt relay ---------------------------------------------------------------------------
    Scene("j1-w05-s07", setting="sky", beats=(
        B("Now, the bug-hunt relay! There are three broken projects, like three legs of a race.",
          speaker=NARRATOR, cue="relay", pause=0.5),
        B("Each card says what the project should do. You build it exactly as you see it, then test, look, "
          "and change one thing.", speaker=NARRATOR, cue="card", pause=0.6),
        B("Fix one leg, get a sticker, then swap Driver!", speaker=NARRATOR, cue="sticker", pause=0.4),
        B("Let's do Leg one together.", speaker=NARRATOR, cue="leg1", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The relay", at="relay", color="navy"),
        A("cards", items=["The Quiet Cat: say hi and meow", "Bye Before Hi: hi first, then bye",
                          "Too Many Meows: meow three times"], x=200, y=280, w=980, gap=150, size=40,
          reveal=["relay@0.5", "relay@0.7", "relay@0.9"], active=[("leg1", "end"), None, None]),
        A("icons", at="sticker", x=1500, y=500, gap=260,
          items=[("star", "Sticker!", "sticker@0.3"), ("laptop", "Swap Driver", "sticker@0.7")]),
        A("aiden", x=200, y=1080, s=0.5, moods={"start": "happy", "leg1": "proud"}),
    )),
    # 8. Leg 1: The Quiet Cat -------------------------------------------------------------------------
    Scene("j1-w05-s08", setting="mint", beats=(
        B("Leg one: The Quiet Cat. It should say hi and meow.", speaker=NARRATOR, cue="quiet", pause=0.5),
        B("Test!", speaker=NARRATOR, cue="test", pause=2.8),
        B("Look: the cat says hi, but there is no meow.", speaker=NARRATOR, cue="look", pause=0.5),
        B("Is every block touching?", speaker=NARRATOR, cue="touch", pause=3.0),
        B("No! The sound block is not snapped on. Let's drag it until it clicks.", speaker=NARRATOR, cue="fix",
          pause=0.8),
        B("Test again!", speaker=NARRATOR, cue="again", pause=3.6),
        B("Hi, and meow! One sticker for us!", speaker=NARRATOR, cue="sticker", pause=0.4),
        B("Beep! Swap Driver!", speaker=PIXI, cue="swap", pause=0.8),
    ), actions=(
        A("banner", "Leg 1: The Quiet Cat", at="quiet", color="navy"),
        A("scratch", "Should: say hi and meow", blocks=[FLAG, SAYHI], x=130, y=260, w=900, h=360, scale=BIG,
          until="fix@0.7"),
        A("scratch", blocks=[MEOW], x=190, y=720, w=700, h=150, panel=False, scale=BIG, until="fix@0.7",
          highlight=[(0, "fix", "fix@0.7")]),
        A("scratch", "Should: say hi and meow", blocks=[FLAG, SAYHI, MEOW], x=130, y=260, w=900, h=460,
          scale=BIG, at="fix@0.7", highlight=[(2, "fix@0.7", "fix$+0.6")]),
        A("sfx", "snap", at="fix@0.7"),
        A("stage", x=1100, y=230, w=700, h=480, flag_at="again+0.2", sprite_scale=CAT,
          actions=[("test+0.3", "say", "Hi!", 2.0), ("again+0.3", "say", "Hi!", 2.0),
                   ("again+2.4", "say", "Meow!", 1.0)]),
        A("sfx", "pop", at="test+0.2"),
        A("badge", ok=False, at="look", until="again", x=1760, y=290),
        A("thought", "Touching?", at="touch$+0.2", until="fix", x=1450, y=870),
        A("chip", "Not snapped on", at="fix", until="again", x=1450, y=860, color="red", size=46),
        A("badge", ok=True, at="sticker", x=1760, y=290),
        A("icons", at="sticker", x=1450, y=830, items=[("star", "Sticker!", "sticker")]),
    )),
    # 9. legs 2 and 3, and My Best Show ---------------------------------------------------------------
    Scene("j1-w05-s09", setting="lavender", beats=(
        B("Legs two and three are for you and your partner to fix!", speaker=NARRATOR, cue="yours", pause=0.4),
        B("Stuck? Read the should-do line again. What is different?", speaker=NARRATOR, cue="stuck", pause=0.6),
        B("Then, build your very best show. It needs the green flag, and a repeat.", speaker=NARRATOR, cue="best",
          pause=0.5),
        B("Here is one idea. Watch!", speaker=NARRATOR, cue="idea", pause=7.6),
        B("Now tell your grown-up what your script does. My script makes the cat say watch me, walk four "
          "little steps, and say ta-da!", speaker=NARRATOR, cue="tell", pause=0.8),
    ), actions=(
        A("chip", "Legs 2 and 3: your turn!", at="yours", until="best", x=960, y=380, color="green", size=50),
        A("chip", "Read the should-do line again", at="stuck", until="best", x=960, y=540, color="yellow",
          size=46),
        A("banner", "Exercise 5.3: My Best Show", at="best", color="green"),
        A("chip", "green flag + repeat", at="best@0.5", until="idea", x=960, y=460, color="orange", size=50),
        A("scratch", "My Best Show", blocks=SHOW, x=110, y=250, w=960, h=800, scale=1.1, at="idea"),
        A("stage", x=1120, y=250, w=700, h=480, at="idea", flag_at="idea+0.8", sprite_scale=CAT,
          actions=[("idea+0.9", "say", "Watch me!", 2.0), ("idea+2.9", "move", 10, 0.4),
                   ("idea+3.9", "move", 10, 0.4), ("idea+4.9", "move", 10, 0.4), ("idea+5.9", "move", 10, 0.4),
                   ("idea+6.9", "say", "Ta-da!", 2.0)]),
        A("chip", "My script makes the cat...", at="tell", x=1470, y=880, color="white", size=42),
    )),
    # 10. what makes a project fun for everyone ----------------------------------------------------------
    Scene("j1-w05-s10", setting="workshop", beats=(
        B("What makes a project fun for everyone who sees it?", speaker=NARRATOR, cue="fun", pause=2.4),
        B("Kind words in the speech bubbles.", speaker=NARRATOR, cue="kind", pause=0.4),
        B("Sounds that are not too loud or too long. Remember Too Many Meows!", speaker=NARRATOR, cue="loud",
          pause=0.4),
        B("Everyone gets a turn to click the flag.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("And nicknames only, so everyone stays safe.", speaker=NARRATOR, cue="nick", pause=0.6),
        B("Do you agree? Show me a big thumbs up!", speaker=NARRATOR, cue="thumbs", pause=2.0),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "thinking", "kind": "happy", "nick": "proud"},
          chin=("fun", "kind"), wave=("thumbs", "end")),
        A("pixi", x=620, y=760),
        A("thought", "Fun for everyone?", at="fun$+0.2", until="kind", x=1300, y=440),
        A("icons", at="kind", x=1300, y=440, gap=270,
          items=[("heart", "Kind words", "kind"), ("music", "Not too loud", "loud"),
                 ("person", "Everyone's turn", "turn"), ("lock", "Nicknames only", "nick")]),
    )),
    # 11. robot freeze dance (wiggle break) --------------------------------------------------------------
    Scene("j1-w05-s11", setting="workshop", beats=(
        B("Wiggle break! Robot freeze dance. Stand up!", speaker=NARRATOR, cue="up", pause=0.4),
        B("Walk like a stiff robot. When you hear bug, freeze! When you hear fixed, walk again.", speaker=NARRATOR,
          cue="rules", pause=0.6),
        B("Robot walk!", speaker=NARRATOR, cue="walk1", pause=1.6),
        B("Bug!", speaker=PIXI, cue="bug1", pause=1.6),
        B("Fixed!", speaker=NARRATOR, cue="fix1", pause=1.6),
        B("Bug!", speaker=PIXI, cue="bug2", pause=1.6),
        B("Fixed! Now look far out of a window, and count to five. Rest your eyes.", speaker=NARRATOR, cue="eyes",
          pause=2.0),
    ), actions=(
        A("aiden", x=320, y=960, wave=[("walk1", "bug1"), ("fix1", "bug2")],
          moods={"start": "happy", "bug1": "surprised", "fix1": "happy", "bug2": "surprised", "eyes": "happy"}),
        A("pixi", x=640, y=760, moods={"bug1": "surprised", "fix1": "happy", "bug2": "surprised", "eyes": "happy"},
          path=[("walk1", 640, 760), ("walk1+1.2", 760, 760), ("fix1", 760, 760), ("fix1+1.2", 640, 760)]),
        A("bigtext", "Robot walk!", at="walk1", until="walk1>", x=1350, y=480, size=90, color="green"),
        A("bigtext", "BUG! Freeze!", at="bug1", until="bug1>", x=1350, y=480, size=90, color="red"),
        A("bigtext", "Fixed!", at="fix1", until="fix1>", x=1350, y=480, size=90, color="green"),
        A("bigtext", "BUG! Freeze!", at="bug2", until="bug2>", x=1350, y=480, size=90, color="red"),
        A("icons", at="eyes@0.4", x=1350, y=480, items=[("house", "Look far away", "eyes@0.4")]),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j1-w05-s12", setting="workshop", tail=0.8, beats=(
        B("Say what we practiced with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Steps in order!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Repeat!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Fix the bug!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("Now it's your turn, with a grown-up.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Solve the arrow maze, run the bug-hunt relay, then build your best show and say what it does.",
          speaker=NARRATOR, cue="next", pause=0.6),
        B("Color one star for each relay leg you fix.", speaker=NARRATOR, cue="stars", pause=0.5),
        B("Not yet is OK. Every coder keeps practicing. See you next week. Happy coding!", speaker=NARRATOR,
          cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Steps in order!", at="w1", until="w1>", y=560, size=90, color="blue"),
        A("bigtext", "Repeat!", at="w2", until="w2>", y=560, size=90, color="orange"),
        A("bigtext", "Fix the bug!", at="w3", until="w3>", y=560, size=90, color="green"),
        A("banner", "NEXT: Arrow Maze, Relay and My Best Show", at="turn", color="green"),
        A("cards", items=["Arrow Maze", "Bug-Hunt Relay", "My Best Show"], x=1000, y=300, w=640, gap=120,
          reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "Not yet is OK!", at="bye", x=1320, y=760, color="sky", size=46),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
