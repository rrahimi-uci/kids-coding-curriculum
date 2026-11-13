# TEACHER REFERENCE SOLUTION: Mood Meter (Exercise 1.2)
#
# What the program does: it asks how much energy the child has (0 to 10) and
# whether they had a snack, picks a mood word, and draws a colored bar whose
# length shows the energy, with the mood written above it.
# Key ideas practiced: if / elif / else, and the three helper words "and",
# "or" and "not".
# Approach: mood_for() checks the strictest rule first (energy 8+ AND a snack),
# then the looser one (energy 5+ OR a snack), and everything else falls to
# "Recharge time". The drawing code was given; the child only writes the deciding.

import turtle

# Colors chosen so people with color blindness can still tell them apart.
GREEN = "#009E73"
ORANGE = "#E69F00"
VERMILLION = "#D55E00"


def mood_for(energy, had_snack):
    """Choose a mood word from energy (0 to 10) and had_snack (True/False)."""
    # Order matters: Python stops at the first rule that is true. The strict
    # rule must come first, or a super charged child would get "Ready to play".
    if energy >= 8 and had_snack:          # both must be true
        return "Super charged"
    elif energy >= 5 or had_snack:         # only one of them needs to be true
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
    # A rectangle: long side, short side, long side, short side. The long side
    # is energy * 30, so more energy draws a longer bar.
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
    # .lower() makes "YES" and "Yes" work too. The comparison gives True or False.
    had_snack = snack_answer.lower() == "yes"
    mood = mood_for(energy, had_snack)
    print(f"Your mood: {mood}")
    if not had_snack:                      # "not" flips False into True
        print("Tip: a healthy snack and a glass of water help your brain.")
    t = turtle.Turtle()
    draw_meter(t, energy, mood)
    turtle.done()


# Common mistakes children make here:
# - Writing "energy >= 8 and >= 5" or "energy >= 5 or 8": each side of and / or
#   must be a full question on its own.
# - Putting the "Ready to play" rule before the "Super charged" rule, so the
#   strict rule is never reached.
# - Writing "if not had_snack" without the colon, or using "== not"; "not" goes
#   directly in front of the True/False value.
# - Using "and" in TODO 2 where the README says "or" (energy 2 with a snack must
#   still be "Ready to play").
#
# Another correct way: test the snack first with a nested if.
#   if had_snack and energy >= 8:
#       return "Super charged"
#   if had_snack or energy >= 5:
#       return "Ready to play"
#   return "Recharge time"
