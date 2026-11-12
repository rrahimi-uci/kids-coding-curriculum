"""TEACHER REFERENCE SOLUTION: Exercise 7.3 - Python Flower

What the child sees: 6 squares around one middle point, like a flower.
The turtle ends where it started, looking the same way.
Key idea: a repeat inside a repeat (nested loop), as in Scratch week 1.
The inner loop draws one square; the outer loop draws the square 6 times,
with a small turn between squares.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
# Speed 8 is fast, but children can still watch it draw. 1 is slow, 10 is very fast.
t.speed(8)

# The only change: 2 became 6. Outer repeat: one round per square.
for i in range(6):
    # Inner repeat: pushed in 4 more spaces, so it sits inside the outer
    # one. It draws one whole square every time the outer loop goes round.
    for side in range(4):
        t.forward(80)
        t.left(90)
    # This turn is inside the outer loop but NOT inside the inner one:
    # it happens once after each square. 60 is the hexagon number on the
    # turn card, so 6 squares bring the turtle all the way round.
    t.left(60)

turtle.done()

# Other answers the tests accept: range(4) with t.left(90) (a window of
# 4 squares), or range(12) with t.left(30) if a child tries it.
# Common mistakes:
# - Changing the 4 in the inner range instead of the 2: the "squares" get
#   more sides and overlap in a tangle. Change the outer number.
# - Pushing t.left(60) in further, into the inner loop: the corners are
#   no longer quarter turns, so no squares appear.
