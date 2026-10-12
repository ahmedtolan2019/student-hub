# Sheet (3), Q #02
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Price per kilogram
# HAVE: w1, p1, w2, p2; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Lower is better; equality means the same unit price.
# CHECK: Double one package’s weight and price. Does the ranking change?
# 1. Read inputs; 2. relate values; 3. display and check.

w1, p1 = eval(input("Weight kg, price for package 1: "))
w2, p2 = eval(input("Weight kg, price for package 2: "))
if w1 <= 0 or w2 <= 0:
    print("Invalid weight")
else:
    pricePerKilo1 = p1 / w1
    pricePerKilo2 = p2 / w2
    print("Price per kg:", pricePerKilo1, pricePerKilo2)
    if pricePerKilo1 < pricePerKilo2:
        print("Package 1 has a better price")
    elif pricePerKilo2 < pricePerKilo1:
        print("Package 2 has a better price")
    else:
        print("Equal unit price")
