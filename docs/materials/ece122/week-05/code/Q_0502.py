# Sheet_05, Q_02
# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Main program
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform operations using functions and display results
print("Sum:", add(number1, number2))
print("Difference:", subtract(number1, number2))
print("Product:", multiply(number1, number2))
