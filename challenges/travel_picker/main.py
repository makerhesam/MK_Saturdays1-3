import random


#destination lists
beach_destinations = [
    "Maldives", "Hawaii", "Bahamas", "Bora Bora", "Cancun",
    "Phuket", "Bali", "Maui", "Fiji", "Seychelles", "Havana"
    ]

mountain_destinations = [
    "Swiss Alps", "Rocky Mountains", "Mount Everest", "Banff", "Andes", 
    "Patagonia", "Dolomites", "Himalayas", "Appalachians", "Tatra Mountains"
]

urban_destinations = [
    "Tokyo", "New York", "Paris", "Dubai", "London", 
    "Shanghai", "Singapore", "Los Angeles", "Berlin", "Hong Kong"
]


#destination activtities

relaxing_destinations = [
    "Maldives", "Bora Bora", "Hawaii", "Banff", "Bahamas", 
    "Phuket", "Seychelles", "Fiji", "Santorini", "Bali"
]
nature_destinations = [
    "Banff", "Swiss Alps", "Andes", "Maldives", "Mount Everest", 
    "Patagonia", "Dolomites", "Phuket", "Himalayas", "Yosemite"
]
sightseeing_destinations = [
    "Paris", "Tokyo", "New York", "London", "Dubai", 
    "Rome", "Cairo", "Kyoto", "Istanbul", "Beijing"
]
history_destinations = [
    "Rome", "Athens", "Kyoto", "Cairo", "Istanbul", 
    "Jerusalem", "Machu Picchu", "Florence", "Petra", "Delphi", "Havana"
]

#price destinations

cheap_destinations = [
    "Cancun", "Athens", "Cairo", "Andes", "Istanbul", 
    "Phuket", "Hanoi", "Bangkok", "Tbilisi", "Kathmandu", "Havana"
]
moderate_destinations = [
    "Hawaii", "Rocky Mountains", "Banff", "Rome", "Tokyo", 
    "Berlin", "Florence", "Barcelona", "Bali", "Cape Town"
]
expensive_destinations = [
    "Bora Bora", "Swiss Alps", "Paris", "Dubai", "New York", 
    "Machu Picchu", "Santorini", "Kyoto", "London", "Los Angeles"
]
luxury_destinations = [
    "Maldives", "Mount Everest", "Bahamas", "London", "Kyoto", 
    "Seychelles", "Singapore", "Shanghai", "Hong Kong", "Aspen"
]

def filter_destinations(destinations, filter_list):
    result = []
    for destination in destinations:
        if destination in filter_list:
            result.append(destination)
    return result


print("Welcome to the vacation picker!")
print("Answer a few questions, and I'll suggest a great vacation")


matching_destinations = (beach_destinations + mountain_destinations + urban_destinations)


print("What type of destination do you prefer?")
print("Options: Beach, Mountains, Urban")
type_preference = input("Enter your choice: ").lower()

if type_preference == "beach":
    matching_destinations = filter_destinations(matching_destinations, beach_destinations)
elif type_preference == "mountains":
    matching_destinations = filter_destinations(matching_destinations, mountain_destinations)
elif type_preference == "urban":
    matching_destinations = filter_destinations(matching_destinations, urban_destinations)
else:
    print("Invalid choice, please restart the program")
    exit()


print("what kind of activity do you prefer? ")
print("Options: relaxing, nature, sightseeing, history")
activity_preference = input("Enter your choice: ").lower()


if activity_preference == "relaxing":
    matching_destinations = filter_destinations(matching_destinations, relaxing_destinations)
elif activity_preference == "nature":
    matching_destinations = filter_destinations(matching_destinations, nature_destinations)
elif activity_preference == "sightseeing":
    matching_destinations = filter_destinations(matching_destinations, sightseeing_destinations)
elif activity_preference == "history":
    matching_destinations = filter_destinations(matching_destinations, history_destinations)
else:
    print("Invalid choice. Please restart the program.")
    exit()


print("what is your budget?")
print("Options: Cheap, Moderate, Expensive, Luxury")

budget_preference = input("Enter your choice: ").lower()

if budget_preference == "cheap":
    matching_destinations = filter_destinations(matching_destinations, cheap_destinations)
elif budget_preference == "moderate":
    matching_destinations = filter_destinations(matching_destinations, moderate_destinations)
elif budget_preference == "expensive":
    matching_destinations = filter_destinations(matching_destinations, expensive_destinations)
elif budget_preference == "luxury":
    matching_destinations = filter_destinations(matching_destinations, luxury_destinations)
else:
    print("Invalid choice. please restart the program.")


print("final matching destinations: ")
#if matching destinations is not empty
if matching_destinations:
    print(", ".join(matching_destinations))
else:
    print("No destinations match your preferences. try adjusting your choices")