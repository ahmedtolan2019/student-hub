# Sheet (4), Q #15
# PLAN
# WANT: coordinates of five vertices
# HAVE: radius; centre at (0, 0); first point at top
# CONVERT: degrees to radians
# RELATE: x = r*cos(angle), y = r*sin(angle)
# CHECK: x*x + y*y is approximately r*r
import math
radius = float(input("Enter a positive radius: "))
if radius <= 0:
    print("Radius must be positive.")
else:
    for i in range(5):
        # 1. Convert the next angle to radians.
        angle = math.radians(90 - i * 72)
        # 2. Compute the two coordinates.
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        print(f"Point {i+1}: ({x:.2f}, {y:.2f})")
