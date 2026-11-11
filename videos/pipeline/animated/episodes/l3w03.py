"""Level 3 Week 3: Families of Objects (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, Scene

COPIED = '''class Robot:
    def move(self):
        self.x = self.x + 1

class PaintBot:
    def move(self):
        self.x = self.x + 1

class DanceBot:
    def move(self):
        self.x = self.x + 1
'''

ROBOT = '''class Robot:
    def __init__(self, name, x=0):
        self.name = name
        self.x = x
    def move(self):
        self.x = self.x + 1
'''

PAINTBOT = '''class PaintBot(Robot):
    def __init__(self, name, x=0, color="blue"):
        super().__init__(name, x)
        self.color = color

    def move(self):
        super().move()
        print(self.name, "paints a", self.color, "dot")

juno = PaintBot("Juno", color="green")
juno.move()
'''

BUG1 = '''class PaintBot(Robot):
    def __init__(self, name, x=0, color="blue"):
        self.color = color

    def moove(self):
        super().move()
        print(self.name, "paints a", self.color, "dot")

juno = PaintBot("Juno", color="green")
juno.move()
'''
BUG2 = BUG1.replace('        self.color = color\n', '        super().__init__(name, x)\n        self.color = color\n')
FIXED = BUG2.replace("def moove", "def move")

EPISODE = Episode(level=3, week=3, scenes=(
    Scene("l3-w03-s01", setting="workshop", lead_in=0.2, beats=(
        B("Nova's robot workshop is growing.", cue="growing", pause=0.3),
        B("There's a plain Robot that rolls one step at a time.", cue="plain", pause=0.3),
        B("Now Nova wants a PaintBot that rolls and paints, and lots more kinds after that.", cue="paintbot",
          pause=0.3),
        B("‘Do I have to copy the whole Robot class every time?’", speaker=NOVA, cue="ask", pause=0.1),
        B("asks Nova.", cue="asks", pause=0.3),
        B("Pixel holds up a family tree.", cue="tree", pause=0.3),
        B("What if robots could have families?", cue="question", pause=3.0),
    ), actions=(
        A("nova", x=300, y=960, enter="left", moods={"growing": "happy", "ask": "worried", "tree": "surprised",
                                                     "question": "thinking"}, chin=("question", "end")),
        A("pixel", x=620, y=760, drop=True, moods={"tree": "proud"}, carrying=("tree", "end")),
        A("banner", "MISSION: A family of robots", at="growing"),
        A("panel", "Robot", at="plain", until="ask", x=860, y=220, w=440, items=[("plain@0.4", "rolls 1 step")]),
        A("pixel", at="plain", until="ask", x=1000, y=800, s=0.35, ground=870, label="Robot",
          path=[("plain@0.3", 1000, 800), ("plain@0.5", 1080, 800), ("plain@0.7", 1080, 800),
                ("plain@0.9", 1160, 800)]),
        A("panel", "PaintBot", at="paintbot", until="ask", x=1360, y=220, w=460,
          items=[("paintbot@0.3", "rolls 1 step"), ("paintbot@0.5", "paints"), ("paintbot@0.8", "…and more kinds")]),
        A("code", code=COPIED, title="robots.py", x=860, y=190, w=960, h=660, size=32, shell=False, at="ask",
          until="tree", highlight=[(2, "ask@0.3", "tree"), (3, "ask@0.3", "tree"), (6, "ask@0.5", "tree"),
                                   (7, "ask@0.5", "tree"), (10, "ask@0.7", "tree"), (11, "ask@0.7", "tree")]),
        A("chip", "copy, copy, copy…", at="ask@0.4", until="tree", x=1340, y=930, color="red"),
        A("tree", at="tree", x=1340, y=220, gap=420, w=360, level_gap=280,
          nodes=[("Robot", None, ["rolls"], "tree"), ("PaintBot", "Robot", ["+ paints"], "tree@0.4"),
                 ("???", "Robot", ["+ ?"], "tree@0.7")]),
        A("chip", "Pause: What do all robots share?", at="question", x=1340, y=780, color="yellow", size=40),
        A("thought", "", at="question$+0.3", until="end", x=640, y=360),
    )),
    Scene("l3-w03-s02", setting="sky", beats=(
        B("They can!", cue="can", pause=0.2),
        B("A child class inherits everything from its parent class: all its attributes and methods.",
          cue="inherits", pause=0.3),
        B("Then it changes only what is different.", cue="changes", pause=0.4),
        B("Think of Grandma's pancake recipe.", cue="pancake", pause=0.3),
        B("Your recipe says: make Grandma's pancakes, then add blueberries.", cue="blue", pause=0.3),
        B("You don't copy her whole recipe.", cue="dont", pause=0.2),
        B("You use it and add one thing.", cue="use", pause=0.4),
        B("Changing a method in the child is called overriding.", cue="override", pause=0.3),
        B("And super means ‘my parent.’", cue="super", pause=0.4),
        B("One more way to build: a Workshop isn't a kind of Robot, but a Workshop has Robots.", cue="workshop",
          pause=0.3),
        B("That's composition.", cue="comp", pause=0.3),
        B("Say the sentence aloud.", cue="say", pause=0.4),
        B("Is a means inheritance.", cue="isa", pause=0.3),
        B("Has a means composition.", cue="hasa", pause=0.8),
    ), actions=(
        A("tree", at="inherits", until="pancake", x=960, y=170, gap=520, w=420, level_gap=330,
          nodes=[("Robot", None, ["name, x, move()"], "inherits"),
                 ("PaintBot", "Robot", ["(everything from Robot)", "+ color"], "inherits@0.5"),
                 ("?", "Robot", ["(everything from Robot)", "+ ?"], "changes")]),
        A("chip", "parent", at="inherits@0.2", until="pancake", x=1360, y=230, color="purple", size=36),
        A("chip", "child", at="inherits@0.6", until="pancake", x=440, y=455, color="purple", size=36),
        A("chip", "class PaintBot(Robot):  → is a", at="changes", until="pancake", x=960, y=850, color="orange",
          size=44),
        A("panel", "Grandma's pancakes", at="pancake", until="override", x=140, y=260, w=760,
          items=[("pancake@0.3", "flour, eggs, milk"), ("pancake@0.6", "mix and cook")]),
        A("panel", "My pancakes", at="blue", until="override", x=1020, y=260, w=760,
          items=[("blue@0.3", "make Grandma's pancakes"), ("blue@0.7", "+ blueberries")]),
        A("chip", "Don't copy: use it + add one thing", at="dont", until="override", x=960, y=700, color="green"),
        A("tree", at="override", until="workshop", x=820, y=200, w=440, level_gap=300,
          nodes=[("Robot", None, ["move()"], "override"), ("PaintBot", "Robot", ["move()  ← override"], "override@0.3")]),
        A("arrow", at="super", until="workshop", x1=1160, y1=560, x2=1160, y2=270, color="#6B4FC2"),
        A("chip", "super()", at="super+0.3", until="workshop", x=1290, y=415, color="purple", size=36),
        A("chip", "override = change a method in the child", at="override@0.5", until="workshop", x=960, y=780,
          color="sky"),
        A("chip", "super() = “my parent”", at="super@0.4", until="workshop", x=960, y=900, color="purple", size=46),
        A("panel", "Workshop", at="workshop@0.3", x=1060, y=230, w=700,
          items=[("workshop@0.6", "has a Robot"), ("workshop@0.8", "has a PaintBot")]),
        A("tree", at="say", x=520, y=230, w=340, level_gap=260,
          nodes=[("Robot", None, [], "say"), ("PaintBot", "Robot", ["is a Robot"], "say@0.3")]),
        A("chip", "is a → inheritance", at="isa", x=520, y=760, color="orange", size=46),
        A("chip", "has a → composition", at="hasa", x=1410, y=760, color="green", size=46),
    )),
    Scene("l3-w03-s03", setting="lavender", beats=(
        B("Here's the parent class, Robot.", cue="parent", pause=0.2),
        B("Its setup saves a name and an x position, and move adds one to x.", cue="setup", pause=0.3),
        B("Now the child class, PaintBot, with Robot in parentheses.", cue="child", pause=0.2),
        B("That means a PaintBot is a Robot.", cue="isa", pause=0.3),
        B("PaintBot's __init__ starts by calling super, so the parent sets up the name and x.", cue="superinit", pause=0.2),
        B("‘Parent, set up your part!’", speaker=NOVA, cue="yourpart", pause=0.1),
        B("says Nova.", cue="says", pause=0.2),
        B("Then the child adds its extra: a color.", cue="extra", pause=0.3),
        B("PaintBot also overrides move.", cue="overrides", pause=0.2),
        B("First, super runs the parent's move.", cue="supermove", pause=0.2),
        B("Then it adds its own part: a paint message.", cue="paint", pause=0.3),
        B("Nova makes a green PaintBot named Juno.", cue="juno", pause=0.2),
        B("Pixel tells Juno to move.", cue="runs", pause=0.2),
        B("Predict!", cue="predict", pause=2.6),
        B("x becomes one,", cue="xone", pause=0.2),
        B("and it prints: Juno paints a green dot.", cue="prints", pause=0.4),
        B("A plain Robot and a PaintBot both understand move, but each does it its own way.", cue="both", pause=0.3),
        B("That's polymorphism: many shapes.", cue="poly", pause=0.6),
    ), actions=(
        A("code", code=ROBOT, title="robot.py", x=60, y=170, w=700, h=370, size=27, shell=False, at="parent",
          highlight=[(2, "setup", "setup@0.5"), (3, "setup", "setup@0.5"), (4, "setup", "setup@0.5"),
                     (5, "setup@0.5", "setup$"), (6, "setup@0.5", "setup$"), (5, "supermove", "supermove$"),
                     (2, "superinit", "yourpart$")]),
        A("code", code=PAINTBOT, exec=ROBOT + "\n" + PAINTBOT, title="paintbot.py", x=790, y=170, w=1065, h=740,
          size=27, shell_h=170, at="child",
          reveal=["child", "superinit", "superinit@0.4", "extra", "overrides", "overrides", "supermove", "paint",
                  "juno", "juno", "runs"],
          highlight=[(1, "child", "isa$"), (3, "superinit@0.4", "says$"), (4, "extra", "extra$"),
                     (6, "overrides", "overrides$"), (7, "supermove", "supermove$"), (8, "paint", "paint$"),
                     (11, "runs", "prints$")],
          run="prints", expect=["Juno paints a green dot"]),
        A("chip", "PaintBot is a Robot", at="isa", until="superinit", x=1322, y=975, color="orange"),
        A("chip", "super().__init__(name, x)", at="superinit@0.4", until="supermove", x=1322, y=975, color="purple"),
        A("chip", "super().move()", at="supermove@0.3", until="prints", x=1322, y=975, color="purple"),
        A("chip", "Shell: Juno paints a green dot", at="prints@0.4", until="poly", x=1322, y=975, color="green"),
        A("chip", "polymorphism = many shapes", at="poly", x=1322, y=975, color="orange"),
        A("nova", x=170, y=1010, s=0.55, moods={"parent": "happy", "predict": "thinking", "prints": "proud"}),
        A("bubble", "Parent, set up your part!", at="yourpart", until="extra", x=220, y=650, size=34),
        A("thought", "", at="predict+0.3", until="xone", x=520, y=700),
        A("box", "juno.x", x=560, y=670, at="xone", values=[("xone", 0), ("xone@0.5", 1)]),
        A("pixel", at="both", x=420, y=880, s=0.3, ground=940, label="Robot",
          path=[("both@0.2", 420, 880), ("both@0.5", 470, 880)]),
        A("pixel", at="both@0.3", x=640, y=880, s=0.3, ground=940, label="Juno",
          path=[("both@0.5", 640, 880), ("both@0.8", 690, 880)], beep=("both@0.8", "end")),
    )),
    Scene("l3-w03-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Nova makes a quick copy of PaintBot, and it has two family bugs.", cue="copy", pause=0.3),
        B("Bug one: the child's setup forgot the line that calls super.", cue="one", pause=0.2),
        B("It only saves the color.", cue="only", pause=0.3),
        B("Pixel tells Juno to move and gets AttributeError: ‘PaintBot’ object has no attribute ‘x’.", cue="runs",
          pause=0.3),
        B("Read it from the bottom up.", cue="read", pause=0.2),
        B("No x?", cue="nox", pause=2.8),
        B("The parent's setup never ran!", cue="never", pause=0.3),
        B("Test one change: put the super line back.", cue="test", pause=0.2),
        B("Run again.", cue="again", pause=0.4),
        B("No crash!", cue="nocrash", pause=0.3),
        B("But wait…", cue="butwait", pause=0.3),
        B("Juno rolls and never paints.", cue="rolls", pause=0.3),
        B("No error at all.", cue="noerror", pause=0.2),
        B("That's a silent bug.", cue="silent", pause=2.8),
        B("Look closely at the method's name: m, o, o, v, e.", cue="look", pause=0.2),
        B("Moove!", cue="moove", pause=0.3),
        B("That doesn't match, so Python used the parent's move.", cue="match", pause=0.4),
        B("Fix the spelling and test.", cue="fix", pause=0.4),
        B("Override names must match exactly.", cue="exact", pause=0.6),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", code=BUG1, exec=ROBOT + "\n" + BUG1, title="paintbot.py", x=60, y=190, w=1080, h=730, size=28,
          shell_h=170, at="copy", until="test", run="runs@0.3", allow_error=True, error_line=10,
          expect=["AttributeError: 'PaintBot' object has no attribute 'x'"],
          highlight=[(2, "one", "only"), (3, "only", "only$"), (3, "never", "test")]),
        A("code", code=BUG2, exec=ROBOT + "\n" + BUG2, title="paintbot.py", x=60, y=190, w=1080, h=730, size=28,
          shell_h=170, at="test", until="fix", run="again", expect=[],
          highlight=[(3, "test", "again"), (6, "silent", "match$")]),
        A("code", code=FIXED, exec=ROBOT + "\n" + FIXED, title="paintbot.py", x=60, y=190, w=1080, h=730, size=28,
          shell_h=170, at="fix", run="fix@0.6", expect=["Juno paints a green dot"], highlight=[(6, "fix", "fix@0.6")]),
        A("chip", "AttributeError: ... no attribute 'x'", at="runs@0.5", until="test", x=1510, y=260, color="red",
          size=32),
        A("thought", "", at="nox+0.3", until="nox>", x=1510, y=520),
        A("tree", at="never", until="test", x=1510, y=360, w=420, level_gap=240,
          nodes=[("Robot", None, ["setup never ran"], "never"), ("PaintBot", "Robot", ["only saves color"], "never@0.3")]),
        A("badge", ok=True, at="nocrash", until="butwait", x=1510, y=480),
        A("pixel", at="rolls", until="look", x=1400, y=500, s=0.35, ground=570, label="Juno",
          path=[("rolls@0.2", 1400, 500), ("rolls$", 1600, 500)], moods={"noerror": "confused"}),
        A("chip", "no paint, no error", at="noerror", until="look", x=1510, y=760, color="yellow", size=36),
        A("chip", "def moove(self):   # silent bug!", at="silent", until="fix", x=1510, y=260, color="yellow",
          size=34),
        A("thought", "", at="silent+0.3", until="silent>", x=1510, y=900),
        A("listrow", "moove", at="look", until="fix", x=1510, y=500, cell=100, indexes=False,
          items=["m", "o", "o", "v", "e"],
          highlight=[("look@0.55", "look@0.65", 0), ("look@0.65", "look@0.75", 1), ("look@0.75", "match$", 2),
                     ("look@0.85", "look@0.92", 3), ("look@0.92", "look$", 4)]),
        A("listrow", "move (parent)", at="moove", until="fix", x=1510, y=740, cell=100, indexes=False,
          items=["m", "o", "v", "e"], color="green"),
        A("badge", ok=True, at="fix@0.6+0.6", x=1510, y=480),
        A("confetti", at="fix@0.6+0.6", x=1510, y=420),
        A("chip", "Override names must match exactly", at="exact", x=600, y=980, color="green", size=40),
        A("pixel", x=1780, y=880, s=0.4, ground=960, beep=[("runs", "runs$"), ("again", "again$")],
          moods={"runs": "confused", "fix": "proud"}),
    )),
    Scene("l3-w03-s05", setting="workshop", tail=0.8, beats=(
        B("Family reunion!", cue="reunion", pause=0.3),
        B("A child class inherits from its parent and changes only what is different.", cue="child", pause=0.3),
        B("super runs the parent's part.", cue="super", pause=0.3),
        B("Overriding replaces a method, so the same call can do different things.", cue="override", pause=0.3),
        B("That's polymorphism.", cue="poly", pause=0.3),
        B("And has a means composition.", cue="hasa", pause=0.4),
        B("Now, a question for game makers: who gets to be the hero?", cue="hero", pause=1.8),
        B("When you design a character family, include many kinds of people: different names, skin tones, ages and "
          "abilities.", cue="include", pause=0.3),
        B("Don't make one group always the villain or always the helper.", cue="dont", pause=0.4),
        B("Now open Enemy Family.", cue="next", pause=0.2),
        B("Finish the Zigzagger, the Sprinter and move all.", cue="finish", pause=0.3),
        B("Then press Run.", cue="run", pause=0.3),
        B("Does every enemy move its own way?", cue="goal", pause=0.8),
    ), actions=(
        A("door", "DOOR 3", x=1660, y=920, open="reunion"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "child"), ("goal", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "Child(Parent) • super() • override", at="child", until="hero", x=1000, y=240, color="orange",
          size=44),
        A("tree", at="child", until="hero", x=1000, y=330, w=360, level_gap=230,
          nodes=[("Robot", None, ["move()"], "child"), ("PaintBot", "Robot", ["move() + paint"], "child@0.4")]),
        A("arrow", at="super", until="hero", x1=1260, y1=600, x2=1260, y2=380, color="#6B4FC2"),
        A("chip", "super()", at="super+0.3", until="hero", x=1390, y=490, color="purple", size=34),
        A("chip", "polymorphism = same call, own way", at="poly", until="hero", x=1000, y=780, color="sky"),
        A("chip", "has a → composition", at="hasa", until="hero", x=1000, y=890, color="green"),
        A("chip", "Heroes of every kind", at="hero", until="next", x=1000, y=240, color="green", size=46),
        A("icons", at="include", until="next", x=1020, y=500, gap=250,
          items=[("person", "names", "include@0.4"), ("heart", "skin tones", "include@0.55"),
                 ("grownup", "ages", "include@0.75"), ("star", "abilities", "include@0.9")]),
        A("grownup", at="include", until="next", x=1380, y=990, s=0.55),
        A("cat", at="include@0.5", until="next", x=760, y=990, s=0.6),
        A("chip", "Not always the villain or the helper", at="dont", until="next", x=1000, y=780, color="yellow"),
        A("banner", "NEXT: Enemy Family", at="next", color="green"),
        A("cards", at="next", x=620, y=230, w=760, gap=110,
          items=["Finish the Zigzagger", "Finish the Sprinter", "Finish move_all", "Press Run"],
          reveal=["finish", "finish@0.4", "finish@0.75", "run"]),
        A("chip", "Does every enemy move its own way?", at="goal", x=1000, y=760, color="yellow", size=44),
    )),
))
