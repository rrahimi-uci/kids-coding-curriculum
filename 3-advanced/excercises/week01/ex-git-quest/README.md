# Exercise 1.1 - The Git Quest

**Goal:** make your first save points (commits) with git, look back in time,
spot a change, and undo a mistake.

You will track one small art program, `hero_badge.py` (it is in this folder),
inside a brand-new folder called `git-quest`. Everything stays on your Mac:
no website, no account.

Type each command in **Terminal** exactly, then press **Return**.
Lines starting with `#` are notes for you - do not type them.

## Before you start (once per Mac, done by your teacher)

```
git --version
```

If you see something like `git version 2.39.5`, git is ready.
If a window pops up asking to install "command line developer tools",
your teacher clicks **Install** (free, no Apple ID needed) and waits.

## Level 1 - Make a quest folder

```
cd ~/Documents
mkdir git-quest
cd git-quest
```

Now copy `hero_badge.py` into the `git-quest` folder (drag it in Finder, or
use **File > Save As...** in Thonny and pick `Documents/git-quest`).

```
ls
```

You should see `hero_badge.py`.

## Level 2 - Tell git who you are (a nickname, not your real name)

```
git config --global user.name "PixelFox"
git config --global user.email "pixelfox@example.com"
```

Use YOUR nickname. `example.com` is a pretend address that is safe to use.
Your real name and real email never go into the history.

## Level 3 - Start the save system

```
git init
git status
```

`git status` says `hero_badge.py` is **untracked**: git sees it but is not
saving it yet.

## Level 4 - Your first save point

```
git add hero_badge.py
git commit -m "Add hero badge drawing"
git log --oneline
```

The log shows one line: a short code (the commit id) and your message.

## Level 5 - Change something and spot the difference

1. Open `hero_badge.py` in Thonny (from the `git-quest` folder).
2. Change `BADGE_COLOUR` to another colour from the palette, e.g. `"#009E73"`.
3. Change `HERO_NAME` to your own made-up hero name. Save. Run it to see it.

```
git diff
```

Lines with `-` were removed, lines with `+` were added.
Now save it:

```
git add hero_badge.py
git commit -m "Change badge colour to green"
git log --oneline
```

Two save points!

## Level 6 - Make a mistake on purpose, then undo it

1. In Thonny, delete the whole `draw_star` function. Save.
2. Run it: it crashes. Oh no!

```
git status
git restore hero_badge.py
```

3. In Thonny, close the file and open it again (or click into it so Thonny
   reloads it). The `draw_star` function is back. Run it - it works.

`git restore` jumps the file back to your last save point.

## Level 7 (boss level) - Make a third commit of your own

Make any change you like (bigger star, new colour, add a second star),
check it with `git diff`, then `add` and `commit` with a helpful message.

## Expected behavior

- `git log --oneline` in `git-quest` shows at least 3 commits.
- Every message says **what** changed, e.g. `Make star bigger`,
  not `stuff` or `update`.
- `git status` says `nothing to commit, working tree clean` at the end.
- No real name, real email or password appears anywhere.

## Checklist

- [ ] `git --version` shows a version number
- [ ] I set `user.name` to a nickname and `user.email` to `...@example.com`
- [ ] I ran `git init` inside `Documents/git-quest` (not anywhere else)
- [ ] I made my first commit with `git add` and `git commit -m "..."`
- [ ] I used `git diff` to see my change before committing it
- [ ] I broke the file on purpose and fixed it with `git restore`
- [ ] `git log --oneline` shows 3 or more commits with helpful messages

## Command cheat sheet

| Command | What it does | Game words |
|---|---|---|
| `git init` | start a save system in this folder | new save file |
| `git status` | what changed since the last save? | check the pause menu |
| `git add file` | choose what goes in the next save | pack your backpack |
| `git commit -m "msg"` | make a save point with a label | save the game |
| `git log --oneline` | list all save points, newest first | load-game menu |
| `git diff` | show exactly what changed | spot the difference |
| `git restore file` | throw away unsaved changes | reload last save |
