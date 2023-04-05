"""
Caesar Cipher
Time complexity: O(n)
ex 1) substitution_cipher("Hey Saeid", "XYZABCDEFGHIJKLMNOPQRSTUVQ") => Ebv Pxbfa
"""
import string


def substitution_cipher(text, substitution_key):
    result = ""
    alphabet = string.ascii_uppercase
    
    for char in text:

        if char.isalpha():
            index = alphabet.index(char.upper())
            if char.isupper():
                result += substitution_key[index].upper()
            else:
                result += substitution_key[index].lower()
        else:
            result += char
    
    return result