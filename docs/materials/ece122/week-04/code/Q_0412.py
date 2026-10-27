# Sheet (4), Q #12
x = float(input("Enter x: "))
total = 0.0
for i in range(16):
    fact = 1
    for j in range(2, i + 1):
        fact = fact * j
    total = total + (x ** i) / fact

print("Approximation through degree 15 =",
      format(total, ".8f"))
