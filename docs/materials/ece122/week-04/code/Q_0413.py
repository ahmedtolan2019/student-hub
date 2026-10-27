# Sheet (4), Q #13
num = int(input("Enter an integer: "))
if num < 2:
    print("Not a prime number")
else:
    count = 0
    i = 2
    while i < num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 0:
        print("Prime number")
    else:
        print("Not a prime number")
