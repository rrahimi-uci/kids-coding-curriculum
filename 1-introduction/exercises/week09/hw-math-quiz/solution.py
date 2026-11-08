# TEACHER REFERENCE SOLUTION: Mini Math Quiz
#
# What the program does: it asks two math questions in the Shell, says
# "Correct!" or gives the right answer kindly, and finally prints the score.
# Key ideas: a variable (score) that remembers something, turning input text
# into a number with int(), and if / else.
# Approach: question 2 is a copy of question 1 with new numbers. The score
# goes up by 1 only inside the "right answer" branch.

print("Welcome to the Mini Math Quiz!")
score = 0       # nobody has scored yet

# Question 1
answer = int(input("What is 7 x 8? "))      # int() turns the typed text into a number
if answer == 56:
    print("Correct!")
    score = score + 1       # take the old score, add 1, and store the new score
else:
    print("Good try! 7 x 8 = 56")

# Question 2
# The same name, answer, is used again. The old answer is no longer needed.
answer = int(input("What is 9 + 15? "))
if answer == 24:
    print("Correct!")
    score = score + 1
else:
    print("Good try! 9 + 15 = 24")

# Last line: the checker reads the number after the word "scored".
# print() adds the spaces between the pieces for us.
print("You scored", score, "out of 2")

# Common mistakes children make here:
# - Forgetting int(), so 24 typed in is the text "24" and never equals 24.
# - Adding 1 to the score in the else branch, so wrong answers get points.
# - Writing score + 1 without score = in front. That calculates but forgets.
# - Writing "out of 2" but leaving the score out, or printing the score before
#   the questions are finished.
#
# Another correct way: an f-string puts the numbers inside the text.
#   print(f"You scored {score} out of 2")
