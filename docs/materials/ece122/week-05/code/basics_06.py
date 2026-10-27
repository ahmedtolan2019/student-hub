number = 4827
total = 0
while number > 0:
    total += number % 10
    number //= 10
print(total)
