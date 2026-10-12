# Sheet (3), Q #09
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Triangle angles
# HAVE: a, b, c; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Q8: sqrt(s*(s-a)*(s-b)*(s-c)). Q9: degrees(acos(...)).
# CHECK: Compare a right triangle, an equilateral triangle and a flat case.
# 1. Read inputs; 2. relate values; 3. display and check.

import math

a, b, c = eval(input("Enter the side lengths of the triangle a, b, and c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
    B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
    C = math.acos((c * c - b * b - a * a) / (-2 * a * b))

    print("The three interior angles in degrees:")
    print("Angle A = ",format(math.degrees(A),"<8.2f"))
    print("Angle B = ",format(math.degrees(B),"<8.2f"))
    print("Angle C = ",format(math.degrees(C),"<8.2f"))
else:
    print("Invalid triangle")
