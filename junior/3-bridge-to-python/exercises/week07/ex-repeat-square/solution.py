"""TEACHER REFERENCE SOLUTION: Exercise 7.1 - Repeat 4

What the child sees: a closed square with 4 equal sides, drawn by a loop.
Key idea: "for i in range(4):" is Scratch's "repeat 4". The lines pushed in
by 4 spaces under it are the blocks inside the repeat's mouth.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

# The only change: 2 became 4. range(4) means "do this 4 times".
# The i is a name Python needs after "for". We do not use it here.
for i in range(4):
    # Both lines are pushed in by 4 spaces, so both are inside the repeat:
    # one side and one quarter turn, 4 times.
    t.forward(100)
    t.left(90)

turtle.done()

# Extra from the README (also correct, and the tests accept it):
# a triangle with the turn card: range(3) and t.left(120).
# Common mistakes:
# - Deleting the colon at the end of the for line: red text, "expected ':'".
# - Changing 2 to 4 inside the comment instead of inside range( ).
# - Changing range(3) for a triangle but keeping t.left(90): the shape
#   does not close. Read the turn from the turn card.
