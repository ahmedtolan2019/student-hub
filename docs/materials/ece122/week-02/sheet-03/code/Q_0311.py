# Sheet (3), Q #11
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Point in a rectangle
# HAVE: x, y; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Combine inside tests with and.
# CHECK: Test a corner and a point beyond one edge.
# 1. Read inputs; 2. relate values; 3. display and check.

x, y = eval(input("Enter x,y: "))
if abs(x) <= 10/2 and abs(y) <= 5/2:
    print("Inside rectangle, boundary included")
else:
    print("Outside rectangle")
