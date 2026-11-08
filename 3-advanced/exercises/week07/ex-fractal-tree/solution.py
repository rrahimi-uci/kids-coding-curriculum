# TEACHER REFERENCE SOLUTION: Exercise 7.2 - Fractal tree
#
# What the program does: draws a forest of three trees (depth 3, 7 and 5).
# Every branch splits into two shorter branches, again and again.
# Key ideas: recursion that calls itself TWICE, a base case (depth 0), and
# leaving the turtle exactly where it started so the caller can carry on.
# Approach: branch() draws a trunk, turns left and draws a smaller tree,
# turns right and draws another smaller tree, then turns back and walks
# down to where it began. Each smaller tree is one level shallower, so the
# calls eventually reach depth 0 and stop.
# A tree of depth d has 2**d - 1 branches: 1, 3, 7, 15 ...

import turtle

# Okabe-Ito color-blind-safe palette
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

    # The turns must add up to zero (left 25, right 50, left 25) so that the
    # turtle faces the same way again after both smaller trees are drawn.
    t.left(ANGLE)
    branch(t, length * SHRINK, depth - 1)   # a smaller tree on the left
    t.right(2 * ANGLE)                  # swing from "left of up" to "right of up"
    branch(t, length * SHRINK, depth - 1)   # a smaller tree on the right
    t.left(ANGLE)                       # face up again

    # Walk back down to the start of this branch without drawing, so the
    # caller finds the turtle exactly where it left it.
    t.penup()
    t.back(length)
    t.pendown()


def draw_forest():
    """Draw three trees with different depths, each labeled."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for x, depth in [(-220, 3), (0, 7), (220, 5)]:
        t.penup()
        t.goto(x, -200)
        t.setheading(90)                # point up
        t.pendown()
        branch(t, 90 if depth == 7 else 60, depth)  # the tallest tree starts longer
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


# Common mistakes children make here:
#   - Turning left ANGLE and then right only ANGLE (not 2 * ANGLE), so the
#     second tree grows straight up instead of to the right.
#   - Forgetting the last left(ANGLE), so the turtle ends tilted and the
#     tree looks lopsided after every level.
#   - Calling branch with depth instead of depth - 1, which never reaches
#     the base case and ends in a RecursionError.
#
# Another correct way: loop over the two directions with a for loop.
#   for turn in (ANGLE, -2 * ANGLE):
#       t.left(turn)
#       branch(t, length * SHRINK, depth - 1)
#   t.left(ANGLE)
