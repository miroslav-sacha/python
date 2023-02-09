# BMI
vyska = float(input("Vlozte svoji vysku v metrech: "))
vaha  = float(input("vlozte svou váhu v kg: "))

bmi  = vaha / (vyska * vyska)

# print (round(bmi, 1))

if bmi < 18.5:
    print(f"Vas bmi ma hodnotu {round(bmi, 1)}, mate podváhu")
elif bmi < 24.9:
    print(f"Vas bmi ma hodnotu {round(bmi, 1)}, jste v normalu")
elif bmi < 29.9:
    print(f"Vas bmi ma hodnotu {round(bmi, 1)}, mate nadvahu")
elif bmi < 34.9:
    print(f"Vas bmi ma hodnotu {round(bmi, 1)}, jste obezni")
else:
    print(f"Vas bmi ma hodnotu {round(bmi, 1)}, mate obezitu")

