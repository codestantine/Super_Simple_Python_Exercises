# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

# generate a random number
# number = random.randint(0, 1)
#
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")

# for i in range(10):
#     number = random.randint(0, 1)
#     if number == 1:
#         print(f"{i}: number => {number} Heads")
#     else:
#         print(f"{i}: number => {number} Tails")

print("Heads" if random.randint(0, 1) == 1 else "Tails")

