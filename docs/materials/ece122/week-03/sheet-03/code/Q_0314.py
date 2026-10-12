# Sheet (3), Q #14
# Learning version; see the Guide note for differences from the reference.
# PLAN
# WANT: Units and category boundaries
# HAVE: weight, height; units and valid domain are in the Guide.
# CONVERT: Keep the units named in this question.
# RELATE: Test <18.5, then <25, then <30, then else.
# CHECK: Test all three exact thresholds and zero height.
# 1. Read inputs; 2. relate values; 3. display and check.

weight = eval(input("Weight in kg: "))
height = eval(input("Height in metres: "))
if height <= 0 or weight <= 0:
    print("Invalid weight or height")
else:
    bmi = weight / height**2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print("BMI:", format(bmi, ".1f"), category)
