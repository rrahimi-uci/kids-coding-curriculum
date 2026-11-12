"""Junior Level 1 Week 4: Repeat It! (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/1-little-robots/teaching-material/lessons/week04.tex: the dance-loops warm-up (the long
way, then STOMP, STOMP, CLAP inside a REPEAT 3 card; too many with 10, too few with 1), the Scratch
repeat block (a big letter C) and the brushing-teeth analogy, costumes and animation, the worked
example Exercise 4.1 Dance, Ballerina! (the long way first, then repeat 4 around next costume and
wait 1 seconds), the exit question as a quick quiz (repeat 3 around Meow), Exercise 4.2 The Noisy Cat
(Leo's repeat 10: too many), sharing the mouse fairly with the timer, and the recap.
Kit note: the stage cannot change costumes, so Pixi acts out the Ballerina's four dance moves.
Exercise 4.3 (Mei's ballerina, too many or too few?) is named for home but not answered.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
NEXT = ("looks", "next costume")
WAIT = ("control", "wait [1] seconds")
MEOW = ("sound", "play sound [Meow] until done")
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage

LONG = ["STOMP", "STOMP", "CLAP"] * 3
POSES = ["surprised", "proud", "happy", "thinking"]


def pixi_dance(base: str, x: float, y: float, every: float = 1.0, moves: int = 4, first: float = 0.4):
    """Pixi hops into a new pose on every move: (path, moods) keyed on `base`."""
    path, moods = [(base, x, y)], {}
    for i in range(moves):
        t = first + i * every
        dx = 50 if i % 2 == 0 else -50
        path += [(f"{base}+{t:.2f}", x + dx, y - 40), (f"{base}+{t + 0.45:.2f}", x, y)]
        moods[f"{base}+{t:.2f}"] = POSES[i % len(POSES)]
    return path, moods


S6_PATH, S6_MOODS = pixi_dance("test", 1450, 760, moves=2, first=0.6)
S7_PATH, S7_MOODS = pixi_dance("count", 1450, 760, every=1.1, first=0.2)
S7_MOODS = {"start": "happy", **S7_MOODS, "wow": "proud"}
MEOWS10 = [(f"test+{0.5 + 0.6 * i:.2f}", "say", "Meow!", 0.45) for i in range(10)]
MEOWS3 = [(f"again+{0.5 + 0.6 * i:.2f}", "say", "Meow!", 0.45) for i in range(3)]

EPISODE = Episode(level="j1", week=4, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w04-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, coders! It's Aiden and Pixi again!", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, we were bug detectives: test, look, change one thing.", speaker=AIDEN, cue="last",
          pause=0.5),
        B("Today, we learn a coding superpower. It is called repeat!", speaker=AIDEN, cue="today", pause=0.4),
        B("And we will make a ballerina dance. Are you ready to dance?", speaker=AIDEN, cue="dance", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("dance", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("chip", "test • look • change one thing", at="last", until="today", x=1300, y=420, color="yellow",
          size=42),
        A("bigtext", "repeat", at="today@0.6", x=1300, y=500, size=90, color="orange"),
        A("banner", "MISSION: Make the ballerina dance", at="dance"),
    )),
    # 2. warm-up: the long way (dance along) ------------------------------------------------------------
    Scene("j1-w04-s02", setting="workshop", beats=(
        B("Let's warm up with a dance. Stand up!", speaker=AIDEN, cue="up", pause=0.4),
        B("Here are our dance cards, the long way. Dance with me!", speaker=AIDEN, cue="cards", pause=0.5),
        B("Stomp, stomp, clap! Stomp, stomp, clap! Stomp, stomp, clap!", speaker=AIDEN, cue="do", pause=0.8),
        B("Phew! That was a lot of cards!", speaker=AIDEN, cue="phew", pause=0.5),
        B("Do you see a part that happens again and again?", speaker=AIDEN, cue="again", pause=3.0),
        B("Yes! Stomp, stomp, clap. Three times!", speaker=AIDEN, cue="yes", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("up", "up$"), ("do", "do$")],
          moods={"start": "happy", "phew": "surprised", "again": "thinking", "yes": "proud"},
          chin=("again$", "yes")),
        A("pixi", x=520, y=860, s=0.62, ground=1000, moods={"do": "proud", "phew": "surprised", "yes": "happy"},
          path=[("do", 520, 860), ("do@0.3", 520, 820), ("do@0.35", 520, 860), ("do@0.63", 520, 820),
                ("do@0.68", 520, 860), ("do@0.96", 520, 820), ("do$", 520, 860)]),
        A("listrow", "The long way", items=LONG, x=1150, y=480, cell=150, indexes=False, at="cards",
          highlight=[(f"do@{i / 9:.3f}", f"do@{(i + 1) / 9:.3f}", i) for i in range(9)]
          + [("yes", "end", i) for i in range(3)]),
        A("chip", "9 cards!", at="phew", until="again", x=1150, y=720, color="red", size=50),
        A("thought", "Again and again?", at="again$+0.2", until="yes", x=1150, y=740),
        A("chip", "stomp, stomp, clap: 3 times", at="yes", x=1150, y=720, color="orange", size=46),
    )),
    # 3. warm-up: the REPEAT card, too many and too few ------------------------------------------------
    Scene("j1-w04-s03", setting="workshop", beats=(
        B("So we put stomp, stomp, clap inside a loop, with a REPEAT card on top.", speaker=AIDEN, cue="loop",
          pause=0.5),
        B("REPEAT 3 says: do the steps inside the loop three times.", speaker=AIDEN, cue="three", pause=0.5),
        B("It is the same dance, with fewer cards!", speaker=AIDEN, cue="same", pause=0.6),
        B("Now, what if the number is ten?", speaker=AIDEN, cue="ten", pause=2.8),
        B("Stomp, stomp, clap, on and on and on! Too many!", speaker=AIDEN, cue="many", pause=0.5),
        B("And what if it is one? The dance is over before it starts. Too few!", speaker=AIDEN, cue="one",
          pause=0.5),
        B("Three is the right number. Beep!", speaker=PIXI, cue="right", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, moods={"start": "happy", "ten": "thinking", "many": "surprised",
                                                 "one": "happy", "right": "proud"}, chin=("ten$", "many")),
        A("pixi", x=520, y=860, s=0.62, ground=1000, moods={"many": "worried", "right": "proud"}),
        A("panel", "REPEAT 3", x=760, y=260, w=520, until="ten",
          items=[("loop@0.3", "STOMP"), ("loop@0.4", "STOMP"), ("loop@0.5", "CLAP")], size=44, color="orange"),
        A("panel", "REPEAT 10", x=760, y=260, w=520, at="ten", until="one",
          items=["STOMP", "STOMP", "CLAP"], size=44, color="red"),
        A("panel", "REPEAT 1", x=760, y=260, w=520, at="one", until="right",
          items=["STOMP", "STOMP", "CLAP"], size=44, color="red"),
        A("panel", "REPEAT 3", x=760, y=260, w=520, at="right", items=["STOMP", "STOMP", "CLAP"], size=44,
          color="green"),
        A("chip", "3 cards, not 9!", at="same", until="ten", x=1020, y=760, color="green", size=48),
        A("thought", "Ten times?", at="ten$+0.2", until="many", x=1560, y=420),
        A("chip", "Too many!", at="many@0.6", until="one", x=1020, y=760, color="red", size=50),
        A("chip", "Too few!", at="one@0.6", until="right", x=1020, y=760, color="red", size=50),
        A("chip", "Right number!", at="right", x=1020, y=760, color="green", size=50),
    )),
    # 4. the repeat block --------------------------------------------------------------------------------
    Scene("j1-w04-s04", setting="lavender", beats=(
        B("Scratch has a repeat block too. It is in the orange Control circle.", speaker=AIDEN, cue="block",
          pause=0.5),
        B("It looks like a big letter C, like a hug. Can you make a C with your hand?", speaker=AIDEN, cue="c",
          pause=2.2),
        B("The blocks inside the C run again and again. The number says how many times.", speaker=AIDEN,
          cue="inside", pause=0.6),
        B("It's like brushing your teeth. A grown-up does not say: brush, brush, brush, brush, brush.",
          speaker=AIDEN, cue="brush", pause=0.4),
        B("They say: brush ten times! That is a repeat.", speaker=AIDEN, cue="ten", pause=0.8),
    ), actions=(
        A("scratch", "Control: orange", blocks=[("control", "repeat [10]", [])], x=180, y=300, w=760, h=380,
          scale=BIG, at="block", highlight=[(0, "c", "c$")]),
        A("chip", "a big letter C", at="c", until="brush", x=1380, y=320, color="orange", size=48),
        A("chip", "inside = again and again", at="inside", until="brush", x=1380, y=460, color="yellow",
          size=44),
        A("chip", "the number = how many times", at="inside@0.6", until="brush", x=1380, y=600, color="sky",
          size=42),
        A("chip", "brush, brush, brush, brush...", at="brush@0.5", until="ten", x=1380, y=400, color="white",
          size=42),
        A("bigtext", "brush 10 times!", at="ten", x=1380, y=560, size=72, color="green"),
        A("aiden", x=200, y=1080, s=0.5, moods={"start": "happy", "ten": "proud"}),
    )),
    # 5. costumes and animation --------------------------------------------------------------------------
    Scene("j1-w04-s05", setting="sky", beats=(
        B("Here is one more new word: costume.", speaker=AIDEN, cue="word", pause=0.4),
        B("Sprites have costumes. A costume is a different picture of the same sprite, like a different pose.",
          speaker=AIDEN, cue="pose", pause=0.6),
        B("Watch Pixi change poses, again and again.", speaker=AIDEN, cue="watch", pause=4.4),
        B("It looks like Pixi is moving! That is called animation, like a cartoon.", speaker=AIDEN, cue="anim",
          pause=0.5),
        B("Beep! I'm a cartoon!", speaker=PIXI, cue="cartoon", pause=0.8),
    ), actions=(
        A("chip", "costume = a different picture of the same sprite", at="pose", until="anim", x=960, y=200,
          color="purple", size=40),
        A("pixi", x=960, y=760, s=1.0, moods={"start": "happy", **pixi_dance("watch", 960, 760, every=0.9,
                                                                              first=0.3)[1], "anim": "proud"},
          path=pixi_dance("watch", 960, 760, every=0.9, first=0.3)[0]),
        A("chip", "1", at="watch+0.3", until="anim", x=560, y=520, color="sky", size=56),
        A("chip", "2", at="watch+1.2", until="anim", x=560, y=640, color="sky", size=56),
        A("chip", "3", at="watch+2.1", until="anim", x=1360, y=520, color="sky", size=56),
        A("chip", "4", at="watch+3.0", until="anim", x=1360, y=640, color="sky", size=56),
        A("chip", "animation = changing costumes again and again", at="anim", x=960, y=200, color="orange",
          size=40),
    )),
    # 6. Dance, Ballerina! the long way --------------------------------------------------------------
    Scene("j1-w04-s06", setting="mint", beats=(
        B("Let's build Dance, Ballerina! First, click Choose a Sprite, the round cat button under the stage, "
          "and pick Ballerina.", speaker=AIDEN, cue="choose", pause=0.5),
        B("Click the Costumes tab. Look: she has four costumes. Four dance moves! Then click the Code tab.",
          speaker=AIDEN, cue="costumes", pause=0.6),
        B("Now, the yellow Events circle: when green flag clicked.", speaker=AIDEN, cue="events", pause=0.6),
        B("Let's try the long way. Purple Looks: next costume. Orange Control: wait one seconds. And again.",
          speaker=AIDEN, cue="long", pause=0.6),
        B("Pixi will be our ballerina. Click the flag!", speaker=AIDEN, cue="test", pause=2.4),
        B("Two moves. For four moves, we would need eight blocks! There is a shorter way.", speaker=AIDEN,
          cue="eight", pause=0.6),
        B("Drag these blocks back to the left. That deletes them.", speaker=AIDEN, cue="delete", pause=0.8),
    ), actions=(
        A("banner", "Exercise 4.1: Dance, Ballerina!", at="choose", color="green"),
        A("chip", "Choose a Sprite: Ballerina", at="choose@0.4", until="costumes", x=960, y=440, color="white",
          size=48),
        A("chip", "4 costumes = 4 dance moves", at="costumes@0.4", until="events", x=960, y=440, color="purple",
          size=48),
        A("scratch", "The long way", blocks=[FLAG, NEXT, WAIT, NEXT, WAIT], x=130, y=260, w=880, h=700, scale=BIG,
          at="events", until="delete@0.6",
          reveal=["events", "long@0.3", "long@0.55", "long@0.8", "long@0.9"]),
        A("pixi", x=1450, y=760, at="long", moods={"start": "happy", **S6_MOODS, "eight": "happy"}, path=S6_PATH),
        A("chip", "Ballerina", at="long", x=1450, y=960, color="white", size=40),
        A("chip", "8 blocks? Too many!", at="eight@0.4", until="delete@0.6", x=1450, y=360, color="red", size=44),
        A("sfx", "whoosh", at="delete@0.6"),
    )),
    # 7. the repeat way ------------------------------------------------------------------------------
    Scene("j1-w04-s07", setting="mint", beats=(
        B("Here is the repeat way. From orange Control, drag repeat ten under the green flag block.",
          speaker=AIDEN, cue="repeat", pause=0.6),
        B("Drag next costume into the mouth of the C. Then wait one seconds under it, still inside.",
          speaker=AIDEN, cue="inside", pause=0.6),
        B("Now change ten to four, for four moves.", speaker=AIDEN, cue="four", pause=0.6),
        B("Click the green flag, and count her moves with me!", speaker=AIDEN, cue="flag", pause=0.3),
        B("One, two, three, four!", speaker=AIDEN, cue="count", pause=1.0),
        B("Four moves, with only three blocks! She ends in the pose where she started.", speaker=AIDEN, cue="wow",
          pause=0.4),
        B("Beep! I love to dance!", speaker=PIXI, cue="love", pause=0.8),
    ), actions=(
        A("scratch", "Dance, Ballerina!", blocks=[FLAG, ("control", "repeat [10]", [NEXT, WAIT])], x=130, y=260,
          w=880, h=560, scale=BIG, reveal=["start", "repeat@0.6", "inside@0.35", "inside@0.8"],
          edits=[("four@0.6", 1, "repeat [4]")],
          highlight=[(1, "four", "four$+0.3"), (2, "count", "count@0.12"), (3, "count@0.12", "count@0.25"),
                     (2, "count@0.25", "count@0.37"), (3, "count@0.37", "count@0.5"),
                     (2, "count@0.5", "count@0.62"), (3, "count@0.62", "count@0.75"),
                     (2, "count@0.75", "count@0.87"), (3, "count@0.87", "count$")]),
        A("chip", "Control: orange", at="repeat", until="inside", x=1450, y=360, color="orange", size=44),
        A("chip", "inside the C", at="inside", until="four", x=1450, y=360, color="yellow", size=46),
        A("chip", "10 → 4", at="four", until="flag", x=1450, y=360, color="sky", size=52),
        A("pixi", x=1450, y=760, moods=S7_MOODS, path=S7_PATH),
        A("chip", "Ballerina", x=1450, y=960, color="white", size=40),
        A("bigtext", "1", at="count", until="count@0.24", x=1450, y=380, size=110, color="purple"),
        A("bigtext", "2", at="count@0.25", until="count@0.49", x=1450, y=380, size=110, color="purple"),
        A("bigtext", "3", at="count@0.5", until="count@0.74", x=1450, y=380, size=110, color="purple"),
        A("bigtext", "4", at="count@0.75", until="wow", x=1450, y=380, size=110, color="purple"),
        A("badge", ok=True, at="wow", x=1760, y=300),
        A("confetti", at="wow", x=1450, y=480),
    )),
    # 8. quick quiz: how many meows? -----------------------------------------------------------------
    Scene("j1-w04-s08", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("This repeat says three, around play sound Meow. How many meows will we hear?", speaker=AIDEN,
          cue="how", pause=3.2),
        B("Three meows! The repeat says three.", speaker=AIDEN, cue="three", pause=0.5),
        B("Now I want five meows. What do I change?", speaker=AIDEN, cue="five", pause=3.2),
        B("Change the three to five!", speaker=AIDEN, cue="change", pause=0.4),
        B("Meow, meow, meow, meow, meow!", speaker=PIXI, cue="meow", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Quiz script", blocks=[FLAG, ("control", "repeat [3]", [MEOW])], x=180, y=300, w=880, h=460,
          scale=BIG, at="how", edits=[("change@0.5", 1, "repeat [5]")],
          highlight=[(1, "three", "three$"), (1, "change", "change$+0.4")]),
        A("thought", "How many meows?", at="how$+0.2", until="three", x=1460, y=480),
        A("chip", "3 meows", at="three", until="five", x=1460, y=480, color="pink", size=56),
        A("thought", "What do I change?", at="five$+0.2", until="change", x=1460, y=480),
        A("chip", "3 → 5", at="change", x=1460, y=480, color="sky", size=56),
        A("pixi", x=1460, y=880, s=0.55, at="change", ground=980),
    )),
    # 9. bug hunt: The Noisy Cat ---------------------------------------------------------------------
    Scene("j1-w04-s09", setting="mint", beats=(
        B("Bug hunt time! Leo wants his cat to meow three times.", speaker=AIDEN, cue="bug", pause=0.4),
        B("Here is Leo's script. Click the cat first, so the script goes on the cat.", speaker=AIDEN, cue="leo",
          pause=0.5),
        B("Test! Count the meows with me!", speaker=AIDEN, cue="test", pause=6.6),
        B("Ten meows! Too many! The red stop sign can stop it early.", speaker=AIDEN, cue="ten", pause=0.5),
        B("Which number do we change?", speaker=AIDEN, cue="which", pause=3.0),
        B("The number in the repeat! Change ten to three.", speaker=AIDEN, cue="fix", pause=0.6),
        B("Test again!", speaker=AIDEN, cue="again", pause=2.6),
        B("One, two, three meows. Bug fixed! Like our dance with ten: too many.", speaker=AIDEN, cue="fixed",
          pause=0.4),
        B("Ahh, nice and quiet. Beep!", speaker=PIXI, cue="quiet", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Noisy Cat", at="bug", color="navy"),
        A("scratch", "Leo's script", blocks=[FLAG, ("control", "repeat [10]", [MEOW])], x=130, y=260, w=900,
          h=460, scale=BIG, at="leo", edits=[("fix@0.7", 1, "repeat [3]")],
          highlight=[(2, "test+0.5", "test+6.4"), (1, "which$", "fix$+0.4"), (2, "again+0.5", "again+2.3")]),
        A("stage", x=1100, y=230, w=700, h=480, at="leo", flag_at="test+0.4", sprite_scale=CAT,
          actions=MEOWS10 + MEOWS3),
        A("sfx", "pop", at="again+0.4"),
        *[A("chip", str(i + 1), at=f"test+{0.5 + 0.6 * i:.2f}", until=f"test+{1.05 + 0.6 * i:.2f}", x=1450, y=860,
            color="pink", size=60) for i in range(10)],
        A("badge", ok=False, at="ten", until="again", x=1760, y=290),
        A("chip", "Too many!", at="ten", until="which", x=1450, y=860, color="red", size=50),
        A("thought", "Which number?", at="which$+0.2", until="fix", x=1450, y=870),
        A("chip", "10 → 3", at="fix", until="again", x=1450, y=860, color="sky", size=56),
        *[A("chip", str(i + 1), at=f"again+{0.5 + 0.6 * i:.2f}", until=f"again+{1.05 + 0.6 * i:.2f}", x=1450,
            y=860, color="pink", size=60) for i in range(3)],
        A("badge", ok=True, at="fixed", x=1760, y=290),
        A("confetti", at="fixed", x=1450, y=470),
        A("chip", "3 meows!", at="fixed@0.3", x=1450, y=860, color="green", size=52),
    )),
    # 10. fair turns with the timer ----------------------------------------------------------------
    Scene("j1-w04-s10", setting="workshop", beats=(
        B("When you code with a partner, the timer decides whose turn it is.", speaker=AIDEN, cue="timer",
          pause=0.4),
        B("Not who is bigger, older or faster. The timer!", speaker=AIDEN, cue="not", pause=0.5),
        B("When the timer runs out, the Driver lets go of the mouse and says: your turn!", speaker=AIDEN,
          cue="turn", pause=0.4),
        B("And the Helper says: thanks!", speaker=PIXI, cue="thanks", pause=0.5),
        B("Helpers keep their hands in their lap, and point with a finger. Nobody grabs.", speaker=AIDEN,
          cue="lap", pause=0.6),
        B("Let's practice. Say it with me: your turn!", speaker=AIDEN, cue="practice", pause=1.8),
        B("Thanks!", speaker=PIXI, cue="thanks2", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "lap": "proud"}, point=("lap", "lap$")),
        A("pixi", x=620, y=760, moods={"thanks": "proud"}),
        A("icons", x=1300, y=420, gap=320,
          items=[("clock", "The timer", "timer@0.5"), ("laptop", "Driver: your turn!", "turn@0.5"),
                 ("heart", "Helper: thanks!", "thanks")]),
        A("chip", "Nobody grabs", at="lap@0.5", until="practice", x=1300, y=760, color="green", size=50),
        A("bigtext", "Your turn! Thanks!", at="practice@0.5", x=1300, y=780, size=64, color="green"),
    )),
    # 11. recap and next -------------------------------------------------------------------------------
    Scene("j1-w04-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Repeat!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Costume!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Animation!", speaker=AIDEN, cue="w3", pause=1.2),
        B("A repeat does the blocks inside it again, as many times as the number says.", speaker=AIDEN,
          cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Make the ballerina dance, fix the Noisy Cat, then check Mei's ballerina: too many, or too few?",
          speaker=AIDEN, cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Repeat!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Costume!", at="w2", until="w2>", y=560, size=90, color="purple"),
        A("bigtext", "Animation!", at="w3", until="w3>", y=560, size=90, color="green"),
        A("chip", "repeat = again, as many times as the number", at="recap", until="turn", x=1150, y=560,
          color="orange", size=42),
        A("banner", "NEXT: Dance, Ballerina! and The Noisy Cat", at="turn", color="green"),
        A("cards", items=["Dance, Ballerina!", "Fix the Noisy Cat", "Too Many or Too Few?"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.4", "next@0.7"], at="next"),
        A("chip", "Swap on the timer", at="next$", x=1320, y=760, color="sky", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
