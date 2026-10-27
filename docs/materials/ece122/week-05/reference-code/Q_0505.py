# Sheet_05, Q_05
import math
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

# Main program
lower_value = int(input("Enter the lower value of the range: "))
upper_value = int(input("Enter the upper value of the range: "))

if lower_value > upper_value:
    print("Error: Lower value cannot be greater than upper value.")
else:
    print(f"Prime numbers between {lower_value} and {upper_value} are: ", end="")

    for i in range(lower_value, upper_value + 1):
        if is_prime(i):
            print(i, end=" ")

    print()
    
    