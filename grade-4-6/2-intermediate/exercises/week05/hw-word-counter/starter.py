# Word Counter
# Count how many times each word appears, using a dictionary.


def count_words(text):
    """Return a dictionary: word -> how many times it appears in the text."""
    counts = {}
    for word in text.lower().split():
        # TODO 1 (bug): every word gets the count 1, even if we saw it before.
        # If the word is already in counts, add 1. Otherwise start it at 1.
        counts[word] = 1
    return counts


def most_common(counts):
    """Return the word with the biggest count."""
    best_word = ""
    best_count = 0
    # TODO 2: for word, count in counts.items():
    #             if count is bigger than best_count, remember this word and count
    return best_word


if __name__ == "__main__":
    song = "the slime jumps and the slime bounces and the dragon sleeps"
    counts = count_words(song)
    for word, count in counts.items():
        print(f"{word}: {count}")
    print(f"Most common word: {most_common(counts)}")
