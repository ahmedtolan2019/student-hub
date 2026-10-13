# Sheet (3), Q #13
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     how the two circles relate
#   HAVE     centre and radius of each circle
#   CONVERT  none
#   RELATE   d between centres; containment: d + r2 ≤ r1; overlap or touch: d ≤ r1 + r2; otherwise separate
#   CHECK    swap the circles: the containment direction must flip

import math

# 1. read both circles
x1, y1, r1 = eval(input("Circle 1: x,y,r: "))
x2, y2, r2 = eval(input("Circle 2: x,y,r: "))

# 2. distance between the centres
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# 3. ask in order: invalid, same, inside, overlap; else separate
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
