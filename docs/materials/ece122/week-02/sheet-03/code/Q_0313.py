# Sheet (3), Q #13
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Two-circle relationship
# HAVE: x1, y1, r1, x2, y2, r2; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Without containment, d<=r1+r2 means overlap or touch.
# CHECK: Swap large and small circles; containment direction must reverse.
# 1. Read inputs; 2. relate values; 3. display and check.

import math
x1, y1, r1 = eval(input("Circle 1: x,y,r: "))
x2, y2, r2 = eval(input("Circle 2: x,y,r: "))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
if r1 <= 0 or r2 <= 0:
    print("Invalid radius")
elif distance == 0 and r1 == r2:
    print("Coincident circles")
elif distance + r2 <= r1:
    print("circle2 is inside circle1, internal touch included")
elif distance + r1 <= r2:
    print("circle1 is inside circle2, internal touch included")
elif distance <= r1 + r2:
    print("Circles overlap or touch externally")
else:
    print("Separate circles")
