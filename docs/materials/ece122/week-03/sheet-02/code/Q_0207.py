# Sheet (2), Q #07
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Arc length from a and h
# HAVE: a, h; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: L=x1+x2*log(x3+sqrt(x3**2+1)).
# CHECK: Compare the original case with both dimensions doubled.
# 1. Read inputs; 2. relate values; 3. display and check.

import math     # import math module to use the math functions

a, h = eval(input("Enter the values of a and h: "))
x1 = math.sqrt(a**2 + 4*h**2)
x2 = a**2 / (2*h)
x3 = 2*h/a
L_ABC= x1 + x2 * math.log( x3 + math.sqrt(x3**2+1))
print("Length of arc ABC =", format(L_ABC,"<10.2f"))


