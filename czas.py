import math
G = 9.81
#wspolczynnik tarcia
u = float(input("podaj wspolczynnik tarcia: "))
print("wspoczynnik tarcia rowna sie: " + str(u))
#podaj odleglosc przebyta(pozioma)
s = float(input("podaj przebyta droge w poziomie w metrach: "))
print("przebyta droga w poziomie rowna sie: " + str(s))
#predkosc poczatkowa
v0 = float(input("podaj predkosc poczatkowa w m/s: "))
print("predkosc poczatkowa rowna sie: " + str(v0))
#kat nachylenia
kat = float(input("podaj kat nachylenia w stopniach:"))
print("kat rowna sie: " + str(kat))
# konwersja kąta z stopni na radiany
kat_w_radianach = math.radians(kat)

#obliczenia sily grawitacyjnej na rowni pochylej
czas = - (v0 + math.sqrt(v0**2 + 2 * G * (u * math.cos(kat_w_radianach) - math.sin(kat_w_radianach)) * s)) / (G * (math.sin(kat_w_radianach) - u * math.cos(kat_w_radianach)))
#wynik
print(f"czas rowna sie: {czas:.2f} sekund")