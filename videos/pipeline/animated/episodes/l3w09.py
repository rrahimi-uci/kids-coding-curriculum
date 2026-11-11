"""Level 3 Week 9: How Do Machines Learn? (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

# Dragon-egg cards: (spots, size, label letter, color). F = fire, I = ice (a letter, never color alone).
EGGS = [(8, 2, "F fire", "orange"), (9, 4, "F fire", "orange"), (2, 8, "I ice", "sky"), (3, 7, "I ice", "sky")]

RULE = '''teeth = 7
if teeth > 5:
    print("grumpy")'''

# s04: biased training data (one lonely fire egg), test eggs and the fixed data
LONELY = [(10, 0, "F", "orange"), (2, 8, "I", "sky"), (3, 7, "I", "sky"), (2, 9, "I", "sky"), (4, 6, "I", "sky"),
          (3, 9, "I", "sky"), (5, 5, "I", "sky")]
TEST_EGGS = [(7, 3, "?", "white"), (6, 2, "?", "white"), (2, 7, "?", "white"), (3, 8, "?", "white")]
MORE_FIRE = [(8, 2, "F", "orange"), (9, 4, "F", "orange"), (7, 1, "F", "orange")]


def chart_xy(fx, fy, x, y, w, h, span=10):
    """Screen position of a feature point on a scatter at (x, y, w, h) (same formula as the kit)."""
    return x + 60 + (w - 100) * fx / span, y + h - 60 - (h - 100) * fy / span


# s03 chart geometry
S3 = dict(x=120, y=170, w=1000, h=780)
Q3 = chart_xy(7, 3, **S3)
C3 = chart_xy(3, 3, **S3)
I3 = chart_xy(3, 7, **S3)
# s04 chart geometry
S4 = dict(x=90, y=180, w=960, h=780)
Q4 = chart_xy(7, 3, **S4)
C4 = chart_xy(10, 3, **S4)
L4 = chart_xy(10, 0, **S4)

EPISODE = Episode(level=3, week=9, scenes=(
    # ------------------------------------------------------------------ s01 hook
    Scene("l3-w09-s01", setting="workshop", lead_in=0.2, beats=(
        B("Pixel has a new job: sorting dragon eggs into fire eggs and ice eggs.", cue="job", pause=0.3),
        B("But nobody wrote any rules!", cue="rules", pause=0.3),
        B("‘Just learn from these examples,’", speaker=NOVA, cue="learn", pause=0.1),
        B("says Nova, and sets down a basket of labeled eggs.", cue="basket", pause=0.3),
        B("‘Learn?’", speaker=PIXEL, cue="learnq", pause=0.1),
        B("beeps Pixel.", cue="beeps", pause=0.1),
        B("‘I only follow instructions!’", speaker=PIXEL, cue="only", pause=0.4),
        B("Can a program really learn from examples?", cue="can", pause=1.6),
        B("And what if the examples are wrong?", cue="wrong", pause=3.0),
    ), actions=(
        A("door", "DOOR 9", x=1700, y=900),
        A("nova", x=300, y=960, enter="left", point="basket", moods={"rules": "surprised", "can": "thinking"},
          chin=("wrong", "end")),
        A("pixel", x=600, y=760, drop=True, moods={"rules": "confused", "learnq": "surprised", "can": "confused"}),
        A("banner", "MISSION: Learn from examples", at="job"),
        A("chip", "FIRE (F)", at="job@0.5", until="can", x=900, y=260, color="orange", size=44),
        A("chip", "ICE (I)", at="job@0.75", until="can", x=1250, y=260, color="sky", size=44),
        A("file", "rulebook.txt", at="rules", until="basket", x=860, y=360, w=520, h=300,
          lines=["", "  (no rules yet!)"]),
        A("listrow", "basket of labeled eggs", x=1120, y=520, cell=130, at="basket", until="wrong",
          items=["F", "I", "F", "I", "I", "F"], indexes=False),
        A("chip", "examples + labels", at="basket@0.6", until="wrong", x=1080, y=680, color="white", size=36),
        A("chip", "Pause: Can a program learn?", at="can", x=1080, y=250, color="yellow"),
        A("chip", "What if the examples are wrong?", at="wrong", x=1080, y=560, color="red", size=40),
        A("thought", "?", at="wrong$+0.2", until="end", x=840, y=380),
    )),
    # ------------------------------------------------------------------ s02 rules vs learning
    Scene("l3-w09-s02", setting="sky", beats=(
        B("So far, your programs follow rules you typed: if teeth is more than five, say grumpy.", cue="rules",
          pause=0.4),
        B("A learning program is different.", cue="different", pause=0.3),
        B("It gets examples with the right answers, called labels, and finds the pattern itself.", cue="labels",
          pause=0.3),
        B("The things it measures are called features.", cue="features", pause=0.3),
        B("Our dragon eggs have two features: spots and size, each from zero to ten.", cue="two", pause=0.4),
        B("Put every example on a chart.", cue="chart", pause=0.3),
        B("To guess a mystery egg, find the closest example and copy its label.", cue="guess", pause=0.3),
        B("That's a nearest-neighbor classifier.", cue="nn", pause=0.4),
        B("To check it, we hide some examples in a test pile, train on the rest, and count the right guesses: its "
          "accuracy.", cue="check", pause=0.4),
        B("Testing on examples it learned from would be like seeing the exam answers first!", cue="exam", pause=0.6),
    ), actions=(
        A("chip", "Rules", at="rules", until="chart", x=480, y=200, color="navy", size=40),
        A("code", code=RULE, title="rules.py", x=110, y=260, w=740, h=430, size=36, at="rules", until="chart",
          run="rules@0.7", line_delay=0.6, expect=["grumpy"], shell_h=130),
        A("chip", "Learning", at="different", until="chart", x=1380, y=200, color="green", size=40),
        A("table", x=1020, y=260, col_w=240, at="labels", until="chart", header=["spots", "size", "label"],
          rows=[["8", "2", "FIRE"], ["9", "4", "FIRE"], ["2", "8", "ICE"], ["3", "7", "ICE"]],
          reveal=["labels", "labels@0.2", "labels@0.4", "labels@0.6"]),
        A("chip", "Label = the right answer", at="labels@0.5", until="chart", x=1380, y=680, color="yellow",
          size=40),
        A("chip", "Features = what we measure", at="features", until="chart", x=1380, y=800, color="sky", size=40),
        A("chip", "spots • size: 0 to 10", at="two@0.5", until="chart", x=1380, y=920, color="white", size=38),
        A("scatter", x=110, y=170, w=920, h=800, at="chart", axes=("spots", "size"), points=EGGS,
          query=("guess", 4, 6), nearest=("guess@0.6", 3)),
        A("chip", "mystery egg", at="guess", until="check", x=640, y=470, color="white", size=30),
        A("chip", "→ copy: ICE", at="guess$", until="check", x=1400, y=300, color="sky", size=40),
        A("chip", "Nearest neighbor: copy the closest label", at="nn", until="check", x=1450, y=420,
          color="green", size=34),
        A("listrow", "Training pile", x=1440, y=420, cell=110, at="check", items=["F", "I", "F", "I", "F", "I"],
          indexes=False),
        A("listrow", "Test pile", x=1440, y=700, cell=110, at="check@0.3", items=["?", "?"], indexes=False),
        A("chip", "accuracy = right guesses", at="check@0.8", x=1440, y=830, color="white", size=34),
        A("chip", "Train on one pile, test on another", at="check@0.4", x=1440, y=200, color="orange", size=36),
        A("chip", "No peeking at the answers!", at="exam", x=1440, y=950, color="yellow", size=36),
    )),
    # ------------------------------------------------------------------ s03 steps distance and Markov chain
    Scene("l3-w09-s03", setting="lavender", beats=(
        B("Here's a mystery egg: seven spots, size three.", cue="mystery", pause=0.3),
        B("Which example is closest?", cue="which", pause=1.6),
        B("Pretend each egg is a game piece on the grid from week seven.", cue="piece", pause=0.2),
        B("It can only step across or up and down, never on a slant.", cue="step", pause=0.3),
        B("So the steps distance is the gap in spots plus the gap in size.", cue="steps", pause=0.3),
        B("A gap is the bigger number minus the smaller one.", cue="gap", pause=0.3),
        B("To the fire egg with eight spots, size two, the gaps are one and one: two steps.", cue="fire", pause=0.4),
        B("To the ice egg with three spots, size seven, the gaps are four and four: eight steps.", cue="ice", pause=0.4),
        B("The fire egg is closer, so the guess is fire!", cue="closer", pause=0.6),
        B("Machines can learn words, too.", cue="words", pause=0.3),
        B("A Markov chain learns one thing: after each word, which words came next?", cue="markov", pause=0.3),
        B("From ‘my dog ran, my dog hid,’ it learns that after dog came ran or hid.", cue="from", pause=0.4),
        B("Then it writes by picking a random next word, again and again.", cue="writes", pause=0.3),
        B("It sounds right, but understands nothing.", cue="sounds", pause=0.6),
    ), actions=(
        A("scatter", **S3, at="mystery", until="words", axes=("spots", "size"), points=EGGS,
          query=("mystery@0.4", 7, 3), nearest=("fire@0.3", 0)),
        A("chip", "? (7, 3)", at="mystery@0.5", until="words", x=Q3[0] - 120, y=Q3[1] - 40, color="white", size=30),
        A("thought", "Which one?", at="which$", until="which>", x=1500, y=420),
        A("chip", "across ↔ or up and down ↕ (no slants)", at="step", until="words", x=1520, y=180, color="white",
          size=30),
        A("chip", "Steps distance = gap + gap", at="steps", until="words", x=1520, y=300, color="orange", size=40),
        A("chip", "gap = bigger − smaller", at="gap", until="words", x=1520, y=410, color="white", size=36),
        A("chip", "(7, 3) → (8, 2): 1 + 1 = 2 steps", at="fire@0.5", until="words", x=1520, y=530, color="green",
          size=34),
        A("arrow", x1=Q3[0], y1=Q3[1], x2=C3[0], y2=C3[1], color="#6B4FC2", at="ice@0.3", until="words", width=8),
        A("arrow", x1=C3[0], y1=C3[1], x2=I3[0], y2=I3[1] + 22, color="#6B4FC2", at="ice@0.55", until="words",
          width=8),
        A("chip", "(7, 3) → (3, 7): 4 + 4 = 8 steps", at="ice@0.7", until="words", x=1520, y=650, color="purple",
          size=34),
        A("chip", "Guess: FIRE", at="closer", until="words", x=1520, y=790, color="orange", size=46),
        A("badge", ok=True, at="closer@0.4", until="words", x=1780, y=790),
        # Markov chain
        A("listrow", "training text", x=960, y=290, cell=170, at="markov", items=["my", "dog", "ran", "my", "dog", "hid"],
          indexes=False, highlight=[("from@0.6", "from$", 2), ("from@0.6", "from$", 5)]),
        A("dict", "after each word", x=200, y=480, w=720, at="from",
          states=[("from", [("my", "[dog]")]), ("from@0.3", [("my", "[dog]"), ("dog", "[ran]")]),
                  ("from@0.45", [("my", "[dog]"), ("dog", "[ran]"), ("ran", "[my]")]),
                  ("from@0.75", [("my", "[dog]"), ("dog", "[ran, hid]"), ("ran", "[my]")])],
          highlight=[("from@0.6", "writes", "dog")]),
        A("chip", "dog → [ran, hid]", at="from@0.75", x=1400, y=560, color="green", size=44),
        A("listrow", "a new sentence", x=960, y=930, cell=130, at="writes",
          states=[("writes", ["my"]), ("writes@0.2", ["my", "dog"]), ("writes@0.4", ["my", "dog", "ran"]),
                  ("writes@0.6", ["my", "dog", "ran", "my"]), ("writes@0.8", ["my", "dog", "ran", "my", "dog"]),
                  ("writes$", ["my", "dog", "ran", "my", "dog", "hid"])], indexes=False),
        A("chip", "Sounds right ≠ understands", at="sounds", x=1400, y=700, color="yellow", size=40),
    )),
    # ------------------------------------------------------------------ s04 bug hunt: biased data
    Scene("l3-w09-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Someone collected new training eggs but met only one fire egg, a very unusual one at ten spots, size zero, "
          "plus lots of ice eggs.", cue="collected", pause=0.3),
        B("Pixel tests it on four eggs it has never seen, and every fire egg gets labeled ice!", cue="tests",
          pause=0.4),
        B("Is the bug in the code, or in the data?", cue="isbug", pause=1.6),
        B("Let's use our steps.", cue="steps", pause=0.2),
        B("Read: there's no red error at all.", cue="read", pause=0.3),
        B("Predict.", cue="predict", pause=3.6),
        B("‘The code runs fine. I think the examples are the problem,’", speaker=NOVA, cue="nova", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("Watch one guess on the chart.", cue="watch", pause=0.2),
        B("A real fire egg is six steps from that lonely fire example, but only four steps from an ice egg, so it "
          "copies ice.", cue="six", pause=0.4),
        B("That's bias: unbalanced examples make unfair guesses.", cue="bias", pause=0.3),
        B("When a learning program is wrong, check the examples before the code.", cue="checkdata", pause=0.4),
        B("Fix one thing: add more fire examples.", cue="fix", pause=0.4),
        B("Check: test again, and the fire eggs are labeled fire.", cue="again", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("scatter", **S4, at="collected", until="tests", axes=("spots", "size"), points=LONELY),
        A("scatter", **S4, at="tests", until="fix", axes=("spots", "size"), points=LONELY + TEST_EGGS,
          query=("watch", 7, 3), nearest=("six@0.45", 6)),
        A("chip", "lonely fire egg (10, 0)", at="collected@0.5", until="tests", x=780, y=820, color="orange",
          size=32),
        A("tests", "test eggs (never seen)", at="tests", until="steps", x=1110, y=240, w=740,
          items=[("tests@0.3", "fire (7, 3) → ice", False), ("tests@0.45", "fire (6, 2) → ice", False),
                 ("tests@0.6", "ice (2, 7) → ice", True), ("tests@0.75", "ice (3, 8) → ice", True)]),
        A("chip", "Is the bug in the code or the data?", at="isbug", until="steps", x=1480, y=700, color="yellow",
          size=38),
        A("cards", at="steps", until="again", x=1150, y=240, w=660, gap=86, size=34,
          items=["Read", "Predict", "Watch", "Fix ONE thing", "Check"],
          reveal=["steps", "steps@0.2", "steps@0.4", "steps@0.6", "steps@0.8"],
          active=["read", ("predict", "watch"), ("watch", "fix"), "fix", ("again", "end")],
          done=["predict", "watch", "fix", "again", None]),
        A("chip", "no red error", at="read@0.5", until="predict$", x=1480, y=780, color="white", size=36),
        A("thought", "Code or data?", at="predict$+0.2", until="predict>", x=1480, y=820),
        A("arrow", x1=Q4[0], y1=Q4[1], x2=C4[0], y2=C4[1], color="#C77700", at="six@0.15", until="fix", width=8),
        A("arrow", x1=C4[0], y1=C4[1], x2=L4[0], y2=L4[1] - 22, color="#C77700", at="six@0.25", until="fix",
          width=8),
        A("chip", "6 steps vs 4 steps → copies ice", at="six@0.6", until="fix", x=1480, y=760, color="red",
          size=34),
        A("chip", "Bias: unbalanced examples, unfair guesses", at="bias", until="fix", x=1460, y=860,
          color="orange", size=30),
        A("chip", "Check the examples before the code", at="checkdata", until="fix", x=1480, y=960,
          color="yellow", size=34),
        A("scatter", **S4, at="fix", axes=("spots", "size"), points=LONELY + MORE_FIRE + TEST_EGGS),
        A("chip", "+ 3 fire examples", at="fix@0.5", x=820, y=420, color="orange", size=32),
        A("tests", "test again", at="again", x=1110, y=240, w=740,
          items=[("again@0.3", "fire (7, 3) → fire", True), ("again@0.4", "fire (6, 2) → fire", True),
                 ("again@0.5", "ice (2, 7) → ice", True), ("again@0.6", "ice (3, 8) → ice", True)]),
        A("badge", ok=False, at="tests@0.5", until="fix", x=1830, y=150, r=40),
        A("badge", ok=True, at="again$", x=1480, y=760),
        A("confetti", at="again$", x=1480, y=600),
        A("nova", x=1720, y=1060, s=0.5, at="again", moods={"again": "happy", "again$": "proud"}),
    )),
    # ------------------------------------------------------------------ s05 recap, AI ethics, project kickoff
    Scene("l3-w09-s05", setting="workshop", tail=0.8, beats=(
        B("Door nine unlocked!", cue="door", pause=0.4),
        B("A learning program finds patterns in labeled examples.", cue="finds", pause=0.3),
        B("Features are what it measures, the steps distance finds the nearest example, and a test pile checks its "
          "accuracy.", cue="features", pause=0.3),
        B("But AI copies the mistakes in its examples.", cue="copies", pause=0.4),
        B("AI can be wrong, even when it sounds sure: check important facts with a trusted source or adult.",
          cue="wrongai", pause=0.3),
        B("Never type your real name, address, school, passwords, photos or secrets into a chatbot; what you type may "
          "be stored.", cue="never", pause=0.3),
        B("Deepfakes are fake pictures, voices or videos:", cue="deepfakes", pause=0.1),
        B("ask, ‘Who made this, and why?’", cue="ask", pause=0.2),
        B("and never make fakes of real people.", cue="nofakes", pause=0.3),
        B("AI is only as fair as its examples.", cue="fair", pause=0.5),
        B("Now open Exercise 9.1, the Monster sorter, and type along with your teacher.", cue="next", pause=0.3),
        B("Then start your Build Something Big pitch card!", cue="pitch", pause=0.6),
    ), actions=(
        A("door", "DOOR 9", x=1700, y=920, open="door"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "finds"), ("pitch", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("cards", at="finds", until="wrongai", x=700, y=230, w=820, gap=110, size=36,
          items=["Patterns from labeled examples", "Features = what it measures", "Steps distance → nearest",
                 "Test pile → accuracy"],
          reveal=["finds", "features", "features@0.4", "features@0.75"]),
        A("chip", "AI copies the mistakes in its examples", at="copies", until="wrongai", x=1110, y=760,
          color="red", size=38),
        A("icons", at="wrongai", until="next", x=1110, y=380, gap=230,
          items=[("warning", "Can be wrong", "wrongai+0.4"), ("lock", "Keep it private", "never"),
                 ("camera", "Spot deepfakes", "deepfakes"), ("magnifier", "Check for bias", "fair")]),
        A("chip", "Check with a trusted source or adult", at="wrongai@0.5", until="never", x=1110, y=640,
          color="white", size=36),
        A("chip", "No real name, address, school, passwords, photos", at="never@0.3", until="deepfakes", x=1110,
          y=640, color="white", size=32),
        A("chip", "Who made this, and why?", at="ask", until="fair", x=1110, y=640, color="yellow", size=40),
        A("chip", "Wrong • Private • Fake • Unfair: be AI-wise", at="fair", until="next", x=1100, y=760,
          color="orange", size=36),
        A("banner", "NEXT: 9.1 Monster sorter, then M1 Pitch", at="next", color="green"),
        A("cards", at="next", x=700, y=230, w=800, gap=110,
          items=["Open 9.1 Monster sorter", "Type along with your teacher", "Start your pitch card (M1)"],
          reveal=["next@0.1", "next@0.5", "pitch"]),
        A("chip", "PROJECT: Build Something Big", at="pitch", x=1100, y=620, color="purple", size=40),
        A("roadmap", x=760, y=760, w=760, at="pitch", items=["M1 Pitch", "M2", "M3", "M4", "Showcase"],
          current=[("pitch", 0)]),
    )),
))
