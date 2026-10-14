# Core practice A. Implement the first-match contract from the whiteboard.
# Do not use .index(), 'in' as a search shortcut, or an imported search.
# INDEPENDENT ATTEMPT
# Fold the worked function with the arrow beside its def line number in PyCharm.
# Keep the definition: folding hides its body without disabling it.
# Write your own loop, run the tests, then explain aloud:
# why return -1 is outside the loop; why worst-case work grows with n.
# EARLY FINISHER: write pseudocode, trace a case and add a test.
# The full specification/design/correctness/analysis cycle is on the whiteboard.

def find_order(ids, target):
    # TODO: replace this placeholder with your loop and decisions.
    return -1


# Predict, then run. Add at least one test of your own.
print(find_order([42, 17, 63, 23], 63))  # expected: 2
print(find_order([42, 17, 63, 23], 42))  # expected: 0
print(find_order([42, 17, 63, 23], 99))  # expected: -1
print(find_order([], 42))              # expected: -1
print(find_order([17, 42, 17], 17))     # expected: 0
