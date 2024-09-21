file = open("videogames.csv", "r")

def display_games():
    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]
        
        print("Title: " + title)
        print("Release Year: " + release_year)
        print("Genre: " + genre)
        print("Developer: " + developer)
        print("Platform: " + platform)
        print()


def list_games_by_year():
    year = input("What year are you interested in? ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if year == release_year:
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()


def list_games_by_developer():
    dev = input("Which Developer are you interested in? ")

    for line in file:
        data = line.split(",")

        title = data[0]
        release_year = data[1]
        genre = data[2]
        developer = data[3]
        platform = data[4]

        if dev == developer:
            print("Title: " + title)
            print("Release Year: " + release_year)
            print("Genre: " + genre)
            print("Developer: " + developer)
            print("Platform: " + platform)
            print()

#display_games()
#list_games_by_year()
# list_games_by_developer()


#make a funciton called list_games_by_genre
#1. it asks the user for a genre
#2. prints all the games that have that genre


#make a function called list_games_before_year
#it asks the user for a year, and lists all the 
#games from that year and before