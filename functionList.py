def letter_to_integer(letter):
    return ord(letter) - ord('A')

def integer_to_letter(integer):
    return chr(integer + 65)

def clean_letter(str):
    result = ""
    for char in str:
        if char != " ":
            if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
                result += char
    return result

def read_binary_file(file):
    f = open(file,'rb')
    content = f.read().decode('latin-1')
    return content

def read_text_file(file):
    f = open(file,'r')
    content = f.read()
    return content

def save_file(cipherText, fileName):
    with open(fileName, 'wb') as f:
        f.write(cipherText.encode('latin-1'))
        

