# Sheet (3), Q #05
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the amount in the other currency
#   HAVE     the rate (EGP per USD), the direction 0 or 1, the amount
#   CONVERT  units: USD × EGP/USD = EGP
#   RELATE   0: multiply by the rate. 1: divide by it
#   CHECK    convert and convert back with the same rate: you must get the same amount

# 1. read rate, direction and amount
exchange_rate = eval(input("Exchange rate, EGP per USD: "))
conversion = eval(input("0: USD to EGP, 1: EGP to USD: "))
amount = eval(input("Amount to convert: "))

# 2. reject a rate that is not positive
if exchange_rate <= 0:
    print("Invalid exchange rate")

# 3. convert in the chosen direction
elif conversion == 0:
    EGP = amount * exchange_rate
    print(format(EGP, ".2f"), "EGP")
elif conversion == 1:
    USD = amount / exchange_rate
    print(format(USD, ".2f"), "USD")
else:
    print("Invalid direction")
