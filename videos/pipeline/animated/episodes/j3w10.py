"""Junior Level 3 Week 10: Graduation Showcase (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/3-bridge-to-python/teaching-material/lessons/week10.tex: a look back over the whole junior
track, the last-minute bug check and the typo rescue (steps only; the hidden typo is never shown), the
museum-guide analogy and a showcase in three sentences (Omar's roof loop from week 9), practicing the
sentence frames, the turtle-parade wiggle break, the gallery walk with sticker feedback, what to do if a
website asks for your name (stop, do not type it, get a grown-up), the graduation certificate, and what
is next: main-track Level 1.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

# Omar's postcard from week 9 after parts 1 and 2: a blue house with a gold roof.
OMAR = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.pensize(5)
t.color("blue")
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.color("gold")
for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()"""

ROOF_VIEW = """t.color("gold")
for i in range(3):
    t.forward(100)
    t.left(120)"""

PARADE = """import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pensize(4)
for i in range({n}):
    t.forward({side})
    t.left({turn})
turtle.done()"""

SQUARE = PARADE.format(n=4, side=100, turn=90)
TRIANGLE = PARADE.format(n=3, side=100, turn=120)
HEXAGON = PARADE.format(n=6, side=60, turn=60)

EPISODE = Episode(level="j3", week=10, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j3-w10-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi! I'm Aiden, and this is my robot friend, Pixi.", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Today is a party!", speaker=PIXI, cue="hello", pause=0.5),
        B("Yes! Today is our Graduation Showcase!", speaker=AIDEN, cue="today", pause=0.5),
        B("A showcase is a little show where we share what we made.", speaker=AIDEN, cue="show", pause=0.5),
        B("You will show your Big Build, explain one part of your code, and celebrate!", speaker=AIDEN,
          cue="will", pause=0.5),
        B("Ready? Let's go!", speaker=AIDEN, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello", moods={"hello": "happy"}),
        A("banner", "MISSION: Graduation Showcase", at="today"),
        A("confetti", at="today", x=1300, y=400),
        A("icons", at="will", x=1300, y=520, gap=240,
          items=[("laptop", "Show", "will@0.1"), ("magnifier", "Explain", "will@0.45"),
                 ("trophy", "Celebrate", "will@0.8")]),
    )),
    # 2. look back at the whole junior track -------------------------------------------------------------
    Scene("j3-w10-s02", setting="sky", beats=(
        B("Look how far you have come!", speaker=AIDEN, cue="far", pause=0.4),
        B("In Little Robots, you gave exact steps, and made a cat talk, move and repeat.", speaker=AIDEN,
          cue="l1", pause=0.6),
        B("In Game Makers, you made games with forever loops, scores and messages.", speaker=AIDEN, cue="l2",
          pause=0.6),
        B("And in Bridge to Python, you made patterns, collected data, and learned how computers learn.",
          speaker=AIDEN, cue="l3", pause=0.5),
        B("Then you wrote real Python!", speaker=AIDEN, cue="py", pause=0.5),
        B("That is the whole junior track. Wow!", speaker=AIDEN, cue="whole", pause=0.5),
        B("And every time you found a bug, you treated it like a clue.", speaker=AIDEN, cue="clue", pause=0.8),
    ), actions=(
        A("roadmap", at="far", x=380, y=380, w=1160, items=["Little Robots", "Game Makers", "Bridge to Python"],
          checks=[("l1@0.6", 0), ("l2@0.6", 1), ("py", 2)], current=[("l1", 0), ("l2", 1), ("l3", 2)]),
        A("chip", "steps • Scratch • repeat", at="l1@0.3", until="l2", x=960, y=640, color="orange", size=46),
        A("chip", "forever • score • messages", at="l2@0.3", until="l3", x=960, y=640, color="green", size=46),
        A("chip", "patterns • data • Python", at="l3@0.3", x=960, y=640, color="purple", size=46),
        A("confetti", at="whole", x=960, y=380),
        A("chip", "A bug is a clue!", at="clue", x=960, y=780, color="yellow", size=46),
        A("aiden", x=200, y=1080, s=0.5, at="far", moods={"start": "happy", "whole": "proud"}),
        A("pixi", x=1720, y=980, s=0.5, at="far", ground=1040),
    )),
    # 3. the last-minute bug check and the typo rescue ---------------------------------------------------------
    Scene("j3-w10-s03", setting="mint", beats=(
        B("Before a show, performers check their props. Coders check their code.", speaker=AIDEN, cue="before",
          pause=0.5),
        B("Start your project. Then start it a second time. Does it start the same way?", speaker=AIDEN,
          cue="twice", pause=0.6),
        B("Check each must-have on your plan card. Can everyone see it?", speaker=AIDEN, cue="must", pause=0.5),
        B("Fix one thing only. Then stop building, and save.", speaker=AIDEN, cue="fix", pause=0.6),
        B("Then comes the typo rescue! Your grown-up hides one typo in a copy of the postcard.", speaker=AIDEN,
          cue="rescue", pause=0.5),
        B("Press Run, read the last line of the red text, find the line number, and fix it.", speaker=AIDEN,
          cue="steps", pause=0.6),
        B("Then change one color and one number, and run it again.", speaker=AIDEN, cue="change", pause=0.5),
        B("This is a check, not a test. If a fix takes a long time, ask your grown-up to help.", speaker=AIDEN,
          cue="help", pause=0.8),
    ), actions=(
        A("banner", "Last-minute bug check", at="before", color="navy"),
        A("cards", items=["Start it twice", "Check the must-haves", "Fix one thing, then save"], x=560, y=280,
          w=800, gap=130, reveal=["twice", "must", "fix"], at="twice", until="rescue",
          active=[("twice", "must"), ("must", "fix"), ("fix", "rescue")]),
        A("chip", "Typo rescue!", at="rescue", x=960, y=250, color="orange", size=50),
        A("cards", items=["Press Run", "Read the last line", "Find the line number", "Fix it, run again"],
          x=560, y=360, w=800, gap=120, at="steps", reveal=["steps", "steps@0.2", "steps@0.5", "steps@0.8"]),
        A("chip", "Then: one new color, one new number", at="change", until="help", x=960, y=900, color="green",
          size=42),
        A("chip", "A check, not a test", at="help", x=960, y=900, color="yellow", size=44),
        A("chip", "Check your props!", at="before@0.5", until="twice", x=960, y=420, color="yellow", size=48),
        A("pixi", x=1700, y=880, s=0.55, at="before", ground=980),
    )),
    # 4. the museum guide ----------------------------------------------------------------------------------
    Scene("j3-w10-s04", setting="lavender", beats=(
        B("How do we explain our code? Like a museum guide!", speaker=AIDEN, cue="guide", pause=0.5),
        B("A guide does not explain every painting.", speaker=AIDEN, cue="every", pause=0.4),
        B("A guide stops at one, points, and tells you something special about it.", speaker=AIDEN, cue="one",
          pause=0.6),
        B("You are the guide of your own project.", speaker=AIDEN, cue="you", pause=0.4),
        B("Pick one part, point at the code, and tell us about it.", speaker=AIDEN, cue="pick", pause=0.8),
    ), actions=(
        A("aiden", x=320, y=1000, s=0.8, moods={"start": "happy", "you": "proud"}, point=("one", "one$")),
        A("chip", "Be a museum guide!", at="guide@0.4", until="every", x=1160, y=420, color="purple", size=50),
        A("icons", at="every", x=1160, y=420, gap=300,
          items=[("star", "Painting", "every"), ("heart", "Painting", "every@0.2"), ("trophy", "Painting", "every@0.4")]),
        A("arrow", at="one@0.3", until="you", x1=1160, y1=700, x2=1160, y2=560, color="navy", width=10),
        A("chip", "one part, one point, one story", at="pick", x=1160, y=760, color="orange", size=46),
    )),
    # 5. worked example: a showcase in three sentences ----------------------------------------------------------
    Scene("j3-w10-s05", setting="mint", beats=(
        B("Here is Omar's showcase, in three sentences.", speaker=AIDEN, cue="omar", pause=0.5),
        B("One, my plan: my plan card said a house and a roof, and both parts work.", speaker=AIDEN, cue="s1",
          pause=0.6),
        B("Two, one part of my code: this for loop draws the roof.", speaker=AIDEN, cue="s2", pause=0.5),
        B("Quick quiz! How many times does this loop go round?", speaker=AIDEN, cue="quiz", pause=3.0),
        B("Three times, because a triangle has three sides. The two lines pushed in are inside the loop: forward, "
          "then turn one hundred twenty.", speaker=AIDEN, cue="three", pause=0.6),
        B("Three, what I changed, and credit: I made the house blue and the roof gold. The house and roof came "
          "from the starter program.", speaker=AIDEN, cue="s3", pause=0.6),
        B("Great guide! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("turtle", code=OMAR, x=1220, y=180, w=620, h=600, at="omar", duration=3.0, world=180),
        A("code", code=ROOF_VIEW, title="postcard_omar.py", x=60, y=180, w=1100, h=440, size=46, shell=False,
          at="s2", highlight=[(2, "s2@0.4", "quiz$+3.0"), (3, "three@0.5", "three@0.8"),
                              (4, "three@0.8", "three$"), (1, "s3", "s3@0.5")]),
        A("chip", "1. My plan", at="s1", until="s2", x=610, y=400, color="orange", size=50),
        A("chip", "2. One part of my code", at="s2", until="s3", x=610, y=720, color="sky", size=44),
        A("thought", "How many times?", at="quiz$+0.2", until="three", x=610, y=900),
        A("chip", "3 times: a triangle", at="three", until="s3", x=610, y=860, color="yellow", size=44),
        A("chip", "3. What I changed + credit", at="s3", x=610, y=720, color="green", size=44),
        A("pixi", x=1720, y=980, s=0.45, at="pixi", ground=1040, beep="pixi"),
    )),
    # 6. practice the sentence frames -------------------------------------------------------------------------
    Scene("j3-w10-s06", setting="peach", beats=(
        B("Now you practice. Say your three sentences to your grown-up.", speaker=AIDEN, cue="practice",
          pause=0.5),
        B("My plan card said…", speaker=AIDEN, cue="f1", pause=1.6),
        B("This part of my code…", speaker=AIDEN, cue="f2", pause=1.6),
        B("I changed… and my idea came from…", speaker=AIDEN, cue="f3", pause=1.6),
        B("If you freeze, that's OK. Point at one loop and say what it does.", speaker=AIDEN, cue="freeze",
          pause=0.8),
    ), actions=(
        A("aiden", x=220, y=1000, s=0.75, moods={"start": "happy", "freeze": "proud"}, point=("f1", "f3$")),
        A("cards", items=["My plan card said…", "This part of my code…", "I changed… My idea came from…"],
          x=640, y=300, w=1000, gap=140, reveal=["f1", "f2", "f3"], at="f1",
          active=[("f1", "f2"), ("f2", "f3"), ("f3", "freeze")]),
        A("chip", "Practice with your grown-up", at="practice@0.3", until="f1", x=1140, y=420, color="green",
          size=48),
        A("chip", "Frozen? Point at one loop", at="freeze", x=1140, y=820, color="yellow", size=46),
    )),
    # 7. wiggle break: the turtle parade -----------------------------------------------------------------------
    Scene("j3-w10-s07", setting="workshop", beats=(
        B("Wiggle break! It's a turtle parade. Stand up!", speaker=AIDEN, cue="wiggle", pause=0.4),
        B("Walk a square: four sides, and a quarter turn after each.", speaker=AIDEN, cue="square", pause=4.0),
        B("Now a triangle: three sides, and a big turn.", speaker=AIDEN, cue="triangle", pause=3.0),
        B("Now a hexagon: six small sides.", speaker=AIDEN, cue="hexagon", pause=4.0),
        B("And a graduation bow!", speaker=AIDEN, cue="bow", pause=1.2),
        B("Beep! Bow!", speaker=PIXI, cue="pixi", pause=1.0),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("wiggle", "square"), ("bow", "end")],
          moods={"start": "happy", "bow": "proud"}),
        A("pixi", x=620, y=760, beep="pixi", moods={"pixi": "happy"}),
        A("chip", "WIGGLE BREAK: turtle parade", at="wiggle", until="square", x=1300, y=420, color="orange",
          size=46),
        A("turtle", code=SQUARE, x=1000, y=200, w=600, h=560, at="square", until="triangle", duration=3.0,
          world=170),
        A("turtle", code=TRIANGLE, x=1000, y=200, w=600, h=560, at="triangle", until="hexagon", duration=2.6,
          world=170),
        A("turtle", code=HEXAGON, x=1000, y=200, w=600, h=560, at="hexagon", until="bow", duration=3.0,
          world=170),
        A("bigtext", "Square!", at="square", until="triangle", x=1300, y=860, size=72, color="green"),
        A("bigtext", "Triangle!", at="triangle", until="hexagon", x=1300, y=860, size=72, color="blue"),
        A("bigtext", "Hexagon!", at="hexagon", until="bow", x=1300, y=860, size=72, color="purple"),
        A("bigtext", "Bow!", at="bow", x=1300, y=480, size=100, color="orange"),
        A("confetti", at="bow", x=1300, y=420),
    )),
    # 8. the gallery walk -----------------------------------------------------------------------------------
    Scene("j3-w10-s08", setting="sky", beats=(
        B("Next, the gallery walk. Walk around like visitors in a museum, with your hands behind your back.",
          speaker=AIDEN, cue="walk", pause=0.5),
        B("At each project, ask the owner: May I try it?", speaker=AIDEN, cue="ask", pause=0.5),
        B("Then put one sticker in the column you liked best: the colors, the pattern, or the surprise.",
          speaker=AIDEN, cue="sticker", pause=0.5),
        B("Say why: I liked the colors, because the gold roof stands out.", speaker=AIDEN, cue="why", pause=0.6),
        B("Only kind words. And never change someone else's project.", speaker=AIDEN, cue="kind", pause=0.5),
        B("Did not like something? Then say nothing about it. That is kind, too.", speaker=AIDEN, cue="nothing",
          pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "kind": "proud"},
          path=[("walk", 200, 1000), ("walk$", 320, 1000)]),
        A("chip", "Gallery walk: like a museum", at="walk@0.3", until="ask", x=1060, y=420, color="purple",
          size=48),
        A("chip", "“May I try it?”", at="ask", until="sticker@0.1", x=1060, y=420, color="white", size=50),
        A("icons", at="sticker", x=1060, y=400, gap=380,
          items=[("star", "I liked the colors", "sticker@0.15"), ("star", "I liked the pattern", "sticker@0.45"),
                 ("star", "I liked the surprise", "sticker@0.75")]),
        A("chip", "…because the gold roof stands out", at="why@0.3", until="kind", x=1060, y=760, color="yellow",
          size=42),
        A("chip", "Kind words only • hands off", at="kind", x=1060, y=760, color="green", size=44),
    )),
    # 9. safety: what if a website asks for your name? ---------------------------------------------------------
    Scene("j3-w10-s09", setting="lavender", beats=(
        B("After today, you might find coding websites, games and apps. Some of them ask for things.",
          speaker=AIDEN, cue="after", pause=0.5),
        B("A game says: Type your name, your age and your school to save your score! What do you do?",
          speaker=AIDEN, cue="game", pause=3.0),
        B("Three steps. Say them with me!", speaker=AIDEN, cue="say", pause=0.4),
        B("Stop!", speaker=AIDEN, cue="s1", pause=1.2),
        B("Don't type it!", speaker=AIDEN, cue="s2", pause=1.2),
        B("Get a grown-up!", speaker=AIDEN, cue="s3", pause=1.2),
        B("The grown-up decides. If the site is OK, we use a nickname.", speaker=AIDEN, cue="decides",
          pause=0.5),
        B("A chatbot asks where you live? The same three steps.", speaker=AIDEN, cue="chatbot", pause=0.8),
    ), actions=(
        A("aiden", x=200, y=1000, s=0.7, moods={"start": "happy", "game": "worried", "say": "proud"},
          chin=("game", "say")),
        A("chip", "Some sites ask for things", at="after@0.5", until="game", x=1060, y=420, color="yellow",
          size=48),
        A("panel", "Super Space Game", at="game", until="say", x=660, y=230, w=820, size=40, color="red",
          items=[("game@0.2", "Your name: ______"), ("game@0.35", "Your age: ______"),
                 ("game@0.5", "Your school: ______")]),
        A("thought", "What do you do?", at="game$+0.2", until="say", x=1600, y=700),
        A("icons", at="s1", x=1060, y=420, gap=380, crossed=[1],
          items=[("warning", "1. Stop.", "s1"), ("laptop", "2. Don't type it.", "s2"),
                 ("grownup", "3. Get a grown-up.", "s3")]),
        A("chip", "OK site? A nickname only", at="decides", until="chatbot", x=1060, y=800, color="green",
          size=44),
        A("chip", "Chatbot? Same three steps", at="chatbot", x=1060, y=800, color="orange", size=44),
    )),
    # 10. the graduation certificate ----------------------------------------------------------------------------
    Scene("j3-w10-s10", setting="workshop", beats=(
        B("And now, the moment you have been waiting for!", speaker=AIDEN, cue="moment", pause=0.6),
        B("You planned a Big Build, built it part by part, and explained your code.", speaker=AIDEN,
          cue="planned", pause=0.6),
        B("You are a Bridge to Python graduate!", speaker=AIDEN, cue="grad", pause=0.6),
        B("Give yourself a big clap!", speaker=AIDEN, cue="clap", pause=2.6),
        B("Hooray! Beep, beep, hooray!", speaker=PIXI, cue="hooray", pause=0.5),
        B("Put your certificate where you can see it!", speaker=AIDEN, cue="put", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("grad", "end")], moods={"start": "happy", "grad": "proud"}),
        A("pixi", x=600, y=760, beep="hooray", moods={"grad": "proud"}),
        A("panel", "Junior Graduation Certificate", at="moment", x=900, y=220, w=900, size=38, color="purple",
          items=[("planned@0.1", "Planned a Big Build"), ("planned@0.4", "Built it part by part"),
                 ("planned@0.75", "Explained my code"), ("grad@0.3", "Bridge to Python graduate!")]),
        A("sfx", "chime", at="grad"),
        A("confetti", at="grad", x=1350, y=400),
        A("bigtext", "Clap, clap, clap!", at="clap", x=1350, y=820, size=72, color="orange"),
        A("confetti", at="hooray", x=1350, y=420),
    )),
    # 11. what's next, and goodbye ---------------------------------------------------------------------------
    Scene("j3-w10-s11", setting="workshop", tail=0.8, beats=(
        B("What comes next? Main-track Level 1, the course for grades four and five.", speaker=AIDEN,
          cue="what", pause=0.5),
        B("Lots of it will feel familiar: Scratch, loops, events and Python.", speaker=AIDEN, cue="familiar",
          pause=0.5),
        B("Until then, Scratch and Thonny stay on your Mac for free play. Offline, with no accounts.",
          speaker=AIDEN, cue="until", pause=0.5),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Check your Big Build, show it off, and visit the gallery.", speaker=AIDEN, cue="next", pause=0.6),
        B("I'm so proud of you. Happy coding, graduates!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("chip", "Next: main-track Level 1", at="what@0.3", until="turn", x=1200, y=400, color="purple", size=48),
        A("chip", "Scratch • loops • events • Python", at="familiar", until="turn", x=1200, y=540, color="sky",
          size=44),
        A("chip", "Free play: offline, no accounts", at="until", until="turn", x=1200, y=680, color="green",
          size=44),
        A("banner", "NEXT: Bug check, showcase, gallery walk", at="turn", color="green"),
        A("cards", items=["Last-minute bug check", "My showcase", "Gallery walk"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("chip", "Happy coding, graduates!", at="bye", x=1320, y=760, color="orange", size=46),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
