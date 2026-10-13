# Sheet (2), Q #07
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the length of arc ABC in inches
#   HAVE     a = 8 half the base, h = 13 the height
#   CONVERT  ln is math.log
#   RELATE   x1 = √(a²+4h²), x2 = a²/(2h), x3 = 2h/a, L = x1 + x2·ln(x3 + √(x3²+1))
#   CHECK    longer than AB+BC and shorter than 2a + 2h: 30.53 < 31.87 < 42.00

import math     # import math module to use the math functions

# 1. read the half-base and height
a, h = eval(input("Enter the values of a and h: "))

# 2. the repeated parts of the formula
x1 = math.sqrt(a**2 + 4*h**2)
x2 = a**2 / (2*h)
x3 = 2*h/a

# 3. combine them into the arc length
L_ABC= x1 + x2 * math.log( x3 + math.sqrt(x3**2+1))

# 4. show the arc length
print("Length of arc ABC =", format(L_ABC,"<10.2f"))
