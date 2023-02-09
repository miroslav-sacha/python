import random
import math

# generóvani nahodneho celeho cisla z rozsahu
print (random.randint(10, 18))

# generóvani nahodneho desetineho cisla z rozsahu 0-1
print(random.random())

# generóvani nahodneho celeho cisla z rozmezi + zadani kroku
print(random.randrange(15, 25, 2))

# math a ceil zaokrouhli na cele cislo nahoru
print(math.ceil(5.1))

# math a ceil zaokrouhli na cele cislo dolu
print(math.floor(6.1))

a = ['Adolf', 'Vsiliy', 'Jiri', 'Jakub', 'Honza']
b = ['Krestov', 'Turnovsky', 'Hitler', 'Lipsky', 'Nespesny']

x = random.randint(0, 4)
y = random.randint(0, 4)

print(f'{a[x]} {b[y]}')
