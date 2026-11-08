# Slime Battle - reference solution
# hits_needed() uses a while loop that stops when the slime's health
# reaches 0. Something inside the loop MUST change (health goes down),
# or the loop would never end.


def hits_needed(health, damage):
    """Return how many hits it takes to bring health down to 0 or less.
    damage must be more than 0."""
    hits = 0
    while health > 0:
        health = health - damage
        hits = hits + 1
    return hits


def ask_yes_no(question):
    """Keep asking until the answer is yes or no, then return it in lower case."""
    while True:
        answer = input(question).lower()
        if answer == "yes" or answer == "no":
            return answer
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
