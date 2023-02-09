ucet = int(input ("Kolik mate celkem zaplatit: \n"))
spropitne = int(input ("Kolik chcete dat spropitneho v %: \n"))
rozdeleni = int(input ("Mezi kolik lidi se ma castka rozedlit: \n"))
# x = (spropitne /100 )
# y = (ucet * x)
# v = (ucet + y)
# z = (v / rozdeleni)
z = (ucet + (ucet * spropitne / 100)) / rozdeleni
# zaokrouleni na dve des. mista
final = "{:.2f}".format(z)
print (f"Kazdy clovek by mel celkem zaplatit: {final}")
