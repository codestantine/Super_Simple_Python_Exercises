# bank roulette
import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# first step
# length of names list
list_length = len(names)

random_index = random.randint(0, 4)
lucky_person = names[random_index]
print(f"{lucky_person} will pay for everybody's food bill.")

