import csv

#function to load the csv file to our python
def load_birthdays(filename):
    birthdays = []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            birthdays.append(row)
    return birthdays

# result = load_birthdays("birthdays.csv")
# print(result)

#function to display all birthdays in a specific month
def display_birthdays_by_month(birthdays, month):
    print(f"Birthdays in {month}: ")
    print()
    for entry in birthdays:
        birthday_month = entry['Birthday'].split('/')[0]
        if birthday_month == month:
            print(f"{entry['Name']} - {entry['Birthday']}")


result = load_birthdays("birthdays.csv")
display_birthdays_by_month(result, '01')