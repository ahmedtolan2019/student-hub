# Sheet_05, Q_12
# Function to calculate the sum of four arguments with default values
def calculate_sum(arg1=0, arg2=0, arg3=0, arg4=0):
    return arg1 + arg2 + arg3 + arg4

# Main program
# Calling the function with all arguments explicitly assigned
sum1 = calculate_sum(10, 20, 30, 40)
print(f"Sum 1 (all arguments assigned): {sum1}")

# Calling the function with some arguments assigned, others using default values
sum2 = calculate_sum(5, 15)
print(f"Sum 2 (first two arguments assigned): {sum2}")

# Calling the function with only one argument assigned
sum3 = calculate_sum(100)
print(f"Sum 3 (first argument assigned): {sum3}")

# Calling the function with no arguments, all using default values
sum4 = calculate_sum()
print(f"Sum 4 (no arguments assigned): {sum4}")
