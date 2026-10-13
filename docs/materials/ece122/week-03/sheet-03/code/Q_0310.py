# Sheet (3), Q #10
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     whether the point is inside the circle
#   HAVE     x and y; the circle has centre (0, 0) and radius 10
#   CONVERT  none
#   RELATE   d = √(x² + y²); inside if d ≤ 10 (the edge counts)
#   CHECK    (6, 8) is exactly on the edge: d = 10.0

import math

# 1. read the point
x, y = eval(input("Enter a point with two coordinates: "))

# 2. distance from the centre
d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# 3. compare with the radius, edge included
if d > 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is out of the circle")

elif d <= 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is in the circle")
