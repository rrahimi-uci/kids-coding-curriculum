"""Level 1 Week 9: Variables, Input, and Choices (kit episode)."""

from ..kit_dsl import A, B, Episode, PIXEL, Scene

ASK_CONVERT = """color_name = input("Portal glow color? ")
size = int(input("Pick a size: "))
print(color_name, size + 10)"""

PORTAL_RULE = """size = int(input("Size? "))
if size > 100:
    print("big portal")
elif size > 50:
    print("medium portal")
else:
    print("small portal")"""

STEPS_BUG = """import turtle
t = turtle.Turtle()
answer = input("How many steps should I walk? ")
steps = answer
t.forward(steps)
turtle.done()"""

STEPS_FIXED = STEPS_BUG.replace("steps = answer", "steps = int(answer)")
TYPE_ERROR = "TypeError: can't multiply sequence by non-int of type 'float'"
PROMPT = "How many steps should I walk? "

COLOR_TEST = """color_name = input("Pick a color: ")
if color_name == "blue":
    print("Blue portal!")
else:
    print("Hmm, try orange, blue or green.")"""


def _walk(steps: int) -> str:
    return f"import turtle\nt = turtle.Turtle()\nt.forward({steps})\nturtle.done()"


EPISODE = Episode(level=1, week=9, scenes=(
    Scene("w09-s01", setting="workshop", lead_in=0.2, beats=(
        B("Welcome back to Kids Coding!", cue="welcome", pause=0.3),
        B("The next door asks,", cue="asks", pause=0.1),
        B("‘Choose a portal size: 40, 80, or 120.’", cue="portal", pause=0.3),
        B("Nova types 80.", cue="types", pause=0.3),
        B("Pixel stores the answer, but then tries to add ten and gets stuck.", cue="stores", pause=0.4),
        B("The input looked like a number.", cue="looked", pause=0.3),
        B("So why does Python see it as text?", cue="why", pause=1.8),
        B("And how can our program choose the right portal?", cue="choose", pause=2.6),
    ), actions=(
        A("door", "DOOR 9", x=1560, y=900),
        A("nova", x=300, y=960, enter="left", wave="welcome",
          moods={"types": "happy", "stores": "surprised", "why": "thinking"}, chin=("why", "end"),
          point=("types", "types>")),
        A("pixel", x=620, y=760, drop=True, beep=("stores", "stores@0.5"),
          moods={"stores@0.5": "confused", "choose": "thinking"}),
        A("banner", "MISSION: Ask, remember, choose", at="asks"),
        A("bubble", "Choose a portal size: 40, 80, or 120.", x=1540, y=520, tail="down-right", at="portal",
          until="types$"),
        A("box", "answer", at="types@0.5", x=1000, y=560, values=[("types@0.5", "80"), ("why$+0.6", "'80'")]),
        A("chip", "answer + 10 → stuck!", at="stores@0.6", until="why", x=1000, y=760, color="red", size=40),
        A("badge", ok=False, at="stores$", until="why", x=1180, y=470),
        A("chip", "Input begins as text", at="why$+0.6", x=1000, y=760, color="yellow", size=42),
        A("thought", "", at="choose$+0.2", until="end", x=500, y=330),
    )),
    Scene("w09-s02", setting="sky", beats=(
        B("A Python variable is a name connected to a value.", cue="var", pause=0.3),
        B("This line uses input to ask a playful question,", cue="line", pause=0.1),
        B("then stores the answer in a variable called color_name.",
          cue="code", pause=0.4),
        B("Input returns a string, which means text, even if you typed digits.", cue="string", pause=0.4),
        B("When we need number math or comparisons, int can convert suitable digit text into a whole number.",
          cue="int", pause=0.3),
        B("The next line asks for a size and turns the answer into a number.", cue="size", pause=0.4),
        B("First ask, then convert, then use.", cue="steps", pause=0.8),
    ), actions=(
        A("box", "size", at="var", until="string", x=1460, y=500, values=[("var@0.5", 100)]),
        A("chip", "variable = a name + a value", at="var@0.3", until="string", x=1460, y=680,
          color="sky", size=38),
        A("code", title="portal.py", code=ASK_CONVERT, x=100, y=180, w=980, h=540, size=32, at="line",
          reveal=["line@0.2", "size", "steps"], run="steps@0.5", inputs=["blue", "80"],
          expect=["Portal glow color? blue", "Pick a size: 80", "blue 90"],
          highlight=[(1, "line@0.2", "string$"), (2, "size", "steps")]),
        A("chip", "color_name = input(...)", at="code@0.3", until="size", x=1460, y=280, color="navy", size=40),
        A("box", "color_name", at="string", until="size", x=1460, y=500, w=300, values=[("string", "'blue'")]),
        A("chip", "input → text", at="string@0.4", until="steps", x=1460, y=680, color="yellow", size=42),
        A("machine", "int", at="int", until="steps", x=960, y=880, items=[("int@0.35", "'80'", "80")]),
        A("chip", 'size = int(input("Pick a size: "))', at="size", x=1460, y=280, color="navy", size=34),
        A("box", "size", at="size@0.5", x=1460, y=500, values=[("size@0.5", 80)]),
        A("cards", at="steps", x=560, y=800, w=420, gap=0, items=["Ask"], numbers=[1], reveal=["steps"]),
        A("cards", at="steps", x=1000, y=800, w=420, gap=0, items=["Convert"], numbers=[2], reveal=["steps@0.35"]),
        A("cards", at="steps", x=1440, y=800, w=420, gap=0, items=["Use"], numbers=[3], reveal=["steps@0.7"]),
    )),
    Scene("w09-s03", setting="peach", beats=(
        B("An if-elif-else chain is an ordered set of doors.", cue="chain", pause=0.3),
        B("Python checks from the top.", cue="top", pause=0.2),
        B("The first rule that's true wins, and the rest are skipped.", cue="first", pause=0.3),
        B("Else catches everything left over, and else never has a condition.", cue="else_", pause=0.4),
        B("Try this rule: if size is greater than 100, open the big portal; elif size is greater than 50, open "
          "the medium portal; else, open the small one.", cue="rule", pause=0.4),
        B("120 goes big, and only big.", cue="t120", pause=0.6),
        B("80 goes medium.", cue="t80", pause=0.6),
        B("40 goes small.", cue="t40", pause=0.5),
        B("Here's a tricky one: 100!", cue="tricky", pause=2.6),
        B("100 isn't greater than 100, so it goes medium.", cue="t100", pause=0.6),
        B("Remember: one equals sign puts a value in a box.", cue="equals", pause=0.3),
        B("Two equals signs ask, ‘Are these the same?’", cue="two", pause=0.8),
    ), actions=(
        A("code", title="portal.py", code=PORTAL_RULE, x=100, y=180, w=860, h=680, size=32, at="chain",
          run="t100@0.6", inputs=["100"], expect=["Size? 100", "medium portal"],
          highlight=[(2, "top", "top$"), (2, "rule@0.05", "rule@0.3"), (4, "rule@0.3", "rule@0.6"),
                     (6, "else_", "else_$"), (6, "rule@0.6", "rule$"),
                     (3, "t120", "t80"), (5, "t80", "t40"), (7, "t40", "tricky"), (5, "t100", "equals")]),
        A("flow", at="chain", x=1230, y=330, gap=200, items=["size > 100?", "size > 50?"],
          outcomes=["big", "medium", "small"],
          token=[("t120", "120", 0), ("t80", "80", 1), ("t40", "40", 2), ("t100", "100", 1)]),
        A("chip", "First true rule wins", at="first", until="equals", x=1380, y=900, color="green", size=44),
        A("chip", "else: no condition", at="else_@0.5", until="rule", x=1380, y=1000, color="orange", size=38),
        A("thought", "100?", at="tricky$+0.2", until="t100", x=1640, y=230),
        A("chip", "size = 80   puts a value in the box", at="equals", x=1300, y=880, color="sky", size=38),
        A("chip", "size == 80   asks: the same?", at="two", x=1300, y=990, color="yellow", size=38),
    )),
    Scene("w09-s04", setting="mint", beats=(
        B("Time for a bug hunt!", cue="bug", pause=0.3),
        B("Pixel asks,", cue="asks", pause=0.1),
        B("‘How many steps should I walk?’", speaker=PIXEL, cue="howmany", pause=0.2),
        B("Nova types 100.", cue="types", pause=0.3),
        B("Expected: Pixel walks 100 steps.", cue="expected", pause=0.3),
        B("Actual: a red TypeError!", cue="actual", pause=0.4),
        B("Pause: what's inside the box called steps?", cue="pause", pause=2.6),
        B("Type steps in the Shell.", cue="shell", pause=0.3),
        B("Thonny shows ‘100’ with quote marks.", cue="quotes", pause=0.3),
        B("That's text, and a turtle can't walk text.", cue="text", pause=0.4),
        B("The fix: convert the answer with int, so steps holds a number.", cue="fix", pause=0.4),
        B("Run again with 100, then 50, then 250.", cue="again", pause=1.4),
        B("One more test: on a color question, type Blue with a capital B.", cue="more", pause=0.6),
        B("No crash, but it goes to else, because Python is picky: ‘Blue’ and ‘blue’ are different.",
          cue="crash", pause=0.4),
        B("That's why a friendly else message helps.", cue="friendly", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", title="walk.py", code=STEPS_BUG, x=100, y=190, w=1060, h=620, size=30, at="asks", until="fix",
          run="expected$-0.2", inputs=["100"], expect=[PROMPT + "100", TYPE_ERROR], allow_error=True,
          error_line=5, highlight=[(4, "pause", "fix")]),
        A("code", title="walk.py", code=STEPS_FIXED, x=100, y=190, w=1060, h=620, size=30, at="fix",
          until="again@0.4", run="again", inputs=["100"], expect=[PROMPT + "100"],
          highlight=[(4, "fix", "again")]),
        A("code", title="walk.py", code=STEPS_FIXED, x=100, y=190, w=1060, h=620, size=30, at="again@0.4",
          until="again@0.75", run="again@0.4", inputs=["50"], expect=[PROMPT + "50"]),
        A("code", title="walk.py", code=STEPS_FIXED, x=100, y=190, w=1060, h=620, size=30, at="again@0.75",
          until="more", run="again@0.75", inputs=["250"], expect=[PROMPT + "250"]),
        A("turtle", code=_walk(100), x=1240, y=190, w=600, h=440, world=300, at="asks", run="again+0.5",
          duration=1.0, until="again@0.4"),
        A("turtle", code=_walk(50), x=1240, y=190, w=600, h=440, world=300, at="again@0.4", duration=0.8,
          until="again@0.75"),
        A("turtle", code=_walk(250), x=1240, y=190, w=600, h=440, world=300, at="again@0.75", duration=1.2,
          until="more"),
        A("pixel", x=1180, y=1000, s=0.42, ground=1030, beep="howmany",
          moods={"actual": "confused", "again$": "proud"}, until="more"),
        A("bubble", "How many steps should I walk?", x=1230, y=820, at="howmany", until="types$", size=34),
        A("chip", "Expected: walks 100 steps", at="expected", until="pause", x=620, y=900, color="green", size=40),
        A("badge", ok=False, at="actual", until="fix", x=1760, y=290),
        A("thought", "steps = ?", at="pause$+0.2", until="shell", x=1560, y=860),
        A("panel", "Shell", x=1290, y=680, w=540, size=36, at="shell", until="fix",
          items=[("shell@0.3", ">>> steps"), ("quotes@0.3", "'100'")]),
        A("chip", "Text '100' ≠ number 100", at="text", until="fix", x=620, y=900, color="yellow", size=42),
        A("chip", "int(answer) → a number", at="fix@0.4", until="more", x=620, y=900, color="green", size=42),
        A("badge", ok=True, at="again$", until="more", x=1760, y=290),
        # the capital-B test
        A("code", title="color.py", code=COLOR_TEST, x=100, y=190, w=1060, h=560, size=30, at="more",
          run="more$", inputs=["Blue"], expect=["Pick a color: Blue", "Hmm, try orange, blue or green."],
          highlight=[(2, "crash", "crash@0.5"), (4, "crash@0.5", "friendly"), (5, "friendly", "end")]),
        A("chip", "No crash → else", at="crash", x=1500, y=360, color="sky", size=42),
        A("chip", '"Blue" ≠ "blue"', at="crash@0.6", x=1500, y=500, color="yellow", size=48),
        A("chip", "A friendly else message helps", at="friendly", x=1500, y=640, color="green", size=38),
        A("nova", x=1500, y=1060, s=0.5, at="more", moods={"more": "thinking", "friendly": "happy"}),
    )),
    Scene("w09-s05", setting="workshop", tail=0.8, beats=(
        B("Portal opened!", cue="opened", pause=0.4),
        B("Input asks, variables remember, int turns digit text into a number, and if-elif-else picks the first "
          "true path.", cue="recap", pause=0.4),
        B("Here's our rule: ask about choices, like colors, sizes, and numbers, never about who you are.",
          cue="rule", pause=0.3),
        B("So no full name, home address, school, birthday, password, or photo.", cue="nofull", pause=0.4),
        B("If an app or game asks for personal details, stop and ask a grown-up.", cue="grownup", pause=0.5),
        B("Now open Exercise 9.1, Square of Any Size, then 9.2, Pick a Color.", cue="next", pause=0.3),
        B("Test every answer: orange, blue, green, and something silly, like pizza.", cue="test", pause=0.4),
        B("Happy coding!", cue="happy", pause=0.4),
    ), actions=(
        A("door", "DOOR 9", x=1700, y=920, open="opened"),
        A("nova", x=260, y=1010, s=0.72, wave=[("opened", "recap"), ("happy", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("chip", "Ask • Store • Convert • Choose", at="recap", until="rule", x=960, y=260, color="orange", size=46),
        A("cards", at="recap", until="rule", x=640, y=360, w=680, gap=110,
          items=["input asks", "variables remember", "int → a number", "if-elif-else: first true path"],
          reveal=["recap@0.05", "recap@0.2", "recap@0.4", "recap@0.7"]),
        A("chip", "Ask about choices, not about you", at="rule", until="next", x=1000, y=240, color="green",
          size=44),
        A("icons", at="rule@0.2", until="nofull", x=1000, y=440, gap=260,
          items=[("star", "Colors", "rule@0.25"), ("gear", "Sizes", "rule@0.35"), ("check", "Numbers", "rule@0.45")]),
        A("icons", at="nofull", until="next", x=960, y=440, gap=200, crossed=[0, 1, 2, 3, 4, 5], size=30,
          items=[("person", "Full name", "nofull@0.1"), ("house", "Home address", "nofull@0.25"),
                 ("book", "School", "nofull@0.4"), ("clock", "Birthday", "nofull@0.55"),
                 ("key", "Password", "nofull@0.7"), ("camera", "Photo", "nofull@0.85")]),
        A("icons", at="grownup", until="next", x=1000, y=730, items=[("grownup", "Stop • ask a grown-up", "grownup")],
          gap=400),
        A("banner", "NEXT: Square of Any Size + Pick a Color", at="next", color="green"),
        A("cards", at="next", x=620, y=230, w=720, gap=110,
          items=["9.1 Square of Any Size", "9.2 Pick a Color", "Test orange, blue, green", "…and pizza!"],
          reveal=["next@0.1", "next@0.6", "test@0.2", "test@0.8"]),
        A("chip", "Happy coding!", at="happy", x=960, y=780, color="orange", size=48),
    )),
))
