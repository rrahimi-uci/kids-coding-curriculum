# TEACHER REFERENCE SOLUTION: Exercise 9.3 - Markov story machine
#
# What the program does: reads a short training text, learns which words
# came straight after each word, then writes three made-up sentences by
# picking a random follower again and again.
# Key ideas: a very simple language model (predict the next word from the
# current one), dictionaries of lists, and random choice.
# Approach: build_chain makes a dictionary word -> list of followers.
# Repeats are kept on purpose, so a follower that appeared often is more
# likely to be picked. generate walks through the chain one word at a time.
# The machine copies patterns; it does not understand what it writes.

import random

TEXT = """
The dragon sat on the hill and sang a song to the moon.
The robot sat on the moon and sang a song to the stars.
The cat sat on the robot and sang a song to nobody at all.
The moon looked down at the hill and the dragon looked up at the moon.
The stars looked down at the robot and the robot waved back at the stars.
"""


def words_of(text):
    """Lower-case words, split on spaces (periods stay on their word)."""
    return text.lower().split()


def build_chain(words):
    """A dictionary: each word -> the list of words that came straight after it.
    Repeats are kept, so common followers are picked more often."""
    chain = {}
    # Stop one word early (len - 1): the very last word has no word after it,
    # and words[i + 1] would go off the end of the list.
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if word not in chain:
            chain[word] = []              # first time we meet this word
        # append (not "set"): we keep EVERY follower, repeats included.
        chain[word].append(next_word)
    return chain


def generate(chain, start, length):
    """Make up to length words, starting with start."""
    # (Given code.) Start at one word and keep jumping to a random follower.
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


# Common mistakes children make here:
#   - Writing chain[word] = next_word, which keeps only the LAST follower
#     instead of a list of all of them.
#   - Looping over range(len(words)) so words[i + 1] crashes on the last
#     word (IndexError).
#   - Using a set or removing repeats, so common followers are no longer
#     more likely than rare ones.
#
# Another correct way: setdefault creates the empty list for us.
#   for word, next_word in zip(words, words[1:]):
#       chain.setdefault(word, []).append(next_word)
