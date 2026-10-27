# Sheet_05, Q_10
# A function to calculate factorial in each term
def calculate_factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, k + 1):
            factorial *= i
        return factorial

# A function to calculate the sum of the series
def series_sum(x, n):
    total = 0

    for i in range(1, n + 1, 2):  # Odd powers only
        total += (x ** i) / calculate_factorial(i)

    return total

# Main program
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n (odd): "))

# Calculate and display the sum
result = series_sum(x, n)
print(f"Sum of the series = {result:.6f}")

