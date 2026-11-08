# Markov story machine
# A very small "language model". It learns ONE thing from a text:
#   "after this word, which words came next?"
# Then it writes new text by starting with a word and repeatedly picking
# a random word that followed it in the training text.
# The training text below was written for this course (free to use).

import random

TEXT = """
The dragon sat on the hill and sang a song to the moon.
The robot sat on the moon and sang a song to the stars.
The cat sat on the robot and sang a song to nobody at all.
The moon looked down at the hill and the dragon looked up at the moon.
The stars looked down at the robot and the robot waved back at the stars.
"""


def words_of(text):
    """Lower-case words, split on spaces (full stops stay on their word)."""
    return text.lower().split()


def build_chain(words):
    """A dictionary: each word -> the list of words that came straight after it.
    Repeats are kept, so common followers are picked more often."""
    chain = {}
    # TODO: for i in range(len(words) - 1):
    #           word = words[i] and next_word = words[i + 1]
    #           if word is not a key in chain yet, set chain[word] = []
    #           append next_word to chain[word]
    return chain


def generate(chain, start, length):
    """Make up to length words, starting with start."""
    story = [start]
    current = start
    while len(story) < length:
        options = chain.get(current, [])
        if not options:              # dead end: this word never had a follower
            break
        current = random.choice(options)
        story.append(current)
    return " ".join(story)


if __name__ == "__main__":
    chain = build_chain(words_of(TEXT))
    print("After 'the' came:", chain.get("the"))
    random.seed(7)                   # same seed = same story every time
    for _ in range(3):
        print("-", generate(chain, "the", 14))
