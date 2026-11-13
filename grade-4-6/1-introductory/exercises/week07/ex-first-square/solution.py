# TEACHER REFERENCE SOLUTION: My First Square
#
# What the program does: the turtle draws a square with four equal sides
# and finishes exactly where it started.
# Key ideas: a program is a list of steps, and a square is the same two steps
# ("go forward, turn a corner") done four times.
# Approach: the starter already draws side 1, so we copy the same two lines
# three more times, one block for each TODO.

import turtle

t = turtle.Turtle()
t.shape("turtle")

# Side 1 (this part came with the starter).
t.forward(100)
t.left(90)

# Side 2. Every side uses 100 steps, so all four sides are the same length.
t.forward(100)
t.left(90)

# Side 3.
t.forward(100)
t.left(90)

# Side 4. The last turn of 90 degrees makes the full turn add up to 360,
# so the turtle ends up facing the way it began.
t.forward(100)
t.left(90)

turtle.done()

# Common mistakes children make here:
# - Using a different number on one side, so the shape is not a square.
# - Turning a different angle, like 45 or 60. A square corner is 90 degrees.
# - Forgetting one of the four sides, so the square has a gap.
# - Mixing left and right turns, which makes a zigzag instead of a square.
#
# Another correct way: a loop repeats the two steps for us (week 8 idea).
#   for side in range(4):
#       t.forward(100)
#       t.left(90)
