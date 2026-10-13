# Independent practice B. Copy YOUR tested find_order into this file.
# Cancel only the first matching ID. Change the supplied list in place.
# Return True if removed, False if absent. Preserve all other IDs and order.
# ALGORITHM DESIGN (complete before implementation)
# Specification: inputs, output, preconditions, postconditions, mutation.
# Pseudocode: language-independent steps using the board's notation.
# Correctness: why the result follows; why the algorithm terminates.
# Analysis: define n; worst-case time and auxiliary space, with reasons.
# Test cases: inputs -> expected results, including boundary cases.

def cancel_order(ids, target):
    # TODO: find the index, guard -1, then remove that position.
    return False


orders = [42, 17, 63, 17]
print(cancel_order(orders, 17))  # expected: True
print(orders)                   # expected: [42, 63, 17]
print(cancel_order(orders, 99))  # expected: False
print(orders)                   # expected: [42, 63, 17], unchanged
print(cancel_order([], 99))     # expected: False
