print("Welcome to the tip calculator.")
total_value = float(input("What was the total bill? $"))
tip_value = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_number = int(input("How many people to split the bill? "))
total_per_people = (total_value / people_number) * (float(tip_value / 100) + 1)
print(f"Each person should pay: ${format(total_per_people, '.2f')}")