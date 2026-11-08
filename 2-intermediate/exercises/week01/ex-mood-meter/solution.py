# Mood Meter - reference solution
# Ask how much energy you have and whether you had a snack, choose a mood
# with if / elif / else plus "and" / "or" / "not", then draw a meter.

import turtle

GREEN = "#009E73"
ORANGE = "#E69F00"
VERMILLION = "#D55E00"


def mood_for(energy, had_snack):
    """Choose a mood word from energy (0 to 10) and had_snack (True/False)."""
    if energy >= 8 and had_snack:
        return "Super charged"
    elif energy >= 5 or had_snack:
        return "Ready to play"
    else:
        return "Recharge time"


def color_for(mood):
    """Pick a color for the bar. The words are drawn too, so color is never the only clue."""
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
    t.color("black", color_for(mood))
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
    if not had_snack:
        print("Tip: a healthy snack and a glass of water help your brain.")
    t = turtle.Turtle()
    draw_meter(t, energy, mood)
    turtle.done()
