"""Level 3 Week 8: Data Detectives: Clean, Count, Chart (kit episode)."""

from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

# Nova's little made-up, anonymous survey file (not the exercise's favorite_games.csv).
PETS = ["response,pet,minutes_playing", "1,Cat,20", "2, cat ,10", "3,,", "4,Dog,", "5,CAT,30"]

READ_CODE = '''import csv

with open("pets.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["pet"])'''

# The panel shows READ_CODE; the run first writes Nova's file so the code reads a real CSV.
READ_EXEC = "with open('pets.csv', 'w') as f:\n    f.write(" + repr("\n".join(PETS) + "\n") + ")\n" + READ_CODE

BUG_CODE = '''minutes = ["10", "9", "7"]
print(max(minutes))
print(sum(minutes))'''

FIX_CODE = '''text = ["10", "9", "7"]
minutes = []
for value in text:
    minutes.append(int(value))
print(max(minutes))
print(sum(minutes))'''

EPISODE = Episode(level=3, week=8, scenes=(
    # ------------------------------------------------------------------ s01 hook
    Scene("l3-w08-s01", setting="workshop", lead_in=0.2, beats=(
        B("Nova ran a survey: ‘What's your favorite pet?’", cue="survey", pause=0.3),
        B("Everyone could choose to answer or pass, and nobody wrote their name.", cue="pass", pause=0.3),
        B("Now the answers are in a file, and Pixel proudly reports:", cue="file", pause=0.1),
        B("‘Cat and CAT are two different pets!’", speaker=PIXEL, cue="report", pause=0.4),
        B("Hmm.", cue="hmm", pause=0.2),
        B("That doesn't sound right.", cue="right", pause=0.3),
        B("How can a data detective find the true story in messy answers?", cue="how", pause=3.0),
    ), actions=(
        A("door", "DOOR 8", x=1700, y=900),
        A("nova", x=300, y=960, enter="left", point="survey",
          moods={"report": "surprised", "hmm": "thinking"}, chin=("hmm", "end")),
        A("pixel", x=600, y=760, drop=True, moods={"report": "proud", "how": "confused"}, beep="report$"),
        A("banner", "MISSION: Find the true story", at="survey"),
        A("chip", "What's your favorite pet?", at="survey@0.4", until="file", x=1080, y=240, color="white",
          size=44),
        A("icons", at="pass", until="file", x=1080, y=470, gap=320,
          items=[("check", "Answer or pass", "pass@0.2"), ("lock", "No names", "pass@0.6")]),
        A("file", "pets.csv", at="file", until="end", x=780, y=200, w=640, h=420, lines=PETS),
        A("chip", "Cat", at="report@0.2", until="how", x=1500, y=300, color="green", size=46),
        A("chip", "CAT", at="report@0.5", until="how", x=1500, y=420, color="orange", size=46),
        A("magnifier", s=0.8, at="right", until="end",
          path=[("right", 1000, 330), ("how", 1150, 420), ("how$", 950, 520)]),
        A("chip", "Pause: Are Cat and CAT the same?", at="how", x=1080, y=760, color="yellow"),
        A("thought", "", at="how$+0.2", until="end", x=1500, y=360),
    )),
    # ------------------------------------------------------------------ s02 pipeline and CSV
    Scene("l3-w08-s02", setting="sky", beats=(
        B("Data detectives always work in the same order: read, clean, count, calculate, chart.", cue="order",
          pause=0.4),
        B("First, read.", cue="read", pause=0.2),
        B("A CSV file, short for comma-separated values, is a table saved as plain text.", cue="csv", pause=0.3),
        B("One line is one row, and commas split the columns.", cue="line", pause=0.3),
        B("The first line is the header: the column names.", cue="header", pause=0.4),
        B("Python's csv dot DictReader turns each row into a dictionary, so row, pet, in square brackets, gives that "
          "row's answer.", cue="dict", pause=0.4),
        B("Next, clean.", cue="clean", pause=0.2),
        B("Data is like vegetables from the garden: you wash off the mud before you cook.", cue="veg", pause=0.3),
        B("Strip extra spaces, fix MiXeD capitals, and throw away empty rows.", cue="strip", pause=0.3),
        B("Only then do we count, average and chart.", cue="only", pause=0.6),
    ), actions=(
        A("chip", "Read → Clean → Count → Calculate → Chart", at="order", x=960, y=110, color="orange", size=46),
        A("cards", at="order", x=50, y=220, w=300, gap=104,
          items=["Read", "Clean", "Count", "Calculate", "Chart"],
          reveal=["order@0.45", "order@0.55", "order@0.68", "order@0.8", "order@0.92"],
          active=[("read", "clean"), ("clean", "only"), "only@0.4", "only@0.6", "only@0.8"],
          done=["clean", "only", None, None, None]),
        A("file", "pets.csv", at="csv", until="dict", x=380, y=220, w=620, h=420, lines=PETS),
        A("table", x=1030, y=230, col_w=280, at="line", until="dict",
          header=["response", "pet", "minutes_playing"], rows=[["1", "Cat", "20"], ["2", " cat ", "10"],
                                                       ["3", "", ""], ["4", "Dog", ""], ["5", "CAT", "30"]],
          reveal=["line@0.3", "line@0.4", "line@0.5", "line@0.6", "line@0.7"]),
        A("chip", "CSV = a table saved as plain text", at="csv@0.4", until="dict", x=1150, y=760, color="sky",
          size=40),
        A("chip", "Header = the column names", at="header", until="dict", x=1450, y=186, color="yellow", size=34),
        A("code", code=READ_CODE, exec=READ_EXEC, title="read_pets.py", x=400, y=200, w=980, h=700, size=30,
          shell_h=300, at="dict", until="clean", run="dict@0.55", line_delay=0.5,
          expect=["Cat", " cat ", "", "Dog", "CAT"], highlight=[(4, "dict", "dict@0.5"), (5, "dict@0.5", "clean")]),
        A("dict", "row", x=1440, y=330, w=420, at="dict@0.3", until="clean",
          rows=[("response", '"1"'), ("pet", '"Cat"')], highlight=[("dict@0.5", "clean", "pet")]),
        A("chip", 'row["pet"] → "Cat"', at="dict@0.55", until="clean", x=1650, y=600, color="green", size=36),
        A("chip", "Wash off the mud before you cook", at="veg", until="only", x=1200, y=260, color="green", size=40),
        A("listrow", "pet (messy)", x=1200, y=500, cell=180, at="veg@0.5", until="end",
          items=["Cat", " cat ", "", "Dog", "CAT"], highlight=[("strip", "strip@0.3", 1), ("strip@0.3", "strip@0.6", 4),
                                                         ("strip@0.6", "strip$", 2)]),
        A("listrow", "pet (clean)", x=1200, y=800, cell=180, at="strip", until="end",
          states=[("strip", [" cat "]), ("strip@0.2", ["Cat", "cat"]), ("strip@0.45", ["Cat", "Cat", "CAT"]),
                  ("strip@0.55", ["Cat", "Cat", "Cat"]), ("strip@0.75", ["Cat", "Cat", "Dog", "Cat"])]),
        A("chip", "Clean before you count!", at="only", x=1200, y=980, color="yellow", size=40),
    )),
    # ------------------------------------------------------------------ s03 clean, tally, average, chart
    Scene("l3-w08-s03", setting="lavender", beats=(
        B("Here's Nova's little file.", cue="file", pause=0.3),
        B("Row two says space, cat, space.", cue="row2", pause=0.3),
        B("Row three is empty.", cue="row3", pause=0.3),
        B("Row four, Dog, has no minutes.", cue="row4", pause=0.3),
        B("After cleaning with strip and title, every spelling becomes Cat with a capital C, and the empty row is "
          "skipped.", cue="after", pause=0.5),
        B("Now count with a dictionary, like a tally chart.", cue="count", pause=0.3),
        B("A new pet starts at zero, then we add one.", cue="zero", pause=0.3),
        B("At the end: Cat, three. Dog, one.", cue="end3", pause=0.5),
        B("Next, the average minutes.", cue="avg", pause=0.2),
        B("The average is a fair share: put everything in one pile, then share it equally.", cue="fair", pause=0.3),
        B("Twenty plus ten plus thirty is sixty.", cue="sixty", pause=0.3),
        B("Three people answered, so sixty divided by three is twenty.", cue="twenty", pause=0.4),
        B("And the blank?", cue="blank", pause=1.2),
        B("A blank means ‘we don't know,’ not zero, so we skip it.", cue="dontknow", pause=0.5),
        B("Last, the chart.", cue="chart", pause=0.2),
        B("Cat gets the tallest bar.", cue="tallest", pause=0.3),
        B("Dog has one vote and Cat has three, so Dog's bar is one third as tall.", cue="third", pause=0.3),
        B("Write the name under every bar and the number on top.", cue="write", pause=0.6),
    ), actions=(
        A("table", "pets.csv", x=200, y=200, col_w=300, at="file", until="count",
          header=["response", "pet", "minutes_playing"],
          rows=[["1", "Cat", "20"], ["2", "' cat '", "10"], ["3", "", ""], ["4", "Dog", ""], ["5", "CAT", "30"]],
          highlight=[("row2", "row3", 1), ("row3", "row4", 2), ("row4", "after", 3)]),
        A("chip", "empty row", at="row3+0.3", until="after", x=1300, y=410, color="red", size=34),
        A("chip", "no minutes", at="row4+0.3", until="after", x=1300, y=480, color="red", size=34),
        A("listrow", "pet after .strip().title()", x=660, y=820, cell=170, at="after", until="count",
          states=[("after", ["Cat", "' cat '", "", "Dog", "CAT"]), ("after@0.35", ["Cat", "Cat", "", "Dog", "Cat"]),
                  ("after@0.8", ["Cat", "Cat", "Dog", "Cat"])], highlight=[("after@0.35", "after@0.8", 1),
                                                                         ("after@0.35", "after@0.8", 4)]),
        A("chip", "empty row skipped", at="after@0.8", until="count", x=1420, y=820, color="green", size=34),
        # tally with a dictionary
        A("dict", "counts", x=560, y=300, w=800, at="count", until="avg",
          states=[("count", []), ("zero@0.3", [("Cat", 0)]), ("zero@0.7", [("Cat", 1)]),
                  ("zero$+0.2", [("Cat", 2)]), ("zero$+0.5", [("Cat", 2), ("Dog", 1)]),
                  ("end3", [("Cat", 3), ("Dog", 1)])],
          highlight=[("zero@0.3", "zero$", "Cat"), ("end3", "end3@0.5", "Cat"), ("end3@0.5", "end3$", "Dog")]),
        A("chip", "counts = {}  (an empty dictionary)", at="count", until="zero@0.3", x=960, y=500, color="white",
          size=38),
        A("chip", "tally:  Cat |||   Dog |", at="end3", until="avg", x=960, y=620, color="white", size=40),
        A("chip", "Cat 3 • Dog 1", at="end3@0.5", until="avg", x=960, y=760, color="green", size=50),
        # fair-share average
        A("bars", x=250, y=270, w=780, h=460, at="avg", until="chart", labels=["row 1", "row 2", "row 5"],
          states=[("avg", [20, 10, 30]), ("twenty@0.6", [20, 20, 20])],
          highlight=[("sixty", "sixty$", [0, 1, 2])]),
        A("box", "total", x=1400, y=380, at="sixty", until="chart",
          values=[("sixty", 20), ("sixty@0.3", 30), ("sixty@0.6", 60)]),
        A("box", "average", x=1400, y=650, at="twenty", until="chart", values=[("twenty@0.6", 20)], color="green"),
        A("chip", "Average = fair share: 60 ÷ 3 = 20", at="twenty@0.6", until="chart", x=960, y=900,
          color="orange", size=44),
        A("chip", "row 4 (Dog): ?", at="blank", until="chart", x=1640, y=190, color="white", size=36),
        A("chip", "Blank = ‘we don't know’, not 0", at="dontknow", until="chart", x=960, y=1000, color="yellow",
          size=40),
        # the chart
        A("bars", x=560, y=240, w=800, h=500, at="chart", labels=["Cat", "Dog"], values=[3, 1],
          highlight=[("tallest", "tallest$", [0]), ("third", "third$", [1])]),
        A("chip", "1 vote = 1/3 of 3 votes", at="third@0.6", until="write", x=1600, y=640, color="white", size=34),
        A("chip", "Every bar: name below, number on top", at="write", x=960, y=920, color="green", size=44),
    )),
    # ------------------------------------------------------------------ s04 bug hunt
    Scene("l3-w08-s04", setting="mint", beats=(
        B("Bug hunt!", cue="bug", pause=0.3),
        B("Nova's minutes came straight from a file: quote ten, quote nine, quote seven.", cue="minutes", pause=0.3),
        B("Pixel finds the biggest with max, and max says quote nine.", cue="max", pause=0.3),
        B("Nine is bigger than ten?", cue="bigger", pause=1.2),
        B("Then sum crashes with a red error.", cue="crash", pause=0.4),
        B("Let's use our steps.", cue="steps", pause=0.2),
        B("Read the last line: TypeError, unsupported operand types for plus, int and str.", cue="read", pause=0.3),
        B("Predict.", cue="predict", pause=0.2),
        B("‘I think these numbers are really words,’", speaker=NOVA, cue="words", pause=0.1),
        B("says Nova.", cue="says", pause=0.3),
        B("Watch: each number has quote marks around it.", cue="watch", pause=0.3),
        B("Every CSV value arrives as text, and text is compared letter by letter.", cue="text", pause=0.4),
        B("Fix one thing:", cue="fix", pause=3.6),
        B("turn text into numbers while cleaning.", cue="turn", pause=0.3),
        B("int of quote ten gives the number ten.", cue="int", pause=0.3),
        B("But careful!", cue="careful", pause=0.2),
        B("int of an empty answer crashes with a ValueError, so a blank becomes None, and we skip it.", cue="empty",
          pause=0.4),
        B("Check: run again.", cue="check", pause=0.3),
        B("The biggest is ten, and the total is twenty-six.", cue="total", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT!", at="bug", color="navy"),
        A("code", code=BUG_CODE, title="minutes.py", x=90, y=180, w=880, h=520, size=36, shell_h=230,
          at="minutes", until="turn", type=("minutes", "minutes@0.6"), run="max@0.5", line_delay=2.6,
          allow_error=True, error_line=3, expect=["9", "TypeError: unsupported operand type(s) for +: 'int' and 'str'"],
          highlight=[(2, "max", "bigger>"), (3, "crash", "read$"), (1, "watch", "text$")]),
        A("chip", 'max(["10", "9", "7"]) → "9"', at="max@0.8", until="read", x=530, y=780, color="orange", size=40),
        A("pixel", x=1500, y=860, s=0.5, ground=930, at="max", until="steps", moods={"max": "proud", "bigger": "confused"}),
        A("chip", "TypeError: unsupported operand type(s) for +: 'int' and 'str'", at="read", until="text", x=840,
          y=780, color="red", size=30),
        A("cards", at="steps", x=1090, y=240, w=660, gap=86, size=34,
          items=["Read", "Predict", "Watch", "Fix ONE thing", "Check"],
          reveal=["steps", "steps@0.2", "steps@0.4", "steps@0.6", "steps@0.8"],
          active=["read", ("predict", "watch"), ("watch", "fix"), ("fix", "check"), ("check", "end")],
          done=["predict", "watch", "fix", "check", "total+1.0"]),
        A("chip", "CSV values arrive as text", at="text", until="int", x=530, y=780, color="yellow", size=40),
        A("thought", "Which one change?", at="fix$+0.3", until="fix>", x=530, y=880),
        A("code", code=FIX_CODE, title="minutes.py", x=90, y=180, w=880, h=560, size=30, shell_h=170,
          at="turn", run="check$", line_delay=0.5, expect=["10", "26"],
          highlight=[(4, "turn", "int$")]),
        A("machine", "int", x=1250, y=900, at="int", until="check",
          items=[("int", '"10"', "10"), ("empty", '""', "crash")]),
        A("chip", "ValueError", at="empty@0.45", until="check", x=1700, y=760, color="red", size=36),
        A("chip", 'int("10") → 10', at="int@0.5", until="empty", x=520, y=800, color="green", size=40),
        A("chip", "Blank → None → skip it", at="empty@0.5", x=520, y=800, color="yellow", size=40),
        A("badge", ok=False, at="crash", until="turn", x=1830, y=370, r=40),
        A("badge", ok=True, at="total", x=1400, y=860),
        A("confetti", at="total", x=1400, y=700),
        A("nova", x=1720, y=1060, s=0.5, at="total", moods={"total": "proud"}),
    )),
    # ------------------------------------------------------------------ s05 recap
    Scene("l3-w08-s05", setting="workshop", tail=0.8, beats=(
        B("Case closed!", cue="closed", pause=0.4),
        B("Read the CSV, clean it, count with a dictionary, take a fair-share average that skips blanks, and label "
          "every bar.", cue="recap", pause=0.4),
        B("Now the most important part.", cue="important", pause=0.3),
        B("Nova's survey asked first, let people pass, and had no names.", cue="asked", pause=0.3),
        B("That's consent and anonymity.", cue="consent", pause=0.4),
        B("Even without names, some answers together can point to one person, like the only thirteen-year-old in the "
          "chess club.", cue="point", pause=0.4),
        B("Before sharing data, keep only the columns you need, replace names with IDs like R1 and R2, and never "
          "collect addresses, schools, birthdays or photos.", cue="before", pause=0.5),
        B("Now open Exercise 8.1, the Survey cleaner, and type along with your teacher.", cue="next", pause=0.3),
        B("Spot the mess in favorite_games.csv, then clean it until the Shell says Clean answers: seventeen.",
          cue="spot", pause=0.4),
        B("Happy detecting!", cue="happy", pause=0.4),
    ), actions=(
        A("door", "DOOR 8", x=1700, y=920, open="closed"),
        A("nova", x=260, y=1010, s=0.72, wave=[("start", "recap"), ("happy", "end")], moods={"start": "proud"}),
        A("pixel", x=470, y=860, s=0.62, ground=1000, moods={"start": "proud"}),
        A("cards", at="recap", until="asked", x=720, y=230, w=760, gap=100, size=36,
          items=["Read the CSV", "Clean it", "Count with a dictionary", "Fair-share average", "Label every bar"],
          reveal=["recap", "recap@0.15", "recap@0.3", "recap@0.55", "recap@0.85"]),
        A("chip", "Clean • Count • Average • Label", at="recap@0.4", until="asked", x=1100, y=760,
          color="orange", size=42),
        A("icons", at="asked", until="point", x=1100, y=420, gap=270,
          items=[("check", "Asked first", "asked@0.2"), ("check", "Can pass", "asked@0.5"),
                 ("lock", "No names", "asked@0.8")]),
        A("chip", "Consent • Anonymity", at="consent", until="point", x=1100, y=700, color="green", size=44),
        A("table", x=700, y=260, col_w=200, at="point", until="before@0.35",
          header=["nickname", "age", "club", "pet"],
          rows=[["Star", "10", "art", "Cat"], ["Comet", "11", "chess", "Dog"], ["Moon", "13", "chess", "Cat"]],
          highlight=[("point@0.6", "before", 2)]),
        A("chip", "only one 13 in chess → it's Moon!", at="point@0.7", until="before@0.35", x=1100, y=630,
          color="red", size=38),
        A("chip", "Consent • Keep only what you need • R1, R2", at="before", until="next", x=1080, y=200,
          color="orange", size=40),
        A("table", x=900, y=270, col_w=200, at="before@0.35", until="next", header=["id", "pet"],
          rows=[["R1", "Cat"], ["R2", "Dog"], ["R3", "Cat"]]),
        A("icons", at="before@0.6", until="next", x=1080, y=680, gap=220, crossed=[0, 1, 2, 3],
          items=[("house", "Addresses", "before@0.62"), ("book", "Schools", "before@0.7"),
                 ("star", "Birthdays", "before@0.8"), ("camera", "Photos", "before@0.9")]),
        A("banner", "NEXT: 8.1 Survey cleaner", at="next", color="green"),
        A("cards", at="next", x=700, y=230, w=800, gap=110,
          items=["Open 8.1 Survey cleaner", "Type along with your teacher", "Spot the mess in favorite_games.csv",
                 "Clean until: Clean answers: 17"],
          reveal=["next@0.1", "next@0.5", "spot", "spot@0.6"]),
        A("chip", "Happy detecting!", at="happy", x=1100, y=780, color="orange", size=48),
    )),
))
