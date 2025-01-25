import random
import csv

#function that display first x letters of a word and 
#replaces the rest with dashes

def display_clue(word, x):
    clue = ""

    for i in range(len(word)):
        #if current index is less than number of clues
        if i < x:
            clue += word[i]
        else:
            clue += "_"
        
        clue += " "
    
    print("Name the country: " + clue.upper())


#test display clue function
#display_clue("makerkids", 5)


#saves the leaderboard to the .csv file
def save_leaderboard(name, score, filename="leaderboard.csv"):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score])


#save_leaderboard("Hesam", 10)


#function to display the leaderboard

def display_leaderboard(filename="leaderboard.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            scores = list(reader)

            #sort the scores from large to small:
            scores.sort(key=lambda x: int(x[1]), reverse=True)

            print("Leaderboard (Top 10): ")
            for i in range(10):
                if i < len(scores):
                    print(f"{i+1}. {scores[i][0]} - {scores[i][1]} points")
    except FileNotFoundError:
        print("No leaderboard data found")

#display_leaderboard()



#main program starts here

countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
    "Chile", "China", "Colombia", "Comoros", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "North Korea", "South Korea", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan",
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

player_score = 0

#shuffle list of countries to randomize the order
random.shuffle(countries)
#select the first 10 countries
used_countries = countries[:10]

print("Welcome to the Name the Country Quiz")


#quiz loop(go through the 10 random countries)
for round_num in range(len(used_countries)):
    country = used_countries[round_num]
    print(f"Round {round_num+1}: ")
    clue_length = 1

    #give the user clues until either they guess correct
    #or we gave them all clues possible (all letters of the country)
    while clue_length <= len(country):
        display_clue(country, clue_length)
        #ask the user for their guess
        #.title() makes first letter capital, rest small
        guess = input("Your guess? ").title()

        if guess == country:
            points = len(country) - clue_length + 1 #calculate score
            player_score += points #add it to the player score
            print(f"Correct! you got {points} points!")
            break
        else:
            print("wrong guess! here is more of the clue.")
            clue_length += 1
    else:
        print(f"Sorry, the correct answer was: {country}")

print("Game Over!")
print(f"total score: {player_score}")


player_name = input("Enter your name: ")
#saves the player name and score to leaderboard.csv
save_leaderboard(player_name, player_score) 

print()
print("Final Leaderboard")
display_leaderboard()