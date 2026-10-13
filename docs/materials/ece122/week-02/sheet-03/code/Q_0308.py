# Sheet (3), Q #08
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the triangle’s area, or a message that it is invalid
#   HAVE     three lengths a, b, c
#   CONVERT  none
#   RELATE   valid if every length is positive and every two sides exceed the third; s = (a+b+c)/2; Heron
#   CHECK    3, 4, 5 has area 6 (6.00); 1, 2, 3 is flat: invalid

import math

# 1. read the sides
a, b, c = eval(input("Enter the side lengths of the triangle a, b, and c: "))

# 2. only a real triangle has an area
if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    # 3. Heron's formula
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area = ",format(area,"<8.2f") )

else:
    print("Invalid triangle")
