# Sheet (3), Q #09
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the three angles in degrees, or an invalid message
#   HAVE     three lengths a, b, c
#   CONVERT  acos returns radians: degrees for printing
#   RELATE   the same validity test, then the cosine law for each angle
#   CHECK    the angles add to 180; 2, 2, 2 gives 60 each

import math

# 1. read the sides
a, b, c = eval(input("Enter the side lengths of the triangle a, b, and c: "))

# 2. only a real triangle has angles
if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    # 3. cosine law for each angle
    A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
    B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
    C = math.acos((c * c - b * b - a * a) / (-2 * a * b))

    # 4. show the angles in degrees
    print("The three interior angles in degrees:")
    print("Angle A = ",format(math.degrees(A),"<8.2f"))
    print("Angle B = ",format(math.degrees(B),"<8.2f"))
    print("Angle C = ",format(math.degrees(C),"<8.2f"))
else:
    print("Invalid triangle")
