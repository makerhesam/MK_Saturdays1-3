cup_price = 0.50
cone_price = 0.80
scoop_price = 1.20
flake_price = 0.40
chocolate_price = 0.30
strawberry_price = 0.60


price = 0
container = input("Would you like a cup or a cone? ")
if container.upper() == "CUP":
    price = price + cup_price
else:
    price = price + cone_price

scoops = int(input("How many scoops would you like? "))
price = price + (scoops * scoop_price)

flakes = input("would you like flakes on the ice cream? ")
if flakes.upper() == "YES":
    price = price + flake_price

chocolate = input("would you like chocolate sprinkles on the ice cream? ")
if chocolate.upper() == "YES":
    price = price + chocolate_price

strawberry = input("would you like strawberry coulis on the ice cream? ")
if strawberry.upper() == "YES":
    price = price + strawberry_price


print("your total is $" + str(price))