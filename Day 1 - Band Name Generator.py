from random import randint

print("Welcome to the Band Name Generator!")

city = input("What's the name of the city you grew up in? \n")

pet_name = input("What is the name of your pet? \n")

if randint(1,2) % 2 == 0:
    print(f"Your band name is {city} {pet_name}!")
else:
    print(f"Your band name is {pet_name} {city}!")