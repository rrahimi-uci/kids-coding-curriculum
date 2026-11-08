# Exercise 9.2 - Pick a Color

**Goal:** the program asks for a color and paints a circle in that color.
If it does not know the color, it says so and uses black.

1. Open `starter.py` and press **Run** (F5). Type `orange` in the Shell and
   press **Return**. It works!
2. Run again and type `green`. A red error! The program does not know green yet.
3. Add an `elif` for `"green"` (use `"#009E73"`).
4. Add an `else:` for any other answer: print a friendly message and use
   black `"#000000"`.
5. Test all four: `orange`, `blue`, `green`, and something silly like `pizza`.

**Remember:** Python is picky - `"Blue"` and `"blue"` are different. Type
small letters. Each `if`, `elif` and `else` line ends with a colon `:`, and the
lines under it are pushed in 4 spaces.

**Done looks like:** every answer draws a circle, and the color name is
written under it (so you can tell colors apart without seeing color).

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add sky blue (`"#56B4E9"`), vermillion (`"#D55E00"`) and purple
(`"#CC79A7"`).
