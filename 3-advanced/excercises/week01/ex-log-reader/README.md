# Exercise 1.3 - Log Reader

**Goal:** teach Python to read the list of save points that
`git log --oneline` prints, like this:

```
9c1e2d4 Add high score file
5b7a913 Fix hero walking through walls
0f9e8d7 Start game project
```

The first word of each line is the **commit id**. The rest is the **message**.
Git shows the newest commit at the top.

1. Open `starter.py` in Thonny. `parse_line` is already done - read it first.
2. Finish the four `TODO`s: `parse_log`, `count_commits`, `find_commits`
   and `oldest_first`.
3. Press **Run**. You should see:

```
This project has 5 commits.
The story of the project, from the beginning:
  1. Start game project
  2. Draw first level
  ...
Commits about the hero: ['5b7a913', '2d4f6a8']
```

**Check your work:** open `check_my_work.py` and press **Run**. One check
makes a real (tiny, temporary) git project and reads its log!

**Extra:** in Terminal, inside your `git-quest` folder, type
`git log --oneline`, copy the lines, and paste them into `SAMPLE_LOG`
(between the `"""` marks). Run again to read YOUR history.
