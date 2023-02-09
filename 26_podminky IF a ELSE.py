# podminky v Pythonu
print("Vitajte na horske draze")
vyska = int(input("Jaka je vase vyska v cm?\n"))

if vyska >= 87:
    print("Muzete jet horskou drahou")
    age = int(input("Jaky je vas vek?\n"))
    if age < 18:
        print("cena vaseho listku je 100 kč")
    else:
        print ("cena vaseho listku je 150kc")
else:
    print("Nemuzete jet na draze")