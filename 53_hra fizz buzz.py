# cislo delitelne 3 = Fizz
# cislo delitelne 5 = Buzz
# cislo delitelne 3 a 5 = FizzBuzz
# jinak vypsat bezne cislo

for one_number in range(1, 101):
    if one_number % 3 == 0 and one_number % 5 == 0:
        print("FizzBuzz")
    elif one_number % 3 == 0:
        print("Fizz")
    elif one_number % 5 == 0:
        print("Buzz")
    else:
        print(one_number)