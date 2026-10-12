# Sheet (3), Q #08
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Triangle validity and area
# HAVE: a, b, c; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Q8: sqrt(s*(s-a)*(s-b)*(s-c)). Q9: degrees(acos(...)).
# CHECK: Compare a right triangle, an equilateral triangle and a flat case.
# 1. Read inputs; 2. relate values; 3. display and check.

import math

a, b, c = eval(input("Enter the side lengths of the triangle a, b, and c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area = ",format(area,"<8.2f") )

else:
    print("Invalid triangle")
