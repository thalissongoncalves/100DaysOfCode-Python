names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names_length = len(names) #3
random_name = random.randint(0, names_length - 1)
print(f"{names[random_name]} is going to buy the meal today!")