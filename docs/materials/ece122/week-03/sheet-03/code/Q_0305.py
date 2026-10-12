# Sheet (3), Q #05
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Currency conversion and units
# HAVE: rate, direction, amount; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: rate must be positive; other directions are invalid.
# CHECK: Convert an amount and reverse it using the same rate.
# 1. Read inputs; 2. relate values; 3. display and check.

exchange_rate = eval(input("Exchange rate, EGP per USD: "))
conversion = eval(input("0: USD to EGP, 1: EGP to USD: "))
amount = eval(input("Amount to convert: "))
if exchange_rate <= 0:
    print("Invalid exchange rate")
elif conversion == 0:
    EGP = amount * exchange_rate
    print(format(EGP, ".2f"), "EGP")
elif conversion == 1:
    USD = amount / exchange_rate
    print(format(USD, ".2f"), "USD")
else:
    print("Invalid direction")
