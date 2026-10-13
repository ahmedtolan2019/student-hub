# Sheet (2), Q #05
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the ellipse perimeter in inches (approximate)
#   HAVE     a = 18 and b = 7: the semi-axes
#   CONVERT  the same unit for both (inches)
#   RELATE   p = π·(3(a+b) − √((3a+b)(a+3b)))
#   CHECK    if a = b it is a circle: p = 2πa (43.98 = 43.98)

import math     # import math module to use the math functions

# 1. read the semi-axes
a, b = eval(input("Enter the values of a and b: "))

# 2. perimeter from the approximation
PI = math.pi
p = PI*(3*(a+b)-((3*a+b)*(a+3*b))**(0.5))

# 3. show the perimeter
print("Perimeter of the ellipse =", format(p,"<10.2f"))
