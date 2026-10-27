# Sheet (4), Q #11
import math
print(f"{'n':>4} {'pi':>10}")
for n in range(100, 601, 100):
    total = 0.0
    for j in range(1, n + 1):
        total = total + 1.0 / (j * j)
    pi_approx = math.sqrt(6.0 * total)
    print(f"{n:>4} {pi_approx:>10.6f}")
