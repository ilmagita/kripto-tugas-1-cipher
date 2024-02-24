from functionList import *

def encrypt_autoKeyVignere(plainText,inputKey):
    plainText = clean_letter(plainText)
    plainText = plainText.upper()
    inputKey = inputKey.upper()
    
    key = inputKey
    cipherText = ""
    
    for i in range(len(plainText)-len(inputKey)):
        key += plainText[i]
        
    for i, char in enumerate(plainText):       
        cipher = (letter_to_integer(char) + letter_to_integer(key[i])) % 26
        cipherText += integer_to_letter(cipher)
        
    return(cipherText)

def decrypt_autoKeyVigenere(cipherText, inputKey):
    cipherText = clean_letter(cipherText)
    cipherText = cipherText.upper()
    inputKey = inputKey.upper()

    key = inputKey
    plainText = ""
    
    for i, char in enumerate(cipherText):   
        cipher = (letter_to_integer(char) - letter_to_integer(key[i])) % 26
        plainText += integer_to_letter(cipher)
        
        if(len(key) < len(cipherText)):
            key += integer_to_letter(cipher)
            
    return(plainText)
    
    

plainText = 'negara penghasil minyak mentah di dunia'
key = 'INDO'

a = encrypt_autoKeyVignere(plainText,key)
b = decrypt_autoKeyVigenere(a,key)
print(a)    
print(b)

