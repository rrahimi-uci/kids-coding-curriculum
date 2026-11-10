# Exercise 7.1 - Save High Scores

**Goal:** make Lucky Dice remember every score, even after the program closes.

Right now the program forgets everything when it stops. You will save each
game as one line in a text file called `high_scores.txt`:

```text
Ada,120
Kai,95
```

1. Open `starter.py` in Thonny and press **Run**. Type a nickname and
   press Return. Play twice. Does it remember your first game? (Not yet! It
   says `Games saved so far: 0`.)
2. **TODO 1** `save_score()`: open the file with `"a"` (append = add to the
   end) and write one line `nickname,score`.
3. **TODO 2** `load_scores()`: for every line, `strip()` it, skip empty lines,
   `split(",")` it and add `[nickname, score]` to the list. The score must be
   a number: `int(parts[1])`.
4. **TODO 3** the file might not exist yet (first game ever). Make an empty
   one with `"w"`.
5. Run the game three times. Then open `high_scores.txt` in Thonny
   (**File > Open**, same folder) and look at your saved scores. If you
   cannot see the file, choose "all files" in the file-type menu of the
   Open window.

**Done looks like:** "Games saved so far" goes up by one every time you play,
and the high score is the best one from all the games. Your third game
might look like this (your rolls will be different):

```text
=== Lucky Dice: roll three dice and beat the high score! ===
Your nickname (not your real name): Ada
Roll 1: 4
Roll 2: 6
Roll 3: 2
Ada, you scored 120!
Games saved so far: 3
High score: Ada with 120
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Careful:** `"w"` wipes the file clean before writing. Use `"a"` to add.

**Extra:** print every saved game as a numbered list (`1. Ada - 120`), or
show how many games each nickname has played (a dictionary is perfect).

**Privacy:** save nicknames and scores only. Never save real names, ages or
where you live.
