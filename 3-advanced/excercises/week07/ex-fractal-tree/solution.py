# Fractal tree - reference solution
# A tree is a trunk with two smaller trees on top of it.
# Each smaller tree is a trunk with two even smaller trees on top... and so on.
# That "a thing made of smaller copies of itself" idea is called a FRACTAL.

import turtle

# Okabe-Ito colour-blind-safe palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

ANGLE = 25      # how far each branch bends (try 15 or 40)
SHRINK = 0.7    # each new branch is 70% as long as the one below it


def branch(t, length, depth):
    """Draw a branch of this length with depth levels of branches on top.
    The turtle ends exactly where it started, facing the same way."""
    if depth == 0:                      # base case: no branch left to draw
        return
    t.pensize(depth)                    # thick trunk, thin twigs
    t.pencolor(PALETTE[depth % len(PALETTE)])
    t.forward(length)                   # draw this branch

    t.left(ANGLE)
    branch(t, length * SHRINK, depth - 1)   # a smaller tree on the left
    t.right(2 * ANGLE)
    branch(t, length * SHRINK, depth - 1)   # a smaller tree on the right
    t.left(ANGLE)                       # face up again

    t.penup()                           # walk back down without drawing
    t.back(length)
    t.pendown()


def draw_forest():
    """Draw three trees with different depths, each labelled."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for x, depth in [(-220, 3), (0, 7), (220, 5)]:
        t.penup()
        t.goto(x, -200)
        t.setheading(90)                # point up
        t.pendown()
        branch(t, 90 if depth == 7 else 60, depth)
        t.penup()
        t.goto(x, -230)
        t.pencolor("black")
        t.write(f"depth {depth}", align="center", font=("Arial", 14, "normal"))


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Fractal forest")
    screen.tracer(0)        # draw everything at once (fast!)
    draw_forest()
    screen.update()
    turtle.done()
