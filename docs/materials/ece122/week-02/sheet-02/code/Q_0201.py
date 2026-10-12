# Sheet (2), Q #01
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Pentagon from its radius
# HAVE: r; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Write A = 5/2 * r**2 * sin(2*pi/5).
# CHECK: If r doubles, how does area change? Compare the cases.
# 1. Read inputs; 2. relate values; 3. display and check.

import math

r = eval(input("Enter the length from the center to a vertex: "))
s = 2 * r * math.sin(math.pi / 5)
area = 5/2 * math.pow(r,2) * math.sin(2/5*math.pi)
print("The side length is", format(s,"10.3f"))
print("The area of the pentagon is", format(area,"10.3f"))
