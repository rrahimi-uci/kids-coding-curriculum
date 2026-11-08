# Guess My Number
# check_guess() is done. Finish the two while loops.

import random


def check_guess(guess, secret):
    """Return "Too low", "Too high" or "Correct"."""
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else:
        return "Correct"


def ask_number(low, high):
    """Keep asking until the player types a whole number from low to high, then return it."""
    # TODO 2: typing "banana" crashes the game! Put this in a  while True:  loop.
    # Only return the number if answer.isdigit() is True AND it is from low to high.
    # Otherwise print a friendly "Please type a whole number..." message.
    answer = input(f"Guess a number from {low} to {high}: ")
    return int(answer)


def play(secret, low=1, high=20):
    """Play one game. Return how many guesses it took."""
    tries = 0
    while True:
        guess = ask_number(low, high)
        # TODO 1: add 1 to tries here.
        result = check_guess(guess, secret)
        print(result)
        # TODO 3: if result is "Correct", break out of the loop.
        #         (Until you do, the game never ends! Press the red Stop button.)
    print(f"You got it in {tries} tries!")
    return tries


if __name__ == "__main__":
    print("I am thinking of a number from 1 to 20...")
    secret = random.randint(1, 20)
    play(secret)
