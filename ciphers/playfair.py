## PLAYFAIR CYPHER

from .functionList import letter_to_integer as lti
from .functionList import integer_to_letter as itl
from math import ceil
from .functionList import clean_letter

## HELPER FUNCTIONS
def str_to_playfair_key(string, ch_to_remove='J'):
    """
    Function to arrange a string of a cipherkey to the Playfair square.
    """
    ch_to_remove = ch_to_remove.upper()

    string = clean_letter(string)
    string = string.upper()
    string = string.replace(ch_to_remove, '')

    # remove duplicate letters
    ch_list = []
    for i in range(len(string)):
        if string[i] not in ch_list:
            ch_list.append(string[i])

    alphabet = list('ABCDEFGHIKLMNOPQRSTUVWXYZ')

    for i in range(len(alphabet)):
        if alphabet[i] not in ch_list:
            ch_list.append(alphabet[i])

    playfair_key = [[ch_list[i * 5 + j] for j in range(5)] for i in range(5)]
    return playfair_key

def str_to_playfair_bigram_list(string, substitute_ch='X', ch_to_remove='J', replacement_ch='I'):
    """
    Function to arrange plaintext to an array of bigrams intended for Playfair cipher.
    """
    ch_to_remove = ch_to_remove.upper()

    string = clean_letter(string)
    string = string.upper()
    string = string.replace(ch_to_remove, replacement_ch)

    # handle repeating letters in a bigram - insert substitute character between
    bigram_check_list = [string[i:i+2] for i in range(0, len(string), 2)]
    for i in range(len(bigram_check_list)):
        if len(bigram_check_list[i]) > 1:
            if bigram_check_list[i][0] == bigram_check_list[i][1]:
                first_letter = bigram_check_list[i][0]
                second_letter = bigram_check_list[i][1]
                bigram_check_list[i] = first_letter + substitute_ch + second_letter
    
    new_string = ''.join(bigram_check_list)

    bigram_list = ['' for i in range(ceil(len(new_string) / 2))]
    i = 0
    j = 0

    while j <= len(new_string) - 1:
        k = j + 2

        bigram_list[i] = new_string[j:k]

        # add substitute_ch if string is odd-length
        if len(bigram_list[i]) == 1:
            bigram_list[i] += substitute_ch

        j = k
        i += 1

    return bigram_list

def find_el_in_matrix(matrix, el):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == el:
                return i, j
    return None

## ENCRYPTION FUNCTIONS
def playfair_encrypt_bigram(playfair_key, bigram):
    first_el_position = find_el_in_matrix(playfair_key, bigram[0])
    second_el_position = find_el_in_matrix(playfair_key, bigram[1])

    if first_el_position is not None and second_el_position is not None:
        first_el_row, first_el_col = first_el_position
        second_el_row, second_el_col = second_el_position

        cipher_bigram = ['', '']

        if (first_el_row == second_el_row):
            # if both elements in same row
            cipher_bigram[0] = playfair_key[first_el_row][(first_el_col + 1) % 5]
            cipher_bigram[1] = playfair_key[second_el_row][(second_el_col + 1) % 5]

        elif (first_el_col == second_el_col):
            # if both elements in same column
            cipher_bigram[0] = playfair_key[(first_el_row + 1) % 5][first_el_col]
            cipher_bigram[1] = playfair_key[(second_el_row + 1) % 5][second_el_col]

        else:
            cipher_bigram[0] = playfair_key[first_el_row][second_el_col]
            cipher_bigram[1] = playfair_key[second_el_row][first_el_col]

        cipher_bigram = ''.join(cipher_bigram)

        return cipher_bigram

def playfair_encryption(plaintext_input='temui ibu nanti malam', cipherkey_input='jalan ganesha sepuluh'):
    plaintext_bigram_list = str_to_playfair_bigram_list(plaintext_input)
    cipherkey_matrix = str_to_playfair_key(cipherkey_input)

    cipher_list = []

    for i in range(len(plaintext_bigram_list)):
        cipher_list.append(playfair_encrypt_bigram(cipherkey_matrix, plaintext_bigram_list[i]))

    ciphertext = ''.join(cipher_list)
    return ciphertext

## DECRYPTION FUNCTIONS
def playfair_decrypt_bigram(playfair_key, bigram):
    first_el_position = find_el_in_matrix(playfair_key, bigram[0])
    second_el_position = find_el_in_matrix(playfair_key, bigram[1])

    if first_el_position is not None and second_el_position is not None:
        first_el_row, first_el_col = first_el_position
        second_el_row, second_el_col = second_el_position

        cipher_bigram = ['', '']

        if (first_el_row == second_el_row):
            # if both elements in same row
            cipher_bigram[0] = playfair_key[first_el_row][(first_el_col - 1) % 5]
            cipher_bigram[1] = playfair_key[second_el_row][(second_el_col - 1) % 5]

        elif (first_el_col == second_el_col):
            # if both elements in same column
            cipher_bigram[0] = playfair_key[(first_el_row - 1) % 5][first_el_col]
            cipher_bigram[1] = playfair_key[(second_el_row - 1) % 5][second_el_col]

        else:
            cipher_bigram[0] = playfair_key[first_el_row][second_el_col]
            cipher_bigram[1] = playfair_key[second_el_row][first_el_col]

        cipher_bigram = ''.join(cipher_bigram)

        return cipher_bigram
    
def playfair_decryption(plaintext_input='ZBRSFYKUPGLGRKVSNLQV', cipherkey_input='jalan ganesha sepuluh'):
    plaintext_bigram_list = str_to_playfair_bigram_list(plaintext_input)
    cipherkey_matrix = str_to_playfair_key(cipherkey_input)

    cipher_list = []

    for i in range(len(plaintext_bigram_list)):
        cipher_list.append(playfair_decrypt_bigram(cipherkey_matrix, plaintext_bigram_list[i]))

    ciphertext = ''.join(cipher_list)
    return ciphertext

## MAIN PROGRAM
print(playfair_encryption())
print(playfair_decryption())