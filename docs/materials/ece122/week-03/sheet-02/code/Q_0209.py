# Sheet (2), Q #09
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Latitude, longitude and distance
# HAVE: lat1, lon1, lat2, lon2; units and valid domain are in the Guide.
# CONVERT: Degrees to radians before trigonometry.
# RELATE: d = R*acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon1-lon2)).
# CHECK: Swap the cities. Does distance change?
# 1. Read inputs; 2. relate values; 3. display and check.

import math
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
radius = 6371.01

d1 = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
d2 = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2))
distance = radius * math.acos(d1 + d2)

print("The distance between the two points is", format(distance,"10.2f"), "km")
