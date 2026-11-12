"""TEACHER REFERENCE SOLUTION: My Big Build, Python path.

The postcard "A House in the Sun": a long green ground
line, an orange house with a blue door, a purple roof,
a gold sun and a row of three flowers.

Key ideas: every shape is a for loop (square: 4 sides and
a quarter turn of 90; triangle: turn card 120; hexagon:
turn card 60). The turtle walks between shapes with the
pen up, using only forward, left and right, so there are
no positions and no negative numbers. The flower is a
def (the stretch path: a Python "My Block"), used 3 times.

It started from project/starter/postcard.py: the house
and roof are the starter's square and triangle, made
bigger (120) with new colors. The ground, door, sun and
flowers were added one at a time, with Run after each.

SMOKE: run
"""

import turtle

# ===== PART 1: THE TURTLE =====
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)          # faster than the starter: lots to draw


# ===== PART 2: MY OWN BLOCK (THE STRETCH PATH) =====
def flower():
    """Draw one flower: a green stem, purple petals on top.

    The turtle starts on the ground facing right, and it
    ends in the same place, facing right again.
    """
    t.color("green")
    t.left(90)              # face up
    t.forward(40)           # the stem
    # Step 10 to the left with the pen up, so the petals
    # sit in the middle of the stem.
    t.left(90)
    t.penup()
    t.forward(10)
    t.left(180)             # a half turn: face right
    t.pendown()
    t.color("purple")
    for i in range(6):      # a hexagon: turn card 60
        t.forward(20)
        t.left(60)
    # Walk back down the stem with the pen up.
    t.penup()
    t.forward(10)
    t.right(90)             # face down
    t.forward(40)
    t.left(90)              # face right
    t.pendown()


# ===== PART 3: THE GROUND =====
# Walk left with the pen up, turn round, draw one line.
t.penup()
t.left(180)
t.forward(250)
t.left(180)
t.pendown()
t.color("green")
t.pensize(8)
t.forward(500)

# ===== PART 4: THE HOUSE (the starter's square) =====
# Turn round and walk back to the house corner, pen up.
t.penup()
t.left(180)
t.forward(450)
t.left(180)
t.pendown()
t.color("orange")
t.pensize(5)
for i in range(4):          # 4 sides, a quarter turn each
    t.forward(120)
    t.left(90)

# ===== PART 5: THE DOOR (a rectangle) =====
# Long side, short side, two times.
t.penup()
t.forward(45)               # 45 + 30 + 45 = 120: centered
t.pendown()
t.color("blue")
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)

# ===== PART 6: THE ROOF (the starter's triangle) =====
# Back to the corner, then up the wall, pen up.
t.penup()
t.left(180)
t.forward(45)
t.right(90)                 # face up
t.forward(120)
t.right(90)                 # face right
t.pendown()
t.color("purple")
for i in range(3):          # turn card: 120 for a triangle
    t.forward(120)
    t.left(120)

# ===== PART 7: THE SUN (a hexagon in the sky) =====
t.penup()
t.forward(330)              # right, over the roof
t.left(90)
t.forward(60)               # and a little higher
t.right(90)
t.pendown()
t.color("gold")
t.pensize(8)
for i in range(6):          # a hexagon again: turn card 60
    t.forward(40)
    t.left(60)

# ===== PART 8: THE FLOWERS (my own block, 3 times) =====
# Walk down to the ground and left of the sun, pen up.
t.penup()
t.right(90)                 # face down
t.forward(180)
t.right(90)                 # face left
t.forward(170)
t.left(180)                 # a half turn: face right
t.pendown()
t.pensize(5)
for i in range(3):
    flower()
    t.penup()
    t.forward(50)           # space between the flowers
    t.pendown()

t.hideturtle()              # a finished card has no turtle
turtle.done()
