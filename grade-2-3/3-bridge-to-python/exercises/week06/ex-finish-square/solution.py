"""TEACHER REFERENCE SOLUTION: Exercise 6.2 - Finish the Square

What the child sees: the turtle draws a closed square with 4 equal sides and
ends where it started.
Key idea: the computer runs the lines in order, top to bottom, like a Scratch
script under the green flag. A square is "forward, quarter turn" four times.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

# Sides 1 to 3 were already in the starter.
t.forward(100)   # side 1
t.left(90)
t.forward(100)   # side 2
t.left(90)
t.forward(100)   # side 3
t.left(90)
# The one new line the child types: side 4 closes the square.
t.forward(100)   # side 4
# Optional second new line: turn once more, so the turtle looks the same
# way as at the start (to the right). The square is finished without it.
t.left(90)

turtle.done()

# Common mistakes:
# - Typing forwad or Forward: Python shows red text and names the line.
#   Compare the new line with side 3, letter by letter.
# - Missing the closing bracket: the red text says "'(' was never closed".
# - A different number, like t.forward(10): the square does not close.
# - Spaces at the start of the new line: Python says "unexpected indent".
#   The new line starts at the left edge, like the other lines.
# Next week the same square is written with a loop: for i in range(4).
