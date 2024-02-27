import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtCore import QProcess
import subprocess

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('windows/main.ui', self)

        # Connect the buttons to their respective functions
        self.vigenere_app_button.clicked.connect(self.open_vigenere)
        self.extended_vigenere_app_button.clicked.connect(self.open_extended_vigenere)
        self.playfair_app_button.clicked.connect(self.open_playfair)
        self.product_app_button.clicked.connect(self.open_product)
        self.affine_app_button.clicked.connect(self.open_affine)
        self.autokey_vigenere_app_button.clicked.connect(self.open_autokey_vigenere)

    def open_vigenere(self):
        self.open_app('vigenere_app.py')

    def open_extended_vigenere(self):
        self.open_app('extended_vigenere_app.py')

    def open_playfair(self):
        self.open_app('playfair_app.py')

    def open_product(self):
        self.open_app('product_app.py')

    def open_affine(self):
        self.open_app('affine_app.py')

    def open_extended_vigenere(self):
        self.open_app('extended_vigenere_app.py')

    def open_autokey_vigenere(self):
        self.open_app('autoKey_vigenere_app.py')

    def open_app(self, script_name):
        command = f"py {script_name}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())