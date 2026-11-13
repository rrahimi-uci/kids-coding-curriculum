"""Junior Level 2 Week 8: Start, Win and Lose (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/2-game-makers/teaching-material/lessons/week08.tex: the board-game rules warm-up
(tic-tac-toe sorted on START / PLAY / WIN / LOSE cards, a game that never ends and one that ends right
away), the three parts of a game, the referee analogy and "stop all" as the final whistle, the worked
example Exercise 8.1 Win and Lose (misses counted on the Apple; the Bowl's referee script: set score and
misses to 0, say the goal, forever: if misses = 3 Game over, stop all; if score = 10 You win, stop all),
testing both endings with the freeze-ball wiggle, the bug hunt Exercise 8.2 Never or Right Away? (Leo's
"misses = 0", Zoe's "if score = 10" above the forever), and the no-tricks talk: good games end.
Level 2 conventions: the hidden Star marker for the falling apple; misses count up (never negative).
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

BIG = 1.25  # block scale: big enough for young eyes
SPRITE = 1.0  # sprite size on the stage

FLAG = ("event", "when {flag} clicked")
SET_SCORE = ("variables", "set [score] to [0]")
SET_MISSES = ("variables", "set [misses] to [0]")
GOAL = ("looks", "say [Catch 10 apples!] for [2] seconds")
STOP = ("control", "stop [all]")
GAME_OVER = ("looks", "say [Game over!] for [2] seconds")
YOU_WIN = ("looks", "say [You win!] for [2] seconds")
LOSE = ("control", "if <misses = 3> then", [GAME_OVER, STOP])
WIN = ("control", "if <score = 10> then", [YOU_WIN, STOP])
EDGE = ("control", "if <touching [edge] ?> then", [("variables", "change [misses] by [1]"),
                                                   ("motion", "go to [Star]")])

# On the stages below the apple is the moving sprite and the Bowl sits at the bottom (stage coordinates).
TOP = 140  # where the hidden Star marker is
BOWL = ("bowl", 0, -130)


def catches(first: str, count: int, every: float = 0.55, base: float = 0.0) -> list:
    """The apple falls into the bowl `count` times, going back to the Star after each catch."""
    acts = []
    for i in range(count):
        acts += [(f"{first}+{base + i * every:.2f}", "goto", 0, TOP, 0.05),
                 (f"{first}+{base + i * every + 0.05:.2f}", "goto", 0, -95, every - 0.1)]
    return acts


def misses(first: str, count: int, every: float = 0.9) -> list:
    """The apple falls past the bowl to the bottom edge `count` times."""
    acts = []
    for i in range(count):
        acts += [(f"{first}+{i * every:.2f}", "goto", 150, TOP, 0.05),
                 (f"{first}+{i * every + 0.05:.2f}", "goto", 150, -150, every - 0.15)]
    return acts


def counting(first: str, count: int, every: float, delay: float) -> list:
    """Monitor values 1..count, each when that fall lands."""
    return [(f"{first}+{i * every + delay:.2f}", i + 1) for i in range(count)]


EPISODE = Episode(level="j2", week=8, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j2-w08-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi", pause=0.3),
        B("Beep boop! Let's play!", speaker=PIXI, cue="hello", pause=0.5),
        B("Our catch game is fun. But it goes on, and on, and on.", speaker=NARRATOR, cue="onandon", pause=0.5),
        B("Real games have an ending. You win, or it is game over!", speaker=NARRATOR, cue="real", pause=0.5),
        B("Today, we give our catch game a start, a goal and an ending.", speaker=NARRATOR, cue="mission",
          pause=0.5),
        B("Ready? Let's go!", speaker=NARRATOR, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("ready", "end")],
          moods={"start": "happy", "onandon": "confused", "real": "happy", "mission": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("stage", x=1000, y=200, w=760, h=500, at="onandon", flag=False, sprite="apple", sprite_scale=SPRITE,
          extra=[BOWL], sprite_y=TOP, actions=catches("onandon", 9, 0.7)),
        A("chip", "on and on and on...", at="onandon@0.5", until="mission", x=1380, y=820, color="yellow",
          size=44),
        A("banner", "MISSION: Give my game an ending", at="mission"),
        A("chip", "start • goal • ending", at="mission@0.4", x=1380, y=820, color="green", size=46),
    )),
    # 2. board-game rules ------------------------------------------------------------------------------
    Scene("j2-w08-s02", setting="lavender", beats=(
        B("Let's warm up with a game everyone knows: tic-tac-toe.", speaker=NARRATOR, cue="warm", pause=0.4),
        B("Every game has rules. Let's sort them on four cards.", speaker=NARRATOR, cue="rules", pause=0.5),
        B("Start: the grid is empty, and X goes first.", speaker=NARRATOR, cue="startcard", pause=0.6),
        B("Play: we take turns.", speaker=NARRATOR, cue="play", pause=1.4),
        B("Win: three in a row!", speaker=NARRATOR, cue="win", pause=0.8),
        B("Lose: if nobody wins, the game ends when the grid is full.", speaker=NARRATOR, cue="lose", pause=0.8),
    ), actions=(
        A("grid", rows=["...", "...", "..."], x=200, y=300, cell=170, at="warm",
          marks=[("startcard@0.8", 0, 0, "X"), ("play@0.3", 0, 2, "O"), ("play@0.6", 1, 1, "X"),
                 ("play$+0.4", 2, 0, "O"), ("win@0.3", 2, 2, "X")]),
        A("arrow", x1=230, y1=330, x2=680, y2=780, at="win@0.5", until="lose", color="green"),
        A("cards", items=["START: empty grid, X first", "PLAY: take turns", "WIN: three in a row",
                          "LOSE: nobody wins, grid full"], x=1000, y=280, w=680, gap=130,
          reveal=["startcard", "play", "win", "lose"], at="rules", color="purple",
          active=[("startcard", "play"), ("play", "win"), ("win", "lose"), ("lose", "end")]),
    )),
    # 3. never ends, ends right away ---------------------------------------------------------------
    Scene("j2-w08-s03", setting="workshop", beats=(
        B("Now a game with no ending. We pass a ball around, and around, and around.", speaker=NARRATOR,
          cue="ball", pause=0.5),
        B("How do you win?", speaker=NARRATOR, cue="how", pause=2.8),
        B("You can't! There is no way to win, and it never stops. That is not really a game.", speaker=NARRATOR,
          cue="cant", pause=0.6),
        B("Next game. The rule is: if you are wearing socks, you lose!", speaker=NARRATOR, cue="socks", pause=0.5),
        B("Oh no! I lose before the game even starts!", speaker=PIXI, cue="pixi", pause=0.5),
        B("That ending came too soon.", speaker=NARRATOR, cue="soon", pause=0.4),
        B("A game that never ends, and a game that ends right away: those are today's bugs!", speaker=NARRATOR,
          cue="bugs", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=980, s=0.8, moods={"how": "thinking", "cant": "happy", "pixi": "surprised",
                                                "bugs": "happy"}, chin=("how", "cant")),
        A("pixi", x=560, y=780, s=0.7, ground=960, moods={"pixi": "surprised"},
          path=[("ball", 560, 780), ("ball+1.0", 700, 780), ("ball+2.0", 560, 780), ("ball+3.0", 700, 780),
                ("ball+4.0", 560, 780)]),
        A("thought", "How do you win?", at="how$+0.2", until="cant", x=1300, y=400),
        A("chip", "No way to win. It never ends!", at="cant", until="socks", x=1300, y=400, color="red", size=44),
        A("chip", "Socks? You lose!", at="socks@0.6", until="bugs", x=1300, y=400, color="orange", size=46),
        A("chip", "Ends too soon!", at="soon", until="bugs", x=1300, y=540, color="red", size=46),
        A("cards", items=["never ends", "ends right away"], x=1040, y=360, w=520, gap=140, at="bugs",
          reveal=["bugs@0.2", "bugs@0.5"], color="red"),
        A("chip", "today's bugs!", at="bugs@0.7", x=1300, y=700, color="yellow", size=46),
    )),
    # 4. three parts and the referee ----------------------------------------------------------------
    Scene("j2-w08-s04", setting="sky", beats=(
        B("Real games have three parts.", speaker=NARRATOR, cue="three", pause=0.4),
        B("A start: everything is set to zero, and the player learns the goal.", speaker=NARRATOR, cue="part1",
          pause=0.5),
        B("The play: a forever loop keeps things moving.", speaker=NARRATOR, cue="part2", pause=0.5),
        B("And an ending: you win, or it is game over.", speaker=NARRATOR, cue="part3", pause=0.6),
        B("In soccer, a referee watches the whole game, and keeps checking: is it over yet?", speaker=NARRATOR,
          cue="referee", pause=0.5),
        B("When it is, the whistle blows, and everybody stops.", speaker=NARRATOR, cue="whistle", pause=0.5),
        B("In Scratch, the whistle is the block stop all, from orange Control.", speaker=NARRATOR, cue="stopall",
          pause=0.6),
        B("Today, the Bowl gets a referee script!", speaker=NARRATOR, cue="bowl", pause=0.8),
    ), actions=(
        A("cards", items=["START: set to 0, say the goal", "PLAY: forever", "ENDING: win or game over"],
          x=160, y=300, w=760, gap=140, reveal=["part1", "part2", "part3"], at="part1", color="green"),
        A("chip", "Is it over yet?", at="referee@0.6", until="bowl", x=1400, y=320, color="yellow", size=46),
        A("icons", at="referee", until="stopall", x=1400, y=560, gap=260,
          items=[("person", "Referee", "referee@0.2")]),
        A("scratch", blocks=[STOP], x=1150, y=520, w=560, h=150, panel=False, scale=BIG, at="stopall",
          highlight=[(0, "stopall@0.5", "bowl")]),
        A("chip", "stop all = the final whistle", at="stopall@0.5", x=1400, y=720, color="orange", size=42),
        A("stage", x=1190, y=800, w=420, h=200, at="bowl", flag=False, sprite="bowl", sprite_y=-30,
          sprite_scale=0.8),
    )),
    # 5. counting misses on the Apple ----------------------------------------------------------------
    Scene("j2-w08-s05", setting="mint", beats=(
        B("To lose, we count misses.", speaker=NARRATOR, cue="misses", pause=0.4),
        B("Click orange-red Variables, then Make a Variable. Type misses, and click OK.", speaker=NARRATOR,
          cue="variable", pause=0.6),
        B("Every apple that falls past the bowl is one miss.", speaker=NARRATOR, cue="past", pause=0.5),
        B("Click the Apple. Inside its if touching edge, snap change misses by one, above go to Star.",
          speaker=NARRATOR, cue="apple", pause=0.8),
        B("The apple goes back to the hidden Star marker at the top, and falls again.", speaker=NARRATOR,
          cue="star", pause=0.6),
        B("Watch the misses count up: one, two, three!", speaker=NARRATOR, cue="count", pause=1.2),
    ), actions=(
        A("chip", "Variables: orange-red", at="variable", until="apple", x=560, y=330, color="orange", size=44),
        A("chip", "Make a Variable: misses", at="variable@0.5", until="apple", x=560, y=450, color="white",
          size=42),
        A("scratch", "Apple", blocks=[EDGE], x=130, y=260, w=860, h=440, scale=BIG, at="apple",
          reveal=["apple", "apple@0.5", "apple@0.85"], highlight=[(1, "apple@0.5", "star")]),
        A("chip", "one miss", at="past", until="apple", x=560, y=570, color="red", size=44),
        A("stage", x=1100, y=230, w=700, h=480, at="misses", flag=False, sprite="apple", sprite_scale=SPRITE,
          sprite_x=150, sprite_y=TOP, extra=[BOWL, ("star", 150, TOP + 10)],
          monitors=[("misses", [("misses", 0), ("past+1.2", 1), ("count+0.2", 1)] +
                     counting("count", 3, 1.0, 0.85))],
          actions=misses("past", 1, 1.3) + [("star", "goto", 150, TOP, 0.4)] + misses("count", 3, 1.0)),
        A("chip", "hidden Star marker", at="star", until="count", x=1450, y=820, color="yellow", size=44),
        A("chip", "misses count up", at="count", x=1450, y=820, color="orange", size=46),
    )),
    # 6. the referee: the start ------------------------------------------------------------------------
    Scene("j2-w08-s06", setting="mint", beats=(
        B("Now click the Bowl. From yellow Events, drag in a new when green flag clicked. This is the "
          "referee script.", speaker=NARRATOR, cue="bowl", pause=0.6),
        B("First, the start. From Variables, snap set score to zero, and set misses to zero.", speaker=NARRATOR,
          cue="zero", pause=0.6),
        B("Then purple Looks: say Catch ten apples, for two seconds. Now the player knows the goal!",
          speaker=NARRATOR, cue="goal", pause=0.6),
        B("Next, the play: an orange forever loop.", speaker=NARRATOR, cue="forever", pause=0.8),
    ), actions=(
        A("banner", "Exercise 8.1: Win and Lose", at="bowl", color="green"),
        A("scratch", "Bowl: the referee", blocks=[FLAG, SET_SCORE, SET_MISSES, GOAL, ("control", "forever", [])],
          x=130, y=260, w=860, h=720, scale=BIG,
          reveal=["bowl@0.5", "zero@0.55", "zero@0.85", "goal@0.3", "forever@0.5"]),
        A("stage", x=1100, y=230, w=700, h=480, at="bowl", flag_at="goal@0.6", sprite="bowl",
          sprite_y=-110, sprite_scale=SPRITE,
          monitors=[("score", [("bowl", 4), ("zero@0.7", 0)]), ("misses", [("bowl", 2), ("zero@0.95", 0)])],
          actions=[("goal@0.7", "say", "Catch 10 apples!", 2.4)]),
        A("chip", "Events: yellow", at="bowl", until="zero", x=1450, y=860, color="yellow", size=44),
        A("chip", "Variables: orange-red", at="zero", until="goal", x=1450, y=860, color="orange", size=44),
        A("chip", "Looks: purple", at="goal", until="forever", x=1450, y=860, color="purple", size=44),
        A("chip", "Control: orange", at="forever", x=1450, y=860, color="orange", size=44),
    )),
    # 7. the referee: the ending -----------------------------------------------------------------------
    Scene("j2-w08-s07", setting="lavender", beats=(
        B("Now the ending. Inside the forever, put an if then.", speaker=NARRATOR, cue="ifthen", pause=0.5),
        B("From green Operators, drop in an equals block. Drag the round misses into the left side, and type "
          "three on the right.", speaker=NARRATOR, cue="equals", pause=0.6),
        B("Inside the if: say Game over for two seconds, then stop all.", speaker=NARRATOR, cue="over", pause=0.6),
        B("Under it, a second if: score equals ten. Inside: say You win for two seconds, then stop all.",
          speaker=NARRATOR, cue="youwin", pause=0.6),
        B("The forever loop keeps checking, again and again, like a referee.", speaker=NARRATOR, cue="checking",
          pause=0.4),
        B("Is it over yet? Is it over yet?", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Bowl: the ending", blocks=[("control", "forever", [LOSE, WIN])], x=130, y=250, w=900,
          h=770, scale=1.0, reveal=["ifthen", "ifthen@0.5", "over", "over@0.6", "youwin@0.3", "youwin@0.6",
                                     "youwin@0.85"],
          highlight=[(1, "checking", "checking@0.5"), (4, "checking@0.5", "checking$"),
                     (1, "pixi", "pixi@0.5"), (4, "pixi@0.5", "pixi$")]),
        A("chip", "Operators: green", at="equals", until="over", x=1440, y=330, color="green", size=46),
        A("chip", "misses = 3", at="equals@0.5", until="over", x=1440, y=460, color="white", size=48),
        A("chip", "stop all = the final whistle", at="over@0.6", until="checking", x=1440, y=330,
          color="orange", size=40),
        A("chip", "score = 10", at="youwin@0.3", until="checking", x=1440, y=460, color="white", size=48),
        A("chip", "forever = keeps checking", at="checking", x=1440, y=330, color="yellow", size=42),
        A("pixi", x=1440, y=760, s=0.6, at="checking", ground=860),
    )),
    # 8. test both endings (freeze-ball) --------------------------------------------------------------
    Scene("j2-w08-s08", setting="peach", beats=(
        B("A good game maker tests every ending. Let's play to win!", speaker=NARRATOR, cue="test", pause=0.4),
        B("When you hear You win, jump and cheer!", speaker=NARRATOR, cue="jump", pause=6.6),
        B("Now click the flag again, and lose on purpose. When you hear Game over, freeze!", speaker=NARRATOR,
          cue="lose", pause=0.4),
        B("What will the Bowl say when misses gets to three?", speaker=NARRATOR, cue="predict", pause=3.6),
        B("Game over! Freeze! Both endings work.", speaker=NARRATOR, cue="both", pause=0.4),
        B("Beep! I'm frozen!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("stage", x=560, y=200, w=800, h=540, at="test", flag_at="jump$", sprite="apple", sprite_scale=SPRITE,
          sprite_y=TOP, extra=[BOWL],
          monitors=[("score", [("test", 0)] + counting("jump$", 10, 0.55, 0.75) + [("lose", 0)]),
                    ("misses", [("test", 0)] + counting("predict", 3, 1.0, 0.85))],
          actions=catches("jump$", 10, base=0.3) + [("lose", "goto", 0, TOP, 0.05)] + misses("predict", 3, 1.0)),
        A("bubble", "You win!", x=1060, y=560, at="jump$+5.9", until="lose", size=44),
        A("bubble", "Game over!", x=1060, y=560, at="predict+3.0", until="pixi$", size=44),
        A("thought", "What will it say?", at="predict$+0.2", until="predict+3.0", x=1620, y=420),
        A("aiden", x=200, y=1080, s=0.5, at="test", moods={"lose": "happy", "predict": "thinking", "both": "proud"},
          chin=("predict", "both"), wave=("jump$+6.0", "lose")),
        A("chip", "Jump and cheer!", at="jump$+6.0", until="lose", x=1660, y=860, color="green", size=44),
        A("chip", "Freeze!", at="both", x=1660, y=860, color="sky", size=48),
        A("pixi", x=1660, y=700, s=0.5, at="both", ground=780, moods={"both": "surprised"}),
        A("badge", ok=True, at="both@0.6", x=1290, y=260),
    )),
    # 9. bug hunt: Leo -----------------------------------------------------------------------------------
    Scene("j2-w08-s09", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=NARRATOR, cue="bug", pause=0.4),
        B("Leo's game ends right at the start. He clicks the flag, and it says Game over at once!",
          speaker=NARRATOR, cue="leo", pause=0.8),
        B("Look at his if. Which block is the clue?", speaker=NARRATOR, cue="clue", pause=3.0),
        B("Misses equals zero! Misses start at zero, so the referee blows the whistle right away.",
          speaker=NARRATOR, cue="zero", pause=0.6),
        B("The fix: three, not zero. Now the game waits for three misses.", speaker=NARRATOR, cue="fix", pause=3.0),
        B("It works!", speaker=NARRATOR, cue="works", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Never or Right Away?", at="bug", color="navy"),
        A("scratch", "Leo's game", blocks=[FLAG, SET_MISSES, ("control", "forever", [
            ("control", "if <misses = 0> then", [GAME_OVER, STOP])])],
          x=130, y=260, w=860, h=700, scale=1.1, at="leo", edits=[("fix@0.3", 3, "if <misses = 3> then")],
          highlight=[(3, "zero", "fix$")]),
        A("stage", x=1100, y=230, w=700, h=480, at="leo", flag_at="leo@0.45", sprite="apple",
          sprite_scale=SPRITE, sprite_y=TOP, extra=[BOWL],
          monitors=[("misses", [("leo", 0)])],
          actions=[("fix$+0.2", "goto", 0, -95, 0.8), ("fix$+1.1", "goto", 0, TOP, 0.05),
                   ("fix$+1.2", "goto", 0, -95, 0.8)]),
        A("bubble", "Game over!", x=1560, y=560, at="leo@0.55", until="clue", size=40),
        A("badge", ok=False, at="leo@0.75", until="fix", x=1760, y=290),
        A("thought", "Which block?", at="clue$+0.2", until="zero", x=1450, y=860),
        A("chip", "misses start at 0", at="zero", until="fix", x=1450, y=820, color="red", size=44),
        A("chip", "3, not 0", at="fix", x=1450, y=820, color="green", size=48),
        A("sfx", "snap", at="fix@0.3"),
        A("badge", ok=True, at="works", x=1760, y=290),
    )),
    # 10. bug hunt: Zoe ----------------------------------------------------------------------------------
    Scene("j2-w08-s10", setting="mint", beats=(
        B("Zoe catches ten apples, but her game never ends!", speaker=NARRATOR, cue="zoe", pause=3.8),
        B("Look where her if score equals ten is.", speaker=NARRATOR, cue="where", pause=3.0),
        B("It sits above the forever loop. So it checks only once, at the very start, when the score is zero.",
          speaker=NARRATOR, cue="above", pause=0.6),
        B("The fix: drag the if back inside the forever, under the misses check.", speaker=NARRATOR, cue="fix",
          pause=0.6),
        B("Test again. Catch ten apples!", speaker=NARRATOR, cue="test", pause=5.6),
        B("You win! We fixed both bugs!", speaker=NARRATOR, cue="fixed", pause=0.4),
        B("Bug hunters, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! Never or Right Away?", at="start", color="navy"),
        A("scratch", "Zoe's game", blocks=[FLAG, SET_SCORE, WIN, ("control", "forever", [LOSE])],
          x=130, y=260, w=860, h=760, scale=0.85, at="start", until="fix@0.5", highlight=[(2, "above", "fix@0.5")]),
        A("scratch", "Zoe's game (fixed)", blocks=[FLAG, SET_SCORE, ("control", "forever", [LOSE, WIN])],
          x=130, y=260, w=860, h=760, scale=0.85, at="fix@0.5", highlight=[(6, "fix@0.5", "test")]),
        A("sfx", "snap", at="fix@0.5"),
        A("stage", x=1100, y=230, w=700, h=480, at="start", flag_at="zoe+0.1", sprite="apple",
          sprite_scale=SPRITE, sprite_y=TOP, extra=[BOWL],
          monitors=[("score", [("start", 0)] + counting("zoe", 12, 0.4, 0.6) + [("test", 0)] +
                     counting("test", 10, 0.5, 0.7))],
          actions=catches("zoe", 12, 0.4, base=0.3) + catches("test", 10, 0.5, base=0.3)),
        A("chip", "score 10... still going!", at="zoe+4.0", until="above", x=1450, y=860, color="red", size=40),
        A("thought", "Where is the if?", at="where$+0.2", until="above", x=1450, y=860),
        A("chip", "checks only once", at="above@0.4", until="test", x=1450, y=860, color="orange", size=44),
        A("bubble", "You win!", x=1560, y=560, at="test+5.3", until="end", size=40),
        A("badge", ok=True, at="fixed", x=1760, y=290),
        A("confetti", at="fixed", x=1450, y=470),
    )),
    # 11. no tricks: good games end ---------------------------------------------------------------------
    Scene("j2-w08-s11", setting="workshop", beats=(
        B("Our games end. You win, or it is game over, and then you choose what to do next.", speaker=NARRATOR,
          cue="ours", pause=0.5),
        B("Some games on phones and tablets are made so you never want to stop.", speaker=NARRATOR, cue="some",
          pause=0.4),
        B("They say: You almost won! One more go! That is a trick.", speaker=NARRATOR, cue="trick", pause=0.5),
        B("A game keeps saying: You were so close, play again! What can you do?", speaker=NARRATOR, cue="what",
          pause=3.0),
        B("Stop anyway! Say: No thanks, I am done. Take a break, and tell a grown-up if it is hard to stop.",
          speaker=NARRATOR, cue="stop", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "trick": "worried", "what": "thinking", "stop": "proud"},
          chin=("what", "stop")),
        A("pixi", x=600, y=760, moods={"trick": "worried", "stop": "happy"}),
        A("bubble", "One more go!", x=1300, y=330, at="trick@0.4", until="stop", size=42),
        A("thought", "What can you do?", at="what$+0.2", until="stop", x=1300, y=560),
        A("icons", at="ours", until="end", x=1300, y=760, gap=250,
          items=[("trophy", "Good games end", "ours@0.3"), ("cross", "No thanks!", "stop@0.1"),
                 ("clock", "Take a break", "stop@0.5"), ("grownup", "Tell a grown-up", "stop@0.8")]),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j2-w08-s12", setting="workshop", tail=0.8, beats=(
        B("Say the three parts of a game with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Start!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Play!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Ending!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("The start sets everything to zero. The forever keeps checking. Stop all is the final whistle.",
          speaker=NARRATOR, cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Add misses and the referee, test both endings, then write your game rules for next week.",
          speaker=NARRATOR, cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=NARRATOR, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Start!", at="w1", until="w1>", y=560, size=90, color="green"),
        A("bigtext", "Play!", at="w2", until="w2>", y=560, size=90, color="orange"),
        A("bigtext", "Ending!", at="w3", until="w3>", y=560, size=90, color="red"),
        A("chip", "start • play • ending", at="recap", until="turn", x=1200, y=520, color="green", size=48),
        A("chip", "stop all = the final whistle", at="recap@0.7", until="turn", x=1200, y=650, color="orange",
          size=44),
        A("banner", "NEXT: Win and Lose", at="turn", color="green"),
        A("cards", items=["Add misses and the referee", "Test both endings", "Write my game rules"], x=1000,
          y=300, w=640, gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
