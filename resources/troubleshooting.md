# Troubleshooting

Most problems have a quick fix. Find your problem below. If you are stuck for more than five minutes, write down what you tried and ask a grown-up or bring the question to the next session. That is a great result too.

## Scratch

**Scratch will not open ("cannot be opened because Apple cannot check it").**
In Applications, Control-click **Scratch 3**, choose **Open**, then **Open** again. You only need to do this once.

**The pen blocks are missing.**
Click the **Add Extension** button (bottom left) and choose **Pen**. Each new project needs it again.

**A sprite has vanished off the stage.**
Click the sprite in the sprite list, set x and y to 0 in the boxes above it, and check that **Show** is on.

**My project was not saved, or I cannot find it.**
Choose **File > Save to your computer** and pick the `My Scratch` folder in Documents. Open it with **File > Load from your computer**.

**Nothing happens when I click the green flag.**
The script needs a "when green flag clicked" block on top, and the blocks must be snapped together. Drag the top block: does the whole stack move as one?

## Thonny and Python

**The Run button is gray, or nothing happens.**
A program is still running. Press the red **Stop** button (or **Ctrl+F2**), then Run again.

**The turtle window will not close, or the beachball spins.**
Click the turtle window and close it, or press **Stop** in Thonny. `turtle.done()` keeps the window open on purpose until you close it.

**The turtle window does not appear.**
It may be hidden behind Thonny. Press **Cmd+Tab** or click the Python icon in the Dock.

**A `Terminator` error appears after closing the window.**
It is harmless. Press Run again.

**`AttributeError: module 'turtle' has no attribute 'Turtle'`.**
You saved your file as `turtle.py` (or `random.py`). Rename it, for example `my_square.py`, and delete any `turtle.py` in that folder.

**`IndentationError` ("expected an indented block" or "unexpected indent").**
Lines inside `for`, `if`, `while` and `def` need 4 spaces; other lines need none. Select the lines and press **Tab** (move in) or **Shift+Tab** (move out). Check that the line above ends with a colon.

**`SyntaxError`.**
Look at the line Thonny highlights and the line above it. A missing `)`, `"` or `:` is the usual cause. **View > Assistant** explains errors in friendlier words.

**`NameError: name 'Print' is not defined`.**
Check spelling and capital letters. Python words are lower case: `print`, `forward`.

**`ModuleNotFoundError: No module named 'pytest'`.**
Install pytest: **Tools > Manage packages...**, search `pytest`, **Install**, then restart Thonny. See [Set up your Mac](../setup-mac/#pytest-level-2-needed-from-week-8).

**A test says `ModuleNotFoundError` for my own program.**
The test file and your program must be in the same folder, and the `import` line must match your file name without `.py`.

**Key presses do nothing in a turtle program.**
Click the turtle window once so it has the keyboard focus. Check that the program calls `screen.listen()` and that the key name is right: `"Left"`, `"Right"`, `"Up"`, `"Down"`, `"space"` or a lower-case letter.

**A function runs once at the start and then never again.**
`onkey(jump(), "space")` calls the function straight away. Remove the brackets: `onkey(jump, "space")`.

**My program never stops.**
Press the red **Stop** button. Then find the `while` loop and check that something inside it changes, so the condition can become False. A great bug hunt!

## Files

**`FileNotFoundError`.**
The file is not in the folder where your program is saved. Check the spelling and the extension (Finder may hide `.txt`). For high scores, catch the error with `try` and `except FileNotFoundError:` and start with an empty list.

**My file is created somewhere strange.**
The program was never saved. An "untitled" program runs from your home folder. Save it first.

**All my saved data disappeared.**
`open(name, "w")` empties the file first. Use `"a"` to add to the end.

## Level 3: git, recursion and data

**The screen filled with strange text after I forgot `-m "message"`.**
Git opened the `vim` editor. Press **Esc**, type `:q!` and press **Return**. Then commit again with `-m`. (In `nano`: press **Ctrl+X**.) The [Mac setup](../setup-mac/#terminal-and-git-level-3) sets `nano` to avoid this.

**`You are in 'detached HEAD' state`.**
You used `git checkout <code>` to look at an old save point. Nothing is lost. Type `git switch main` to go back to the latest work.

**`git restore` deleted my changes.**
`restore` throws away changes that were never committed, and it cannot be undone. This is why we commit often.

**`xcrun: error: invalid active developer path`.**
This usually happens after a macOS update. Run `xcode-select --install` again.

**`RecursionError: maximum recursion depth exceeded`.**
The function keeps calling itself. Check three things: is there a base case (like `if n == 0: return`)? Does every call make the problem smaller (`n - 1`)? In a flood fill, mark a square as visited before you recurse.

**A `KeyError` for the first column of a CSV file, or a `UnicodeDecodeError`.**
The file came from a spreadsheet app with a hidden marker at the start. Open it with `encoding="utf-8-sig"`.

**`TypeError: can only concatenate str (not "int")` with CSV data.**
Everything read from a CSV file is text. Convert it with `int(...)`, and skip empty rows first.

**The turtle drawing is very slow.**
Add `screen.tracer(0)` at the start and `screen.update()` after drawing each frame.

## The Mac

**"Thonny would like to access files in your Documents folder".**
Click **Allow**. Scratch may ask the same.

**Scratch asks to use the microphone or camera.**
Click **Don't Allow**. You do not need them.

**Screen Time blocks an app.**
A grown-up can add Thonny and Scratch to "Always Allowed" in **System Settings > Screen Time**.
