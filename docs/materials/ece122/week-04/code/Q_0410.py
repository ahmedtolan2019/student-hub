# Sheet (4), Q #10
prod = 1.0
for n in range(5, 98, 4):
    term = 1.0 / n
    prod = prod * term

print("Product =", format(prod, ".6e"))
