def bmi(weight, height):
    #your code here
    final_bmi = weight/height**2
    if final_bmi <= 18.5:
        return "Underweight"
    elif final_bmi <= 25.0:
        return "Normal"
    elif final_bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(80, 1.80))
print(bmi(80, 1.60))
print(bmi(90, 1.80))
print(bmi(70, 1.70))