# vigenere cypher

plaintext = input('Masukkan plaintext: ')
input_key = input('Masukkan key: ')

if len(input_key) < len(plaintext):
    key = ''
    j = 0
    while len(key) < len(plaintext):
        key = key + input_key[j]
        print(key)

        if j == len(input_key) - 1:
            j = 0
        else:
            j += 1
else:
    key = input_key

print(plaintext)
print(key)
        
