# Pick a Color
# The program asks a question, then CHOOSES what to do with if / elif / else.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

color_name = input("Pick a color: orange, blue or green? ")

if color_name == "orange":
    color = "#E69F00"
elif color_name == "blue":
    color = "#0072B2"
# TODO: add an elif for "green" (use "#009E73")
# TODO: add an else: print a friendly message and use black "#000000"

# Paint a circle in the chosen color
t.color(color)
t.begin_fill()
t.circle(80)
t.end_fill()

# Write the color name under the circle, so color is not the only clue
t.penup()
t.goto(0, -40)
t.write(color_name, align="center", font=("Arial", 20, "bold"))

turtle.done()
