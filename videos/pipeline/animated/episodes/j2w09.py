"""Junior Level 2 Week 9: Project Studio, My First Arcade Game (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/2-game-makers/teaching-material/lessons/week09.tex: planning before building on the game
plan card (Mei's sample card, never a child's answer), the paper prototype played by a partner, the five
must-haves built one at a time like a house (floor and walls first), the worked example "Mei's Banana
Drop: the first must-have" (the hidden Star marker; Bananas: set rotation style left-right, go to Star,
point in direction 180, forever move 5 steps; then if touching Bowl: start sound Pop, go to Star), the
rest of the card in words (score and misses, the random wait, the week 8 referee), the act-out-your-game
wiggle, the playtest bug hunt (Exercise 9.3: hands in your lap, a bug list, fix one bug: the Star too near
an edge), and asking before you share someone else's game.
Level 2 conventions: point in direction 180, then move; the hidden Star marker; misses count up.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

BIG = 1.25  # block scale: big enough for young eyes
SPRITE = 1.0  # sprite size on the stage

FLAG = ("event", "when {flag} clicked")
GO_STAR = ("motion", "go to [Star]")
POP = ("sound", "start sound [Pop]")
CATCH = ("control", "if <touching [Bowl] ?> then", [POP, GO_STAR])
BANANAS = [FLAG, ("motion", "set rotation style [left-right]"), GO_STAR, ("motion", "point in direction [180]"),
           ("control", "forever", [("motion", "move [5] steps")])]
STAR_SCRIPT = [FLAG, ("looks", "hide")]
RANDOM_WAIT = ("control", "wait <pick random 1 to 3> seconds")

TOP = 130  # the hidden Star marker (stage coordinates)
BOWL = ("bowl", 0, -130)
MUST_HAVES = ["A forever loop", "An if touching", "A score or misses", "Random: a surprise",
              "A win or game over"]

EPISODE = Episode(level="j2", week=9, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j2-w09-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, game makers! I'm Aiden, and this is Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Today is a big day!", speaker=PIXI, cue="hello", pause=0.5),
        B("Today, you start your very own arcade game!", speaker=AIDEN, cue="today", pause=0.5),
        B("It can be a catch game, or a maze game. You choose!", speaker=AIDEN, cue="choose", pause=0.5),
        B("Game makers plan before they build. So let's plan first!", speaker=AIDEN, cue="plan", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("plan", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("banner", "MISSION: My First Arcade Game", at="today"),
        A("chip", "catch game", at="choose@0.2", x=1180, y=420, color="yellow", size=48),
        A("chip", "maze game", at="choose@0.6", x=1560, y=420, color="sky", size=48),
        A("chip", "Plan first, then build!", at="plan@0.4", x=1370, y=600, color="green", size=46),
    )),
    # 2. the game plan card -------------------------------------------------------------------------
    Scene("j2-w09-s02", setting="lavender", beats=(
        B("This is a game plan card.", speaker=AIDEN, cue="card", pause=0.5),
        B("It asks: Is it a catch game or a maze game? Who is the player? What do you catch or avoid?",
          speaker=AIDEN, cue="asks", pause=0.5),
        B("How do you win? How do you lose? And what is one surprise?", speaker=AIDEN, cue="asks2", pause=0.6),
        B("Here is Mei's card. Mei planned a catch game called Banana Drop.", speaker=AIDEN, cue="mei", pause=0.5),
        B("I am the Bowl. Bananas fall, and I catch them. I win when I catch ten. I lose when I miss three.",
          speaker=AIDEN, cue="read", pause=0.4),
        B("Surprise: the bananas wait a random time at the top.", speaker=AIDEN, cue="surprise", pause=0.6),
        B("Your card will be different!", speaker=AIDEN, cue="yours", pause=0.8),
    ), actions=(
        A("panel", "Game plan card", x=110, y=200, w=800, size=36,
          items=[("asks@0.1", "Catch game or maze game?"), ("asks@0.4", "Who is the player?"),
                 ("asks@0.7", "What do you catch or avoid?"), ("asks2@0.1", "How do you win?"),
                 ("asks2@0.4", "How do you lose?"), ("asks2@0.7", "One surprise?")]),
        A("panel", "Mei's card: Banana Drop", x=1000, y=200, w=800, size=36, at="mei", color="yellow",
          items=[("mei@0.6", "Catch game"), ("read@0.1", "Player: the Bowl"), ("read@0.3", "Catch: bananas"),
                 ("read@0.6", "Win: catch 10"), ("read@0.85", "Lose: miss 3"),
                 ("surprise@0.3", "Surprise: a random wait")]),
        A("chip", "Your card: your own game!", at="yours", x=960, y=900, color="green", size=46),
    )),
    # 3. the paper prototype --------------------------------------------------------------------------
    Scene("j2-w09-s03", setting="workshop", beats=(
        B("Next, make a paper prototype. A prototype is a quick test version, made before the real one.",
          speaker=AIDEN, cue="proto", pause=0.5),
        B("Draw the stage on paper. Draw and tear out the player and the thing that falls.", speaker=AIDEN,
          cue="draw", pause=0.5),
        B("A partner slides the player. You slide the falling thing down, and say what happens.",
          speaker=AIDEN, cue="slide", pause=0.6),
        B("You caught it! One point!", speaker=PIXI, cue="caught", pause=1.2),
        B("You missed. One miss!", speaker=PIXI, cue="missed", pause=0.6),
        B("Then ask your partner: Could you win? Could you lose? Was anything confusing?", speaker=AIDEN,
          cue="ask", pause=0.5),
        B("If you need to, change one thing on your card.", speaker=AIDEN, cue="change", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=980, s=0.8, moods={"start": "happy", "ask": "thinking", "change": "happy"},
          point=("slide", "slide$")),
        A("pixi", x=520, y=780, s=0.7, ground=960),
        A("chip", "prototype = a quick test version", at="proto@0.3", until="slide", x=1300, y=850,
          color="yellow", size=42),
        A("stage", x=900, y=200, w=800, h=520, at="draw", flag=False, sky="#FFFFFF", sprite="banana",
          sprite_scale=SPRITE, sprite_x=-40, sprite_y=TOP, extra=[("bowl", -140, -130)],
          actions=[("slide+1.5", "goto", -40, -100, 1.6), ("caught$+0.3", "goto", 120, TOP, 0.05),
                   ("caught$+0.4", "goto", 120, -150, 1.2)]),
        A("chip", "1 point!", at="caught", until="missed", x=1300, y=850, color="green", size=46),
        A("chip", "1 miss!", at="missed", until="ask", x=1300, y=850, color="orange", size=46),
        A("panel", "Ask your partner", at="ask", x=900, y=760, w=800, size=34,
          items=[("ask@0.3", "Could you win? Could you lose?"), ("ask@0.7", "Was anything confusing?")]),
    )),
    # 4. must-haves, one at a time ---------------------------------------------------------------------
    Scene("j2-w09-s04", setting="workshop", beats=(
        B("Every arcade game needs five must-haves.", speaker=AIDEN, cue="five", pause=0.4),
        B("A forever loop keeps it going. An if touching makes something happen. A score or misses variable "
          "counts. Random gives a surprise. And you can win, or it is game over.", speaker=AIDEN, cue="list",
          pause=0.6),
        B("We build one must-have at a time. Then we test it, and check it off.", speaker=AIDEN, cue="one",
          pause=0.5),
        B("It is like building a house. Builders make the floor and the walls first, and check they are "
          "strong. The paint comes last.", speaker=AIDEN, cue="house", pause=0.5),
        B("Must-haves first. Extras later!", speaker=AIDEN, cue="first", pause=0.4),
        B("Floor! Walls! Paint!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "first": "proud"}, point=("one", "one$")),
        A("pixi", x=600, y=760, beep="pixi"),
        A("cards", items=MUST_HAVES, x=1000, y=210, w=680, gap=112, at="five", color="green",
          reveal=["list@0.05", "list@0.25", "list@0.45", "list@0.65", "list@0.85"],
          active=[("one", "one@0.5"), None, None, None, None], done=["one@0.7", None, None, None, None],
          until="house"),
        A("icons", at="house", until="end", x=1340, y=420, gap=280,
          items=[("house", "Floor and walls first", "house@0.2"), ("star", "Paint last", "house@0.8")]),
        A("chip", "Must-haves first. Extras later!", at="first", x=1340, y=760, color="green", size=44),
    )),
    # 5. Mei's Banana Drop: the Star and the forever ----------------------------------------------------
    Scene("j2-w09-s05", setting="mint", beats=(
        B("Let's build the first must-have of Mei's game together. The Bowl already moves with the arrow keys.",
          speaker=AIDEN, cue="build", pause=0.5),
        B("First, the Star marker. Choose the Star sprite, drag it near the top, and give it: when green flag "
          "clicked, hide.", speaker=AIDEN, cue="star", pause=0.6),
        B("Now choose the Bananas sprite. From yellow Events: when green flag clicked.", speaker=AIDEN,
          cue="bananas", pause=0.5),
        B("From blue Motion: set rotation style left-right, go to Star, and point in direction one hundred "
          "eighty. That points down.", speaker=AIDEN, cue="motion", pause=0.6),
        B("Then an orange forever, with move five steps inside.", speaker=AIDEN, cue="forever", pause=0.5),
        B("Click the flag. Test!", speaker=AIDEN, cue="test", pause=2.6),
        B("The bananas fall. Forever: check!", speaker=AIDEN, cue="check", pause=0.8),
    ), actions=(
        A("banner", "Mei's Banana Drop: the first must-have", at="build", color="green"),
        A("scratch", "Star", blocks=STAR_SCRIPT, x=130, y=260, w=860, h=290, scale=BIG, at="star@0.6",
          until="bananas"),
        A("chip", "Looks: purple", at="star@0.7", until="bananas", x=560, y=700, color="purple", size=44),
        A("scratch", "Bananas", blocks=BANANAS, x=130, y=260, w=860, h=720, scale=BIG, at="bananas",
          reveal=["bananas@0.6", "motion@0.25", "motion@0.4", "motion@0.6", "forever@0.3", "forever@0.7"],
          highlight=[(3, "motion@0.8", "forever")]),
        A("stage", x=1100, y=230, w=700, h=480, at="build", until="test", flag=False, sprite="bowl",
          sprite_y=-120, sprite_scale=SPRITE, extra=[("star", 0, TOP + 20)],
          actions=[("build@0.6", "goto", 80, -120, 0.8), ("build@0.8", "goto", -60, -120, 0.8)]),
        A("stage", x=1100, y=230, w=700, h=480, at="test", flag_at="test@0.4", sprite="banana",
          sprite_scale=SPRITE, sprite_y=TOP, extra=[("bowl", -120, -130)],
          actions=[("test@0.5", "goto", 0, -150, 2.0), ("check+0.8", "goto", 0, TOP, 0.05)]),
        A("chip", "direction 180 = down", at="motion@0.8", until="test", x=1450, y=860, color="sky", size=44),
        A("chip", "Forever: check!", at="check", x=1450, y=860, color="green", size=46),
        A("badge", ok=True, at="check", x=1760, y=290),
    )),
    # 6. quick quiz, then the if touching -----------------------------------------------------------------
    Scene("j2-w09-s06", setting="peach", beats=(
        B("Quick quiz! Before Mei builds the next must-have, what should she do?", speaker=AIDEN, cue="quiz",
          pause=3.0),
        B("Test it, and check it off! If something goes wrong, we know where to look.", speaker=AIDEN,
          cue="answer", pause=0.6),
        B("Next must-have: if touching. Inside the forever, put an if then from orange Control, with touching "
          "Bowl from light blue Sensing.", speaker=AIDEN, cue="iftouch", pause=0.6),
        B("Inside the if: start sound Pop, and go to Star.", speaker=AIDEN, cue="inside", pause=0.6),
        B("Test with the arrow keys. Catch a banana!", speaker=AIDEN, cue="test", pause=3.0),
        B("Pop! The banana goes back to the top. If touching: check!", speaker=AIDEN, cue="check", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", until="iftouch", color="purple"),
        A("thought", "What should Mei do?", at="quiz$+0.2", until="answer", x=960, y=500),
        A("cards", items=["Build one must-have", "Test it", "Check it off"], x=620, y=330, w=680, gap=130,
          at="answer", until="iftouch", reveal=["answer", "answer@0.15", "answer@0.3"], color="green"),
        A("scratch", "Bananas: inside the forever",
          blocks=[("control", "forever", [("motion", "move [5] steps"), CATCH])],
          x=130, y=260, w=860, h=700, scale=BIG, at="iftouch",
          reveal=["iftouch", "iftouch", "iftouch@0.5", "inside@0.3", "inside@0.7"],
          highlight=[(2, "test", "check$")]),
        A("chip", "Control: orange", at="iftouch@0.4", until="inside", x=1450, y=860, color="orange", size=44),
        A("chip", "Sensing: light blue", at="iftouch@0.75", until="inside", x=1450, y=960, color="sky", size=42),
        A("stage", x=1100, y=230, w=700, h=480, at="iftouch", flag_at="test@0.2", sprite="banana",
          sprite_scale=SPRITE, sprite_y=TOP, extra=[BOWL],
          actions=[("test@0.4", "goto", 0, -95, 2.0), ("test+2.4", "goto", 0, TOP, 0.05)]),
        A("sfx", "pop", at="test+2.35"),
        A("chip", "If touching: check!", at="check", x=1450, y=860, color="green", size=46),
        A("badge", ok=True, at="check", x=1760, y=290),
    )),
    # 7. the rest of the card ---------------------------------------------------------------------------
    Scene("j2-w09-s07", setting="sky", beats=(
        B("Look at the rest of Mei's card. Next come the score and misses, the surprise and the ending.",
          speaker=AIDEN, cue="rest", pause=0.5),
        B("You built them all in your catch game!", speaker=AIDEN, cue="built",
          pause=0.5),
        B("Mei's surprise is a wait with pick random one to three, right after each go to Star.", speaker=AIDEN,
          cue="random", pause=0.5),
        B("Nobody knows when the next banana will drop!", speaker=AIDEN, cue="nobody", pause=0.5),
        B("And the Bowl gets the referee script from last week.", speaker=AIDEN, cue="referee", pause=0.8),
    ), actions=(
        A("cards", items=MUST_HAVES, x=120, y=230, w=680, gap=112, at="rest", color="green",
          done=["rest", "rest", None, None, None],
          active=[None, None, ("rest@0.5", "random"), ("random", "referee"), ("referee", "end")]),
        A("chip", "Look in your catch game!", at="built", until="random", x=1350, y=420, color="yellow", size=44),
        A("scratch", blocks=[RANDOM_WAIT], x=1000, y=330, w=760, h=150, panel=False, scale=BIG, at="random",
          until="referee"),
        A("chip", "Operators: green", at="random@0.4", until="referee", x=1350, y=540, color="green", size=44),
        A("stage", x=1050, y=600, w=600, h=340, at="nobody", until="referee", flag=False, sprite="banana",
          sprite_scale=0.8, sprite_x=60, sprite_y=TOP,
          actions=[("nobody+0.6", "goto", 60, -100, 1.0), ("nobody+1.7", "goto", -80, TOP, 0.05)]),
        A("chip", "referee script from week 8", at="referee", x=1350, y=420, color="orange", size=44),
        A("chip", "if misses = 3 • if score = 10", at="referee@0.4", x=1350, y=540, color="white", size=40),
    )),
    # 8. wiggle break: act out your game ----------------------------------------------------------------
    Scene("j2-w09-s08", setting="workshop", beats=(
        B("Wiggle break! Stand up and act out your game.", speaker=AIDEN, cue="wiggle", pause=0.5),
        B("Slide left and right, like the player.", speaker=AIDEN, cue="slide", pause=2.0),
        B("Now you are a banana. Fall from the ceiling!", speaker=AIDEN, cue="fall", pause=2.0),
        B("Catch! Jump up high!", speaker=AIDEN, cue="jump", pause=1.6),
        B("Game over! Fall to the floor, in slow motion.", speaker=AIDEN, cue="over", pause=2.4),
        B("Now stand up, and stretch.", speaker=AIDEN, cue="stretch", pause=1.4),
        B("Beep! Stretch!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("jump", "jump$"), ("stretch", "end")],
          moods={"start": "happy", "over": "surprised", "stretch": "proud"},
          path=[("slide", 300, 960), ("slide+0.6", 420, 960), ("slide+1.4", 220, 960), ("slide+2.2", 300, 960)]),
        A("pixi", x=640, y=760, beep="pixi",
          path=[("fall", 640, 560), ("fall+1.4", 640, 800), ("jump", 640, 620), ("jump+0.6", 640, 760)]),
        A("bigtext", "Slide!", at="slide", until="fall", x=1300, y=400, size=80, color="blue"),
        A("bigtext", "Fall!", at="fall", until="jump", x=1300, y=400, size=80, color="orange"),
        A("bigtext", "Jump!", at="jump", until="over", x=1300, y=400, size=80, color="green"),
        A("bigtext", "Game over...", at="over", until="stretch", x=1300, y=400, size=80, color="red"),
        A("bigtext", "Stretch!", at="stretch", x=1300, y=400, size=80, color="purple"),
    )),
    # 9. bug hunt: the playtest ---------------------------------------------------------------------------
    Scene("j2-w09-s09", setting="lavender", beats=(
        B("Now the playtest. It is our bug hunt!", speaker=AIDEN, cue="bug", pause=0.4),
        B("Swap seats. The Player plays your game twice: once to win, and once to lose.", speaker=AIDEN,
          cue="twice", pause=0.5),
        B("You watch. Keep your hands in your lap, and say nothing. That is the hardest job!", speaker=AIDEN,
          cue="watch", pause=0.6),
        B("Write or draw each problem on your bug list.", speaker=AIDEN, cue="list", pause=0.4),
        B("The bananas went through the bowl. I did not know how to win. It said Game over at the start.",
          speaker=AIDEN, cue="bugs", pause=0.6),
        B("Then the Player gives two stars and a wish.", speaker=AIDEN, cue="stars", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Playtest", at="bug", color="navy"),
        A("icons", at="twice", until="list", x=960, y=420, gap=300,
          items=[("game", "Play to win", "twice@0.5"), ("game", "Play to lose", "twice@0.8"),
                 ("heart", "Hands in your lap", "watch@0.2")]),
        A("chip", "Say nothing!", at="watch@0.5", until="list", x=960, y=760, color="yellow", size=46),
        A("panel", "My bug list", at="list", x=320, y=250, w=1280, size=38,
          items=[("bugs", "The bananas went through the bowl."), ("bugs@0.35", "I did not know how to win."),
                 ("bugs@0.7", "It said Game over at the start.")]),
        A("icons", at="stars", x=960, y=780, gap=200,
          items=[("star", "a star", "stars@0.2"), ("star", "a star", "stars@0.35"), ("heart", "a wish", "stars@0.6")]),
    )),
    # 10. fix one bug ----------------------------------------------------------------------------------
    Scene("j2-w09-s10", setting="mint", beats=(
        B("Now pick one bug, and fix it: test, look, change one thing.", speaker=AIDEN, cue="pick", pause=0.5),
        B("Mei's Player found this one. Click the flag, and the misses count up right away. Game over!",
          speaker=AIDEN, cue="symptom", pause=1.0),
        B("Why? Look at the Star marker.", speaker=AIDEN, cue="why", pause=3.0),
        B("The Star is touching the edge! So the banana touches the edge right at the start.",
          speaker=AIDEN, cue="edge", pause=0.6),
        B("Mei drags the Star a little lower, away from the edge. Test again!", speaker=AIDEN, cue="fix",
          pause=3.0),
        B("Misses start at zero. Fixed!", speaker=AIDEN, cue="fixed", pause=0.4),
        B("Bug squashed!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Playtest", at="start", color="navy"),
        A("cards", items=["Test", "Look", "Change one thing"], x=130, y=260, w=560, gap=130, at="pick",
          reveal=["pick@0.5", "pick@0.65", "pick@0.8"], color="sky",
          active=[("symptom", "why"), ("why", "fix"), ("fix", "fixed")], done=["why", "fix", "fixed"]),
        A("stage", x=900, y=230, w=860, h=560, at="symptom", until="fix@0.5", flag_at="symptom@0.4",
          sprite="banana", sprite_scale=SPRITE, sprite_y=125, extra=[BOWL, ("star", 0, 125)],
          monitors=[("misses", [("symptom", 0), ("symptom@0.5", 1), ("symptom@0.6", 2), ("symptom@0.7", 3)])]),
        A("bubble", "Game over!", x=1500, y=660, at="symptom@0.75", until="why", size=40),
        A("thought", "Why?", at="why$+0.2", until="edge", x=410, y=760),
        A("chip", "Star touching the edge", at="edge", until="fix", x=410, y=760, color="red", size=40),
        A("pointer", x=1330, y=290, at="fix", until="fix@0.6", path=[("fix", 1330, 290), ("fix@0.5", 1330, 390)]),
        A("stage", x=900, y=230, w=860, h=560, at="fix@0.5", flag_at="fix$+0.3", sprite="banana",
          sprite_scale=SPRITE, sprite_y=80, extra=[BOWL, ("star", 0, 80)],
          monitors=[("misses", [("fix@0.5", 0)])],
          actions=[("fix$+0.4", "goto", 0, -95, 2.0)]),
        A("chip", "Star lower: away from the edge", at="fix@0.5", until="fixed", x=410, y=760, color="green",
          size=36),
        A("badge", ok=True, at="fixed", x=1680, y=290),
        A("confetti", at="fixed", x=1330, y=470),
    )),
    # 11. ask before you share -------------------------------------------------------------------------
    Scene("j2-w09-s11", setting="workshop", beats=(
        B("Your game is yours. Zoe's game is Zoe's.", speaker=AIDEN, cue="yours", pause=0.4),
        B("To show someone else's game, take a photo, or copy it, ask first: May I show your game?",
          speaker=AIDEN, cue="ask", pause=0.5),
        B("And never change someone else's game without asking. Make a copy with a new name.", speaker=AIDEN,
          cue="copy", pause=0.5),
        B("Our games stay with our family. We do not put them on the internet.", speaker=AIDEN, cue="family",
          pause=0.6),
        B("Leo loves Priya's maze. He wants to show it to his cousin. What should he do?", speaker=AIDEN,
          cue="leo", pause=3.0),
        B("Ask Priya first! If she says no, he does not show it.", speaker=AIDEN, cue="answer", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "leo": "thinking", "answer": "proud"},
          chin=("leo", "answer")),
        A("pixi", x=600, y=760),
        A("bubble", "May I show your game?", x=1300, y=330, at="ask@0.7", until="leo", size=40),
        A("icons", at="ask", until="end", x=1260, y=700, gap=250,
          items=[("person", "Ask first", "ask@0.5"), ("file", "Copy, new name", "copy@0.5"),
                 ("house", "Stays with family", "family@0.2"), ("wifi_off", "Not online", "family@0.6")]),
        A("thought", "What should Leo do?", at="leo$+0.2", until="answer", x=1260, y=330),
        A("chip", "Ask Priya first!", at="answer", x=1260, y=330, color="green", size=48),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j2-w09-s12", setting="workshop", tail=0.8, beats=(
        B("Say it with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Plan!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Build!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Playtest!", speaker=AIDEN, cue="w3", pause=1.2),
        B("Plan, then build one must-have at a time. Then a Player helps you find bugs.", speaker=AIDEN,
          cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Fill in your game plan card, build your must-haves, then playtest and fix one bug.", speaker=AIDEN,
          cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Plan!", at="w1", until="w1>", y=560, size=90, color="purple"),
        A("bigtext", "Build!", at="w2", until="w2>", y=560, size=90, color="orange"),
        A("bigtext", "Playtest!", at="w3", until="w3>", y=560, size=90, color="green"),
        A("chip", "one must-have at a time", at="recap", until="turn", x=1200, y=520, color="green", size=48),
        A("banner", "NEXT: My First Arcade Game", at="turn", color="green"),
        A("cards", items=["Fill in my game plan card", "Build my must-haves", "Playtest and fix one bug"],
          x=1000, y=300, w=640, gap=120, reveal=["next@0.1", "next@0.45", "next@0.8"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
