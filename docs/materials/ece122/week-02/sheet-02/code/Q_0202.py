# Sheet (2), Q #02
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     area of the pentagon (square units)
#   HAVE     s: the side length
#   CONVERT  π/5 in radians, not 36 degrees, inside tan
#   RELATE   apothem = s/(2·tan(π/5)); area = ½ × perimeter × apothem = 5s²/(4·tan(π/5))
#   CHECK    s = 2 gives 6.882, the same as Q1 with the matching radius

import math

# 1. read the side
s = eval(input("Enter the side length: "))

# 2. area from perimeter and apothem
area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))

# 3. show the area
print("The area of the pentagon is", format(area,"10.3f"))
