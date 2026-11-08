# Loop Square
# A for loop repeats the lines that are pushed in (indented) under it.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#009E73")
t.pensize(3)

for i in range(4):
    t.forward(100)
    # TODO: add the turn here, lined up with the line above

turtle.done()
