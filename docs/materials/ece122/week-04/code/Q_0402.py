# Sheet (4), Q #02
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Enter a non-negative integer.")
else:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print("Factorial =", fact)
