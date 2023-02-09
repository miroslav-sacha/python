rok = int(input("Jaký rok chcete zkontrolovat?\n"))

if rok % 4 == 0: # pokud rok je delitelny 4
    if rok % 100 == 0: # pokud je rok delitelny 100
        if rok % 400 == 0:
            print("Je to prestupny rok")
        else:
            print("Neni to prestupny rok")
    else:
        print ("Je to prestupny rok")
else:
    print("Neni to prestupny rok") 