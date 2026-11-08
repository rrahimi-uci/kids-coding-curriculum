"""TEACHER REFERENCE SOLUTION: Guess-the-Number Bot

What the program does: the child thinks of a number from 1 to 100 and the bot finds it by
asking "Is it ...?". The child answers h (higher), l (lower) or c (correct). The bot always
needs 7 guesses or fewer. It can also play alone against a known secret number.

Key ideas practiced: binary search (always guess the middle of what is left, so every answer
throws away half of the numbers), a `while` loop that shrinks a range, and functions that
return a result.

Approach: the bot remembers a range `low..high`. `next_guess` picks the middle. After each
answer, the range shrinks: "higher" moves `low` up past the guess, "lower" moves `high` down
below it. Only `check` and `next_guess` are TODOs; the loops around them are provided.
"""


def check(guess, secret):
    """Return "higher", "lower" or "correct" (what the secret is compared to the guess)."""
    # Step 1: the answer is about the SECRET, not the guess. A guess that is too small
    # means the secret is "higher".
    if guess < secret:
        return "higher"
    elif guess > secret:
        return "lower"
    return "correct"


def next_guess(low, high):
    """The smart bot guesses the middle of the range low..high."""
    # Step 2: "//" divides and drops the fraction, so the guess is always a whole number.
    # Guessing the middle removes about half of the possible numbers whatever the answer is.
    return (low + high) // 2


def bot_play(secret, low=1, high=100):
    """Let the bot find secret on its own. Return the list of its guesses."""
    guesses = []
    while low <= high:
        guess = next_guess(low, high)
        guesses.append(guess)
        answer = check(guess, secret)
        if answer == "correct":
            return guesses
        elif answer == "higher":
            low = guess + 1    # the guess itself was wrong, so skip past it
        else:
            high = guess - 1
    return guesses


def play_with_human(low=1, high=100):
    """You think of a number. The bot asks questions until it finds it."""
    print(f"Think of a whole number from {low} to {high}. I will find it!")
    tries = 0
    while low <= high:
        guess = next_guess(low, high)
        tries = tries + 1
        prompt = f"Is it {guess}? Type h (higher), l (lower) or c (correct): "
        answer = input(prompt).strip().lower()
        if answer == "c":
            print(f"Got it in {tries} tries!")
            return tries
        elif answer == "h":
            low = guess + 1
        elif answer == "l":
            high = guess - 1
        else:
            print("Please type h, l or c.")
            tries = tries - 1  # a typo should not count as a guess
    # The range became empty: the answers contradicted each other somewhere.
    print("Hmm, the answers do not add up. Did a bug sneak into an answer? Let's play again!")
    return tries


if __name__ == "__main__":
    print("Bot practice: secret 73 found with guesses", bot_play(73))
    play_with_human()


# Common mistakes children make here:
# - Turning check around ("higher" when the guess is too big), so the bot searches the wrong
#   half and never finds the number.
# - Using `/` instead of `//` in next_guess, which gives a decimal like 50.5.
# - Guessing a random number in the range: it works, but sometimes needs more than 7 guesses.
# - (In their own versions of the loop) setting `low = guess` instead of `guess + 1`, which
#   can repeat the same guess forever.
#
# Another correct way for next_guess (stay away from the very edge of big numbers):
#     return low + (high - low) // 2
