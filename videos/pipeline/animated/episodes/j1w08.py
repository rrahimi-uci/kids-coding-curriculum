"""Junior Level 1 Week 8: Draw With the Pen (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/1-little-robots/teaching-material/lessons/week08.tex: walking a square on the floor grid
(3 steps, a quarter turn, four times, buttons dropped with pen down), adding the Pen extension, the
crayon on the cat's tail (pen down, pen up, erase all), a quarter turn is 90 and two make a half turn,
Exercise 8.1 Draw a Square built step by step, a quiz on a missing pen down, stamp and the turn card
for Exercise 8.3 (the ring is not built here), Exercise 8.2 The One-Side Square (the turn outside the
repeat), passwords are like a toothbrush, the walk-a-square wiggle break and the greeting card kickoff.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
SIZE = ("looks", "set size to [40] %")
ERASE = ("pen", "erase all")
DOWN = ("pen", "pen down")
UP = ("pen", "pen up")
MOVE = ("motion", "move [100] steps")
TURN = ("motion", "turn ↻ [90] degrees")
BIG = 1.25  # block scale: big enough for young eyes
SMALL_CAT = 0.6  # the lesson sets the cat's size to 40 % so it leaves room to draw

# The floor-grid warm-up: Pixi walks 3 steps and makes a quarter turn, four times, dropping a button
# (a blue cell) on every square it steps on.
_SQUARE = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]


def _rows(visited):
    return ["".join("B" if (c, r) in visited else "." for c in range(4)) for r in range(4)]


WALK_PATH = [(f"walk@{k / 12:.3f}", c, r) for k, (c, r) in enumerate(_SQUARE)]
WALK_STATES = [("start", _rows({(0, 0)}))] + [(f"walk@{k / 12:.3f}", _rows(set(_SQUARE[:k + 1])))
                                              for k in range(1, 13)]

EPISODE = Episode(level="j1", week=8, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w08-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, coders! It's Aiden and Pixi again.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello, artists!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, two sprites took turns to talk.", speaker=AIDEN, cue="last", pause=0.5),
        B("Today, the cat gets a crayon, and it draws a square for us!", speaker=AIDEN, cue="today", pause=0.5),
        B("Are you ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("chip", "two sprites take turns", at="last", until="today", x=1300, y=420, color="orange", size=44),
        A("banner", "MISSION: Make the cat draw a square", at="today"),
        A("stage", x=1000, y=340, w=760, h=520, at="today", flag=False, sprite_scale=SMALL_CAT, sprite_x=-60,
          sprite_y=60, actions=[("today@0.6", "draw", 4, 100, 3.0, -90)]),
    )),
    # 2. warm-up: walk a square ---------------------------------------------------------------------
    Scene("j1-w08-s02", setting="workshop", beats=(
        B("Let's warm up. Pixi is a robot that draws.", speaker=AIDEN, cue="robot", pause=0.4),
        B("Here is the program. Pen down. Then repeat four: three steps, and a quarter turn.", speaker=AIDEN,
          cue="program", pause=0.5),
        B("Pen down means: drop a button on every square you step on.", speaker=AIDEN, cue="pen", pause=0.4),
        B("A quarter turn is like the big hand of a clock, going from twelve to three.", speaker=AIDEN,
          cue="clock", pause=0.5),
        B("Go, Pixi! Three steps, quarter turn. Three steps, quarter turn. Three steps, quarter turn. Three "
          "steps, quarter turn.", speaker=AIDEN, cue="walk", pause=0.8),
        B("What shape did Pixi draw?", speaker=AIDEN, cue="shape", pause=3.0),
        B("A square! And Pixi ended back where it started.", speaker=AIDEN, cue="square", pause=0.6),
    ), actions=(
        A("aiden", x=230, y=1000, s=0.75, moods={"shape": "thinking", "square": "happy"}, chin=("shape", "square"),
          point=("program", "program$")),
        A("cards", items=["PEN DOWN", "REPEAT 4: 3 STEPS", "REPEAT 4: QUARTER TURN"], x=400, y=380, w=700,
          gap=120, reveal=["program@0.15", "program@0.5", "program@0.75"], at="program"),
        A("grid", x=1260, y=380, cell=100, at="robot", states=WALK_STATES, walker=WALK_PATH),
        A("chip", "quarter turn: 12 to 3", at="clock", until="walk", x=760, y=820, color="yellow", size=44),
        A("thought", "What shape?", at="shape$+0.2", until="square", x=760, y=820),
        A("chip", "a square! back home", at="square", x=760, y=820, color="green", size=46),
    )),
    # 3. the pen: a crayon on the cat's tail --------------------------------------------------------
    Scene("j1-w08-s03", setting="sky", beats=(
        B("In Scratch, the crayon is called the pen.", speaker=AIDEN, cue="pen", pause=0.4),
        B("The pen blocks are hiding, so we add them first.", speaker=AIDEN, cue="hiding", pause=0.4),
        B("Click Add Extension, the blue button at the very bottom left. Then click Pen.", speaker=AIDEN,
          cue="ext", pause=0.5),
        B("A green Pen circle appears. We do this once in every new project.", speaker=AIDEN, cue="green",
          pause=0.6),
        B("Imagine a crayon tied to the cat's tail.", speaker=AIDEN, cue="tail", pause=0.4),
        B("Pen down puts the crayon on the paper, so the cat draws when it walks.", speaker=AIDEN, cue="down",
          pause=1.2),
        B("Pen up lifts it off, so the cat walks without drawing.", speaker=AIDEN, cue="up", pause=1.2),
        B("And erase all is a big eraser that cleans the whole stage.", speaker=AIDEN, cue="erase", pause=1.0),
    ), actions=(
        A("cards", items=["Add Extension", "Pen"], x=160, y=280, w=620, gap=130, reveal=["ext@0.1", "ext@0.6"],
          at="ext", until="tail", color="sky"),
        A("chip", "Pen: green, in every new project", at="green", until="tail", x=470, y=620, color="green",
          size=40),
        A("stage", x=1000, y=260, w=760, h=520, at="pen", flag=False, sprite_scale=SMALL_CAT, sprite_x=-180,
          actions=[("down@0.5", "draw", 1, 150, 1.6), ("up@0.5", "move", 150, 1.6), ("erase@0.6", "clear"),
                   ("erase@0.7", "goto", -180, 0, 0.8)]),
        A("scratch", blocks=[DOWN], x=260, y=360, w=560, h=150, panel=False, scale=BIG, at="down",
          until="down>"),
        A("scratch", blocks=[UP], x=260, y=360, w=560, h=150, panel=False, scale=BIG, at="up", until="up>"),
        A("scratch", blocks=[ERASE], x=260, y=360, w=560, h=150, panel=False, scale=BIG, at="erase"),
        A("chip", "pen down = draw", at="down", until="end", x=500, y=620, color="green", size=46),
        A("chip", "pen up = stop drawing", at="up", until="end", x=500, y=740, color="sky", size=44),
        A("chip", "erase all = big eraser", at="erase", until="end", x=500, y=860, color="yellow", size=44),
    )),
    # 4. a quarter turn is 90 ------------------------------------------------------------------------
    Scene("j1-w08-s04", setting="lavender", beats=(
        B("To draw a square, the cat must turn.", speaker=AIDEN, cue="turn", pause=0.4),
        B("In Scratch, a quarter turn is ninety.", speaker=AIDEN, cue="ninety", pause=0.6),
        B("Two quarter turns make a half turn. That is one hundred eighty.", speaker=AIDEN, cue="half", pause=0.6),
        B("Let's do it! Stand up. Make a quarter turn with me. Ninety!", speaker=AIDEN, cue="stand", pause=1.4),
        B("One more quarter turn. Ninety! Now we made a half turn.", speaker=AIDEN, cue="more", pause=1.2),
        B("Say it with me: a quarter turn is ninety!", speaker=AIDEN, cue="sayit", pause=1.6),
        B("Ninety, ninety, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=980, s=0.8, wave=[("stand", "stand$"), ("more", "more$")], moods={"stand": "proud"},
          look={"start": 0.2, "stand@0.6": 1.0, "more@0.4": -1.0, "sayit": 0.2}),
        A("pixi", x=620, y=800, s=0.65, ground=980, beep="pixi"),
        A("stage", x=1000, y=230, w=760, h=520, at="turn", flag=False, sprite_scale=SMALL_CAT, sprite_x=-120,
          sprite_y=60, actions=[("ninety@0.3", "draw", 2, 120, 2.0, -90)]),
        A("chip", "quarter turn = 90", at="ninety", until="sayit", x=1380, y=860, color="orange", size=48),
        A("chip", "half turn = 180", at="half", until="sayit", x=1380, y=970, color="purple", size=44),
        A("bigtext", "a quarter turn is 90!", at="sayit", until="end", x=1380, y=970, size=56, color="orange"),
    )),
    # 5. Draw a Square: the start of the script ------------------------------------------------------
    Scene("j1-w08-s05", setting="mint", beats=(
        B("Let's build Draw a Square together.", speaker=AIDEN, cue="build", pause=0.4),
        B("From the yellow Events circle: when green flag clicked.", speaker=AIDEN, cue="events", pause=0.6),
        B("From the purple Looks circle: set size to one hundred percent. Change it to forty. A small cat "
          "leaves room to draw.", speaker=AIDEN, cue="looks", pause=0.8),
        B("From the green Pen circle: erase all, then pen down.", speaker=AIDEN, cue="pen", pause=0.8),
        B("Now the crayon is on the paper!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("banner", "Exercise 8.1: Draw a Square", at="build", color="green"),
        A("scratch", "Draw a Square", blocks=[FLAG, ("looks", "set size to [100] %"), ERASE, DOWN], x=180, y=280,
          w=900, h=560, scale=BIG, reveal=["events", "looks", "pen@0.2", "pen@0.6"],
          edits=[("looks@0.45", 1, "set size to [40] %")]),
        A("chip", "Events: yellow", at="events", until="events>", x=1480, y=420, color="yellow", size=44),
        A("chip", "Looks: purple", at="looks", until="looks>", x=1480, y=420, color="purple", size=44),
        A("chip", "Pen: green", at="pen", x=1480, y=420, color="green", size=44),
        A("pixi", x=1480, y=820, s=0.6, at="pixi", ground=920),
    )),
    # 6. Draw a Square: the repeat, and the flag ----------------------------------------------------
    Scene("j1-w08-s06", setting="mint", beats=(
        B("From the orange Control circle: repeat ten. Change ten to four.", speaker=AIDEN, cue="repeat",
          pause=0.6),
        B("From the blue Motion circle: put move ten steps inside the repeat. Change it to one hundred.",
          speaker=AIDEN, cue="move", pause=0.6),
        B("Then turn fifteen degrees, the arrow that goes like a clock. Put it inside, under the move. Change "
          "it to ninety.", speaker=AIDEN, cue="turn", pause=0.6),
        B("Last, pen up, under the repeat.", speaker=AIDEN, cue="up", pause=0.5),
        B("How many sides will the cat draw?", speaker=AIDEN, cue="predict", pause=3.0),
        B("Let's click the green flag and count!", speaker=AIDEN, cue="flag", pause=0.2),
        B("One, two, three, four!", speaker=AIDEN, cue="count", pause=0.6),
        B("A square! And the cat came home.", speaker=AIDEN, cue="home", pause=0.4),
        B("Beep! Beautiful!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Draw a Square", blocks=[FLAG, SIZE, ERASE, DOWN,
                                              ("control", "repeat [10]", [("motion", "move [10] steps"),
                                                                          ("motion", "turn ↻ [15] degrees")]),
                                              UP],
          x=140, y=230, w=860, h=800, scale=1.0, reveal=["start", "start", "start", "start", "repeat", "move",
                                                          "turn", "up"],
          edits=[("repeat@0.6", 4, "repeat [4]"), ("move@0.75", 5, "move [100] steps"),
                 ("turn@0.85", 6, "turn ↻ [90] degrees")],
          highlight=[(4, "predict", "predict$+3.0"), (5, "count", "home"), (6, "count", "home")]),
        A("chip", "Control: orange", at="repeat", until="move", x=1440, y=880, color="orange", size=44),
        A("chip", "Motion: blue", at="move", until="up", x=1440, y=880, color="sky", size=44),
        A("chip", "Pen: green", at="up", until="predict", x=1440, y=880, color="green", size=44),
        A("stage", x=1080, y=200, w=760, h=520, at="repeat", flag_at="flag@0.5", sprite_scale=SMALL_CAT,
          sprite_x=-60, sprite_y=60, actions=[("count", "draw", 4, 100, 3.6, -90)]),
        A("thought", "How many sides?", at="predict$+0.2", until="flag", x=1440, y=880),
        A("chip", "4 sides: a square!", at="home", x=1440, y=880, color="green", size=46),
        A("badge", ok=True, at="home", x=1760, y=260),
        A("confetti", at="home", x=1460, y=460),
    )),
    # 7. quick quiz: no line ------------------------------------------------------------------------
    Scene("j1-w08-s07", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("Leo's cat walks, but no line appears. Which block is missing?", speaker=AIDEN, cue="which", pause=3.2),
        B("Pen down! Without pen down, the crayon never touches the paper.", speaker=AIDEN, cue="answer",
          pause=0.6),
        B("Pen down goes before the repeat.", speaker=AIDEN, cue="before", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Leo's script", blocks=[FLAG, ERASE, ("control", "repeat [4]", [MOVE, TURN])], x=180, y=280,
          w=880, h=560, scale=BIG, at="which", until="answer@0.5"),
        A("scratch", "Leo's script (fixed)", blocks=[FLAG, ERASE, DOWN, ("control", "repeat [4]", [MOVE, TURN])],
          x=180, y=280, w=880, h=640, scale=1.0, at="answer@0.5", highlight=[(2, "answer@0.5", "end")]),
        A("stage", x=1180, y=260, w=640, h=440, at="which", flag_at="which@0.3", flag=True, sprite_scale=0.45,
          sprite_x=-80, sprite_y=60,
          actions=[("which@0.4", "move", 100, 0.8), ("which@0.4+0.9", "turn", 90, 0.1),
                   ("which@0.4+1.0", "move", 100, 0.8), ("answer", "goto", -80, 60, 0.6),
                   ("before", "draw", 4, 100, 3.0, -90)]),
        A("thought", "Which block?", at="which$+0.2", until="answer", x=1500, y=860),
        A("chip", "pen down: before the repeat", at="before", x=1500, y=860, color="green", size=40),
    )),
    # 8. stamp and the turn card ---------------------------------------------------------------------
    Scene("j1-w08-s08", setting="lavender", beats=(
        B("Here is one more pen block: stamp.", speaker=AIDEN, cue="stamp", pause=0.4),
        B("Stamp leaves a picture of the cat on the stage, like a rubber stamp.", speaker=AIDEN, cue="rubber",
          pause=0.6),
        B("Click stamp, and the cat walks away. The picture stays!", speaker=AIDEN, cue="walk", pause=1.2),
        B("In Stamp a Ring, you make a ring of six cats.", speaker=AIDEN, cue="ring", pause=0.4),
        B("The turn comes from the turn card. Square: ninety. Triangle: one hundred twenty. Six sides: sixty.",
          speaker=AIDEN, cue="card", pause=0.6),
        B("We read the number off the card. That's all!", speaker=AIDEN, cue="read", pause=0.8),
    ), actions=(
        A("scratch", blocks=[("pen", "stamp")], x=220, y=330, w=500, h=150, panel=False, scale=BIG, at="stamp",
          highlight=[(0, "walk", "walk+0.6")]),
        A("stage", x=980, y=240, w=800, h=520, at="stamp", flag=False, sprite_scale=SMALL_CAT, sprite_x=-120,
          actions=[("walk+0.6", "move", 180, 1.2)]),
        A("cat", x=1180 - 3, y=500 + 50 + 0, s=SMALL_CAT, at="walk+0.5", until="ring"),
        A("chip", "stamp = a picture that stays", at="rubber", until="ring", x=470, y=640, color="green", size=40),
        A("banner", "Exercise 8.3: Stamp a Ring", at="ring", color="purple"),
        A("panel", "Turn card", x=200, y=560, w=620, size=40, at="card",
          items=[("card@0.2", "Square: 90"), ("card@0.45", "Triangle: 120"), ("card@0.75", "Six sides: 60")]),
        A("chip", "read it off the card!", at="read", x=1380, y=880, color="yellow", size=44),
    )),
    # 9. bug hunt: the One-Side Square ---------------------------------------------------------------
    Scene("j1-w08-s09", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.5),
        B("Omar wants a square. Watch what his cat draws.", speaker=AIDEN, cue="omar", pause=4.4),
        B("One long line! How many times did the cat turn?", speaker=AIDEN, cue="how", pause=3.0),
        B("Only once, at the end.", speaker=AIDEN, cue="once", pause=0.5),
        B("Look closely. The turn is under the repeat, not inside it.", speaker=AIDEN, cue="look", pause=0.5),
        B("Like in our warm-up, when the quarter turn card was outside the repeat card.", speaker=AIDEN,
          cue="warm", pause=0.5),
        B("Let's drag the turn up, inside the repeat, under the move.", speaker=AIDEN, cue="fix", pause=0.8),
        B("Test it again.", speaker=AIDEN, cue="test", pause=4.2),
        B("Four sides! We fixed the bug!", speaker=AIDEN, cue="fixed", pause=0.4),
        B("Square-tastic!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The One-Side Square", at="bug", color="navy"),
        A("scratch", "Omar's script", blocks=[FLAG, ERASE, DOWN, ("control", "repeat [4]", [MOVE]), TURN],
          x=140, y=260, w=860, h=720, scale=BIG, at="omar", until="fix+0.4", highlight=[(5, "look", "fix")]),
        A("scratch", "Omar's script (fixed)", blocks=[FLAG, ERASE, DOWN, ("control", "repeat [4]", [MOVE, TURN])],
          x=140, y=260, w=860, h=720, scale=BIG, at="fix+0.4", highlight=[(5, "fix+0.4", "fix+1.6")]),
        A("sfx", "snap", at="fix+0.4"),
        A("stage", x=1080, y=240, w=740, h=500, at="omar", flag_at="omar@0.6", sprite_scale=0.45,
          sprite_x=-190, sprite_y=60,
          actions=[("omar$", "draw", 4, 95, 3.2, 0), ("omar$+3.4", "turn", -90, 0.4),
                   ("test", "clear"), ("test", "goto", -60, 60, 0.4), ("test+0.6", "draw", 4, 100, 3.2, -90)]),
        A("badge", ok=False, at="how", until="test", x=1760, y=300),
        A("thought", "How many turns?", at="how$+0.2", until="once", x=1450, y=870),
        A("chip", "turned once", at="once", until="look", x=1450, y=870, color="red", size=46),
        A("chip", "turn: inside the repeat", at="look", until="fixed", x=1450, y=870, color="orange", size=42),
        A("badge", ok=True, at="fixed", x=1760, y=300),
        A("chip", "4 sides!", at="fixed", x=1450, y=870, color="green", size=48),
        A("confetti", at="fixed", x=1450, y=480),
    )),
    # 10. passwords are like a toothbrush -----------------------------------------------------------
    Scene("j1-w08-s10", setting="workshop", beats=(
        B("Some apps and games use a password. A password is a secret word that keeps your things safe.",
          speaker=AIDEN, cue="password", pause=0.5),
        B("A password is like your toothbrush. You use it, but you never share it, not even with your best "
          "friend.", speaker=AIDEN, cue="tooth", pause=0.6),
        B("Only the grown-ups who look after you may know it.", speaker=AIDEN, cue="grown", pause=0.6),
        B("Your friend says: Tell me your password, I won't tell. What do you do?", speaker=AIDEN, cue="friend",
          pause=3.0),
        B("Say no, and tell a grown-up!", speaker=AIDEN, cue="no", pause=0.5),
        B("Our Scratch app has no password and no account, and that is on purpose.", speaker=AIDEN,
          cue="scratch", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"friend": "thinking", "no": "proud"}, chin=("friend", "no")),
        A("pixi", x=600, y=760, moods={"no": "happy"}),
        A("banner", "Passwords are like a toothbrush", at="password", color="green"),
        A("icons", at="password", until="end", x=1260, y=540, gap=280,
          items=[("lock", "Secret", "password@0.5"), ("person", "Not your best friend", "tooth@0.6"),
                 ("grownup", "Only your grown-ups", "grown")], crossed=[1]),
        A("thought", "What do you do?", at="friend$+0.2", until="no", x=1260, y=840),
        A("chip", "Say no. Tell a grown-up!", at="no", x=1260, y=820, color="red", size=46),
        A("chip", "Scratch here: no password, no account", at="scratch", x=1260, y=930, color="sky", size=36),
    )),
    # 11. wiggle break: walk a square ---------------------------------------------------------------
    Scene("j1-w08-s11", setting="workshop", beats=(
        B("Wiggle break! Stand up and walk a square around the room.", speaker=AIDEN, cue="stand", pause=0.5),
        B("Pen down! Draw in the air with one finger as you go.", speaker=AIDEN, cue="finger", pause=0.6),
        B("Four steps, quarter turn. Four steps, quarter turn. Four steps, quarter turn. Four steps, quarter "
          "turn.", speaker=AIDEN, cue="walk", pause=1.2),
        B("You are back home! Beep beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("finger", "walk$")], moods={"start": "happy", "walk": "proud"}),
        A("pixi", x=600, y=760, beep="pixi"),
        A("bigtext", "Walk a square!", at="stand", x=1410, y=420, size=80, color="green"),
        A("stage", x=1060, y=530, w=700, h=440, at="finger", flag=False, sprite="pixi", sprite_scale=0.7,
          sprite_x=-60, sprite_y=60, actions=[("walk", "draw", 4, 100, 7.0, -90)]),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j1-w08-s12", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Pen down!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Quarter turn!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Stamp!", speaker=AIDEN, cue="w3", pause=1.2),
        B("A square is repeat four of move and a quarter turn. Both go inside the repeat.", speaker=AIDEN,
          cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Draw a Square, fix the One-Side Square, then Stamp a Ring.", speaker=AIDEN, cue="next", pause=0.6),
        B("And in two weeks, we have a showcase! You will make a greeting card for someone special. Who could "
          "it be for?", speaker=AIDEN, cue="card", pause=3.0),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud", "card": "thinking",
                                                                         "bye": "happy"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Pen down!", at="w1", until="w1>", y=560, size=90, color="green"),
        A("bigtext", "Quarter turn!", at="w2", until="w2>", y=560, size=90, color="orange"),
        A("bigtext", "Stamp!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("chip", "square = repeat 4: move + quarter turn", at="recap", until="turn", x=1200, y=560,
          color="orange", size=40),
        A("banner", "NEXT: Draw with the pen", at="turn", color="green"),
        A("cards", items=["Draw a Square", "Fix the One-Side Square", "Stamp a Ring"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.45", "next@0.8"], at="next", until="card"),
        A("icons", at="card", until="bye", x=1300, y=420, gap=280,
          items=[("heart", "Someone special", "card@0.5"), ("star", "A greeting card", "card@0.3")]),
        A("thought", "Who is it for?", at="card$+0.2", until="bye", x=1300, y=760),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
