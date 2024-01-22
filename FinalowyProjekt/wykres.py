import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.animation as animation
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

TIME = 0.2 # Co ile sprawdzać prędkość i drogę
class Wykres():

    def __init__(self):
        super(Wykres, self).__init__()
        self.timer = 0
        self.czyDojechalDoKonca = False
        self.czasPrzejazduRowni = 0 
        self.droga = 0 
        self.czasyTab = []
        self.drogiTab = []
        self.predkosciTab = []

    def petla(self, predkosc_poczatkowa, przyspieszenie, dlugosc_rowni):

        file = open("wyniki.csv", "w")

        # obliczony_czas = DzialaniaFizyczne.czas(predkosc_poczatkowa, kat_nachylenia, droga, WSPOLCZYNNIK_TARCIA)
        file.write(f"0, 0, {round(predkosc_poczatkowa, 2)}\n")
        self.drogiTab.append(0)
        self.czasyTab.append(0)
        self.predkosciTab.append(predkosc_poczatkowa)
        while(predkosc_poczatkowa > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
            if(predkosc_poczatkowa < abs(przyspieszenie)*TIME): # gdy 'predkosc_poczatkowa - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
                self.droga += predkosc_poczatkowa * predkosc_poczatkowa/abs(przyspieszenie)
                self.drogiTab.append(self.droga)
                self.timer += predkosc_poczatkowa*TIME/abs(przyspieszenie)
                self.czasyTab.append(self.timer)
                self.predkosciTab.append(predkosc_poczatkowa)
                predkosc_poczatkowa = 0
                file.write(f"{round(self.timer, 2)}, {round(self.droga, 2)}, {round(predkosc_poczatkowa, 2)}")
                break
                # time.sleep(TIME) # Można zakomentować, nic nie zmienia
            self.timer += TIME
            self.czasyTab.append(self.timer)
            predkosc_poczatkowa -= abs(przyspieszenie)*TIME - 1/2*abs(przyspieszenie)*pow(TIME,2)
            self.predkosciTab.append(predkosc_poczatkowa)
            self.droga += predkosc_poczatkowa*TIME
            self.drogiTab.append(self.droga)
            file.write(f"{round(self.timer, 2)}, {round(self.droga, 2)}, {round(predkosc_poczatkowa,2)}\n")

            # Sprawdza czy zaraz dojedziemy do końca równi lub czy już nie dojechaliśmy
            if(self.czyDojechalDoKonca == False and (dlugosc_rowni < self.droga + (predkosc_poczatkowa - abs(przyspieszenie)*TIME))):
                self.czyDojechalDoKonca = True
                pozostala_droga = dlugosc_rowni - self.droga
                pozostaly_czas = pozostala_droga / predkosc_poczatkowa
                self.predkosc_koncowa = (predkosc_poczatkowa - abs(przyspieszenie)*pozostaly_czas)
                self.czasPrzejazduRowni = self.timer + pozostaly_czas

                if( self.czasPrzejazduRowni != 0):
                    print(f"Czas przejazdu równi: {round( self.czasPrzejazduRowni, 2)}s")
                    print(f"Prędkość na końcu równi: {round( self.predkosc_koncowa, 2)}m/s")
                else: 
                    print("Nie przejechał równi")

        file.close()
    

    def wyswietlanie_wykresu(self, os_x, os_y):
        fig, ax = plt.subplots()
        scat = ax.scatter(os_x[0], os_y[0], c="b", label=f'Czas = {round(os_x[0],2)}s')
        line2 = ax.plot(os_x[0], os_y[0], label=f'Droga = {round(os_y[0])}m')[0]
        ax.set(xlim=[0, max(os_x)], ylim=[0, max(os_y)+5], xlabel='Czas (s)', ylabel='Droga (m)')
        ax.legend()

        def update(frame):
            x = os_x[:frame]
            y = os_y[:frame]
            scat.set_offsets(np.stack([x, y]).T)
            line2.set_xdata(x)
            line2.set_ydata(y)
            return (scat, line2)

        ani = animation.FuncAnimation(fig=fig, func=update, frames=len(os_x), interval=TIME*1000)
        plt.show()