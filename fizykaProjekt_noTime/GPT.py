import math
import os
def oblicz_parametry_ruchu(v_poczatkowa, kat, wspolczynnik_tarcia, grawitacja=9.8):
    # v_poczatkowa - początkowa prędkość obiektu
    # kat - kąt nachylenia równi w stopniach
    # wspolczynnik_tarcia - współczynnik tarcia między obiektem a równią
    
    # Przeliczamy kąt na radiany
    kat_radiany = math.radians(kat)
    
    # Obliczamy prędkość końcową
    v_koncowa = v_poczatkowa * math.cos(kat_radiany) / (1 + wspolczynnik_tarcia)
    
    # Obliczamy maksymalną wysokość
    max_wysokosc = (v_poczatkowa**2 * math.sin(2 * kat_radiany)) / (2 * grawitacja * (1 + wspolczynnik_tarcia)**2)
    
    # Obliczamy drogę przebytą
    droga = (v_poczatkowa**2 * math.sin(2 * kat_radiany)) / grawitacja
    
    # Obliczamy czas
    czas = (2 * v_poczatkowa * math.sin(kat_radiany)) / (grawitacja * (1 + wspolczynnik_tarcia))
    
    # Obliczamy przyspieszenie
    przyspieszenie = grawitacja * math.sin(kat_radiany) / (1 + wspolczynnik_tarcia)
    
    return v_koncowa, max_wysokosc, droga, czas, przyspieszenie

# Przykładowe dane
# v_poczatkowa = float(input("Podaj początkową prędkość (m/s): "))
# kat = float(input("Podaj kąt nachylenia równi (stopnie): "))
# wspolczynnik_tarcia = float(input("Podaj współczynnik tarcia: "))

v_poczatkowa = 20
kat = 30
wspolczynnik_tarcia = 0.5
os.system('cls')
# Wywołujemy funkcję i wyświetlamy wyniki
wyniki = oblicz_parametry_ruchu(v_poczatkowa, kat, wspolczynnik_tarcia)
print(f"Prędkość końcowa: {wyniki[0]:.2f} m/s")
print(f"Maksymalna wysokość: {wyniki[1]:.2f} metrów")
print(f"Droga przebyta: {wyniki[2]:.2f} metrów")
print(f"Czas: {wyniki[3]:.2f} sekundy")
print(f"Przyspieszenie: {wyniki[4]:.2f} m/s^2")
