"""TEACHER REFERENCE SOLUTION: Exercise 8.2 - Two-Color Flower

What the child sees: 6 squares around a middle point, like the week 7
flower, but the squares take turns: purple, gold, purple, gold...
Key idea: change a working program to make it your own, and say whose idea
you started from (the credit line at the top).
"""
# Made by: the Kids Coding course.
# Changed by: Zoe
# (The child types a nickname here, never a full name.)

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(8)

# The outer loop goes round 3 times. Each time it draws TWO squares,
# one in each color, so we get 6 squares in all.
for i in range(3):
    t.color("purple")         # first color
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)

    # The change: the second "purple" became "gold".
    t.color("gold")           # second color
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)

turtle.done()

# Notice that the square loop is written twice. The week 8 stretch
# (Exercise 8.3) gives it a name with def, like a Scratch My Block.
# Common mistakes:
# - Changing the first color, so both are still the same.
# - A color typo like "gld": red text ending "bad color string: gld".
# - Gold and orange look alike to some people; purple and gold are clear to
#   tell apart for almost everyone.
