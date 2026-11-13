"""MY ART STUDIO - starter template (project option B).

Run it first! Click the window, then press:
    n   make a new random design
    s   save the design in my_design.txt (next to this program)
    l   load the saved design          (TODO 2 makes this work)
Then make it YOUR studio by working through the TODOs.

Project checklist - your finished studio needs all of these:
  [ ] functions with parameters that return values (random_design ...)
  [ ] a list        (PALETTE - TODO 3: a list of designs, a gallery)
  [ ] a dictionary  (each design is a dict)
  [ ] a while loop  (draw_spiral)
  [ ] a file        (save works; TODO 2: make load work)
  [ ] 3+ tests      (my_tests.py)
"""

import random
import turtle
from pathlib import Path

# Okabe-Ito colors: safe for color-blind viewers.
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

# The saved design sits in the same folder as this program.
SAVE_FILE = Path(__file__).parent / "my_design.txt"

view = {}                 # the screen and the turtle
current = {}              # the design on the screen right now


# ---------- RULES: pure functions, no turtle. Test them in my_tests.py.

def random_design():
    """Return a new design: a dictionary of settings."""
    # TODO 1: add your own keys, e.g. "background" or "stroke".
    return {
        "petals": random.randint(3, 12),
        "size": random.randint(60, 180),
        "color": random.choice(PALETTE[:7]),
    }


def design_to_text(design):
    """Turn a design into text, one "key=value" line per setting."""
    lines = []
    for key, value in design.items():
        lines.append(f"{key}={value}")
    return "\n".join(lines) + "\n"


def text_to_design(text):
    """The opposite of design_to_text: turn the text back into a dict."""
    design = {}
    # TODO 2: for each line in text.split("\n"):
    #   skip empty lines ("");
    #   parts = line.split("=")   ->  "petals=6" becomes ["petals", "6"]
    #   key = parts[0] and value = parts[1];
    #   if value.isdigit() (only digits, like "6"), turn it into int(value);
    #   then put it in the dictionary: design[key] = value
    return design


# ---------- DRAWING AND KEYS

def draw_spiral(t, size):
    """A small spiral in the middle. It grows WHILE it is smaller than size."""
    t.penup()
    t.goto(0, 0)
    t.pendown()
    length = 2
    while length < size / 4:
        t.forward(length)
        t.left(30)
        length = length + 1


def draw_design(t, design):
    """Draw one design: petals in a circle, then a spiral."""
    t.clear()
    t.color(design["color"])
    t.pensize(2)
    for _ in range(design["petals"]):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.circle(design["size"] / 2, 120)   # one side of a petal
        t.left(60)
        t.circle(design["size"] / 2, 120)   # the other side
        t.left(60 + 360 / design["petals"])
    draw_spiral(t, design["size"])
    view["screen"].update()


def new_design():
    current.clear()
    current.update(random_design())
    draw_design(view["artist"], current)


def save_design():
    with open(SAVE_FILE, "w") as file:
        file.write(design_to_text(current))
    print("Saved to", SAVE_FILE.name)


def load_design():
    try:
        with open(SAVE_FILE) as file:
            design = text_to_design(file.read())
    except FileNotFoundError:
        print("Nothing saved yet - press s first.")
        return
    if not design:
        print("TODO 2: finish text_to_design so loading works.")
        return
    current.clear()
    current.update(design)
    draw_design(view["artist"], current)


def start_studio():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("My Art Studio")
    screen.tracer(0)
    artist = turtle.Turtle()
    artist.hideturtle()
    view.update(screen=screen, artist=artist)
    screen.onkey(new_design, "n")
    screen.onkey(save_design, "s")
    screen.onkey(load_design, "l")
    # TODO 3: keep a LIST of designs (a gallery) and press g to show them.
    screen.listen()
    new_design()


if __name__ == "__main__":
    start_studio()
    turtle.done()
