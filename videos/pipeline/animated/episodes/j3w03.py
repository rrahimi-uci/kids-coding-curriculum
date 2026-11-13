"""Junior Level 3 Week 3: Data Detectives (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/3-bridge-to-python/teaching-material/lessons/week03.tex: a family fruit survey kept with
tally marks (the fifth mark across, like a gate), a bar graph whose tallest bar is the favorite, the
pebbles-in-a-bag analogy for a variable, Exercise 3.2 Fruit Survey Robot (ask and wait, answer,
if/else, two counters), tricky answers (Scratch's = ignores big and small letters, "apples" is a
different word), Exercise 3.3 The Two Apples (bug hunt on paper), only asking what we need, fair
data, and a human bar graph as the wiggle break. The warm-up numbers are this episode's own, not the
ones from Exercise 3.1 Tally Time.

Kit note: the tally chart is drawn on a plain drawing canvas (the `turtle` view with its own title
and no cursor), because the kit has no tally component; its code is never shown.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
ASK = ("sensing", "ask [What is your favorite fruit?] and wait")
IF_APPLE = ("control", "if <answer = apple> then", [("variables", "change [apple votes] by [1]")],
            [("variables", "change [other votes] by [1]")])
FRUITS = ["apple", "banana", "orange", "grapes"]
SURVEY = [3, 6, 2, 1]  # our family survey (12 answers)

TALLY = """import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
rows = [("apple", 3), ("banana", 6), ("orange", 2), ("grapes", 1)]
y = 150
for name, count in rows:
    t.penup()
    t.goto(-200, y - 12)
    t.write(name)
    for k in range(count):
        x = (k // 5) * 130 + (k % 5) * 24
        t.penup()
        if k % 5 == 4:
            t.goto(x - 106, y - 16)
            t.pendown()
            t.goto(x + 10, y + 16)
        else:
            t.goto(x, y - 22)
            t.pendown()
            t.goto(x, y + 22)
    y = y - 100
turtle.done()"""

EPISODE = Episode(level="j3", week=3, scenes=(
    # 1. hook --------------------------------------------------------------------------------------
    Scene("j3-w03-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi", pause=0.3),
        B("Beep boop! Detective Pixi, reporting!", speaker=PIXI, cue="hello", pause=0.5),
        B("Today, we are data detectives!", speaker=NARRATOR, cue="today", pause=0.4),
        B("Data is information we collect.", speaker=NARRATOR, cue="data", pause=0.5),
        B("We will ask one question: what is your favorite fruit? Apple, banana, orange or grapes?",
          speaker=NARRATOR, cue="question", pause=0.6),
        B("Then we count the answers, and draw a graph that tells their story.", speaker=NARRATOR, cue="graph",
          pause=0.5),
        B("Are you ready? Let's go!", speaker=NARRATOR, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True, beep="hello"),
        A("magnifier", x=1500, y=560, at="today", until="question"),
        A("banner", "MISSION: Data detectives", at="today"),
        A("chip", "Data = information we collect", at="data", until="question", x=1300, y=820, color="yellow",
          size=42),
        A("cards", items=["apple", "banana", "orange", "grapes"], x=1060, y=260, w=480, gap=115,
          reveal=["question@0.55", "question@0.65", "question@0.75", "question@0.85"], at="question",
          color="green"),
        A("chip", "Count • Graph • Story", at="graph@0.3", x=1300, y=820, color="sky", size=44),
    )),
    # 2. warm-up: the family survey and tally marks -------------------------------------------------------
    Scene("j3-w03-s02", setting="workshop", beats=(
        B("We asked everyone at home, and the toys too: what is your favorite fruit?", speaker=NARRATOR, cue="ask",
          pause=0.5),
        B("To keep count, we use tally marks. One line for each answer.", speaker=NARRATOR, cue="tally", pause=0.6),
        B("Here's the trick. The fifth line goes across the other four, like a gate.", speaker=NARRATOR,
          cue="gate", pause=0.6),
        B("Then we can count in fives!", speaker=NARRATOR, cue="fives", pause=0.5),
        B("Count the banana row with me: one, two, three, four, the gate makes five, and six!", speaker=NARRATOR,
          cue="count", pause=0.8),
        B("Six bananas! Beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("aiden", x=260, y=980, s=0.8, point=("count", "count$"), moods={"start": "happy", "pixi": "proud"}),
        A("pixi", x=520, y=780, s=0.7, ground=960, beep="pixi"),
        A("turtle", code=TALLY, title="Our tally", cursor=False, x=760, y=200, w=760, h=620, world=230,
          at="ask@0.4", run="tally", duration=9.0),
        A("chip", "1 line = 1 answer", at="tally@0.5", until="gate", x=1680, y=880, color="sky", size=40),
        A("chip", "5th line = a gate", at="gate@0.5", until="count", x=1680, y=880, color="yellow", size=40),
        A("chip", "1, 2, 3, 4, gate = 5, 6!", at="count@0.3", x=1140, y=900, color="orange", size=42),
    )),
    # 3. the bar graph ----------------------------------------------------------------------------------
    Scene("j3-w03-s03", setting="sky", beats=(
        B("A tally is great for counting. A bar graph is great for seeing.", speaker=NARRATOR, cue="seeing",
          pause=0.5),
        B("Each answer gets one square, and the squares stack up into a bar.", speaker=NARRATOR, cue="square",
          pause=0.5),
        B("Apple, three. Banana, six. Orange, two. Grapes, one.", speaker=NARRATOR, cue="read", pause=0.6),
        B("Which fruit is the favorite?", speaker=NARRATOR, cue="fav", pause=3.0),
        B("Banana! The tallest bar is the favorite.", speaker=NARRATOR, cue="banana", pause=0.5),
        B("How many more bananas than apples?", speaker=NARRATOR, cue="more", pause=3.0),
        B("Three more! The graph tells the story of our data at one look.", speaker=NARRATOR, cue="story",
          pause=0.6),
    ), actions=(
        A("bars", x=200, y=260, w=1000, h=560, at="seeing@0.5", values=SURVEY, labels=FRUITS,
          highlight=[("read", "read@0.25", [0]), ("read@0.25", "read@0.55", [1]), ("read@0.55", "read@0.8", [2]),
                     ("read@0.8", "read$", [3]), ("banana", "banana$+0.4", [1]), ("story", "story@0.4", [0, 1])]),
        A("chip", "1 square = 1 answer", at="square", until="fav", x=1530, y=330, color="sky", size=42),
        A("thought", "Which one?", at="fav$+0.2", until="banana", x=1530, y=400),
        A("chip", "Tallest bar = favorite", at="banana", until="more", x=1530, y=330, color="yellow", size=40),
        A("thought", "How many more?", at="more$+0.2", until="story", x=1530, y=400),
        A("chip", "6 is 3 more than 3", at="story", x=1530, y=330, color="orange", size=42),
        A("pixi", x=1560, y=900, s=0.55, at="story", ground=990),
    )),
    # 4. a survey robot: variables are bags of pebbles ----------------------------------------------------
    Scene("j3-w03-s04", setting="lavender", beats=(
        B("Now let's make a survey robot in Scratch!", speaker=NARRATOR, cue="robot", pause=0.4),
        B("It asks a question, waits for you to type the answer, checks it, and counts it.", speaker=NARRATOR,
          cue="does", pause=0.5),
        B("Long ago, shepherds counted sheep with pebbles: one pebble in the bag for each sheep.", speaker=NARRATOR,
          cue="pebbles", pause=0.5),
        B("A variable is like the bag. Each time we change it by one, one more pebble goes in.", speaker=NARRATOR,
          cue="bag", pause=0.5),
        B("Our robot needs two bags: apple votes, and other votes.", speaker=NARRATOR, cue="two", pause=0.6),
    ), actions=(
        A("cat", x=1380, y=820, s=1.0, at="robot", until="pebbles"),
        A("bubble", "What is your favorite fruit?", who="cat", x=1380, y=820, at="robot@0.4", until="pebbles",
          size=34),
        A("cards", items=["Ask", "Wait for the answer", "Check it", "Count it"], x=160, y=260, w=620, gap=118,
          reveal=["does@0.1", "does@0.3", "does@0.55", "does@0.8"], at="does", color="sky"),
        A("chip", "1 pebble = 1 sheep", at="pebbles@0.5", until="two", x=1350, y=330, color="yellow", size=44),
        A("box", "apple votes", x=1180, y=640, at="bag", values=[("bag", 0), ("bag@0.7", 1), ("bag$+0.3", 2)]),
        A("chip", "change by 1 = 1 more pebble", at="bag@0.5", until="two", x=1350, y=860, color="orange",
          size=38),
        A("box", "other votes", x=1560, y=640, at="two@0.5", values=[("two@0.5", 0)]),
    )),
    # 5. Fruit Survey Robot, part 1: set, repeat, ask -------------------------------------------------------
    Scene("j3-w03-s05", setting="mint", beats=(
        B("Let's build the Fruit Survey Robot.", speaker=NARRATOR, cue="build", pause=0.3),
        B("Orange-red Variables: make apple votes, and other votes.", speaker=NARRATOR, cue="vars", pause=0.6),
        B("Yellow Events: when green flag clicked. Then set both of them to zero.", speaker=NARRATOR, cue="setup",
          pause=0.6),
        B("Orange Control: repeat, changed to four. We will ask four people.", speaker=NARRATOR, cue="rep",
          pause=0.5),
        B("Light blue Sensing: ask and wait, inside the repeat. The words are: What is your favorite fruit?",
          speaker=NARRATOR, cue="ask", pause=0.6),
        B("We never ask for names. We only ask what we need.", speaker=NARRATOR, cue="names", pause=0.6),
    ), actions=(
        A("banner", "Exercise 3.2: Fruit Survey Robot", at="build", color="green"),
        A("scratch", "Fruit Survey Robot", blocks=[FLAG, ("variables", "set [apple votes] to [0]"),
                                                   ("variables", "set [other votes] to [0]"),
                                                   ("control", "repeat [10]", [ASK])],
          x=130, y=260, w=960, h=560, scale=1.0, reveal=["setup", "setup@0.5", "setup@0.7", "rep", "ask@0.4"],
          edits=[("rep@0.5", 3, "repeat [4]")], highlight=[(4, "names", "names$")]),
        A("chip", "Variables: orange-red", at="vars", until="setup", x=1460, y=880, color="orange", size=42),
        A("chip", "Events: yellow", at="setup", until="rep", x=1460, y=880, color="yellow", size=42),
        A("chip", "Control: orange", at="rep", until="ask", x=1460, y=880, color="orange", size=42),
        A("chip", "Sensing: light blue", at="ask", until="names", x=1460, y=880, color="sky", size=42),
        A("chip", "Only ask what we need", at="names", x=1460, y=880, color="green", size=42),
        A("box", "apple votes", x=1300, y=420, at="vars@0.5", values=[("vars@0.5", 0)]),
        A("box", "other votes", x=1640, y=420, at="vars@0.8", values=[("vars@0.8", 0)]),
        A("icons", at="names", x=1470, y=680, items=[("person", "No names", "names")], crossed=[0]),
    )),
    # 6. Fruit Survey Robot, part 2: if / else, and a test -------------------------------------------------
    Scene("j3-w03-s06", setting="mint", beats=(
        B("Orange Control: if then else, under the ask.", speaker=NARRATOR, cue="ifelse", pause=0.5),
        B("Green Operators: the equals block goes in the if. Put the round answer block on the left, and type "
          "apple on the right.", speaker=NARRATOR, cue="equals", pause=0.6),
        B("Variables: change apple votes by one in the top gap, and change other votes by one in the bottom gap.",
          speaker=NARRATOR, cue="change", pause=0.6),
        B("Last, purple Looks: say Thank you!, under the repeat.", speaker=NARRATOR, cue="thanks", pause=0.5),
        B("Click the flag, type apple, and press Return.", speaker=NARRATOR, cue="apple", pause=3.0),
        B("Now type banana.", speaker=NARRATOR, cue="banana", pause=2.6),
        B("Apple goes in the apple votes bag, and every other answer goes in other votes!", speaker=NARRATOR,
          cue="works", pause=0.5),
        B("Counting robot, beep beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Fruit Survey Robot (after the sets)",
          blocks=[("control", "repeat [4]", [ASK, IF_APPLE]), ("looks", "say [Thank you!] for [2] seconds")],
          x=130, y=220, w=960, h=800, scale=1.0,
          reveal=["start", "start", "ifelse", "change@0.2", "change@0.65", "thanks"],
          highlight=[(2, "equals", "equals$"), (1, "apple@0.6", "apple$+0.6"), (3, "apple$+0.6", "apple$+2.0"),
                     (1, "banana", "banana$+0.4"), (4, "banana$+0.4", "banana$+2.0")]),
        A("chip", "Control: orange", at="ifelse", until="equals", x=1490, y=710, color="orange", size=42),
        A("chip", "Operators: green", at="equals", until="change", x=1490, y=710, color="green", size=42),
        A("chip", "Variables: orange-red", at="change", until="thanks", x=1490, y=710, color="orange", size=42),
        A("chip", "Looks: purple", at="thanks", until="apple", x=1490, y=710, color="purple", size=42),
        A("stage", x=1140, y=200, w=700, h=440, at="ifelse", flag_at="apple@0.2", sprite_scale=0.8,
          actions=[("apple@0.3", "say", "What is your favorite fruit?", 2.6),
                   ("banana", "say", "What is your favorite fruit?", 2.0)]),
        A("chip", "typed: apple", at="apple$", until="banana", x=1490, y=720, color="white", size=40),
        A("chip", "typed: banana", at="banana$", until="works", x=1490, y=720, color="white", size=40),
        A("box", "apple votes", x=1300, y=900, at="ifelse", values=[("ifelse", 0), ("apple$+0.8", 1)]),
        A("box", "other votes", x=1640, y=900, at="ifelse", values=[("ifelse", 0), ("banana$+0.6", 1)]),
        A("badge", ok=True, at="works", x=1790, y=250),
    )),
    # 7. quick quiz: tricky answers ----------------------------------------------------------------------
    Scene("j3-w03-s07", setting="peach", beats=(
        B("Quick quiz!", speaker=NARRATOR, cue="quiz", pause=0.4),
        B("What if someone types Apple, with a big A? Does the robot count it as apple?", speaker=NARRATOR,
          cue="big", pause=3.0),
        B("Yes! In Scratch, the equals block does not care about big and small letters.", speaker=NARRATOR,
          cue="yes", pause=0.5),
        B("But apples, with an s, counts as other. It is not exactly the same word.", speaker=NARRATOR, cue="s",
          pause=0.6),
        B("And here's a secret: soon we meet Python, and Python is pickier. It thinks Apple and apple are "
          "different!", speaker=NARRATOR, cue="python", pause=0.6),
        B("Picky Python! Beep!", speaker=PIXI, cue="pixi", pause=0.6),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("cards", items=["Apple → apple votes", "APPLE → apple votes", "apples → other votes"], x=200, y=280,
          w=760, gap=130, reveal=["big@0.2", "yes@0.5", "s@0.3"], color="green"),
        A("thought", "Apple or other?", at="big$+0.2", until="yes", x=1430, y=420),
        A("chip", "big or small letters: same in Scratch", at="yes@0.4", until="python", x=1360, y=720,
          color="yellow", size=34),
        A("chip", "Python is pickier!", at="python@0.4", x=1360, y=720, color="sky", size=46),
        A("pixi", x=1420, y=960, s=0.5, at="pixi", ground=1010, beep="pixi"),
    )),
    # 8. bug hunt: The Two Apples -----------------------------------------------------------------------
    Scene("j3-w03-s08", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=NARRATOR, cue="bug", pause=0.5),
        B("Kai made a tally chart. Apple, with a big A, has two marks. apple, with a small a, has three. And "
          "banana has four.", speaker=NARRATOR, cue="kai", pause=0.5),
        B("Kai says banana won!", speaker=NARRATOR, cue="won", pause=0.5),
        B("Are Apple and apple different fruits?", speaker=NARRATOR, cue="diff", pause=3.2),
        B("No! They are the same answer, written two ways. The apple answers were split into two rows.",
          speaker=NARRATOR, cue="no", pause=0.5),
        B("Let's put the rows together. Two and three make five!", speaker=NARRATOR, cue="merge", pause=1.6),
        B("Now we fix the graph too. Apple won, with five!", speaker=NARRATOR, cue="fixed", pause=0.5),
        B("Tidy data means one way to write each answer.", speaker=PIXI, cue="tidy", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Two Apples", at="bug", color="navy"),
        A("bars", x=180, y=280, w=900, h=520, at="kai", until="merge+0.6", values=[2, 3, 4],
          labels=["Apple", "apple", "banana"],
          highlight=[("won", "won$", [2]), ("diff", "no$", [0, 1])]),
        A("chip", "Kai: “banana won!”", at="won", until="diff", x=1450, y=420, color="orange", size=44),
        A("badge", ok=False, at="won@0.5", until="merge", x=1780, y=270),
        A("thought", "Same fruit?", at="diff$+0.2", until="no", x=1450, y=420),
        A("chip", "Same answer, two ways", at="no", until="merge", x=1450, y=420, color="yellow", size=42),
        A("chip", "2 + 3 = 5", at="merge@0.5", x=1450, y=420, color="green", size=52),
        A("bars", x=180, y=280, w=900, h=520, at="merge+0.6", values=[5, 4], labels=["apple", "banana"],
          highlight=[("fixed", "fixed$+0.5", [0])]),
        A("badge", ok=True, at="fixed", x=1780, y=270),
        A("confetti", at="fixed", x=1450, y=520),
        A("chip", "One way to write each answer", at="tidy", x=1450, y=880, color="sky", size=38),
    )),
    # 9. only ask what you need ---------------------------------------------------------------------------
    Scene("j3-w03-s09", setting="workshop", beats=(
        B("Good data detectives only ask what they need.", speaker=NARRATOR, cue="need", pause=0.4),
        B("To find the favorite fruit, we need one answer: the fruit.", speaker=NARRATOR, cue="fruit", pause=0.5),
        B("We never ask for anybody's name, age, address, school, birthday or photo.", speaker=NARRATOR,
          cue="never", pause=0.4),
        B("That's personal information. If a program asks you for it, stop and tell a grown-up.", speaker=NARRATOR,
          cue="personal", pause=0.6),
        B("Zoe's survey asks: What is your favorite fruit? And: What is your home address? Which question should "
          "she delete?", speaker=NARRATOR, cue="zoe", pause=3.0),
        B("The address question! Delete it.", speaker=NARRATOR, cue="delete", pause=0.6),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "zoe": "thinking", "delete": "proud"},
          chin=("zoe", "delete")),
        A("pixi", x=600, y=760, moods={"never": "worried", "delete": "happy"}),
        A("chip", "We need: the fruit", at="fruit@0.4", until="never", x=1260, y=420, color="green", size=48),
        A("icons", at="never", until="zoe", x=1260, y=420, gap=230, crossed=[0, 1, 2, 3],
          items=[("person", "Name, age", "never@0.15"), ("house", "Address", "never@0.4"),
                 ("book", "School", "never@0.55"), ("camera", "Photo", "never@0.85")]),
        A("chip", "Stop and tell a grown-up", at="personal@0.5", until="zoe", x=1260, y=720, color="yellow",
          size=42),
        A("cards", items=["Favorite fruit?", "Home address?"], x=960, y=330, w=620, gap=140, at="zoe",
          reveal=["zoe@0.2", "zoe@0.55"], active=[None, ("delete", "end")]),
        A("thought", "Which one goes?", at="zoe$+0.2", until="delete", x=1720, y=320),
        A("icons", at="delete@0.3", x=1720, y=500, items=[("house", "Delete it!")], crossed=[0]),
    )),
    # 10. fair data + wiggle break: a human bar graph --------------------------------------------------------
    Scene("j3-w03-s10", setting="workshop", beats=(
        B("A fair survey asks all kinds of people.", speaker=NARRATOR, cue="fair", pause=0.4),
        B("If we only asked the apple club, our graph would say everyone loves apples. And it would be wrong!",
          speaker=NARRATOR, cue="club", pause=0.6),
        B("Next week, we find out that computers learn from data like this. So fair data really matters.",
          speaker=NARRATOR, cue="next", pause=0.6),
        B("Wiggle break! Let's make a bar graph out of people. Stand up, and line up behind your favorite fruit!",
          speaker=NARRATOR, cue="wiggle", pause=2.4),
        B("I pick grapes! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("wiggle", "end")], moods={"start": "happy", "club": "surprised",
                                                                  "next": "happy", "wiggle": "proud"}),
        A("pixi", x=600, y=760, beep="pixi", moods={"pixi": "happy"}),
        A("chip", "Ask all kinds of people", at="fair@0.3", until="wiggle", x=1260, y=280, color="green", size=44),
        A("bars", x=880, y=420, w=760, h=330, at="club", until="wiggle", values=[8, 0, 0, 0], labels=FRUITS),
        A("chip", "Only the apple club? Not fair!", at="club@0.6", until="wiggle", x=1260, y=880, color="red",
          size=40),
        A("cards", items=["apple", "banana", "orange", "grapes"], x=1000, y=280, w=480, gap=118,
          reveal=["wiggle@0.4", "wiggle@0.5", "wiggle@0.6", "wiggle@0.7"], at="wiggle",
          active=[None, None, None, ("pixi", "end")]),
    )),
    # 11. recap and next -------------------------------------------------------------------------------
    Scene("j3-w03-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Data!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Tally!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Bar graph!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("Data is information we collect, and a graph tells its story.", speaker=NARRATOR, cue="recap", pause=0.5),
        B("Now it's your turn, with a grown-up.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Do Tally Time, build the Fruit Survey Robot, then hunt for the Two Apples.", speaker=NARRATOR,
          cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=NARRATOR, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Data!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Tally!", at="w2", until="w2>", y=560, size=90, color="purple"),
        A("bigtext", "Bar graph!", at="w3", until="w3>", y=560, size=90, color="green"),
        A("chip", "A graph tells the story", at="recap", until="turn", x=1200, y=520, color="sky", size=48),
        A("banner", "NEXT: Tally Time and the Survey Robot", at="turn", color="green"),
        A("cards", items=["Tally Time", "Build the Fruit Survey Robot", "Hunt for the Two Apples"], x=960, y=280,
          w=720, gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
