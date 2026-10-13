# Optional extension. Use ascending order before calling binary_search.
from searches import binary_search

ids = [17, 23, 42, 58, 63, 71, 86]
position = binary_search(ids, 71)
print("Found at index:", position)
print("Missing ID:", binary_search(ids, 60))
print("Empty list:", binary_search([], 71))
