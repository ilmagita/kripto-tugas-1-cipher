## VIIGENERE CYPHER

from functionList import letter_to_integer as lti
from functionList import integer_to_letter as itl
from functionList import clean_letter
from math import gcd

## HELPER FUNCTIONS
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    
def modulo_inverse(a, m=26):
    g, x, a = extended_gcd(a, m)
    if (g != 1):
        return f'Modular inverse does not exist.'
    else:
        return x % m

## ENCRYPTION FUNCTIONS
def affine_encryption(plaintext, m, b):

    if type(m) != int:
        m = int(m)
    if type(b) != int:
        b = int(b)

    # check if m and 26 (alphabet size) are coprimes
    if gcd(m, 26) != 1:
        return f'The m = {m} key is not coprimes with the number 26.'

    plaintext = clean_letter(plaintext)
    plaintext = plaintext.upper()

    plaintext_idx = [0 for i in range(len(plaintext))]
    ciphertext_idx = [0 for i in range(len(plaintext))]
    ciphertext = ['a' for i in range(len(plaintext))]

    for i in range(len(plaintext)):
        plaintext_idx[i] = lti(plaintext[i])
        ciphertext_idx[i] = (m * plaintext_idx[i] + b) % 26
        ciphertext[i] = itl(ciphertext_idx[i])

    ciphertext_str = ''.join(ciphertext)

    return ciphertext_str

## DECRYPTION FUNCTIONS
def affine_decryption(ciphertext, m, b):
    
    if type(m) != int:
        m = int(m)
    if type(b) != int:
        b = int(b)

    # check if m and 26 (alphabet size) are coprimes
    if gcd(m, 26) != 1:
        return f'The m = {m} key is not coprimes with the number 26.'
    
    ciphertext = clean_letter(ciphertext)
    ciphertext = ciphertext.upper()
    
    # solve inverse modulo
    a = modulo_inverse(m)

    plaintext_idx = [0 for i in range(len(ciphertext))]
    ciphertext_idx = [0 for i in range(len(ciphertext))]
    plaintext = ['a' for i in range(len(ciphertext))]

    for i in range(len(ciphertext)):
        ciphertext_idx[i] = lti(ciphertext[i])
        plaintext_idx[i] = (a * (ciphertext_idx[i] - b)) % 26
        plaintext[i] = itl(plaintext_idx[i])

    plaintext_str = ''.join(plaintext)

    return plaintext_str

print(affine_encryption('kripto', 7, 10))
print(affine_decryption('czolne', 7, 10))


