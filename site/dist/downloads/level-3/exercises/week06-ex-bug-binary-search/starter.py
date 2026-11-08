# Bug Hunt 3: Word Finder
# find_word uses binary search on a sorted list of words.
# It has 2 off-by-one bugs. Some words are never found - and if you fix only
# one bug, it may even crash with an IndexError!
# Expected output when fixed:
#   apple -> 0
#   dragon -> 3
#   lemon -> 11
#   zebra -> -1

WORDS = ["apple", "banana", "cherry", "dragon", "eagle", "falcon",
         "guitar", "harbor", "island", "jungle", "koala", "lemon"]


def find_word(words, target):
    """Binary search in a SORTED list. Return the index of target, or -1."""
    low = 0
    high = len(words)
    while low < high:
        mid = (low + high) // 2
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    for word in ["apple", "dragon", "lemon", "zebra"]:
        print(word, "->", find_word(WORDS, word))
