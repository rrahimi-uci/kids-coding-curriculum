# TEACHER REFERENCE SOLUTION: Pick a Color
#
# What the program does: it asks for a color name, paints a circle in that
# color, and writes the name under the circle. For a color it does not know,
# it says so and uses black.
# Key ideas: if / elif / else lets the program CHOOSE between several paths,
# and else catches everything the earlier checks did not match.
# Approach: add one elif for "green" and one else for all other answers. Every
# path sets the variable color, so the drawing code below always has a color.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

color_name = input("Pick a color: orange, blue or green? ")

# Python checks these from the top and stops at the first one that is true.
# == means "is the same as". A single = would mean "store a value".
# The words must be small letters: "Blue" is not the same as "blue".
if color_name == "orange":
    color = "#E69F00"
elif color_name == "blue":
    color = "#0072B2"
elif color_name == "green":
    color = "#009E73"
else:
    # Any other answer ends up here, so the program never crashes.
    print("Hmm, I do not know that color. I will use black.")
    color = "#000000"

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

# Common mistakes children make here:
# - Forgetting the colon : at the end of an elif or else line.
# - Using one = instead of two == in the check.
# - Not pushing the line under elif or else in by 4 spaces.
# - Writing the else with no color line. Then color is never set for "pizza"
#   and Python stops with a NameError.
#
# Another correct way: look the color up in a dictionary (a later idea).
#   colors = {"orange": "#E69F00", "blue": "#0072B2", "green": "#009E73"}
#   color = colors.get(color_name, "#000000")
