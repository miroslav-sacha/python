sizze = input("Zadejte velikost pizzy S, M nebo L: ")
feferonka = input("Chcete feferonky?? A nebo N: ")
syr = input("Chcete syr navic?? A nebo N: ")

bill = 0

if sizze == "S":
    bill += 100
elif sizze == "M":
    bill += 150
elif sizze == "L":
    bill += 200

if feferonka == "A":
    if sizze != "S":
        bill += 30
    else:
        bill += 20

if syr == "A":
    bill += 15
else:
    bill == 0

print(f"Castka k zaplaceni je {bill} Kc")

