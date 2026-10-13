# Sheet (3), Q #11
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     whether the point is inside the rectangle
#   HAVE     x and y; the rectangle is centred at (0, 0), width 10, height 5
#   CONVERT  half-width 5 and half-height 2.5
#   RELATE   inside if abs(x) ≤ 5 and abs(y) ≤ 2.5
#   CHECK    (2, 2) inside, (6, 4) outside, the corner (-5, -2.5) inside

# 1. read the point
x, y = eval(input("Enter x,y: "))

# 2. both distances within half the size
if abs(x) <= 10/2 and abs(y) <= 5/2:
    print("Inside rectangle, boundary included")
else:
    print("Outside rectangle")
