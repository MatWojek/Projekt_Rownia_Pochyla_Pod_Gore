# stworzenie GUI
# wyświetlenie wyników poniżej, na początku będą ukryte
# podstawienie do wzoru wykonywane na oczach użytkownika, wzory też będą wypisane w gui (jeszcze nie wiem jak)
# pokazuje dane przy wyniku na końcu 
# guzik random, wpisujący randomowe wartości do potrzebnych pól wejścia
# menu do interfejsu gdzie sobie można wybrać co chcesz obliczyć 
# wyświetla wykres w gui 

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QRadioButton, QButtonGroup, QWidget,  QComboBox, QVBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.animation as animation

from dzialania_fizyczne import DzialaniaFizyczne as DF
from wykres import Wykres

class GUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()
        self.wykres = Wykres()
        
    def interfejs(self):

        # informacje na temat tego co mamy wpisać do pól 
        pole1 = QLabel("Współczynnik tarcia: ", self)
        pole2 = QLabel("Prędkość początkowa: ", self)
        pole3 = QLabel("Kąt nachylenia:", self)
        pole4 = QLabel("Długość równi: ", self)
        pole5 = QLabel("Masa przedmiotu:", self)
    
        # pole typu select, pole wyboru, z jednostkami prędkości
        self.select = QComboBox(self)
        self.select.addItem('m/s')
        self.select.addItem('km/h')
        self.select.currentIndexChanged.connect(self.wybranaOpcja)
        
        # jednostki
        pole6 = QLabel("°", self)
        pole7 = QLabel("m", self)
        pole8 = QLabel("kg", self)
        
        # informacje o wprowadzonych danych
        self.pole9 = QLabel("Wprowadzone dane: ", self)
        self.wspolczynnik_tarciaDane = QLabel("Współczynnik tarcia: ", self)
        self.predkosc_poczatkowaDane = QLabel("Prędkość początkowa: ", self)
        self.kat_nachyleniaDane = QLabel("Kąt nachylenia: ", self)
        self.dlugosc_rowniDane = QLabel("Długość równi: ", self)
        self.masaDane = QLabel("Masa przedmiotu: ", self)

        # informacje o wynikach
        self.pole10 = QLabel("Wyniki: ", self)
        self.przyspieszenieWynik = QLabel("Przyspieszenie: ", self)
        self.drogaWynik = QLabel("Przebyta droga: ", self)
        self.czasWynik = QLabel("Czas: ", self)
        self.maksymalna_wysokoscWynik = QLabel("Maksymalna wysokość: ", self)
        self.silaWynik = QLabel("Siła: ", self)
        self.wynik = QLabel("Wynik: ", self)

        self.grupa_radio = QButtonGroup()

        # pole radio, ze wspolczynnikiem tarcia
        self.radio1 = QRadioButton('0.5', self)
        self.radio1.value = 0.5
        self.radio1.setChecked(True)
        self.grupa_radio.addButton(self.radio1)
        
        self.radio2 = QRadioButton('0.7', self)
        self.radio2.value = 0.7
        self.radio2.setChecked(True)
        self.grupa_radio.addButton(self.radio2)
        
        # ukryte wyniki dzialania programu
        self.pole9.hide()
        self.przyspieszenieWynik.hide()
        self.drogaWynik.hide()
        self.czasWynik.hide()
        self.maksymalna_wysokoscWynik.hide()
        self.wynik.hide()
        self.silaWynik.hide()

        # ukryte dane działania programu
        self.pole10.hide()
        self.wspolczynnik_tarciaDane.hide()
        self.predkosc_poczatkowaDane.hide()
        self.dlugosc_rowniDane.hide()
        self.kat_nachyleniaDane.hide()
        self.masaDane.hide()

        # wyświetlenie wszystkich pól, guzików, radio, select 
        uklad = QGridLayout()
        uklad.addWidget(pole1, 1, 0)
        uklad.addWidget(pole2, 2, 0)
        uklad.addWidget(pole3, 3, 0)
        uklad.addWidget(pole4, 4, 0)
        uklad.addWidget(pole5, 5, 0)
        
        uklad.addWidget(self.select, 2, 3)
        uklad.addWidget(pole6, 3, 3)
        uklad.addWidget(pole7, 4, 3)
        uklad.addWidget(pole8, 5, 3)
        
        # wyświetla wprowadzone dane
        uklad.addWidget(self.pole9, 7, 0)
        uklad.addWidget(self.masaDane, 8, 0)
        uklad.addWidget(self.wspolczynnik_tarciaDane, 9, 0)
        uklad.addWidget(self.predkosc_poczatkowaDane, 10, 0)
        uklad.addWidget(self.kat_nachyleniaDane, 11, 0)
        uklad.addWidget(self.dlugosc_rowniDane, 12, 0)

        # wyświetla wyniki 
        uklad.addWidget(self.pole10, 7, 2)
        uklad.addWidget(self.przyspieszenieWynik, 8, 2)
        uklad.addWidget(self.drogaWynik, 9, 2)
        uklad.addWidget(self.czasWynik, 10, 2)
        uklad.addWidget(self.maksymalna_wysokoscWynik, 11, 2)
        uklad.addWidget(self.silaWynik, 12, 2)
        uklad.addWidget(self.wynik, 7, 2)

        # pole do wpisywania danych
        self.predkosc_poczatkowaW = QLineEdit()
        self.kat_nachyleniaW = QLineEdit()
        self.dlugosc_rowni = QLineEdit()
        self.masaW = QLineEdit()
        randomP = QPushButton("&Random", self)
        obliczP = QPushButton("&Oblicz", self)
        
        # układ pól do wpisywania wartości 
        uklad.addWidget(self.radio1, 1, 1)
        uklad.addWidget(self.radio2, 1, 2)
        uklad.addWidget(self.predkosc_poczatkowaW, 2, 1)
        uklad.addWidget(self.kat_nachyleniaW, 3, 1)
        uklad.addWidget(self.masaW, 4, 1)
        uklad.addWidget(self.dlugosc_rowni, 5, 1)

        # guziki
        uklad.addWidget(obliczP, 6, 0, 1, 2)
        uklad.addWidget(randomP, 6, 2, 1, 2)

       
        self.setLayout(uklad)

        obliczP.clicked.connect(self.obliczanie)
        randomP.clicked.connect(self.randomF)

        self.setGeometry(700, 200, 500, 500)
        self.setWindowIcon(QIcon('logo.jpg'))
        self.resize(500, 500)
        self.setMinimumWidth(500)
        self.setMaximumWidth(1000)
        self.setWindowTitle("Równia pochyła w pod górę")
        self.show()

        
    # funkcja do pola select, gdzie są podane jednostki do wyboru
    def wybranaOpcja(self):
        return self.select.currentText()

    # funkcja do pola radio, aby wybrać jakie jest tarcie
    def sprawdzCzyZaznaczone(self):
        sprawdzam = self.grupa_radio.checkedButton()
        if sprawdzam:
            return sprawdzam.value
        else:
            QMessageBox.warning(self, 'Ostrzeżenie', 'Nie zaznaczono żadnej opcji')    
    
    # wszystkie obliczenia
    def obliczanie(self):

        try:
            wspolczynnik_tarcia = float(self.sprawdzCzyZaznaczone())
            kat_nachylenia = float(self.kat_nachyleniaW.text())
            masa = float(self.masaW.text())
            wybor = self.wybranaOpcja()
            predkosc_poczatkowa = float(self.predkosc_poczatkowaW.text())
            if wybor == "km/h": 
                    predkosc_poczatkowa = DF.zamiana_jednostekF(liczba=predkosc_poczatkowa, jednostka=wybor)
            dlugosc_rowni = float(self.dlugosc_rowni.text())
            
            if(kat_nachylenia < 90): # czy kąt jest mniejszy niż 90 stopni

                # obliczanie funkcji i wprowadzenie ich jako tesktu do aplikacji
                przyspieszenieW = DF.przyspieszenieF(wspolczynnik_tarcia=wspolczynnik_tarcia, kat_nachylenia=kat_nachylenia)
                czasW = DF.czasF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
                drogaW = DF.drogaF(predkosc_poczatkowa=predkosc_poczatkowa, czas=czasW, przyspieszenie=przyspieszenieW, wspolczynnik_tarcia=wspolczynnik_tarcia)
                maksymalna_wysokoscW = DF.maksymalna_wysokoscF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
                silaW = DF.silaF(kat_nachylenia=kat_nachylenia, masa=masa)    

                self.wyswietlanie(
                    przyspieszenieW=przyspieszenieW, 
                    czasW=czasW, 
                    maksymalna_wysokoscW=maksymalna_wysokoscW, 
                    silaW=silaW,
                    masa=masa,
                    drogaW=drogaW,
                    wybor=wybor,
                    predkosc_poczatkowa=predkosc_poczatkowa,
                    kat_nachylenia=kat_nachylenia,
                    wspolczynnik_tarcia=wspolczynnik_tarcia,
                    dlugosc_rowni=dlugosc_rowni)
                

            else: # wypadek gdy kąt jest większy niż 90 stopni 
                self.wynik.setText("Nie może być kąt równy/powyżej 90 stopni.")
                self.wynik.show()
                return GUI

        except ValueError:
            self.wynik.setText("Wprowadź prawidłowe liczby!")
            self.wynik.show()

    def randomF(self):
        import random 
        
        wspolczynnik_tarcia = float(random.choice([1.5, 1.7]))
        kat_nachylenia = float(random.uniform(0.0, 89.0))
        masa = float(random.uniform(0.0, 10000.0))
        wybor = random.choice(["km/h", "m/s"])
        predkosc_poczatkowa = float(random.uniform(0.0, 300.0))
        if wybor == "km/h": 
            predkosc_poczatkowa = DF.zamiana_jednostekF(liczba=predkosc_poczatkowa, jednostka=wybor)
        dlugosc_rowni = float(random.uniform(0.0, 10000.0))

        # obliczanie funkcji i wprowadzenie ich jako tesktu do aplikacji
        przyspieszenieW = DF.przyspieszenieF(wspolczynnik_tarcia=wspolczynnik_tarcia, kat_nachylenia=kat_nachylenia)
        czasW = DF.czasF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
        drogaW = DF.drogaF(predkosc_poczatkowa=predkosc_poczatkowa, czas=czasW, przyspieszenie=przyspieszenieW, wspolczynnik_tarcia=wspolczynnik_tarcia)
        maksymalna_wysokoscW = DF.maksymalna_wysokoscF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
        silaW = DF.silaF(kat_nachylenia=kat_nachylenia, masa=masa)    

        self.wyswietlanie(
                    przyspieszenieW=przyspieszenieW, 
                    czasW=czasW, 
                    maksymalna_wysokoscW=maksymalna_wysokoscW, 
                    silaW=silaW,
                    masa=masa,
                    wybor=wybor,
                    drogaW=drogaW,
                    predkosc_poczatkowa=predkosc_poczatkowa,
                    kat_nachylenia=kat_nachylenia,
                    wspolczynnik_tarcia=wspolczynnik_tarcia,
                    dlugosc_rowni=dlugosc_rowni)
        
    def wyswietlanie(self, maksymalna_wysokoscW, przyspieszenieW, czasW, drogaW, silaW, wybor, wspolczynnik_tarcia, kat_nachylenia, masa, dlugosc_rowni, predkosc_poczatkowa):

        # wypisanie danych
        maksymalna_wysokoscWynik = f"Maksymalna wysokość: {round(maksymalna_wysokoscW, 2)} m"
        przyspieszenieWynik = f"Przyspieszenie: {round(przyspieszenieW, 2)} m/s²"
        czasWynik = f"Czas: {round(czasW, 2)} s"
        drogaWynik = f"Przebyta droga: {round(drogaW, 2)} m"
        silaWynik = f"Siła: {round(silaW, 2)} kg"

        # wpisanie wyników do zmiennych
        wspolczynnik_tarciaD = f"Współczynnik tarcia: {wspolczynnik_tarcia}"
        if wybor == "km/h":
            predkosc_poczatkowa = DF.zamiana_jednostekF(liczba=predkosc_poczatkowa, jednostka="m/s")
        predkosc_poczatkowaD = f"Prędkość początkowa: {round(predkosc_poczatkowa, 2)} {wybor}"
        kat_nachyleniaD = f"Kąt nachylenia: {round(kat_nachylenia,2)} °"
        masaD = f"Masa: {round(masa,2)} kg"
        dlugosc_rowniD = f"Długość równi: {round(dlugosc_rowni,2)} m"

        # wypisanie danych 
        self.predkosc_poczatkowaDane.setText(predkosc_poczatkowaD)
        self.dlugosc_rowniDane.setText(dlugosc_rowniD)
        self.wspolczynnik_tarciaDane.setText(wspolczynnik_tarciaD)
        self.kat_nachyleniaDane.setText(kat_nachyleniaD)
        self.masaDane.setText(masaD)
        self.silaWynik.setText(silaWynik)

        # wypisanie wyników
        self.przyspieszenieWynik.setText(przyspieszenieWynik)
        self.czasWynik.setText(czasWynik)
        self.drogaWynik.setText(drogaWynik)
        self.maksymalna_wysokoscWynik.setText(maksymalna_wysokoscWynik)
                
        # pokazanie wyników 
        self.pole9.show()
        self.przyspieszenieWynik.show()
        self.czasWynik.show()
        self.drogaWynik.show()
        self.maksymalna_wysokoscWynik.show()
        self.silaWynik.show()
              
        # pokazanie danych 
        self.pole10.show()
        self.predkosc_poczatkowaDane.show()
        self.dlugosc_rowniDane.show()
        self.wspolczynnik_tarciaDane.show()
        self.kat_nachyleniaDane.show()
        self.masaDane.show()
                
        # zmiana rozmiaru okna
        self.resize(600,600)

        self.wykres.petla(predkosc_poczatkowa=predkosc_poczatkowa, dlugosc_rowni=dlugosc_rowni,
                              przyspieszenie=przyspieszenieW)