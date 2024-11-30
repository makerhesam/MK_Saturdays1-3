import random


first_names = ["Aria", "Drake", "Kendrick", "Luna", "Tuna", "Thor"]
last_names = ["Storm", "Shadow", "Frost", "Speed", "Light", "McQueen"]
species = ["Elf", "Dwarf", "Human", "Dragon", "Machine"]
powers = ["Invisibility", "Fireball", "Healing", "Lightning", "Shape-shifting"]



first_name = random.choice(first_names)
last_name = random.choice(last_names)
email = first_name + "." + last_name + "@gmail.com"
specie = random.choice(species)
power = random.choice(powers)


print("Here is your randomly generated fantasy character:")
print("Name: " + first_name + " " + last_name)
print("Species: " + specie)
print("Magical Power: " + power)