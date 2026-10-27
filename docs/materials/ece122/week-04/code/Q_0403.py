# Sheet (4), Q #03
sum_p = 0.0
sum_n = 0.0
num = float(input("Enter a number, 0 to stop: "))
while num != 0:
    if num > 0:
        sum_p = sum_p + num
    else:
        sum_n = sum_n + num
    num = float(input("Enter a number, 0 to stop: "))

print("Sum of positive numbers =", sum_p)
print("Sum of negative numbers =", sum_n)
