# Sheet (2), Q #10
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: ASCII number to character
# HAVE: code; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Print chr(code) with a label.
# CHECK: Test the first and last values in the range.
# 1. Read inputs; 2. relate values; 3. display and check.

code = eval(input("Enter an ASCII code (32 : 126): "))
# Print the equivalent character
print("The character is", chr(code))
