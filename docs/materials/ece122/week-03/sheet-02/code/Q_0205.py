# Sheet (2), Q #05
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Ellipse perimeter
# HAVE: a, b; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: p = pi*(3*(a+b)-sqrt((3*a+b)*(a+3*b))).
# CHECK: Set a=b and check against circle circumference.
# 1. Read inputs; 2. relate values; 3. display and check.

import math     # import math module to use the math functions

a, b = eval(input("Enter the values of a and b: "))
PI = math.pi
p = PI*(3*(a+b)-((3*a+b)*(a+3*b))**(0.5))
print("Perimeter of the ellipse =", format(p,"<10.2f"))
