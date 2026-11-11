"""Level 3 Week 7: Grids, Recursion and Fractal Art (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

# The finished countdown() from the Exercise 7.1 starter (comments shown as on-screen labels instead).
COUNTDOWN = '''def countdown(n):
    if n <= 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)'''


def tree_program(depth: int, length: int = 100) -> str:
    """A real recursive fractal tree (the canvas runs it; the code itself is never shown on screen)."""
    return f'''import turtle

t = turtle.Turtle()
t.left(90)

def tree(length, depth):
    if depth == 0:
        return
    t.pensize(depth + 1)
    t.pencolor(["#E69F00", "#009E73", "#56B4E9", "#0072B2", "#D55E00", "#CC79A7"][depth % 6])
    t.forward(length)
    t.left(25)
    tree(length * 0.7, depth - 1)
    t.right(50)
    tree(length * 0.7, depth - 1)
    t.left(25)
    t.penup()
    t.back(length)
    t.pendown()

t.penup()
t.back({length})
t.pendown()
tree({length}, {depth})
turtle.done()
'''


FOREST = '''import turtle

t = turtle.Turtle()
t.left(90)

def tree(length, depth):
    if depth == 0:
        return
    t.pensize(depth)
    t.pencolor(["#E69F00", "#009E73", "#56B4E9", "#0072B2", "#D55E00"][depth % 5])
    t.forward(length)
    t.left(25)
    tree(length * 0.7, depth - 1)
    t.right(50)
    tree(length * 0.7, depth - 1)
    t.left(25)
    t.penup()
    t.back(length)
    t.pendown()

for x in [-160, 0, 160]:
    t.penup()
    t.goto(x, -150)
    t.pendown()
    tree(70, 5)
turtle.done()
'''

DOLL_BUG = '''def open_doll(size):
    print("Opening doll", size)
    open_doll(size - 1)

open_doll(3)'''

DOLL_FIX = '''def open_doll(size):
    if size == 0:
        print("Solid doll!")
        return
    print("Opening doll", size)
    open_doll(size - 1)

open_doll(3)'''

GRID_CODE = '''grid = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
]
print(grid[1][3])'''

LETTERS = ["ABCD", "EFGH", "IJKL"]

# Letter grid geometry (s03): 4 columns x 3 rows, cell 130, top-left (1150, 300)
GX, GY, GC = 1150, 300, 130


def cell_center(row: int, col: int) -> tuple[float, float]:
    return GX + col * GC + GC / 2, GY + row * GC + GC / 2


EPISODE = Episode(level=3, week=7, scenes=(
    # ------------------------------------------------------------------ s01 hook
    Scene("l3-w07-s01", setting="workshop", lead_in=0.2, beats=(
        B("Welcome back to Kids Coding!", cue="welcome", pause=0.3),
        B("Today Nova wants two things: a whole forest of trees drawn by code, and a paint bucket that fills a pixel "
          "picture with one click.", cue="wants", pause=0.3),
        B("‘That sounds like thousands of lines,’", speaker=PIXEL, cue="lines", pause=0.1),
        B("beeps Pixel.", cue="beeps", pause=0.3),
        B("‘Not if a function can call itself,’", speaker=NOVA, cue="notif", pause=0.1),
        B("says Nova.", cue="says", pause=0.4),
        B("Wait… a function that calls itself?", cue="wait", pause=0.3),
        B("Can it ever stop?", cue="stop", pause=3.0),
    ), actions=(
        A("door", "DOOR 7", x=1700, y=900),
        A("nova", x=300, y=960, enter="left", wave="welcome",
          moods={"lines": "surprised", "notif": "proud", "wait": "thinking"}, point="notif", chin=("stop", "end")),
        A("pixel", x=600, y=760, drop=True, moods={"lines": "worried", "wait": "confused"}),
        A("banner", "MISSION: A forest and a paint bucket", at="wants"),
        A("turtle", code=FOREST, x=760, y=190, w=480, h=440, run="wants@0.15", duration=3.2, title="A forest",
          at="wants", until="lines"),
        A("grid", x=1290, y=180, cell=50, at="wants", until="lines",
          states=[("wants", ["........", ".######.", ".#....#.", ".#....#.", ".######.", "........"]),
                  ("wants@0.85", ["........", ".######.", ".#BBBB#.", ".#BBBB#.", ".######.", "........"])]),
        A("chip", "one click → fill!", at="wants@0.85", until="lines", x=1420, y=530, color="sky", size=34),
        A("stack", x=1050, y=900, at="lines", until="notif",
          states=[("lines", ["page 1"]), ("lines@0.35", ["page 1", "page 2"]),
                  ("lines@0.7", ["page 1", "page 2", "page 3"]),
                  ("beeps", ["page 1", "page 2", "page 3", "… page 9999"])]),
        A("sfx", "boing", at="beeps"),
        A("chip", "def tree(): … tree() ↺", at="notif", until="stop", x=1040, y=420, color="green", size=44),
        A("chip", "A function that calls itself?", at="wait", until="stop", x=1040, y=560, color="white", size=40),
        A("chip", "Pause: Can a function call itself?", at="stop", x=1040, y=250, color="yellow"),
        A("thought", "?", at="stop$+0.2", until="end", x=840, y=380),
    )),
    # ------------------------------------------------------------------ s02 base case and recursive case
    Scene("l3-w07-s02", setting="sky", beats=(
        B("Picture a set of Russian dolls.", cue="picture", pause=0.3),
        B("Your job is: open the doll.", cue="job", pause=0.3),
        B("Inside is a smaller doll, so your job is the same again.", cue="inside", pause=0.3),
        B("You keep going until you reach the tiny solid doll.", cue="keep", pause=0.3),
        B("It can't open, so you stop.", cue="cant", pause=0.4),
        B("That's recursion: a function that calls itself on a smaller problem.", cue="recursion", pause=0.4),
        B("Every recursive function has two parts.", cue="two", pause=0.3),
        B("The recursive case does one small step, then calls itself on something smaller.", cue="rcase", pause=0.3),
        B("The base case is the tiny problem you can answer straight away, so you stop.", cue="bcase", pause=0.4),
        B("Look at countdown.", cue="look", pause=0.3),
        B("If n is zero or less, print Liftoff and return.", cue="ifline", pause=0.2),
        B("That's the base case.", cue="thats", pause=0.3),
        B("Otherwise, print n, then call countdown with n minus one.", cue="otherwise", pause=0.6),
    ), actions=(
        A("box", "doll", x=420, y=480, w=340, h=300, color="pink", at="picture", until="look",
          values=[("picture", "open")]),
        A("arrow", x1=620, y1=480, x2=720, y2=480, color="navy", at="inside", until="look"),
        A("box", "smaller", x=880, y=480, w=260, h=230, color="orange", at="inside", until="look",
          values=[("inside", "open")]),
        A("arrow", x1=1040, y1=480, x2=1120, y2=480, color="navy", at="keep@0.2", until="look"),
        A("box", "smaller", x=1250, y=480, w=200, h=170, color="yellow", at="keep@0.2", until="look",
          values=[("keep@0.2", "open")]),
        A("arrow", x1=1380, y1=480, x2=1450, y2=480, color="navy", at="keep@0.7", until="look"),
        A("box", "solid", x=1560, y=480, w=160, h=130, color="green", at="keep@0.7", until="look",
          values=[("keep@0.7", ""), ("cant", "STOP")]),
        A("badge", ok=True, at="cant", until="look", x=1640, y=380, r=36),
        A("chip", "base case", at="cant@0.5", until="look", x=1560, y=640, color="orange", size=36),
        A("chip", "Recursion = same job, smaller problem", at="recursion", until="look", x=960, y=120,
          color="orange", size=46),
        A("chip", "Recursive case = small step + call again", at="rcase", until="look", x=960, y=800,
          color="sky", size=42),
        A("chip", "Base case = stop here", at="bcase", until="look", x=960, y=920, color="orange", size=42),
        A("code", code=COUNTDOWN, title="countdown.py", x=140, y=200, w=1060, h=600, size=44, at="look",
          highlight=[(2, "ifline", "thats$"), (3, "ifline", "thats$"), (4, "ifline", "thats$"),
                     (5, "otherwise", "end"), (6, "otherwise@0.4", "end")]),
        A("arrow", x1=1440, y1=396, x2=1215, y2=396, color="#C77700", at="thats"),
        A("chip", "base case", at="thats", x=1600, y=396, color="orange", size=40),
        A("chip", "stop here", at="thats+0.3", x=1600, y=480, color="white", size=32),
        A("arrow", x1=1440, y1=651, x2=1215, y2=651, color="blue", at="otherwise@0.4"),
        A("chip", "recursive case", at="otherwise@0.4", x=1640, y=651, color="sky", size=40),
        A("chip", "small step + call again", at="otherwise@0.6", x=1640, y=735, color="white", size=32),
    )),
    # ------------------------------------------------------------------ s03 calls, fractal tree, grid
    Scene("l3-w07-s03", setting="lavender", beats=(
        B("Let's watch countdown of three run.", cue="watch", pause=0.3),
        B("It prints three, then calls countdown of two, which waits inside it like a smaller doll.", cue="prints",
          pause=0.2),
        B("Two, one…", cue="twoone", pause=0.2),
        B("then countdown of zero reaches the base case: Liftoff!", cue="zero", pause=0.6),
        B("A fractal is a shape made of smaller copies of itself.", cue="fractal", pause=0.3),
        B("A tree is a trunk with two smaller trees on top, until the depth reaches zero.", cue="tree", pause=0.3),
        B("Depth one is one line.", cue="d1", pause=0.4),
        B("Depth two, three lines.", cue="d2", pause=0.4),
        B("Depth three, seven.", cue="d3", pause=0.6),
        B("Now grids.", cue="grids", pause=0.2),
        B("A grid is a list of rows, and each row is a list.", cue="rows", pause=0.3),
        B("grid, row one, column three, means go down to row one, then across to column three, both counted from "
          "zero.", cue="cell", pause=0.3),
        B("Like a movie ticket: row first, then seat.", cue="ticket", pause=0.3),
        B("That cell is H.", cue="h", pause=0.5),
        B("A paint bucket paints one square, then asks each neighbor, up, down, left and right, to do the same.",
          cue="bucket", pause=0.3),
        B("Where should the paint stop?", cue="where", pause=2.6),
        B("You'll work that out in Exercise 7.3!", cue="ex", pause=0.6),
    ), actions=(
        # countdown(3) with the call stack
        A("code", code=COUNTDOWN + "\n\ncountdown(3)", title="countdown.py", x=120, y=170, w=900, h=780, size=32,
          shell_h=290, at="watch", until="fractal", run="watch$", line_delay=1.6,
          expect=["3", "2", "1", "Liftoff!"],
          highlight=[(8, "watch", "prints"), (5, "prints", "prints@0.4"), (6, "prints@0.4", "twoone"),
                     (2, "zero", "zero$")]),
        A("stack", "calls waiting inside each other", x=1420, y=820, at="prints", until="fractal",
          states=[("prints", ["countdown(3)"]), ("prints@0.45", ["countdown(3)", "countdown(2)"]),
                  ("twoone@0.5", ["countdown(3)", "countdown(2)", "countdown(1)"]),
                  ("zero", ["countdown(3)", "countdown(2)", "countdown(1)", "countdown(0)"]),
                  ("zero$+0.2", ["countdown(3)", "countdown(2)", "countdown(1)"]),
                  ("zero$+0.4", ["countdown(3)", "countdown(2)"]),
                  ("zero$+0.6", ["countdown(3)"]), ("fractal-0.2", [])]),
        A("chip", "countdown(3): 3, 2, 1, Liftoff!", at="zero$", until="fractal", x=1420, y=180, color="green",
          size=40),
        # fractal trees
        A("chip", "Fractal = smaller copies of itself", at="fractal", until="d1", x=960, y=130, color="orange",
          size=44),
        A("turtle", code=tree_program(6, 90), x=660, y=220, w=600, h=600, run="fractal", duration=3.0,
          title="fractal tree", world=190, at="fractal", until="tree@0.8"),
        A("turtle", code=tree_program(1), x=150, y=240, w=500, h=500, run="d1", duration=1.0, title="depth 1",
          world=140, at="tree@0.8", until="grids"),
        A("turtle", code=tree_program(2), x=710, y=240, w=500, h=500, run="d2", duration=1.4, title="depth 2",
          world=140, at="d2", until="grids"),
        A("turtle", code=tree_program(3), x=1270, y=240, w=500, h=500, run="d3", duration=1.8, title="depth 3",
          world=140, at="d3", until="grids"),
        A("chip", "1 line", at="d1+0.6", until="grids", x=400, y=800, color="white", size=38),
        A("chip", "3 lines", at="d2+0.8", until="grids", x=960, y=800, color="white", size=38),
        A("chip", "7 lines", at="d3+1.0", until="grids", x=1520, y=800, color="white", size=38),
        A("chip", "Depth 1 → 1 line • 2 → 3 • 3 → 7", at="d3$", until="grids", x=960, y=940, color="green",
          size=46),
        # a grid of letters
        A("code", code=GRID_CODE, title="grid.py", x=100, y=190, w=860, h=630, size=32, at="rows", until="bucket",
          run="h", expect=["H"], highlight=[(1, "rows", "rows$"), (5, "rows", "rows$"), (3, "cell", "h$"),
                                            (6, "cell", "h$")]),
        A("grid", x=GX, y=GY, cell=GC, at="grids", until="bucket",
          states=[("grids", ["....", "....", "...."]), ("h", ["....", "...G", "...."])],
          marks=[("grids", r, c, LETTERS[r][c]) for r in range(3) for c in range(4)]
          + [("rows", -1, c, str(c)) for c in range(4)] + [("rows", r, -1, str(r)) for r in range(3)]),
        A("chip", "rows ↓   columns →", at="rows", until="cell", x=GX + 2 * GC, y=GY - 160, color="white", size=34),
        A("pointer", s=0.9, at="cell", until="h$", path=[("cell", GX + 4 * GC + 20, GY + GC / 2),
                                                          ("cell@0.35", GX + 4 * GC + 20, GY + GC * 1.5),
                                                          ("cell@0.75", GX + 3 * GC + GC * 0.8, GY + GC * 1.5)]),
        A("chip", "grid[1][3] → row 1, then column 3", at="cell", until="bucket", x=960, y=860, color="orange",
          size=44),
        A("chip", "[row][col] is not (x, y)", at="ticket", until="bucket", x=960, y=980, color="yellow", size=42),
        # paint bucket
        A("grid", x=660, y=230, cell=120, at="bucket",
          states=[("bucket", [".....", ".....", ".....", ".....", "....."]),
                  ("bucket+0.4", [".....", ".....", "..B..", ".....", "....."])]),
        A("chip", "paint", at="bucket+0.4", until="where", x=960, y=530, color="sky", size=28),
        A("arrow", x1=960, y1=470, x2=960, y2=370, color="#C77700", at="bucket@0.45", width=10),
        A("arrow", x1=960, y1=590, x2=960, y2=690, color="#C77700", at="bucket@0.55", width=10),
        A("arrow", x1=900, y1=530, x2=800, y2=530, color="#C77700", at="bucket@0.7", width=10),
        A("arrow", x1=1020, y1=530, x2=1120, y2=530, color="#C77700", at="bucket@0.8", width=10),
        A("chip", "up", at="bucket@0.45", x=960, y=330, color="white", size=28),
        A("chip", "down", at="bucket@0.55", x=960, y=740, color="white", size=28),
        A("chip", "left", at="bucket@0.7", x=730, y=530, color="white", size=28),
        A("chip", "right", at="bucket@0.8", x=1190, y=530, color="white", size=28),
        A("thought", "?", at="where", until="ex", x=1500, y=420),
        A("chip", "Exercise 7.3: Paint bucket", at="ex", x=960, y=960, color="green", size=44),
    )),
    # ------------------------------------------------------------------ s04 bug hunt
    Scene("l3-w07-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Nova writes a function called open_doll.", cue="writes", pause=0.2),
        B("It prints ‘Opening doll’ and the size, then calls open_doll with the size minus one.", cue="prints",
          pause=0.3),
        B("Pixel runs open_doll of three.", cue="runs", pause=0.3),
        B("Three, two, one, zero, minus one, minus two…", cue="falling", pause=0.2),
        B("the numbers keep falling below zero, and then a red error appears.", cue="red", pause=0.4),
        B("Let's use our bug-hunting steps.", cue="steps", pause=0.3),
        B("One, read the last line of the error: RecursionError, maximum recursion depth exceeded.", cue="read",
          pause=0.3),
        B("Two, predict.", cue="predict", pause=0.2),
        B("‘I think it never stops,’", speaker=NOVA, cue="never", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("RecursionError? Look for the base case first!", cue="look", pause=0.4),
        B("Three, watch: in the debugger, Step into, and the calls pile up like plates.", cue="watch", pause=0.4),
        B("Four, fix one thing.", cue="fix", pause=3.6),
        B("Nova adds a base case: if size is zero, print ‘Solid doll!’ and return.", cue="adds", pause=0.4),
        B("Five, check: run it again.", cue="check", pause=0.3),
        B("Opening doll three, two, one, Solid doll!", cue="rerun", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        # Python stops this code after about a thousand calls; the run uses a lower limit so the
        # Shell shows the same story in a few seconds (same lines, same error).
        A("code", code=DOLL_BUG, title="dolls.py", x=90, y=200, w=900, h=650, size=34, shell_h=290,
          at="writes", until="adds", type=("writes", "prints$"), run="runs$", line_delay=0.3,
          exec="import sys\nsys.setrecursionlimit(25)\n" + DOLL_BUG, allow_error=True, error_line=3,
          expect=[f"Opening doll {n}" for n in range(3, -17, -1)]
          + ["RecursionError: maximum recursion depth exceeded while calling a Python object"],
          highlight=[(3, "look", "look$"), (3, "watch", "watch$")]),
        A("chip", "RecursionError: maximum recursion depth exceeded", at="read", until="look", x=540, y=900,
          color="red", size=32),
        A("chip", "RecursionError? Find the base case first", at="look", until="fix", x=540, y=900,
          color="yellow", size=38),
        A("chip", "Read • Predict • Watch • Fix one • Check", at="steps", x=1420, y=200, color="white", size=34),
        A("cards", at="steps", x=1090, y=250, w=660, gap=86, size=34,
          items=["Read", "Predict", "Watch", "Fix ONE thing", "Check"],
          reveal=["steps", "steps@0.2", "steps@0.4", "steps@0.6", "steps@0.8"],
          active=["read", ("predict", "look>"), "watch", ("fix", "check"), ("check", "end")],
          done=["predict", "watch", "fix", "check", "rerun+1.2"]),
        A("stack", x=1420, y=1000, at="watch", until="fix",
          states=[("watch@0.3", ["open_doll(3)"]), ("watch@0.45", ["open_doll(3)", "open_doll(2)"]),
                  ("watch@0.6", ["open_doll(3)", "open_doll(2)", "open_doll(1)"]),
                  ("watch@0.75", ["open_doll(3)", "open_doll(2)", "open_doll(1)", "open_doll(0)"])]),
        A("thought", "Which one change?", at="fix$+0.3", until="fix>", x=1420, y=830),
        A("code", code=DOLL_FIX, title="dolls.py", x=90, y=200, w=900, h=780, size=34, shell_h=260,
          at="adds", run="check$", line_delay=0.5,
          expect=["Opening doll 3", "Opening doll 2", "Opening doll 1", "Solid doll!"],
          highlight=[(2, "adds", "check"), (3, "adds", "check"), (4, "adds", "check")]),
        A("chip", "Each call must get smaller", at="rerun", x=1380, y=830, color="green", size=40),
        A("badge", ok=False, at="red", until="adds", x=1830, y=380, r=40),
        A("badge", ok=True, at="rerun+1.0", x=1420, y=960),
        A("confetti", at="rerun+1.0", x=1420, y=700),
        A("pixel", x=1770, y=930, s=0.45, ground=1000, at="rerun", moods={"rerun": "proud"}),
    )),
    # ------------------------------------------------------------------ s05 recap
    Scene("l3-w07-s05", setting="workshop", tail=0.8, beats=(
        B("Door seven unlocked!", cue="door", pause=0.4),
        B("Recursion means a function calls itself on a smaller problem.", cue="rec", pause=0.3),
        B("The base case says stop, and the recursive case does one small step and calls itself again.", cue="cases",
          pause=0.3),
        B("A grid is a list of rows: row first, then column.", cue="grid", pause=0.4),
        B("The fractal tree is a famous idea, and the Koch snowflake was invented by Helge von Koch in 1904.",
          cue="koch", pause=0.3),
        B("When you show generative art, say where the idea came from, like", cue="credit", pause=0.1),
        B("‘Fractal tree, based on a classic recursive algorithm; my colors and angles.’", cue="quote", pause=0.3),
        B("Add a comment that starts with Based on at the top of your file.", cue="comment", pause=0.5),
        B("Now open Exercise 7.2, the Fractal tree, and type along with your teacher.", cue="next", pause=0.3),
        B("Then finish sum_to and reverse in Exercise 7.1.", cue="then", pause=0.3),
        B("Where's your base case?", cue="where", pause=0.6),
        B("Happy coding!", cue="happy", pause=0.4),
    ), actions=(
        A("door", "DOOR 7", x=1700, y=920, open="door"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "rec"), ("happy", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("box", "doll", x=780, y=520, w=200, h=180, color="pink", at="rec", until="koch", values=[("rec", "open")]),
        A("box", "solid", x=980, y=540, w=170, h=130, color="green", at="cases", until="koch", size=40,
          values=[("cases", "stop")]),
        A("grid", x=1130, y=440, cell=56, at="grid", until="koch", rows=["....", "...G", "...."]),
        A("chip", "Base case • Smaller call • grid[row][col]", at="grid", until="koch", x=1060, y=280,
          color="orange", size=42),
        A("turtle", code=tree_program(5, 90), x=720, y=200, w=460, h=440, run="koch", duration=2.5,
          title="Fractal tree", world=180, at="koch", until="comment"),
        A("chip", "Koch snowflake: Helge von Koch, 1904", at="koch@0.5", until="comment", x=1080, y=730,
          color="white", size=36),
        A("bubble", "Fractal tree, based on a classic recursive algorithm; my colors and angles.", at="quote",
          until="comment", x=1190, y=420, tail="down-left", size=34, max_width=460),
        A("code", code="# Based on: classic fractal tree; my colors\nimport turtle", title="fractal_tree.py",
          x=660, y=640, w=900, h=220, size=28, at="comment", until="next"),
        A("chip", "# Based on: classic fractal tree", at="comment@0.4", until="next", x=1120, y=480,
          color="green", size=38),
        A("banner", "NEXT: 7.2 Fractal tree, then 7.1", at="next", color="green"),
        A("cards", at="next", x=700, y=230, w=760, gap=110,
          items=["Open 7.2 Fractal tree", "Type along with your teacher", "Finish sum_to and reverse (7.1)",
                 "Where's your base case?"],
          reveal=["next@0.1", "next@0.5", "then", "where"]),
        A("chip", "Happy coding!", at="happy", x=1080, y=780, color="orange", size=48),
    )),
))
