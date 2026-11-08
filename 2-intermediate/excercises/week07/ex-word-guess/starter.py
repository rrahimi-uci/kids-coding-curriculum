# Word Guess
# The secret words live in words.txt (one word per line), not in the code.
# Your job: read the words from the file, and show the player's progress.
# Do the TODOs in order. Press Run after each one.

import random

WORD_FILE = "words.txt"
MAX_MISSES = 6


def load_words(filename):
    """Read one word per line. Skip empty lines, remove spaces, make lowercase."""
    words = []
    # TODO 1: open the file in "r" mode with a with-block.
    #         For every line in the file:
    #             word = line.strip().lower()
    #             if the word is not empty (""), append it to words.
    return words


def show_progress(secret, guessed):
    """Return the secret word with letters not guessed yet shown as _.
    show_progress("pixel", ["p", "e"]) gives "p _ _ e _"."""
    shown = ""
    for letter in secret:
        # TODO 2: if the letter is in guessed, add the letter and a space
        #         to shown. Otherwise add "_ " (underscore and a space).
        shown = shown + "_ "
    return shown.strip()


def is_solved(secret, guessed):
    """True when every letter of the secret word has been guessed."""
    for letter in secret:
        if letter not in guessed:
            return False
    return True


def play(words):
    """Play one round of Word Guess with a random word from the list."""
    if len(words) == 0:
        print("I have no words yet! Check words.txt and load_words().")
        return
    secret = random.choice(words)
    guessed = []
    misses = 0
    while misses < MAX_MISSES and not is_solved(secret, guessed):
        print(f"{show_progress(secret, guessed)}    misses left: {MAX_MISSES - misses}")
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please type exactly one letter.")
        elif guess in guessed:
            print("You already tried that one.")
        else:
            guessed.append(guess)
            if guess not in secret:
                misses = misses + 1
                print("Not in the word.")
    if is_solved(secret, guessed):
        print(f"You got it! The word was {secret}.")
    else:
        print(f"Out of guesses. The word was {secret}.")


if __name__ == "__main__":
    words = load_words(WORD_FILE)
    print(f"=== Word Guess === I know {len(words)} words.")
    play(words)
