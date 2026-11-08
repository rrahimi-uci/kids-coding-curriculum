# TEACHER REFERENCE SOLUTION: Guess My Number (Exercise 4.1)
#
# What the program does: the computer picks a secret number from 1 to 20 and the
# player guesses until they are right. Each guess gets "Too low", "Too high" or
# "Correct", and at the end the game says how many tries it took.
# Key ideas practiced: two while loops (a game loop and an input-checking loop),
# a counter variable, break, and input validation (not trusting what is typed).
# Approach: play() is the game loop: ask, count, check, repeat until the guess is
# right. ask_number() is the checking loop: it keeps asking until the answer is
# digits only AND inside the range, so "banana" or 99 can never crash the game.
# The bug hunt: the starter loop never ended because nothing inside it ever
# stopped it, so we add a counter (TODO 1) and a break (TODO 3).

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
    while True:                              # keep asking until we return a good answer
        answer = input(f"Guess a number from {low} to {high}: ")
        # Check isdigit() BEFORE int(). int("banana") would crash, so we only
        # convert when the text is made of digits 0-9 only.
        if answer.isdigit():
            number = int(answer)
            if number >= low and number <= high:
                return number                # a good answer: leave the function
        # We only get here when the answer was not good, so scold kindly and loop again.
        print(f"Oops! Please type a whole number from {low} to {high}.")


def play(secret, low=1, high=20):
    """Play one game. Return how many guesses it took."""
    tries = 0
    while True:
        guess = ask_number(low, high)
        # FIX 1: the starter never counted guesses, so it could not report them.
        tries = tries + 1
        result = check_guess(guess, secret)
        print(result)
        if result == "Correct":
            # FIX 2: without a break the loop never ended, even after a correct guess.
            break                             # leave the loop: the game is won
    print(f"You got it in {tries} tries!")
    return tries


if __name__ == "__main__":
    print("I am thinking of a number from 1 to 20...")
    secret = random.randint(1, 20)            # both ends are included: 1 and 20
    play(secret)


# Common mistakes children make here:
# - Putting tries = 0 inside the loop, so the counter resets and always reports 1.
# - Using break outside the if (for example on the same level as print(result)),
#   which ends the game after the very first guess.
# - Calling int(answer) before checking isdigit(), so "banana" still crashes.
# - Forgetting that negative numbers like "-5" are not digits: isdigit() is False
#   for them, which is fine here because they are out of range anyway.
#
# Another correct way: try / except catches the crash instead of preventing it.
#   try:
#       number = int(answer)
#   except ValueError:
#       number = None
#   if number is not None and low <= number <= high:
#       return number
