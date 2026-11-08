# Final project starter: Arcade Game or Art Studio

You get to build your own program! Pick ONE option:

| Option | Start from | What it does now |
|---|---|---|
| A. Arcade game | `game_template.py` | Arrow keys move a square; touch the coin before the 30-second timer runs out. |
| B. Art studio | `art_studio_template.py` | `n` draws a new random flower, `s` saves it to `my_design.txt`. Loading (`l`) is your TODO. |

## Getting started (5 minutes)

1. In Finder, make a new folder for your project, for example
   `my-project-ada` (use your nickname, not your full name).
2. Copy your template **and** `my_tests.py` into that folder.
3. Rename the template to your game's name, for example `space_snack.py`.
   Use lowercase letters and underscores, no spaces.
4. Open it in Thonny and press the green **Run** button. Click the turtle
   window once so it can hear your keys.
5. Read the TODOs from top to bottom. Do them one at a time and press Run
   after every small change.

## Your project must have

- [ ] functions with parameters that **return** a value
- [ ] a **list** (enemies, coins, colours, a gallery of designs...)
- [ ] a **dictionary** (settings, a design, a player...)
- [ ] a `while` loop or a game loop with `ontimer`
- [ ] a **file** (high scores or saved designs), created if it is missing
- [ ] at least **3 tests** of your own functions in `my_tests.py`

## Running your tests

1. Open `my_tests.py`. Change the `import` line to your program's file
   name (without `.py`).
2. Press **Run**. Every test should say `PASSED`.
3. If Thonny says `No module named pytest`: **Tools > Manage packages...**,
   type `pytest`, click **Search**, then **Install**. No account needed.

Tip: put the rules of your program (scores, moving, touching) in small
functions that do **not** use turtle. Those are easy to test.

## Stuck?

- Nothing happens when you press a key: did you call `screen.listen()`?
  Did you write `onkey(go_left, "Left")` **without** `()` after `go_left`?
- `FileNotFoundError`: the file does not exist yet. Catch it with
  `try` / `except FileNotFoundError` and start with an empty list.
- The program freezes: a `while` loop never ends. Press the red **Stop**
  button and check that something inside the loop changes.
- Ask your partner to be the "rubber duck": explain your code line by line.
