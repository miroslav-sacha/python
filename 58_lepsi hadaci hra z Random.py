# hadaci hra z nahodnych jmen
import random

print("Vitejte ve hre Harry Potter")
characters = ["Harry", "Ron", "Herminona", "Draco", "Crabbe", "Goyle"]
character = characters[random.randint(0, len(characters)-1)]
gues = ""
gues_count = 5

while character != gues:
    if gues_count != 0:
        gues = input("Uhodnete postava z filmu Harry Potter\n")
        gues_count -= 1
    else:
        print("Pocet pokusu je vycerpan")
        break
    
    if character == gues:
        print(f"Uhadli jste!!! slovo bylo {character}")