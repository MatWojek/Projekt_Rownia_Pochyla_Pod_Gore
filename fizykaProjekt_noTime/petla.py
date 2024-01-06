import time
import os
import math

from maxWys import maxHeight, czas
from przysp_droga_force import przyspieszenie, droga, force
G = 9.80665

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


while(v0 > 0): # 'co sekunde' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
    if(v0 - abs(a) < 0): # gdy 'v0 - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
        droga += v0 * v0/abs(a)
        timer += v0/abs(a)
        print("v =", v0)
        v0 = 0
        print("v =", v0)
        break

    time.sleep(1) # Można zakomentować, nic nie zmienia tylko pokazuje jak to gówno działa :)
    print("v =", v0)
    timer += 1
    v0 -= abs(a)
    droga += v0


maxHeight = math.sin(math.radians(alfa)) * droga
print(f"Czas: {timer:.2f}s")
print(f"Przebyta droga: {droga:.2f}m")
print(f"Max wysokość: {maxHeight:.2f}m")