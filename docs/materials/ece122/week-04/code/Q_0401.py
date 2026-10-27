# Sheet (4), Q #01
# Learning version: accepts decimal input too.
total = 0.0
i = 0
while i < 10:
    num = float(input("Enter number: "))
    total = total + num
    i = i + 1

average = total / 10
print("Average =", format(average, ".3f"))
