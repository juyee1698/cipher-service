def caesar_encode(plain_text:str, shift:int):
    cipher_text = ""
    for c in plain_text:
        num = ord(c) + int(shift)
        c_encoded = chr(num)
        cipher_text+= c_encoded
    return cipher_text

