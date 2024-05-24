age = input("What is your current age? ")

ninety_month = 1080
ninety_week = 4680
ninety_day = 32850

age_month = int(age) * 12
age_week = int(age) * 52
age_day = int(age) * 365

print(f"You have { ninety_week - age_week } weeks left.")