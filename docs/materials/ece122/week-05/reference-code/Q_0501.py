# Sheet_05, Q_01
import math
# Function to calculate the cube of a number
def calculate_cube(num):
    result = math.pow(num, 3)
    return result

# Main program
number = float(input("Enter a number to find its cube: "))
result = calculate_cube(number)

# Display the result
print(f"The cube of {number} is: {result}")