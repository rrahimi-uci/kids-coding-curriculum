# Homework 5 - Word Counter

**Goal:** use a dictionary to count things.

```
"the slime jumps and the slime ..."   ->   {"the": 3, "slime": 2, "jumps": 1, ...}
```

Two string tools help:

* `text.lower()` makes every letter small, so `The` and `the` match.
* `text.split()` cuts the text into a list of words at the spaces.

1. Open `starter.py` and press **Run**. Every word says 1. Bug!
2. **TODO 1:** if the word is already in `counts`, add 1. Otherwise start at 1.
3. **TODO 2:** finish `most_common()`.

**Done looks like:**

```
the: 3
slime: 2
jumps: 1
and: 2
bounces: 1
dragon: 1
sleeps: 1
Most common word: the
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** codebreakers count LETTERS in secret messages: the most common
letter in English is usually e. Change the program to count letters instead
of words.
