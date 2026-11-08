# TEACHER REFERENCE SOLUTION: Bug Hunt 3 - Word Finder (off-by-one binary search)
#
# What the program does: find_word looks for a word in a SORTED list and
# says where it is (its index), or -1 if the word is not there.
# Key ideas: binary search (keep cutting the search area in half) and
# "off-by-one" mistakes at the edges of a list.
# Approach: two numbers, low and high, mark the part of the list that could
# still hold the word. We peek at the middle word and throw away the half
# that cannot contain the target. The two bugs were both about the edges.
#
# The two off-by-one bugs (marked FIX below):
#   FIX 1: high = len(words)   -> high = len(words) - 1
#   FIX 2: while low < high    -> while low <= high

WORDS = ["apple", "banana", "cherry", "dragon", "eagle", "falcon",
         "guitar", "harbor", "island", "jungle", "koala", "lemon"]


def find_word(words, target):
    """Binary search in a SORTED list. Return the index of target, or -1."""
    low = 0
    # FIX 1: the last valid index is len(words) - 1, because counting starts
    # at 0. A list of 12 words has indexes 0 to 11, so index 12 does not exist.
    high = len(words) - 1
    # FIX 2: when low and high are equal, ONE word is still left to check.
    # Stopping at "low < high" skipped that last word.
    while low <= high:
        mid = (low + high) // 2  # the middle spot of the area still in play
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            # The target comes later in the alphabet, so everything up to
            # and including mid is ruled out.
            low = mid + 1
        else:
            # The target comes earlier, so mid and everything after is out.
            high = mid - 1
    # The search area became empty without a match: the word is not here.
    return -1


if __name__ == "__main__":
    for word in ["apple", "dragon", "lemon", "zebra"]:
        print(word, "->", find_word(WORDS, word))


# Common mistakes children make here:
#   - Fixing only one bug. With only FIX 1 the first and last words can be
#     missed; with only FIX 2 the program can crash with an IndexError.
#   - Writing high = len(words) - 1 but keeping "while low < high", so the
#     last remaining word is never checked (a one-word list fails).
#   - Changing "mid + 1" or "mid - 1" to just "mid", which can make the
#     loop run forever.
#
# Another correct way: Python's built-in bisect module does the same job.
#   import bisect
#   spot = bisect.bisect_left(words, target)
#   return spot if spot < len(words) and words[spot] == target else -1
