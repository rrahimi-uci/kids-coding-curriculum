# Exercise 3.3 - Game Roster

**Goal:** use **composition**: a `Game` object HAS a list of `Player`
objects and asks them to do things.

1. Open `starter.py` in Thonny. `Player` is done. Read it first.
2. Finish the `TODO`s in `Game`: `add_player`, `give_points`, `leader`
   and `still_playing`.
3. Press **Run**. You should see:

```
Space Race: 3 players
Leader: Comet
Still playing: ['Comet', 'Nova']
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a method `scoreboard(self)` that returns a list of lines like
`"Comet: 50 points, 3 lives"`.
