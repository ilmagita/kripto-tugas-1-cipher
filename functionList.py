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