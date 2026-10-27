# Sheet (4), Q #07
num = abs(int(input("Enter an integer: ")))
if num == 0:
    prod = 0
else:
    prod = 1
    while num != 0:
        digit = num % 10
        prod = prod * digit
        num = num // 10

print("Product of digits =", prod)
