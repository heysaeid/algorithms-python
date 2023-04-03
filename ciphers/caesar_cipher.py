"""
Caesar Cipher
Time complexity: O(n)
ex 1) caesar_cipher("HELLO WORLD", 3) => KHOOR ZRUOG
"""

def caesar_cipher(text, key):
    result = ""
    
    for char in text:

        if char.isalpha():
            ascii_value = ord(char)
            shifted_value = (ascii_value - 65 + key) % 26 + 65
            shifted_char = chr(shifted_value)
            result += shifted_char
        else:
            result += char
    
    return result