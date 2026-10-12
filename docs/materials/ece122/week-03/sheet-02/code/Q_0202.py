# Sheet (2), Q #02
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Pentagon from its side
# HAVE: s; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Divide 5*s**2 by (4*tan(pi/5)).
# CHECK: Double s and compare areas.
# 1. Read inputs; 2. relate values; 3. display and check.

import math

s = eval(input("Enter the side length: "))
area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is", format(area,"10.3f"))
