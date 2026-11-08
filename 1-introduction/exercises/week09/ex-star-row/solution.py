# How Many Stars? - reference solution
# Ask a number, check it is sensible, then draw that many stars.

import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("#000000", "#F0E442")   # black outline, yellow inside

answer = input("How many stars? (1 to 10) ")
stars = int(answer)

if stars > 10:
    print("Wow, that is a lot! Only 10 fit, so I will draw 10.")
    stars = 10
elif stars < 1:
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
        t.right(144)
    t.end_fill()
    t.penup()
    t.forward(60)       # move along to the next star

turtle.done()
