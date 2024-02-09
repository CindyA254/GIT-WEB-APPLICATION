#bmi = weight_kg / (height_m ** 2)

name = input("what is your name? ")
age = input("what is your age? ")
weight = input("what is your weight? ")
height = input("what is your height? ")
BMI = (float(weight)+float(height))/2
print(BMI)
if BMI < 18:
    print(" Underweight")
elif 18 <= BMI < 24:
     print(" Normal weight")
elif 25 <= BMI < 30:
    print(" Overweight")
else:
    print(" abnornam overweight")


