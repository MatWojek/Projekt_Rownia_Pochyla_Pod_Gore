# stworzenie GUI
# wyświetlenie wyników poniżej, na początku będą ukryte
# podstawienie do wzoru wykonywane na oczach użytkownika, wzory też będą wypisane w gui (jeszcze nie wiem jak)4
# pokazuje dane przy wyniku na końcu 
# guzik random, wpisujący randomowe wartości do potrzebnych pól wejścia
# menu do interfejsu gdzie sobie można wybrać co chcesz obliczyć 

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt

from dzialania_fizyczne import DzialaniaFizyczne as DF

class GUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs() 
        
    def interfejs(self):
        
        pole1 = QLabel("Współczynnik tarcia: ", self)
        pole2 = QLabel("Prędkość początkowa: ", self)
        pole3 = QLabel("Kąt nachylenia:", self)
        pole4 = QLabel("Podaj masę przedmiotu:", self)
        
        pole5 =  QLabel("m/s", self)
        pole6 = QLabel("°", self)
        pole7 = QLabel("kg", self)
        
        self.przyspieszenieWynik = QLabel("Przyspieszenie: ", self)
        self.drogaWynik = QLabel("Przebyta droga: ", self)
        self.czasWynik = QLabel("Czas: ", self)
        self.maksymalna_wysokoscWynik = QLabel("Maksymalna wysokość: ", self)

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
        self.przyspieszenieWynik.hide()
        self.drogaWynik.hide()
        self.czasWynik.hide()
        self.maksymalna_wysokoscWynik.hide()

        uklad = QGridLayout()
        uklad.addWidget(pole1, 1, 0)
        uklad.addWidget(pole2, 2, 0)
        uklad.addWidget(pole3, 3, 0)
        uklad.addWidget(pole4, 4, 0)
        
        uklad.addWidget(pole5, 2, 3)
        uklad.addWidget(pole6, 3, 3)
        uklad.addWidget(pole7, 4, 3)

        uklad.addWidget(self.przyspieszenieWynik, 6, 0)
        uklad.addWidget(self.drogaWynik, 7, 0)
        uklad.addWidget(self.czasWynik, 8, 0)
        uklad.addWidget(self.maksymalna_wysokoscWynik, 9, 0)

        self.predkosc_poczatkowaW = QLineEdit()
        self.kat_nachyleniaW = QLineEdit()
        self.masaW = QLineEdit()
        oblicz = QPushButton("&Oblicz", self)
        
        uklad.addWidget(self.radio1, 1, 1)
        uklad.addWidget(self.radio2, 1, 2)
        uklad.addWidget(self.predkosc_poczatkowaW, 2, 1)
        uklad.addWidget(self.kat_nachyleniaW, 3, 1)
        uklad.addWidget(self.masaW, 4, 1)
        uklad.addWidget(oblicz, 5, 0, 1, 3)
       
        self.setLayout(uklad)

        oblicz.clicked.connect(self.obliczanie)

        self.setGeometry(700, 200, 500, 500)
        self.setWindowIcon(QIcon('logo.jpg'))
        self.resize(500, 500)
        self.setMinimumWidth(500)
        self.setMaximumWidth(1000)
        self.setWindowTitle("Równia pochyła w pod górę")
        self.show()
        
    def sprawdzCzyZaznaczone(self):
        sprawdzam = self.grupa_radio.checkedButton()
        if sprawdzam:
            return sprawdzam.value
        else:
            QMessageBox.warning(self, 'Ostrzeżenie', 'Nie zaznaczono żadnej opcji')

    def obliczanie(self):

        przyspieszenieWynik = ""
        czasWynik = ""
        drogaWynik = ""
        maksymalna_wysokoscWynik = ""

        try:
            wspolczynnik_tarcia = float(self.sprawdzCzyZaznaczone())
            kat_nachylenia = float(self.kat_nachyleniaW.text())
            masa = float(self.masaW.text())
            predkosc_poczatkowa = float(self.predkosc_poczatkowaW.text())

            przyspieszenieW = DF.przyspieszenieF(wspolczynnik_tarcia=wspolczynnik_tarcia, kat_nachylenia=kat_nachylenia)
            przyspieszenieWynik = f"Przyspieszenie: {przyspieszenieW}"
            czasW = DF.czasF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
            czasWynik = f"Czas: {czasW}"
            drogaW = DF.drogaF(predkosc_poczatkowa=predkosc_poczatkowa, czas=czasW, przyspieszenie=przyspieszenieW, wspolczynnik_tarcia=wspolczynnik_tarcia)
            drogaWynik = f"Przebyta droga: {drogaW}"
            maksymalna_wysokoscW = DF.maksymalna_wysokoscF(predkosc_poczatkowa=predkosc_poczatkowa, kat_nachylenia=kat_nachylenia, wspolczynnik_tarcia=wspolczynnik_tarcia)
            maksymalna_wysokoscWynik = f"Maksymalna wysokość: {maksymalna_wysokoscW}"
        
            self.przyspieszenieWynik.setText(przyspieszenieWynik)
            self.czasWynik.setText(czasWynik)
            self.drogaWynik.setText(drogaWynik)
            self.maksymalna_wysokoscWynik.setText(maksymalna_wysokoscWynik)

            self.przyspieszenieWynik.show()
            self.czasWynik.show()
            self.drogaWynik.show()
            self.maksymalna_wysokoscWynik.show()

        except ValueError:
            self.result_label.setText("Wprowadź prawidłowe liczby!")

if __name__ == '__main__':
    import sys

    aplikacja = QApplication(sys.argv)
    aplikacja.setStyleSheet(open('style.qss').read())
    okno = GUI()
    sys.exit(aplikacja.exec_())