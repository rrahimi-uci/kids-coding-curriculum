"""TEACHER REFERENCE SOLUTION: Exercise 6.1 - Hello, Turtle!

What the child sees: the turtle walks to the right and draws one long line,
then makes a quarter turn and looks up.
Key idea: each Python line is one Scratch block written as words, and the
number inside the brackets is the white oval we change in Scratch.
"""

# Get the turtle toolbox. This line is in every turtle program.
import turtle

# Make one turtle and call it t. Every drawing line starts with "t."
t = turtle.Turtle()
# Show a little turtle instead of an arrow, so children can watch it walk.
t.shape("turtle")

# The only change: 50 became 150. Like "move 150 steps" in Scratch.
# Any whole number from 100 to 300 is right; much more than 300 walks
# out of the window.
t.forward(150)
# A quarter turn is 90, like "turn left 90 degrees" in Scratch.
t.left(90)

# Keep the window open at the end. Without it the window can close at once.
turtle.done()

# Common mistakes:
# - Deleting the brackets or the dot while changing the number:
#   t.forward150 or t.forward(150 gives red text. Put them back.
# - Typing the new number in the Shell (bottom part) instead of the Editor.
# - Forgetting to press Run again after the change, so nothing looks new.
