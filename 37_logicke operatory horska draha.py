# podminky v Pythonu
print("Vitajte na horske draze")
vyska = int(input("Jaka je vase vyska v cm?\n"))
bill = 0

if vyska >= 87:
    print("Muzete jet horskou drahou")
    age = int(input("Jaky je vas vek?\n"))
    if age < 12:
        bill = 50
        print("cena vaseho listku je 50 kč")
    elif age <18:
        bill = 100
        print("Cena vaseho listku je 100Kc")
    elif age >= 40 and age <= 50:
        bill = 0
    else:
        bill = 150
        print ("cena vaseho listku je 150kc")
    photo = input("chcete behem jizdy vyfotit? ano nebo ne \n")
    if photo == "ano":
        bill = bill + 40 
    print(f"Vase cena je : {bill} kč")
else:
    print("Nemuzete jet na draze")