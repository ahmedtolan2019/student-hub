# Sheet (2), Q #08
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the gravitational force in newtons
#   HAVE     G, two masses in kg, the distance in m
#   CONVERT  the distance must be in metres to match G
#   RELATE   F = G·m1·m2/d² (the printed sheet omits the square)
#   CHECK    Earth and Moon give 1.973e+20 N, close to the sheet’s 1.973e20

# 1. the constant, then the masses and the distance
G = 6.6743e-11
M1 = eval(input("Enter the mass of the first body: "))
M2 = eval(input("Enter the mass of the second body: "))
d = eval(input("Enter the distance between the two bodies: "))

# 2. inverse-square law
force = G * M1 * M2 / d**2

# 3. show the force
print("The force between the two bodies = ",format(force,"10.3e"),"Newtons")
