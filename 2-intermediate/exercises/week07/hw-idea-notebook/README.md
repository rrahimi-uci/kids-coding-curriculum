# Homework 7 - Game Idea Notebook

**Goal:** a notebook program that remembers your game and art ideas, even
after you close it. (Great for collecting ideas for your final project!)

1. Open `starter.py` and press **Run**. Type `a`, an idea, then `l`. The idea
   is gone: nothing is saved yet.
2. **TODO 1** `add_idea()`: open the file with `"a"` and write the idea plus
   `"\n"` (a new line).
3. **TODO 2** `load_ideas()`: read the file line by line. If the file is
   missing, catch `FileNotFoundError` and make an empty one.
4. Run it, add three ideas, quit with `q`, run it again and type `l`. Your
   ideas are still there!

**Done looks like:**

```text
a = add an idea, l = list ideas, q = quit: l
1. A dragon racing game
2. Rainbow spiral art
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Privacy:** this file is for ideas only. Do not write real names, ages,
schools, addresses or passwords in it.

**Extra:** add `d` = delete all ideas (hint: open the file with `"w"` and write
nothing), or `c` = count the ideas.
