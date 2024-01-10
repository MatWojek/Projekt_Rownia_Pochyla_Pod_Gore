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
TIME = 0.2 # Co ile sprawdzać prędkość i drogę
WSPOLCZYNNIK_TARCIA = 1

file = open("wyniki.csv", "w")
os.system('cls')

predkosc_poczatkowa = float(input("Podaj prędkość początkową: "))
masa = 10
kat_nachylenia = float(input("Podaj kąt nachylenia: "))
droga = 30

timer = 0 
droga = 0 

czasyTab = []
drogiTab = []
predkosciTab = []

obliczone_przyspieszenie = przyspieszenie(WSPOLCZYNNIK_TARCIA, kat_nachylenia)
obliczony_czas = czas(predkosc_poczatkowa, kat_nachylenia, s, WSPOLCZYNNIK_TARCIA)

file.write(f"0, 0, {round(predkosc_poczatkowa, 2)}\n")
drogiTab.append(0)
czasyTab.append(0)
predkosciTab.append(predkosc_poczatkowa)
while(predkosc_poczatkowa > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
    if(predkosc_poczatkowa < abs(obliczone_przyspieszenie)*TIME): # gdy 'predkosc_poczatkowa - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
        droga += predkosc_poczatkowa * predkosc_poczatkowa/abs(obliczone_przyspieszenie)
        drogiTab.append(droga)
        timer += predkosc_poczatkowa*TIME/abs(obliczone_przyspieszenie)
        czasyTab.append(timer)
        print("v =", predkosc_poczatkowa)
        predkosciTab.append(predkosc_poczatkowa)
        predkosc_poczatkowa = 0
        print("v =", predkosc_poczatkowa)
        file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa, 2)}")
        break
    # time.sleep(TIME) # Można zakomentować, nic nie zmienia tylko pokazuje jak to gówno działa :)
    print("v =", predkosc_poczatkowa)
    timer += TIME
    czasyTab.append(timer)
    predkosc_poczatkowa -= abs(obliczone_przyspieszenie)*TIME
    predkosciTab.append(predkosc_poczatkowa)
    droga += predkosc_poczatkowa*TIME
    drogiTab.append(droga)
    file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa,2)}\n")

file.close()
maxHeight = math.sin(math.radians(kat_nachylenia)) * s
print(f"Czas: {timer:.2f}s")
print(f"Przebyta droga: {droga:.2f}m")
print(f"Max wysokość: {maxHeight:.2f}m")


fig, ax = plt.subplots()
# plt.ylabel('Przebyta droga')
# plt.xlabel('Czas')
# plt.plot(czasyTab, drogiTab)


# Wykres z animacją:
scat = ax.scatter(czasyTab[0], drogiTab[0], c="b", label=f'Czas = {round(timer,2)}s')
line2 = ax.plot(czasyTab[0], drogiTab[0], label=f'Droga = {round(droga)}m')[0]
ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(drogiTab)+5], xlabel='Czas (s)', ylabel='Droga (m)')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    x = czasyTab[:frame]
    y = drogiTab[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(czasyTab[:frame])
    line2.set_ydata(drogiTab[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=200, interval=TIME*1000)
plt.show()

