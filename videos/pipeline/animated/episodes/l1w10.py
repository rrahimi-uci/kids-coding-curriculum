"""Level 1 Week 10: Random Art and Our Own Commands (kit episode).

The video's recipe is flower(size); Flower Stamp's starter uses flower(x, y), and its calls are never shown.
"""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

PALETTE_LINE = ('PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",\n'
                '           "#0072B2", "#D55E00", "#CC79A7", "#000000"]')
PALETTE_CODES = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

RECIPE = """def flower(size):
    for petal in range(8):
        t.circle(size)
        t.left(45)"""

FLOWER60 = f"""import turtle
t = turtle.Turtle()

{RECIPE}

flower(60)
turtle.done()"""

# Three calls side by side (the canvas also moves the turtle between the calls).
THREE_SIZES = f"""import turtle
t = turtle.Turtle()
t.pensize(3)
{RECIPE}

for size, x in [(30, -480), (60, -230), (90, 250)]:
    t.penup()
    t.goto(x, 0)
    t.pendown()
    flower(size)
turtle.done()"""

# The hook's gallery picture (code hidden).
GALLERY = f"""import random
import turtle
{PALETTE_LINE}
t = turtle.Turtle()
t.pensize(3)
{RECIPE}

for i in range(7):
    t.penup()
    t.goto(random.randint(-220, 220), random.randint(-120, 120))
    t.pendown()
    t.color(random.choice(PALETTE))
    flower(random.randint(10, 45))
turtle.done()"""

RANDOM_SHOWN = """import random
import turtle

print(random.choice(PALETTE))
print(random.randint(10, 80))"""
RANDOM_EXEC = f"""import random
import turtle
{PALETTE_LINE}
print(random.choice(PALETTE))
print(random.randint(10, 80))"""

LOOP_SHOWN = """for i in range(6):
    t.color(random.choice(PALETTE))
    flower(random.randint(10, 80))"""
GARDEN = f"""import random
import turtle
{PALETTE_LINE}
t = turtle.Turtle()
t.pensize(3)
{RECIPE}

{LOOP_SHOWN}
turtle.done()"""

BUG_NO_CALL = f"""import turtle
t = turtle.Turtle()

{RECIPE}

turtle.done()"""

COPY_PASTE = """t.circle(30)
t.left(45)
t.circle(30)
t.left(45)
t.circle(30)
t.left(45)
..."""


def _line_y(top: int, size: int = 34, n: int = 1) -> float:
    return top + 90 + (n - 1) * size * 1.45 + size * 1.45 / 2


EPISODE = Episode(level=1, week=10, scenes=(
    Scene("w10-s01", setting="workshop", lead_in=0.2, beats=(
        B("Welcome back to Kids Coding!", cue="welcome", pause=0.3),
        B("The workshop gallery needs a hundred flowers, and no two should look exactly alike.", cue="gallery",
          pause=0.3),
        B("Nova could copy the same drawing code again and again.", cue="copy", pause=0.3),
        B("But Pixel has a better idea:", cue="idea", pause=0.1),
        B("‘Teach Python one flower-making command, then call it with different sizes and random colors!’",
          speaker=PIXEL, cue="teach", pause=0.4),
        B("Can one recipe create a whole garden?", cue="garden", pause=2.8),
    ), actions=(
        A("nova", x=300, y=960, enter="left", wave="welcome", moods={"copy": "worried", "idea": "surprised",
                                                                    "teach": "happy", "garden": "thinking"},
          chin=("garden", "end")),
        A("pixel", x=620, y=760, drop=True, beep="teach", moods={"teach": "proud"}),
        A("banner", "MISSION: One recipe, many artworks", at="gallery"),
        A("chip", "100 flowers • no two alike", at="gallery@0.3", until="copy", x=1340, y=420, color="pink",
          size=46),
        A("code", title="copy_paste.py", code=COPY_PASTE, x=930, y=190, w=820, h=470, shell=False,
          at="copy", type=("copy", "copy$"), until="idea$"),
        A("chip", "copy… paste… copy… paste…", at="copy@0.6", until="idea$", x=1340, y=720, color="red", size=40),
        A("machine", "flower", at="teach", until="garden", x=1250, y=430,
          items=[("teach@0.25", "size 30", "small"), ("teach@0.65", "size 90", "big")]),
        A("turtle", code=GALLERY, x=960, y=190, w=780, h=560, at="garden", duration=4.5, title="Gallery"),
        A("chip", "Reusable + adjustable + surprising", at="garden$", x=1350, y=830, color="yellow", size=40),
        A("thought", "", at="garden$+0.2", until="end", x=500, y=330),
    )),
    Scene("w10-s02", setting="sky", beats=(
        B("A function is your own command, just like a My Block in Scratch.", cue="func", pause=0.3),
        B("We write def, the name flower, and an input slot in parentheses: a parameter called size.", cue="defn",
          pause=0.2),
        B("Then a colon.", cue="colon", pause=0.3),
        B("The pushed-in lines are the recipe.", cue="recipe", pause=0.4),
        B("But a recipe card isn't a cake.", cue="cake", pause=0.3),
        B("Defining writes the card; nothing is drawn yet.", cue="nothing", pause=0.4),
        B("To use it, call flower with the number sixty.", cue="call", pause=0.3),
        B("Sixty goes into the size slot.", cue="slot", pause=0.4),
        B("Define once, call many times: thirty, sixty, and ninety make three flower sizes from one recipe.",
          cue="many", pause=1.0),
    ), actions=(
        A("scratch", "My Block", blocks=[("myblocks", "define flower [size]")], x=1180, y=230, w=620, h=220,
          at="func", until="defn@0.5"),
        A("code", title="flower.py", code=FLOWER60, x=100, y=180, w=960, h=600, shell=False, at="func",
          until="many", reveal=["func", "func", "func", "defn", "recipe", "recipe", "recipe", "recipe", "call",
                                 "call"],
          highlight=[(4, "defn", "colon$"), (5, "recipe", "cake"), (6, "recipe", "cake"), (7, "recipe", "cake"),
                     (9, "call", "slot$"), (4, "slot", "slot$")]),
        A("chip", "def → define the recipe", at="defn@0.2", until="nothing", x=1480, y=520, color="orange"),
        A("chip", "parameter → input slot", at="defn@0.7", until="nothing", x=1480, y=640, color="green"),
        A("chip", "recipe card ≠ cake", at="cake", until="nothing", x=1480, y=760, color="pink"),
        A("turtle", code=FLOWER60, x=1180, y=200, w=620, h=560, at="nothing", run="call$", duration=2.6,
          until="many"),
        A("chip", "flower(60) → call the function", at="call@0.4", until="many", x=1490, y=850, color="yellow",
          size=40),
        A("box", "size", at="slot", until="many", x=580, y=900, values=[("slot", 60)], h=140),
        A("machine", "flower", at="many", x=960, y=330,
          items=[("many@0.3", "30", "small"), ("many@0.5", "60", "medium"), ("many@0.7", "90", "big")]),
        A("turtle", code=THREE_SIZES, x=160, y=560, w=1600, h=440, world=200, at="many", run="many@0.3",
          duration=5.0, title="Three sizes, one recipe"),
    )),
    Scene("w10-s03", setting="lavender", beats=(
        B("First, write import random at the top, next to import turtle.", cue="imp", pause=0.3),
        B("Then random.choice picks one item from a list, like picking a crayon from a bag with your eyes closed.",
          cue="choice", pause=0.3),
        B("Here, it picks from our color-blind-safe PALETTE.", cue="palette", pause=0.4),
        B("And random.randint, with ten and eighty, picks a whole number from ten up to eighty, and both ten and "
          "eighty can be picked.", cue="randint", pause=0.3),
        B("Smaller number first!", cue="smaller", pause=0.4),
        B("Random doesn't mean ‘anything in the universe.’", cue="universe", pause=0.2),
        B("We choose the limits.", cue="limits", pause=0.5),
        B("A loop can call our flower function several times with new choices, so the garden changes every run, "
          "but it still follows our rules.", cue="loop", pause=1.2),
    ), actions=(
        A("code", title="random_flowers.py", code=RANDOM_SHOWN, exec=RANDOM_EXEC, x=100, y=180, w=1000, h=560,
          shell_h=180, at="imp", until="loop", reveal=["imp", "imp", "imp", "choice@0.3", "randint@0.2"], run="smaller$",
          expect=["#009E73", "18"],
          highlight=[(1, "imp", "imp$"), (4, "choice@0.3", "palette$"), (5, "randint@0.2", "randint$"),
                     (5, "smaller", "smaller$")]),
        A("chip", "import random", at="imp@0.3", until="loop", x=1480, y=250, color="navy", size=44),
        A("chip", "random.choice(PALETTE)", at="choice@0.2", until="loop", x=1480, y=370, color="orange", size=40),
        A("chip", "random.randint(10, 80)", at="randint@0.2", until="loop", x=1480, y=490, color="green", size=40),
        A("chip", "10 … 80: both ends can be picked", at="randint@0.6", until="loop", x=1480, y=610, color="sky",
          size=34),
        A("chip", "smaller number first", at="smaller", until="loop", x=1480, y=720, color="yellow", size=36),
        A("listrow", "PALETTE", at="palette", until="loop", x=960, y=880, cell=200, indexes=False,
          items=PALETTE_CODES, highlight=[("smaller$+0.5", "loop", 2)]),
        A("chip", "Random choices stay inside our limits", at="limits", until="loop", x=1300, y=170,
          color="pink", size=36),
        A("code", title="garden.py", code=LOOP_SHOWN, x=100, y=220, w=1000, h=300, shell=False, at="loop",
          highlight=[(1, "loop", "loop@0.3"), (2, "loop@0.3", "loop@0.5"), (3, "loop@0.3", "loop@0.5")]),
        A("chip", "Random choices stay inside our limits", at="loop", x=600, y=620, color="pink", size=36),
        A("turtle", code=GARDEN, x=1180, y=170, w=600, h=420, at="loop", run="loop+0.3", duration=3.0,
          title="Run 1"),
        A("turtle", code=GARDEN, seed=2, x=1180, y=620, w=600, h=420, at="loop@0.6", duration=3.0, title="Run 2"),
        A("chip", "New run → new garden", at="loop@0.7", x=600, y=760, color="green", size=40),
    )),
    Scene("w10-s04", setting="mint", beats=(
        B("Time for a bug hunt!", cue="bug", pause=0.3),
        B("Nova's program runs with no red error, but the screen stays blank.", cue="blank", pause=0.3),
        B("‘Where's my flower?’", speaker=NOVA, cue="where", pause=0.1),
        B("asks Nova.", cue="asksnova", pause=0.4),
        B("What did we expect?", cue="expect", pause=0.6),
        B("One flower.", cue="one", pause=0.3),
        B("What actually happened?", cue="happened", pause=0.6),
        B("Nothing.", cue="nothing", pause=0.4),
        B("Read the code one line at a time, with your finger.", cue="read", pause=0.3),
        B("The flower recipe looks perfect.", cue="perfect", pause=0.3),
        B("But scan below it: nothing ever calls it.", cue="scan", pause=0.4),
        B("Defining writes the recipe; calling makes it run.", cue="defining", pause=0.4),
        B("Pause: what one line could we add?", cue="pause", pause=3.2),
        B("Call flower with sixty, on a new line below the recipe, at the left edge, not pushed in.",
          cue="fixline", pause=0.3),
        B("Run again.", cue="runagain", pause=2.2),
        B("A blank screen with no error can still be a clue.", cue="clue", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", title="flower.py", code=BUG_NO_CALL, x=100, y=190, w=960, h=700, size=30, at="blank", until="fixline",
          run="blank@0.2", expect=[], shell_h=160,
          highlight=[(4, "perfect", "perfect$"), (5, "perfect", "perfect$"), (6, "perfect", "perfect$"),
                     (7, "perfect", "perfect$"), (8, "scan", "pause$"), (9, "scan", "pause$")]),
        A("pointer", x=980, y=_line_y(190, size=30, n=1), at="read", until="defining",
          path=[("read", 980, _line_y(190, size=30, n=1)), ("read$", 980, _line_y(190, size=30, n=3)),
                ("perfect$", 980, _line_y(190, size=30, n=7)), ("scan@0.6", 980, _line_y(190, size=30, n=9))]),
        A("code", title="flower.py", code=FLOWER60, x=100, y=190, w=960, h=700, size=30, at="fixline", run="runagain",
          expect=[], shell_h=160, highlight=[(9, "fixline", "clue")]),
        A("turtle", code=FLOWER60, x=1180, y=190, w=620, h=480, at="blank", run="runagain+0.3", duration=2.0),
        A("chip", "No red error can still mean a bug", at="blank@0.7", until="expect", x=580, y=960,
          color="yellow", size=40),
        A("bubble", "Where's my flower?", x=1110, y=800, at="where", until="asksnova$", size=36),
        A("panel", "Detective notes", x=1180, y=720, w=620, size=34, at="expect", until="defining",
          items=[("one", "Expected: one flower"), ("nothing", "Happened: nothing")]),
        A("badge", ok=False, at="nothing", until="runagain", x=1740, y=280),
        A("chip", "Defined ≠ called", at="defining", x=1490, y=780, color="orange", size=44),
        A("thought", "One line?", at="pause$+0.2", until="fixline", x=1490, y=930),
        A("chip", "Add at the left edge: flower(60)", at="fixline@0.4", x=1490, y=900, color="green", size=34),
        A("badge", ok=True, at="runagain+2.3", x=1740, y=280),
        A("confetti", at="runagain+2.3", x=1490, y=430),
        A("chip", "No red error can still mean a bug", at="clue", x=580, y=960, color="yellow", size=40),
        A("nova", x=1110, y=1065, s=0.45, moods={"blank": "confused", "pause": "thinking",
                                                 "runagain+2.3": "proud"}),
    )),
    Scene("w10-s05", setting="workshop", tail=0.8, beats=(
        B("The garden blooms!", cue="blooms", pause=0.4),
        B("Functions are your own commands, parameters are their input slots, calls make them run, and random "
          "adds surprises inside our limits.", cue="recap", pause=0.4),
        B("Now meet your final project: My Interactive Art Show.", cue="meet", pause=0.4),
        B("It greets the viewer, asks one or two questions, and draws a picture using six ingredients:",
          cue="greets", pause=0.1),
        B("a question with input, a variable, an if, a loop, something random, and a function you made with def.",
          cue="six", pause=0.4),
        B("First, build Flower Stamp and Random Bubble Art.", cue="first", pause=0.3),
        B("Then fill in your plan sheet.", cue="plan", pause=0.3),
        B("Borrowed an idea?", cue="borrowed", pause=0.3),
        B("Make it yours, and add a credit comment.", cue="credit", pause=0.4),
        B("Happy coding!", cue="happy", pause=0.4),
    ), actions=(
        A("door", "DOOR 10", x=1720, y=920, open="blooms"),
        A("nova", x=260, y=1010, s=0.72, wave=[("blooms", "recap"), ("happy", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("confetti", at="blooms", x=1000, y=400),
        A("cards", at="recap", until="meet", x=640, y=280, w=720, gap=110,
          items=["Functions = your own commands", "Parameters = input slots", "Calls make them run",
                 "Random = surprises inside limits"],
          reveal=["recap", "recap@0.25", "recap@0.5", "recap@0.7"]),
        A("banner", "PROJECT: My Interactive Art Show", at="meet", until="first", color="purple"),
        A("chip", "greets • asks • draws", at="greets", until="first", x=1000, y=250, color="sky", size=42),
        A("icons", at="six", until="first", x=1000, y=440, gap=205, size=32,
          items=[("laptop", "input", "six@0.05"), ("file", "variable", "six@0.2"), ("key", "if", "six@0.32"),
                 ("clock", "loop", "six@0.45"), ("star", "random", "six@0.6"), ("gear", "def", "six@0.8")]),
        A("chip", "input • variable • if • loop • random • def", at="six$", until="first", x=1000, y=680,
          color="yellow", size=40),
        A("banner", "NEXT: Flower Stamp + Random Bubble Art", at="first", color="green"),
        A("cards", at="first", x=620, y=230, w=740, gap=110,
          items=["10.1 Flower Stamp", "10.2 Random Bubble Art", "Fill in your plan sheet (M1)",
                 "Credit borrowed ideas"],
          reveal=["first@0.2", "first@0.6", "plan", "credit"]),
        A("chip", "# Flower idea remixed from Exercise 10.1", at="credit@0.4", x=1000, y=740, color="white",
          size=34),
        A("chip", "Happy coding!", at="happy", x=1000, y=850, color="orange", size=48),
    )),
))
