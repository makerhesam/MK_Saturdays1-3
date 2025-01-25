import json
import random


with open('countries.json', "r") as file:
    countries = json.load(file)

def quiz_game():
    print("Welcome to world quiz!")
    print("Select a category to be quizzed on: ")
    print("1. Capital Cities")
    print("2. Largest Cities")
    print("3. Total Area")
    print("type exit to stop the quiz")

    category_map = {
        "1": "Capital",
        "2": "Largest City",
        "3": "Total Area"
    }

    while True:
        choice = input("Enter the number of the category you wanna be quizzed on: ")
        if choice in category_map:
            category = category_map[choice]
            break
        elif choice == "exit":
            print("Exiting the game...")
            return
        else:
            print("invalid choice. choose a valid number")
    
    print(f"You chose {category}. Lets begin! \n")

    score = 0
    total_questions = 0

    while True:
        country = random.choice(list(countries.keys()))
        answer = countries[country][category]

        if category == "Total Area":
            print(f"Which country has a total area of {answer}? ")
        else:
            print(f"Which country has {answer} as its {category}? ")

        user_guess = input("Your answer: ")
        if user_guess == "exit":
            print("Exiting quiz...")
            break

        total_questions += 1

        if user_guess.lower() == country.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {country}")
        print()
    



quiz_game()