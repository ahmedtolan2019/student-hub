# Week 3 worked example. Predict each print before running.
ids = [42, 17, 63, 23]
print("Start:", ids)
print("Index 1:", ids[1])
ids[1] = 18
print("Replace:", ids)
ids.append(71)
print("Append:", ids)
ids.insert(1, 99)
print("Insert:", ids)
removed = ids.pop(2)
print("Removed:", removed)
print("Remaining:", ids)
