# Sheet (4), Q #14
a = abs(int(input("Enter the first integer: ")))
b = abs(int(input("Enter the second integer: ")))
if a == 0 and b == 0:
    print("No greatest positive divisor for 0 and 0.")
else:
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    print("GCD =", a)
