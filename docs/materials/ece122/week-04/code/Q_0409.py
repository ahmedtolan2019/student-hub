# Sheet (4), Q #09
# Learning version follows the printed series.
n = int(input("Enter a positive integer n: "))
if n < 1:
    print("n must be positive.")
else:
    total = 0.0
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        total = total + 1 / fact
        i += 1
    print("Sum =", format(total, ".6f"))
