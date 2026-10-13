# Core practice A. Implement the first-match contract from the whiteboard.
# Do not use .index(), 'in' as a search shortcut, or an imported search.
# ALGORITHM DESIGN (complete before implementation)
# Specification: inputs, output, preconditions, postconditions, mutation.
# Pseudocode: language-independent steps using the board's notation.
# Correctness: why the result follows; why the algorithm terminates.
# Analysis: define n; worst-case time and auxiliary space, with reasons.
# Test cases: inputs -> expected results, including boundary cases.

def find_order(ids, target):
    # TODO: replace this placeholder with your loop and decisions.
    return -1


# Predict, then run. Add at least one test of your own.
print(find_order([42, 17, 63, 23], 63))  # expected: 2
print(find_order([42, 17, 63, 23], 42))  # expected: 0
print(find_order([42, 17, 63, 23], 99))  # expected: -1
print(find_order([], 42))              # expected: -1
print(find_order([17, 42, 17], 17))     # expected: 0
