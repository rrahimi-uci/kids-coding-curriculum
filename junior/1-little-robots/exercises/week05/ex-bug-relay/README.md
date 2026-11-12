# Exercise 5.2 – Bug-Hunt Relay (bug hunt)

**Goal:** fix three broken projects, one leg at a time.
**Tool:** Scratch app. **Work with a partner:** swap Driver after each leg.

## Build steps

1. Click **File**, then **New**. Build the leg as you see it.
2. **Test:** click the green flag.
3. **Look:** what should it do? What did it do?
4. **Change one thing.** Then test again.
5. Swap Driver. Next leg!

## The script in words (with the bugs)

**Leg 1: The Quiet Cat.** It should say hi and meow.

- when green flag clicked (yellow Events)
- say Hi! for 2 seconds (purple Looks)
- (not snapped on) play sound Meow until done (pink Sound)

**Leg 2: Bye Before Hi.** It should say hi first, then bye.

- when green flag clicked
- say Bye! for 2 seconds
- say Hi! for 2 seconds

**Leg 3: Too Many Meows.** It should meow three times.

- when green flag clicked
- repeat 10 (orange Control)
  - play sound Meow until done

## Expected behavior

After each fix, the cat does what the leg says it should do.
The red stop sign stops a project at any time.

## Checklist

- [ ] Leg 1: the cat says hi and meows.
- [ ] Leg 2: the cat says hi, then bye.
- [ ] Leg 3: the cat meows three times.
