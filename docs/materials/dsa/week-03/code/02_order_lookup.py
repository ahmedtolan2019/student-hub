# Week 3 worked example. searches.py must stay in the same folder.
from searches import linear_search

ids = [42, 17, 63, 23]
target = 63
position = linear_search(ids, target)

# Check -1 explicitly. Index 0 is a valid success.
if position == -1:
    print("Order not found")
else:
    print("Found at index:", position)
    print("Order ID:", ids[position])
