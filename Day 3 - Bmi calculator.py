height = float(input("Enter your height in meters\n"))
weight = int(input("Enter your weight in kilograms\n"))
bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
if bmi < 25:
    print(f"Your BMI is {bmi}, you are overweight")
else:
    print(f"Your BMI is {bmi}, you are perfectly weighted")