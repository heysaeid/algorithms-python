"""
Transposition Cipher
Time complexity: O(n)
"""

def transposition_cipher_encrypt(plain_text, key):
    n = len(key)
    m = len(plain_text)
    num_blocks = m // n if m % n == 0 else m // n + 1

    plain_text += "X" * (num_blocks * n - m)

    blocks = [plain_text[i:i+n] for i in range(0, num_blocks * n, n)]

    permuted_blocks = ["" for _ in range(num_blocks)]
    for i, k in enumerate(key):
        permuted_blocks[k-1] = blocks[i]
    cipher_text = "".join(permuted_blocks)

    return cipher_text

def transposition_cipher_decrypt(cipher_text, key):
    n = len(key)
    m = len(cipher_text)
    num_blocks = m // n if m % n == 0 else m // n + 1

    blocks = [cipher_text[i:i+num_blocks] for i in range(0, m, num_blocks)]

    permuted_blocks = ["" for _ in range(n)]
    for i, k in enumerate(key):
        permuted_blocks[i] = blocks[k-1]
    plain_text = "".join(["".join(x) for x in zip(*permuted_blocks)])

    plain_text = plain_text.rstrip("X")

    return plain_text
