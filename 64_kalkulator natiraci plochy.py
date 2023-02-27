# Hodnoty od uzivatele
import math
wall_h = int(input("Vyska steny v metrech: "))
wall_w = int(input("Sirka steny v metrech: "))
coverage = 5

def paint_calculator(width, height, cover):
    area = width * height
    number_can = math.ceil (area / 5)
    print(f"budete potrebivat {number_can} plechovek barvy")
paint_calculator(width=wall_h, height=wall_w, cover=coverage)