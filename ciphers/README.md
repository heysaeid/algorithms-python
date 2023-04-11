# Caesar Cipher
The Caesar Cipher is a simple encryption algorithm that is based on shifting the letters of the alphabet by a fixed amount, known as the key. It is named after Julius Caesar, who is said to have used this encryption technique to send secret messages to his army commanders.

The Caesar Cipher works by replacing each letter in the plaintext with a letter k positions down the alphabet, where k is the key. For example, if the key is 3, then the letter 'A' would be replaced by the letter 'D', 'B' by 'E', 'C' by 'F', and so on. When we reach the end of the alphabet, we wrap around to the beginning. So, 'X' would be replaced by 'A', 'Y' by 'B', 'Z' by 'C', and so on.

To encrypt a message using the Caesar Cipher, we first choose a key, which is typically a number between 1 and 25. Then, we take the plaintext message and shift each letter in the message by k positions down the alphabet. The resulting message is the ciphertext.

To decrypt a message that has been encrypted using the Caesar Cipher, we simply shift each letter in the ciphertext backwards by k positions to recover the original plaintext message.

The Caesar Cipher is a very weak encryption algorithm and is easily broken by modern cryptographic techniques. However, it is still used today as a basic example of encryption and decryption.

The time complexity of the Caesar Cipher algorithm is O(n), where n is the length of the plaintext message. This is because the algorithm iterates over each character in the message exactly once, performing a constant number of operations (primarily arithmetic and string manipulation) on each character. Therefore, the overall time complexity is proportional to the length of the input message.

# Substitution Cipher
The Substitution Cipher is a type of encryption algorithm that replaces each letter in the plaintext message with a different letter, according to a predetermined substitution key. The substitution key is a mapping of each letter of the alphabet to another letter, such that no two letters map to the same letter.

The time complexity of the substitution cipher algorithm depends on the length of the message and the size of the key space. Generally, the algorithm has a time complexity of O(n), where n is the length of the message. However, the time complexity can increase if the key space is large, as the algorithm would need to perform more substitution operations. Overall, the time complexity of the substitution cipher algorithm is considered to be relatively low.

# Transposition Cipher
The transposition cipher is a type of encryption technique that rearranges the letters of a message to create a new, encrypted message. It works by using a specific key to rearrange the letters of the original message into a new order. The new order of the letters is then used to create the encrypted message.

The time complexity of the Transposition cipher algorithm is O(n), where n is the length of the plaintext or ciphertext. This is because both encryption and decryption involve iterating over each character in the input string exactly once.

# Hill Cipher
The Hill Cipher algorithm is a polygraphic substitution cipher based on linear algebra. It was invented by Lester S. Hill in 1929. In this cipher, a plaintext message is broken down into blocks of n letters and then encrypted using an n x n matrix. The resulting ciphertext blocks are then concatenated to form the final encrypted message.

The time complexity of the Hill Cipher algorithm depends on the size of the plaintext and the key matrix. In the provided Python example, the encryption and decryption functions operate on blocks of n letters, where n is the size of the key matrix (i.e., n x n). Therefore, the time complexity of both encryption and decryption functions is O(len(message) * n^3), where len(message) is the length of the plaintext and n is the size of the key matrix.
