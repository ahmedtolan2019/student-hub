# Optional extension C. Ascending IDs; any duplicate match is acceptable.
# No sorting inside this function. Do not use slicing or recursion.
# INDEPENDENT ATTEMPT
# Fold the worked function with the arrow beside its def line number in PyCharm.
# Keep the definition: folding hides its body without disabling it.
# Write your own loop, run the tests, then explain aloud:
# why input must be sorted; why each boundary update shrinks the interval.
# EARLY FINISHER: write pseudocode, trace a case and add a test.
# The full specification/design/correctness/analysis cycle is on the whiteboard.

def find_sorted(ids, target):
    # TODO: maintain low and high; inspect mid; shrink the interval.
    return -1


print(find_sorted([17, 23, 42, 58, 63, 71, 86], 71))  # expected: 5
print(find_sorted([17, 23, 42, 58, 63, 71, 86], 60))  # expected: -1
print(find_sorted([17], 17))                        # expected: 0
print(find_sorted([], 17))                          # expected: -1
