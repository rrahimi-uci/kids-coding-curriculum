"""Level 3 Week 2: Blueprints and Objects (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, Scene

COPIES = "\n".join(f"plant{i}_height = 1\nplant{i}_grow = 1" for i in range(1, 5))
LATER = "\n".join(f"plant{i}_height = 1\nplant{i}_grow = 1" for i in range(47, 51))

PLANT = '''class Plant:
    def __init__(self, name):
        self.name = name
        self.height = 1

    def water(self):
        self.height = self.height + 3

sunny = Plant("Sunny")
fern = Plant("Fern")
sunny.water()
'''

BUG = '''class Plant:
    def __init__(self, name):
        self.name = name
        self.height = 1

    def water({param}):
        {left} = {right} + 3

sunny = Plant("Sunny")
sunny.water()
'''
BUG1 = BUG.format(param="", left="height", right="height")
BUG2 = BUG.format(param="self", left="height", right="height")
FIXED = BUG.format(param="self", left="self.height", right="self.height") + "print(sunny.height)\n"

EPISODE = Episode(level=3, week=2, scenes=(
    Scene("l3-w02-s01", setting="workshop", lead_in=0.2, beats=(
        B("Nova wants a garden game with lots and lots of plants.", cue="garden", pause=0.3),
        B("‘I'll write the code for one plant,’", speaker=NOVA, cue="one", pause=0.1),
        B("says Nova,", cue="says", pause=0.1),
        B("‘then copy it… and copy it… and copy it.’", speaker=NOVA, cue="copy", pause=0.3),
        B("Nova starts copying.", cue="starts", pause=0.3),
        B("Fifty copies later, Nova wants plants to grow faster.", cue="fifty", pause=0.3),
        B("Uh-oh.", cue="uhoh", pause=0.2),
        B("That's fifty changes!", cue="changes", pause=0.3),
        B("Can we write the plan once and build as many plants as we like?", cue="question", pause=3.0),
    ), actions=(
        A("nova", x=300, y=960, enter="left", moods={"garden": "happy", "uhoh": "surprised", "question": "thinking"},
          chin=("question", "end")),
        A("pixel", x=620, y=760, drop=True, moods={"uhoh": "confused"}),
        A("banner", "MISSION: One plan, many plants", at="garden"),
        A("code", code=COPIES, title="garden.py", x=860, y=190, w=960, h=520, shell=False, at="one",
          until="fifty", reveal=["one@0.3", "one@0.6", "copy", "copy@0.15", "copy@0.45", "copy@0.6",
                                 "copy@0.85", "copy$"]),
        A("code", code=LATER, title="garden.py", x=860, y=190, w=960, h=520, shell=False, at="fifty",
          until="question", highlight=[(2, "changes", "question"), (4, "changes@0.15", "question"),
                                       (6, "changes@0.3", "question"), (8, "changes@0.45", "question")]),
        A("box", "copies", x=1340, y=860, at="one@0.3",
          values=[("one@0.3", 1), ("copy@0.4", 2), ("copy$", 4), ("starts", 12), ("starts@0.5", 30), ("fifty", 50)]),
        A("chip", "50 changes!", at="changes", until="question", x=1700, y=860, color="red"),
        A("chip", "Pause: How could we avoid 50 copies?", at="question", x=1300, y=420, color="yellow", size=40),
        A("thought", "", at="question$+0.3", until="end", x=640, y=360),
    )),
    Scene("l3-w02-s02", setting="sky", beats=(
        B("We can!", cue="can", pause=0.2),
        B("Think of a cookie cutter.", cue="cutter", pause=0.3),
        B("One cutter makes lots of cookies, and each cookie can have its own sprinkles and flavor.", cue="cookies",
          pause=0.4),
        B("In Python, the cutter is a class: a blueprint.", cue="class", pause=0.3),
        B("Each cookie is an object: one thing built from the blueprint.", cue="object", pause=0.4),
        B("The facts an object remembers are called attributes, like a plant's height.", cue="attr", pause=0.3),
        B("The actions it can do are methods: functions that live inside the class.", cue="methods", pause=0.4),
        B("The setup method has a funny name: __init__.", cue="dunder", pause=0.3),
        B("That's two underscores, init, two underscores.", cue="underscores", pause=0.3),
        B("It runs once, every time a new object is made.", cue="once", pause=0.4),
        B("Pause and point: is the cookie cutter the class or the object?", cue="point", pause=3.2),
    ), actions=(
        A("tree", at="cutter", until="attr", x=960, y=170, gap=470, w=400, level_gap=290,
          nodes=[("cutter", None, ["one star shape"], "cutter"),
                 ("cookie 1", "cutter", ["sprinkles: pink", "flavor: lemon"], "cookies@0.2"),
                 ("cookie 2", "cutter", ["sprinkles: blue", "flavor: honey"], "cookies@0.45"),
                 ("cookie 3", "cutter", ["sprinkles: none", "flavor: mint"], "cookies@0.7")]),
        A("chip", "class = blueprint (cookie cutter)", at="class", until="attr", x=960, y=800, color="orange", size=44),
        A("chip", "object = one thing built from it", at="object", until="attr", x=960, y=920, color="green", size=44),
        A("panel", "class Plant", at="attr", x=120, y=220, w=620,
          items=[("attr@0.5", "attribute: height"), ("methods@0.4", "method: water()"),
                 ("dunder@0.6", "setup: dunder init")]),
        A("chip", "attribute = a fact • method = an action", at="methods@0.5", x=1290, y=260, color="sky"),
        A("listrow", "dunder init", at="underscores", x=1290, y=520, cell=120, indexes=False,
          items=["_", "_", "init", "_", "_"],
          highlight=[("underscores+0.2", "underscores@0.3", 0), ("underscores+0.2", "underscores@0.3", 1),
                     ("underscores@0.35", "underscores@0.6", 2), ("underscores@0.65", "underscores$", 3),
                     ("underscores@0.65", "underscores$", 4)]),
        A("chip", "__init__ = setup (dunder init)", at="once", x=1290, y=730, color="orange"),
        A("chip", "runs once per new object", at="once@0.4", x=1290, y=840, color="white", size=36),
        A("thought", "Class or object?", at="point+0.3", until="end", x=440, y=820),
    )),
    Scene("l3-w02-s03", setting="lavender", beats=(
        B("Let's build a Plant class.", cue="build", pause=0.2),
        B("It starts with class Plant.", cue="classline", pause=0.2),
        B("Inside, the __init__ method takes self and a name.", cue="init", pause=0.2),
        B("It stores self.name and sets self.height to one.", cue="saves", pause=0.3),
        B("Then comes a method called water, which also takes self.", cue="water", pause=0.2),
        B("It adds three to self.height.", cue="plus", pause=0.3),
        B("So what's self?", cue="what", pause=1.4),
        B("Self means ‘my.’", cue="my", pause=0.2),
        B("So self.height means ‘my height.’", cue="myheight", pause=0.2),
        B("And Python fills in self for you.", cue="fills", pause=0.4),
        B("Now Nova makes two plants: one called Sunny, and one called Fern.", cue="two",
          pause=0.3),
        B("Pixel runs the last line, which waters Sunny.", cue="runs", pause=0.2),
        B("Predict!", cue="predict", pause=3.0),
        B("How tall is Sunny now?", cue="tall", pause=0.8),
        B("Four.", cue="four", pause=0.4),
        B("And Fern?", cue="andfern", pause=0.8),
        B("Still one!", cue="one", pause=0.3),
        B("Nothing happened to Fern.", cue="nothing", pause=0.2),
        B("Watering Sunny only changed Sunny.", cue="only", pause=0.3),
        B("Same blueprint, different objects, and each one keeps its own numbers.", cue="same", pause=0.6),
    ), actions=(
        A("code", code=PLANT, title="garden.py", x=70, y=180, w=900, h=650, size=32, shell=False, at="build",
          reveal=["classline", "init", "saves", "saves@0.5", "water", "water", "plus", "two", "two@0.45",
                  "two@0.85", "runs"],
          highlight=[(2, "init", "init$"), (7, "myheight", "fills$"), (3, "fills", "fills$"), (4, "fills", "fills$"),
                     (11, "runs", "one$")]),
        A("chip", "self means “my”", at="my", x=520, y=930, color="pink", size=46),
        A("tree", at="classline", x=1420, y=180, gap=420, w=360, level_gap=300,
          nodes=[("Plant", None, ["the blueprint"], "classline"), ("sunny", "Plant", ["name: Sunny"], "two@0.55"),
                 ("fern", "Plant", ["name: Fern"], "two@0.9")]),
        A("box", "sunny.height", x=1210, y=730, w=300, at="two@0.6", values=[("two@0.6", 1), ("four", 4)]),
        A("box", "fern.height", x=1630, y=730, w=300, at="two@0.95", values=[("two@0.95", 1)]),
        A("thought", "", at="predict+0.3", until="four", x=1420, y=960),
        A("chip", "sunny.height → 4", at="four", x=1210, y=920, color="green", size=38),
        A("chip", "fern.height → 1", at="one", x=1630, y=920, color="sky", size=38),
        A("pixel", x=1790, y=330, s=0.42, ground=410, beep=("runs", "runs$"), moods={"one": "happy"}),
    )),
    Scene("l3-w02-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Nova writes a new version of water, but forgets something.", cue="forgets", pause=0.3),
        B("The new water method has empty parentheses.", cue="empty", pause=0.2),
        B("Inside, it adds three to height.", cue="inside", pause=0.3),
        B("Pixel waters Sunny and gets a red error.", cue="runs", pause=0.4),
        B("Let's read it from the bottom up.", cue="read", pause=0.2),
        B("TypeError: Plant.water() takes 0 positional arguments but 1 was given.", cue="typeerror",
          pause=0.3),
        B("Hmm.", cue="hmm", pause=1.0),
        B("Python tried to hand the plant to the method, but there was no self to catch it!", cue="hand", pause=0.4),
        B("Guess, and test one change: put self in the parentheses.", cue="guess", pause=0.3),
        B("Run again.", cue="again", pause=0.4),
        B("A new error: UnboundLocalError.", cue="unbound", pause=0.3),
        B("Ask: whose height?", cue="whose", pause=3.2),
        B("Not the plant's!", cue="notplant", pause=0.3),
        B("Change one more thing: write self.height on both sides.", cue="change", pause=0.3),
        B("Run it.", cue="runit", pause=0.4),
        B("Sunny grows!", cue="grows", pause=0.3),
        B("Every method needs self first.", cue="every", pause=0.6),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", code=BUG1, title="garden.py", x=60, y=190, w=1000, h=760, size=30, shell_h=170, at="forgets",
          until="guess", run="runs@0.5", allow_error=True, error_line=6,
          expect=["TypeError: Plant.water() takes 0 positional arguments but 1 was given"],
          highlight=[(6, "empty", "empty$"), (7, "inside", "inside$"), (6, "hand", "guess")]),
        A("code", code=BUG2, title="garden.py", x=60, y=190, w=1000, h=760, size=30, shell_h=170, at="guess",
          until="change", run="again", allow_error=True, error_line=7,
          expect=["UnboundLocalError: local variable 'height' referenced before assignment"],
          highlight=[(6, "guess", "guess$"), (7, "whose", "change")]),
        A("code", code=FIXED, title="garden.py", x=60, y=190, w=1000, h=760, size=30, shell_h=170, at="change",
          run="runit", expect=["4"], highlight=[(7, "change", "runit")]),
        A("pointer", at="read", until="hand", x=1000, y=900, s=0.7),
        A("chip", "TypeError: ... 0 positional arguments", at="typeerror", until="guess", x=1470, y=300,
          color="red", size=34),
        A("chip", "def water():   # forgot self!", at="hand", until="again", x=1470, y=420, color="yellow", size=36),
        A("chip", "Read → find the line → guess → test", at="guess", until="every", x=1470, y=300, color="sky",
          size=34),
        A("thought", "Whose height?", at="whose+0.3", until="whose>", x=1470, y=700),
        A("chip", "Whose height? → self.height", at="change", x=1470, y=540, color="green", size=36),
        A("badge", ok=False, at="runs@0.8", until="guess", x=1700, y=680),
        A("badge", ok=False, at="unbound", until="change", x=1700, y=850),
        A("badge", ok=True, at="grows", x=1700, y=680),
        A("bigtext", "Every method needs self first", at="every", x=1470, y=840, size=40, color="purple"),
        A("nova", x=1830, y=1060, s=0.45, moods={"forgets": "happy", "runs": "confused", "whose": "thinking",
                                                 "grows": "proud"}),
    )),
    Scene("l3-w02-s05", setting="workshop", tail=0.8, beats=(
        B("Blueprint built!", cue="built", pause=0.3),
        B("A class is a blueprint.", cue="class", pause=0.2),
        B("Objects are the things you build from it, and each one keeps its own attributes.", cue="objects",
          pause=0.3),
        B("Methods are actions, and self means ‘my.’", cue="self", pause=0.4),
        B("Now, a design question.", cue="design", pause=0.2),
        B("Some pet apps say, ‘Your pet is sad. You forgot it!’", cue="sad", pause=0.3),
        B("How does that make players feel?", cue="feel", pause=1.8),
        B("Our pets never get sick, never run away, and never make you feel guilty.", cue="never", pause=0.3),
        B("They never need money or daily streaks, either.", cue="money", pause=0.3),
        B("Programmers choose how their games treat people.", cue="choose", pause=0.4),
        B("Now open Pet Class.", cue="next", pause=0.2),
        B("Finish play, mood and describe.", cue="finish", pause=0.3),
        B("Then press Run and play with Pip.", cue="run", pause=0.3),
        B("Does Bo change too?", cue="bo", pause=0.8),
        B("Find out!", cue="find", pause=0.6),
    ), actions=(
        A("door", "DOOR 2", x=1660, y=920, open="built"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "class"), ("find", "end")],
          moods={"start": "proud", "sad": "worried", "never": "happy"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud", "sad": "confused", "never": "happy"}),
        A("chip", "class → many objects", at="class", until="design", x=1000, y=240, color="orange", size=46),
        A("tree", at="objects", until="design", x=1000, y=340, gap=330, w=300, level_gap=220,
          nodes=[("Plant", None, ["blueprint"], "objects"), ("sunny", "Plant", ["height 4"], "objects@0.3"),
                 ("fern", "Plant", ["height 1"], "objects@0.5")]),
        A("chip", "self means “my”", at="self@0.4", until="design", x=1000, y=860, color="pink", size=44),
        A("bubble", "Your pet is sad. You forgot it!", at="sad@0.3", until="never", x=1050, y=560, tail="down",
          size=40),
        A("badge", ok=False, at="feel", until="never", x=1370, y=430),
        A("chip", "Kind design: fun, not guilt", at="never", until="next", x=1000, y=240, color="green", size=46),
        A("icons", at="never", until="next", x=1020, y=520, gap=250,
          items=[("heart", "never sick", "never@0.15"), ("house", "never runs away", "never@0.4"),
                 ("star", "no guilt", "never@0.75"), ("clock", "no money or streaks", "money")]),
        A("banner", "NEXT: Pet Class", at="next", color="green"),
        A("cards", at="next", x=620, y=230, w=760, gap=110,
          items=["Finish play", "Finish mood", "Finish describe", "Run: play with Pip"],
          reveal=["finish", "finish@0.4", "finish@0.75", "run"]),
        A("chip", "Does Bo change too?", at="bo", x=1000, y=760, color="yellow", size=46),
    )),
))
