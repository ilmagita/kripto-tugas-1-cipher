## PRODUCT APP GUI

## IMPORTS
import sys
from PyQt5.QtWidgets import (
     QApplication, QMainWindow, QPushButton, QPlainTextEdit, QFileDialog
)
from PyQt5.uic import loadUi

from ciphers.product import *
from ciphers.functionList import (save_file)

## MAIN GUI PROGRAMS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('windows/product_window.ui', self)

        # CONNECTION SLOTS
        self.input_type_combobox.currentIndexChanged.connect(self.on_input_type_combobox_plaintext_selected)
        self.browse_button.clicked.connect(self.on_browse_button_clicked)
        self.encrypt_button.clicked.connect(self.on_encrypt_button_clicked)
        self.decrypt_button.clicked.connect(self.on_decrypt_button_clicked)
        self.save_button.clicked.connect(self.on_save_button_clicked)

    def on_input_type_combobox_plaintext_selected(self, index):
        if index == 0:
            self.browse_button.show()
        else:
            self.browse_button.hide()

    def on_browse_button_clicked(self):
        # Open file dialog
        file_dialog = QFileDialog(self)
        filename, _ = file_dialog.getOpenFileName(self, "Open File", "", "Text files (*.txt)")

        if filename:
            # Read the file content
            with open(filename, 'r') as file:
                contents = file.read()

            # Set the content to the text box
            self.input_box.setPlainText(contents)

            # Close file dialog
            file_dialog.reject()
            file.close()

    def on_encrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key_vigenere = self.key_box_text.toPlainText()
        input_key_transpos = int(self.key_box_int.toPlainText())
        

        output = encrypt_product(input_text, input_key_vigenere, input_key_transpos)
        self.output_box.setPlainText(output)

    def on_decrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key_vigenere = self.key_box_text.toPlainText()
        input_key_transpos = int(self.key_box_int.toPlainText())

        output = decrypt_product(input_text,  input_key_vigenere, input_key_transpos)
        self.output_box.setPlainText(output)

    def on_save_button_clicked(self):
        output_text = self.output_box.toPlainText()
        output = save_file(output_text, 'output/output.txt')

## GUI PROGRAM
if __name__ == "__main__":
    import sys

    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of your MainWindow class
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
