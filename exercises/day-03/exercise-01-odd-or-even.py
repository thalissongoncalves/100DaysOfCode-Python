# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

calculate = number % 2
if float(calculate) == 0.00:
  print("This is an even number.")
else:
  print("This is an odd number.")