import random

names = input("Napis jmena vsech oddelene carkou\n")
list_people = names.split(", ")
random_number = random.randint(0, len(list_people)-1)
print(f"{list_people[random_number]} bude dnes platit ucet")