# Mood Meter
# The drawing part is done for you. Your job is the DECIDING part:
# finish mood_for() using "and" and "or", then use "not" at the bottom.

import turtle

GREEN = "#009E73"
ORANGE = "#E69F00"
VERMILLION = "#D55E00"


def mood_for(energy, had_snack):
    """Choose a mood word from energy (0 to 10) and had_snack (True/False)."""
    # TODO 1: "Super charged" needs energy 8 or more AND a snack.
    if energy >= 8:
        return "Super charged"
    # TODO 2: add an elif: energy 5 or more OR a snack gives "Ready to play".
    else:
        return "Recharge time"


def colour_for(mood):
    """Pick a colour for the bar. The words are drawn too, so colour is never the only clue."""
    if mood == "Super charged":
        return GREEN
    elif mood == "Ready to play":
        return ORANGE
    else:
        return VERMILLION


def draw_meter(t, energy, mood):
    """Draw an outline box with a filled bar inside: 30 pixels per energy point."""
    t.hideturtle()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.color("black", colour_for(mood))
    t.pensize(2)
    t.begin_fill()                      # the filled bar
    for side in [energy * 30, 40, energy * 30, 40]:
        t.forward(side)
        t.left(90)
    t.end_fill()
    for side in [300, 40, 300, 40]:     # the outline of the whole meter (0 to 10)
        t.forward(side)
        t.left(90)
    t.penup()
    t.goto(-150, 60)
    t.write(f"Mood: {mood}", font=("Arial", 20, "bold"))
    t.goto(-150, -40)
    t.write(f"Energy: {energy} out of 10", font=("Arial", 14, "normal"))


if __name__ == "__main__":
    energy = int(input("How much energy do you have? (0 to 10) "))
    snack_answer = input("Did you have a snack? (yes/no) ")
    had_snack = snack_answer.lower() == "yes"      # a bool: True or False
    mood = mood_for(energy, had_snack)
    print(f"Your mood: {mood}")
    # TODO 3: if NOT had_snack, print a friendly tip about having a snack.
    t = turtle.Turtle()
    draw_meter(t, energy, mood)
    turtle.done()
