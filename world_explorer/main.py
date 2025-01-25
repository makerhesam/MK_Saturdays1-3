import json


with open("countries.json", "r") as file:
    countries = json.load(file)

#print everything about canada


print("Welcome to the World Explorer")
print("Type the name of a country to explore its information")
print("Type exit to leave the program. \n")

while True:
    country_name = input("Enter a country name or type exit: ")

    if country_name == "exit":
        print("BYEEE")
        break


    if country_name in countries:
        print(f"Lets explore {country_name}!")
        country_info = countries[country_name]
        print(f"  - Capital: {country_info['Capital']}")
        print(f"  - Largest City: {country_info['Largest City']}")
        print(f"  - Total Area: {country_info['Total Area']} km²")
        print(f"  - Landmarks: {', '.join(country_info['Landmarks'])}")
        print(f"  - Cultural Highlights: {', '.join(country_info['Cultural Highlights'])}")
        print(f"  - Daily Life: {', '.join(country_info['Daily Life'])}")
    
    else:
        print("That country is not in our database.")