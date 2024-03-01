def caesar_encode(plain_text:str, shift:int):
    cipher_text = ""
    for c in plain_text:
        num = (ord(c)-97) + int(shift)
        num = num % 26
        c_encoded = chr(num + 97)
        cipher_text+= c_encoded
    return cipher_text