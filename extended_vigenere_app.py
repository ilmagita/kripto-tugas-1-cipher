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
        self.save_button_enc.clicked.connect(self.on_save_button_enc_clicked)
        self.save_button_dec.clicked.connect(self.on_save_button_dec_clicked)
        

    def on_input_type_combobox_plaintext_selected(self, index):
        if index == 0:
            self.browse_button.show()
            self.file_name_box.show()
            self.label_5.show()
            
            self.input_box.setPlainText("")
            self.input_box.hide()
            self.label.hide()
            

            
        else:
            self.browse_button.hide()
            self.file_name_box.hide()
            self.label_5.hide()
            
            self.input_box.show()
            self.label.show()

            

    def on_browse_button_clicked(self):
        # Open file dialog
        file_dialog = QFileDialog(self)
        filename, _ = file_dialog.getOpenFileName(self, "Open File")

        if filename:
            # Read the file content
            with open(filename, 'rb') as file:
                contents = file.read().decode('latin-1')

            # Set the content to the text box
            

            # Set the text box to file name
            self.file_name_box.setText(filename)
            self.input_box.setPlainText("")
           
            

            # Close file dialog
            file_dialog.reject()
            file.close()


    def on_encrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()
        
        
        if input_text == "":
            filepath = self.file_name_box.text()
            filename_full = os.path.basename(filepath)
            filename_ori = filename_full[:-4]
            filename_type = filename_full[-4:]
            with open(filepath, 'rb') as file:
                contents = file.read().decode('latin-1')
                
            output = encrypt_extended_vigenere(contents, input_key)
            result = "".join(output)
            #save = save_file(result, f'output/{filename_ori}_encrypted{filename_type}')
              
        else:
            output = encrypt_extended_vigenere(input_text, input_key)
            result = "".join(output)
            
        
        self.output_box.setPlainText(result)
        

    def on_decrypt_button_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()
        
        
        if input_text == "":
            filepath = self.file_name_box.text()
            filename_full = os.path.basename(filepath)
            filename_ori = filename_full[:-4]
            filename_type = filename_full[-4:]
            
            with open(filepath, 'rb') as file:
                contents = file.read().decode('latin-1')
                
            output = decrypt_extended_vigenere(contents, input_key)
            result = "".join(output)
            #save = save_file(result, f'output/{filename_ori}_decrypted{filename_type}')
            
        else:
            output = decrypt_extended_vigenere(input_text, input_key)
            result = "".join(output)
            
        
        self.output_box.setPlainText(result)
       

    def on_save_button_enc_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()
        
        
        if input_text == "":
            filepath = self.file_name_box.text()
            filename_full = os.path.basename(filepath)
            filename_ori = filename_full[:-4]
            filename_type = filename_full[-4:]
            with open(filepath, 'rb') as file:
                contents = file.read().decode('latin-1')
                
            output = encrypt_extended_vigenere(contents, input_key)
            result = "".join(output)
            save = save_file(result, f'output/{filename_ori}_encrypted{filename_type}')
              
        else:
            output = encrypt_extended_vigenere(input_text, input_key)
            result = "".join(output)
            save = save_file(result, 'output/encryption.txt')
            
            

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Encryption Saved as File')
        if input_text == "":
            msg_box.setText(f'File saved as {filename_ori}_encrypted{filename_type}in output folder.')
        else:
            msg_box.setText(f'encryption.txt')
            
        msg_box.exec_()
        
    def on_save_button_dec_clicked(self):
        input_text = self.input_box.toPlainText()
        input_key = self.key_box.toPlainText()
        
        
        if input_text == "":
            filepath = self.file_name_box.text()
            filename_full = os.path.basename(filepath)
            filename_ori = filename_full[:-4]
            filename_type = filename_full[-4:]
            with open(filepath, 'rb') as file:
                contents = file.read().decode('latin-1')
                
            output = decrypt_extended_vigenere(contents, input_key)
            result = "".join(output)
            save = save_file(result, f'output/{filename_ori}_decrypted{filename_type}')
              
        else:
            output = decrypt_extended_vigenere(input_text, input_key)
            result = "".join(output)
            save = save_file(result, 'output/decryption.txt')
            
            

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Decryption Saved as File')
        if input_text == "":
            msg_box.setText(f'File saved as {filename_ori}_decrypted{filename_type}in output folder.')
        else:
            msg_box.setText(f'decryption.txt')
            
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