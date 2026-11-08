# Guess My Number - reference solution
# A while loop keeps going until something changes. ask_number() keeps
# asking until the answer is a real number in range (input validation).
# play() is the game loop: guess, check, repeat - until the guess is right.

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
    while True:
        answer = input(f"Guess a number from {low} to {high}: ")
        if answer.isdigit():                 # only the digits 0-9? Then int() is safe
            number = int(answer)
            if number >= low and number <= high:
                return number
        print(f"Oops! Please type a whole number from {low} to {high}.")


def play(secret, low=1, high=20):
    """Play one game. Return how many guesses it took."""
    tries = 0
    while True:
        guess = ask_number(low, high)
        tries = tries + 1
        result = check_guess(guess, secret)
        print(result)
        if result == "Correct":
            break                             # leave the loop: the game is won
    print(f"You got it in {tries} tries!")
    return tries


if __name__ == "__main__":
    print("I am thinking of a number from 1 to 20...")
    secret = random.randint(1, 20)
    play(secret)
