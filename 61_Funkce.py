# predpripravene funkce
print("Ahoj")
number_character = len("Ahoj")
print(number_character)

# vlastni funkce
def greet():
    print("Dobrý den")
    print("Jmenuji se Jan")
    print("Na shledanou")
greet()

# name je parametr 
def greet_name(name): 
    print(f"Ahoj ja jsem {name}")
# David to co je v zavorkách u vystupu je argument
greet_name("David")
greet_name("Harry")

# funkce s vice parametry
def greeta (names, location):
    print(f"Ahoj ja jsem {names} a pochazim z mesta {location}")

# positional arguments
greeta("David", "Ceske Budejovcie")

# keywords arguments
greeta(names="Martina", location="Tábor")