# Triangle Time - reference solution
# Three equal sides, turning 120 degrees each time (3 x 120 = 360).

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#CC79A7")
t.pensize(3)

t.forward(120)
t.left(120)

t.forward(120)
t.left(120)

t.forward(120)
t.left(120)

turtle.done()
