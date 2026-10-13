"""Week 3 worked examples. Plain Python; no installation or imports needed.

Indexes refer to the supplied list. Neither search changes that list.
"""


def linear_search(ids, target):
    # INPUT: list of integer IDs and an integer target; any order, even empty.
    # OUTPUT: first matching index, or -1 if absent. The list is unchanged.
    # INVARIANT: before inspecting i, no earlier position matches target.
    # TERMINATION: each mismatch advances one position toward the end.
    # ANALYSIS: n = len(ids); worst time O(n), auxiliary space O(1).
    # TESTS: first, last, absent, empty and duplicate IDs.
    # 1. Visit each position in order.
    for i in range(len(ids)):
        # 2. Stop at the first match.
        if ids[i] == target:
            return i
    # 3. Report absence only after checking every position.
    return -1


def binary_search(ids, target):
    # INPUT: list of integer IDs and an integer target; empty input is valid.
    # OUTPUT: a matching index, or -1 if absent. The list is unchanged.
    # PRECONDITION: caller supplies sorted data. We do not sort or validate it.
    # DUPLICATES: this version may return any matching index, not the first.
    # INVARIANT: every possible match is inside the inclusive low..high range.
    # TERMINATION: every non-returning iteration strictly shrinks the range.
    # ANALYSIS: n = len(ids); worst time O(log n) for n >= 2, extra space O(1).
    # TESTS: first, last, absent, empty, singleton and duplicate IDs.
    # 1. Keep an inclusive interval of candidate indexes.
    low = 0
    high = len(ids) - 1
    while low <= high:
        # 2. Inspect the middle candidate.
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        # 3. Exclude the checked middle and an impossible half.
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # 4. No candidates remain.
    return -1
