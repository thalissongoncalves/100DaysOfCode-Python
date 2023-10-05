print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_names = name1.lower() + name2.lower()
T = combined_names.count("t")
R = combined_names.count("r")
U = combined_names.count("u")
E = combined_names.count("e")
total_true = T + R + U + E

L = combined_names.count("l")
O = combined_names.count("o")
V = combined_names.count("v")
E = combined_names.count("e")
total_love = L + O + V + E

combined_names_value = int(f"{total_true}{total_love}")
if combined_names_value < 10 or combined_names_value > 90:
  print(f"Your score is {combined_names_value}, you go together like coke and mentos.")
elif combined_names_value >= 40 and combined_names_value <= 50:
  print(f"Your score is {combined_names_value}, you are alright together.")
else:
  print(f"Your score is {combined_names_value}.")