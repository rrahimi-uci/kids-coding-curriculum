"""Level 3 Week 11: Project Studio 2: Test and Polish (kit episode). Bee Garden is Nova's own example."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

BEE = '''class Bee:
    def __init__(self):
        self.lives = 3

    def lose_life(self):
        self.lives -= 1
        if self.lives < 0:
            self.lives = 0'''

BEE_BROKEN = '''class Bee:
    def __init__(self):
        self.lives = 3

    def lose_life(self):
        self.lives -= 1'''

TESTS = '''from bee_garden import Bee

def test_bee_starts_with_3_lives():
    assert Bee().lives == 3

def test_lives_never_go_below_zero():
    bee = Bee()
    for i in range(5):
        bee.lose_life()
    assert bee.lives == 0'''

GARDEN = ["....P", ".W...", "..#..", "P..W.", "....."]

EPISODE = Episode(level=3, week=11, scenes=(
    # ------------------------------------------------------------------ s01 hook
    Scene("l3-w11-s01", setting="workshop", lead_in=0.2, beats=(
        B("Bee Garden runs!", cue="runs", pause=0.3),
        B("Nova is ready to show everyone.", cue="ready", pause=0.3),
        B("Then Pixel walks the bee into the corner of the garden…", cue="corner", pause=0.1),
        B("and the whole game crashes.", cue="crash", pause=0.4),
        B("‘But it worked when I played it!’", speaker=NOVA, cue="worked", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("Other people press keys you'd never think of.", cue="keys", pause=0.3),
        B("How can we catch bugs like this before the showcase?", cue="how", pause=3.0),
    ), actions=(
        A("door", "DOOR 11", x=1720, y=900),
        A("nova", x=300, y=960, enter="left", wave="runs",
          moods={"crash": "surprised", "keys": "thinking"}, chin=("how", "end")),
        A("banner", "STUDIO MISSION: Catch bugs early", at="runs"),
        A("grid", x=800, y=200, cell=96, at="runs", until="how", rows=GARDEN,
          states=[("runs", GARDEN), ("crash", [r.replace(".", "X") if i == 4 else r for i, r in enumerate(GARDEN)])],
          marks=[("runs", 0, 4, "P"), ("runs", 3, 0, "P"), ("runs", 1, 1, "W"), ("runs", 3, 3, "W")],
          walker=[("corner", 1, 2), ("corner@0.5", 4, 2), ("corner$", 4, 4)]),
        A("chip", "Bee Garden", at="runs", until="how", x=1040, y=720, color="white", size=36),
        A("pixel", x=600, y=760, drop=True, moods={"crash": "surprised", "worked": "worried"}),
        A("sfx", "boing", at="crash"),
        A("chip", "red error!", at="crash", until="how", x=1040, y=820, color="red", size=44),
        A("badge", ok=False, at="crash", until="how", x=1380, y=180),
        A("icons", at="ready", until="corner", x=1540, y=330, items=[("trophy", "Showcase!")]),
        A("chip", "keys you'd never press", at="keys", until="how", x=1040, y=920, color="white", size=34),
        A("chip", "Pause: How can we find them first?", at="how", x=1080, y=300, color="yellow"),
        A("icons", at="how", x=1080, y=560, items=[("clock", "Showcase soon")]),
        A("thought", "", at="how$+0.2", until="end", x=820, y=480),
    )),
    # ------------------------------------------------------------------ s02 tests, edge cases, playtests, READMEs
    Scene("l3-w11-s02", setting="sky", beats=(
        B("Today has three jobs.", cue="three", pause=0.3),
        B("First, tests: tiny programs that check your program.", cue="tests", pause=0.3),
        B("They're like crash-test dummies for cars.", cue="dummies", pause=0.3),
        B("You can break things on purpose, safely, as often as you like.", cue="break", pause=0.3),
        B("Test the logic, like moving and scoring, not the drawing.", cue="logic", pause=0.3),
        B("And test normal cases and edge cases: the corner, the wall, the empty list, the last life.", cue="edge",
          pause=0.4),
        B("Second, a playtest: someone else uses your project while you watch silently and take notes.",
          cue="playtest", pause=0.3),
        B("Every time they get stuck, you learn something.", cue="stuck", pause=0.4),
        B("Third, a README: it tells a stranger what your project is, how to run it, how it works, and who you thank.",
          cue="readme", pause=0.3),
        B("Future-you is a stranger too!", cue="future", pause=0.6),
    ), actions=(
        A("cards", at="three", x=60, y=230, w=420, gap=130, items=["Tests", "Playtest", "README"],
          reveal=["three@0.2", "three@0.5", "three@0.8"],
          active=[("tests", "playtest"), ("playtest", "readme"), ("readme", "end")], done=["playtest", "readme", None]),
        A("chip", "Tests = tiny programs that check your program", at="tests", until="dummies", x=1180, y=220,
          color="white", size=38),
        A("chip", "Tests = crash-test dummies", at="dummies", until="edge", x=1180, y=220, color="orange", size=44),
        A("icons", at="dummies@0.3", until="edge", x=1180, y=440, gap=300,
          items=[("person", "test dummy", "dummies@0.3"), ("check", "pops back up!", "break")]),
        A("chip", "Break it on purpose, safely", at="break", until="edge", x=1180, y=650, color="white", size=36),
        A("chip", "Test: moving, scoring", at="logic", until="edge", x=960, y=780, color="green", size=36),
        A("chip", "Not: the drawing", at="logic@0.6", until="edge", x=1440, y=780, color="red", size=36),
        A("grid", x=620, y=240, cell=100, at="edge", until="playtest", rows=["....", "..#.", "....", "...G"]),
        A("chip", "wall", at="edge@0.4", until="playtest", x=870, y=200, color="white", size=30),
        A("chip", "corner", at="edge@0.3", until="playtest", x=970, y=680, color="yellow", size=30),
        A("chip", "[ ]  empty list", at="edge@0.6", until="playtest", x=1300, y=360, color="sky", size=40),
        A("icons", at="edge@0.8", until="playtest", x=1650, y=380, items=[("heart", "last life")]),
        A("chip", "Edge cases: corner, wall, empty, last life", at="edge$", until="playtest", x=1180, y=820,
          color="orange", size=40),
        A("icons", at="playtest", until="readme", x=1180, y=420, gap=320,
          items=[("person", "Someone else plays", "playtest@0.2"), ("magnifier", "You watch silently",
                                                                     "playtest@0.5"),
                 ("file", "Take notes", "playtest@0.8")]),
        A("chip", "Playtest: watch silently", at="playtest@0.6", until="readme", x=1180, y=720, color="green",
          size=42),
        A("chip", "Stuck? You learn something", at="stuck", until="readme", x=1180, y=840, color="white", size=36),
        A("file", "README.md", at="readme", x=620, y=220, w=620, h=520,
          states=[("readme", ["# Bee Garden"]), ("readme@0.25", ["# Bee Garden", "What it is"]),
                  ("readme@0.45", ["# Bee Garden", "What it is", "## How to run"]),
                  ("readme@0.65", ["# Bee Garden", "What it is", "## How to run", "## How it works"]),
                  ("readme@0.85", ["# Bee Garden", "What it is", "## How to run", "## How it works", "## Credits"])]),
        A("chip", "README: what • run • how • credits", at="readme@0.5", x=1560, y=400, color="orange", size=30),
        A("chip", "Future-you is a stranger too!", at="future", x=1560, y=560, color="yellow", size=32),
    )),
    # ------------------------------------------------------------------ s03 two tests for a tiny Bee class
    Scene("l3-w11-s03", setting="lavender", beats=(
        B("Let's test a tiny Bee class.", cue="tiny", pause=0.3),
        B("A new bee has three lives.", cue="three", pause=0.3),
        B("lose_life takes one away, and if lives drop below zero, it sets them back to zero.", cue="lose", pause=0.4),
        B("Nova writes two tests, and each name says what it checks.", cue="writes", pause=0.3),
        B("Test one: a new bee starts with three lives.", cue="t1", pause=0.3),
        B("Test two is an edge case: lose five lives in a row, and lives should stop at zero.", cue="t2", pause=0.4),
        B("In Thonny's system shell, type python, dash m, pytest, dash q.", cue="shell", pause=0.3),
        B("Two dots: two passing tests!", cue="dots", pause=0.4),
        B("But is test two any good?", cue="good", pause=1.4),
        B("Break the code on purpose.", cue="breakit", pause=0.3),
        B("Nova deletes the two lines that stop at zero, and runs again.", cue="deletes", pause=0.3),
        B("An F appears, with the name: lives never go below zero.", cue="f", pause=0.3),
        B("The test caught it!", cue="caught", pause=0.4),
        B("Put the lines back, green again, and commit: ‘Add tests for Bee lives.’", cue="back", pause=0.8),
    ), actions=(
        A("code", code=BEE, title="bee_garden.py", x=60, y=160, w=860, h=520, size=32, at="tiny", until="deletes",
          shell=False, highlight=[(3, "three", "three>"), (6, "lose", "lose@0.4"), (7, "lose@0.4", "lose>"),
                                  (8, "lose@0.4", "lose>"), (7, "breakit", "deletes"), (8, "breakit", "deletes")]),
        A("code", code=BEE_BROKEN, title="bee_garden.py", x=60, y=160, w=860, h=520, size=32, at="deletes",
          until="back", shell=False),
        A("code", code=BEE, title="bee_garden.py", x=60, y=160, w=860, h=520, size=32, at="back", shell=False,
          highlight=[(7, "back", "back@0.4"), (8, "back", "back@0.4")]),
        A("code", code=TESTS, title="test_bee_garden.py", x=960, y=160, w=900, h=520, size=28, at="writes",
          shell=False, type=("writes", "t2$"),
          highlight=[(3, "t1", "t1>"), (4, "t1", "t1>"), (6, "t2", "t2>"), (8, "t2", "t2>"), (10, "t2@0.6", "t2>"),
                     (6, "f", "caught>")]),
        A("terminal", title="System shell", at="shell", until="deletes", x=60, y=720, w=1080, h=300, size=28,
          lines=[("shell@0.2", "python -m pytest -q", "cmd"), ("dots", "..   [100%]", "out"),
                 ("dots@0.3", "2 passed in 0.01s", "out")]),
        A("terminal", title="System shell", at="deletes", until="back", x=60, y=720, w=1080, h=300, size=24,
          lines=[("deletes@0.7", "python -m pytest -q", "cmd"), ("f", ".F   [100%]", "out"),
                 ("f@0.4", "FAILED test_bee_garden.py::test_lives_never_go_below_zero", "out"),
                 ("f@0.7", "1 failed, 1 passed in 0.03s", "out")]),
        A("terminal", title="System shell", at="back", x=60, y=720, w=1080, h=300, size=26,
          lines=[("back@0.3", "python -m pytest -q", "cmd"), ("back@0.45", "..   [100%]", "out"),
                 ("back@0.5", "2 passed in 0.01s", "out"),
                 ("back@0.6", 'git commit -m "Add tests for Bee lives"', "cmd")]),
        A("chip", "Test names say what they check", at="writes@0.4", until="shell", x=1500, y=760, color="yellow",
          size=34),
        A("chip", "python -m pytest -q", at="shell@0.4", until="breakit", x=1500, y=760, color="sky", size=40),
        A("chip", ". = pass • F = fail", at="dots", x=1500, y=860, color="white", size=40),
        A("thought", "Any good?", at="good$", until="good>", x=1500, y=760),
        A("chip", "Break it on purpose: does it go red?", at="breakit", x=1500, y=960, color="orange", size=32),
        A("badge", ok=False, at="f", until="back", x=1820, y=780, r=40),
        A("badge", ok=True, at="caught", until="back", x=1700, y=760, r=44),
        A("badge", ok=True, at="back@0.5", x=1700, y=760, r=44),
    )),
    # ------------------------------------------------------------------ s04 playtest triage (bug hunt)
    Scene("l3-w11-s04", setting="mint", beats=(
        B("Playtest time!", cue="play", pause=0.3),
        B("Pixel plays Bee Garden for three minutes, thinking out loud, while Nova stays silent and writes one "
          "feedback card per thing: what happened, and what did the player expect?", cue="plays", pause=0.3),
        B("The cards say: the game crashes in the corner.", cue="c1", pause=0.3),
        B("Pollen and wasps look the same.", cue="c2", pause=0.3),
        B("And, ‘I wish there were sound effects.’", cue="c3", pause=0.4),
        B("Now triage: sort the cards into three piles.", cue="triage", pause=0.3),
        B("Must fix: crashes, can't start, can't win.", cue="must", pause=0.3),
        B("Should fix: confusing, unfair, hard to read.", cue="should", pause=0.3),
        B("Nice to have: new ideas for version two.", cue="nice", pause=0.4),
        B("Which pile does the crash go in?", cue="which", pause=0.2),
        B("Pause and decide.", cue="decide", pause=3.6),
        B("Yes, must fix!", cue="yes", pause=0.4),
        B("For a crash, first write a test that shows the bug, then fix it, so it never comes back.", cue="test",
          pause=0.3),
        B("Commit: ‘Fix crash when the bee walks into the corner.’", cue="commit", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Playtest triage", at="play", color="navy"),
        A("pixel", x=320, y=760, s=0.8, at="play", until="triage", moods={"plays": "thinking", "c1": "surprised"}),
        A("bubble", "Hmm, where do I go?", at="plays@0.1", until="plays@0.45", x=360, y=520, size=32),
        A("nova", x=1640, y=980, s=0.75, at="play", until="triage", moods={"plays": "thinking"}),
        A("chip", "silent • taking notes", at="plays@0.4", until="triage", x=1640, y=540, color="white", size=32),
        A("panel", "Feedback card", x=620, y=200, w=760, at="plays@0.5", until="triage", size=32,
          items=[("plays@0.75", "What happened?"), ("plays@0.88", "What did the player expect?")]),
        A("chip", "Crashes in the corner", at="c1", until="triage", x=1000, y=560, color="red", size=38),
        A("chip", "Pollen and wasps look the same", at="c2", until="triage", x=1000, y=670, color="yellow", size=38),
        A("chip", "Wish: sound effects", at="c3", until="triage", x=1000, y=780, color="sky", size=38),
        A("panel", "1 Must fix", x=110, y=200, w=540, at="triage", color="#D55E00", size=32,
          items=[("must", "crashes"), ("must@0.35", "can't start"), ("must@0.65", "can't win"),
                 ("yes", "→ crash in the corner")]),
        A("panel", "2 Should fix", x=690, y=200, w=540, at="triage@0.3", color="#C77700", size=32,
          items=[("should", "confusing"), ("should@0.3", "unfair"), ("should@0.6", "hard to read"),
                 ("should$", "→ pollen = wasps?")]),
        A("panel", "3 Nice to have", x=1270, y=200, w=540, at="triage@0.6", color="#009E73", size=32,
          items=[("nice", "new ideas"), ("nice@0.4", "for version 2"), ("nice$", "→ sound effects")]),
        A("chip", "Must fix • Should fix • Nice to have", at="triage$", until="test", x=960, y=680, color="white",
          size=40),
        A("chip", "Crashes in the corner", at="which", until="yes", x=960, y=800, color="red", size=40),
        A("thought", "Which pile?", at="decide$", until="decide>", x=1400, y=820),
        A("badge", ok=True, at="yes", until="test", x=600, y=280, r=36),
        A("tests", "pytest", at="test@0.15", until="test@0.6", x=110, y=640, w=830,
          items=[("test@0.2", "test_bee_stops_in_the_corner", False)]),
        A("tests", "pytest", at="test@0.6", x=110, y=640, w=830,
          items=[("test@0.65", "test_bee_stops_in_the_corner", True)]),
        A("chip", "Crash? Write a test first, then fix", at="test", x=960, y=950, color="orange", size=40),
        A("terminal", at="commit", x=970, y=640, w=890, h=180, size=21,
          lines=[("commit@0.1", 'git commit -m "Fix crash when the bee walks into the corner"', "cmd")]),
        A("chip", 'git commit -m "Fix crash when..."', at="commit@0.5", x=1460, y=875, color="green",
          size=34),
    )),
    # ------------------------------------------------------------------ s05 recap, accessibility, handoff
    Scene("l3-w11-s05", setting="workshop", tail=0.8, beats=(
        B("Project leveled up!", cue="up", pause=0.4),
        B("Tests are crash-test dummies, edge cases hide in corners, and triage means fixing the most important thing "
          "first.", cue="recap", pause=0.4),
        B("Now the accessibility and usability check.", cue="check", pause=0.3),
        B("Use colors from the Okabe-Ito palette, and never color alone: add shapes, letters or text.", cue="colors",
          pause=0.3),
        B("Make text big enough to read from a chair.", cue="big", pause=0.3),
        B("Write the controls on screen.", cue="controls", pause=0.3),
        B("Nothing flashes fast.", cue="flash", pause=0.3),
        B("A new player should know what to do within ten seconds.", cue="ten", pause=0.4),
        B("And list every borrowed image or sound with its license.", cue="license", pause=0.4),
        B("Now Milestone 3: write five tests, including an edge case, and commit when they pass.", cue="m3", pause=0.3),
        B("Then the playtest swap and triage.", cue="swap", pause=0.3),
        B("Then Milestone 4: your README and one accessibility fix.", cue="m4", pause=0.6),
    ), actions=(
        A("door", "DOOR 11", x=1720, y=920, open="up"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "recap"), ("m4@0.7", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("cards", at="recap", until="check", x=700, y=230, w=820, gap=110, size=36,
          items=["Tests = crash-test dummies", "Edge cases hide in corners", "Triage: most important first"],
          reveal=["recap", "recap@0.35", "recap@0.7"]),
        A("chip", "Accessibility + usability check", at="check", until="big", x=1110, y=200, color="orange",
          size=42),
        A("grid", x=890, y=300, cell=110, at="colors", until="big", rows=["G.B", ".G.", "B.G"],
          marks=[("colors@0.5", 0, 0, "P"), ("colors@0.5", 1, 1, "P"), ("colors@0.5", 2, 2, "P"),
                 ("colors@0.5", 0, 2, "W"), ("colors@0.5", 2, 0, "W")]),
        A("chip", "P = pollen • W = wasp", at="colors@0.6", until="big", x=1110, y=680, color="white", size=34),
        A("chip", "Never color alone: add shapes or letters", at="colors@0.7", until="big", x=1110, y=790,
          color="yellow", size=36),
        A("icons", at="big", until="m3", x=1110, y=360, gap=230,
          items=[("book", "Big text", "big"), ("game", "Controls on screen", "controls"),
                 ("warning", "No fast flashing", "flash"), ("clock", "Clear in 10 seconds", "ten")]),
        A("chip", "Big text • Controls on screen • No flashing", at="flash@0.5", until="m3", x=1110, y=640,
          color="green", size=36),
        A("chip", "Credits: every borrowed image or sound + license", at="license", until="m3", x=1110, y=760,
          color="white", size=32),
        A("banner", "NEXT: M3 tests → playtest → M4 README", at="m3", color="green"),
        A("cards", at="m3", x=700, y=230, w=820, gap=110,
          items=["M3: 5 tests (one edge case), commit", "Playtest swap + triage", "M4: README + one accessibility fix"],
          reveal=["m3@0.1", "swap", "m4"]),
        A("roadmap", x=760, y=700, w=760, at="m3", items=["M1", "M2", "M3", "M4", "Showcase"],
          checks=[("m3", 0), ("m3", 1)], current=[("m3", 2), ("m4", 3)]),
    )),
))
