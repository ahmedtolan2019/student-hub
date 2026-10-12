# Sheet (2), Q #06
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Arc length from a and b
# HAVE: a, b; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: L=0.5*x1+x2*log((4*a+x1)/b).
# CHECK: Double all lengths. Does arc length double?
# 1. Read inputs; 2. relate values; 3. display and check.

import math     # import math module to use the math functions

a, b = eval(input("Enter the values of a and b: "))
x1 = math.sqrt(b**2 + 16*a**2)
x2 = b**2/(8*a)
L_ABC= 1/2* x1 + x2 * math.log((4*a + x1)/b)
print("Length of arc ABC =", format(L_ABC,"<10.2f"))
