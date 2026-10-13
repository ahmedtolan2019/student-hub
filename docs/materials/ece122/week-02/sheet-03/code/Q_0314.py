# Sheet (3), Q #14
# Learning version; see the Guide note for differences from the reference.
# PLAN
#   WANT     the BMI and its category from the sheet’s table
#   HAVE     weight in kg and height in metres
#   CONVERT  height in metres (the reference reads centimetres and divides by 100)
#   RELATE   bmi = weight / height²; ask < 18.5, then < 25, then < 30; the rest is else
#   CHECK    test the exact boundaries: 18.5, 25 and 30

# 1. read weight in kg and height in metres
weight = eval(input("Weight in kg: "))
height = eval(input("Height in metres: "))

# 2. reject impossible values
if height <= 0 or weight <= 0:
    print("Invalid weight or height")
else:
    # 3. BMI from metres
    bmi = weight / height**2

    # 4. first interval that fits; else is 30 and above
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print("BMI:", format(bmi, ".1f"), category)
