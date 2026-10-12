# Sheet (3), Q #07
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Quadratic equation
# HAVE: a, b, c; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: For negative D: real=-b/(2*a), imag=sqrt(-D)/(2*abs(a)).
# CHECK: Test positive, zero and negative D, plus a=0.
# 1. Read inputs; 2. relate values; 3. display and check.

import math
a, b, c = eval(input("Enter a, b, c: "))
if a == 0:
    print("Not a quadratic equation")
else:
    disc = b**2 - 4*a*c
    print("Discriminant:", disc)
    if disc > 0:
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
        print("Two real roots:", format(r1, ".2f"), format(r2, ".2f"))
    elif disc == 0:
        root = -b / (2*a)
        print("Repeated root:", format(root, ".2f"))
    else:
        realPart = -b / (2*a)
        imagPart = math.sqrt(-disc) / (2*abs(a))
        print("r1 =", format(realPart, ".2f"), "+ j", format(imagPart, ".2f"))
        print("r2 =", format(realPart, ".2f"), "- j", format(imagPart, ".2f"))
