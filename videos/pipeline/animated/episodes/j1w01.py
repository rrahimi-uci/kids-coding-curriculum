"""Junior Level 1 Week 1: Robots Need Instructions (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/1-little-robots/teaching-material/lessons/week01.tex: the first episode of the junior
series. Aiden and Pixi say hello, the "what do you like to make?" chat, our two rules (nicknames only,
and the "ask a grown-up!" game), a robot follows instructions and cannot guess (the blindfold friend),
the three arrow cards (FORWARD, TURN LEFT, TURN RIGHT: a quarter turn on the spot), a program and an
algorithm, the worked example (the robot walks to the star), the order matters, Exercise 1.2 The Wrong
Card (Ada's bug hunt), the robot dance wiggle break, and the parent-robot exercises for home.
Fully unplugged: no Scratch this week. Pixi is the robot on the floor grid.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

# ------------------------------------------------------------------------------------------- helpers
STEP = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
RIGHT = {"up": "right", "right": "down", "down": "left", "left": "up"}
LEFT = {v: k for k, v in RIGHT.items()}


def _t(base: str, offset: float) -> str:
    return f"{base}+{offset:.2f}" if offset >= 0 else f"{base}-{-offset:.2f}"


def facing(gx, gy, cell, col, row, way, at, until):
    """A short orange arrow that pokes out of the robot's square: the way the robot faces."""
    cx, cy = gx + col * cell + cell / 2, gy + row * cell + cell / 2
    dx, dy = STEP[way]
    return A("arrow", at=at, until=until, x1=cx + dx * cell * 0.30, y1=cy + dy * cell * 0.30,
             x2=cx + dx * cell * 0.84, y2=cy + dy * cell * 0.84, color="#E8590C", width=14, duration=0.25)


def walk(gx, gy, cell, steps, col, row, way, shown_from, until, move=0.8):
    """Walker keyframes and facing arrows for a row of cards.

    steps: [(base cue, offset seconds, card)] where card is FORWARD, TURN LEFT or TURN RIGHT.
    Returns (path, arrows, (col, row, way)) so a later walk can carry on.
    """
    path = [(shown_from, col, row)]
    arrows = []
    for base, offset, card in steps:
        if card == "FORWARD":
            arrows.append(facing(gx, gy, cell, col, row, way, shown_from, _t(base, offset)))
            dc, dr = STEP[way]
            path.append((_t(base, offset), col, row))
            col, row = col + dc, row + dr
            path.append((_t(base, offset + move), col, row))
            shown_from = _t(base, offset + move)
        else:
            arrows.append(facing(gx, gy, cell, col, row, way, shown_from, _t(base, offset)))
            way = RIGHT[way] if card == "TURN RIGHT" else LEFT[way]
            shown_from = _t(base, offset + 0.3)
    arrows.append(facing(gx, gy, cell, col, row, way, shown_from, until))
    return path, arrows, (col, row, way)


# Floor grid for the worked example: 4 by 4, start in the near left corner, the star two ahead and one right.
GX, GY, CELL = 1100, 250, 150
FLOOR = ["....", ".G..", "....", "S..."]
STAR = [("start", 1, 1, "★")]
PLAN = ["FORWARD", "FORWARD", "TURN RIGHT", "FORWARD"]

# Ada's 3 by 3 grid for the bug hunt: start in the near left corner, the star in the far right corner.
AX, AY, ACELL = 1020, 250, 170
ADA_ROWS = ["..G", "...", "S.."]
ADA_STAR = [("start", 0, 2, "★")]
ADA = ["FORWARD", "TURN RIGHT", "FORWARD", "FORWARD", "FORWARD"]
ADA_FIXED = ["FORWARD", "FORWARD", "TURN RIGHT", "FORWARD", "FORWARD"]

# scene 7: the plan, read card by card
S7_PATH, S7_ARROWS, _ = walk(GX, GY, CELL, [("c1", 0.1, "FORWARD"), ("c2", 0.1, "FORWARD"), ("c3", 0.2, "TURN RIGHT"),
                                            ("c4", 0.1, "FORWARD")], 0, 3, "up", "start", "end")
# scene 8: TURN RIGHT first
S8_PATH, S8_ARROWS, _ = walk(GX, GY, CELL, [("test", 0.6, "TURN RIGHT"), ("test", 1.7, "FORWARD"),
                                            ("test", 2.9, "FORWARD"), ("test", 4.1, "FORWARD")], 0, 3, "up", "what",
                             "end")
# scene 9: Ada's buggy row, then the fixed row
S9_BUG_STEPS = [("test", 0.6 + 1.25 * i, card) for i, card in enumerate(ADA)]
S9_PATH1, S9_ARROWS1, _ = walk(AX, AY, ACELL, S9_BUG_STEPS, 0, 2, "up", "ada", "move")
S9_FIX_STEPS = [("move", 3.2 + 1.25 * i, card) for i, card in enumerate(ADA_FIXED)]
S9_PATH2, S9_ARROWS2, _ = walk(AX, AY, ACELL, S9_FIX_STEPS, 0, 2, "up", "move+1.0", "end")
S9_PATH = S9_PATH1 + [("move+0.2", 3, 1), ("move+1.0", 0, 2)] + S9_PATH2[1:]


def card_windows(steps, last):
    """active windows for cards: each card glows from its step until the next one."""
    times = [_t(base, offset) for base, offset, _ in steps] + [last]
    return [(times[i], times[i + 1]) for i in range(len(steps))]


EPISODE = Episode(level="j1", week=1, scenes=(
    # 1. hello! -------------------------------------------------------------------------------------
    Scene("j1-w01-s01", setting="workshop", lead_in=0.3, beats=(
        B("Meet Aiden, an eight-year-old scientist and builder who loves making things.", speaker=NARRATOR,
          cue="hi", pause=0.4),
        B("And meet Pixi, his helpful robot friend!", speaker=NARRATOR, cue="friend", pause=0.3),
        B("Beep boop! Hello, coders! I'm so happy to meet you!", speaker=PIXI, cue="hello", pause=0.5),
        B("Welcome to Kids Coding! In this club, you will make your own animations and games.", speaker=NARRATOR,
          cue="welcome", pause=0.5),
        B("But first, I want to know about you. What do you like to make? Drawings? Songs? Stories?",
          speaker=NARRATOR, cue="make", pause=3.0),
        B("Those are all great ideas! Every answer is a good answer.", speaker=NARRATOR, cue="great", pause=0.5),
        B("Today, we start without a computer. We start with a robot!", speaker=NARRATOR, cue="today", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hi$"), ("hello", "hello$")],
          moods={"start": "happy", "make": "thinking", "great": "happy", "today": "proud"},
          chin=("make$", "great")),
        A("pixi", x=640, y=760, at="friend", drop=True),
        A("icons", at="make", until="today", x=1300, y=480, gap=280,
          items=[("star", "Drawings", "make@0.6"), ("music", "Songs", "make@0.75"), ("book", "Stories", "make@0.9")]),
        A("thought", "What do I like to make?", at="make$+0.2", until="great", x=1300, y=820),
        A("banner", "MISSION: Help the robot reach the star", at="today"),
        A("chip", "No computer today!", at="today@0.3", x=1300, y=560, color="yellow", size=48),
    )),
    # 2. nicknames ----------------------------------------------------------------------------------
    Scene("j1-w01-s02", setting="workshop", beats=(
        B("Every coder in our club has a nickname.", speaker=NARRATOR, cue="every", pause=0.4),
        B("A nickname is a pretend name. We use it instead of our real name.", speaker=NARRATOR, cue="pretend",
          pause=0.6),
        B("Aiden's coding nickname is Rocket Fox.", speaker=NARRATOR, cue="mine", pause=0.4),
        B("And mine is Captain Bolt! Beep!", speaker=PIXI, cue="bolt", pause=0.6),
        B("What nickname will you pick? Maybe Rainbow Shark, or Pixel Panda?", speaker=NARRATOR, cue="pick",
          pause=3.0),
        B("Ask your grown-up to help you write it on a sticky note. That is your coding badge!", speaker=NARRATOR,
          cue="badge", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "pick": "thinking", "badge": "proud"},
          chin=("pick$", "badge"), point=("pretend", "pretend$")),
        A("pixi", x=620, y=760, moods={"bolt": "proud"}),
        A("chip", "nickname = a pretend name", at="pretend", until="pick", x=1300, y=360, color="orange", size=46),
        A("chip", "Rocket Fox", at="mine", until="pick", x=1100, y=520, color="yellow", size=48),
        A("chip", "Captain Bolt", at="bolt", until="pick", x=1500, y=520, color="sky", size=48),
        A("thought", "My nickname is...", at="pick$+0.2", until="badge", x=1300, y=500),
        A("chip", "Nicknames only", at="badge", x=1300, y=420, color="green", size=48),
        A("chip", "My badge: Pixel Panda", at="badge@0.5", x=1300, y=560, color="white", size=44),
    )),
    # 3. ask a grown-up! (movement game) ------------------------------------------------------------
    Scene("j1-w01-s03", setting="workshop", beats=(
        B("Here is our second rule. Sometimes an app asks for things.", speaker=NARRATOR, cue="second", pause=0.4),
        B("Let's play a game! If an app asks for anything, put your hands on your head and shout: ask a grown-up!",
          speaker=NARRATOR, cue="game", pause=0.6),
        B("The app says: What is your name?", speaker=NARRATOR, cue="q1", pause=0.4),
        B("Ask a grown-up!", speaker=NARRATOR, cue="a1", pause=1.0),
        B("The app says: Can I take a photo?", speaker=NARRATOR, cue="q2", pause=0.4),
        B("Ask a grown-up!", speaker=NARRATOR, cue="a2", pause=1.0),
        B("Tap OK to buy gems!", speaker=NARRATOR, cue="q3", pause=0.4),
        B("Ask a grown-up!", speaker=NARRATOR, cue="a3", pause=1.0),
        B("Where do you live?", speaker=NARRATOR, cue="q4", pause=0.4),
        B("Ask a grown-up! Beep!", speaker=PIXI, cue="a4", pause=0.8),
        B("Great job! Those are our two rules: nicknames only, and when an app asks for anything, we stop and "
          "ask a grown-up.", speaker=NARRATOR, cue="rules", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("a1", "a1$"), ("a2", "a2$"), ("a3", "a3$")],
          moods={"start": "happy", "q1": "surprised", "a1": "happy", "q2": "surprised", "a2": "happy",
                 "q3": "surprised", "a3": "happy", "q4": "surprised", "a4": "happy", "rules": "proud"}),
        A("pixi", x=620, y=760, beep="a4", moods={"q4": "surprised", "a4": "happy"}),
        A("laptop", x=1320, y=760, s=1.2, at="game", until="rules"),
        A("bubble", "What is your name?", x=1320, y=430, at="q1", until="a1$", tail="down"),
        A("bubble", "Can I take a photo?", x=1320, y=430, at="q2", until="a2$", tail="down"),
        A("bubble", "Tap OK to buy gems!", x=1320, y=430, at="q3", until="a3$", tail="down"),
        A("bubble", "Where do you live?", x=1320, y=430, at="q4", until="a4$", tail="down"),
        A("bigtext", "Ask a grown-up!", at="a1", until="a1>", x=1320, y=940, size=60, color="green"),
        A("bigtext", "Ask a grown-up!", at="a2", until="a2>", x=1320, y=940, size=60, color="green"),
        A("bigtext", "Ask a grown-up!", at="a3", until="a3>", x=1320, y=940, size=60, color="green"),
        A("bigtext", "Ask a grown-up!", at="a4", until="a4>", x=1320, y=940, size=60, color="green"),
        A("icons", at="rules", x=1300, y=430, gap=340,
          items=[("person", "Nicknames only", "rules@0.25"), ("grownup", "Ask a grown-up", "rules@0.6")]),
    )),
    # 4. robots cannot guess ------------------------------------------------------------------------
    Scene("j1-w01-s04", setting="sky", beats=(
        B("A robot is a machine that follows instructions.", speaker=NARRATOR, cue="robot", pause=0.4),
        B("Robots are very fast, but they cannot guess what we mean.", speaker=NARRATOR, cue="guess", pause=0.5),
        B("Watch this. Pixi, go to the star!", speaker=NARRATOR, cue="go", pause=0.6),
        B("Does not compute. I need cards!", speaker=PIXI, cue="compute", pause=0.8),
        B("See? A robot is like a friend wearing a blindfold. If we say: over there, it does not help.",
          speaker=NARRATOR, cue="blind", pause=0.5),
        B("We have to give exact steps, one at a time, in the right order.", speaker=NARRATOR, cue="exact",
          pause=0.8),
    ), actions=(
        A("grid", x=GX, y=GY, cell=CELL, rows=FLOOR, marks=STAR, walker=[("start", 0, 3)]),
        facing(GX, GY, CELL, 0, 3, "up", "start", "end"),
        A("chip", "robot = a machine that follows instructions", at="robot", until="go", x=860, y=960,
          color="sky", size=40),
        A("chip", "Robots cannot guess", at="guess", until="go", x=480, y=400, color="orange", size=46),
        A("bubble", "Does not compute!", x=1175, y=690, at="compute", until="blind", tail="down", size=34),
        A("chip", "Over there? It does not help.", at="blind@0.5", until="exact", x=480, y=400, color="red",
          size=40),
        A("chip", "exact steps, in order", at="exact", x=480, y=400, color="green", size=48),
        A("aiden", x=230, y=1080, s=0.55, moods={"go": "happy", "compute": "surprised", "blind": "happy"},
          point=("go", "go$")),
    )),
    # 5. the three cards (movement) -----------------------------------------------------------------
    Scene("j1-w01-s05", setting="mint", beats=(
        B("So here are our robot cards.", speaker=NARRATOR, cue="here", pause=0.4),
        B("FORWARD means: move one square ahead.", speaker=NARRATOR, cue="fwd", pause=1.0),
        B("TURN LEFT and TURN RIGHT mean: turn a quarter turn, on the spot.", speaker=NARRATOR, cue="turn",
          pause=0.8),
        B("The robot's feet stay in the same square. A turn is not a step!", speaker=NARRATOR, cue="feet",
          pause=0.6),
        B("Can you do it? Stand up. Turn right, a quarter turn, on the spot!", speaker=NARRATOR, cue="stand",
          pause=2.6),
        B("Now turn left, back again. Great turning!", speaker=NARRATOR, cue="back", pause=1.0),
        B("Beep! Good robots!", speaker=PIXI, cue="good", pause=0.8),
    ), actions=(
        A("cards", items=["FORWARD", "TURN LEFT", "TURN RIGHT"], x=150, y=280, w=520, gap=140, size=44,
          reveal=["here@0.3", "turn", "turn@0.3"],
          active=[("fwd", "fwd>"), ("turn", "turn@0.6"), ("turn@0.6", "feet")]),
        A("grid", x=1080, y=250, cell=170, rows=["...", "...", "..."],
          walker=[("start", 1, 2), ("fwd+0.4", 1, 2), ("fwd+1.2", 1, 1)]),
        facing(1080, 250, 170, 1, 2, "up", "start", "fwd+0.4"),
        facing(1080, 250, 170, 1, 1, "up", "fwd+1.2", "turn@0.3"),
        facing(1080, 250, 170, 1, 1, "left", "turn@0.35", "turn@0.6"),
        facing(1080, 250, 170, 1, 1, "up", "turn@0.65", "turn@0.8"),
        facing(1080, 250, 170, 1, 1, "right", "turn@0.85", "back"),
        facing(1080, 250, 170, 1, 1, "up", "back+0.3", "end"),
        A("chip", "FORWARD = one square ahead", at="fwd", until="turn", x=1335, y=880, color="sky", size=44),
        A("chip", "TURN = a quarter turn, on the spot", at="turn", until="stand", x=1335, y=880, color="orange",
          size=40),
        A("bigtext", "Stand up and turn right!", at="stand", until="back", x=1335, y=900, size=56, color="green"),
        A("aiden", x=230, y=1080, s=0.5, moods={"start": "happy", "stand": "proud"}, wave=("back", "end")),
    )),
    # 6. a program and an algorithm -----------------------------------------------------------------
    Scene("j1-w01-s06", setting="lavender", beats=(
        B("When we put cards in a row, we make a program.", speaker=NARRATOR, cue="program", pause=0.4),
        B("A program is a list of exact steps, in order.", speaker=NARRATOR, cue="list", pause=0.6),
        B("Planning the steps to get a job done is called an algorithm.", speaker=NARRATOR, cue="algo", pause=0.6),
        B("Let's plan one! The robot starts here, facing the far side.", speaker=NARRATOR, cue="starts", pause=0.5),
        B("The star is two squares ahead, and one square to the right.", speaker=NARRATOR, cue="star", pause=0.6),
        B("Here is our plan: FORWARD, FORWARD, TURN RIGHT, FORWARD.", speaker=NARRATOR, cue="plan", pause=1.0),
    ), actions=(
        A("chip", "program = steps in order", at="program@0.6", until="starts", x=960, y=420, color="orange",
          size=52),
        A("chip", "algorithm = a plan of steps", at="algo@0.6", until="starts", x=960, y=580, color="purple",
          size=52),
        A("grid", x=GX, y=GY, cell=CELL, rows=FLOOR, marks=STAR, at="starts", walker=[("starts", 0, 3)]),
        facing(GX, GY, CELL, 0, 3, "up", "starts@0.6", "end"),
        A("arrow", at="star@0.3", until="plan", x1=GX + 75, y1=GY + 3 * CELL + 20, x2=GX + 75, y2=GY + 1 * CELL + 75,
          color="green", width=8),
        A("arrow", at="star@0.6", until="plan", x1=GX + 75, y1=GY + CELL + 75, x2=GX + CELL + 55, y2=GY + CELL + 75,
          color="green", width=8),
        A("cards", items=PLAN, x=150, y=260, w=500, gap=125, size=42, at="plan",
          reveal=["plan@0.3", "plan@0.45", "plan@0.65", "plan@0.85"]),
        A("aiden", x=230, y=1080, s=0.5, point=("starts", "starts$"), moods={"start": "happy", "algo": "proud"}),
    )),
    # 7. read the cards and walk ---------------------------------------------------------------------
    Scene("j1-w01-s07", setting="sky", beats=(
        B("Now let's read the cards together, one at a time. Say them with me!", speaker=NARRATOR, cue="read",
          pause=0.6),
        B("Forward!", speaker=NARRATOR, cue="c1", pause=1.2),
        B("Forward!", speaker=NARRATOR, cue="c2", pause=1.2),
        B("Turn right!", speaker=NARRATOR, cue="c3", pause=1.2),
        B("Forward!", speaker=NARRATOR, cue="c4", pause=1.4),
        B("The robot is on the star! Our program worked!", speaker=NARRATOR, cue="worked", pause=0.4),
        B("Beep boop! I found the star!", speaker=PIXI, cue="found", pause=0.5),
        B("The robot did the cards one at a time, in order.", speaker=NARRATOR, cue="order", pause=0.8),
    ), actions=(
        A("cards", items=PLAN, x=150, y=260, w=500, gap=125, size=42,
          active=[("c1", "c2"), ("c2", "c3"), ("c3", "c4"), ("c4", "worked")], done=["c2", "c3", "c4", "worked"]),
        A("grid", x=GX, y=GY, cell=CELL, rows=FLOOR, marks=STAR, walker=S7_PATH),
        *S7_ARROWS,
        A("badge", ok=True, at="worked", x=1780, y=240),
        A("confetti", at="worked", x=1400, y=500),
        A("chip", "one at a time, in order", at="order", x=1400, y=960, color="green", size=46),
        A("aiden", x=230, y=1080, s=0.5, moods={"start": "happy", "worked": "proud"}, wave=("worked", "order")),
    )),
    # 8. quick quiz: TURN RIGHT first ---------------------------------------------------------------
    Scene("j1-w01-s08", setting="peach", beats=(
        B("Quick quiz!", speaker=NARRATOR, cue="quiz", pause=0.4),
        B("What if we put TURN RIGHT first? Same cards, new order.", speaker=NARRATOR, cue="what", pause=0.6),
        B("Will the robot still reach the star?", speaker=NARRATOR, cue="will", pause=3.2),
        B("Let's test it!", speaker=NARRATOR, cue="test", pause=5.4),
        B("No! The robot ended up somewhere else.", speaker=NARRATOR, cue="no", pause=0.5),
        B("The same cards in a different order make a different path. The order matters!", speaker=NARRATOR,
          cue="matters", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("cards", items=["TURN RIGHT", "FORWARD", "FORWARD", "FORWARD"], x=150, y=260, w=500, gap=125, size=42,
          at="what", reveal=["what@0.3", "what@0.45", "what@0.6", "what@0.75"],
          active=card_windows([("test", 0.6, ""), ("test", 1.7, ""), ("test", 2.9, ""), ("test", 4.1, "")], "no")),
        A("grid", x=GX, y=GY, cell=CELL, rows=FLOOR, marks=STAR, at="what", walker=S8_PATH),
        *S8_ARROWS,
        A("thought", "Star or no star?", at="will$+0.2", until="test", x=1420, y=960),
        A("badge", ok=False, at="no", x=1780, y=240),
        A("chip", "The order matters!", at="matters@0.5", x=1400, y=960, color="orange", size=48),
        A("aiden", x=230, y=1080, s=0.5, moods={"will": "thinking", "test": "happy", "no": "surprised",
                                               "matters": "happy"}, chin=("will", "test")),
    )),
    # 9. bug hunt: The Wrong Card -------------------------------------------------------------------
    Scene("j1-w01-s09", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=NARRATOR, cue="bug", pause=0.4),
        B("Ada wants the robot to reach the star in the far corner. Here are her cards.", speaker=NARRATOR, cue="ada",
          pause=0.6),
        B("Let's test them.", speaker=NARRATOR, cue="test", pause=6.6),
        B("Beep! Off the grid!", speaker=PIXI, cue="off", pause=0.6),
        B("A bug is a mistake in a program. One card is in the wrong place.", speaker=NARRATOR, cue="mistake",
          pause=0.5),
        B("Which card is in the wrong place?", speaker=NARRATOR, cue="which", pause=3.2),
        B("TURN RIGHT! The robot turned too early. It should come after the second FORWARD.", speaker=NARRATOR,
          cue="tr", pause=0.6),
        B("Let's move that one card, and test again.", speaker=NARRATOR, cue="move", pause=8.6),
        B("The robot reached the star! We found the bug, and we fixed it!", speaker=NARRATOR, cue="fixed", pause=0.4),
        B("Bug fixed! Beep boop!", speaker=PIXI, cue="yay", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Wrong Card", at="bug", color="navy"),
        A("cards", items=ADA, x=150, y=240, w=480, gap=118, size=40, at="ada", until="move+1.15",
          reveal=["ada@0.5", "ada@0.6", "ada@0.7", "ada@0.8", "ada@0.9"],
          active=card_windows(S9_BUG_STEPS, "off") + [],
          reorder=("move+0.4", [0, 2, 1, 3, 4])),
        A("cards", items=ADA_FIXED, x=150, y=240, w=480, gap=118, size=40, at="move+1.15",
          reveal=["move+1.15"] * 5, active=card_windows(S9_FIX_STEPS, "fixed")),
        A("grid", x=AX, y=AY, cell=ACELL, rows=ADA_ROWS, marks=ADA_STAR, at="ada", walker=S9_PATH),
        *S9_ARROWS1,
        *S9_ARROWS2,
        A("badge", ok=False, at="off", until="move", x=1780, y=240),
        A("chip", "A bug is a mistake in a program", at="mistake", until="which", x=1290, y=860, color="yellow",
          size=40),
        A("thought", "Which card?", at="which$+0.2", until="tr", x=1290, y=880),
        A("chip", "TURN RIGHT: too early!", at="tr", until="move", x=1290, y=860, color="red", size=44),
        A("badge", ok=True, at="fixed", x=1780, y=240),
        A("confetti", at="fixed", x=1300, y=450),
        A("chip", "Bug found and fixed!", at="fixed@0.5", x=1290, y=860, color="green", size=46),
    )),
    # 10. robot dance (wiggle break) ------------------------------------------------------------------
    Scene("j1-w01-s10", setting="workshop", beats=(
        B("Robot dance time! Stand up and be a robot.", speaker=NARRATOR, cue="dance", pause=0.4),
        B("Do each card I call out. Ready?", speaker=NARRATOR, cue="ready", pause=0.8),
        B("FORWARD! Stomp!", speaker=NARRATOR, cue="d1", pause=1.2),
        B("TURN LEFT!", speaker=NARRATOR, cue="d2", pause=1.2),
        B("TURN RIGHT!", speaker=NARRATOR, cue="d3", pause=1.2),
        B("FORWARD! Stomp!", speaker=NARRATOR, cue="d4", pause=1.2),
        B("Now power down. Slowly, slowly, all the way to sitting.", speaker=NARRATOR, cue="power", pause=1.6),
        B("Powering down. Beep... boop.", speaker=PIXI, cue="pd", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, wave=[("dance", "dance$"), ("d1", "d1>"), ("d4", "d4>")],
          moods={"start": "happy", "dance": "proud", "power": "happy"}),
        A("pixi", x=640, y=760, moods={"dance": "happy", "pd": "thinking"},
          path=[("d1", 640, 760), ("d1+0.8", 760, 760), ("d4", 760, 760), ("d4+0.8", 880, 760),
                ("power", 880, 760), ("power+1.6", 880, 800)]),
        A("bigtext", "FORWARD!", at="d1", until="d1>", x=1350, y=480, size=90, color="blue"),
        A("bigtext", "TURN LEFT!", at="d2", until="d2>", x=1350, y=480, size=90, color="orange"),
        A("bigtext", "TURN RIGHT!", at="d3", until="d3>", x=1350, y=480, size=90, color="green"),
        A("bigtext", "FORWARD!", at="d4", until="d4>", x=1350, y=480, size=90, color="blue"),
        A("chip", "Power down...", at="power", x=1350, y=480, color="sky", size=52),
    )),
    # 11. recap and next ------------------------------------------------------------------------------
    Scene("j1-w01-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Program!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Algorithm!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Bug!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("A program is exact steps, in order. An algorithm is the plan. A bug is a mistake we can fix.",
          speaker=NARRATOR, cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up. Your grown-up is the robot!", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Play Parent Robot, fix The Wrong Card, then plan your own path to the star.", speaker=NARRATOR, cue="next",
          pause=0.6),
        B("And remember our rules: nicknames only, and ask a grown-up.", speaker=NARRATOR, cue="rules", pause=0.5),
        B("Next week, we meet Scratch. See you then. Happy coding!", speaker=NARRATOR, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Program!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Algorithm!", at="w2", until="w2>", y=560, size=90, color="purple"),
        A("bigtext", "Bug!", at="w3", until="w3>", y=560, size=90, color="red"),
        A("chip", "program = exact steps, in order", at="recap", until="turn", x=1200, y=440, color="orange",
          size=44),
        A("chip", "algorithm = the plan", at="recap@0.45", until="turn", x=1200, y=560, color="purple", size=44),
        A("chip", "bug = a mistake we can fix", at="recap@0.75", until="turn", x=1200, y=680, color="yellow",
          size=44),
        A("banner", "NEXT: Parent Robot", at="turn", color="green"),
        A("cards", items=["Parent Robot", "Fix The Wrong Card", "My Own Path"], x=900, y=280, w=640, gap=120,
          reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("icons", at="rules", x=1220, y=740, gap=340,
          items=[("person", "Nicknames only", "rules@0.3"), ("grownup", "Ask a grown-up", "rules@0.6")]),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
