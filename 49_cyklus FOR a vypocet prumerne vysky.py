vyska = input("Vlozte vysky lidi oddelene carkou\n")
list = vyska.split(", ")
suma = 0

for prvni_list in list:
    suma = suma + int(prvni_list)
suma = suma / len(list)
print (f"Prumerna vyska lidi je: {suma}")
