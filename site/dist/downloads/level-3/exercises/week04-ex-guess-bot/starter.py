# Guess-the-Number Bot - YOUR version
# The bot uses binary search: always guess the middle of what is left.
# You think of a number; the bot guesses; you answer h, l or c.
# Finish the TODOs, then press Run and see if it does what the README says.


def check(guess, secret):
    """Return "higher", "lower" or "correct" (what the secret is compared to the guess)."""
    # TODO 1: if guess < secret return "higher";
    #         if guess > secret return "lower"; otherwise "correct"
    return "correct"


def next_guess(low, high):
    """The smart bot guesses the middle of the range low..high."""
    # TODO 2: this slow bot always guesses the lowest number. Make it smart:
    #         return the middle, (low + high) // 2
    return low


def bot_play(secret, low=1, high=100):
    """Let the bot find secret on its own. Return the list of its guesses.
    (Already done!)"""
    guesses = []
    while low <= high:
        guess = next_guess(low, high)
        guesses.append(guess)
        answer = check(guess, secret)
        if answer == "correct":
            return guesses
        elif answer == "higher":
            low = guess + 1
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
        answer = input(f"Is it {guess}? Type h (higher), l (lower) or c (correct): ").strip().lower()
        if answer == "c":
            print(f"Got it in {tries} tries!")
            return tries
        elif answer == "h":
            low = guess + 1
        elif answer == "l":
            high = guess - 1
        else:
            print("Please type h, l or c.")
            tries = tries - 1
    print("Hmm, the answers do not add up. Did a bug sneak into an answer? Let's play again!")
    return tries


if __name__ == "__main__":
    print("Bot practice: secret 73 found with guesses", bot_play(73))
    play_with_human()
