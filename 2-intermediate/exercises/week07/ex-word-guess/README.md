# Exercise 7.2 - Word Guess

**Goal:** a guess-the-word game that reads its secret words from a file.

The words are in `words.txt`, one per line. Open it in Thonny
(**File > Open**) and have a look. Anyone can add words to the game by
editing this file - no coding needed! (If you cannot see `words.txt` in the
Open window, choose "all files" in the file-type menu.)

1. Open `starter.py` and press **Run**. It says "I have no words yet!"
2. **TODO 1** `load_words()`: open `words.txt`, and for every line
   `strip()` it, make it lowercase with `lower()`, and add it to the list if
   it is not empty. Run again: the game starts!
3. **TODO 2** `show_progress()`: show the letters you have guessed and `_`
   for the others, like `p _ _ e _`.
4. Play a round with your partner. Then add three new words to `words.txt`
   (one word on each line, letters only, no spaces), save it, and play
   again. The game should now say it knows 18 words.

**Done looks like:**

```text
=== Word Guess === I know 15 words.
_ _ _ _ _    misses left: 6
Guess a letter: e
_ _ _ e _    misses left: 6
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** make a second word file (`animals.txt`, `space.txt`...) and ask
the player which one to use, or show the letters already tried.
