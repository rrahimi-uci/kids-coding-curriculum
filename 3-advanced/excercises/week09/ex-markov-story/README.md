# Exercise 9.3 - Markov story machine

**Goal:** build a tiny text generator - a great-great-grandparent of the
chatbots you may have heard about.

It learns just one thing from the training text: **after each word, which
words came next?** Then it writes by picking a random next word again and
again.

```
"the" -> ["dragon", "hill", "moon", "robot", ...]
"sat" -> ["on", "on", "on"]
```

**Steps**

1. Open `starter.py` and press **Run**. The story is just "the" - the
   chain is empty.
2. TODO: finish `build_chain(words)` so each word maps to the list of words
   that came straight after it (keep repeats!).
3. Run again. Read the three stories. Which sound sensible? Which are silly?

**Done looks like:** `After 'the' came: ['dragon', 'hill', 'moon.', 'robot', ...]`
and three made-up sentences.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** replace `TEXT` with a poem *you* wrote. Change `random.seed(7)` to
another number. Does the machine understand what it writes?
