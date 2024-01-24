import os
from PyQt5.QtWidgets import QApplication
from ui import GUI
import sys

os.system('cls')

# Otworzenie okna aplikacji
aplikacja = QApplication(sys.argv)
okno = GUI()
okno.show()
sys.exit(aplikacja.exec_())