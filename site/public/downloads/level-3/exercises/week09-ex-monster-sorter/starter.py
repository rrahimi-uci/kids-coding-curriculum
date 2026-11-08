# Monster sorter
# A tiny "machine learning" program: a NEAREST-NEIGHBOR classifier.
# Each monster card has two FEATURES we can measure:
#   fluff (0-10): how fluffy it is      teeth (0-10): how many sharp teeth
# and a LABEL a person gave it: "friendly" or "grumpy".
# To guess the label of a new (mystery) monster, find the training card that
# is CLOSEST to it and copy that card's label. No rules written by hand!

import math
import turtle

# (fluff, teeth, label) - made-up training cards
TRAINING = [
    (9, 1, "friendly"), (8, 2, "friendly"), (7, 3, "friendly"),
    (6, 1, "friendly"), (8, 4, "friendly"),
    (2, 9, "grumpy"), (3, 8, "grumpy"), (1, 7, "grumpy"),
    (4, 9, "grumpy"), (2, 6, "grumpy"),
]
MYSTERY = [(5, 2), (3, 6), (5, 5)]

SCALE = 36            # pixels per point on the chart
ORIGIN = (-180, -180)  # where (0, 0) goes on the screen


def distance(a, b):
    """Straight-line distance between two cards, using their first two
    numbers (fluff, teeth). Pythagoras: sqrt(dx*dx + dy*dy)."""
    # TODO 1: work out dx (the difference in fluff) and dy (the
    #         difference in teeth), then return math.sqrt(dx * dx + dy * dy)
    return 0


def nearest(training, mystery):
    """The training card closest to the mystery monster."""
    best = training[0]
    # TODO 2: loop over every card in training. If the card is closer to
    #         the mystery than best is, the card becomes the new best.
    return best


def classify(training, mystery):
    """Guess the label: copy the label of the nearest card."""
    return nearest(training, mystery)[2]


# ---------------------------------------------------------------- drawing
def to_screen(fluff, teeth):
    return ORIGIN[0] + fluff * SCALE, ORIGIN[1] + teeth * SCALE


def draw_axes(t):
    x0, y0 = to_screen(0, 0)
    x1, y1 = to_screen(10, 10)
    t.penup(); t.goto(x0, y0); t.pendown(); t.goto(x1, y0)
    t.penup(); t.goto(x0, y0); t.pendown(); t.goto(x0, y1)
    t.penup(); t.goto(x1 - 40, y0 - 30)
    t.write("fluff ->", align="center", font=("Arial", 12, "normal"))
    t.goto(x0 - 10, y1 + 10)
    t.write("teeth", align="center", font=("Arial", 12, "normal"))


def draw_card(t, fluff, teeth, label):
    """Friendly = orange circle with F, grumpy = blue square with G."""
    x, y = to_screen(fluff, teeth)
    t.penup()
    if label == "friendly":
        t.goto(x, y - 12)
        t.fillcolor("#E69F00")
        t.pendown(); t.begin_fill(); t.circle(12); t.end_fill()
        letter = "F"
    else:
        t.goto(x - 11, y - 11)
        t.setheading(0)
        t.fillcolor("#56B4E9")
        t.pendown(); t.begin_fill()
        for _ in range(4):
            t.forward(22); t.left(90)
        t.end_fill()
        letter = "G"
    t.penup(); t.goto(x, y - 8)
    t.write(letter, align="center", font=("Arial", 11, "bold"))


def draw_link(t, training, mystery):
    """A line from the mystery monster to its nearest neighbor."""
    near = nearest(training, mystery)
    t.penup(); t.goto(*to_screen(*mystery)); t.pendown()
    t.pensize(2)
    t.goto(*to_screen(near[0], near[1]))
    t.pensize(1)


def draw_mystery(t, training, mystery):
    """A white circle with '?', and the guess written above it."""
    x, y = to_screen(*mystery)
    t.penup(); t.goto(x, y - 12)
    t.fillcolor("white")
    t.pendown(); t.begin_fill(); t.circle(12); t.end_fill()
    t.penup(); t.goto(x, y - 9)
    t.write("?", align="center", font=("Arial", 13, "bold"))
    t.goto(x, y + 14)
    t.write("guess: " + classify(training, mystery), align="center", font=("Arial", 10, "normal"))


if __name__ == "__main__":
    for m in MYSTERY:
        print(m, "->", classify(TRAINING, m))
    screen = turtle.Screen()
    screen.title("Monster sorter: nearest neighbor")
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    draw_axes(pen)
    for m in MYSTERY:
        draw_link(pen, TRAINING, m)     # lines first, so the cards sit on top
    for card in TRAINING:
        draw_card(pen, *card)
    for m in MYSTERY:
        draw_mystery(pen, TRAINING, m)
    screen.update()
    turtle.done()
