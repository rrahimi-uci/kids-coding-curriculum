# Flower Garden - reference solution
# draw_flower() has parameters (where, how many petals, which color), so one
# function draws many different flowers. petal_turn() RETURNS a number that
# draw_flower() uses.

import turtle

PURPLE = "#CC79A7"
SKY = "#56B4E9"
ORANGE = "#E69F00"
YELLOW = "#F0E442"
GREEN = "#009E73"


def petal_turn(petals):
    """Return how many degrees to turn between petals so they go all the way round."""
    return 360 / petals


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
    t.goto(x, y)
    t.setheading(270)            # face down to draw the stem
    t.pendown()
    t.color(GREEN)
    t.pensize(4)
    t.forward(size * 1.5)
    t.penup()
    t.goto(x, y)                 # back to the center for the petals
    t.pendown()
    t.pensize(1)
    t.color("black", color)
    for _ in range(petals):
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
