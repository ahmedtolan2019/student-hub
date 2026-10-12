# Sheet (2), Q #08
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Gravity and scientific notation
# HAVE: m1, m2, d; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: F = G*m1*m2/d**2.
# CHECK: Double only distance and compare forces.
# 1. Read inputs; 2. relate values; 3. display and check.

G = 6.6743e-11
M1 = eval(input("Enter the mass of the first body: "))
M2 = eval(input("Enter the mass of the second body: "))
d = eval(input("Enter the distance between the two bodies: "))

force = G * M1 * M2 / d**2
print("The force between the two bodies = ",format(force,"10.3e"),"Newtons")
