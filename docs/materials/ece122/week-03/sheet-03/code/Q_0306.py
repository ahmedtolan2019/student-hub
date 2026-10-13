# Sheet (3), Q #06
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the x and y that satisfy both equations
#   HAVE     a1, b1, c1, a2, b2, c2
#   CONVERT  none
#   RELATE   D = a1·b2 − b1·a2; if D ≠ 0: x = (c1·b2 − b1·c2)/D, y = (a1·c2 − c1·a2)/D
#   CHECK    substitute x and y back into both original equations

# 1. read the coefficients
a1, b1, c1, a2, b2, c2 = eval(input("Enter values for a1, b1, c1, a2, b2, c2: "))

# 2. the determinant decides if there is one solution
D = a1 * b2 - b1 * a2

# 3. solve only when D is not zero
if D != 0:
    x = (c1 * b2 - b1 * c2) / D
    y = (a1 * c2 - c1 * a2) / D
    print("The solution to the equation is X =", x, "Y =", y)

else:
    print("The equation has no solution")
