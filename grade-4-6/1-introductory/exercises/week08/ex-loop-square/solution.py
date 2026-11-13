# TEACHER REFERENCE SOLUTION: Loop Square
#
# What the program does: the turtle draws a closed square using a loop that
# repeats 4 times.
# Key ideas: a for loop repeats the lines that are pushed in (indented) under
# it, and a square needs both a move AND a turn each time.
# Approach: the starter loop only moved forward, so the turtle went in a
# straight line. We add t.left(90) inside the loop, lined up with t.forward.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#009E73")
t.pensize(3)

# range(4) means "do this 4 times". The name i is just a counter that we do
# not need to use here.
for i in range(4):
    t.forward(100)
    # The turn is pushed in by 4 spaces, so it is INSIDE the loop and happens
    # after every side. If it were not pushed in, it would only run once at
    # the very end, and the turtle would draw a straight line four times.
    t.left(90)

turtle.done()

# Common mistakes children make here:
# - Not pushing t.left(90) in by 4 spaces, so it is outside the loop.
# - Pushing it in by a different number of spaces, which gives a red
#   IndentationError.
# - Writing the turn above t.forward(100). The square still closes, but the
#   turtle turns before its first side, so it starts in a different direction.
# - Changing the 4 but not the 90, so the shape does not close. The turn
#   should always be 360 divided by the number of sides.
#
# Another correct way: a while loop with a counter (a later idea).
#   sides_drawn = 0
#   while sides_drawn < 4:
#       t.forward(100)
#       t.left(90)
#       sides_drawn = sides_drawn + 1
