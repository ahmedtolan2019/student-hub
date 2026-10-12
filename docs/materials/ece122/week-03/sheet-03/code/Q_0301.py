# Sheet (3), Q #01
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Ordering three values
# HAVE: num1, num2, num3; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Use a separate if for each comparison.
# CHECK: Try equal and negative values.
# 1. Read inputs; 2. relate values; 3. display and check.

num1, num2, num3 = eval(input("Enter three integers: "))

# Bubble-up swap logic to order num1, num2, num3
if num1 > num2:
    num1, num2 = num2, num1

if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1

print(str(num1) + "\n" + str(num2) + "\n" + str(num3))
