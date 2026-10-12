# Sheet (3), Q #12
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Point in a right triangle
# HAVE: x, y; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: x>=0 and y>=0 and y<=-0.5*x+100.
# CHECK: Test on the hypotenuse, above it and with a negative coordinate.
# 1. Read inputs; 2. relate values; 3. display and check.

# Prompt the user to enter a point's coordinates
x, y = eval(input("Enter a point with two coordinates (x,y): "))

# Check if the point satisfies all three boundaries of the triangle
if x >= 0 and y >= 0 and y <= (-0.5 * x + 100):
    print(f"The point ({x}, {y}) is INSIDE the triangle.")
else:
    print(f"The point ({x}, {y}) is OUTSIDE the triangle.")
