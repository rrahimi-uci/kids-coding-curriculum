# TEACHER REFERENCE SOLUTION: Triangle Time
#
# What the program does: the turtle draws a triangle with three equal sides
# and finishes where it started.
# Key ideas: the turtle turns once at each corner, and all the turns of a
# closed shape add up to one full circle, 360 degrees.
# Approach: the starter draws side 1. We divide 360 by the 3 corners to get
# 120 degrees, then repeat "forward, left" for sides 2 and 3.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#CC79A7")
t.pensize(3)

# Side 1 (this part came with the starter).
t.forward(120)
t.left(120)

# Side 2. 120 steps again so the sides are equal.
t.forward(120)
t.left(120)

# Side 3. 3 turns x 120 degrees = 360, so the turtle faces its first way again.
t.forward(120)
t.left(120)

turtle.done()

# Common mistakes children make here:
# - Turning 60 degrees. That is the angle INSIDE the triangle, but the turtle
#   needs the outside turn, which is 120 degrees.
# - Using a different length on one side, so the sides are not equal.
# - Adding only one more side, so the triangle is not closed.
#
# Another correct way: a loop repeats the two steps (week 8 idea).
#   for side in range(3):
#       t.forward(120)
#       t.left(120)
