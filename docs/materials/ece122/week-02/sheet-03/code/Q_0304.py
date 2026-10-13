# Sheet (3), Q #04
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     whether the student’s product is correct
#   HAVE     two random 2-digit numbers and the student’s answer
#   CONVERT  2 digits = 10 to 99
#   RELATE   answer == num1 * num2
#   CHECK    the largest product is 99 × 99 = 9801

import random

# 1. two two-digit numbers
num1 = random.randint(10, 99)
num2 = random.randint(10, 99)

# 2. ask the student
answer = eval(input("What is "+ str(num1) + " * " + str(num2) + " ? "))

# 3. compare with the true product
if num1 * num2 == answer:
    print("You are correct!")

else:
    print("Your answer is wrong.\n", num1, '*', num2, " = ", num1 * num2)
