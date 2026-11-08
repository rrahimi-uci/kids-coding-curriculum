# Word Counter - reference solution
# A dictionary can count things: each word is a key, its count is the value.
# .lower() makes "The" and "the" the same. .split() cuts a sentence into words.


def count_words(text):
    """Return a dictionary: word -> how many times it appears in the text."""
    counts = {}
    for word in text.lower().split():
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts


def most_common(counts):
    """Return the word with the biggest count."""
    best_word = ""
    best_count = 0
    for word, count in counts.items():
        if count > best_count:
            best_word = word
            best_count = count
    return best_word


if __name__ == "__main__":
    song = "the slime jumps and the slime bounces and the dragon sleeps"
    counts = count_words(song)
    for word, count in counts.items():
        print(f"{word}: {count}")
    print(f"Most common word: {most_common(counts)}")
