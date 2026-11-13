"""Junior Level 2 Week 10: Arcade Showcase (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/2-game-makers/teaching-material/lessons/week10.tex: the arcade (show in one minute, let
someone play, celebrate), the last-minute bug check (Exercise 10.1: flag twice, play to win, play to
lose, sound on) with its most common bug (a "set misses to 0" missing at the top of the referee
script), a design choice and the shopkeeper analogy, the worked example "A one-minute demo" with Mei's
Banana Drop (what it is, how to win and lose, "I chose 3 misses, not 1", credit, hand over), the exit
question as a quiz (3 changed to 5: easier), the sentence frames (Exercise 10.2) and the show-me corner,
the arcade gallery with sticker feedback (Exercise 10.3), the arcade dance, showcase safety (family
only, nicknames, credit), and the Game Maker certificate.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

BIG = 1.25  # block scale: big enough for young eyes
SPRITE = 1.0  # sprite size on the stage

FLAG = ("event", "when {flag} clicked")
SET_SCORE = ("variables", "set [score] to [0]")
SET_MISSES = ("variables", "set [misses] to [0]")
GOAL = ("looks", "say [Catch 10 apples!] for [2] seconds")
LOSE = ("control", "if <misses = 3> then", [("looks", "say [Game over!] for [2] seconds"),
                                            ("control", "stop [all]")])
TOP = 130  # the hidden Star marker (stage coordinates)
DEMO = ["What it is", "How to win and lose", "A design choice", "Credit", "Hand over"]

EPISODE = Episode(level="j2", week=10, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j2-w10-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, game makers! I'm Aiden, and this is Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Welcome to the arcade!", speaker=PIXI, cue="hello", pause=0.5),
        B("Today, our home is an arcade! At an arcade, people walk around and play games.", speaker=AIDEN,
          cue="arcade", pause=0.5),
        B("We do three things. We show our game in one minute, we let someone play it, and we celebrate!",
          speaker=AIDEN, cue="three", pause=0.6),
        B("Ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "arcade": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("banner", "MISSION: Arcade Showcase", at="arcade"),
        A("cards", items=["Show it in one minute", "Let someone play", "Celebrate!"], x=1000, y=300, w=640,
          gap=130, at="three", reveal=["three@0.2", "three@0.55", "three@0.85"], color="yellow"),
    )),
    # 2. last-minute bug check ------------------------------------------------------------------------
    Scene("j2-w10-s02", setting="lavender", beats=(
        B("Before an arcade opens, the owners check every machine. Let's do a last-minute bug check.",
          speaker=AIDEN, cue="check", pause=0.5),
        B("One: click the flag. Do the score and misses start at zero? Does the game say its goal?",
          speaker=AIDEN, cue="one", pause=0.6),
        B("Two: play to win. Does it say You win, and stop?", speaker=AIDEN, cue="two", pause=0.6),
        B("Three: click the flag again, and play to lose. Game over?", speaker=AIDEN, cue="three", pause=0.6),
        B("Four: is the sound on? Can you hear it?", speaker=AIDEN, cue="four", pause=0.6),
        B("Found a bug? Fix one thing, then save your game.", speaker=AIDEN, cue="save", pause=0.8),
    ), actions=(
        A("banner", "Exercise 10.1: Last-Minute Bug Check", at="check", color="green"),
        A("cards", items=["Flag: starts at 0? Says the goal?", "Play to win: You win! and stop?",
                          "Flag again, play to lose: Game over?", "Sound on?"],
          x=260, y=280, w=920, gap=150, at="one", color="purple",
          reveal=["one", "two", "three", "four"],
          active=[("one", "two"), ("two", "three"), ("three", "four"), ("four", "save")],
          done=["two", "three", "four", "save"]),
        A("icons", at="check", until="end", x=1550, y=520, gap=260, items=[("game", "Check every game", "check@0.4")]),
    )),
    # 3. bug hunt: the second game -------------------------------------------------------------------
    Scene("j2-w10-s03", setting="mint", beats=(
        B("Bug hunt! Here is a common last-minute bug.", speaker=AIDEN, cue="bug", pause=0.4),
        B("The first game works. But on the second game, it says Game over right away!", speaker=AIDEN,
          cue="second", pause=1.0),
        B("Look at the top of the referee script. What is missing?", speaker=AIDEN, cue="missing", pause=3.0),
        B("Set misses to zero! The misses were still three from the last game.", speaker=AIDEN, cue="answer",
          pause=0.6),
        B("Snap set misses to zero at the top, and test again.", speaker=AIDEN, cue="fix", pause=3.0),
        B("Now every game starts fresh at zero. Fixed!", speaker=AIDEN, cue="fixed", pause=0.5),
        B("Every arcade game has a bug sometimes. Fix one thing, save, then stop building.", speaker=AIDEN,
          cue="calm", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Second Game", at="bug", color="navy"),
        A("scratch", "Bowl: top of the referee", blocks=[FLAG, SET_SCORE, GOAL], x=130, y=260, w=860, h=420,
          scale=BIG, at="second", until="fix@0.4", highlight=[(1, "missing", "answer$")]),
        A("scratch", "Bowl: top of the referee (fixed)", blocks=[FLAG, SET_SCORE, SET_MISSES, GOAL], x=130,
          y=260, w=860, h=520, scale=BIG, at="fix@0.4", highlight=[(2, "fix@0.4", "fixed$")]),
        A("sfx", "snap", at="fix@0.4"),
        A("stage", x=1100, y=230, w=700, h=480, at="second", flag_at="second@0.5", sprite="bowl",
          sprite_y=-110, sprite_scale=SPRITE,
          monitors=[("score", [("second", 4), ("second@0.55", 0), ("fix$+0.3", 0)]),
                    ("misses", [("second", 3), ("fix$+0.3", 0)])],
          actions=[("second@0.6", "say", "Game over!", 2.0), ("fix$+0.4", "say", "Catch 10 apples!", 2.4)]),
        A("badge", ok=False, at="second@0.8", until="fixed", x=1760, y=290),
        A("thought", "What is missing?", at="missing$+0.2", until="answer", x=1450, y=860),
        A("chip", "misses still 3!", at="answer", until="fix", x=1450, y=860, color="red", size=46),
        A("chip", "starts fresh at 0", at="fixed", until="calm", x=1450, y=860, color="green", size=46),
        A("badge", ok=True, at="fixed", x=1760, y=290),
        A("chip", "Fix one thing. Save. Stop.", at="calm", x=1450, y=860, color="yellow", size=42),
    )),
    # 4. a design choice and the shopkeeper -------------------------------------------------------------
    Scene("j2-w10-s04", setting="workshop", beats=(
        B("In your one minute, say what your game is, how to win and lose, and one design choice.",
          speaker=AIDEN, cue="minute", pause=0.5),
        B("A design choice is something you decided on purpose, and why.", speaker=AIDEN, cue="design",
          pause=0.6),
        B("Imagine you run a game stand at a fair. A visitor comes. You say what the game is, how to play and "
          "win, and one cool thing about it.", speaker=AIDEN, cue="stand", pause=0.5),
        B("Then you hand them the controls, and cheer them on!", speaker=AIDEN, cue="cheer", pause=0.4),
        B("Go, go, go!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "cheer": "proud"}, point=("design", "design$"),
          wave=("cheer", "end")),
        A("pixi", x=600, y=760, beep="pixi"),
        A("chip", "design choice = decided on purpose, and why", at="design", until="stand", x=1250, y=360,
          color="yellow", size=38),
        A("icons", at="stand", until="end", x=1250, y=420, gap=270,
          items=[("person", "What it is", "stand@0.4"), ("trophy", "How to win", "stand@0.6"),
                 ("star", "One cool thing", "stand@0.85")]),
        A("chip", "Hand over the controls!", at="cheer", x=1250, y=720, color="green", size=44),
    )),
    # 5. Mei's one-minute demo, part 1 -------------------------------------------------------------------
    Scene("j2-w10-s05", setting="sky", beats=(
        B("Watch me show Mei's game, Banana Drop.", speaker=AIDEN, cue="watch", pause=0.5),
        B("What it is: My game is called Banana Drop. You are the Bowl. Use the arrow keys.", speaker=AIDEN,
          cue="what", pause=0.6),
        B("How to win and lose: Catch ten bananas to win. Miss three, and it is game over.", speaker=AIDEN,
          cue="how", pause=0.8),
    ), actions=(
        A("banner", "A one-minute demo", at="watch", color="green"),
        A("cards", items=DEMO, x=130, y=250, w=660, gap=118, at="watch", color="green",
          reveal=["watch@0.3"] * 5, active=[("what", "how"), ("how", "end"), None, None, None],
          done=["how", None, None, None, None]),
        A("stage", x=1000, y=230, w=780, h=520, at="watch", flag_at="what@0.4", sprite="banana",
          sprite_scale=SPRITE, sprite_x=-60, sprite_y=TOP, extra=[("bowl", -60, -130)],
          monitors=[("score", [("watch", 0), ("how+0.6", 1)]), ("misses", [("watch", 0)])],
          actions=[("what@0.5", "goto", -60, -95, 2.0), ("how", "goto", -60, TOP, 0.05)]),
        A("chip", "Banana Drop", at="what@0.3", until="how", x=1390, y=860, color="yellow", size=48),
        A("chip", "Catch 10 • Miss 3", at="how@0.3", x=1390, y=860, color="orange", size=48),
    )),
    # 6. Mei's one-minute demo, part 2 -------------------------------------------------------------------
    Scene("j2-w10-s06", setting="sky", beats=(
        B("A design choice: I chose three misses, not one, because my Player said one was too hard. That was "
          "a wish from the playtest.", speaker=AIDEN, cue="choice", pause=0.6),
        B("Then point at the script, and read the if: If misses equals three, then Game over, stop all.",
          speaker=AIDEN, cue="read", pause=0.6),
        B("Credit: The bananas and the bowl are from the Scratch library.", speaker=AIDEN, cue="credit",
          pause=0.6),
        B("Hand over: Who wants to play?", speaker=AIDEN, cue="hand", pause=0.4),
        B("Me! Me! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "A one-minute demo", at="start", color="green"),
        A("cards", items=DEMO, x=130, y=250, w=660, gap=118, at="start", color="green",
          active=[None, None, ("choice", "credit"), ("credit", "hand"), ("hand", "end")],
          done=["start", "start", "credit", "hand", "pixi"]),
        A("scratch", "Mei's referee", blocks=[LOSE], x=1000, y=280, w=800, h=440, scale=BIG, at="choice@0.3",
          highlight=[(0, "read@0.3", "credit")]),
        A("chip", "3 misses, not 1", at="choice@0.4", until="read", x=1390, y=790, color="yellow", size=46),
        A("chip", "a wish from the playtest", at="choice@0.8", until="read", x=1390, y=900, color="green",
          size=42),
        A("chip", "from the Scratch library", at="credit", until="hand", x=1390, y=790, color="sky", size=44),
        A("pixi", x=1390, y=880, s=0.5, at="hand", ground=960, beep="pixi"),
    )),
    # 7. quick quiz: 3 becomes 5 --------------------------------------------------------------------------
    Scene("j2-w10-s07", setting="peach", beats=(
        B("Quick quiz! What would happen if Mei changed three to five?", speaker=AIDEN, cue="quiz", pause=0.5),
        B("Would the game be easier, or harder?", speaker=AIDEN, cue="which", pause=3.2),
        B("Easier! The game ends after five misses, not three. You can miss more before it is game over.",
          speaker=AIDEN, cue="easier", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Mei's referee", blocks=[LOSE], x=180, y=300, w=820, h=440, scale=BIG, at="quiz",
          edits=[("quiz@0.7", 0, "if <misses = 5> then")], highlight=[(0, "quiz@0.7", "which$")]),
        A("thought", "Easier or harder?", at="which$+0.2", until="easier", x=1450, y=480),
        A("chip", "Easier!", at="easier", x=1450, y=420, color="green", size=56),
        A("chip", "5 misses before game over", at="easier@0.4", x=1450, y=560, color="orange", size=42),
    )),
    # 8. your own demo, and the show-me corner ------------------------------------------------------------
    Scene("j2-w10-s08", setting="lavender", beats=(
        B("Now practice your own demo with a partner. Use these sentences.", speaker=AIDEN, cue="practice",
          pause=0.5),
        B("Say the name of your game, and who the player is. Say how you win.", speaker=AIDEN, cue="frames",
          pause=0.5),
        B("Then say one choice: I chose this, because of that.", speaker=AIDEN, cue="choice", pause=0.6),
        B("No design choice yet? Ask: Why that goal? Why that speed? Why that sprite?", speaker=AIDEN,
          cue="stuck", pause=0.5),
        B("Any reason you give is a design choice!", speaker=AIDEN, cue="any", pause=0.5),
        B("Your grown-up may also say: Show me a message. Show me a My Block.", speaker=AIDEN, cue="showme",
          pause=0.8),
    ), actions=(
        A("banner", "Exercise 10.2: My One-Minute Demo", at="practice", color="green"),
        A("panel", "My demo", x=200, y=240, w=1000, size=40, at="practice",
          items=[("frames@0.1", "My game is called ..."), ("frames@0.4", "You are the ..."),
                 ("frames@0.75", "You win when ..."), ("choice@0.2", "I chose ..., because ...")]),
        A("chip", "Why 10? Why 3? Why that sprite?", at="stuck", until="showme", x=1500, y=360, color="yellow",
          size=38),
        A("chip", "Any reason = a design choice!", at="any", until="showme", x=1500, y=500, color="green",
          size=38),
        A("scratch", blocks=[("event", "broadcast [hello]")], x=1300, y=330, w=560, h=120, panel=False,
          scale=BIG, at="showme@0.4"),
        A("scratch", blocks=[("myblocks", "celebrate")], x=1300, y=500, w=560, h=120, panel=False, scale=BIG,
          at="showme@0.8"),
        A("chip", "Show-me corner", at="showme", x=1500, y=720, color="pink", size=44),
    )),
    # 9. the arcade gallery with stickers --------------------------------------------------------------------
    Scene("j2-w10-s09", setting="workshop", beats=(
        B("Now the arcade gallery! Visitors walk around and play each game.", speaker=AIDEN, cue="gallery",
          pause=0.4),
        B("At each game, ask: May I play? Then play one round.", speaker=AIDEN, cue="may", pause=0.5),
        B("Put a sticker on the part you liked best: fun to play, cool sounds, or great surprise.",
          speaker=AIDEN, cue="sticker", pause=0.6),
        B("Then say two stars and a wish, with kind words: I liked the pop sound and the ghost. I wish it was a "
          "bit slower.", speaker=AIDEN, cue="stars", pause=0.6),
        B("And visitors never change someone else's game.", speaker=AIDEN, cue="never", pause=0.5),
        B("I liked the surprise wait! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "stars": "proud"}),
        A("pixi", x=600, y=760, moods={"stars": "happy"}),
        A("bubble", "May I play?", x=1250, y=320, at="may@0.3", until="sticker", size=44),
        A("icons", at="sticker", until="end", x=1300, y=420, gap=300,
          items=[("game", "Fun to play", "sticker@0.55"), ("music", "Cool sounds", "sticker@0.7"),
                 ("star", "Great surprise", "sticker@0.85")]),
        A("chip", "two stars and a wish", at="stars", until="never", x=1300, y=700, color="yellow", size=44),
        A("chip", "Never change someone else's game", at="never", x=1300, y=700, color="red", size=40),
    )),
    # 10. the arcade dance (wiggle break) ------------------------------------------------------------------
    Scene("j2-w10-s10", setting="workshop", beats=(
        B("Wiggle break! Let's do the arcade dance.", speaker=AIDEN, cue="dance", pause=0.5),
        B("Slide like a bowl.", speaker=AIDEN, cue="slide", pause=1.8),
        B("Fall like a banana.", speaker=AIDEN, cue="fall", pause=1.8),
        B("Sneak through a maze.", speaker=AIDEN, cue="sneak", pause=1.8),
        B("Freeze for Game over!", speaker=AIDEN, cue="freeze", pause=1.8),
        B("And jump for You win!", speaker=AIDEN, cue="jump", pause=1.6),
        B("Beep! Arcade dance!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("jump", "end")], moods={"start": "happy", "freeze": "surprised",
                                                                "jump": "proud"},
          path=[("slide", 300, 960), ("slide+0.7", 420, 960), ("slide+1.5", 220, 960), ("slide+2.2", 300, 960)]),
        A("pixi", x=640, y=760, beep="pixi",
          path=[("fall", 640, 560), ("fall+1.4", 640, 800), ("jump", 640, 600), ("jump+0.6", 640, 760)]),
        A("bigtext", "Slide!", at="slide", until="fall", x=1300, y=400, size=80, color="blue"),
        A("bigtext", "Fall!", at="fall", until="sneak", x=1300, y=400, size=80, color="orange"),
        A("bigtext", "Sneak!", at="sneak", until="freeze", x=1300, y=400, size=80, color="purple"),
        A("bigtext", "Freeze!", at="freeze", until="jump", x=1300, y=400, size=80, color="red"),
        A("bigtext", "Jump!", at="jump", x=1300, y=400, size=80, color="green"),
        A("confetti", at="jump", x=1300, y=420),
    )),
    # 11. showcase safety ------------------------------------------------------------------------------------
    Scene("j2-w10-s11", setting="workshop", beats=(
        B("Our arcade is for our family, here at home.", speaker=AIDEN, cue="family", pause=0.4),
        B("On the screen, we use nicknames, never our full names, our school or our address.", speaker=AIDEN,
          cue="nick", pause=0.5),
        B("We do not put our games on the internet, or send them to people we do not know.", speaker=AIDEN,
          cue="online", pause=0.5),
        B("We give credit for the sprites and ideas we did not make.", speaker=AIDEN, cue="credit", pause=0.5),
        B("Want to show your game to someone else? Ask a grown-up first.", speaker=AIDEN, cue="ask", pause=0.5),
        B("Quick check: on the screen, do we use our full name, or a nickname?", speaker=AIDEN, cue="check",
          pause=3.0),
        B("A nickname!", speaker=AIDEN, cue="nickname", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "check": "thinking", "nickname": "proud"},
          chin=("check", "nickname")),
        A("pixi", x=600, y=760),
        A("thought", "Full name or nickname?", at="check$+0.2", until="nickname", x=1260, y=760),
        A("chip", "A nickname!", at="nickname", x=1260, y=760, color="green", size=48),
        A("icons", at="family", until="end", x=1260, y=480, gap=230,
          items=[("house", "Family only", "family@0.3"), ("person", "Nicknames", "nick@0.3"),
                 ("wifi_off", "Not online", "online@0.4"), ("star", "Give credit", "credit@0.3"),
                 ("grownup", "Ask first", "ask@0.4")]),
    )),
    # 12. certificate, recap and goodbye ------------------------------------------------------------------
    Scene("j2-w10-s12", setting="workshop", tail=0.8, beats=(
        B("You planned a game, built it, let a Player test it, fixed bugs, and explained your choices.",
          speaker=AIDEN, cue="did", pause=0.5),
        B("You are now a Game Maker!", speaker=AIDEN, cue="maker", pause=0.6),
        B("Let's give a big clap for every game maker. Clap, clap, clap!", speaker=AIDEN, cue="clap", pause=2.6),
        B("Say it with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Show!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Explain!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Celebrate!", speaker=AIDEN, cue="w3", pause=1.2),
        B("Now it's your turn, with your family.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Check your game, give your one-minute demo, then visit the arcade gallery.", speaker=AIDEN,
          cue="next", pause=0.6),
        B("Congratulations, Game Makers! Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("maker", "clap$+2.4"), ("bye", "end")],
          moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("icons", at="did", until="maker", x=1200, y=420, gap=230,
          items=[("book", "Planned", "did@0.1"), ("gear", "Built", "did@0.25"), ("game", "Tested", "did@0.45"),
                 ("magnifier", "Fixed", "did@0.65"), ("person", "Explained", "did@0.85")]),
        A("bigtext", "Game Maker!", at="maker", until="sayit", y=520, size=96, color="orange"),
        A("sfx", "sparkle", at="clap$+0.3"),
        A("icons", at="maker", until="sayit", x=1200, y=780, gap=230, items=[("trophy", "Certificate", "maker")]),
        A("confetti", at="maker", x=1200, y=420),
        A("bigtext", "Show!", at="w1", until="w1>", y=560, size=90, color="green"),
        A("bigtext", "Explain!", at="w2", until="w2>", y=560, size=90, color="purple"),
        A("bigtext", "Celebrate!", at="w3", until="w3>", y=560, size=90, color="orange"),
        A("banner", "NEXT: Arcade Showcase", at="turn", color="green"),
        A("cards", items=["Last-minute bug check", "My one-minute demo", "Arcade gallery stickers"], x=1000,
          y=300, w=640, gap=120, reveal=["next@0.1", "next@0.45", "next@0.8"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
