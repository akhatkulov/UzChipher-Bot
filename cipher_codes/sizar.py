def caesar_cipher(ch, key):
    key = int(key)
    if not ch.isalpha():
        return ch

    offset = ord('A') if ch.isupper() else ord('a')
    return chr(((ord(ch) + key) - offset) % 26 + offset)


def caesar_encipher(input, key):
    try:
        key = int(key)
        output = ""
        for ch in input:
            output += caesar_cipher(ch, key)
        return output
    except:
        return "Error 1"


def caesar_decipher(input, key):
    try:
        key = int(key)
        return caesar_encipher(input, 26 - key)
    except:
        return "Error 1"




