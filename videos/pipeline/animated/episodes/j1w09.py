"""Junior Level 1 Week 9: Project Studio (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/1-little-robots/teaching-material/lessons/week09.tex: the three-box storyboard warm-up
(start, middle, end, with the event under each box), the card's must-haves, Mei's sample storyboard for
Grandpa, building one box at a time (the LEGO box picture), Mei's box 1 built step by step and tested,
the repeat for box 2 and the balloon's click script for box 3 (Mei's sample card, not a child's card),
Exercise 9.3 Partner Check as the bug hunt (a script with no hat block never starts), ask before you
show, the act-out-your-storyboard wiggle break and the next steps.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
CLICKED = ("event", "when this sprite clicked")
SAY = ("looks", "say [Happy birthday!] for [2] seconds")
MEOW = ("sound", "play sound [Meow] until done")
POP = ("sound", "play sound [Pop] until done")
SURPRISE = ("looks", "say [Surprise!] for [2] seconds")
DANCE = ("control", "repeat [4]", [("looks", "next costume"), ("control", "wait [1] seconds")])
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage

# Mei's sample storyboard, as three boxes side by side
BOARD = (
    A("panel", "1 Start", x=110, y=300, w=540, size=38, at="b1",
      items=[("b1@0.2", "cat says Happy birthday"), ("b1@0.6", "meow!")]),
    A("panel", "2 Middle", x=690, y=300, w=540, size=38, at="b2", items=[("b2@0.3", "cat dances")]),
    A("panel", "3 End", x=1270, y=300, w=540, size=38, at="b3",
      items=[("b3@0.3", "click the balloon:"), ("b3@0.6", "pop, Surprise!")]),
)

EPISODE = Episode(level="j1", week=9, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w09-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, coders! Aiden and Pixi here.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Welcome to the studio!", speaker=PIXI, cue="hello", pause=0.5),
        B("Last week, the cat drew a square with the pen.", speaker=AIDEN, cue="last", pause=0.5),
        B("Today is Project Studio. We make a big project: an animated greeting card for someone special.",
          speaker=AIDEN, cue="today", pause=0.5),
        B("First we plan it. Then we build it, one piece at a time. Let's go!", speaker=AIDEN, cue="ready",
          pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("chip", "pen down • quarter turn", at="last", until="today", x=1300, y=420, color="green", size=44),
        A("banner", "MISSION: My Animated Greeting Card", at="today"),
        A("icons", at="today@0.5", until="end", x=1340, y=480, gap=300,
          items=[("heart", "Someone special", "today@0.5"), ("star", "Plan, then build", "ready")]),
    )),
    # 2. warm-up: a three-box storyboard -------------------------------------------------------------
    Scene("j1-w09-s02", setting="workshop", beats=(
        B("Stories have a start, a middle and an end.", speaker=AIDEN, cue="story", pause=0.5),
        B("A storyboard is a plan in boxes. Movie makers draw one before they film.", speaker=AIDEN,
          cue="board", pause=0.6),
        B("Box one is the start. What happens when you click the green flag?", speaker=AIDEN, cue="b1",
          pause=0.6),
        B("Box two is the middle. What dances or moves again and again?", speaker=AIDEN, cue="b2", pause=0.6),
        B("Box three is the end. What surprise happens when you click a sprite or press a key?", speaker=AIDEN,
          cue="b3", pause=0.6),
        B("Draw a quick picture in each box. Stick figures are perfect! A grown-up can write the words.",
          speaker=AIDEN, cue="draw", pause=0.8),
    ), actions=(
        A("aiden", x=230, y=1000, s=0.75, moods={"start": "happy", "draw": "proud"}, point=("board", "board$")),
        A("pixi", x=440, y=860, s=0.55, ground=1000),
        A("cards", items=["Start: the green flag", "Middle: again and again", "End: a click or a key"],
          x=760, y=400, w=760, gap=140, reveal=["b1", "b2", "b3"], at="b1",
          active=[("b1", "b2"), ("b2", "b3"), ("b3", "draw")]),
        A("chip", "storyboard = a plan in boxes", at="board", until="b1", x=1140, y=420, color="orange", size=44),
        A("chip", "stick figures are perfect!", at="draw", x=1140, y=880, color="yellow", size=44),
    )),
    # 3. the must-haves ------------------------------------------------------------------------------
    Scene("j1-w09-s03", setting="lavender", beats=(
        B("Every greeting card needs five things.", speaker=AIDEN, cue="five", pause=0.4),
        B("The green flag to start it.", speaker=AIDEN, cue="m1", pause=0.4),
        B("A repeat, for a dance or an animation.", speaker=AIDEN, cue="m2", pause=0.4),
        B("A click or a key that does something.", speaker=AIDEN, cue="m3", pause=0.4),
        B("A sound.", speaker=AIDEN, cue="m4", pause=0.4),
        B("And two sprites, or a backdrop that changes.", speaker=AIDEN, cue="m5", pause=0.6),
        B("Count them on your fingers with me. One, two, three, four, five!", speaker=AIDEN, cue="count",
          pause=1.2),
        B("Five things, high five!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("cards", items=["Green flag", "Repeat", "Click or key", "Sound", "Two sprites or a backdrop change"],
          x=180, y=200, w=900, gap=125, reveal=["m1", "m2", "m3", "m4", "m5"],
          active=[("count@0.3", "count@0.45"), ("count@0.45", "count@0.6"), ("count@0.6", "count@0.75"),
                  ("count@0.75", "count@0.9"), ("count@0.9", "pixi")], color="purple"),
        A("chip", "My card must have:", at="five", until="count", x=1480, y=300, color="purple", size=44),
        A("bigtext", "5 things!", at="count", x=1480, y=400, size=90, color="purple"),
        A("pixi", x=1480, y=860, s=0.65, at="count", ground=980, beep="pixi", moods={"pixi": "proud"}),
    )),
    # 4. Mei's storyboard ----------------------------------------------------------------------------
    Scene("j1-w09-s04", setting="sky", beats=(
        B("Here is a sample storyboard. Mei made a card for Grandpa.", speaker=AIDEN, cue="mei", pause=0.5),
        B("Box one: the cat says Happy birthday, and meows.", speaker=AIDEN, cue="b1", pause=0.6),
        B("Box two: the cat dances.", speaker=AIDEN, cue="b2", pause=0.6),
        B("Box three: click the balloon. Pop! Surprise!", speaker=AIDEN, cue="b3", pause=0.8),
        B("Three boxes, one idea each. That is plenty!", speaker=AIDEN, cue="plenty", pause=0.8),
    ), actions=(
        A("banner", "Mei's card for Grandpa", at="mei", color="blue"),
        *BOARD,
        A("cat", x=380, y=820, s=0.8, at="b1", talk=("b1", "b1$")),
        A("cat", x=960, y=820, s=0.8, at="b2",
          path=[("b2", 960, 820), ("b2+0.4", 1000, 820), ("b2+0.8", 920, 820), ("b2+1.2", 1000, 820),
                ("b2+1.6", 960, 820)]),
        A("icons", at="b3", x=1540, y=700, items=[("star", "Surprise!", "b3@0.5")]),
        A("chip", "one idea in each box", at="plenty", x=960, y=960, color="orange", size=46),
    )),
    # 5. one box at a time ---------------------------------------------------------------------------
    Scene("j1-w09-s05", setting="workshop", beats=(
        B("We do not build the whole card at once.", speaker=AIDEN, cue="not", pause=0.4),
        B("We build one box at a time, and we test each box before we start the next.", speaker=AIDEN,
          cue="one", pause=0.6),
        B("Then, if something goes wrong, we know where to look.", speaker=AIDEN, cue="look", pause=0.6),
        B("It is like the picture on a LEGO box. Build one part, check that it looks right, then build the "
          "next part.", speaker=AIDEN, cue="lego", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "lego": "proud"}, point=("one", "one$")),
        A("pixi", x=600, y=760),
        A("cards", items=["Build one box", "Test it", "Check it off", "Next box!"], x=980, y=400, w=640, gap=120,
          reveal=["one@0.1", "one@0.5", "one@0.75", "look"], at="one", color="green"),
        A("chip", "one box at a time", at="lego", x=1300, y=950, color="yellow", size=46),
    )),
    # 6. build box 1 ---------------------------------------------------------------------------------
    Scene("j1-w09-s06", setting="mint", beats=(
        B("Let's build Mei's box one together.", speaker=AIDEN, cue="build", pause=0.4),
        B("Click the cat in the sprite list. From the yellow Events circle: when green flag clicked.",
          speaker=AIDEN, cue="events", pause=0.6),
        B("From the purple Looks circle: say Hello for two seconds. Type: Happy birthday!", speaker=AIDEN,
          cue="looks", pause=0.8),
        B("From the pink Sound circle: play sound Meow until done.", speaker=AIDEN, cue="sound", pause=0.6),
        B("Now we test. Click the green flag!", speaker=AIDEN, cue="flag", pause=3.0),
        B("Box one works! Let's check it off on the storyboard.", speaker=AIDEN, cue="works", pause=0.5),
        B("Check!", speaker=PIXI, cue="check", pause=0.8),
    ), actions=(
        A("banner", "Box 1: Start", at="build", color="green"),
        A("scratch", "Cat's code", blocks=[FLAG, ("looks", "say [Hello!] for [2] seconds"), MEOW], x=150, y=280,
          w=880, h=480, scale=BIG, reveal=["events", "looks", "sound"],
          edits=[("looks@0.75", 1, "say [Happy birthday!] for [2] seconds")]),
        A("chip", "Events: yellow", at="events", until="events>", x=1450, y=870, color="yellow", size=44),
        A("chip", "Looks: purple", at="looks", until="looks>", x=1450, y=870, color="purple", size=44),
        A("chip", "Sound: pink", at="sound", until="sound>", x=1450, y=870, color="pink", size=44),
        A("stage", x=1100, y=260, w=700, h=480, at="build", flag_at="flag@0.6", sprite_scale=CAT,
          actions=[("flag+0.4", "say", "Happy birthday!", 2.0)]),
        A("sfx", "pop", at="flag+2.4"),
        A("chip", "Box 1: check!", at="works", x=1450, y=870, color="green", size=48),
        A("badge", ok=True, at="works", x=1740, y=320),
        A("confetti", at="works", x=1450, y=500),
    )),
    # 7. box 2: the dance ----------------------------------------------------------------------------
    Scene("j1-w09-s07", setting="peach", beats=(
        B("Next is box two: the cat dances.", speaker=AIDEN, cue="next", pause=0.4),
        B("Which block makes something happen again and again?", speaker=AIDEN, cue="which", pause=3.0),
        B("Repeat! Mei put next costume and wait one seconds inside a repeat four.", speaker=AIDEN,
          cue="repeat", pause=0.6),
        B("The wait makes the dance slow enough to see.", speaker=AIDEN, cue="wait", pause=0.6),
        B("Test it, then check off box two.", speaker=AIDEN, cue="test", pause=3.0),
        B("Dance, dance, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "Box 2: Middle", at="next", color="orange"),
        A("scratch", "Cat's code", blocks=[FLAG, SAY, MEOW, DANCE], x=150, y=250, w=900, h=760, scale=1.0,
          reveal=["start", "start", "start", "repeat", "repeat@0.5", "repeat@0.7"],
          highlight=[(3, "repeat", "wait$"), (5, "wait", "wait$")]),
        A("thought", "Again and again?", at="which$+0.2", until="repeat", x=1450, y=860),
        A("stage", x=1120, y=250, w=680, h=460, at="next", flag_at="test@0.5", sprite_scale=CAT,
          actions=[("test+0.6", "move", 30, 0.3), ("test+1.0", "move", -30, 0.3), ("test+1.4", "move", 30, 0.3),
                   ("test+1.8", "move", -30, 0.3)]),
        A("chip", "wait = slow enough to see", at="wait", until="test", x=1450, y=860, color="orange", size=40),
        A("chip", "Box 2: check!", at="test+2.4", x=1450, y=860, color="green", size=48),
        A("pixi", x=1700, y=900, s=0.45, at="pixi", ground=980),
    )),
    # 8. box 3: the surprise -------------------------------------------------------------------------
    Scene("j1-w09-s08", setting="mint", beats=(
        B("Box three is the surprise. Mei adds the balloon with Choose a Sprite.", speaker=AIDEN, cue="add",
          pause=0.5),
        B("She clicks the balloon in the sprite list. Its code is its own.", speaker=AIDEN, cue="own", pause=0.5),
        B("From Events: when this sprite clicked. Then play sound Pop, and say Surprise!", speaker=AIDEN,
          cue="build", pause=0.8),
        B("To test it, we click the balloon.", speaker=AIDEN, cue="test", pause=3.0),
        B("Surprise! Box three works. Check!", speaker=AIDEN, cue="works", pause=0.8),
    ), actions=(
        A("banner", "Box 3: End", at="add", color="purple"),
        A("scratch", "Balloon's code", blocks=[CLICKED, POP, SURPRISE], x=150, y=300, w=900, h=440, scale=BIG,
          at="build", reveal=["build", "build@0.45", "build@0.75"]),
        A("chip", "Choose a Sprite: Balloon", at="add", until="build", x=600, y=420, color="orange", size=44),
        A("chip", "its own code", at="own", until="build", x=600, y=540, color="sky", size=44),
        A("stage", x=1120, y=260, w=700, h=480, at="add", flag=False, sprite="balloon", sprite_scale=1.2,
          sprite_x=90, sprite_y=10, extra=[("cat", -110, -20)], actions=[("test+0.9", "say", "Surprise!", 2.4)]),
        A("pointer", x=1700, y=700, at="test", until="works$",
          path=[("test", 1700, 700), ("test+0.8", 1590, 470)]),
        A("sfx", "pop", at="test+0.8"),
        A("chip", "Box 3: check!", at="works", x=1450, y=870, color="green", size=48),
        A("badge", ok=True, at="works", x=1740, y=320),
        A("confetti", at="works", x=1450, y=500),
    )),
    # 9. bug hunt: Partner Check ---------------------------------------------------------------------
    Scene("j1-w09-s09", setting="mint", beats=(
        B("Time for a bug hunt! It is called Partner Check.", speaker=AIDEN, cue="bug", pause=0.5),
        B("Swap seats. Your partner holds your storyboard, clicks the flag and tries the click.", speaker=AIDEN,
          cue="swap", pause=0.5),
        B("For each box, they say: matches, or not yet.", speaker=AIDEN, cue="say", pause=0.6),
        B("Sam checks Leo's card. Box three says: click the balloon. Sam clicks it, and nothing happens. Not yet!",
          speaker=AIDEN, cue="sam", pause=0.6),
        B("Look at the balloon's script. What is missing on top?", speaker=AIDEN, cue="what", pause=3.2),
        B("A hat block! Without when this sprite clicked, the script never starts.", speaker=AIDEN, cue="hat",
          pause=0.5),
        B("Leo snaps it on top. Sam clicks the balloon again.", speaker=AIDEN, cue="fix", pause=3.2),
        B("Surprise! It matches the storyboard now!", speaker=AIDEN, cue="matches", pause=0.4),
        B("Good teamwork!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Partner Check", at="bug", color="navy"),
        A("cards", items=["Box 1: matches", "Box 2: matches", "Box 3: not yet"], x=220, y=280, w=620, gap=120,
          reveal=["say@0.2", "say@0.6", "sam@0.8"], at="say", until="what", color="sky"),
        A("scratch", "Leo's balloon", blocks=[POP, SURPRISE], x=150, y=320, w=900, h=360, scale=BIG, at="what",
          until="fix+0.4"),
        A("scratch", "Leo's balloon (fixed)", blocks=[CLICKED, POP, SURPRISE], x=150, y=320, w=900, h=440,
          scale=BIG, at="fix+0.4", highlight=[(0, "fix+0.4", "fix+1.8")]),
        A("sfx", "snap", at="fix+0.4"),
        A("stage", x=1120, y=260, w=700, h=480, at="sam", flag=False, sprite="balloon", sprite_scale=1.2,
          sprite_x=90, sprite_y=10, extra=[("cat", -110, -20)], actions=[("fix+2.0", "say", "Surprise!", 2.4)]),
        A("pointer", x=1700, y=700, at="sam@0.5", until="sam$+0.4",
          path=[("sam@0.5", 1700, 700), ("sam@0.5+0.8", 1590, 470)]),
        A("pointer", x=1700, y=700, at="fix@0.6", until="matches$",
          path=[("fix@0.6", 1700, 700), ("fix+1.9", 1590, 470)]),
        A("badge", ok=False, at="sam@0.85", until="fix", x=1740, y=320),
        A("thought", "What is on top?", at="what$+0.2", until="hat", x=1450, y=880),
        A("chip", "no hat block = never starts", at="hat", until="matches", x=1450, y=880, color="red", size=40),
        A("badge", ok=True, at="matches", x=1740, y=320),
        A("chip", "matches!", at="matches", x=1450, y=880, color="green", size=48),
        A("confetti", at="matches", x=1450, y=500),
    )),
    # 10. ask before you show ------------------------------------------------------------------------
    Scene("j1-w09-s10", setting="workshop", beats=(
        B("Your card is yours. Leo's card is Leo's.", speaker=AIDEN, cue="yours", pause=0.5),
        B("If you want to show someone else's card, or take a photo of it, ask first: May I show your card?",
          speaker=AIDEN, cue="ask", pause=0.6),
        B("And we never change someone else's project without asking.", speaker=AIDEN, cue="change", pause=0.6),
        B("Priya loves Kai's card. She wants to show her big sister. What should she do?", speaker=AIDEN,
          cue="priya", pause=3.0),
        B("Ask Kai first!", speaker=AIDEN, cue="kai", pause=0.5),
        B("And on your card, write Grandpa or a nickname, never a full name.", speaker=AIDEN, cue="nick",
          pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"priya": "thinking", "kai": "proud"}, chin=("priya", "kai")),
        A("pixi", x=600, y=760, moods={"kai": "happy"}),
        A("banner", "Ask before you show", at="yours", color="green"),
        A("icons", at="ask", until="end", x=1280, y=560, gap=300,
          items=[("camera", "Ask before a photo", "ask@0.5"), ("person", "Ask before you show", "ask"),
                 ("gear", "Never change it", "change")]),
        A("thought", "What should she do?", at="priya$+0.2", until="kai", x=1280, y=860),
        A("chip", "Ask Kai first!", at="kai", until="nick", x=1280, y=860, color="green", size=48),
        A("chip", "Grandpa or a nickname", at="nick", x=1280, y=860, color="yellow", size=46),
    )),
    # 11. wiggle break: act out your storyboard ------------------------------------------------------
    Scene("j1-w09-s11", setting="workshop", beats=(
        B("Wiggle break! Stand up and act out your storyboard.", speaker=AIDEN, cue="stand", pause=0.5),
        B("Box one: strike a pose for the start!", speaker=AIDEN, cue="pose", pause=1.4),
        B("Box two: a little dance, four times. One, two, three, four!", speaker=AIDEN, cue="dance", pause=1.0),
        B("Box three: a big surprise jump!", speaker=AIDEN, cue="jump", pause=1.6),
        B("Surprise! Beep boop!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("pose", "pose$"), ("dance", "dance$+0.6"), ("jump", "end")],
          moods={"start": "happy", "jump": "surprised", "pixi": "proud"},
          path=[("jump", 300, 960), ("jump@0.6", 300, 900), ("jump$", 300, 960)]),
        A("pixi", x=600, y=760, beep="pixi", moods={"jump": "surprised", "pixi": "happy"}),
        A("cards", items=["Pose", "Dance x 4", "Surprise jump!"], x=1000, y=420, w=640, gap=130,
          reveal=["pose", "dance", "jump"], active=[("pose", "dance"), ("dance", "jump"), ("jump", "end")],
          done=["dance", "jump", "pixi"], color="orange"),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j1-w09-s12", setting="workshop", tail=0.8, beats=(
        B("Say it with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Storyboard!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Start, middle, end!", speaker=AIDEN, cue="w2", pause=1.4),
        B("One box at a time!", speaker=AIDEN, cue="w3", pause=1.4),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Draw your storyboard. Build your card, one box at a time, and test each box. Then do a partner "
          "check.", speaker=AIDEN, cue="next", pause=0.6),
        B("Save often: File, then Save to your computer.", speaker=AIDEN, cue="save", pause=0.5),
        B("Next week is the showcase! Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Storyboard!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Start, middle, end!", at="w2", until="w2>", y=560, size=84, color="green"),
        A("bigtext", "One box at a time!", at="w3", until="w3>", y=560, size=84, color="purple"),
        A("banner", "NEXT: Build my greeting card", at="turn", color="green"),
        A("cards", items=["Draw my storyboard", "Build box by box, test each", "Partner check"], x=1000, y=300,
          w=680, gap=120, reveal=["next@0.1", "next@0.4", "next@0.8"], at="next"),
        A("chip", "Save often!", at="save", x=1340, y=760, color="sky", size=46),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
