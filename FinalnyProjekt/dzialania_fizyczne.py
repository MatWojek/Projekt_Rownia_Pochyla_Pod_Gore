from math import sin, cos, radians

from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

PRZYSPIESZENIE_ZIEMSKIE = 9.81
TIME = 0.001

class DzialaniaFizyczne():
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.droga = 0
        self.czyDojechalDoKonca = False

        self.czasyTab = []
        self.drogiTab = []
        self.predkosciTab = []
        self.energieKinetyczne = []
        self.energiePotencjalne =[]

    
    def przyspieszenieF(wspolczynnik_tarcia, kat_nachylenia):
        return PRZYSPIESZENIE_ZIEMSKIE * (sin(radians(kat_nachylenia)) + wspolczynnik_tarcia * cos(radians(kat_nachylenia)))

    def drogaF(predkosc_poczatkowa, czas, przyspieszenie, wspolczynnik_tarcia): #przyjmuje predkosc_poczatkowa w m/s, czas w s
        return (predkosc_poczatkowa * czas + (przyspieszenie*pow(czas, 2)) / 2 - (wspolczynnik_tarcia * PRZYSPIESZENIE_ZIEMSKIE * pow(czas, 2)) / 2)

    def silaF(masa, kat_nachylenia):
        return masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia))
    
    def maksymalna_wysokoscF(predkosc_poczatkowa, kat_nachylenia, wspolczynnik_tarcia):
        return (pow(predkosc_poczatkowa, 2) * pow(sin(radians(kat_nachylenia)), 2)) / (2 * PRZYSPIESZENIE_ZIEMSKIE * (1 + wspolczynnik_tarcia))

    def czasF(predkosc_poczatkowa, kat_nachylenia, wspolczynnik_tarcia):
        return (2 * predkosc_poczatkowa * sin(radians(kat_nachylenia))) / (PRZYSPIESZENIE_ZIEMSKIE * (1 + wspolczynnik_tarcia))
    
    def zamiana_jednostekF(liczba, jednostka):
        if jednostka == "km/h":
            return (liczba * 1000) / 3600
        elif jednostka == "m/s":
            return (liczba * 3600) / 1000
        else: 
            return "Została podana błędna jednostka." 
        
    def energia_kinetyczna(masa, predkosc_poczatkowa):
        return (masa*pow(predkosc_poczatkowa, 2) / 2)
    
    def energia_potencjalna(masa, kat_nachylenia):
        return (masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia)))
    
    def maksymalna_wysokoscWynik(kat_nachylenia, droga):
        return (sin(radians(kat_nachylenia)) * droga)


    def wyswietl_wykres(self, czasyTab, drogiTab, timer, droga, energiePotencjalne, energieKinetyczne):

        self.dane_do_wykresu(czasyTab=czasyTab, drogiTab=drogiTab, timer=timer, droga=droga, energieKinetyczne=energieKinetyczne, energiePotencjalne=energiePotencjalne)

    
    def dane_do_wykresu(self, czasyTab, drogiTab, timer, droga, energiePotencjalne, energieKinetyczne):

        # Wykres Przebytej drogi do czasu
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)

        self.ax.set_title("Wykres zależności drogi od czasu")
        plt.ylabel('Przebyta droga')
        plt.xlabel('Czas')
        plt.plot(czasyTab, drogiTab)

        scat = self.ax.scatter(czasyTab[0], drogiTab[0], c="b", label=f'Czas = {round(timer,2)}s')
        line2 = self.ax.plot(czasyTab[0], drogiTab[0], label=f'Droga = {round(droga)}m')[0]
        self.ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(drogiTab)+5], xlabel='Czas (s)', ylabel='Droga (m)')
        self.ax.legend()

        plt.show()


        # Wykres Ek do Ep
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Wykres zależności energii potencjalnej do kinetycznej")
        plt.ylabel('Energia Potencjalna (J)')
        plt.xlabel('Energie Kinetyczne (J)')
        plt.plot(energiePotencjalne, energieKinetyczne)

        scat = self.ax.scatter(energiePotencjalne[0], energieKinetyczne[0], c="b", label=f'Energia Kinetyczna = {round(energieKinetyczne[-1],2)}J')
        line2 = self.ax.plot(energiePotencjalne[0], energieKinetyczne[0], label=f'Energia Potencjalna = {round(energiePotencjalne[-1])}J')[0]
        self.ax.set(xlim=[0, max(energiePotencjalne)+5], ylim=[0, max(energieKinetyczne)], xlabel='Energia Potencjalna (J)', ylabel='Energia Kinetyczna (J)')
        self.ax.legend()

        self.canvas.draw()
        plt.show()

        # Wykres Ek do czasu
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Wykres zależności energii kinetycznej do czasu")
        plt.ylabel('Energia Kinetyczna (J)')
        plt.xlabel('Czas')
        plt.plot(czasyTab, energieKinetyczne)

        scat = self.ax.scatter(czasyTab[0], energieKinetyczne[0], c="b", label=f'Czas = {round(timer,2)}s')
        line2 = self.ax.plot(czasyTab[0], energieKinetyczne[0], label=f'Energia Kinetyczna = {round(energieKinetyczne[-1])}J')[0]
        self.ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(energieKinetyczne)+5], xlabel='Czas (s)', ylabel='Energia Kinetyczna (J)')
        self.ax.legend()

        self.canvas.draw()
        plt.show()


        # Wykres Ep do czasu
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Wykres zależności energii potencjalnej do czasu")
        plt.ylabel('Energia Potencjalna (J)')
        plt.xlabel('Czas')
        plt.plot(czasyTab, energiePotencjalne)

        scat = self.ax.scatter(czasyTab[0], energiePotencjalne[0], c="b", label=f'Czas = {round(timer,2)}s')
        line2 = self.ax.plot(czasyTab[0], energiePotencjalne[0], label=f'Energia Potencjalna = {round(energiePotencjalne[-1])}J')[0]
        self.ax.set(xlim=[0, max(czasyTab)], ylim=[0, max(energiePotencjalne)+5], xlabel='Czas (s)', ylabel='Energia Potencjalna (J)')
        self.ax.legend()

        self.canvas.draw()
        plt.show()

    #         # Wykres z animacją:

    #     # def update(frame):
    #     #     # for each frame, update the data stored on each artist.
    #     #     x = czasyTab[:frame]
    #     #     y = drogiTab[:frame]
    #     #     # update the scatter plot:
    #     #     data = np.stack([x, y]).T
    #     #     scat.set_offsets(data)
    #     #     # update the line plot:
    #     #     line2.set_xdata(czasyTab[:frame])
    #     #     line2.set_ydata(drogiTab[:frame])
    #     #     return (scat, line2)


    #     # ani = animation.FuncAnimation(fig=fig, func=update, frames=3000, interval=TIME*1000)





                