## VIIGENERE CYPHER

from functionList import letter_to_integer as lti
from functionList import integer_to_letter as itl
from functionList import clean_letter

## ENCRYPTION FUNCTIONS
def vignere_key(input_key, plaintext):
    if len(input_key) < len(plaintext):
        key = ''
        j = 0
        while len(key) < len(plaintext):
            key = key + input_key[j].upper()

            if j == len(input_key) - 1:
                j = 0
            else:
                j += 1
    else:
        key = input_key.upper()

    return key

def vignere_encryption(plaintext='thisplaintext', input_key='sony'):
    plaintext = clean_letter(plaintext)
    plaintext = plaintext.upper()

    key = vignere_key(input_key, plaintext)

    plaintext_idx = [0 for i in range(len(plaintext))]
    key_idx = [0 for i in range(len(plaintext))]
    ciphertext_idx = [0 for i in range (len(plaintext))]
    ciphertext = ['a' for i in range(len(plaintext))]

    for i in range(len(plaintext)):
        plaintext_idx[i] = lti(plaintext[i])
        key_idx[i] = lti(key[i])

        ciphertext_idx[i] = (plaintext_idx[i] + key_idx[i]) % 26
        ciphertext[i] = itl(ciphertext_idx[i])

    ciphertext = ''.join(ciphertext)

    return ciphertext

## DECRYPTION FUNCTION
def vignere_decryption(ciphertext='lvvqhzngfhrvl', input_key='sony'):
    ciphertext = clean_letter(ciphertext)
    ciphertext = ciphertext.upper()

    key = vignere_key(input_key, ciphertext)

    ciphertext_idx = [0 for i in range(len(ciphertext))]
    key_idx = [0 for i in range(len(ciphertext))]
    plaintext_idx = [0 for i in range (len(ciphertext))]
    plaintext = ['a' for i in range(len(ciphertext))]

    for i in range(len(ciphertext)):
        ciphertext_idx[i] = lti(ciphertext[i])
        key_idx[i] = lti(key[i])

        plaintext_idx[i] = (ciphertext_idx[i] - key_idx[i]) % 26
        plaintext[i] = itl(plaintext_idx[i])

    plaintext = ''.join(plaintext)

    return plaintext

## MAIN PROGRAM
print(vignere_encryption())
print(vignere_decryption())
