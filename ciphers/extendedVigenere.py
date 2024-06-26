from .functionList import *

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


#p = read_binary_file('./foto.png')
# a = read_binary_file('foto.png')
#a = encrypt_extended_vigenere(p,'sony')
#b = decrypt_extended_vigenere(a,'sony')

#print(p)

# print(a)
# print(b)
# print(p)

#if (p==b):
    #print("UDah bener")
#else:
    #print("Belum")

#save_file(a,'encrypted_foto.png')
#save_file(b,'decrypted_foto.png')


