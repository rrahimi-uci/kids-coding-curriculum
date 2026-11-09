# Flower Garden
# draw_flower() should draw a flower anywhere, with any number of petals.
# Right now every flower lands in the same spot and has 4 petals. Fix it!

import turtle

PURPLE = "#CC79A7"
SKY = "#56B4E9"
ORANGE = "#E69F00"
YELLOW = "#F0E442"
GREEN = "#009E73"


def petal_turn(petals):
    """Return how many degrees to turn between petals so they go all the way around."""
    # TODO 1: a full turn is 360 degrees. Share it out between the petals.
    return 90


def draw_petal(t, size):
    """Draw one filled, leaf-shaped petal and end where it started."""
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.end_fill()


def draw_flower(t, x, y, petals, color, size=60):
    """Draw a flower with its center at (x, y)."""
    t.penup()
    # TODO 2: go to (x, y) here, before drawing the stem.
    t.setheading(270)            # face down to draw the stem
    t.pendown()
    t.color(GREEN)
    t.pensize(4)
    t.forward(size * 1.5)
    t.penup()
    t.goto(0, 0)                 # TODO 3: back to the center: (x, y), not (0, 0)
    t.pendown()
    t.pensize(1)
    t.color("black", color)
    # TODO 4: repeat for the number of petals, not always 4.
    for _ in range(4):           # _ is a name for a loop counter we do not use
        draw_petal(t, size)
        t.left(petal_turn(petals))
    t.dot(size // 3, YELLOW)     # the middle of the flower


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_flower(t, -180, 40, 5, PURPLE)
    draw_flower(t, 0, 80, 8, SKY, 70)
    draw_flower(t, 180, 20, 12, ORANGE, 50)
    turtle.done()
