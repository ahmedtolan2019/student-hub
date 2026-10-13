# Sheet (3), Q #12
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     whether the point is inside the triangle
#   HAVE     x and y; the vertices (0, 0), (200, 0), (0, 100)
#   CONVERT  none
#   RELATE   x ≥ 0 and y ≥ 0 and y ≤ −0.5x + 100
#   CHECK    (100, 50) is on the slanted edge: inside; (100, 60) above it: outside

# 1. read the point
x, y = eval(input("Enter a point with two coordinates (x,y): "))

# 2. all three edges at once
if x >= 0 and y >= 0 and y <= (-0.5 * x + 100):
    print(f"The point ({x}, {y}) is INSIDE the triangle.")
else:
    print(f"The point ({x}, {y}) is OUTSIDE the triangle.")
