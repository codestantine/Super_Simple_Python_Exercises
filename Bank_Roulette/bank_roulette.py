# bank roulette
import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# index 0 - length of the list - 1
length_of_list = len(names)
high_index = length_of_list - 1
low_index = 0
lucky_index = random.randint(low_index, high_index)
lucky_person = names[lucky_index]
print(f"{lucky_person} is paying for everyone's food bill today!")



