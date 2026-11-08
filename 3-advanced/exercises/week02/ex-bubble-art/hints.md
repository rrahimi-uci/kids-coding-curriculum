## Hint 1: Where to look
Start at the top of the `Bubble` class and work down through the `TODO`s in order. A bubble must remember its own numbers, so the first job is in `__init__`. Look at how `self.x` is already saved.

## Hint 2: Try this
Inside a class, `self.name = value` saves a value on that one object. To change a saved number, set it to its old value plus something. For `make_bubbles`, use `for _ in range(____):` and `random.randint(low, high)` for each number.

## Hint 3: Almost there
Follow this pattern: `self.size = self.size + ____`. In `__init__`, write `self.color = ____` using the parameter with the same name. For the dot, call `t.dot(____, ____)`. In the loop, make `x`, `y`, `size` and `color`, then `bubbles.append(Bubble(____))`.
