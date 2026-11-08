# TEACHER REFERENCE SOLUTION: Loop Fixer
#
# What the program does: it draws a closed blue square and a closed orange
# 5-pointed star.
# Key ideas: the number inside range() says how many times a loop repeats, and
# only the lines pushed in (indented) under the for line are repeated.
# Approach: the starter has 2 loop bugs. Both are marked FIX 1 and FIX 2.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

# A blue square
t.penup()
t.goto(-200, -50)
t.pendown()
t.color("#0072B2")
# FIX 1: was range(3). The loop only drew 3 sides, so the square was open.
# A square has 4 sides, so the loop must repeat 4 times.
for i in range(4):
    t.forward(100)
    t.left(90)

# An orange star with 5 points
t.penup()
t.goto(50, 0)
t.pendown()
t.color("#E69F00")
for i in range(5):
    t.forward(150)
    # FIX 2: was not pushed in, so it sat outside the loop and ran only once
    # after all 5 lines. The turtle drew a straight line. Pushed in by
    # 4 spaces, it turns after every line. 5 turns x 144 = 720, two full
    # circles, which is what makes the points of a star.
    t.right(144)

turtle.done()

# Common mistakes children make here:
# - Fixing the square by adding extra lines instead of changing the 3 to 4.
# - Pushing t.right(144) in by a different number of spaces than t.forward(150).
#   Both lines must line up exactly.
# - Changing 144 to 72 (360 / 5). That draws a pentagon, not a star.
# - Fixing only one of the two bugs. Run the program and watch both shapes.
