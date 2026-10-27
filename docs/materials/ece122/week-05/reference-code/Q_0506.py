# Sheet_05, Q_06
# Function to calculate the factorial of an integer
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Main program
number = int(input("Enter a positive integer: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")

