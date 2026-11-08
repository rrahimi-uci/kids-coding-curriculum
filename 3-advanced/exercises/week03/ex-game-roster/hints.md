## Hint 1: Where to look
Read `Player` first, since it is done. A `Game` keeps a list called `self.players`, and your `TODO`s all use that list. The method `find` is also done, and it can help you in `give_points`.

## Hint 2: Try this
To make a new object, call the class like a function: `Player(...)`. Then `.append()` puts it in the list. For `leader`, keep a running "best so far" while you loop. At the start, there is no best yet, so it is `None`. Check for that.

## Hint 3: Almost there
In `add_player`, make the player, `self.players.append(____)`, then `return ____`. In `give_points`, use `self.find(____)` and check `is not None`. In `leader`, check `if best is None or ____ > ____:`. In `still_playing`, test `if not ____.is_out():`.
