# Sheet_05, Q_07
# Function to calculate the sum of an AP series
def ap_sum(a, d, n):
    total = 0
    for i in range(n):
        total += a + i * d
    return total

# Main program
a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

if n < 1:
    print("Error: number of terms must be at least 1.")
else:
    # Calculate and display the sum
    result = ap_sum(a, d, n)
    print(f"Sum of the AP series = {result}")
