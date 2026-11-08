# Bug Hunt 3: Word Finder - FIXED version (teacher)
# The two off-by-one bugs:
#   1. high = len(words)       -> high = len(words) - 1  (the last index)
#   2. while low < high        -> while low <= high      (check the last one left)

WORDS = ["apple", "banana", "cherry", "dragon", "eagle", "falcon",
         "guitar", "harbor", "island", "jungle", "koala", "lemon"]


def find_word(words, target):
    """Binary search in a SORTED list. Return the index of target, or -1."""
    low = 0
    high = len(words) - 1
    while low <= high:
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
