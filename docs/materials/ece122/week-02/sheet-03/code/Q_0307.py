# Sheet (3), Q #07
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the kind of roots and their values
#   HAVE     a, b, c with a ≠ 0
#   CONVERT  none
#   RELATE   D = b² − 4ac; D > 0 two roots, D = 0 a repeated root, D < 0 two complex roots
#   CHECK    substitute each root into a·x² + b·x + c: it must give zero

import math

# 1. read the coefficients
a, b, c = eval(input("Enter a, b, c: "))

# 2. a must not be zero
if a == 0:
    print("Not a quadratic equation")
else:
    # 3. the discriminant chooses the kind of roots
    disc = b**2 - 4*a*c
    print("Discriminant:", disc)

    # 4. compute the roots for that kind
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
