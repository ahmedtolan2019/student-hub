# Sheet (3), Q #03
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     whether the student’s sum is correct
#   HAVE     two random 3-digit numbers and the student’s answer
#   CONVERT  3 digits = 100 to 999
#   RELATE   answer == num1 + num2
#   CHECK    try a right and a wrong answer for the same two numbers

import random

# 1. two three-digit numbers
num1 = random.randint(100, 999)
num2 = random.randint(100, 999)

# 2. ask the student
answer = eval(input("What is "+ str(num1) + " + " + str(num2) + " ? "))

# 3. compare with the true sum
if num1 + num2 == answer:
    print("You are correct!")

else:
    print("Your answer is wrong.\n", num1, '+', num2, " = ", num1 + num2)
