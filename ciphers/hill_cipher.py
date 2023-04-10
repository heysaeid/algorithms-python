"""
Hill Cipher
"""
import numpy as np


def hill_cipher_encrypt(message, key):
    message = message.upper()
    
    message = message.replace(" ", "")
    
    n = int(np.sqrt(len(key)))
    
    if len(message) % n != 0:
        message += "X" * (n - (len(message) % n))
    
    ciphertext = ""
    
    for i in range(0, len(message), n):
        block = [ord(c) - ord("A") for c in message[i:i+n]]
        block = np.array(block).reshape(n, 1)
        
        enc_block = np.dot(key, block) % 26
        
        enc_block = [chr(c + ord("A")) for c in enc_block.flatten()]
        ciphertext += "".join(enc_block)
    
    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
    n = int(np.sqrt(len(key)))
    
    inv_key = np.linalg.inv(key)
    det = int(round(np.linalg.det(key)))
    inv_det = pow(det, -1, 26)
    inv_key = np.round(inv_key * det * inv_det) % 26
    
    plaintext = ""
    
    for i in range(0, len(ciphertext), n):
        block = [ord(c) - ord("A") for c in ciphertext[i:i+n]]
        block = np.array(block).reshape(n, 1)
        
        dec_block = np.dot(inv_key, block) % 26
        
        dec_block = [chr(c + ord("A")) for c in dec_block.flatten()]
        plaintext += "".join(dec_block)
    
    return plaintext

key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

plaintext = "Hey Saeid"

ciphertext = hill_cipher_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = hill_cipher_decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)