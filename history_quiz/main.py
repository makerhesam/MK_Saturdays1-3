import json
import random


with open("ages.json", "r") as file:
    ages = json.load(file)


print("Welcome to the Historical Quiz!")
print("You will be quizzed on inventions, major events, or daily life.")
print("Try to guess the correct time period. Type exit to quit.")

score = 0

while True:
    #ask the user for a category
    print("What would you like to be quizzed on? ")
    print("Options: Inventions, Major Events, Daily Life")
    category = input("Enter your choice").strip().lower()

    if category == "exit":
        print("Thanks for playing!")
        print(f"Your final score: {score}")
        break
    
    if category not in ["inventions", "major events", "daily life"]:
        print("Invalid choice. please choose from the options")
        continue


    quiz_items = []

    for age, details in ages.items():
        quiz_items.append((random.choice(details[category.capitalize()]), age))   
    
    quiz_item, correct_age = random.choice(quiz_items)
    print("Which time period does this belong to? ")
    print(quiz_item)
    user_answer = input("Your Answer: ").strip()

    if user_answer.lower() == correct_age.lower():
        print("Correct!")
        score += 1
        print(f"Score: {score}")
    else:
        print(f"Inocorrect! the correct answer is: {correct_age}")
        print(f"Score: {score}")
