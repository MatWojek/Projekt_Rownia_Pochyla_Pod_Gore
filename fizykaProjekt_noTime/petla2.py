import time
import os
import math

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

a = przyspieszenie(u, alfa)
t = czas(v0, alfa, s, u)

TIME = 0.5 # Co ile sprawdzać prędkość i drogę (s)

file.write(f"0, 0, {v0:.2f}\n")
while(v0 > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
    if(v0 < abs(a)*TIME): # gdy 'v0 - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
        droga += v0 * v0/abs(a)
        timer += v0*TIME/abs(a)
        print("v =", v0)
        v0 = 0
        print("v =", v0)
        file.write(f"{timer:.2f}, {droga:.2f}, {v0:.2f}")
        break

    # time.sleep(TIME) # Można zakomentować, nic nie zmienia tylko pokazuje jak to gówno działa :)
    print("v =", v0)
    timer += TIME
    v0 -= abs(a)*TIME
    droga += v0*TIME
    file.write(f"{timer:.2f}, {droga:.2f}, {v0:.2f}\n")

file.close()
maxHeight = math.sin(math.radians(alfa)) * droga
print(f"Czas: {timer:.2f}s")
print(f"Przebyta droga: {droga:.2f}m")
print(f"Max wysokość: {maxHeight:.2f}m")