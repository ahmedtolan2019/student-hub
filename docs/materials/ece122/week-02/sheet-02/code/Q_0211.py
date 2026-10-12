# Sheet (2), Q #11
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Character to ASCII number
# HAVE: character; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: This exercise is ASCII; choose a character in its range, not arbitrary Unicode.
# CHECK: Compare uppercase and lowercase.
# 1. Read inputs; 2. relate values; 3. display and check.

Chr = input("Enter one printable ASCII character: ")
# Print the corresponding decimal ASCII code
print("The corresponding decimal ASCII code is", ord(Chr))
