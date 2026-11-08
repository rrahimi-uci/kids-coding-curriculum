# Polygon Party - reference solution
# Every shape gets its own loop. The turn is always 360 / number of sides.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

# Shape 1: a triangle (3 sides, turn 360 / 3 = 120)
t.penup()          # lift the pen: move without drawing
t.goto(-250, 0)
t.pendown()        # put the pen back down
t.color("#E69F00")
for i in range(3):
    t.forward(100)
    t.left(120)

# Shape 2: a square (4 sides, turn 360 / 4 = 90)
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("#56B4E9")
for i in range(4):
    t.forward(100)
    t.left(90)

# Shape 3: a hexagon (6 sides, turn 360 / 6 = 60)
t.penup()
t.goto(150, 0)
t.pendown()
t.color("#009E73")
for i in range(6):
    t.forward(60)
    t.left(60)

turtle.done()
