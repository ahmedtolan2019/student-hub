# Sheet (3), Q #01
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the three numbers from smallest to largest
#   HAVE     three integers
#   CONVERT  none
#   RELATE   compare neighbours and swap if out of order: (1,2), then (2,3), then (1,2) again
#   CHECK    all 27 arrangements of -2, 0, 2 come out sorted (27 tests)

# 1. read three integers
num1, num2, num3 = eval(input("Enter three integers: "))

# 2. put each neighbouring pair in order
if num1 > num2:
    num1, num2 = num2, num1

if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1

# 3. show them in order
print(str(num1) + "\n" + str(num2) + "\n" + str(num3))
