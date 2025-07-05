"""Description: Ask for height and weight, calculate BMI, and show health status. 
BMI = weight / (height^2)
Concepts Used: float(), if-else, math"""

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
