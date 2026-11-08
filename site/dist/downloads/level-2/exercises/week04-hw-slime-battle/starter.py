# Slime Battle
# Use while loops: one that counts hits, one that checks the player's answer.


def hits_needed(health, damage):
    """Return how many hits it takes to bring health down to 0 or less.
    damage must be more than 0."""
    hits = 0
    # TODO 1: while health is more than 0:
    #             take damage away from health
    #             add 1 to hits
    # Careful: if health never goes down, the loop never stops!
    return hits


def ask_yes_no(question):
    """Keep asking until the answer is yes or no, then return it in lower case."""
    # TODO 2: put this in a while True: loop. Only return when the answer
    # is "yes" or "no". Otherwise print "Please type yes or no."
    answer = input(question).lower()
    return answer


if __name__ == "__main__":
    print("A wobbly slime appears! It has 30 health.")
    for sword in [5, 7, 12]:
        print(f"With a sword that does {sword} damage you need {hits_needed(30, sword)} hits.")
    again = ask_yes_no("Fight another slime? (yes/no) ")
    if again == "yes":
        print("Another slime bounces in!")
    else:
        print("You wave goodbye to the slime.")
