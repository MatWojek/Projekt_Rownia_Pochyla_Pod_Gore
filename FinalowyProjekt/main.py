import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import GUI
import sys

from wykres import Wykres

os.system('cls')

# Otworzenie okna aplikacji
aplikacja = QApplication(sys.argv)
aplikacja.setStyleSheet(open('style.qss').read())
okno = GUI()
wykres = Wykres()
okno.show()
sys.exit(aplikacja.exec_())