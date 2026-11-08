# Teacher reference: Exercise 1.1 - The Git Quest
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 3, Week 1 (Save Points: Git Basics)  **Kind:** Terminal  **Time:** about 25 minutes
**Big idea:** Git is a save-game system: each commit is a save point you can look at, compare and go back to.

## The finished project
Setup (teacher, once per Mac): `git --version` prints a version number; if a window offers the command line developer tools, click Install (free, no Apple ID). Type commands by hand (quotes copied from a PDF break them). The student tracks `hero_badge.py` in a new `git-quest` folder.

```
cd ~/Documents                                   # go to Documents
mkdir git-quest                                  # make the quest folder
cd git-quest                                     # go inside it
# copy hero_badge.py into git-quest (drag in Finder or Save As in Thonny)
ls                                               # shows hero_badge.py
git config --global user.name "PixelFox"         # a nickname, never a real name
git config --global user.email "pixelfox@example.com"   # pretend address
git init                                         # start the save system here
git status                                       # hero_badge.py is untracked
git add hero_badge.py                            # choose what goes in the save
git commit -m "Add hero badge drawing"           # first save point
git log --oneline                                # one line: id and message
# Thonny: change BADGE_COLOR to "#009E73" and HERO_NAME to a made-up name, save, run
git diff                                         # - lines removed, + lines added
git add hero_badge.py                            # pack the backpack again
git commit -m "Change badge color to green"      # second save point
# Thonny: delete the whole draw_star function, save, run (it crashes)
git status                                       # shows hero_badge.py modified
git restore hero_badge.py                        # reload the last save point
# Thonny: close and reopen the file (or click Yes to reload); draw_star is back
# Level 7: make any change of your own (bigger star, new color, second star)
git diff                                         # check the change
git add hero_badge.py
git commit -m "Make star bigger"                 # third save point
git log --oneline                                # at least 3 commits
git status                                       # nothing to commit, working tree clean
```

## What you should see
- `git log --oneline` lists at least 3 commits, newest first, for example (ids always differ):
  `3e8d1f2 (HEAD -> main) Make star bigger`, `9b0c7a4 Change badge color to green`, `7c41e0a Add hero badge drawing`. The branch may say `master`; both are fine.
- Each message starts with a verb and says what changed (not "stuff" or "update").
- `git status` ends with "On branch main" and "nothing to commit, working tree clean".
- `git config user.name` shows a nickname and `git config user.email` an address ending in `@example.com`.
- After `git restore`, the `draw_star` function is back and the program runs and shows the star.

## Talking points
- A commit is a save point: you can try something risky and load the last save if it goes wrong.
- Class photo: `git add` calls people into the photo, `git commit` presses the camera button and adds a caption, `git log` is the album, `git diff` is spot the difference, `git restore` puts things back as in the last photo.
- The history is written in pen: never commit real names, passwords, addresses or photos of people.
- "stuff" will not help you in a month; a message that says what changed will.

## Common mistakes and quick fixes
- `git commit` without `-m` opens a strange full-screen editor (Vim): press Esc, type `:q!`, press Return, then commit again with `-m "message"`.
- `git init` in the wrong folder (for example the home folder): `git status` lists hundreds of files. Do not commit. Delete that `.git` folder (Finder, Cmd+Shift+. to show hidden files), then `cd` into `git-quest` and start again.
- "Please tell me who you are" error: the two `git config` lines were skipped. Type them, then commit again.
- `git diff` shows nothing (file not saved, so press Cmd+S) or "nothing added to commit" (`git add` forgotten).
- After `git restore`, Thonny still shows the broken code: click Yes if it offers to reload, otherwise close the tab and open the file again.

## Check-off list
- [ ] `git --version` shows a version number.
- [ ] I set `user.name` to a nickname and `user.email` to `...@example.com`: check with `git config user.name` and `git config user.email`.
- [ ] I ran `git init` inside `Documents/git-quest` (not anywhere else): `pwd` ends in `git-quest` and `git status` lists only `hero_badge.py`.
- [ ] I made my first commit with `git add` and `git commit -m "..."`: the oldest line in the log is "Add hero badge drawing" or similar.
- [ ] I used `git diff` to see my change before committing it: the student can point at a `-` line and a `+` line.
- [ ] I broke the file on purpose and fixed it with `git restore`: the student can explain that `git restore` brought back `draw_star`.
- [ ] `git log --oneline` shows 3 or more commits with helpful messages.
