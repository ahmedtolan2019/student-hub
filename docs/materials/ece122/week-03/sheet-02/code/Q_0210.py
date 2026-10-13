# Sheet (2), Q #10
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the character for the given code
#   HAVE     a whole number from 32 to 126
#   CONVERT  none
#   RELATE   chr(code)
#   CHECK    97 → a; 32 → a space (present but invisible)

# 1. read the code
code = eval(input("Enter an ASCII code (32 : 126): "))

# 2. show its character
print("The character is", chr(code))
