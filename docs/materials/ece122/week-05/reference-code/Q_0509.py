# Sheet_05, Q_09
import random
# Function to find the sum of digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Main program
number = random.randint(1000, 9999)
print("Random 4-digit number =", number)

# Find and display the sum of its digits
digit_sum = sum_of_digits(number)
print("Sum of digits =", digit_sum)

