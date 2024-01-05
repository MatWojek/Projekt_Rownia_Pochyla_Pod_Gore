import os
# import math

from maxWys import maxHeight, czas
from przysp_droga_force import przyspieszenie, droga, force
G = 9.80665

os.system('cls')

print("Program do obliczania równi pochyłej")

# v0 = float(input("Podaj prędkość początkową obiektu (m/s): "))
# m = float(input("Podaj mase obiektu (kg): "))
# alfa = float(input("Podaj kąt nachylenia równi (°): "))
# u = float(input("Podaj współczynnik tarcia: "))

v0 = 20
m = 10
alfa = 30
u = 0.5
s = 30

a = przyspieszenie(u, alfa)
t = czas(v0, alfa, s, u)

os.system('cls')

print(f"Przyśpieszenie: {a:.2f}m/s²")
print(f"Droga przebyta: {droga(v0, t, a, u):.2f}m")
print(f"Max wysokość: {maxHeight(v0, alfa, u):.2f}m")
print(f"Czas: {t:.2f}s")
print(f"Siła nacisku: {force(m, alfa):.2f}N")
print(f"Prędkość końcowa: {force(m, alfa):.2f}m/s")
