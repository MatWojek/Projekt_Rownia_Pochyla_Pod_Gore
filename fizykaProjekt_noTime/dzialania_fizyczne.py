from math import radians, sin, cos

PRZYSPIESZENIE_ZIEMSKIE = 9.81

class DzialaniaFizyczne():
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def przyspieszenieF(wspolczynnik_tarcia, kat_nachylenia):
        return PRZYSPIESZENIE_ZIEMSKIE * (sin(radians(kat_nachylenia)) - wspolczynnik_tarcia * cos(radians(kat_nachylenia)))

    def drogaF(predkosc_poczatkowa, czas, przyspieszenie, wspolczynnik_tarcia): #przyjmuje predkosc_poczatkowa w m/s, czas w s
        return (predkosc_poczatkowa * czas + (przyspieszenie*pow(czas, 2)) / 2 - (wspolczynnik_tarcia * PRZYSPIESZENIE_ZIEMSKIE * pow(czas, 2)) / 2)

    def silaF(masa, kat_nachylenia):
        return masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia))
    
    def maksymalna_wysokoscF(predkosc_poczatkowa, kat_nachylenia, wspolczynnik_tarcia):
        return (pow(predkosc_poczatkowa, 2) * pow(sin(radians(kat_nachylenia)), 2)) / (2 * PRZYSPIESZENIE_ZIEMSKIE * (1 + wspolczynnik_tarcia))

    def czasF(predkosc_poczatkowa, kat_nachylenia, wspolczynnik_tarcia):
        return (2 * predkosc_poczatkowa * sin(radians(kat_nachylenia))) / (PRZYSPIESZENIE_ZIEMSKIE * (1 + wspolczynnik_tarcia))