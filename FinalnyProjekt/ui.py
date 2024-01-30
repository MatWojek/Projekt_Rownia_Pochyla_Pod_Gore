from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox, QRadioButton, QButtonGroup,  QWidget
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from dzialania_fizyczne import DzialaniaFizyczne as DF
TIME = 0.001

class GUI(QWidget):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)

        self.interfejs()
        
    def interfejs(self):

        # informacje na temat tego co mamy wpisać do pól 
        pole1 = QLabel("Współczynnik tarcia: ", self)
        pole2 = QLabel("Prędkość początkowa: ", self)
        pole3 = QLabel("Kąt nachylenia:", self)
        pole4 = QLabel("Długość równi: ", self)
        pole5 = QLabel("Masa przedmiotu:", self)
    
        # jednostki
        pole11 = QLabel("m/s", self)
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
        self.predkosc_koncowaWynik = QLabel("Prędkość końcowa: ", self)
        self.czas_przejazduWynik = QLabel("Czas Przejazdu równi: ", self)
        self.innyWynik = QLabel("",self)
        self.wynik = QLabel("Wynik: ", self)
        
        self.hideF()

        # wyświetlenie wszystkich pól, guzików, radio, 
        uklad = QGridLayout()
        uklad.addWidget(pole1, 1, 0)
        uklad.addWidget(pole2, 2, 0)
        uklad.addWidget(pole3, 3, 0)
        uklad.addWidget(pole4, 4, 0)
        uklad.addWidget(pole5, 5, 0)
        
        uklad.addWidget(pole11, 2, 3)
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
        uklad.addWidget(self.predkosc_koncowaWynik, 13, 2)
        uklad.addWidget(self.czas_przejazduWynik, 14, 2)
        uklad.addWidget(self.innyWynik, 13, 2)

        # pole do wpisywania danych
        self.wspolczynnik_tarciaW = QLineEdit()
        self.predkosc_poczatkowaW = QLineEdit()
        self.kat_nachyleniaW = QLineEdit()
        self.dlugosc_rowni = QLineEdit()
        self.masaW = QLineEdit()
        randomP = QPushButton("&Random", self)
        obliczP = QPushButton("&Oblicz", self)
        wyswietl_wykresyP = QPushButton("&Wyswietl Wykesy", self)
        
        # układ pól do wpisywania wartości 
        uklad.addWidget(self.wspolczynnik_tarciaW, 1, 1)
        uklad.addWidget(self.predkosc_poczatkowaW, 2, 1)
        uklad.addWidget(self.kat_nachyleniaW, 3, 1)
        uklad.addWidget(self.dlugosc_rowni, 4, 1)
        uklad.addWidget(self.masaW, 5, 1)

        # guziki
        uklad.addWidget(obliczP, 6, 0, 1, 1)
        uklad.addWidget(randomP, 6, 1, 1, 1)
        uklad.addWidget(wyswietl_wykresyP, 6, 2, 1, 1)

        self.setLayout(uklad)

        obliczP.clicked.connect(self.obliczanieF)
        randomP.clicked.connect(self.randomF)
        wyswietl_wykresyP.clicked.connect(self.wyswietl_wykresyF)

        self.setGeometry(700, 200, 500, 500)
        self.setWindowIcon(QIcon('logo.jpg'))
        self.resize(500, 500)
        self.setMinimumWidth(500)
        self.setMaximumWidth(1000)
        self.setWindowTitle("Równia pochyła w pod górę")
        self.show()

  
        
    def hideF(self):
        # ukryte wyniki dzialania programu
        self.pole9.hide()
        self.przyspieszenieWynik.hide()
        self.drogaWynik.hide()
        self.czasWynik.hide()
        self.maksymalna_wysokoscWynik.hide()
        self.wynik.hide()
        self.silaWynik.hide()
        self.innyWynik.hide()
        self.czas_przejazduWynik.hide()
        self.predkosc_koncowaWynik.hide()

        # ukryte dane działania programu
        self.pole10.hide()
        self.wspolczynnik_tarciaDane.hide()
        self.predkosc_poczatkowaDane.hide()
        self.dlugosc_rowniDane.hide()
        self.kat_nachyleniaDane.hide()
        self.masaDane.hide()

    def showF(self):
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
    
    def obliczF(self, wspolczynnik_tarcia, kat_nachylenia, masa, predkosc_poczatkowa, dlugosc_rowni):
         # obliczanie funkcji i wprowadzenie ich jako tesktu do aplikacji
                przyspieszenieW = DF.przyspieszenieF(wspolczynnik_tarcia=wspolczynnik_tarcia, kat_nachylenia=kat_nachylenia)
                energia_kinetycznaW = DF.energia_kinetyczna(masa=masa, predkosc_poczatkowa=predkosc_poczatkowa)
                energia_potencjalnaW = DF.energia_potencjalna(masa=masa, kat_nachylenia=kat_nachylenia)
                silaW = DF.silaF(masa=masa, kat_nachylenia=kat_nachylenia)

                self.pelny_wynik(
                    wspolczynnik_tarcia=wspolczynnik_tarcia,
                    kat_nachylenia=kat_nachylenia,
                    masa=masa,
                    predkosc_poczatkowa=predkosc_poczatkowa,
                    przyspieszenie=przyspieszenieW, 
                    energia_kinetyczna=energia_kinetycznaW,
                    energia_potencjalna=energia_potencjalnaW,
                    sila=silaW,
                    dlugosc_rowni=dlugosc_rowni,
                    pierwsza_predkosc_poczatkowa=predkosc_poczatkowa
                    )



    def obliczanieF(self): 
        
        try:

            self.hideF()

            wspolczynnik_tarcia = float(self.wspolczynnik_tarciaW.text())
            kat_nachylenia = float(self.kat_nachyleniaW.text())
            masa = float(self.masaW.text())
            predkosc_poczatkowa = float(self.predkosc_poczatkowaW.text())
            dlugosc_rowni = float(self.dlugosc_rowni.text())
            
            if (wspolczynnik_tarcia < 0 or kat_nachylenia < 0 or masa < 0 or predkosc_poczatkowa < 0 or dlugosc_rowni < 0):
                    QMessageBox.warning(self, "Błąd", "Żadna z wartości nie powinna być ujemna")
            
            else:

                if(kat_nachylenia < 90): # czy kąt jest mniejszy niż 90 stopni
                    if (wspolczynnik_tarcia > 1.0):
                        pytanie = QMessageBox.question(self, "Pytanie", "Czy na pewno chcesz kontynuować z większym współczynnikiem tarcia?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if pytanie == QMessageBox.Yes:
                            self.obliczF(
                                wspolczynnik_tarcia=wspolczynnik_tarcia,
                                kat_nachylenia=kat_nachylenia,
                                predkosc_poczatkowa=predkosc_poczatkowa,
                                masa=masa,
                                dlugosc_rowni=dlugosc_rowni,
                            )
                        else: 
                            QMessageBox.warning(self, "Błąd", "Wprowadź poprawny współczynnik tarcia")
                    else: 
                        self.obliczF(
                                wspolczynnik_tarcia=wspolczynnik_tarcia,
                                kat_nachylenia=kat_nachylenia,
                                predkosc_poczatkowa=predkosc_poczatkowa,
                                masa=masa,
                                dlugosc_rowni=dlugosc_rowni,
                            )
                            

                else: # wypadek gdy kąt jest większy niż 90 stopni 
                    QMessageBox.warning(self, "Błąd", "Nie może być kąt równy/powyżej 90 stopni")

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Proszę wprowadzić poprawne dane liczbowe.")
    
    def randomF(self):
        import random 

        self.hideF()
        
        wspolczynnik_tarcia = float(random.uniform(0.01, 1.0))
        kat_nachylenia = float(random.uniform(0.0, 89.0))
        masa = float(random.uniform(0.0, 10000.0))
        predkosc_poczatkowa = float(random.uniform(0.0, 300.0))
        dlugosc_rowni = float(random.uniform(0.0, 10000.0))

        # obliczanie funkcji i wprowadzenie ich jako tesktu do aplikacji
        przyspieszenieW = DF.przyspieszenieF(wspolczynnik_tarcia=wspolczynnik_tarcia, kat_nachylenia=kat_nachylenia)
        energia_kinetycznaW = DF.energia_kinetyczna(masa=masa, predkosc_poczatkowa=predkosc_poczatkowa)
        energia_potencjalnaW = DF.energia_potencjalna(masa=masa, kat_nachylenia=kat_nachylenia)
        silaW = DF.silaF(masa=masa, kat_nachylenia=kat_nachylenia)

        self.pelny_wynik(
                    wspolczynnik_tarcia=wspolczynnik_tarcia,
                    kat_nachylenia=kat_nachylenia,
                    masa=masa,
                    predkosc_poczatkowa=predkosc_poczatkowa,
                    przyspieszenie=przyspieszenieW, 
                    energia_kinetyczna=energia_kinetycznaW,
                    energia_potencjalna=energia_potencjalnaW,
                    sila=silaW,
                    dlugosc_rowni=dlugosc_rowni,
                    pierwsza_predkosc_poczatkowa=predkosc_poczatkowa
                )
        
    def wyswietl_wykresyF(self):
        self.wykres = DF()
        try:
            self.wykres.wyswietl_wykres(czasyTab=self.czasyTab, 
                                        energieKinetyczne=self.energieKinetyczne, 
                                        energiePotencjalne=self.energiePotencjalne,
                                        drogiTab=self.drogiTab, 
                                        droga=self.droga, 
                                        timer=self.timer,
                                        predkosciTab=self.predkosciTab)
        except AttributeError: 
            QMessageBox.warning(self, "Błąd", "Brak odpowiednich wartości.")

    def pelny_wynik(self, pierwsza_predkosc_poczatkowa, przyspieszenie, dlugosc_rowni, energia_potencjalna, energia_kinetyczna, masa, predkosc_poczatkowa, wspolczynnik_tarcia, kat_nachylenia, sila):
        PRZYSPIESZENIE_ZIEMSKIE = 9.81
        from math import sin, cos, radians
        with open("wyniki.csv", "w") as file:
            timer = 0 
            droga = 0
            czyDojechalDoKonca = False

            czasyTab = []
            drogiTab = []
            predkosciTab = []
            energieKinetyczne = []
            energiePotencjalne =[]

            file.write(f"Czas, Droga, Pręd\n")
            file.write(f"0, 0, {round(predkosc_poczatkowa, 2)}\n")

            drogiTab.append(0)
            czasyTab.append(0)
            predkosciTab.append(predkosc_poczatkowa)
            energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
            energiePotencjalne.append(masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia)) * droga)

            while(predkosc_poczatkowa > 0): # 'Co TIME' odejmuje od prędkości wartość opóźnienia, dodaje do przebytej drogi odl jaką w tą sekunde przejechał obiekt
                if(predkosc_poczatkowa < abs(przyspieszenie)*TIME): # gdy 'predkosc_poczatkowa - a' będzie ujemne trzeba odjąć mniej bo ten złom ma się zatrzymać a nie cofać
                    droga += predkosc_poczatkowa * predkosc_poczatkowa/abs(przyspieszenie)
                    drogiTab.append(droga)
                    timer += predkosc_poczatkowa*TIME/abs(przyspieszenie)
                    czasyTab.append(timer)
                    # print("v =", predkosc_poczatkowa)
                    predkosciTab.append(predkosc_poczatkowa)
                    predkosc_poczatkowa = 0
                    energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
                    energiePotencjalne.append(masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia)) * droga)

                    # print("v =", predkosc_poczatkowa)
                    file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa, 2)}")
                    break
                # time.sleep(TIME) # Można zakomentować, nic nie zmienia
                
                # print("v =", predkosc_poczatkowa)
                timer += TIME
                czasyTab.append(timer)
                predkosc_poczatkowa -= abs(przyspieszenie)*TIME
                predkosciTab.append(predkosc_poczatkowa)
                droga += predkosc_poczatkowa*TIME
                drogiTab.append(droga)

                energieKinetyczne.append(masa*pow(predkosc_poczatkowa, 2) / 2)
                energiePotencjalne.append(masa * PRZYSPIESZENIE_ZIEMSKIE * sin(radians(kat_nachylenia)) * droga)

                file.write(f"{round(timer, 2)}, {round(droga, 2)}, {round(predkosc_poczatkowa,2)}\n")

                # Sprawdza czy zaraz dojedziemy do końca równi lub czy już nie dojechaliśmy
                if(czyDojechalDoKonca == False and (dlugosc_rowni < droga + (predkosc_poczatkowa - abs(przyspieszenie)*TIME))):
                    czyDojechalDoKonca = True
                    pozostala_droga = dlugosc_rowni - droga
                    pozostaly_czas = pozostala_droga / predkosc_poczatkowa
                    predkosc_koncowa = (predkosc_poczatkowa - abs(przyspieszenie) * pozostaly_czas)
                    czasPrzejazduRowni = timer + pozostaly_czas
    
        # for i in range(len(drogiTab)):
        #     print(f"Ek = {energieKinetyczne[i]:.2f}, Ep = {energiePotencjalne[i]:.2f}, Suma = {energieKinetyczne[i] + energiePotencjalne[i]:.2f}")

        if(czyDojechalDoKonca):
            czas_przejazduW = f"Czas przejazdu równi: {round(czasPrzejazduRowni, 2)} s"
            predkosc_koncowaW = f"Prędkość na końcu równi: {round(predkosc_koncowa, 2)} m/s"
            
            self.czas_przejazduWynik.setText(czas_przejazduW)
            self.predkosc_koncowaWynik.setText(predkosc_koncowaW)

            self.predkosc_koncowaWynik.show()
            self.czas_przejazduWynik.show()
        else:
            innyW = f"Obiekt nie dojechał do końca równi"

            self.innyWynik.setText(innyW)
            self.innyWynik.show()

        # wypisanie danych
        przyspieszenieWynik = f"Przyspieszenie: {round(przyspieszenie, 2)} m/s²"
        silaWynik = f"Siła: {round(sila, 2)} N"
        czasWynik = f"Czas: {round(timer,2)} s"
        przebyta_drogaWynik = f"Przebyta droga: {round(droga,2)} m"
        maksymalna_wysokoscWynik = f"Maksymalna wysokość: {round(DF.maksymalna_wysokoscWynik(kat_nachylenia=kat_nachylenia, droga=droga),2)} m"

        # wpisanie wyników do zmiennych
        wspolczynnik_tarciaD = f"Współczynnik tarcia: {round(wspolczynnik_tarcia,2)}"
        predkosc_poczatkowaD = f"Prędkość początkowa: {round(pierwsza_predkosc_poczatkowa, 2)} m/s"
        kat_nachyleniaD = f"Kąt nachylenia: {round(kat_nachylenia,2)} °"
        masaD = f"Masa: {round(masa,2)} kg"
        dlugosc_rowniD = f"Długość równi: {round(dlugosc_rowni,2)} m"

        # wypisanie danych 
        self.predkosc_poczatkowaDane.setText(predkosc_poczatkowaD)
        self.dlugosc_rowniDane.setText(dlugosc_rowniD)
        self.wspolczynnik_tarciaDane.setText(wspolczynnik_tarciaD)
        self.kat_nachyleniaDane.setText(kat_nachyleniaD)
        self.masaDane.setText(masaD)

        # wypisanie wyników
        self.przyspieszenieWynik.setText(przyspieszenieWynik)
        self.czasWynik.setText(czasWynik)
        self.drogaWynik.setText(przebyta_drogaWynik)
        self.maksymalna_wysokoscWynik.setText(maksymalna_wysokoscWynik)
        self.silaWynik.setText(silaWynik)



        self.showF()

        self.czasyTab = czasyTab
        self.drogiTab = drogiTab
        self.timer = timer
        self.droga = droga
        self.energieKinetyczne = energieKinetyczne
        self.energiePotencjalne = energiePotencjalne
        self.predkosciTab = predkosciTab