"""Junior Level 1 Week 3: Bugs Are Clues (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/1-little-robots/teaching-material/lessons/week03.tex: the "spot the difference" warm-up
(Pixi gets dressed: shoes before socks, then far too fast, fixed with WAIT cards), a bug is a clue, the
three detective steps (test, look, change one thing) and the word debugging, the worked example
Exercise 3.1 Ready, Set, Go! (plain say blocks, then a wait block added one at a time), the exit
question as a quick quiz (say Hi! then say Bye!), Exercise 3.2 The Sleepy Cat (bug hunt: think Zzz in
the wrong place), kind bug words, the slow-motion robots wiggle break, and the recap.
Kit note: the stage has no think bubble, so the sleeping cat's "think Zzz" shows as a Zzz bubble.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
READY = ("looks", "say [Ready]")
SET = ("looks", "say [Set]")
GO = ("looks", "say [Go!]")
GLIDE = ("motion", "glide [1] secs to [random position]")
WAIT = ("control", "wait [1] seconds")
MORNING = ("looks", "say [Good morning!] for [2] seconds")
MOVE = ("motion", "move [50] steps")
ZZZ = ("looks", "think [Zzz] for [2] seconds")
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage

DRESS = ["PUT ON SOCKS", "PUT ON SHOES", "PUT ON HAT", "WAVE BYE"]
DRESS_WAIT = ["PUT ON SOCKS", "WAIT", "PUT ON SHOES", "WAIT", "PUT ON HAT", "WAIT", "WAVE BYE"]

EPISODE = Episode(level="j1", week=3, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w03-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, coders! It's me, Aiden, and my robot friend, Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello again!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, we made the cat talk, meow and move in Scratch.", speaker=AIDEN, cue="last", pause=0.5),
        B("Today, we become bug detectives!", speaker=AIDEN, cue="today", pause=0.4),
        B("A bug is a mistake in a program. And here is a secret: a bug is not bad news. A bug is a clue!",
          speaker=AIDEN, cue="clue", pause=0.6),
        B("Grab your magnifying glass. Let's go!", speaker=AIDEN, cue="go", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("go", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("cat", x=1480, y=900, s=1.0, at="last", until="today", talk=("last@0.3", "last$")),
        A("banner", "MISSION: Be a bug detective", at="today"),
        A("chip", "bug = a mistake in a program", at="clue", until="go", x=1300, y=420, color="yellow", size=44),
        A("chip", "A bug is a clue!", at="clue@0.7", x=1300, y=560, color="orange", size=52),
        A("magnifier", x=1300, y=780, s=1.2, at="go"),
    )),
    # 2. warm-up: Pixi gets dressed (steps in the wrong order) ------------------------------------
    Scene("j1-w03-s02", setting="workshop", beats=(
        B("Let's warm up. Here is Pixi's plan for getting dressed.", speaker=AIDEN, cue="plan", pause=0.6),
        B("Uh oh. Somebody swapped two cards! Watch closely. Does Pixi do the plan?", speaker=AIDEN, cue="swap",
          pause=0.6),
        B("Shoes on! Now socks... over my shoes? Beep?", speaker=PIXI, cue="shoes", pause=0.8),
        B("Ha ha! What was different from the plan?", speaker=AIDEN, cue="diff", pause=3.0),
        B("The shoes came before the socks! That was a bug: steps in the wrong order.", speaker=AIDEN,
          cue="order", pause=0.5),
        B("We swap the two cards back. Socks first, then shoes!", speaker=AIDEN, cue="back", pause=0.8),
    ), actions=(
        A("aiden", x=250, y=980, s=0.8, moods={"start": "happy", "shoes": "surprised", "diff": "thinking",
                                               "order": "happy"}, chin=("diff$", "order")),
        A("cards", items=DRESS, x=520, y=280, w=520, gap=130, size=40, until="back+0.8",
          reveal=["plan@0.4", "plan@0.55", "plan@0.7", "plan@0.85"], reorder=("swap@0.15", [1, 0, 2, 3]),
          active=[("shoes@0.6", "diff"), ("shoes", "shoes@0.6"), None, None]),
        A("cards", items=DRESS, x=520, y=280, w=520, gap=130, size=40, at="back+0.8"),
        A("pixi", x=1450, y=760, moods={"shoes": "confused", "order": "happy"}),
        A("bubble", "Shoes on!", who="pixi", x=1450, y=760, at="shoes", until="shoes@0.45"),
        A("bubble", "Socks... over my shoes?", who="pixi", x=1450, y=760, at="shoes@0.45", until="diff"),
        A("thought", "What was different?", at="diff$+0.2", until="order", x=1450, y=360),
        A("chip", "Bug: steps in the wrong order", at="order@0.4", x=1450, y=360, color="red", size=40),
    )),
    # 3. warm-up: too fast to see (WAIT cards) ------------------------------------------------------
    Scene("j1-w03-s03", setting="workshop", beats=(
        B("Now Pixi does the plan super fast!", speaker=AIDEN, cue="fast", pause=0.3),
        B("Socks, shoes, hat, bye!", speaker=PIXI, cue="blur", pause=0.6),
        B("Did you see Pixi put on the hat?", speaker=AIDEN, cue="hat", pause=3.0),
        B("Not really! It was too fast to see.", speaker=AIDEN, cue="no", pause=0.5),
        B("So we put a WAIT card between the steps. WAIT means: stop, and count to one.", speaker=AIDEN,
          cue="wait", pause=0.6),
        B("Count with me! Socks, one. Shoes, one. Hat, one. Wave!", speaker=AIDEN, cue="count", pause=0.8),
        B("Now we can see every step. Today, Scratch has a wait block too.", speaker=AIDEN, cue="see", pause=0.8),
    ), actions=(
        A("aiden", x=250, y=980, s=0.8, moods={"start": "happy", "hat": "thinking", "no": "happy",
                                               "see": "proud"}, chin=("hat$", "no"), wave=("count", "count$")),
        A("cards", items=DRESS, x=520, y=280, w=520, gap=130, size=40, until="wait@0.4",
          active=[("blur", "blur@0.25"), ("blur@0.25", "blur@0.5"), ("blur@0.5", "blur@0.75"),
                  ("blur@0.75", "blur$")]),
        A("cards", items=DRESS_WAIT, x=520, y=230, w=520, gap=100, size=36, at="wait@0.4",
          reveal=["wait@0.4", "wait@0.6", "wait@0.4", "wait@0.7", "wait@0.4", "wait@0.8", "wait@0.4"],
          active=[("count@0.15", "count@0.25"), ("count@0.25", "count@0.35"), ("count@0.35", "count@0.5"),
                  ("count@0.5", "count@0.6"), ("count@0.6", "count@0.72"), ("count@0.72", "count@0.85"),
                  ("count@0.85", "count$+0.4")]),
        A("pixi", x=1450, y=760, moods={"blur": "surprised", "hat": "happy", "count": "proud"}),
        A("thought", "Did I see the hat?", at="hat$+0.2", until="no", x=1450, y=360),
        A("chip", "WAIT = stop and count to one", at="wait", until="see", x=1450, y=360, color="orange", size=40),
        A("chip", "Now we see every step!", at="see", x=1450, y=360, color="green", size=44),
    )),
    # 4. the three detective steps -------------------------------------------------------------------
    Scene("j1-w03-s04", setting="lavender", beats=(
        B("Every coder finds bugs, every day. Even grown-up coders!", speaker=AIDEN, cue="every", pause=0.5),
        B("When we find a bug, we do three things. Count them on your fingers!", speaker=AIDEN, cue="three",
          pause=0.6),
        B("One: test. Click the green flag and watch.", speaker=AIDEN, cue="test", pause=0.6),
        B("Two: look. What happened? What did we want to happen?", speaker=AIDEN, cue="look", pause=0.6),
        B("Three: change one thing. Then test again.", speaker=AIDEN, cue="change", pause=0.6),
        B("Finding and fixing bugs is called debugging.", speaker=AIDEN, cue="debug", pause=0.5),
        B("Test, look, change one thing! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("cards", items=["Test", "Look", "Change one thing"], x=200, y=300, w=620, gap=150, size=48,
          color="green", reveal=["test", "look", "change"],
          active=[("test", "test>"), ("look", "look>"), ("change", "change>")]),
        A("chip", "Every coder finds bugs", at="every", until="three", x=1360, y=300, color="yellow", size=46),
        A("magnifier", x=1360, y=560, s=1.2, at="look", until="debug"),
        A("chip", "debugging = finding and fixing bugs", at="debug", x=1360, y=300, color="purple", size=40),
        A("pixi", x=1400, y=860, s=0.6, at="debug", ground=960),
        A("aiden", x=200, y=1080, s=0.5, moods={"start": "happy", "debug": "proud"}, wave=("three", "three$")),
    )),
    # 5. build Ready, Set, Go! -----------------------------------------------------------------------
    Scene("j1-w03-s05", setting="mint", beats=(
        B("Let's build a script called Ready, Set, Go!", speaker=AIDEN, cue="build", pause=0.5),
        B("First, the yellow Events circle. Drag in: when green flag clicked.", speaker=AIDEN, cue="events",
          pause=0.8),
        B("Next, the purple Looks circle. Find the plain say block, the one with no seconds. Snap it on, and "
          "type: Ready.", speaker=AIDEN, cue="looks", pause=0.8),
        B("Snap on two more plain say blocks. Type: Set. And: Go!", speaker=AIDEN, cue="more", pause=0.8),
        B("Last, the blue Motion circle. Snap on: glide one second to random position.", speaker=AIDEN,
          cue="motion", pause=0.8),
        B("The cat should say Ready, then Set, then Go!", speaker=AIDEN, cue="should", pause=0.8),
    ), actions=(
        A("banner", "Exercise 3.1: Ready, Set, Go!", at="build", color="green"),
        A("scratch", "Ready, Set, Go!", blocks=[FLAG, READY, SET, GO, GLIDE], x=110, y=270, w=960, h=640,
          scale=BIG, reveal=["events", "looks@0.7", "more@0.3", "more@0.7", "motion@0.6"]),
        A("chip", "Events: yellow", at="events", until="events>", x=1460, y=560, color="yellow", size=44),
        A("chip", "Looks: purple", at="looks", until="more>", x=1460, y=560, color="purple", size=44),
        A("chip", "Use the plain say block", at="looks@0.3", until="more>", x=1460, y=680, color="white",
          size=40),
        A("chip", "Motion: blue", at="motion", until="motion>", x=1460, y=560, color="sky", size=44),
        A("chip", "Ready, then Set, then Go!", at="should", x=1460, y=560, color="orange", size=44),
    )),
    # 6. test and look: too fast ---------------------------------------------------------------------
    Scene("j1-w03-s06", setting="peach", beats=(
        B("Step one: test. Click the green flag, and watch closely!", speaker=AIDEN, cue="click", pause=3.0),
        B("Step two: look. Did you see Ready? Did you see Set?", speaker=AIDEN, cue="look", pause=3.0),
        B("No! The cat only said Go!", speaker=AIDEN, cue="no", pause=0.5),
        B("The computer is so fast that it said all three words in a blink.", speaker=AIDEN, cue="blink",
          pause=0.5),
        B("It is like a flip book. If you flip it really fast, you only see the last page.", speaker=AIDEN,
          cue="flip", pause=0.6),
        B("That is our clue!", speaker=AIDEN, cue="clue", pause=0.8),
    ), actions=(
        A("scratch", "Ready, Set, Go!", blocks=[FLAG, READY, SET, GO, GLIDE], x=110, y=270, w=960, h=640,
          scale=BIG, highlight=[(1, "click+0.6", "click+0.75"), (2, "click+0.75", "click+0.9"),
                                (3, "click+0.9", "click+1.1"), (4, "click+1.1", "click+2.1")]),
        A("stage", x=1080, y=230, w=760, h=520, flag_at="click+0.5", sprite_scale=CAT,
          actions=[("click+0.6", "say", "Ready", 0.05), ("click+0.7", "say", "Set", 0.05),
                   ("click+0.8", "say", "Go!", 30), ("click+1.1", "goto", 140, 60, 1.0)]),
        A("thought", "Ready? Set?", at="look$+0.2", until="no", x=1460, y=880),
        A("chip", "Too fast to see!", at="blink", until="clue", x=1460, y=870, color="red", size=46),
        A("chip", "Clue: the computer is very fast", at="clue", x=1460, y=870, color="yellow", size=40),
    )),
    # 7. change one thing: add wait blocks -----------------------------------------------------------
    Scene("j1-w03-s07", setting="mint", beats=(
        B("Step three: change one thing. Click the orange Control circle.", speaker=AIDEN, cue="change",
          pause=0.5),
        B("Drag wait one seconds in between say Ready and say Set.", speaker=AIDEN, cue="drag", pause=0.8),
        B("Test again!", speaker=AIDEN, cue="test2", pause=3.2),
        B("Now we see Ready, then Go! Better! But Set is still too fast. Another clue!", speaker=AIDEN,
          cue="better", pause=0.6),
        B("So we snap another wait between say Set and say Go!", speaker=AIDEN, cue="another", pause=0.8),
        B("Test!", speaker=AIDEN, cue="test3", pause=4.4),
        B("Ready, set, go! The cat dashes off!", speaker=AIDEN, cue="dash", pause=0.4),
        B("Woo-hoo! Beep!", speaker=PIXI, cue="woo", pause=0.8),
    ), actions=(
        A("scratch", "Ready, Set, Go!", blocks=[FLAG, READY, SET, GO, GLIDE], x=110, y=230, w=960, h=820,
          scale=BIG, until="drag@0.6"),
        A("scratch", "Ready, Set, Go!", blocks=[FLAG, READY, WAIT, SET, GO, GLIDE], x=110, y=230, w=960, h=820,
          scale=BIG, at="drag@0.6", until="another@0.6", highlight=[(2, "drag@0.6", "test2")]),
        A("scratch", "Ready, Set, Go!", blocks=[FLAG, READY, WAIT, SET, WAIT, GO, GLIDE], x=110, y=230, w=960,
          h=820, scale=BIG, at="another@0.6", highlight=[(4, "another@0.6", "test3")]),
        A("sfx", "snap", at="drag@0.6"),
        A("sfx", "snap", at="another@0.6"),
        A("chip", "Control: orange", at="change", until="test2", x=1460, y=870, color="orange", size=44),
        A("stage", x=1080, y=230, w=760, h=520, flag_at="test3+0.4", sprite_scale=CAT,
          actions=[("test2+0.5", "say", "Ready", 1.0), ("test2+1.5", "say", "Go!", 2.0),
                   ("test2+1.6", "goto", 140, 60, 1.0), ("better@0.6", "goto", 0, 0, 0.6),
                   ("test3+0.5", "say", "Ready", 1.0), ("test3+1.5", "say", "Set", 1.0),
                   ("test3+2.5", "say", "Go!", 2.5), ("test3+2.6", "goto", -150, 70, 1.0)]),
        A("sfx", "pop", at="test2+0.4"),
        A("chip", "Set is still too fast", at="better@0.4", until="test3", x=1460, y=870, color="red", size=44),
        A("badge", ok=True, at="dash", x=1760, y=300),
        A("confetti", at="dash", x=1460, y=480),
        A("chip", "wait = see every step", at="dash", x=1460, y=870, color="green", size=46),
    )),
    # 8. quick quiz: Hi and Bye --------------------------------------------------------------------
    Scene("j1-w03-s08", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("This script says Hi, and then Bye. There is no wait.", speaker=AIDEN, cue="script", pause=0.5),
        B("What will we see when we click the green flag?", speaker=AIDEN, cue="what", pause=3.2),
        B("Only Bye! The computer is too fast to show Hi.", speaker=AIDEN, cue="bye", pause=0.5),
        B("A wait block between them fixes it.", speaker=AIDEN, cue="fix", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Quiz script", blocks=[FLAG, ("looks", "say [Hi!]"), ("looks", "say [Bye!]")], x=180, y=300,
          w=860, h=420, scale=BIG, at="script"),
        A("thought", "Hi? Bye? Both?", at="what$+0.2", until="bye", x=1460, y=880),
        A("stage", x=1080, y=230, w=760, h=520, at="script", flag_at="bye", sprite_scale=CAT,
          actions=[("bye+0.1", "say", "Hi!", 0.05), ("bye+0.2", "say", "Bye!", 30)]),
        A("chip", "Only Bye!", at="bye@0.3", until="fix", x=1460, y=870, color="red", size=48),
        A("chip", "Put a wait in between", at="fix", x=1460, y=870, color="orange", size=46),
    )),
    # 9. bug hunt: The Sleepy Cat --------------------------------------------------------------------
    Scene("j1-w03-s09", setting="mint", beats=(
        B("Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.4),
        B("Sam's cat should sleep, then wake up, then walk. Here is Sam's script.", speaker=AIDEN, cue="sam",
          pause=0.6),
        B("Test!", speaker=AIDEN, cue="test", pause=5.2),
        B("Look: the cat said good morning, walked, and then fell asleep!", speaker=AIDEN, cue="look", pause=0.5),
        B("Which step is in the wrong place?", speaker=AIDEN, cue="which", pause=3.2),
        B("The think Zzz block! The cat should sleep first.", speaker=AIDEN, cue="found", pause=0.5),
        B("Change one thing: drag the bottom block up, and drop it right under the green flag block.",
          speaker=AIDEN, cue="fix", pause=0.8),
        B("Test again!", speaker=AIDEN, cue="again", pause=5.4),
        B("Zzz, good morning, and off it goes! Like Pixi's socks and shoes: the order matters.", speaker=AIDEN,
          cue="fixed", pause=0.4),
        B("Detective Aiden!", speaker=PIXI, cue="detective", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Sleepy Cat", at="bug", color="navy"),
        A("scratch", "Sam's script", blocks=[FLAG, MORNING, MOVE, ZZZ], x=110, y=260, w=960, h=560,
          scale=BIG, at="sam", until="fix@0.7",
          highlight=[(1, "test+0.2", "test+2.2"), (2, "test+2.2", "test+3.0"), (3, "test+3.0", "test+5.0"),
                     (3, "found", "fix@0.7")]),
        A("scratch", "Sam's script (fixed)", blocks=[FLAG, ZZZ, MORNING, MOVE], x=110, y=260, w=960, h=560,
          scale=BIG, at="fix@0.7", highlight=[(1, "fix@0.7", "fix$+0.6"), (1, "again+0.2", "again+2.2"),
                                               (2, "again+2.2", "again+4.2"), (3, "again+4.2", "again+5.0")]),
        A("sfx", "snap", at="fix@0.7"),
        A("sfx", "pop", at="test+0.1"),
        A("stage", x=1100, y=230, w=700, h=480, at="sam", flag_at="again+0.1", sprite_scale=CAT,
          actions=[("test+0.2", "say", "Good morning!", 2.0), ("test+2.2", "move", 50, 0.8),
                   ("test+3.0", "say", "Zzz...", 2.0), ("which", "goto", 0, 0, 0.5),
                   ("again+0.2", "say", "Zzz...", 2.0), ("again+2.2", "say", "Good morning!", 2.0),
                   ("again+4.2", "move", 50, 0.8)]),
        A("badge", ok=False, at="look", until="again", x=1760, y=290),
        A("chip", "Asleep at the end?", at="look@0.5", until="which", x=1450, y=860, color="red", size=44),
        A("thought", "Which block?", at="which$+0.2", until="found", x=1450, y=870),
        A("chip", "Sleep first!", at="found", until="again", x=1450, y=860, color="orange", size=48),
        A("badge", ok=True, at="fixed", x=1760, y=290),
        A("confetti", at="fixed", x=1450, y=470),
        A("chip", "The order matters", at="fixed@0.5", x=1450, y=860, color="green", size=46),
    )),
    # 10. kind bug words (say it with me) ----------------------------------------------------------
    Scene("j1-w03-s10", setting="workshop", beats=(
        B("Bug detectives use kind words.", speaker=AIDEN, cue="kind", pause=0.4),
        B("When you find a bug in your partner's work, you say: I think I found a clue!", speaker=AIDEN,
          cue="find", pause=0.5),
        B("When your partner finds a bug in your work, you say: Thanks! Let's test it.", speaker=AIDEN,
          cue="thanks", pause=0.5),
        B("We never laugh at a bug. Bugs happen to everyone.", speaker=AIDEN, cue="never", pause=0.6),
        B("Say it with me: I think I found a clue!", speaker=AIDEN, cue="say1", pause=2.4),
        B("Thanks! Let's test it!", speaker=PIXI, cue="say2", pause=2.2),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "never": "proud"}, point=("find", "find$")),
        A("pixi", x=640, y=760, moods={"say2": "proud"}),
        A("bubble", "I think I found a clue!", who="aiden", x=300, y=960, at="find@0.5", until="thanks"),
        A("bubble", "Thanks! Let's test it.", who="pixi", x=640, y=760, at="thanks@0.5", until="never"),
        A("icons", at="never", until="say1", x=1300, y=460, gap=300,
          items=[("heart", "Kind words", "never"), ("person", "Bugs happen to everyone", "never@0.5")]),
        A("bigtext", "I think I found a clue!", at="say1", until="say1>", x=1260, y=480, size=64, color="orange"),
        A("bigtext", "Thanks! Let's test it!", at="say2", until="say2>", x=1260, y=480, size=64, color="green"),
    )),
    # 11. slow-motion robots (wiggle break) --------------------------------------------------------
    Scene("j1-w03-s11", setting="workshop", beats=(
        B("Wiggle break! Let's be slow-motion robots. Stand up!", speaker=AIDEN, cue="up", pause=0.5),
        B("When I say move, wiggle like a robot. When I say wait, freeze!", speaker=AIDEN, cue="rules",
          pause=0.6),
        B("Move!", speaker=AIDEN, cue="m1", pause=1.6),
        B("Wait!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Move!", speaker=AIDEN, cue="m2", pause=1.6),
        B("Wait! One long wait. Freeze, two, three, four, five.", speaker=AIDEN, cue="w2", pause=1.0),
        B("Great freezing! You can sit down.", speaker=AIDEN, cue="sit", pause=0.4),
        B("Beep! Unfreeze!", speaker=PIXI, cue="unfreeze", pause=0.8),
    ), actions=(
        A("aiden", x=320, y=960, wave=[("up", "up$"), ("m1", "m1>"), ("m2", "m2>")],
          moods={"start": "happy", "w1": "surprised", "m2": "happy", "w2": "surprised", "sit": "proud"}),
        A("pixi", x=640, y=760, moods={"m1": "happy", "w1": "surprised", "m2": "happy", "w2": "surprised",
                                       "unfreeze": "happy"},
          path=[("m1", 640, 760), ("m1+0.5", 700, 740), ("m1+1.0", 640, 760), ("m2", 640, 760),
                ("m2+0.5", 580, 740), ("m2+1.0", 640, 760)]),
        A("bigtext", "MOVE!", at="m1", until="m1>", x=1350, y=480, size=100, color="green"),
        A("bigtext", "WAIT!", at="w1", until="w1>", x=1350, y=480, size=100, color="red"),
        A("bigtext", "MOVE!", at="m2", until="m2>", x=1350, y=480, size=100, color="green"),
        A("bigtext", "WAIT!", at="w2", until="w2>", x=1350, y=480, size=100, color="red"),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j1-w03-s12", setting="workshop", tail=0.8, beats=(
        B("Say the detective steps with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Test!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Look!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Change one thing!", speaker=AIDEN, cue="w3", pause=1.2),
        B("A bug is a clue. And a wait block helps us see every step.", speaker=AIDEN, cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Build Ready, Set, Go! Then fix The Sleepy Cat. Then make the cat tell a joke, with a wait in the "
          "middle.", speaker=AIDEN, cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Test!", at="w1", until="w1>", y=560, size=90, color="green"),
        A("bigtext", "Look!", at="w2", until="w2>", y=560, size=90, color="blue"),
        A("bigtext", "Change one thing!", at="w3", until="w3>", y=560, size=90, color="orange"),
        A("chip", "A bug is a clue", at="recap", until="turn", x=1200, y=480, color="yellow", size=48),
        A("chip", "wait = see every step", at="recap@0.5", until="turn", x=1200, y=620, color="orange", size=46),
        A("banner", "NEXT: Ready, Set, Go! and The Sleepy Cat", at="turn", color="green"),
        A("cards", items=["Build Ready, Set, Go!", "Fix The Sleepy Cat", "A joke with a wait"], x=1000, y=300,
          w=640, gap=120, reveal=["next@0.1", "next@0.35", "next@0.7"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
