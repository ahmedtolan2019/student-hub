# Sheet (3), Q #06
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Two equations and two unknowns
# HAVE: a1, b1, c1, a2, b2, c2; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: x=(c1*b2-b1*c2)/D and y=(a1*c2-c1*a2)/D.
# CHECK: Try parallel lines, then one equation multiplied by a constant.
# 1. Read inputs; 2. relate values; 3. display and check.

a1, b1, c1, a2, b2, c2 = eval(input("Enter values for a1, b1, c1, a2, b2, c2: "))
D = a1 * b2 - b1 * a2

if D != 0:
    x = (c1 * b2 - b1 * c2) / D
    y = (a1 * c2 - c1 * a2) / D
    print("The solution to the equation is X =", x, "Y =", y)

else:
    print("The equation has no solution")
