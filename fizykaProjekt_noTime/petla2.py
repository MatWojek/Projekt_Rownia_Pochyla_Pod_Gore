import time
import os
import math


# Instalacja matplotlib:
    # python -m pip install -U pip
    # python -m pip install -U matplotlib

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.animation as animation


from maxWys import maxHeight, czas
from przysp_droga_force import przyspieszenie, droga, force

G = 9.80665

file = open("wyniki.csv", "w")
os.system('cls')

v0 = 22
m = 10
alfa = 30
u = 1 # współczynnik tarcia
s = 30

timer = 0
droga = 0

czasyTab = []
drogiTab = []
predkosciTab = []

a = przyspieszenie(u, alfa)
t = czas(v0, alfa, s, u)

TIME = 0.2 # Co ile sprawdzać prędkość i drogę (s)

file.write(f"0, 0, {v0:.2f}\n")
drogiTab.append(0)
czasyTab.append(0)
predkosciTab.append(v0)
while(v0 > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
    if(v0 < abs(a)*TIME): # gdy 'v0 - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
        droga += v0 * v0/abs(a)
        drogiTab.append(droga)
        timer += v0*TIME/abs(a)
        czasyTab.append(timer)
        print("v =", v0)
        predkosciTab.append(v0)
        v0 = 0
        print("v =", v0)
        file.write(f"{timer:.2f}, {droga:.2f}, {v0:.2f}")
        break
    # time.sleep(TIME) # Można zakomentować, nic nie zmienia tylko pokazuje jak to gówno działa :)
    print("v =", v0)
    timer += TIME
    czasyTab.append(timer)
    v0 -= abs(a)*TIME
    predkosciTab.append(v0)
    droga += v0*TIME
    drogiTab.append(droga)
    file.write(f"{timer:.2f}, {droga:.2f}, {v0:.2f}\n")

file.close()
maxHeight = math.sin(math.radians(alfa)) * droga
print(f"Czas: {timer:.2f}s")
print(f"Przebyta droga: {droga:.2f}m")
print(f"Max wysokość: {maxHeight:.2f}m")


fig, ax = plt.subplots()
# plt.ylabel('Przebyta droga')
# plt.xlabel('Czas')
# plt.plot(czasyTab, drogiTab)


# Wykres z animacją:
scat = ax.scatter(czasyTab[0], drogiTab[0], c="b", label=f'Czas = {timer:.2f}s')
line2 = ax.plot(czasyTab[0], drogiTab[0], label=f'Droga = {droga:.2f}m')[0]
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

