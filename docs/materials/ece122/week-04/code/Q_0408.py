# Sheet (4), Q #08
original = int(input("Enter an integer: "))
sign = 1
if original < 0:
    sign = -1
num = abs(original)
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", sign * reverse)
