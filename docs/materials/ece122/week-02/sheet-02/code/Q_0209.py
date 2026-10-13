# Sheet (2), Q #09
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the great-circle distance in km
#   HAVE     latitude and longitude of each airport in degrees; R = 6371.01 km
#   CONVERT  west is negative; every angle to radians before sin and cos
#   RELATE   central angle = acos(...); distance = R × angle
#   CHECK    swap the airports: the same distance. Cairo–London 3533.53 km

import math

# 1. read both points in degrees
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
radius = 6371.01

# 2. cosine of the central angle, angles in radians
d1 = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
d2 = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2))

# 3. arc length = radius × angle
distance = radius * math.acos(d1 + d2)

# 4. show the distance
print("The distance between the two points is", format(distance,"10.2f"), "km")
