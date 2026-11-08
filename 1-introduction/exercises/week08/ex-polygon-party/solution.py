# TEACHER REFERENCE SOLUTION: Polygon Party
#
# What the program does: it draws three closed shapes in a row: an orange
# triangle, a sky-blue square and a green hexagon.
# Key ideas: every shape gets its own for loop, and the turn at each corner is
# always 360 divided by the number of sides.
# Approach: copy the triangle loop from the starter, then change the number of
# repeats, the turn and (for the hexagon) the side length.

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
# The turtle jumps to a new spot with the pen up, so no line joins the shapes.
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("#56B4E9")
for i in range(4):
    t.forward(100)
    t.left(90)

# Shape 3: a hexagon (6 sides, turn 360 / 6 = 60)
# The sides are shorter (60) so the wide hexagon still fits on the screen.
t.penup()
t.goto(150, 0)
t.pendown()
t.color("#009E73")
for i in range(6):
    t.forward(60)
    t.left(60)

turtle.done()

# Common mistakes children make here:
# - Using the wrong turn, such as 60 for the square. The shape then does not
#   close. The turn is 360 divided by the number of sides.
# - Forgetting that the number in range() is the number of sides.
# - Forgetting t.pendown(), so the new shape is not drawn at all.
# - Using the same color for two shapes. The checker tells shapes apart by
#   color, so each shape needs its own color.
#
# Another correct way: one loop over a list of (sides, length, color) groups
# would work too, but it uses ideas from a later week.
