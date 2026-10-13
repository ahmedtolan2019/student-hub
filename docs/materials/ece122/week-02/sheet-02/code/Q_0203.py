# Sheet (2), Q #03
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     area of a regular n-sided polygon
#   HAVE     n, a whole number ≥ 3, and the side s
#   CONVERT  π/n in radians
#   RELATE   n triangles, each ½·s·apothem, with apothem = s/(2·tan(π/n))
#   CHECK    n = 4, s = 2 must give the square’s area 4 (4.000)

import math

# 1. read the number of sides and the side
n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side length: "))

# 2. n triangles: area from side and apothem
area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi / n))

# 3. show the area
print("The area of the polygon is", format(area,"10.3f"))
