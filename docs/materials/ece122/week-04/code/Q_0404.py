# Sheet (4), Q #04
start = int(input("Enter the first bound: "))
end = int(input("Enter the second bound: "))
if start > end:
    temp = start
    start = end
    end = temp

even_sum = 0
odd_sum = 0
current = start
while current <= end:
    if current % 2 == 0:
        even_sum += current
    else:
        odd_sum += current
    current += 1

print("Even sum =", even_sum)
print("Odd sum =", odd_sum)
