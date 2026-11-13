# Teacher reference: Exercise 3.2 - Fruit Survey Robot
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 3 (Data Detectives)  **Kind:** Scratch (offline app)  **Time:** about 15 minutes
**Big idea:** A program can collect data: it asks a question, checks each answer with if/else, and counts it in a variable, like a tally that keeps itself.

## The finished project
Setup: File > New. Keep the cat. Make two variables, "apple votes" and "other votes" (For all sprites). Leave their checkboxes ticked so the counters show on the stage.

Sprite: Sprite1 (the cat)
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

## What you should see
- Green flag: both counters show 0. The cat shows the question in a speech bubble and a typing box appears at the bottom of the stage.
- Type "apple" and press Return (or click the check mark): apple votes goes up by 1. Type anything else: other votes goes up by 1.
- After 4 answers, the cat says "Thank you!" for 2 seconds. The two counters add up to 4.
- Tricky answers: "Apple" and "APPLE" count as apple, because Scratch's "=" ignores big and small letters. "apples", "aple" and "apple " (with a space at the end) count as other, because they are not exactly the same word.

## Talking points
- The variables are the tally; the stage counters are a live scoreboard of the data.
- The if/else makes a choice for every answer: one gap or the other, never both.
- Tidy data: a survey works best when everyone writes the answer the same way. Python (week 6) is pickier than Scratch: there, "Apple" and "apple" are different.
- We ask only about fruit. The "ask" block could ask anything, so we choose questions that never need personal information.

## Common mistakes and quick fixes
- The "answer" block is typed as a word instead of dragged in: every answer counts as other. Drag the round light blue "answer" block into the left side of "=".
- "apple" typed with a capital letter or an extra space on the right of "=": a capital is fine in Scratch; a space is not. Retype the word.
- Both "change" blocks under the if/else instead of in its gaps: both counters go up every time. Drag each into its own gap.
- Counters keep growing from the last run: the two "set ... to 0" blocks are missing.
- Nowhere to type: the box only appears while the cat is waiting. Click the flag first, then click in the box.
- The variable dropdown in a block shows the wrong variable: pick the right one from its little arrow.

## Check-off list
- [ ] Two variables, both set to 0 under the green flag.
- [ ] "ask and wait" and an if/else inside a repeat 4.
- [ ] "answer = apple" in the if, a "change by 1" in each gap.
- [ ] The child tested "Apple" and "apples" and can say what happened.
