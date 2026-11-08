# TEACHER REFERENCE SOLUTION: Exercise 7.2 - Word Guess
#
# What it does: a guess-the-word game. The secret words are read from the
# file words.txt (one word per line), and the player guesses letters until
# the word is complete or six misses are used up.
# Key ideas: reading a text file line by line, cleaning text with strip()
# and lower(), and building a string one letter at a time in a loop.
# Approach: load_words() cleans every line and keeps the non-empty ones,
# and show_progress() shows each guessed letter and "_" for the rest.
# Anyone can add words by editing words.txt - no coding needed.

import random

WORD_FILE = "words.txt"
MAX_MISSES = 6


def load_words(filename):
    """Read one word per line. Skip empty lines, remove spaces, make lowercase."""
    words = []
    with open(filename, "r") as file:
        for line in file:
            # strip() removes spaces and the "\n"; lower() makes "Dragon" into
            # "dragon", so it matches the lowercase letters the player types.
            word = line.strip().lower()
            if word != "":               # a blank line in the file is not a word
                words.append(word)
    return words


def show_progress(secret, guessed):
    """Return the secret word with letters not guessed yet shown as _.
    show_progress("pixel", ["p", "e"]) gives "p _ _ e _"."""
    shown = ""
    for letter in secret:
        if letter in guessed:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "
    # Every piece ends with a space, so there is one spare space at the end.
    return shown.strip()


def is_solved(secret, guessed):
    """True when every letter of the secret word has been guessed."""
    for letter in secret:
        if letter not in guessed:
            return False                 # one missing letter is enough to say "not yet"
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
            print("You already tried that one.")      # a repeat does not cost a miss
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


# Common mistakes children make here:
# - Forgetting strip(): every word keeps its hidden "\n" at the end, so
#   the player can never finish the word (they cannot guess a new line).
# - Forgetting lower(): a word like "Dragon" can never be solved, because
#   the player's guesses are turned into lowercase.
# - In show_progress(), leaving out the space after a letter, so the letters
#   and underscores bunch together ("p__e_" instead of "p _ _ e _").
# - Forgetting to return the list in load_words(), so the game says
#   "I have no words yet!".
#
# Another correct way: build the display with join() instead of a loop:
#     pieces = []
#     for letter in secret:
#         pieces.append(letter if letter in guessed else "_")
#     return " ".join(pieces)
