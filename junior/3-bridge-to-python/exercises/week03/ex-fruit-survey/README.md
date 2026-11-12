# Exercise 3.2 – Fruit Survey Robot

**Goal:** make the cat ask a question and count the answers.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. **Variables** (orange-red): make `apple votes` and `other votes`, **For all sprites**.
2. **Events** (yellow): **when green flag clicked**. Then **set** each variable **to 0**.
3. **Control** (orange): **repeat**, changed to `4`.
4. **Sensing** (light blue): **ask and wait** inside, with the fruit question.
5. **Control** (orange): **if then else** under the ask.
6. **Operators** (green): **=** into the if.
7. **Sensing**: **answer** on the left. Type `apple` on the right.
8. Top gap: **change apple votes by 1**. Bottom gap: **change other votes by 1**.
9. **Looks** (purple): **say Thank you!** at the end.
10. Click the flag. Type an answer. Press Return.

## The script in words

- when green flag clicked
- set apple votes to 0
- set other votes to 0
- repeat 4
  - ask What is your favorite fruit? and wait
  - if answer = apple then
    - change apple votes by 1
  - else
    - change other votes by 1
- say Thank you! for 2 seconds

## Expected behavior

The cat asks 4 times. "apple" adds 1 to apple votes. Other answers add 1
to other votes.

## Checklist

- [ ] Both counters start at 0.
- [ ] apple counts as apple, banana as other.
- [ ] I tested Apple and apples. I wrote down what happened.
