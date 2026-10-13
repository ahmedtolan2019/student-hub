# Sheet (2), Q #04
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     side lengths and inner angles in degrees
#   HAVE     three points (x, y)
#   CONVERT  acos returns radians: convert with degrees
#   RELATE   distance = sqrt(Δx² + Δy²); the cosine law for each angle
#   CHECK    the angles add to 180 (180.00); the triangle (0,0) (3,0) (0,4) has sides 5, 4, 3

import math

# 1. read the three vertices
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

# 2. side lengths from coordinate differences
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

# 3. show the sides
print("Side lengths:", a, b, c)

# 4. angles from the cosine law, converted to degrees
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

# 5. show the angles
print("The three angles are ", "A = ", format(A,"<10.2f"), "B = ",
      format(B,"<10.2f"), "C = ", format(C,"<10.2f"))
