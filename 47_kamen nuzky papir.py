import random

kamen = 'kamen'
nuzky = 'nuzky'
papir = 'papir'

list = [kamen, nuzky, papir]

user = int(input("Napiste vasi volbu 0 kamen 1 nuzky nebo 2 papir \n"))
user_list = list[user]

pocitac = random.randint(0, 2)
pocitac_list = list[pocitac]

print(f"Uzivatel si vybral \n {user_list}")
print(f"Pocitac si vybral \n {pocitac_list}")

if user == pocitac:
    print("Remiza")
elif user == 0 and pocitac == 1:
    print("Vyhral jste")
elif user == 0 and pocitac == 2:
    print("Vyhral pocitac")
elif user == 1 and pocitac == 2:
    print("Vyhral jste")