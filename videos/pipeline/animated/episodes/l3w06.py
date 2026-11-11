"""Level 3 Week 6: Slow-Motion Debugging (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, Scene

FAST = '''total = 0
for n in range(1, 9):
    total = total + n
    print(total)
'''

STARS = '''stars = 2
stars = stars * 5
print(stars)
'''

ROBOT = '''class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 50

    def charge(self, power):
        self.battery = self.battery + power

bolt = Robot("Bolt")
bolt.charge(25)
print(bolt.battery)
'''

COINS_BUG = '''for coin in [3, 4, 5]:
    total = 0
    total = total + coin
print(total)
'''
COINS_FIX = '''total = 0
for coin in [3, 4, 5]:
    total = total + coin
print(total)
'''

TOOLBAR = ["Run", "Debug", "Step over", "Step into", "Resume", "Stop"]

EPISODE = Episode(level=3, week=6, scenes=(
    Scene("l3-w06-s01", setting="workshop", lead_in=0.2, beats=(
        B("Checkpoint week!", cue="checkpoint", pause=0.3),
        B("Nova and Pixel look back at their quest map: save points, blueprints, families, searching and sorting.",
          cue="map", pause=0.3),
        B("But today, Nova's code does something strange, and it happens too fast to see.", cue="strange",
          pause=0.3),
        B("‘I wish I could slow it down,’", speaker=NOVA, cue="wish", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("What if you could watch your code think, one line at a time?", cue="question", pause=3.0),
    ), actions=(
        A("nova", x=300, y=960, enter="left", wave=("checkpoint", "map"),
          moods={"map": "proud", "strange": "surprised", "wish": "worried", "question": "thinking"},
          chin=("question", "end")),
        A("pixel", x=620, y=760, drop=True, moods={"map": "proud", "strange": "confused"}),
        A("banner", "MISSION: Watch the code think", at="checkpoint"),
        A("roadmap", at="map", until="strange", x=880, y=480, w=900,
          items=["Git", "Classes", "Families", "Search", "Sort", "Debug"],
          checks=[("map@0.3", 0), ("map@0.45", 1), ("map@0.6", 2), ("map@0.75", 3), ("map@0.9", 4)],
          current=[("map$", 5)]),
        A("icons", at="map$", until="strange", x=1780, y=760, items=[("magnifier", "door 6", "map$")]),
        A("code", code=FAST, title="mystery.py", x=860, y=190, w=960, h=540, at="strange", run="strange@0.4",
          line_delay=0.12, expect=["1", "3", "6", "10", "15", "21", "28", "36"]),
        A("chip", "too fast to see!", at="strange@0.7", until="question", x=1340, y=820, color="red"),
        A("chip", "slow it down?", at="says", until="question", x=1340, y=930, color="sky", size=38),
        A("chip", "Pause: Where could a bug hide?", at="question", x=1340, y=820, color="yellow", size=40),
        A("thought", "", at="question$+0.3", until="end", x=640, y=360),
    )),
    Scene("l3-w06-s02", setting="sky", beats=(
        B("You can, with a debugger.", cue="can", pause=0.2),
        B("A debugger is a slow-motion replay for your code.", cue="replay", pause=0.3),
        B("It's like the replay of a soccer goal: you can pause on every frame and see where every player is.",
          cue="soccer", pause=0.4),
        B("In Thonny, click Debug, the bug icon next to the green Run button.", cue="thonny", pause=0.3),
        B("The first line lights up.", cue="lights", pause=0.2),
        B("The highlighted line is the one that runs next.", cue="nexts", pause=0.3),
        B("Step over runs that line and stops at the next one.", cue="stepover", pause=0.3),
        B("Step into goes inside a function call, so you can watch its lines too.", cue="stepinto", pause=0.3),
        B("Turn on View, then Variables, to see every variable's value right now.", cue="variables", pause=0.3),
        B("And Stop, the red sign, ends the program.", cue="stop", pause=0.6),
    ), actions=(
        A("chip", "debugger = slow-motion replay", at="replay", until="thonny", x=960, y=200, color="orange",
          size=46),
        A("icons", at="soccer", until="thonny", x=960, y=520, gap=340,
          items=[("camera", "replay", "soccer"), ("clock", "pause any frame", "soccer@0.35"),
                 ("person", "see every player", "soccer@0.7")]),
        A("listrow", "Thonny toolbar", at="thonny", x=960, y=230, cell=250, size=34, indexes=False, items=TOOLBAR,
          highlight=[("thonny@0.6", "thonny@0.9", 0), ("thonny", "thonny@0.6", 1), ("thonny@0.9", "lights", 1),
                     ("stepover", "stepinto", 2), ("stepinto", "variables", 3), ("stop", "end", 5)]),
        A("chip", "Toolbar buttons work on every Mac (F-keys may need fn)", at="thonny@0.5", until="stepover",
          x=960, y=1000, color="white", size=30),
        A("chip", "Debug = slow motion (bug icon)", at="thonny@0.4", until="stepover", x=960, y=380, color="green",
          size=40),
        A("code", code=STARS, title="stars.py", x=100, y=460, w=860, h=330, shell=False, at="lights",
          highlight=[(1, "lights", "stepover@0.5"), (2, "stepover@0.5", "stop"), (3, "stop", "stop@0.5")]),
        A("chip", "highlight = the line that runs next", at="nexts", until="stepover", x=530, y=860, color="yellow",
          size=36),
        A("chip", "Step over: run this line, stop at next", at="stepover", until="stepinto", x=960, y=380,
          color="sky", size=40),
        A("chip", "Step into: go inside a function", at="stepinto", until="variables", x=960, y=380, color="purple",
          size=40),
        A("dict", "Variables", at="variables", x=1100, y=540, w=640,
          states=[("variables", [("stars", 2)])], highlight=[("variables@0.4", "stop", "stars")]),
        A("chip", "View > Variables", at="variables@0.2", x=1420, y=740, color="green", size=40),
        A("chip", "Stop (red sign) = end the program", at="stop", x=960, y=380, color="red", size=40),
    )),
    Scene("l3-w06-s03", setting="lavender", beats=(
        B("Let's try it on a tiny Robot class.", cue="tiny", pause=0.2),
        B("Its setup gives every robot a battery of fifty, and charge adds some power.", cue="setup", pause=0.3),
        B("At the bottom, Nova makes bolt and calls bolt dot charge twenty-five.", cue="bottom", pause=0.3),
        B("Nova clicks Debug, and the first line lights up.", cue="debug", pause=0.3),
        B("Step over, step over…", cue="steps", pause=0.3),
        B("In the Variables view, bolt appears.", cue="vars", pause=0.2),
        B("Click it, and the Object inspector shows its attributes: battery is fifty.", cue="inspect", pause=0.3),
        B("Now the highlighted line calls charge, one of our own methods.", cue="calls", pause=0.2),
        B("So Nova clicks Step into.", cue="into", pause=0.3),
        B("A small window opens.", cue="window", pause=0.2),
        B("That's normal: it shows the method's own variables, like power, which is twenty-five.", cue="normal",
          pause=0.3),
        B("Step over once more, and battery becomes seventy-five.", cue="once", pause=0.3),
        B("Back outside, print shows 75.", cue="print", pause=0.3),
        B("We watched every step!", cue="watched", pause=0.6),
    ), actions=(
        A("code", code=ROBOT, title="robot.py", x=60, y=170, w=970, h=760, size=30, shell_h=170, at="tiny",
          run="print@0.4", expect=["75"],
          highlight=[(4, "setup", "setup@0.5"), (6, "setup@0.5", "setup$"), (7, "setup@0.5", "setup$"),
                     (9, "bottom", "bottom@0.5"), (10, "bottom@0.5", "bottom$"),
                     (1, "debug@0.5", "steps"), (9, "steps", "steps@0.6"), (10, "steps@0.6", "into"),
                     (7, "into@0.5", "print"), (11, "print", "watched")]),
        A("chip", "Debug ▶ first line", at="debug@0.4", until="steps$", x=1420, y=230, color="green", size=38),
        A("dict", "Variables", at="vars", until="into", x=1090, y=290, w=740,
          states=[("vars", [("bolt", "Robot object")])], highlight=[("vars@0.3", "inspect$", "bolt")]),
        A("dict", "Object inspector: bolt", at="inspect", x=1090, y=560, w=740,
          states=[("inspect", [("name", "'Bolt'"), ("battery", 50)]), ("once@0.6", [("name", "'Bolt'"), ("battery", 75)])],
          highlight=[("inspect@0.6", "calls", "battery"), ("once@0.6", "print", "battery")]),
        A("chip", "bolt.battery → 50", at="inspect@0.7", until="into", x=1460, y=830, color="sky", size=40),
        A("chip", "Step into: inside charge(25)", at="into@0.4", until="once", x=1460, y=830, color="purple",
          size=38),
        A("dict", "charge window", at="window", until="print", x=1090, y=290, w=740,
          states=[("window", [("self", "bolt"), ("power", 25)])], highlight=[("normal@0.6", "once", "power")]),
        A("chip", "power 25 → battery 75", at="once@0.6", until="print", x=1460, y=830, color="orange", size=40),
        A("chip", "Shell: 75", at="print@0.6", x=1460, y=830, color="green", size=44),
        A("pixel", at="tiny", x=1790, y=170, s=0.35, ground=225, moods={"watched": "proud"},
          beep=[("steps", "steps$"), ("once", "once$")]),
        A("badge", ok=True, at="watched", x=1460, y=950),
    )),
    Scene("l3-w06-s04", setting="mint", beats=(
        B("Bug-hunt workshop!", cue="bug", pause=0.3),
        B("Nova wants to add up coins: 3, 4 and 5 should make 12.", cue="coins", pause=0.3),
        B("But the program prints 5.", cue="prints", pause=0.4),
        B("There's no red error this time, so let's use the bug-hunting loop.", cue="loop", pause=0.3),
        B("One, read: we expected 12, but got 5.", cue="read", pause=0.3),
        B("Two, predict:", cue="predict", pause=0.2),
        B("‘I think the total line is wrong,’", speaker=NOVA, cue="think", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("Three, watch: click Debug and step over.", cue="watch", pause=0.2),
        B("Total becomes 3, then jumps back to zero, then 4.", cue="total", pause=0.2),
        B("Then zero again!", cue="zero", pause=3.0),
        B("Aha!", cue="aha", pause=0.2),
        B("The line total equals zero is inside the loop, so it runs every time.", cue="inside", pause=0.3),
        B("Four, fix one thing: move that line above the loop.", cue="fix", pause=0.3),
        B("Five, check: run it.", cue="check", pause=0.3),
        B("12!", cue="twelve", pause=0.4),
        B("If it's still failing, go around the loop again.", cue="again", pause=0.3),
        B("Nice catch!", cue="nice", pause=0.6),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", code=COINS_BUG, title="coins.py", x=60, y=190, w=840, h=540, at="coins", until="fix",
          run="prints", expect=["5"],
          highlight=[(1, "watch@0.5", "total"), (2, "total", "total@0.15"), (3, "total@0.15", "total@0.35"),
                     (1, "total@0.35", "total@0.45"), (2, "total@0.45", "total@0.6"), (3, "total@0.6", "total$"),
                     (1, "zero", "zero@0.3"), (2, "zero@0.3", "zero$"), (3, "zero$", "aha"), (2, "aha", "fix")]),
        A("code", code=COINS_FIX, title="coins.py", x=60, y=190, w=840, h=540, at="fix", run="check@0.6",
          expect=["12"], highlight=[(1, "fix", "check")]),
        A("chip", "expected: 12", at="coins@0.6", x=680, y=850, color="green", size=40),
        A("badge", ok=False, at="prints@0.6", until="twelve", x=840, y=700),
        A("box", "total", x=250, y=870, at="watch", w=240,
          values=[("watch", "-"), ("total", 0), ("total@0.15", 3), ("total@0.45", 0), ("total@0.6", 4), ("zero@0.3", 0),
                  ("zero$+0.8", 5), ("fix", "-"), ("check@0.6", 12)]),
        A("cards", at="loop", x=1000, y=200, w=820, gap=106, size=36,
          items=["Read", "Predict", "Watch", "Fix ONE thing", "Check"],
          reveal=["loop@0.4", "loop@0.5", "loop@0.6", "loop@0.7", "loop@0.8"],
          active=[[("read", "predict"), ("again@0.2", "again@0.4")], [("predict", "watch"), ("again@0.4", "again@0.6")],
                  [("watch", "aha"), ("again@0.6", "again@0.8")], [("fix", "check"), ("again@0.8", "again$")],
                  [("check", "again"), ("again$", "nice")]],
          done=["predict", "watch", "fix", "check", "twelve"]),
        A("chip", "1 Read  2 Predict  3 Watch", at="loop@0.5", until="think", x=1410, y=820, color="sky", size=38),
        A("chip", "4 Fix ONE thing  5 Check", at="loop@0.8", until="think", x=1410, y=920, color="sky", size=38),
        A("bubble", "I think the total line is wrong!", at="think", until="watch", x=1760, y=880, tail="down-right",
          size=34),
        A("thought", "", at="zero$+0.3", until="aha", x=1410, y=940),
        A("chip", "total = 0 is inside the loop!", at="inside@0.3", until="fix", x=1410, y=870, color="red", size=38),
        A("badge", ok=True, at="twelve", x=840, y=700),
        A("chip", "Still failing? Go around again", at="again", until="nice", x=1410, y=870, color="yellow", size=36),
        A("confetti", at="nice", x=1410, y=500),
        A("nova", x=1800, y=1060, s=0.42, moods={"prints": "confused", "think": "thinking", "aha": "surprised",
                                                 "twelve": "proud"}),
    )),
    Scene("l3-w06-s05", setting="workshop", tail=0.8, beats=(
        B("Checkpoint reached!", cue="reached", pause=0.3),
        B("A debugger is a slow-motion replay.", cue="replay", pause=0.2),
        B("Debug starts it, Step over runs one line, Step into goes inside your method, and the Variables view "
          "shows every value.", cue="buttons", pause=0.3),
        B("When a bug appears: read, predict, watch, fix one thing, and check.", cue="loop", pause=0.4),
        B("Now, a secret: every programmer meets bugs every day.", cue="secret", pause=0.3),
        B("Bugs are how we learn!", cue="learn", pause=0.4),
        B("If you get stuck, ask for help clearly: what I expected, what happened, what I tried.", cue="help",
          pause=0.3),
        B("That's a skill, not a weakness.", cue="skill", pause=0.3),
        B("And be kind when a partner's code is broken.", cue="kind", pause=0.4),
        B("Now open Bug Hunt 1, Score Keeper.", cue="next", pause=0.2),
        B("Run it, read the last line of the error, and debug one fix at a time.", cue="run", pause=0.3),
        B("Happy hunting!", cue="happy", pause=0.6),
    ), actions=(
        A("door", "DOOR 6", x=1660, y=920, open="reached"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "replay"), ("learn", "learn$"), ("happy", "end")],
          moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud", "learn": "happy"},
          beep=("learn", "learn$")),
        A("chip", "debugger = slow-motion replay", at="replay", until="secret", x=1000, y=240, color="orange",
          size=44),
        A("listrow", "", at="buttons", until="secret", x=1000, y=420, cell=230, size=32, indexes=False,
          items=["Debug", "Step over", "Step into", "Variables"],
          highlight=[("buttons", "buttons@0.2", 0), ("buttons@0.2", "buttons@0.45", 1),
                     ("buttons@0.45", "buttons@0.7", 2), ("buttons@0.7", "buttons$", 3)]),
        A("chip", "Read • Predict • Watch • Fix • Check", at="loop", until="secret", x=1000, y=620, color="sky",
          size=42),
        A("chip", "Bugs are how we learn", at="learn", until="next", x=1000, y=240, color="green", size=46),
        A("panel", "Ask for help clearly", at="help", until="next", x=640, y=330, w=760,
          items=[("help@0.45", "I expected…"), ("help@0.65", "but … happened."), ("help@0.85", "I tried…")]),
        A("chip", "a skill, not a weakness", at="skill", until="next", x=1020, y=700, color="yellow", size=40),
        A("icons", at="kind", until="next", x=1020, y=860, items=[("heart", "be kind", "kind@0.3")]),
        A("banner", "NEXT: Bug Hunt 1: Score Keeper", at="next", color="green"),
        A("cards", at="next", x=620, y=230, w=780, gap=110,
          items=["Press Run", "Read the error's last line", "Debug: step and watch", "Fix one bug, run again"],
          reveal=["next@0.5", "run@0.2", "run@0.55", "run@0.8"]),
        A("chip", "Happy hunting!", at="happy", x=1000, y=760, color="orange", size=48),
    )),
))
