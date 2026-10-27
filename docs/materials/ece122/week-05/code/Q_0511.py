# Sheet_05, Q_11
# Function to display the terms of the harmonic series
def display_harmonic_series(n):
    print(f"\nHarmonic Series up to {n} terms:")
    for i in range(1, n + 1):
        print(f"1/{i}", end="")
        if i < n:
            print(" + ", end="")
    print()

# Function to calculate the sum of the harmonic series
def calculate_harmonic_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1.0 / i
    return total

# Main program
num_terms = int(input("Enter the number of terms (n) for the harmonic series: "))
if num_terms < 1:
    print("Error: number of terms must be at least 1.")
else:
    display_harmonic_series(num_terms)
    
    # Call the function to calculate the sum and display it
    harmonic_sum = calculate_harmonic_sum(num_terms)
    print(f"\nSum of the Harmonic Series up to {num_terms} terms: {harmonic_sum:.6f}")
