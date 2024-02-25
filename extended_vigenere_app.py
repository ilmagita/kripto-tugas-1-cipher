## EXTENDED VIGENRE APP GUI

## IMPORTS
import os
import sys
from PyQt5.QtWidgets import (
     QApplication, QMainWindow, QPushButton, QPlainTextEdit, QFileDialog, QMessageBox
)
from PyQt5.uic import loadUi

from ciphers.extendedVigenere import *
from ciphers.functionList import (save_file)

## MAIN GUI PROGRAMS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('windows/extended_vigenere_window.ui', self)

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
        filename, _ = file_dialog.getOpenFileName(self, "Open File")

        if filename:
            # Read the file content
            with open(filename, 'rb') as file:
                contents = file.read().decode('latin-1')

            # Set the content to the text box
            self.input_box.setPlainText(contents)

            # Set the text box to file name
            self.file_name_box.setText(os.path.basename(filename))

            # Close file dialog
            file_dialog.reject()
            file.close()


    def on_encrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()

        output = encrypt_extended_vigenere(input_text, input_key)
        self.output_box.setPlainText(output)

    def on_decrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()

        output = decrypt_extended_vigenere(input_text, input_key)
        self.output_box.setPlainText(output)

    def on_save_button_clicked(self):
        filename_full = self.file_name_box.text()
        filename_ori = filename_full[:-4]
        filename_type = filename_full[-4:]

        output_text = self.output_box.toPlainText()
        output = save_file(output_text, f'output/{filename_ori}_encrypted{filename_type}')

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Output Saved as File')
        msg_box.setText(f'File saved as {filename_ori}_encrypted{filename_type}in output folder.')
        msg_box.exec_()

## GUI PROGRAM
if __name__ == "__main__":
    import sys

    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of your MainWindow class
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
