import random

# Expanded destination lists
beach_destinations = [
    "Maldives", "Hawaii", "Bahamas", "Bora Bora", "Cancun", 
    "Phuket", "Bali", "Maui", "Fiji", "Seychelles"
]
mountain_destinations = [
    "Swiss Alps", "Rocky Mountains", "Mount Everest", "Banff", "Andes", 
    "Patagonia", "Dolomites", "Himalayas", "Appalachians", "Tatra Mountains"
]
urban_destinations = [
    "Tokyo", "New York", "Paris", "Dubai", "London", 
    "Shanghai", "Singapore", "Los Angeles", "Berlin", "Hong Kong"
]

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
    "Jerusalem", "Machu Picchu", "Florence", "Petra", "Delphi"
]

cheap_destinations = [
    "Cancun", "Athens", "Cairo", "Andes", "Istanbul", 
    "Phuket", "Hanoi", "Bangkok", "Tbilisi", "Kathmandu"
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

# Function to filter destinations based on preferences
def filter_destinations(destinations, filter_list):
    return [d for d in destinations if d in filter_list]

# Welcome message
print("Welcome to the Vacation Picker!")
print("Answer a few questions, and I'll suggest destinations that match your preferences.\n")

# Initial list of all destinations
matching_destinations = (
    beach_destinations + mountain_destinations + urban_destinations
)

# Step 1: Type of destination
print("What type of destination do you prefer?")
print("Options: Beach, Mountains, Urban")
type_preference = input("Enter your choice: ").strip().lower()

if type_preference == "beach":
    matching_destinations = filter_destinations(matching_destinations, beach_destinations)
elif type_preference == "mountains":
    matching_destinations = filter_destinations(matching_destinations, mountain_destinations)
elif type_preference == "urban":
    matching_destinations = filter_destinations(matching_destinations, urban_destinations)
else:
    print("Invalid choice. Please restart the program.")
    exit()

# Step 2: Activity preference
print("\nWhat kind of activity do you prefer?")
print("Options: Relaxing, Nature, Sightseeing, History")
activity_preference = input("Enter your choice: ").strip().lower()

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

# Step 3: Budget preference
print("\nWhat is your budget?")
print("Options: Cheap, Moderate, Expensive, Luxury")
budget_preference = input("Enter your choice: ").strip().lower()

if budget_preference == "cheap":
    matching_destinations = filter_destinations(matching_destinations, cheap_destinations)
elif budget_preference == "moderate":
    matching_destinations = filter_destinations(matching_destinations, moderate_destinations)
elif budget_preference == "expensive":
    matching_destinations = filter_destinations(matching_destinations, expensive_destinations)
elif budget_preference == "luxury":
    matching_destinations = filter_destinations(matching_destinations, luxury_destinations)
else:
    print("Invalid choice. Please restart the program.")
    exit()

# Final output
print("\nFinal matching destinations:")
if matching_destinations:
    print(", ".join(matching_destinations))
else:
    print("No destinations match your preferences. Try adjusting your choices!")
