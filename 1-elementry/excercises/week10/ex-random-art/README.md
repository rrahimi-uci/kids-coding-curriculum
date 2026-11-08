# Exercise 10.2 - Random Bubble Art

**Goal:** fill the screen with 30 bubbles at random places, random sizes and
random colours. Every time you press **Run**, you get a brand-new picture!

1. Open `starter.py` and press **Run** (F5). 30 bubbles... all in the same
   place, so it looks like one bubble.
2. Follow the `# TODO`s inside the loop and use the `random` module:
   * `x = random.randint(-350, 350)` (a random whole number from -350 to 350)
   * `y = random.randint(-250, 250)`
   * `size = random.randint(10, 50)`
   * `colour = random.choice(PALETTE)` (picks one colour from the list)
3. Press **Run** a few times. Is it different every time?

**Done looks like:** colourful bubbles all over the screen, different every run.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a second command, `def star(x, y, size, colour):`, and mix
stars and bubbles. Or try a dark background: `turtle.bgcolor("#000000")`.
