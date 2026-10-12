# Sheet (2), Q #03
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Regular polygon
# HAVE: n, s; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: A = n*s**2/(4*tan(pi/n)).
# CHECK: Keep n fixed and double the side.
# 1. Read inputs; 2. relate values; 3. display and check.

import math

n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side length: "))
area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi / n))
print("The area of the polygon is", format(area,"10.3f"))
