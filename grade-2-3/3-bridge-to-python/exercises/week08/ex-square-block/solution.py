"""TEACHER REFERENCE SOLUTION: Exercise 8.3 - My Square Block (stretch)

What the child sees: 4 squares that touch in the middle, like a window with
4 panes. The turtle ends in the middle, looking the same way.
Key idea: def gives a group of lines a name, like a Scratch My Block.
"define square" is def square():, and the block itself is square().
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)


# "def square():" is like Scratch's pink "define square" hat block.
# Nothing is drawn here yet: Python only learns what square means.
def square():
    # The lines pushed in under def are the blocks under "define square".
    for side in range(4):
        t.forward(60)
        t.left(90)


# The only change: 1 became 4. Each round uses the block once, then makes
# a quarter turn, so the next square goes in the next corner.
for i in range(4):
    square()
    t.left(90)

turtle.done()

# Try this with the child: change 60 inside def square() to 100. All four
# squares get bigger at once, because they all use the same block.
# Common mistakes:
# - Writing square without the brackets: nothing is drawn, and no red text.
#   The brackets mean "use the block now".
# - Changing the 4 inside def square() instead of the 1 at the bottom.
