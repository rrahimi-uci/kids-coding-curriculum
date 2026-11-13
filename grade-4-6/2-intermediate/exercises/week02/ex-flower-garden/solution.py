# TEACHER REFERENCE SOLUTION: Flower Garden (Exercise 2.2)
#
# What the program does: it draws three flowers side by side, with 5, 8 and 12
# petals, each with a green stem and a yellow middle.
# Key ideas practiced: function parameters (the same function draws different
# flowers depending on what we hand it) and a function that RETURNS a number.
# Approach: petal_turn() works out the angle between petals (a full circle,
# 360 degrees, shared out equally). draw_flower() goes to the spot (x, y), draws
# the stem, returns to the spot, then draws one petal per petal asked for,
# turning by that angle each time so the petals end up evenly around the circle.

import turtle

PURPLE = "#CC79A7"
SKY = "#56B4E9"
ORANGE = "#E69F00"
YELLOW = "#F0E442"
GREEN = "#009E73"


def petal_turn(petals):
    """Return how many degrees to turn between petals so they go all the way around."""
    # A full turn is 360 degrees. 6 petals means 360 / 6 = 60 degrees each.
    return 360 / petals


def draw_petal(t, size):
    """Draw one filled, leaf-shaped petal and end where it started."""
    # A petal is two curved sides (each an arc of 60 degrees) that meet in a point.
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.end_fill()


def draw_flower(t, x, y, petals, color, size=60):
    """Draw a flower with its center at (x, y)."""
    t.penup()                    # lift the pen so moving does not draw a line
    t.goto(x, y)                 # the flower must start at (x, y), not the same spot
    t.setheading(270)            # face down to draw the stem
    t.pendown()
    t.color(GREEN)
    t.pensize(4)
    t.forward(size * 1.5)
    t.penup()
    t.goto(x, y)                 # go back to the center (x, y), not always (0, 0)
    t.pendown()
    t.pensize(1)
    t.color("black", color)
    for _ in range(petals):      # one petal for each petal asked for, not always 4
        draw_petal(t, size)
        t.left(petal_turn(petals))
    # // divides and drops the remainder: 60 // 3 is 20 (a whole number).
    t.dot(size // 3, YELLOW)     # the middle of the flower


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)                   # 0 is the fastest drawing speed
    t.hideturtle()
    draw_flower(t, -180, 40, 5, PURPLE)
    draw_flower(t, 0, 80, 8, SKY, 70)        # the last number is an optional bigger size
    draw_flower(t, 180, 20, 12, ORANGE, 50)
    turtle.done()


# Common mistakes children make here:
# - Writing return 360 // petals or 360 * petals; it must be division: 360 / petals.
# - Putting t.goto(x, y) after t.pendown(), which draws an ugly line across the
#   screen from the old spot to the new one. Move with the pen up.
# - Leaving the final goto as (0, 0), so all three flower heads pile up in the middle.
# - Using range(petal_turn(petals)) instead of range(petals): the first is the
#   angle, the second is how many times to repeat.
#
# Another correct way: draw the petals with a while loop that counts.
#   count = 0
#   while count < petals:
#       draw_petal(t, size)
#       t.left(petal_turn(petals))
#       count += 1
