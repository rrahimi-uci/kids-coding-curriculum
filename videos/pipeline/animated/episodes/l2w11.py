"""Level 2 Week 11: Project Studio 2: Test and Polish (kit episode)."""

from ..kit_dsl import A, B, Episode, PIXI, Scene

GAME_FRAME = '''import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
for x, y in [(-120, 150), (150, 180)]:
    pen.goto(x, y)
    pen.dot(40, "orange")
pen.color("gray")
for x, y in [(30, 90), (-60, -10)]:
    pen.goto(x - 18, y - 18)
    pen.begin_fill()
    for corner in [(x + 18, y - 18), (x + 18, y + 18), (x - 18, y + 18)]:
        pen.goto(corner)
    pen.end_fill()
pen.goto(-20, -190)
pen.color("blue")
pen.begin_fill()
for corner in [(20, -190), (0, -140)]:
    pen.goto(corner)
pen.end_fill()'''

RECIPE = '''def load_high_score(filename):
    try:
        with open(filename) as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

def save_high_score(filename, score):
    with open(filename, "w") as f:
        f.write(str(score))

print(load_high_score("highscore.txt"))'''

TESTS_1 = '''from mygame import load_high_score, next_x, save_high_score

def test_moves_right_normally():
    assert next_x(0, 1) == 20

def test_stops_at_the_right_edge():
    assert next_x(280, 1) == 280'''

TESTS_2 = '''def test_high_score_round_trip():
    save_high_score("test_scores.txt", 42)
    assert load_high_score("test_scores.txt") == 42

def test_no_file_means_zero():
    assert load_high_score("no_such_file.txt") == 0

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])'''

NEXT_X = '''def next_x(x, direction):
    new_x = x + direction * SETTINGS["step"]
    return clamp(new_x, SETTINGS["left_edge"],
                 SETTINGS["right_edge"])'''

NEXT_X_BROKEN = '''def next_x(x, direction):
    new_x = x + direction * SETTINGS["step"]
    return new_x'''

NAMES = ["test_moves_right_normally", "test_stops_at_the_right_edge", "test_high_score_round_trip",
         "test_no_file_means_zero"]

PALETTE = '''import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
colors = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
          "#0072B2", "#D55E00", "#CC79A7"]
for i, color in enumerate(colors):
    pen.goto(-180 + i * 60, 0)
    pen.dot(50, color)'''

SHAPES = '''import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-80, 0)
pen.dot(90, "#E69F00")
pen.goto(40, -45)
pen.color("#E69F00")
pen.begin_fill()
for corner in [(130, -45), (130, 45), (40, 45)]:
    pen.goto(corner)
pen.end_fill()
pen.goto(-80, -120)
pen.write("comet", align="center")
pen.goto(85, -120)
pen.write("rock", align="center")'''

ROAD = ["M1 Pitch + plan", "M2 Core loop", "M3 Data + tests", "M4 Polish", "Showcase"]

EPISODE = Episode(level=2, week=11, scenes=(
    Scene("l2-w11-s01", setting="workshop", lead_in=0.2, beats=(
        B("Hi, coders!", cue="hi", pause=0.3),
        B("Next week is the Family Arcade, and Comet Catch works!", cue="works", pause=0.3),
        B("Well, it works when Rose plays it.", cue="rose", pause=0.4),
        B("Pixi tries it for the very first time, presses space twice, and red text appears.", cue="red",
          pause=0.5),
        B("‘Also, I didn't know which keys to press,’", speaker=PIXI, cue="keys", pause=0.1),
        B("says Pixi.", cue="says", pause=0.3),
        B("Uh-oh.", cue="uhoh", pause=0.4),
        B("How can we prove our game works, and make it fun for everyone?", cue="how", pause=2.4),
    ), actions=(
        A("rose", x=300, y=960, enter="left", wave="hi",
          moods={"works": "proud", "red": "surprised", "uhoh": "thinking"}, chin=("how", "end")),
        A("pixi", x=650, y=760, drop=True, moods={"red": "surprised", "keys": "confused", "how": "thinking"},
          beep=("red@0.4", "red@0.7")),
        A("chip", "Family Arcade: next week", at="works", until="how", x=1000, y=300, color="purple", size=40),
        A("turtle", code=GAME_FRAME, title="Comet Catch", at="works@0.4", x=1180, y=400, w=620, h=500, world=230,
          duration=0.01, cursor=False),
        A("chip", "space", at="red@0.4", until="red@0.55", x=1490, y=960, color="navy", size=44),
        A("chip", "space", at="red@0.6", until="red@0.75", x=1490, y=960, color="navy", size=44),
        A("chip", "red text in the Shell!", at="red@0.8", until="how", x=1490, y=960, color="red", size=40),
        A("badge", ok=False, at="red@0.8", until="how", x=1760, y=440),
        A("thought", "Which keys?", at="keys", until="how", x=880, y=520),
        A("banner", "STUDIO MISSION: Test, playtest, polish", at="how"),
        A("chip", "Works for Rose… works for everyone?", at="how@0.4", x=1000, y=260, color="yellow", size=42),
        A("thought", "", at="how$+0.3", until="end", x=640, y=440),
    )),
    Scene("l2-w11-s02", setting="sky", beats=(
        B("Here's the big idea: test the brain, playtest the fun.", cue="idea", pause=0.4),
        B("Your program has two kinds of functions.", cue="two", pause=0.2),
        B("Logic functions are the brain.", cue="logic", pause=0.2),
        B("They take values in and give an answer back with return, so pytest can check them.", cue="return",
          pause=0.3),
        B("Drawing functions are the paint.", cue="paint", pause=0.2),
        B("A computer can't tell if your comet looks nice, but a person can.", cue="person", pause=0.4),
        B("Two tricks.", cue="tricks", pause=0.2),
        B("One: keep the start-up code under the main guard, so pytest can borrow your functions without starting "
          "the game.", cue="guard", pause=0.4),
        B("Two: give file functions the file name as a parameter.", cue="param", pause=0.2),
        B("The game uses highscore.txt.", cue="game", pause=0.2),
        B("The tests use test_scores.txt, so tests never wipe your real score.", cue="tests", pause=0.6),
    ), actions=(
        A("bigtext", "test the brain • playtest the fun", at="idea", until="tricks", y=150, size=50, color="navy"),
        A("panel", "Logic = brain → pytest", at="logic", until="tricks", x=110, y=280, w=800,
          items=[("logic@0.3", "next_x"), ("logic@0.6", "touching"), ("return", "load_high_score")]),
        A("tests", "pytest", at="return@0.5", until="tricks", x=110, y=640, w=800,
          items=[("return@0.6", "test_next_x", True), ("return@0.8", "test_touching", True)]),
        A("panel", "Drawing = paint → playtesters", at="paint", until="tricks", x=1010, y=280, w=800,
          items=[("paint@0.3", "draw_star"), ("paint@0.6", "show_score")]),
        A("icons", at="person", until="tricks", x=1410, y=720, items=[("person", "a playtester", "person@0.5")]),
        A("code", code='if __name__ == "__main__":\n    screen = turtle.Screen()\n    game_loop()', title="mygame.py",
          at="guard", until="param", x=110, y=280, w=920, h=280, shell=False, highlight=[(1, "guard@0.2", "param")]),
        A("chip", "Start-up code under the main guard", at="guard@0.3", until="param", x=570, y=660, color="sky",
          size=42),
        A("icons", at="guard@0.5", until="param", x=1450, y=400, items=[("lock", "the game waits here")]),
        A("chip", "pytest borrows the functions", at="guard@0.7", until="param", x=1450, y=660, color="green",
          size=38),
        A("code", code="def load_high_score(filename):\n    ...", title="mygame.py", at="param", x=110, y=250,
          w=920, h=220, shell=False, highlight=[(1, "param@0.4", "game")]),
        A("chip", "the file name is a parameter", at="param@0.5", x=1440, y=360, color="orange", size=38),
        A("icons", at="game", x=760, y=650, gap=440,
          items=[("game", "highscore.txt", "game"), ("check", "test_scores.txt", "tests")]),
        A("chip", "Tests use test_scores.txt", at="tests@0.4", x=760, y=900, color="green", size=44),
        A("chip", "your real score is safe", at="tests@0.7", x=1500, y=650, color="white", size=38),
    )),
    Scene("l2-w11-s03", setting="lavender", beats=(
        B("Watch Rose add a file and tests.", cue="watch", pause=0.2),
        B("First, two recipe functions from the workbook: load high score and save high score.", cue="recipe",
          pause=0.3),
        B("No file yet? Then the high score is zero, not a crash.", cue="nofile", pause=0.5),
        B("Next, a new file in the same folder: test_mygame.py.", cue="newfile", pause=0.2),
        B("A normal case: next x with zero and one should give twenty.", cue="normal", pause=0.2),
        B("An edge case: next x with two hundred eighty and one should stay at two hundred eighty.", cue="edge"),
        B("The player stays on screen.", cue="stays", pause=0.3),
        B("A round trip: save forty-two in the test file, then load it and expect forty-two.", cue="round",
          pause=0.2),
        B("And a missing file gives zero.", cue="missing", pause=0.3),
        B("Press F5.", cue="f5", pause=0.3),
        B("Four PASSED lines!", cue="four", pause=0.6),
        B("Now Rose breaks next x on purpose, removing the clamp.", cue="breaks", pause=0.4),
        B("FAILED: it got three hundred, not two hundred eighty.", cue="failed", pause=0.3),
        B("The test caught it!", cue="caught", pause=0.3),
        B("Undo, run again: all PASSED.", cue="undo", pause=0.8),
    ), actions=(
        A("code", code=RECIPE, title="mygame.py", x=50, y=150, w=1120, h=860, size=28, at="watch", until="newfile",
          reveal=["recipe", "recipe", "recipe", "recipe", "recipe", "recipe", "recipe@0.6", "recipe@0.6",
                  "recipe@0.6", "recipe@0.6", "nofile", "nofile"],
          highlight=[(5, "nofile", "newfile"), (6, "nofile", "newfile")], run="nofile@0.5", expect=["0"]),
        A("chip", "No file yet → 0, not a crash", at="nofile@0.4", until="newfile", x=1530, y=560, color="green",
          size=38),
        A("code", code=TESTS_1, title="test_mygame.py", x=50, y=150, w=1120, h=420, size=27, shell=False,
          at="newfile", until="round", reveal=["newfile", "normal", "normal", "normal", "edge", "edge", "edge"],
          highlight=[(4, "normal@0.3", "edge"), (7, "edge@0.3", "round")]),
        A("chip", "next_x(0, 1) → 20", at="normal@0.5", until="round", x=1530, y=260, color="sky", size=40),
        A("chip", "assert next_x(280, 1) == 280", at="edge@0.4", until="round", x=1530, y=400, color="orange",
          size=34),
        A("chip", "stays on screen", at="stays", until="round", x=1530, y=530, color="green", size=40),
        A("code", code=TESTS_2, title="test_mygame.py", x=50, y=140, w=1120, h=495, size=27, shell=False,
          at="round", until="breaks", reveal=["round", "round@0.3", "round@0.6", "missing", "missing", "missing",
                                             "f5", "f5", "f5", "f5"],
          highlight=[(3, "round@0.6", "missing"), (6, "missing@0.3", "f5")]),
        A("file", "test_scores.txt", at="round@0.3", until="breaks", x=1300, y=160, w=500, h=220,
          lines=["42"]),
        A("chip", "Round trip: save 42, load 42", at="round@0.6", until="breaks", x=1550, y=460, color="sky",
          size=36),
        A("chip", "missing file → 0", at="missing@0.4", until="breaks", x=1550, y=570, color="green", size=38),
        A("tests", "pytest", at="f5+0.3", until="breaks", x=50, y=650, w=1120,
          items=[(f"f5+{0.5 + 0.3 * i:.1f}", name, True) for i, name in enumerate(NAMES)]),
        A("chip", "4 passed", at="four@0.5", until="breaks", x=1520, y=820, color="green", size=48),
        # break it on purpose
        A("code", code=NEXT_X, title="mygame.py", x=50, y=150, w=1120, h=300, size=30, shell=False, at="breaks",
          until="breaks@0.6"),
        A("code", code=NEXT_X_BROKEN, title="mygame.py", x=50, y=150, w=1120, h=300, size=30, shell=False,
          at="breaks@0.6", until="undo", highlight=[(3, "breaks@0.6", "caught$")]),
        A("chip", "Break it on purpose → FAILED", at="breaks@0.7", until="undo", x=1520, y=230, color="red", size=36),
        A("tests", "pytest", at="failed", until="undo", x=50, y=490, w=1120,
          items=[("failed", NAMES[0], True), ("failed", NAMES[1], False), ("failed", NAMES[2], True),
                 ("failed", NAMES[3], True)]),
        A("terminal", title="pytest", at="failed+0.4", until="undo", x=1220, y=330, w=640, h=210, size=24,
          lines=[("failed+0.4", "E       assert 300 == 280", "out"),
                 ("failed+0.6", "E        +  where 300 = next_x(280, 1)", "out")]),
        A("chip", "The test caught it!", at="caught", until="undo", x=1540, y=640, color="yellow", size=40),
        A("badge", ok=False, at="failed+0.5", until="undo", x=1540, y=760),
        A("code", code=NEXT_X, title="mygame.py", x=50, y=150, w=1120, h=300, size=30, shell=False, at="undo",
          highlight=[(3, "undo", "undo$"), (4, "undo", "undo$")]),
        A("tests", "pytest", at="undo+0.5", x=50, y=490, w=1120,
          items=[(f"undo+{0.7 + 0.25 * i:.2f}", name, True) for i, name in enumerate(NAMES)]),
        A("chip", "Undo → all PASSED", at="undo@0.6", x=1520, y=420, color="green", size=42),
        A("badge", ok=True, at="undo$+0.3", x=1520, y=560),
    )),
    Scene("l2-w11-s04", setting="mint", beats=(
        B("Now the playtest swap.", cue="swap", pause=0.2),
        B("Teams play each other's project for four minutes and fill in feedback cards:", cue="cards", pause=0.2),
        B("I liked.", cue="liked", pause=0.2),
        B("I was confused when.", cue="confused", pause=0.2),
        B("A bug I saw: what I did, what happened, what I expected.", cue="bug", pause=0.2),
        B("One idea.", cue="idea", pause=0.4),
        B("Pixi's cards for Comet Catch say:", cue="pcards", pause=0.1),
        B("‘I pressed space twice and it crashed.’", speaker=PIXI, cue="c1", pause=0.2),
        B("‘I didn't know which keys to use.’", speaker=PIXI, cue="c2", pause=0.2),
        B("‘Add a rainbow comet!’", speaker=PIXI, cue="c3", pause=0.4),
        B("Rose turns the cards into a bug list.", cue="list", pause=0.2),
        B("MUST means it crashes or you can't play.", cue="must", pause=0.2),
        B("SHOULD means it's confusing.", cue="should", pause=0.2),
        B("COULD is a nice idea.", cue="could", pause=0.3),
        B("Pause and point: which gets fixed first?", cue="pause", pause=3.0),
        B("Yes, the crash!", cue="crash", pause=0.3),
        B("Rose reads the traceback and finds the line.", cue="reads", pause=0.3),
        B("If a bug lives in a logic function, write a test that shows it first.", cue="logic", pause=0.2),
        B("It fails.", cue="fails", pause=0.2),
        B("Fix the code.", cue="fix", pause=0.2),
        B("It passes.", cue="passes", pause=0.3),
        B("Now that test guards the bug forever.", cue="guards", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="swap", color="navy"),
        A("icons", at="swap", until="cards@0.5", x=960, y=450, items=[("clock", "4 minutes each", "swap")]),
        A("panel", "Feedback card", at="cards@0.5", until="list", x=90, y=220, w=900, size=34,
          items=[("liked", "I liked …"), ("confused", "I was confused when …"),
                 ("bug", "A bug I saw: did / happened / expected"), ("idea", "One idea …")]),
        A("chip", "I liked • Confused when • Bug • Idea", at="idea", until="list", x=540, y=680, color="yellow",
          size=36),
        A("chip", "What I did / happened / expected", at="bug@0.4", until="list", x=540, y=800, color="sky",
          size=36),
        A("pixi", x=1500, y=860, s=0.6, ground=990, at="pcards", until="list", moods={"c1": "confused",
                                                                                     "c3": "happy"}),
        A("cards", at="c1", until="list", x=1060, y=240, w=800, gap=105, size=32,
          items=["I pressed space twice and it crashed.", "I didn't know which keys to use.", "Add a rainbow comet!"],
          reveal=["c1", "c2", "c3"]),
        # the bug list
        A("table", at="list", x=110, y=230, col_w=425,
          header=["What I did", "What happened", "What I expected", "List"],
          rows=[["space twice", "it crashed", "keep playing", "MUST"],
                ["looked for keys", "no idea", "keys on screen", "SHOULD"],
                ["(an idea)", "", "rainbow comet", "COULD"]],
          reveal=["must", "should", "could"], highlight=[("crash", "end", 0)]),
        A("chip", "MUST → SHOULD → COULD", at="could@0.5", until="reads", x=960, y=640, color="orange", size=46),
        A("thought", "Which first?", at="pause+0.3", until="pause>", x=960, y=820),
        A("badge", ok=True, at="crash", until="reads", x=1460, y=640),
        A("chip", "traceback → the line number", at="reads", until="logic", x=960, y=640, color="red", size=40),
        A("chip", "Bug in logic? Test first, then fix", at="logic", x=960, y=640, color="green", size=44),
        A("tests", "pytest", at="fails", until="passes", x=480, y=740, w=960,
          items=[("fails", "test_shows_the_bug", False)]),
        A("tests", "pytest", at="passes", x=480, y=740, w=960, items=[("passes", "test_shows_the_bug", True)]),
        A("chip", "fix the code", at="fix", until="passes", x=1660, y=800, color="white", size=38),
        A("icons", at="guards", x=1680, y=800, items=[("lock", "guards it", "guards")]),
    )),
    Scene("l2-w11-s05", setting="workshop", tail=0.8, beats=(
        B("Great testing!", cue="great", pause=0.3),
        B("Let's remember.", cue="remember", pause=0.2),
        B("pytest checks the brain, and playtesters check the fun.", cue="brain", pause=0.3),
        B("Test normal cases and edge cases, and give your tests their own file name.", cue="files", pause=0.4),
        B("Now polish, so everyone can play.", cue="polish", pause=0.2),
        B("Use the color-blind-safe palette.", cue="palette", pause=0.2),
        B("Make good and bad things differ in shape or size, not color alone.", cue="shape", pause=0.3),
        B("Use text size sixteen or bigger, explain the keys on screen, and never flash more than three times a "
          "second.", cue="text", pause=0.3),
        B("Start gently, with a slow first level.", cue="gentle", pause=0.4),
        B("Your turn: reach M3.", cue="turn", pause=0.2),
        B("Add your list, dictionary and file, and write three tests until they all say PASSED.", cue="m3",
          pause=0.3),
        B("Then playtest, fix the top MUST bug on your list, and do the accessibility check for M4.", cue="m4",
          pause=0.8),
    ), actions=(
        A("rose", x=260, y=1010, s=0.72, wave=[("start", "remember"), ("m4$", "end")], moods={"start": "proud"}),
        A("pixi", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "pytest → brain • playtesters → fun", at="brain", until="polish", x=1150, y=460, color="orange",
          size=42),
        A("chip", "normal + edge • test_scores.txt", at="files", until="polish", x=1150, y=600, color="green",
          size=42),
        A("turtle", code=PALETTE, title="Okabe-Ito palette", at="palette", until="text", x=740, y=250, w=540,
          h=360, world=200, duration=0.01, cursor=False),
        A("turtle", code=SHAPES, title="comet vs rock", at="shape", until="text", x=1330, y=250, w=540, h=360,
          world=170, duration=0.01, cursor=False),
        A("chip", "Shape or size, not color alone", at="shape@0.4", until="turn", x=1300, y=700, color="yellow",
          size=42),
        A("icons", at="text", until="turn", x=1300, y=400, gap=270,
          items=[("book", "text 16+", "text"), ("key", "keys on screen", "text@0.35"),
                 ("warning", "no fast flashing", "text@0.7"), ("clock", "slow start", "gentle")]),
        A("chip", "Text 16+ • Keys on screen", at="text@0.4", until="turn", x=1300, y=820, color="sky", size=40),
        A("chip", "No fast flashing • Gentle start", at="gentle", until="turn", x=1300, y=930, color="green",
          size=40),
        A("banner", "NEXT: M3 data + 3 tests → M4 polish", at="turn", color="green"),
        A("cards", at="turn", x=640, y=230, w=860, gap=105,
          items=["Add a list, a dictionary, a file", "Write 3 tests: all PASSED", "Playtest, fix the top MUST bug",
                 "Accessibility check (M4)"],
          reveal=["turn@0.4", "m3@0.6", "m4", "m4@0.7"]),
        A("roadmap", at="m3", x=760, y=760, w=1000, items=ROAD, checks=[("m3", 0), ("m3", 1)],
          current=[("m3@0.3", 2), ("m4", 3)]),
    )),
))
