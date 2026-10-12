# Sheet (2), Q #04
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Triangle coordinates, sides and angles
# HAVE: x1, y1, x2, y2, x3, y3; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: A = degrees(acos((b*b+c*c-a*a)/(2*b*c))).
# CHECK: Translate all vertices equally. Do lengths and angles change?
# 1. Read inputs; 2. relate values; 3. display and check.

import math

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

print("Side lengths:", a, b, c)

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are ", "A = ", format(A,"<10.2f"), "B = ",
      format(B,"<10.2f"), "C = ", format(C,"<10.2f"))
