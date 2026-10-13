# Sheet (2), Q #11
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the decimal ASCII code of a character
#   HAVE     one printable character
#   CONVERT  input() already returns text: no eval needed
#   RELATE   ord(ch)
#   CHECK    @ → 64, and chr(ord(ch)) gives the same character back

# 1. read one character as text
Chr = input("Enter one printable ASCII character: ")

# 2. show its code
print("The corresponding decimal ASCII code is", ord(Chr))
