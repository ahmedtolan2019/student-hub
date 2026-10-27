# Sheet_05, Q_08
# Function to calculate the sum of a GP series
def gp_sum(a, r, n):
    total = 0
    for i in range(n):
        total += a * (r ** i)
    return total

# Main program
a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

# Calculate and display the sum
result = gp_sum(a, r, n)
print(f"Sum of the GP series = {result}")

