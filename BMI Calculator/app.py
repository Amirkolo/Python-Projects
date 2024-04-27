"""
BMI Calculator

This program calculates the Body Mass Index (BMI) based on the user's input of weight and height.
It then classifies the BMI into different categories and provides feedback to the user.

BMI categories:
- Under 18.5: Underweight
- 18.5 - 24.9: Normal Weight
- 25 - 29.9: Overweight
- 30 - 34.9: Obese
- 35 - 39.9: Severely Obese
- 40 and over: Morbidly Obese
"""

# Function to calculate BMI
def calculate_bmi(weight, height, weight_unit='kg', height_unit='m'):
    if weight_unit == 'lb':
        weight *= 0.453592  # Convert pounds to kilograms
    if height_unit == 'in':
        height *= 0.0254  # Convert inches to meters
    return weight / (height ** 2)

# Prompt user for input
name = input("Enter your name: ")

# Prompt user to choose weight metric
weight_metric = input("Choose weight metric (kg/lb): ").lower()
while weight_metric not in ['kg', 'lb']:
    print("Invalid input. Please choose either 'kg' or 'lb'.")
    weight_metric = input("Choose weight metric (kg/lb): ").lower()

# Prompt user for weight
weight = float(input(f"Enter your weight in {weight_metric}: "))

# Prompt user to choose height metric
height_metric = input("Choose height metric (m/in): ").lower()
while height_metric not in ['m', 'in']:
    print("Invalid input. Please choose either 'm' or 'in'.")
    height_metric = input("Choose height metric (m/in): ").lower()

# Prompt user for height
height = float(input(f"Enter your height in {height_metric}: "))

# Calculate BMI
BMI = calculate_bmi(weight, height, weight_metric, height_metric)

# Print BMI
print(f"Your BMI is: {BMI:.2f}")

# Determine BMI category and provide feedback
if BMI < 18.5:
    print(f"{name}, you are underweight.")
elif BMI <= 24.9:
    print(f"{name}, you are normal weight.")
elif BMI < 29.9:
    print(f"{name}, you are overweight. You need to exercise more and stop sitting and writing so many Python tutorials.")
elif BMI < 34.9:
    print(f"{name}, you are obese.")
elif BMI < 39.9:
    print(f"{name}, you are severely obese.")
else:
    print(f"{name}, you are morbidly obese.")
