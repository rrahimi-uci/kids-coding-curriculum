# TEACHER REFERENCE SOLUTION: Word Counter (Homework 5)
#
# What the program does: it counts how many times each word appears in a
# sentence, prints the counts, and names the most common word.
# Key ideas practiced: using a dictionary to count things (word is the key,
# count is the value), .lower(), .split(), and finding the biggest value with a
# loop and a "best so far" variable.
# Approach: count_words() goes through the words one at a time. A new word starts
# at 1; a word we have seen before gets 1 added. most_common() walks through the
# counts and remembers the biggest one it has seen so far.


def count_words(text):
    """Return a dictionary: word -> how many times it appears in the text."""
    counts = {}
    # .lower() makes "The" and "the" match; .split() cuts the text into words.
    for word in text.lower().split():
        # FIX 1: the starter wrote counts[word] = 1 every time, which reset the count to
        # 1 even for a word seen before. Now we add to the old count when we have one.
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1              # first time we see this word
    return counts


def most_common(counts):
    """Return the word with the biggest count."""
    best_word = ""
    best_count = 0                        # any real count (at least 1) beats this
    for word, count in counts.items():
        if count > best_count:            # ">" not ">=": if two words tie, the first one wins
            best_word = word
            best_count = count
    return best_word


if __name__ == "__main__":
    song = "the slime jumps and the slime bounces and the dragon sleeps"
    counts = count_words(song)
    for word, count in counts.items():
        print(f"{word}: {count}")
    print(f"Most common word: {most_common(counts)}")


# Common mistakes children make here:
# - Writing counts[word] = counts[word] + 1 without the "if word in counts" check:
#   a new word is not in the dictionary yet, so it crashes with a KeyError.
# - Forgetting .lower(), so "The" and "the" are counted as two different words.
# - Returning best_count instead of best_word from most_common (the README asks
#   for the word, not the number).
# - Putting the "return" inside the loop (indented too far), so only the first
#   word is ever looked at.
#
# Another correct way: get() with a starting value replaces the if / else, and
# max() with key= finds the biggest.
#   counts[word] = counts.get(word, 0) + 1
#   return max(counts, key=counts.get)
