# Sheet (3), Q #02
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the package with the lower price per kg, or a tie
#   HAVE     weight and price of each package
#   CONVERT  both weights in kg, both prices in the same currency
#   RELATE   u1 = p1/w1, u2 = p2/w2; the lower one wins
#   CHECK    2 kg for 60 vs 3 kg for 105 → package 1; 2 for 60 vs 3 for 90 → tie

# 1. read both packages
w1, p1 = eval(input("Weight kg, price for package 1: "))
w2, p2 = eval(input("Weight kg, price for package 2: "))

# 2. reject a weight that is not positive
if w1 <= 0 or w2 <= 0:
    print("Invalid weight")
else:
    # 3. price per kilogram of each
    pricePerKilo1 = p1 / w1
    pricePerKilo2 = p2 / w2
    print("Price per kg:", pricePerKilo1, pricePerKilo2)

    # 4. ask in order: 1 cheaper? 2 cheaper? otherwise a tie
    if pricePerKilo1 < pricePerKilo2:
        print("Package 1 has a better price")
    elif pricePerKilo2 < pricePerKilo1:
        print("Package 2 has a better price")
    else:
        print("Equal unit price")
