print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

total_value = 0

if size == "S":
    total_value += 15
elif size == "M":
    total_value += 20
else:
    total_value += 25

if add_pepperoni == "Y":
    if size == "S":
        total_value += 2
    else:
        total_value += 3

if extra_cheese == "Y":
    total_value += 1

print(f"Your final bill is: ${total_value}.")