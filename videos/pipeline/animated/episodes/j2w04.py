"""Junior Level 2 Week 4: Surprise! Random (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/2-game-makers/teaching-material/lessons/week04.tex: the dice race warm-up, pick
random as a die inside the computer, Exercise 4.1 Dice Race (the cat's half: a roll variable, pick
random 1 to 6, repeat roll), random jumps, go to random position for Exercise 4.2 Ghost Pop (only
the one block, not the whole script), Exercise 4.3 The Stuck Dice (the roll is picked once, above
the forever) and being a good sport. Pixi is the racer on the paper track.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
ROLL10 = ("variables", "set [roll] to [pick random 1 to 10]")
SAY_ROLL = ("looks", "say [roll] for [1] seconds")
WAIT1 = ("control", "wait [1] seconds")
DICE_RACE = [("event", "when [c] key pressed"), ("variables", "set [roll] to [pick random 1 to 6]"), SAY_ROLL,
             ("control", "repeat [roll]", [("motion", "move [20] steps"), ("looks", "next costume")])]
BIG = 1.25  # block scale: big enough for young eyes
SPRITE = 1.0  # sprite size on the stage


def hops(cue, count, start=0.0, gap=0.35):
    """The cat hops `count` times (move 20 steps each), starting at `cue` + start seconds."""
    return [(f"{cue}+{start + i * gap:.2f}", "move", 20, 0.28) for i in range(count)]


EPISODE = Episode(level="j2", week=4, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j2-w04-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello, game makers!", speaker=PIXI, cue="hello", pause=0.5),
        B("Here is a race. Who will win? Can you tell me now?", speaker=AIDEN, cue="who", pause=2.8),
        B("We cannot know! The die decides.", speaker=AIDEN, cue="die", pause=0.5),
        B("Today, we make games full of surprises, with random numbers!", speaker=AIDEN, cue="mission",
          pause=0.5),
        B("Let's go!", speaker=AIDEN, cue="go", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("go", "end")],
          moods={"start": "happy", "who": "thinking", "die": "surprised", "mission": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("thought", "Who will win?", at="who$+0.2", until="die", x=1320, y=420),
        A("bigtext", "?", at="die", until="mission", x=1320, y=440, size=140, color="purple"),
        A("banner", "MISSION: Surprise!", at="mission"),
        A("bigtext", "4", at="mission@0.3", until="mission$", x=1320, y=440, size=120, color="green"),
        A("bigtext", "1", at="mission$", until="go$", x=1320, y=440, size=120, color="orange"),
        A("bigtext", "6", at="go$", x=1320, y=440, size=120, color="blue"),
    )),
    # 2. the dice race (the lesson's warm-up) -----------------------------------------------------------
    Scene("j2-w04-s02", setting="workshop", beats=(
        B("Let's warm up with a dice race! Pixi is our racer.", speaker=AIDEN, cue="race", pause=0.4),
        B("Roll the die, say the number, and hop that many squares.", speaker=AIDEN, cue="rule", pause=0.5),
        B("What number will we get?", speaker=AIDEN, cue="guess", pause=2.8),
        B("Four! Hop, hop, hop, hop.", speaker=AIDEN, cue="four", pause=1.0),
        B("Roll again. What will it be this time?", speaker=AIDEN, cue="again", pause=2.6),
        B("Two! Hop, hop.", speaker=AIDEN, cue="two", pause=0.8),
        B("Nobody can guess the number every time. That is called random.", speaker=AIDEN, cue="random",
          pause=0.6),
        B("And at the end, everyone says good game, whoever won!", speaker=AIDEN, cue="good", pause=0.8),
    ), actions=(
        A("grid", rows=["..............G"], x=210, y=420, cell=100, at="race",
          marks=[("race", 0, 0, "1")],
          walker=[("race", 0, 0), ("four@0.35", 1, 0), ("four@0.55", 2, 0), ("four@0.75", 3, 0),
                  ("four$", 4, 0), ("two@0.5", 5, 0), ("two$", 6, 0)]),
        A("chip", "roll, then hop that many", at="rule", until="guess", x=960, y=700, color="sky", size=44),
        A("thought", "What number?", at="guess$+0.2", until="four", x=960, y=720),
        A("bigtext", "4", at="four", until="again", x=960, y=720, size=110, color="green"),
        A("thought", "What this time?", at="again$+0.2", until="two", x=960, y=720),
        A("bigtext", "2", at="two", until="random", x=960, y=720, size=110, color="orange"),
        A("chip", "random = nobody can guess it", at="random", x=960, y=700, color="purple", size=46),
        A("chip", "Good game!", at="good", x=960, y=830, color="green", size=46),
        A("aiden", x=200, y=1080, s=0.5, moods={"guess": "thinking", "four": "happy", "good": "proud"}),
    )),
    # 3. pick random: a die inside the computer ---------------------------------------------------------
    Scene("j2-w04-s03", setting="lavender", beats=(
        B("Games are more fun when you cannot guess what comes next.", speaker=AIDEN, cue="fun", pause=0.4),
        B("Scratch has a die inside it: the green pick random block, in the Operators circle.", speaker=AIDEN,
          cue="block", pause=0.6),
        B("A real die gives a number from one to six, but you cannot pick it.", speaker=AIDEN, cue="real",
          pause=0.5),
        B("Pick random one to six is a die inside the computer. Pick random one to ten is a die with ten sides.",
          speaker=AIDEN, cue="six", pause=0.6),
        B("Every time the block runs, it rolls again.", speaker=AIDEN, cue="again", pause=0.5),
        B("Roll, roll, roll!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("bigtext", "?", at="fun", until="block", x=960, y=480, size=140, color="purple"),
        A("scratch", blocks=[("operators", "pick random [1] to [10]")], x=240, y=330, w=760, h=120, panel=False,
          scale=1.4, at="block", edits=[("six", 0, "pick random [1] to [6]"), ("six@0.6", 0, "pick random [1] to [10]")]),
        A("chip", "Operators: green", at="block@0.6", until="real", x=560, y=560, color="green", size=46),
        A("chip", "1 to 6: a die", at="six", until="six@0.6", x=560, y=560, color="green", size=46),
        A("chip", "1 to 10: a die with ten sides", at="six@0.6", until="again", x=560, y=560, color="green",
          size=42),
        A("box", "roll", at="real", x=1440, y=450, w=340, h=220, size=90,
          values=[("real", ""), ("again@0.2", 3), ("again@0.5", 8), ("again@0.8", 1), ("pixi", 6),
                  ("pixi@0.5", 2), ("pixi$", 9)]),
        A("chip", "Every run: a new roll", at="again", x=560, y=560, color="purple", size=46),
        A("pixi", x=1440, y=900, s=0.5, at="pixi", ground=990),
    )),
    # 4. build Dice Race, the cat's half (Exercise 4.1) -----------------------------------------------
    Scene("j2-w04-s04", setting="mint", beats=(
        B("Let's build the cat's half of Dice Race. Drag the cat to the left side.", speaker=AIDEN,
          cue="build", pause=0.5),
        B("Orange-red Variables: make a variable called roll. This box holds the number we roll.",
          speaker=AIDEN, cue="var", pause=0.6),
        B("Yellow Events: when space key pressed. Click the little arrow and pick c. C for Cat!", speaker=AIDEN,
          cue="key", pause=0.6),
        B("Snap on set roll to zero. Drop the green pick random block into the zero, and change ten to six.",
          speaker=AIDEN, cue="set", pause=0.7),
        B("Purple Looks: a say block. Drag the round roll block into it, and change two to one.",
          speaker=AIDEN, cue="say", pause=0.7),
        B("Orange Control: repeat. Drag roll into the ten, so the cat hops as many times as the die says.",
          speaker=AIDEN, cue="repeat", pause=0.7),
        B("Inside the repeat: move twenty steps, and next costume.", speaker=AIDEN, cue="inside", pause=0.8),
    ), actions=(
        A("banner", "Exercise 4.1: Dice Race", at="build", color="green"),
        A("scratch", "Cat", blocks=[("event", "when [space] key pressed"), ("variables", "set [roll] to [0]"),
                                    ("looks", "say [Hello!] for [2] seconds"),
                                    ("control", "repeat [10]", [("motion", "move [10] steps"),
                                                                ("looks", "next costume")])],
          x=120, y=250, w=930, h=730, scale=BIG, reveal=["key", "set", "say", "repeat", "inside", "inside@0.5"],
          edits=[("key@0.6", 0, "when [c] key pressed"), ("set@0.45", 1, "set [roll] to [pick random 1 to 10]"),
                 ("set@0.85", 1, "set [roll] to [pick random 1 to 6]"), ("say@0.6", 2, "say [roll] for [1] seconds"),
                 ("repeat@0.4", 3, "repeat [roll]"), ("inside@0.4", 4, "move [20] steps")]),
        A("stage", x=1120, y=250, w=700, h=480, at="build", flag=False, sprite_x=-190, sprite_y=-60,
          sprite_scale=SPRITE, monitors=[("roll", [("var@0.5", 0)])]),
        A("chip", "Variables: orange-red", at="var", until="key", x=1470, y=860, color="orange", size=44),
        A("chip", "Events: yellow", at="key", until="set", x=1470, y=860, color="yellow", size=44),
        A("chip", "Operators: green", at="set@0.4", until="say", x=1470, y=860, color="green", size=44),
        A("chip", "Looks: purple", at="say", until="repeat", x=1470, y=860, color="purple", size=44),
        A("chip", "Control: orange", at="repeat", until="inside", x=1470, y=860, color="orange", size=44),
        A("chip", "Motion: blue", at="inside", x=1470, y=860, color="sky", size=44),
    )),
    # 5. test: how far will the cat go? -------------------------------------------------------------------
    Scene("j2-w04-s05", setting="sky", beats=(
        B("Click the stage once, then press c. How far will the cat go?", speaker=AIDEN, cue="press", pause=2.8),
        B("Three! Hop, hop, hop.", speaker=AIDEN, cue="three", pause=1.6),
        B("Press c again. How far this time?", speaker=AIDEN, cue="again", pause=2.6),
        B("Five! Nobody knows until the die rolls.", speaker=AIDEN, cue="five", pause=1.4),
        B("Surprise!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Cat", blocks=DICE_RACE, x=110, y=270, w=820, h=620, scale=1.0),
        A("stage", x=1000, y=230, w=820, h=560, flag=False, sprite_x=-190, sprite_y=-60, sprite_scale=SPRITE,
          monitors=[("roll", [("start", 0), ("three", 3), ("five", 5)])],
          actions=[("three", "say", "3", 1.0)] + hops("three", 3, 1.1)
          + [("five", "say", "5", 1.0)] + hops("five", 5, 1.1)),
        A("thought", "How far?", at="press$+0.2", until="three", x=1410, y=900),
        A("chip", "3 hops", at="three+1.0", until="again", x=1410, y=900, color="green", size=46),
        A("thought", "How far this time?", at="again$+0.2", until="five", x=1410, y=900),
        A("chip", "5 hops", at="five+1.0", x=1410, y=900, color="green", size=46),
    )),
    # 6. quick quiz ------------------------------------------------------------------------------------
    Scene("j2-w04-s06", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("The block says pick random one to six. Could the cat say nine?", speaker=AIDEN, cue="nine", pause=3.0),
        B("No! Only one, two, three, four, five or six.", speaker=AIDEN, cue="no", pause=0.6),
        B("Could it say the same number two times in a row?", speaker=AIDEN, cue="same", pause=2.8),
        B("Yes! That is still random. Random means nobody can guess the next one.", speaker=AIDEN, cue="yes",
          pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", blocks=[("operators", "pick random [1] to [6]")], x=200, y=330, w=760, h=120, panel=False,
          scale=1.4, at="nine"),
        A("thought", "Could it be 9?", at="nine$+0.2", until="no", x=1400, y=420),
        A("chip", "1  2  3  4  5  6", at="no", until="same", x=1400, y=420, color="green", size=52),
        A("thought", "Same number twice?", at="same$+0.2", until="yes", x=1400, y=420),
        A("chip", "4  4: still random!", at="yes", x=1400, y=420, color="purple", size=50),
        A("chip", "Nobody can guess the next one", at="yes@0.5", x=960, y=760, color="yellow", size=46),
    )),
    # 7. wiggle break: random jumps -----------------------------------------------------------------
    Scene("j2-w04-s07", setting="workshop", beats=(
        B("Wiggle break! Stand up. I roll the die, and we do that many jumps.", speaker=AIDEN, cue="wiggle",
          pause=0.6),
        B("Three! Jump, jump, jump!", speaker=AIDEN, cue="three", pause=1.0),
        B("Roll again. Two! Clap, clap!", speaker=AIDEN, cue="two", pause=1.0),
        B("Now stretch up high, and take three slow breaths.", speaker=AIDEN, cue="breathe", pause=2.4),
        B("Beep! I feel great!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("two", "two$"), ("breathe", "breathe$")],
          moods={"start": "happy", "breathe": "proud"},
          path=[("three@0.4", 300, 960), ("three@0.55", 300, 900), ("three@0.7", 300, 960),
                ("three@0.85", 300, 900), ("three$", 300, 960), ("three$+0.3", 300, 900),
                ("three$+0.6", 300, 960)]),
        A("pixi", x=620, y=760, beep=["three", "two"], moods={"pixi": "happy"}),
        A("bigtext", "3 jumps!", at="three", until="two", x=1300, y=480, size=100, color="green"),
        A("bigtext", "2 claps!", at="two", until="breathe", x=1300, y=480, size=100, color="orange"),
        A("icons", items=[("heart", "Three slow breaths", "breathe")], at="breathe", x=1300, y=500),
    )),
    # 8. go to random position (Ghost Pop) -------------------------------------------------------------
    Scene("j2-w04-s08", setting="sky", beats=(
        B("Random can pick a place too.", speaker=AIDEN, cue="place", pause=0.4),
        B("The blue Motion block, go to random position, sends a sprite to a surprise spot.", speaker=AIDEN,
          cue="block", pause=0.6),
        B("In Exercise 4.2, Ghost Pop, the ghost pops up somewhere new every second.", speaker=AIDEN,
          cue="ghost", pause=0.5),
        B("Click it, and you get a point! Where will it go next?", speaker=AIDEN, cue="next", pause=2.6),
        B("Nobody knows. Surprise!", speaker=AIDEN, cue="surprise", pause=0.8),
    ), actions=(
        A("scratch", blocks=[("motion", "go to [random position]")], x=150, y=360, w=760, h=120, panel=False,
          scale=1.4, at="block"),
        A("chip", "Motion: blue", at="block@0.5", until="ghost", x=500, y=600, color="sky", size=46),
        A("banner", "Exercise 4.2: Ghost Pop", at="ghost", color="green"),
        A("stage", x=1040, y=250, w=780, h=540, at="block", flag_at="ghost@0.3", sprite="ghost", sprite_scale=SPRITE,
          monitors=[("score", [("block", 0), ("next+0.2", 1)])],
          actions=[("block@0.7", "goto", -120, 0, 0.15), ("ghost@0.4", "goto", 140, -40, 0.15),
                   ("ghost@0.8", "goto", -60, -70, 0.15), ("next+0.3", "goto", 120, 10, 0.15),
                   ("next$+1.0", "goto", -150, -20, 0.15), ("surprise", "goto", 60, 0, 0.15),
                   ("surprise$", "goto", -100, -60, 0.15)]),
        A("pointer", x=1335, y=620, at="next", until="next+0.8"),
        A("sfx", "pop", at="next+0.2"),
        A("thought", "Where next?", at="next$+0.2", until="surprise", x=500, y=640),
        A("chip", "Surprise!", at="surprise", x=500, y=640, color="purple", size=52),
    )),
    # 9. bug hunt: The Stuck Dice (Exercise 4.3) -------------------------------------------------------
    Scene("j2-w04-s09", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.4),
        B("Omar's cat should say a new surprise number every two seconds.", speaker=AIDEN, cue="omar",
          pause=0.4),
        B("But it says seven, seven, seven, again and again!", speaker=AIDEN, cue="seven", pause=1.0),
        B("Detectives, where does the die get rolled?", speaker=AIDEN, cue="look", pause=3.2),
        B("Above the forever! The die rolls once, at the start, and never again.", speaker=AIDEN, cue="found",
          pause=0.5),
        B("Like rolling a die once, and then moving that number every turn, forever.", speaker=AIDEN,
          cue="like", pause=0.6),
        B("Fix: drag the forever away, put the set block in the top of the forever, then snap the forever back.",
          speaker=AIDEN, cue="fix", pause=0.8),
        B("Test again.", speaker=AIDEN, cue="test", pause=4.2),
        B("A new number every time! We fixed the bug!", speaker=AIDEN, cue="fixed", pause=0.4),
        B("Roll, roll, roll!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Stuck Dice", at="bug", color="navy"),
        A("scratch", "Omar's script", blocks=[FLAG, ROLL10, ("control", "forever", [SAY_ROLL, WAIT1])], x=120,
          y=250, w=900, h=640, scale=BIG, at="omar", until="fix$",
          highlight=[(1, "found", "fix$")]),
        A("scratch", "Omar's script (fixed)", blocks=[FLAG, ("control", "forever", [ROLL10, SAY_ROLL, WAIT1])],
          x=120, y=250, w=900, h=640, scale=BIG, at="fix$", highlight=[(2, "fix$", "test+1.0")]),
        A("sfx", "snap", at="fix$"),
        A("stage", x=1120, y=250, w=700, h=480, at="omar", flag_at="omar@0.5", sprite_scale=SPRITE,
          monitors=[("roll", [("omar", 0), ("omar@0.6", 7), ("test+0.3", 3), ("test+2.3", 9), ("fixed+0.6", 5)])],
          actions=[("omar@0.6", "say", "7", 1.0), ("seven", "say", "7", 1.0), ("seven+2.0", "say", "7", 1.0),
                   ("test+0.3", "say", "3", 1.0), ("test+2.3", "say", "9", 1.0), ("fixed+0.6", "say", "5", 1.0)]),
        A("badge", ok=False, at="seven@0.6", until="test", x=1750, y=290),
        A("chip", "7, 7, 7...", at="seven", until="look", x=1470, y=840, color="red", size=46),
        A("thought", "Where is the roll?", at="look$+0.2", until="found", x=1470, y=860),
        A("chip", "Rolled once, before the loop", at="found", until="test", x=1470, y=840, color="red", size=40),
        A("chip", "Inside the forever: a new roll each time", at="fixed", x=1470, y=840, color="green", size=34),
        A("badge", ok=True, at="fixed", x=1750, y=290),
        A("confetti", at="fixed", x=1470, y=480),
    )),
    # 10. being a good sport ---------------------------------------------------------------------------
    Scene("j2-w04-s10", setting="workshop", beats=(
        B("In Dice Race, the die decides who wins. Being fast or clever does not help.", speaker=AIDEN,
          cue="die", pause=0.5),
        B("So when we win, we do not tease. When we lose, we do not get angry at the computer or at a friend.",
          speaker=AIDEN, cue="win", pause=0.5),
        B("A good sport says good game, has another go, and is happy for the winner.", speaker=AIDEN,
          cue="sport", pause=0.6),
        B("What can you say when you lose?", speaker=AIDEN, cue="lose", pause=2.8),
        B("Good game! Want to play again? Next time, maybe me!", speaker=AIDEN, cue="say", pause=0.6),
        B("High five!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=280, y=980, s=0.85, moods={"start": "happy", "lose": "thinking", "say": "proud"},
          chin=("lose$", "say"), wave=("pixi", "end")),
        A("pixi", x=560, y=800, s=0.7, ground=960, moods={"pixi": "proud"}),
        A("icons", at="win", x=1260, y=460, gap=300,
          items=[("trophy", "Win: no teasing", "win@0.2"), ("heart", "Lose: stay kind", "win@0.6"),
                 ("person", "Good game!", "sport")]),
        A("thought", "What can you say?", at="lose$+0.2", until="say", x=1260, y=780),
        A("chip", "Good game!", at="say", x=1000, y=750, color="green", size=44),
        A("chip", "Want to play again?", at="say@0.3", x=1500, y=750, color="sky", size=44),
        A("chip", "Next time, maybe me!", at="say@0.65", x=1260, y=865, color="yellow", size=44),
    )),
    # 11. recap and next ---------------------------------------------------------------------------------
    Scene("j2-w04-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Random!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Pick random!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Surprise!", speaker=AIDEN, cue="w3", pause=1.2),
        B("Random picks a number nobody can guess. Every time the block runs, it rolls again.", speaker=AIDEN,
          cue="recap", pause=0.4),
        B("For a new number every time, the roll goes inside the loop.", speaker=AIDEN, cue="recap2", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Build Dice Race, make Ghost Pop, then fix the Stuck Dice.", speaker=AIDEN, cue="next", pause=0.5),
        B("Tip: drag the cat's script onto the Ballerina, and change c to b. Then race!", speaker=AIDEN,
          cue="tip", pause=0.5),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Random!", at="w1", until="w1>", y=560, size=90, color="purple"),
        A("bigtext", "Pick random!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Surprise!", at="w3", until="w3>", y=560, size=90, color="orange"),
        A("chip", "random = nobody can guess it", at="recap", until="turn", x=1200, y=520, color="purple",
          size=44),
        A("chip", "roll inside the loop = new every time", at="recap2", until="turn", x=1200, y=650,
          color="green", size=40),
        A("banner", "NEXT: Dice Race, Ghost Pop, The Stuck Dice", at="turn", color="green", size=50),
        A("cards", items=["Build Dice Race", "Make Ghost Pop", "Fix the Stuck Dice"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.45", "next@0.8"], at="next"),
        A("chip", "Ballerina: change c to b", at="tip", x=1320, y=760, color="sky", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
