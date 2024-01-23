import os
import math

# Instalacja matplotlib:
    # python -m pip install -U pip
    # python -m pip install -U matplotlib

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.animation as animation

from dzialania_fizyczne import DzialaniaFizyczne

G = 9.81 
TIME = 0.001 # Co ile sprawdzać prędkość i drogę
WSPOLCZYNNIK_TARCIA = 0.7
dlugosc_rowni = 100

file = open("wyniki.csv", "w")
os.system('cls')

predkosc_poczatkowa = float(input("Podaj prędkość początkową: "))
masa = 10
kat_nachylenia = float(input("Podaj kąt nachylenia: "))

timer = 0 
droga = 0
czyDojechalDoKonca = False

czasyTab = []
drogiTab = []
predkosciTab = []
energieKinetyczne = []
energiePotencjalne =[]

obliczone_przyspieszenie = DzialaniaFizyczne.przyspieszenieF(WSPOLCZYNNIK_TARCIA, kat_nachylenia)
# obliczony_czas = DzialaniaFizyczne.czas(predkosc_poczatkowa, kat_nachylenia, droga, WSPOLCZYNNIK_TARCIA)
print("Obliczone przyśpieszenie:", round(obliczone_przyspieszenie, 2))

file.write(f"Czas, Droga, Pręd\n")
file.write(f"0, 0, {round(predkosc_poczatkowa, 2)}\n")

drogiTab.append(0)
czasyTab.append(0)
predkosciTab.append(predkosc_poczatkowa)
energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
energiePotencjalne.append(masa * G * math.sin(math.radians(kat_nachylenia)) * droga)

while(predkosc_poczatkowa > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
    if(predkosc_poczatkowa < abs(obliczone_przyspieszenie)*TIME): # gdy 'predkosc_poczatkowa - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
        droga += predkosc_poczatkowa * predkosc_poczatkowa/abs(obliczone_przyspieszenie)
        drogiTab.append(droga)
        timer += predkosc_poczatkowa*TIME/abs(obliczone_przyspieszenie)
        czasyTab.append(timer)
        # print("v =", predkosc_poczatkowa)
        predkosciTab.append(predkosc_poczatkowa)
        predkosc_poczatkowa = 0
        energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
        energiePotencjalne.append(masa * G * math.sin(math.radians(kat_nachylenia)) * droga)

        # print("v =", predkosc_poczatkowa)
        file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa, 2)}")
        break
    # time.sleep(TIME) # Można zakomentować, nic nie zmienia
    
    # print("v =", predkosc_poczatkowa)
    timer += TIME
    czasyTab.append(timer)
    predkosc_poczatkowa -= abs(obliczone_przyspieszenie)*TIME
    predkosciTab.append(predkosc_poczatkowa)
    droga += predkosc_poczatkowa*TIME
    drogiTab.append(droga)

    energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
    energiePotencjalne.append(masa * G * math.sin(math.radians(kat_nachylenia)) * droga)

    file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa,2)}\n")

    # Sprawdza czy zaraz dojedziemy do końca równi lub czy już nie dojechaliśmy
    if(czyDojechalDoKonca == False and (dlugosc_rowni < droga + (predkosc_poczatkowa - abs(obliczone_przyspieszenie)*TIME))):
        czyDojechalDoKonca = True
        pozostala_droga = dlugosc_rowni - droga
        pozostaly_czas = pozostala_droga / predkosc_poczatkowa
        predkosc_koncowa = (predkosc_poczatkowa - abs(obliczone_przyspieszenie)*pozostaly_czas)
        czasPrzejazduRowni = timer + pozostaly_czas



file.close()
maxHeight = math.sin(math.radians(kat_nachylenia)) * droga
print(f"Czas: {timer:.2f}s")
print(f"Przebyta droga: {droga:.2f}m")
print(f"Max wysokość: {maxHeight:.2f}m")

# for i in range(len(drogiTab)):
#     print(f"Ek = {energieKinetyczne[i]:.2f}, Ep = {energiePotencjalne[i]:.2f}, Suma = {energieKinetyczne[i] + energiePotencjalne[i]:.2f}")

if(czyDojechalDoKonca):
    print(f"Czas przejazdu równi: {czasPrzejazduRowni:.2f}s")
    print(f"Prędkość na końcu równi: {predkosc_koncowa:.2f}m/s")
else:
    print(f"Obiekt nie dojechał do końca równi")


# Wykres Przebytej drogi do czasu
fig, ax = plt.subplots()
plt.ylabel('Przebyta droga')
plt.xlabel('Czas')
plt.plot(czasyTab, drogiTab)

scat = ax.scatter(czasyTab[0], drogiTab[0], c="b", label=f'Czas = {round(timer,2)}s')
line2 = ax.plot(czasyTab[0], drogiTab[0], label=f'Droga = {round(droga)}m')[0]
ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(drogiTab)+5], xlabel='Czas (s)', ylabel='Droga (m)')
ax.legend()

plt.show()


# Wykres Ek do Ep
fig, ax = plt.subplots()
plt.ylabel('Energia Potencjalna (J)')
plt.xlabel('Energie Kinetyczne (J)')
plt.plot(energiePotencjalne, energieKinetyczne)

scat = ax.scatter(energiePotencjalne[0], energieKinetyczne[0], c="b", label=f'Energia Kinetyczna = {round(energieKinetyczne[-1],2)}J')
line2 = ax.plot(energiePotencjalne[0], energieKinetyczne[0], label=f'Energia Potencjalna = {round(energiePotencjalne[-1])}J')[0]
ax.set(xlim=[0, max(energiePotencjalne)+5], ylim=[0, max(energieKinetyczne)], xlabel='Energia Potencjalna (J)', ylabel='Energia Kinetyczna (J)')
ax.legend()

plt.show()

# Wykres Ek do czasu
fig, ax = plt.subplots()
plt.ylabel('Energia Kinetyczna (J)')
plt.xlabel('Czas')
plt.plot(czasyTab, energieKinetyczne)

scat = ax.scatter(czasyTab[0], energieKinetyczne[0], c="b", label=f'Czas = {round(timer,2)}s')
line2 = ax.plot(czasyTab[0], energieKinetyczne[0], label=f'Energia Kinetyczna = {round(energieKinetyczne[-1])}J')[0]
ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(energieKinetyczne)+5], xlabel='Czas (s)', ylabel='Energia Kinetyczna (J)')
ax.legend()

plt.show()


# Wykres Ep do czasu
fig, ax = plt.subplots()
plt.ylabel('Energia Potencjalna (J)')
plt.xlabel('Czas')
plt.plot(czasyTab, energiePotencjalne)

scat = ax.scatter(czasyTab[0], energiePotencjalne[0], c="b", label=f'Czas = {round(timer,2)}s')
line2 = ax.plot(czasyTab[0], energiePotencjalne[0], label=f'Energia Potencjalna = {round(energiePotencjalne[-1])}J')[0]
ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(energiePotencjalne)+5], xlabel='Czas (s)', ylabel='Energia Potencjalna (J)')
ax.legend()

plt.show()

    # Wykres z animacją:

# def update(frame):
#     # for each frame, update the data stored on each artist.
#     x = czasyTab[:frame]
#     y = drogiTab[:frame]
#     # update the scatter plot:
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     # update the line plot:
#     line2.set_xdata(czasyTab[:frame])
#     line2.set_ydata(drogiTab[:frame])
#     return (scat, line2)


# ani = animation.FuncAnimation(fig=fig, func=update, frames=3000, interval=TIME*1000)




