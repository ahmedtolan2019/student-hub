# Sheet_05, Q_04
import math
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False

    # Check for divisibility from 2 up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

# Main program
number = int(input("Enter an integer: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
