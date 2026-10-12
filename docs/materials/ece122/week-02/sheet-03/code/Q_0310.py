# Sheet (3), Q #10
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Point in a circle
# HAVE: x, y; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: d<=10 is included; larger is outside.
# CHECK: Change the sign of x or y. Does distance change?
# 1. Read inputs; 2. relate values; 3. display and check.

import math
x, y = eval(input("Enter a point with two coordinates: "))

d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

if d > 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is out of the circle")

elif d <= 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is in the circle")
