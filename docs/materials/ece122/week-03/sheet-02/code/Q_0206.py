# Sheet (2), Q #06
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the length of arc ABC in inches
#   HAVE     a = 11 the height, b = 9 the full base width
#   CONVERT  ln is math.log
#   RELATE   x1 = √(b²+16a²), x2 = b²/(8a), L = ½·x1 + x2·ln((4a+x1)/b)
#   CHECK    the arc is longer than AB+BC and shorter than b + 2a: 23.77 < 24.56 < 31.00

import math     # import math module to use the math functions

# 1. read the height and base
a, b = eval(input("Enter the values of a and b: "))

# 2. the repeated parts of the formula
x1 = math.sqrt(b**2 + 16*a**2)
x2 = b**2/(8*a)

# 3. combine them into the arc length
L_ABC= 1/2* x1 + x2 * math.log((4*a + x1)/b)

# 4. show the arc length
print("Length of arc ABC =", format(L_ABC,"<10.2f"))
