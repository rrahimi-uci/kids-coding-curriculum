"""Level 3 Week 10: Project Studio 1: Design First (kit episode). Bee Garden is Nova's own example."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

TANGLE = '''x = 0
y = 0
wx = 5
wy = 5
p = 0
x = x + 1
if x == wx:
    print("ouch")'''

WASP_BUG = '''class Critter:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Wasp(Critter):
    def __init__(self, row, col):
        self.speed = 1

wasp = Wasp(2, 3)
print(wasp.row)'''

WASP_FIX = '''class Critter:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Wasp(Critter):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.speed = 1

wasp = Wasp(2, 3)
print(wasp.row)'''

FLOWER = '''import turtle

t = turtle.Turtle()
t.pencolor("#E69F00")
t.pensize(4)
for petal in range(12):
    t.forward(120)
    t.left(150)
turtle.done()
'''

# class diagram geometry (s03): tree 1 (is a) centered at x=600, tree 2 (has a) at x=1450
TOP, LOW = 240, 540

EPISODE = Episode(level=3, week=10, scenes=(
    # ------------------------------------------------------------------ s01 hook
    Scene("l3-w10-s01", setting="workshop", lead_in=0.2, beats=(
        B("Nova's pitch card says: Bee Garden, a grid game where a bee collects pollen and dodges wasps.", cue="pitch",
          pause=0.3),
        B("Nova opens Thonny and starts typing as fast as possible.", cue="typing", pause=0.2),
        B("‘Wait!’", speaker=PIXEL, cue="waitp", pause=0.1),
        B("beeps Pixel.", cue="beeps", pause=0.1),
        B("‘Which parts are there? Who does what?’", speaker=PIXEL, cue="which", pause=0.4),
        B("Builders draw plans before they pour concrete.", cue="builders", pause=0.3),
        B("Today we design first.", cue="design", pause=0.3),
        B("What's your plan?", cue="plan", pause=3.0),
    ), actions=(
        A("nova", x=300, y=960, enter="left", point="pitch",
          moods={"typing": "happy", "waitp": "surprised", "builders": "thinking"}, chin=("plan", "end")),
        A("pixel", x=600, y=760, drop=True, moods={"waitp": "worried", "builders": "happy"}),
        A("banner", "STUDIO MISSION: Design first", at="pitch"),
        A("panel", "Pitch card: Bee Garden", x=820, y=200, w=760, until="typing", size=34,
          items=[("pitch@0.3", "A grid game"), ("pitch@0.55", "A bee collects pollen"),
                 ("pitch@0.8", "It dodges the wasps")]),
        A("grid", x=1640, y=230, cell=70, until="typing", rows=["...", "...", "..."],
          marks=[("pitch@0.5", 0, 0, "B"), ("pitch@0.6", 1, 2, "P"), ("pitch@0.85", 2, 1, "W")]),
        A("code", code=TANGLE, title="bee_garden.py", x=760, y=190, w=820, h=560, size=34, at="typing",
          until="builders", type=("typing", "which$")),
        A("chip", "x? wx? p? ???", at="which", until="builders", x=1170, y=820, color="red", size=40),
        A("panel", "Blueprint: Bee Garden", x=800, y=200, w=780, color="blue", at="builders", until="plan", size=34,
          items=[("builders@0.4", "Which parts? (classes)"), ("design", "Who does what?"),
                 ("design@0.5", "Then write the code")]),
        A("chip", "Pause: What parts does your project need?", at="plan", x=1100, y=300, color="yellow", size=40),
        A("thought", "", at="plan$+0.2", until="end", x=840, y=440),
    )),
    # ------------------------------------------------------------------ s02 brief, paths and milestones
    Scene("l3-w10-s02", setting="sky", beats=(
        B("Your final project, Build Something Big, can be a grid game, a generative art app, or a data or AI app.",
          cue="options", pause=0.4),
        B("It needs two or more classes, one using inheritance or composition.", cue="classes", pause=0.3),
        B("It needs a data structure beyond a flat list, like a dictionary, a queue or a grid.", cue="data",
          pause=0.3),
        B("Add one named algorithm, a saved file, five or more pytest tests, eight or more meaningful commits, and a "
          "README.", cue="add", pause=0.3),
        B("It must be fair and safe, too.", cue="fair", pause=0.4),
        B("Most people take the Core path: start from a template, add one class of your own, reuse an algorithm from "
          "class, and save one file.", cue="core", pause=0.3),
        B("The template's tests count toward your five.", cue="count", pause=0.3),
        B("The Full path is extra challenge: your own design.", cue="full", pause=0.4),
        B("The milestones are Pitch, Design and core classes, Features with five tests and a playtest, README and "
          "polish, and the Showcase.", cue="milestones", pause=0.6),
    ), actions=(
        A("banner", "PROJECT: Build Something Big", at="options", color="purple", until="core"),
        A("icons", at="options", until="classes", x=960, y=470, gap=420,
          items=[("game", "Grid game", "options@0.45"), ("star", "Generative art app", "options@0.65"),
                 ("magnifier", "Data or AI app", "options@0.85")]),
        A("panel", "Must-haves", x=120, y=200, w=880, at="classes", until="core", size=32,
          items=[("classes", "2+ classes (inheritance or composition)"), ("data", "A data structure (dict, queue, grid)"),
                 ("add", "One named algorithm"), ("add@0.2", "A saved file"), ("add@0.4", "5+ pytest tests"),
                 ("add@0.65", "8+ meaningful commits"), ("add@0.9", "README"), ("fair", "Fair and safe")]),
        A("chip", "2+ classes • data structure • algorithm", at="add", until="core", x=1440, y=420, color="orange",
          size=32),
        A("chip", "Saved file • 5+ tests • 8+ commits • README", at="add@0.9", until="core", x=1440, y=540,
          color="green", size=30),
        A("chip", "Core path (recommended)", at="core", until="milestones", x=560, y=240, color="green", size=44),
        A("cards", at="core@0.2", until="milestones", x=180, y=320, w=760, gap=104, size=34,
          items=["Start from a template", "Add one class of your own", "Reuse an algorithm from class",
                 "Save one file"],
          reveal=["core@0.25", "core@0.45", "core@0.65", "core@0.85"]),
        A("chip", "Core path: template + 1 new class", at="core$", until="milestones", x=560, y=800, color="orange",
          size=38),
        A("chip", "Template tests count toward 5", at="count", until="milestones", x=560, y=900, color="white",
          size=34),
        A("chip", "Full path (extra challenge)", at="full", until="milestones", x=1430, y=240, color="purple",
          size=44),
        A("chip", "Your own design", at="full@0.6", until="milestones", x=1430, y=360, color="white", size=38),
        A("roadmap", x=230, y=480, w=1460, at="milestones",
          items=["M1 Pitch", "M2 Design + core classes", "M3 Features + 5 tests + playtest", "M4 README + polish",
                 "Showcase"],
          checks=[("milestones@0.15", 0)],
          current=[("milestones@0.15", 0), ("milestones@0.3", 1), ("milestones@0.55", 2), ("milestones@0.78", 3),
                   ("milestones@0.92", 4)]),
        A("chip", "M1 → M2 → M3 → M4 → Showcase", at="milestones@0.5", x=960, y=800, color="orange", size=46),
    )),
    # ------------------------------------------------------------------ s03 CRC cards, class diagram, first commit
    Scene("l3-w10-s03", setting="lavender", beats=(
        B("Let's design Bee Garden.", cue="design", pause=0.3),
        B("A CRC card is an index card for one class: the Class name on top, its Responsibilities on the left, what it "
          "knows and does, and its Collaborators on the right, the classes it works with.", cue="crc", pause=0.3),
        B("Bee: knows its row and column, moves unless a wall is in the way, collects pollen.", cue="bee", pause=0.2),
        B("It works with Garden.", cue="works", pause=0.3),
        B("Garden: holds the grid and says if a square is a wall.", cue="garden", pause=0.4),
        B("Now the class diagram.", cue="diagram", pause=0.2),
        B("A hollow arrow means ‘is a’: a Bee is a Critter, and so is a Wasp.", cue="isa", pause=0.3),
        B("A diamond line means ‘has a’: the Game has a Garden and a Bee.", cue="hasa", pause=0.4),
        B("Then, in Terminal, inside the project folder: git init, git add, and git commit with a message that starts "
          "with a verb, like ‘Add empty Garden and Bee classes.’", cue="git", pause=0.3),
        B("Git writes your name into every save point, so use your nickname, never your real name.", cue="nick",
          pause=0.6),
    ), actions=(
        A("chip", "CRC: Class, Responsibilities, Collaborators", at="crc", until="diagram", x=960, y=130,
          color="orange", size=42),
        A("table", "Class: Bee", x=120, y=300, col_w=400, row_h=96, at="crc@0.3", until="diagram",
          header=["Responsibilities", "Collaborators"],
          rows=[["knows its row, col", "Garden"], ["moves, not into walls", ""], ["collects pollen", ""]],
          reveal=["bee", "bee@0.4", "bee@0.8"], highlight=[("works", "works>", 0)]),
        A("table", "Class: Garden", x=1000, y=300, col_w=400, row_h=96, at="garden", until="diagram",
          header=["Responsibilities", "Collaborators"],
          rows=[["holds the grid", ""], ["is this a wall?", ""]], reveal=["garden@0.3", "garden@0.6"]),
        A("arrow", x1=820, y1=444, x2=1000, y2=444, color="blue", at="works", until="diagram", width=8),
        # class diagram
        A("tree", x=600, y=TOP, gap=460, level_gap=LOW - TOP, w=300, at="diagram", until="git",
          nodes=[("Critter", None, ["row, col"], "isa"), ("Wasp", "Critter", ["speed"], "isa@0.85"),
                 ("Bee", "Critter", ["pollen"], "isa@0.6")]),
        A("arrow", x1=370, y1=LOW - 10, x2=600, y2=TOP + 114, color="navy", at="isa@0.85", until="git", width=6),
        A("arrow", x1=830, y1=LOW - 10, x2=600, y2=TOP + 114, color="navy", at="isa@0.6", until="git", width=6),
        A("chip", "is a", at="isa@0.6", until="git", x=760, y=440, color="white", size=30),
        A("chip", "is a", at="isa@0.85", until="git", x=440, y=440, color="white", size=30),
        A("tree", x=1450, y=TOP, w=300, level_gap=LOW - TOP, at="hasa", until="git",
          nodes=[("Game", None, ["garden, bee"], "hasa"), ("Garden", "Game", ["grid"], "hasa@0.5")]),
        A("arrow", x1=1450, y1=TOP + 114, x2=1450, y2=LOW - 10, color="#C77700", at="hasa@0.5", until="git", width=6),
        A("arrow", x1=1300, y1=TOP + 100, x2=985, y2=LOW + 20, color="#C77700", at="hasa@0.8", until="git",
          width=6),
        A("chip", "has a", at="hasa@0.5", until="git", x=1550, y=450, color="orange", size=30),
        A("chip", "has a", at="hasa@0.8", until="git", x=1160, y=470, color="orange", size=30),
        A("chip", "Hollow arrow = is a • Diamond = has a", at="hasa$", until="git", x=960, y=850, color="yellow",
          size=40),
        # first commit
        A("terminal", at="git", x=120, y=180, w=1680, h=560, size=30,
          lines=[("git@0.15", "git init", "cmd"), ("git@0.25", "Initialized empty Git repository in …/bee-garden/.git/", "out"),
                 ("git@0.35", "git add bee_garden.py", "cmd"),
                 ("git@0.5", 'git commit -m "Add empty Garden and Bee classes"', "cmd"),
                 ("git@0.85", "[master (root-commit) 3f9a2c1] Add empty Garden and Bee classes", "out"),
                 ("nick", "git log", "cmd"), ("nick@0.25", "commit 3f9a2c1…", "out"),
                 ("nick@0.35", "Author: NovaCodes <novacodes@example.com>", "out"),
                 ("nick@0.5", "    Add empty Garden and Bee classes", "out")]),
        A("chip", 'git commit -m "Add empty Garden..."', at="git@0.6", x=620, y=830, color="green", size=38),
        A("chip", "Messages start with a verb", at="git@0.8", x=620, y=950, color="yellow", size=38),
        A("chip", "Nickname, never your real name", at="nick@0.4", x=1380, y=830, color="orange", size=38),
    )),
    # ------------------------------------------------------------------ s04 partner code review (bug hunt)
    Scene("l3-w10-s04", setting="mint", beats=(
        B("Time for a partner code review!", cue="review", pause=0.3),
        B("Partners swap seats and read each other's code using three questions.", cue="swap", pause=0.3),
        B("One: does every class match a CRC card?", cue="q1", pause=0.3),
        B("Two: is there a method that does two jobs?", cue="q2", pause=0.3),
        B("Three: is there a name I don't understand?", cue="q3", pause=0.4),
        B("Pixel reviews Nova's code.", cue="pixelrev", pause=0.2),
        B("A Wasp is a Critter, but its init only sets speed.", cue="wasp", pause=0.3),
        B("Pixel runs it.", cue="runs", pause=0.4),
        B("Read the last line of the error: AttributeError, Wasp object has no attribute row.", cue="read",
          pause=0.3),
        B("Predict.", cue="predict", pause=0.2),
        B("‘I think Wasp never ran Critter's init,’", speaker=NOVA, cue="nova", pause=0.1),
        B("says Nova.", cue="says", pause=3.6),
        B("Fix one thing: add super, dot, init, with row and col, as the first line.", cue="fix", pause=0.3),
        B("Check: run it again.", cue="check", pause=0.3),
        B("Now the wasp knows where it is!", cue="knows", pause=0.4),
        B("Pixel writes one star, ‘Clear class names,’", cue="star", pause=0.2),
        B("and one wish: ‘Add a test for Wasp.’", cue="wish", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Partner code review", at="review", color="navy"),
        A("chair", x=560, y=900, at="swap", until="pixelrev"),
        A("chair", x=1360, y=900, at="swap", until="pixelrev"),
        A("laptop", x=560, y=640, s=0.7, at="swap", until="pixelrev"),
        A("laptop", x=1360, y=640, s=0.7, at="swap", until="pixelrev"),
        A("nova", x=560, y=960, s=0.7, at="review", until="pixelrev", path=[("swap@0.3", 560, 960), ("swap$", 1360, 960)]),
        A("pixel", x=1360, y=820, s=0.6, ground=960, at="review", until="pixelrev",
          path=[("swap@0.3", 1360, 820), ("swap$", 560, 820)]),
        A("cards", at="q1", until="pixelrev", x=560, y=220, w=800, gap=104, size=36,
          items=["Every class matches a CRC card?", "A method doing two jobs?", "A name I don't understand?"],
          reveal=["q1", "q2", "q3"], active=["q1", "q2", "q3"]),
        A("chip", "3 review questions: card? two jobs? name?", at="q3@0.5", until="pixelrev", x=960, y=560,
          color="yellow", size=40),
        A("code", code=WASP_BUG, title="bee_garden.py", x=70, y=170, w=920, h=800, size=30, shell_h=170,
          at="pixelrev", until="fix", run="runs", line_delay=0.6, allow_error=True, error_line=11,
          expect=["AttributeError: 'Wasp' object has no attribute 'row'"],
          highlight=[(6, "wasp", "wasp@0.4"), (7, "wasp@0.4", "runs"), (8, "wasp@0.4", "runs"),
                     (8, "nova", "says>")]),
        A("cards", at="read", x=1090, y=200, w=660, gap=86, size=34,
          items=["Read", "Predict", "Watch", "Fix ONE thing", "Check"],
          reveal=["read", "read@0.1", "read@0.2", "read@0.3", "read@0.4"],
          active=["read", ("predict", "fix"), None, ("fix", "check"), ("check", "star")],
          done=["predict", "fix", None, "check", "knows"], until="star"),
        A("chip", "AttributeError: no attribute 'row'", at="read@0.5", until="fix", x=1420, y=740, color="red",
          size=34),
        A("thought", "Which one change?", at="says$+0.3", until="says>", x=1420, y=860),
        A("code", code=WASP_FIX, title="bee_garden.py", x=70, y=170, w=920, h=820, size=30, shell_h=170,
          at="fix", run="check$", line_delay=0.5, expect=["2"], highlight=[(8, "fix", "knows$")]),
        A("chip", "super().__init__(row, col)", at="fix@0.5", until="star", x=1420, y=740, color="green", size=40),
        A("badge", ok=False, at="read", until="fix", x=1830, y=330, r=40),
        A("badge", ok=True, at="knows", until="star", x=1420, y=880),
        A("chip", "★ Clear class names", at="star", x=1420, y=300, color="yellow", size=44),
        A("chip", "Wish: Add a test for Wasp", at="wish", x=1420, y=450, color="pink", size=40),
        A("chip", "One star + one wish", at="wish@0.5", x=1420, y=600, color="orange", size=40),
        A("pixel", x=1420, y=860, s=0.5, ground=950, at="star", moods={"star": "happy"}),
    )),
    # ------------------------------------------------------------------ s05 recap, licenses, handoff
    Scene("l3-w10-s05", setting="workshop", tail=0.8, beats=(
        B("Design done!", cue="done", pause=0.4),
        B("CRC cards say what each class knows and does.", cue="crc", pause=0.3),
        B("The class diagram shows ‘is a’ and ‘has a.’", cue="diagram", pause=0.3),
        B("Milestones are like LEGO bags, and each commit is a photo after a bag.", cue="lego", pause=0.4),
        B("Now, may you use that picture or sound?", cue="may", pause=0.4),
        B("Everything in your project must be yours or allowed.", cue="yours", pause=0.3),
        B("Python's standard library is free, and your own drawings are yours.", cue="stdlib", pause=0.3),
        B("CC0 means free for anyone.", cue="cc0", pause=0.3),
        B("CC BY means free if you give credit.", cue="ccby", pause=0.3),
        B("All rights reserved, or no license, means no.", cue="arr", pause=0.4),
        B("Never download without a parent, and list borrowed things in your README's Credits.", cue="never",
          pause=0.3),
        B("Easiest choice: draw it with turtle!", cue="turtle", pause=0.4),
        B("Now grab index cards: one CRC card per class.", cue="next", pause=0.3),
        B("Play one turn, draw your diagram, then git init and commit your class skeletons.", cue="play", pause=0.6),
    ), actions=(
        A("door", "DOOR 10", x=1700, y=920, open="done"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "crc"), ("play@0.8", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "CRC cards: knows + does", at="crc", until="lego", x=1150, y=260, color="orange", size=42),
        A("chip", "Diagram: is a • has a", at="diagram", until="lego", x=1150, y=380, color="sky", size=42),
        A("timeline", x=820, y=520, w=900, at="lego", until="may",
          commits=[("lego@0.3", "bag 1 + photo"), ("lego@0.5", "bag 2 + photo"), ("lego@0.7", "bag 3 + photo"),
                   ("lego@0.9", "bag 4 + photo")], head=False),
        A("icons", at="lego@0.2", until="may", x=1260, y=780, gap=260,
          items=[("game", "LEGO bag = milestone"), ("camera", "photo = commit")]),
        A("chip", "May I use this?", at="may", until="cc0", x=1150, y=260, color="yellow", size=46),
        A("icons", at="yours", until="cc0", x=1150, y=500, gap=300,
          items=[("person", "Yours", "yours@0.5"), ("book", "Standard library: free", "stdlib"),
                 ("heart", "Your drawings", "stdlib@0.6")]),
        A("icons", at="cc0", until="never", x=1150, y=330, gap=300, crossed=[2],
          items=[("check", "CC0: free for anyone", "cc0"), ("star", "CC BY: free + give credit", "ccby"),
                 ("lock", "All rights reserved / no license", "arr")]),
        A("chip", "CC0 = free • CC BY = free + credit", at="ccby@0.5", until="never", x=1150, y=620,
          color="green", size=40),
        A("chip", "No license = do not use", at="arr@0.5", until="never", x=1150, y=740, color="red", size=40),
        A("file", "README.md", at="never", until="next", x=760, y=200, w=600, h=500,
          states=[("never", ["# Bee Garden", "", "## Credits"]),
                  ("never@0.7", ["# Bee Garden", "", "## Credits", "- bee sound: CC0", "- (borrowed things go here)"])]),
        A("chip", "Ask a parent before any download", at="never@0.3", until="next", x=1060, y=790, color="white",
          size=34),
        A("turtle", code=FLOWER, x=1420, y=140, w=380, h=370, run="turtle", duration=2.0, title="Draw it with turtle",
          at="turtle", until="next"),
        A("banner", "NEXT: CRC cards → diagram → git init", at="next", color="green"),
        A("cards", at="next", x=700, y=230, w=800, gap=110,
          items=["One CRC card per class", "Play one turn", "Draw your class diagram", "git init + commit skeletons"],
          reveal=["next@0.2", "play", "play@0.3", "play@0.6"]),
    )),
))
