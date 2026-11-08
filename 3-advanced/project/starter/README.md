# Build Something Big - starter kit

Pick ONE option and start from its template:

| Option | Template | What already works |
| --- | --- | --- |
| (a) Grid game | `grid_game_template.py` | a `Grid` class, a `Hero` that moves with the arrow keys and collects treasure |
| (b) Generative art app | `art_app_template.py` | `Shape` and `Square` classes, a `Gallery`, click to add shapes, S = save, L = load |
| (c) Data / AI app | `data_app_template.py` + `data/games.csv` | CSV loading and cleaning, a `DataSet` class, counting, averages, a bar chart |

`test_my_project.py` has example tests for all three. Keep the ones for your
option, delete the rest, and add your own until you have at least 5.

## Getting started (once, with your teacher)

1. Copy this whole `starter` folder into your `Documents/coding-projects`
   folder and rename it, for example `dragon-maze` (no spaces is easiest in
   Terminal).
2. Delete the templates you are not using. Rename yours, for example
   `grid_game_template.py` -> `dragon_maze.py`, and change the `import`
   line in `test_my_project.py` to match.
3. Open a Terminal **from Thonny**: menu **Tools > Open system shell...**
   (this Terminal knows Thonny's Python, which has pytest installed).
   Type these lines, pressing Return after each one:

```bash
cd ~/Documents/coding-projects/dragon-maze
git init
git add .
git commit -m "Start my project from the starter kit"
```

That first commit is your first save point.

## Git workflow cheat list

Do this loop many times: **change a little -> run it -> test it -> commit**.

| I want to... | Type this |
| --- | --- |
| go to my project folder | `cd ~/Documents/coding-projects/dragon-maze` |
| see what changed | `git status` |
| see the exact lines that changed | `git diff` |
| choose a file for the next save point | `git add dragon_maze.py` |
| choose every changed file | `git add .` |
| make a save point | `git commit -m "Add a chaser that uses BFS"` |
| see my save points | `git log --oneline` |
| undo changes I have NOT committed yet | `git restore dragon_maze.py` |
| run my tests (in Thonny's system shell) | `python -m pytest -q` |

Good commit messages say WHAT changed, in a few words, starting with a verb:

* Good: `Add Enemy class that inherits from Character`
* Good: `Fix hero walking through the right-hand wall`
* Not helpful: `stuff`, `changes`, `asdf`, `final final 2`

Golden rules:

* Commit at least once every session, and whenever something works.
* Never commit secrets: no real names, passwords, addresses or photos.
* Stay on one branch (the one git made for you). If git prints something
  that scares you, stop and ask - nothing is lost while it is committed.

## README template (copy into a file called README.md in your project)

```markdown
# <Project name>

<One sentence: what is it and who is it for?>

## How to run it
Open <file name>.py in Thonny and press Run.
Controls: <keys / clicks>

## What it does
- <feature 1>
- <feature 2>
- <feature 3>

## How it is built
- Classes: <ClassName> - <what it is for>; <ClassName> - <...>
- Inheritance or composition: <which class inherits from / has which>
- Data structure: <dict / stack / queue / grid> - <what it stores>
- Algorithm: <search / sort / recursion / BFS> - <where and why>
- Saved file: <file name> - <what is saved>

## Tests
Run `python -m pytest -q` in Thonny's system shell. My tests check: <list>

## A design decision I am proud of
<What did you choose, what else could you have done, and why is your way better?>

## Credits
<Ideas, sounds, pictures, code examples you used and who made them>
```

## What is `.gitignore`?

A hidden file in this folder that lists files git should never save, such as
Python's `__pycache__` folder. You do not need to change it.
