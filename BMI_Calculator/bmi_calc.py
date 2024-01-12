# BMI Calculator

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Equal to or over 25 but below 30 they are slightly overweight
#     Equal to or over 30 but below 35 they are obese
#     Equal to or over 35 they are clinically obese.

print("Welcome to BMI Calculator.")
answer = input("Press Enter (don't type anything) if you want to enter your weight and height in kg and "
               "meters.\nEnter \"US\" if you want to enter your weight and height in pounds and feet: ")
if answer.lower() == "us":
    weight_in_pounds = float(input("Enter your weight in pounds: "))
    height_in_feet = float(input("Enter your height in feet: "))
    weight_in_kg = weight_in_pounds / 2.205
    height_in_meters = height_in_feet / 3.281
else:
    weight_in_kg = float(input("Enter your weight in kilograms: "))
    height_in_meters = float(input("Enter your height in meters: "))
# 5.9 ft
# 176.37
# BMI = 24.7

bmi = weight_in_kg / height_in_meters ** 2
bmi = round(bmi, 1)

# bmi = f"{bmi:.2f}"
# print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are considered underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You are considered normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are considered overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are considered obese.")
else:
    print(f"Your BMI is {bmi}. You are considered clinically obese.")

# feet to meters
# divide the length value by 3.281
# pounds to kg
# divide the mass value by 2.205

# 5.9 ft = 1.8 meters
# 176.37 = 80 kg
# BMI = 24.7

# codestantine
# repo's name is: super simple python exercises.
