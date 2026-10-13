# Sheet (2), Q #01
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     area of the regular pentagon (square length units), and its side
#   HAVE     r: centre-to-vertex distance, a positive length
#   CONVERT  angles in radians: a full turn is 2π
#   RELATE   five triangles with two sides r and angle 2π/5 between them: A = 5/2·r²·sin(2π/5); side s = 2r·sin(π/5)
#   CHECK    double r: the area is multiplied by 4 (area(4) / area(2) = 4.0)

import math

# 1. read the radius
r = eval(input("Enter the length from the center to a vertex: "))

# 2. side and area from the five central triangles
s = 2 * r * math.sin(math.pi / 5)
area = 5/2 * math.pow(r,2) * math.sin(2/5*math.pi)

# 3. show both results
print("The side length is", format(s,"10.3f"))
print("The area of the pentagon is", format(area,"10.3f"))
