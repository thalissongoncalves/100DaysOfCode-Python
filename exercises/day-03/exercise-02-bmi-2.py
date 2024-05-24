# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (int(weight) / float(height) ** 2)

if bmi < 18.5:
  print(f"Your BMI is {float(bmi)}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {float(bmi)}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {float(bmi)}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {float(bmi)}, you are obese.")
else:
  print(f"Your BMI is {float(bmi)}, you are clinically obese.")