"""TEACHER REFERENCE SOLUTION: Exercise 7.2 - The Lonely Turn (bug hunt)

What the child sees: after the fix, a closed square with 4 sides of 80.
Before the fix: one long straight line (4 x 80 steps), then a single turn.
Key idea: only the lines pushed in under "for" are inside the repeat. A line
that is not pushed in runs once, after the repeat has finished.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(80)
    # THE FIX: this line had no spaces in front of it, so it was outside the
    # repeat and ran only once, at the very end. Now it is pushed in by
    # 4 spaces (one press of the Tab key in Thonny), lined up under
    # t.forward(80), so the turtle turns at every corner.
    t.left(90)

turtle.done()

# Common mistakes:
# - Pushing the line in by 2 or 3 spaces: red text, "unindent does not match
#   any outer indentation level". Line it up exactly under t.forward(80).
# - Pushing in turtle.done() as well: the window waits after the first side.
#   turtle.done() always starts at the left edge.
# - Changing the numbers instead of the spaces. The numbers were right.
# Link to Scratch: the turn block was below the repeat, not inside its mouth.
