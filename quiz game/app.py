import random
import csv
import sys

# Read countries and capitals from a CSV file
country_capitals = {}
with open('countries.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        country_capitals[row[0]] = row[1]

# Initialize the score and number of times played
score = 0
times_played = 0

# Create a list of country names
country_names = list(country_capitals.keys())

# Shuffle the list to choose countries at random
random.shuffle(country_names)

# Iterate through the shuffled list
for country in country_names:
    print(f"What is the capital of {country}?")
    print("Enter 'exit' to quit.")
    answer = input("Answer: ")
    
    # Check if the user wants to exit
    if answer.lower() == 'exit':
        print("Exiting the game. Your final score is:", score)
        sys.exit()

    if answer.lower() == country_capitals[country].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong answer. The correct answer is: {country_capitals[country]}")
    
    # Increment the number of times played
    times_played += 1
    print(f"Your score is: {score}/{times_played} ({(score / times_played) * 100:.2f}%)")
