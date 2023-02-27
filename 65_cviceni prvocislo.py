# prvocislo
# cislo 13
def prime_number_checker(number):
    result = "je to prvocislo"
    for one_number in range (2, number):
        if number % one_number == 0:
            result = "Neni to prvocislo"
    print(result)

n = int(input("Zadejte prosim cislo: "))
prime_number_checker(n)