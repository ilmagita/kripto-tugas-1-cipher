def encrypt_extended_vigenere(plainText,inputKey):
    key = ""
    cipherText = ""
    
    for i, char in enumerate(plainText):
        key += inputKey[i % len(inputKey)]
        
        cipher = (ord(char) + ord(key[i])) % 256
        cipherText += chr(cipher)
        
    return(cipherText)

def decrypt_extended_vigenere(cipherText,inputKey):
    key = ""
    plainText = ""
    
    for i, char in enumerate(cipherText):
        key += inputKey[i % len(inputKey)]
        
        cipher = (ord(char) - ord(key[i])) % 256
        plainText += chr(cipher)
        
    return(plainText)


    