# Optional extension C. Ascending IDs; any duplicate match is acceptable.
# No sorting inside this function. Do not use slicing or recursion.
# ALGORITHM DESIGN (complete before implementation)
# Specification: inputs, output, preconditions, postconditions, mutation.
# Pseudocode: language-independent steps using the board's notation.
# Correctness: why the result follows; why the algorithm terminates.
# Analysis: define n; worst-case time and auxiliary space, with reasons.
# Test cases: inputs -> expected results, including boundary cases.

def find_sorted(ids, target):
    # TODO: maintain low and high; inspect mid; shrink the interval.
    return -1


print(find_sorted([17, 23, 42, 58, 63, 71, 86], 71))  # expected: 5
print(find_sorted([17, 23, 42, 58, 63, 71, 86], 60))  # expected: -1
print(find_sorted([17], 17))                        # expected: 0
print(find_sorted([], 17))                          # expected: -1
