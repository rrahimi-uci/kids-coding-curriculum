# TEACHER REFERENCE SOLUTION: Slime Battle (Homework 4)
#
# What the program does: it shows how many sword hits it takes to defeat a slime
# with 30 health using three different swords, then asks whether to fight
# another slime and keeps asking until the answer is "yes" or "no".
# Key ideas practiced: a counting while loop and an input-checking while loop.
# Approach: hits_needed() hits the slime again and again, taking away damage and
# counting the hits, until health is 0 or less. ask_yes_no() loops forever on
# purpose and only leaves (with return) when the answer is a valid one.
# Trace for hits_needed(30, 7): health goes 30, 23, 16, 9, 2, -5 after 5 hits.


def hits_needed(health, damage):
    """Return how many hits it takes to bring health down to 0 or less.
    damage must be more than 0."""
    hits = 0
    while health > 0:
        # Something inside the loop MUST change what the loop checks. Here health goes
        # down every time, so the loop ends. If damage were 0, health would never
        # change and the loop would run forever (that is why damage must be more than 0).
        health = health - damage
        hits = hits + 1
    return hits


def ask_yes_no(question):
    """Keep asking until the answer is yes or no, then return it in lower case."""
    while True:
        # .lower() makes "YES" and "Yes" count as "yes".
        answer = input(question).lower()
        if answer == "yes" or answer == "no":
            return answer                     # a valid answer ends the loop and the function
        print("Please type yes or no.")


if __name__ == "__main__":
    print("A wobbly slime appears! It has 30 health.")
    for sword in [5, 7, 12]:
        print(f"With a sword that does {sword} damage you need {hits_needed(30, sword)} hits.")
    again = ask_yes_no("Fight another slime? (yes/no) ")
    if again == "yes":
        print("Another slime bounces in!")
    else:
        print("You wave goodbye to the slime.")


# Common mistakes children make here:
# - Forgetting to change health inside the loop, so the loop never ends (use the
#   red Stop button in Thonny).
# - Forgetting hits = hits + 1, so the answer is always 0.
# - Writing answer == "yes" or "no": Python reads "no" on its own as always true.
#   Each side of "or" needs its own comparison: answer == "yes" or answer == "no".
# - Using while health > 0 but starting hits at 1, so the count is one too high.
#
# Another correct way: "in" checks a whole list at once, and a loop can also be
# written so the answer is asked before the check.
#   if answer in ["yes", "no"]:
#       return answer
