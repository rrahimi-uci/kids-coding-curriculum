"""Level 2 Week 12: Showcase: The Family Arcade (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene


def comet_catch(gray: bool = False) -> str:
    """A Comet Catch frame: circle comets, square rocks and a rocket (all gray proves the shapes differ)."""
    comet, rock, rocket = ("gray", "gray", "gray") if gray else ("orange", "purple", "blue")
    return f'''import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
for x, y in [(-130, 150), (120, 60)]:
    pen.goto(x, y)
    pen.dot(46, "{comet}")
pen.color("{rock}")
for x, y in [(20, 170), (-60, 20)]:
    pen.goto(x - 22, y - 22)
    pen.begin_fill()
    for corner in [(x + 22, y - 22), (x + 22, y + 22), (x - 22, y + 22)]:
        pen.goto(corner)
    pen.end_fill()
pen.goto(-24, -200)
pen.color("{rocket}")
pen.begin_fill()
for corner in [(24, -200), (0, -140)]:
    pen.goto(corner)
pen.end_fill()'''


EPISODE = Episode(level=2, week=12, scenes=(
    Scene("l2-w12-s01", setting="workshop", lead_in=0.2, beats=(
        B("Hi, coders!", cue="hi", pause=0.3),
        B("Today the classroom becomes the Family Arcade.", cue="today", pause=0.3),
        B("Every computer is a game or an art studio, and families walk from station to station to play.",
          cue="every", pause=0.4),
        B("Nova's heart is thumping.", cue="heart", pause=0.2),
        B("‘What if I forget what to say?’", speaker=NOVA, cue="forget", pause=0.4),
        B("Pixel beeps.", cue="beeps", pause=0.2),
        B("‘Do you explain every single line?’", speaker=PIXEL, cue="everyline", pause=0.4),
        B("No way!", cue="noway", pause=0.4),
        B("So what makes a great showcase?", cue="great", pause=2.4),
    ), actions=(
        A("laptop", at="every", x=1080, y=880, s=0.6),
        A("laptop", at="every@0.15", x=1400, y=880, s=0.6),
        A("laptop", at="every@0.3", x=1720, y=880, s=0.6),
        A("chip", "Comet", at="every", x=1080, y=760, color="white", size=32),
        A("chip", "Star", at="every@0.15", x=1400, y=760, color="white", size=32),
        A("chip", "Mo", at="every@0.3", x=1720, y=760, color="white", size=32),
        A("grownup", at="every@0.5", s=0.85, x=900, y=1050,
          path=[("every@0.5", 900, 1050), ("forget", 1240, 1050), ("noway", 1560, 1050)]),
        A("nova", x=300, y=960, enter="left", wave="hi",
          moods={"heart": "worried", "noway": "surprised", "great": "thinking"}, chin=("great", "end")),
        A("pixel", x=650, y=760, drop=True, moods={"everyline": "thinking", "noway": "happy"},
          beep=("beeps", "beeps$")),
        A("banner", "FINAL MISSION: The Family Arcade", at="today"),
        A("icons", at="heart", until="beeps", x=560, y=410, items=[("heart", "thump thump", "heart")]),
        A("chip", "explain all 200 lines?", at="everyline", until="great", x=1100, y=380, color="white", size=40),
        A("icons", at="noway", until="great", x=1500, y=440, crossed=[0], items=[("book", "every line", "noway")]),
        A("chip", "Short, clear, and proud", at="great@0.5", x=1100, y=300, color="yellow", size=46),
        A("thought", "", at="great$+0.3", until="end", x=640, y=440),
    )),
    Scene("l2-w12-s02", setting="sky", beats=(
        B("First, code freeze!", cue="freeze", pause=0.3),
        B("No new features today.", cue="nofeat", pause=0.2),
        B("Only fixing a crash is allowed.", cue="crash", pause=0.2),
        B("Save a backup copy, too, just in case.", cue="backup", pause=0.4),
        B("A great pitch is short: about one minute.", cue="short", pause=0.2),
        B("Answer four questions, in this order.", cue="four", pause=0.2),
        B("One: what is it?", cue="q1", pause=0.2),
        B("Two: how does one part work?", cue="q2", pause=0.2),
        B("Pick one function, the loop, the list, the dictionary or the file, and say what goes in and what comes "
          "out.", cue="pick", pause=0.3),
        B("Three: one design decision.", cue="q3", pause=0.2),
        B("That's a choice you made on purpose, and why.", cue="choice", pause=0.3),
        B("Four: what next?", cue="q4", pause=0.2),
        B("Not finished? That's normal.", cue="normal", pause=0.2),
        B("Show what works, then say what you would add next.", cue="show", pause=0.6),
    ), actions=(
        A("bigtext", "CODE FREEZE: save a backup", at="freeze", until="short", y=200, size=60, color="blue"),
        A("icons", at="nofeat", until="short", x=960, y=500, gap=440, crossed=[0],
          items=[("star", "new features", "nofeat"), ("check", "fixing a crash", "crash"),
                 ("file", "mygame-showcase.py", "backup")]),
        A("sfx", "sparkle", at="freeze"),
        A("icons", at="short", until="q1", x=960, y=450, items=[("clock", "about 1 minute", "short")]),
        A("chip", "1 What is it?  2 How does one part work?", at="q1", x=960, y=200, color="orange", size=46),
        A("listrow", at="pick", until="q3", x=960, y=420, cell=300, indexes=False,
          items=["function", "loop", "list", "dictionary", "file"],
          highlight=[("pick@0.1", "pick@0.25", 0), ("pick@0.25", "pick@0.35", 1), ("pick@0.35", "pick@0.45", 2),
                     ("pick@0.45", "pick@0.55", 3), ("pick@0.55", "pick@0.65", 4)]),
        A("chip", "what goes in → what comes out", at="pick@0.7", until="q3", x=960, y=620, color="green", size=42),
        A("chip", "3 One design decision", at="q3", x=960, y=360, color="sky", size=46),
        A("chip", "a choice made on purpose, and why", at="choice", until="q4", x=960, y=560, color="white", size=38),
        A("chip", "4 What next?", at="q4", x=960, y=520, color="green", size=46),
        A("chip", "Not finished? That's normal.", at="normal", x=960, y=700, color="white", size=40),
        A("chip", "show what works → say what's next", at="show", x=960, y=840, color="yellow", size=40),
    )),
    Scene("l2-w12-s03", setting="lavender", beats=(
        B("Let's watch Nova's pitch.", cue="watch", pause=0.2),
        B("Pixel is the demo driver, playing the game.", cue="driver", pause=0.2),
        B("Nova is the explainer.", cue="explainer", pause=0.3),
        B("‘This is Comet Catch. You catch comets with a rocket.’", speaker=NOVA, cue="p1", pause=0.3),
        B("That's question one.", cue="one", pause=0.3),
        B("‘Our next x function gets the position and the direction, and returns the new position, but never off "
          "the screen.", speaker=NOVA, cue="p2a", pause=0.1),
        B("We have a test for that.’", speaker=NOVA, cue="p2b", pause=0.3),
        B("That's how one part works: what goes in, and what comes out.", cue="two", pause=0.3),
        B("‘The comets are circles and the rocks are squares, so you can tell them apart even without color.’",
          speaker=NOVA, cue="p3", pause=0.3),
        B("That's a design decision.", cue="three", pause=0.3),
        B("‘Next, we would add a slow mode for beginners.’", speaker=NOVA, cue="p4", pause=0.3),
        B("Four questions, about a minute.", cue="about", pause=0.2),
        B("Then the team takes one question.", cue="question", pause=0.2),
        B("Partners, swap halfway so both of you speak!", cue="swap", pause=0.6),
    ), actions=(
        A("nova", x=270, y=1000, s=0.78, moods={"start": "happy", "about": "proud"}, wave=("swap", "end")),
        A("pixel", x=1550, y=880, s=0.5, ground=980, at="driver", beep=[("driver", "driver$")]),
        A("turtle", code=comet_catch(), title="Comet Catch", at="driver", until="p3@0.5", x=1240, y=170, w=620,
          h=480, world=230, duration=0.01, cursor=False),
        A("turtle", code=comet_catch(gray=True), title="Comet Catch (no color)", at="p3@0.5", until="p4", x=1240,
          y=170, w=620, h=480, world=230, duration=0.01, cursor=False),
        A("turtle", code=comet_catch(), title="Comet Catch", at="p4", x=1240, y=170, w=620, h=480, world=230,
          duration=0.01, cursor=False),
        A("cards", at="watch", x=520, y=230, w=660, gap=110,
          items=["What is it?", "How does one part work?", "One design decision", "What next?"],
          reveal=["watch", "watch@0.3", "watch@0.6", "watch@0.9"],
          active=[("p1", "one$"), ("p2a", "two$"), ("p3", "three$"), ("p4", "about")],
          done=["one$", "two$", "three$", "about"]),
        A("chip", "Pixel = demo driver", at="driver", until="p1", x=860, y=720, color="sky", size=38),
        A("chip", "Nova = explainer", at="explainer", until="p1", x=860, y=830, color="orange", size=38),
        A("chip", "next_x: position in, new position out", at="p2a@0.4", until="p3", x=860, y=700, color="sky",
          size=36),
        A("tests", "pytest", at="p2b", until="p3", x=450, y=780, w=790,
          items=[("p2b", "test_stops_at_the_right_edge", True)]),
        A("chip", "Circles vs squares: not color alone", at="p3@0.5", until="p4", x=860, y=720, color="yellow",
          size=36),
        A("chip", "What next: a slow mode", at="p4@0.4", until="about", x=860, y=720, color="green", size=38),
        A("icons", at="about", until="swap", x=860, y=780, gap=280,
          items=[("clock", "about 1 minute", "about"), ("person", "1 question", "question")]),
        A("chip", "Swap halfway so both speak", at="swap", x=860, y=760, color="purple", size=42),
    )),
    Scene("l2-w12-s04", setting="mint", beats=(
        B("Before the party, one last challenge: the exit assessment.", cue="exit", pause=0.3),
        B("It's not a test you can fail.", cue="fail", pause=0.2),
        B("It's like the stats screen at the end of a video game level.", cue="stats", pause=0.2),
        B("It shows what you've unlocked so far: files, tests, events and functions.", cue="unlocked", pause=0.3),
        B("It's pencil and paper only, with no computer.", cue="paper", pause=0.2),
        B("Stuck? Skip that question and come back.", cue="stuck", pause=0.4),
        B("Then comes the gallery walk.", cue="gallery", pause=0.2),
        B("Visit every station and play each project for two or three minutes.", cue="visit", pause=0.2),
        B("Then leave a feedback card: two stars and a wish.", cue="card", pause=0.2),
        B("That's two specific things that are good, and one kind idea.", cue="specific", pause=0.3),
        B("‘The score text is big and clear’ helps more than ‘cool.’", cue="helps", pause=0.4),
        B("Makers don't explain or defend during the walk.", cue="makers", pause=0.2),
        B("They just watch people play.", cue="watch", pause=0.3),
        B("Pause and think: why is watching quietly so useful?", cue="pause", pause=3.0),
        B("It's great playtest data!", cue="data", pause=0.6),
    ), actions=(
        A("chip", "Exit assessment = your stats screen", at="exit@0.5", until="gallery", x=960, y=180, color="yellow",
          size=44),
        A("chip", "not pass or fail", at="fail", until="gallery", x=960, y=290, color="white", size=38),
        A("icons", at="unlocked", until="gallery", x=960, y=470, gap=300,
          items=[("file", "Files", "unlocked@0.45"), ("check", "Tests", "unlocked@0.6"),
                 ("key", "Events", "unlocked@0.75"), ("gear", "Functions", "unlocked@0.9")]),
        A("icons", at="paper", until="gallery", x=700, y=780, gap=520,
          items=[("book", "pencil + paper", "paper"), ("laptop", "no computer", "paper@0.5")], crossed=[1]),
        A("chip", "Stuck? Skip it and come back", at="stuck", until="gallery", x=1500, y=780, color="sky", size=36),
        # gallery walk
        A("grid", at="gallery", x=120, y=260, cell=120, rows=["G.G.G", ".....", "G.G.G"],
          marks=[("visit@0.1", 0, 0, "1"), ("visit@0.1", 0, 2, "2"), ("visit@0.1", 0, 4, "3"),
                 ("visit@0.1", 2, 0, "4"), ("visit@0.1", 2, 2, "5"), ("visit@0.1", 2, 4, "6")],
          walker=[("visit", 0, 1), ("visit@0.3", 2, 1), ("visit@0.6", 4, 1), ("card", 4, 1), ("specific", 2, 1),
                  ("helps", 0, 1), ("watch", 2, 1), ("data", 4, 1)]),
        A("chip", "2–3 minutes at every station", at="visit@0.4", until="card", x=1320, y=300, color="white",
          size=38),
        A("panel", "Feedback card", at="card", until="makers", x=820, y=230, w=1000, size=36,
          items=[("card@0.5", "Star: something specific"), ("card@0.7", "Star: something specific"),
                 ("card@0.9", "Wish: one kind idea")]),
        A("chip", "Two stars and a wish", at="card@0.6", until="makers", x=520, y=760, color="yellow", size=44),
        A("chip", "“The score text is big and clear”", at="helps", until="makers", x=1220, y=640, color="green",
          size=36),
        A("badge", ok=True, at="helps@0.4", until="makers", x=1660, y=640),
        A("chip", "“cool”", at="helps@0.6", until="makers", x=1220, y=760, color="white", size=36),
        A("nova", x=1100, y=1000, s=0.65, at="makers", moods={"makers": "happy", "pause": "thinking",
                                                            "data": "proud"}),
        A("icons", at="watch", x=1500, y=760, items=[("book", "a small notebook", "watch")]),
        A("chip", "Makers watch quietly", at="makers@0.4", x=1320, y=300, color="purple", size=44),
        A("thought", "Why?", at="pause+0.3", until="pause>", x=1500, y=480),
        A("chip", "great playtest data!", at="data", x=1500, y=480, color="green", size=42),
    )),
    Scene("l2-w12-s05", setting="workshop", tail=0.8, beats=(
        B("Level 2 complete!", cue="complete", pause=0.3),
        B("You saved data in files, proved your code with tests, built games with keys and timers, and turned a plan "
          "into a real project.", cue="recap", pause=0.4),
        B("Before guests play, do the safety check.", cue="safety", pause=0.2),
        B("Open your high-score file and look: nicknames only.", cue="open", pause=0.3),
        B("No real names, schools, addresses, ages or photos, in the code, the window or the title.", cue="noreal",
          pause=0.3),
        B("Photos? Film the screen, not faces, and ask first.", cue="photos", pause=0.3),
        B("Nothing is uploaded or posted without a parent deciding with you.", cue="upload", pause=0.4),
        B("Your turn: freeze your code, fill in your pitch card, and practice once with your partner.", cue="turn",
          pause=0.3),
        B("Later, write your reflection.", cue="later", pause=0.2),
        B("Level 3, here you come!", cue="level3", pause=0.8),
    ), actions=(
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "recap"), ("level3", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("confetti", at="complete", x=1100, y=500),
        A("chip", "Level 2 complete!", at="complete", until="recap", x=1150, y=460, color="orange", size=50),
        A("icons", at="recap", until="safety", x=1250, y=470, gap=280,
          items=[("file", "files", "recap@0.15"), ("check", "tests", "recap@0.35"),
                 ("key", "keys + timers", "recap@0.6"), ("trophy", "a real project", "recap@0.85")]),
        A("file", "highscore.txt", at="open", until="photos", x=700, y=420, w=480, h=330,
          lines=["Comet,120", "Star,95", "Pixel,80"]),
        A("chip", "Nicknames only • Check highscore.txt", at="open@0.5", until="photos", x=1100, y=860,
          color="green", size=40),
        A("icons", at="noreal", until="photos", x=1560, y=480, gap=220, crossed=[0, 1, 2],
          items=[("person", "real names", "noreal@0.1"), ("house", "addresses", "noreal@0.4"),
                 ("camera", "photos", "noreal@0.7")]),
        A("icons", at="photos", until="turn", x=1250, y=460, gap=320,
          items=[("laptop", "film the screen", "photos"), ("person", "ask first", "photos@0.6"),
                 ("grownup", "a parent decides", "upload")]),
        A("chip", "Film the screen, not faces", at="photos@0.3", until="turn", x=1250, y=720, color="sky", size=42),
        A("chip", "Nothing posted without a parent", at="upload@0.3", until="turn", x=1250, y=850, color="orange",
          size=42),
        A("banner", "NEXT: Pitch card + practice", at="turn", color="green"),
        A("cards", at="turn", x=620, y=230, w=860, gap=105,
          items=["Freeze your code (backup!)", "Fill in your pitch card", "Practice once with your partner",
                 "Later: write your reflection"],
          reveal=["turn@0.2", "turn@0.5", "turn@0.8", "later"]),
        A("door", "LEVEL 3", at="turn", x=1700, y=920, open="level3"),
        A("confetti", at="level3+0.4", x=1700, y=500),
    )),
))
