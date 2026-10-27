# Sheet_05, Q_03
# Function to swap two integers
def swap_numbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

# Main program
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Display numbers before swapping
print("\nBefore swapping:")
print(f"First number: {number1} and Second number: {number2}")

# Call the swap_numbers function
number1, number2 = swap_numbers(number1, number2)

# Display numbers after swapping
print("\nAfter swapping:")
print(f"First number: {number1} and Second number: {number2}")
