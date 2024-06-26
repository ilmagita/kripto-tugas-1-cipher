from .functionList import *

def encrypt_vigenere(plainText,inputKey):
    key = ""
    cipherText = ""
    plainText = clean_letter(plainText)
    inputKey = clean_letter(inputKey)
    plainText = plainText.upper()
    inputKey = inputKey.upper()
    
    for i, char in enumerate(plainText): 
        key += inputKey[i % len(inputKey)]
        
        cipher = (letter_to_integer(char) + letter_to_integer(key[i])) % 26
        cipherText += integer_to_letter(cipher)
        
    return(cipherText)

def decrypt_vigenere(cipherText,inputKey):
    key = ""
    plainText = ""
    inputKey = clean_letter(inputKey)
    cipherText = clean_letter(cipherText)
    cipherText = cipherText.upper()
    inputKey = inputKey.upper()
    
    for i, char in enumerate(cipherText):
        key += inputKey[i % len(inputKey)]
        
        cipher = (letter_to_integer(char) - letter_to_integer(key[i])) % 26
        plainText += integer_to_letter(cipher)
        
    return(plainText)

def encrypt_transposition(plainText,columnKey):
    matrix = []
    cipherText = ""
    plainText = clean_letter(plainText)
    plainText = plainText.upper()

    
    for i in range(0, len(plainText), columnKey):
        substr = plainText[i:i+columnKey]
        if len(substr) < columnKey:
            substr += 'Z' * (columnKey - len(substr))
        matrix.append(substr)
    

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            cipherText += matrix[j][i]
            
    return cipherText

def decrypt_transposition(cipherText,columnKey):
    matrix = []
    plainText = ""
    cipherText = clean_letter(cipherText)
    cipherText = cipherText.upper()

    
    decryptKey = len(cipherText)//columnKey
    
    for i in range(0, len(cipherText), decryptKey):
        substr = cipherText[i:i+decryptKey]
        matrix.append(substr)
    

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            plainText += matrix[j][i]
            
    return plainText
    

def encrypt_product(plainText, vignereKey, tranposisitonKey):
    cipherText = encrypt_transposition(encrypt_vigenere(plainText,vignereKey),tranposisitonKey)
    return cipherText

def decrypt_product(cipherText, vignereKey, tranposisitonKey):
    plainText = decrypt_vigenere(decrypt_transposition(cipherText,tranposisitonKey),vignereKey)
    return plainText


"""
plainText = "hello world"
inputKey = "sony"
columnKey = 4

a = encrypt_vigenere(plainText,inputKey)
c = encrypt_transposition(a,columnKey)
d = decrypt_transposition(c,columnKey)
b = decrypt_vigenere(d,inputKey)

print(a)
print(c)
print(b)

print("==============================")
e = encrypt_product(plainText,inputKey,columnKey)
f = decrypt_product(e,inputKey,columnKey)

print(e)
print(f)
"""


