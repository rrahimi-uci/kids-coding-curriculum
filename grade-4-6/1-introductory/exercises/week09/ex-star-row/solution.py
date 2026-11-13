# TEACHER REFERENCE SOLUTION: How Many Stars?
#
# What the program does: it asks how many stars to draw (1 to 10), keeps the
# answer sensible, then draws a row of that many yellow stars.
# Key ideas: comparisons (> and <), if / elif / else, and changing a variable
# so a silly answer becomes a good one.
# Approach: after turning the answer into a number, check if it is too big or
# too small. Fix the number and tell the user. Otherwise say "Coming right up!".

import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("#000000", "#F0E442")   # black outline, yellow inside

answer = input("How many stars? (1 to 10) ")
stars = int(answer)             # input() gives text, so make it a number

# Only one of these three paths runs. The order matters little here because
# a number cannot be both bigger than 10 and smaller than 1.
if stars > 10:
    # More than 10 stars would run off the edge of the screen.
    print("Wow, that is a lot! Only 10 fit, so I will draw 10.")
    stars = 10
elif stars < 1:
    # Zero or a negative number would draw nothing at all.
    print("No stars is too dark. I will draw 1.")
    stars = 1
else:
    print("Coming right up!")

# Draw a row of stars, starting on the left
t.penup()
t.goto(-300, 0)
for i in range(stars):
    t.pendown()
    t.begin_fill()
    for point in range(5):
        t.forward(50)
        t.right(144)    # 144 degrees makes the points of a 5-pointed star
    t.end_fill()
    t.penup()
    t.forward(60)       # move along to the next star

turtle.done()

# Common mistakes children make here:
# - Setting the number but not printing a message, so the user is not told.
# - Writing stars = 10 as stars == 10. Two == only asks a question and does
#   not change anything.
# - Mixing up > and <. Say it out loud: "if stars is greater than 10".
# - Using a second if instead of elif. It still works here, but the else part
#   would then also run after "stars > 10" and print "Coming right up!" too.
#
# Another correct way: min() and max() keep a number between two limits, but
# they do not let us print a message for each case.
#   stars = max(1, min(10, stars))
