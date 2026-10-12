# Sheet (3), Q #04
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Random multiplication quiz
# HAVE: answer; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Compare answer with num1 * num2 using ==.
# CHECK: Test both interval endpoints and correct/incorrect answers.
# 1. Read inputs; 2. relate values; 3. display and check.

import random

# Generate two random two-digit integers
num1 = random.randint(10, 99)
num2 = random.randint(10, 99)

# Ask the student before checking the answer
answer = eval(input("What is "+ str(num1) + " * " + str(num2) + " ? "))

# Check the answer and display the result
if num1 * num2 == answer:
    print("You are correct!")

else:
    print("Your answer is wrong.\n", num1, '*', num2, " = ", num1 * num2)
