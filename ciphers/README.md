# Caesar Cipher
The Caesar Cipher is a simple encryption algorithm that is based on shifting the letters of the alphabet by a fixed amount, known as the key. It is named after Julius Caesar, who is said to have used this encryption technique to send secret messages to his army commanders.

The Caesar Cipher works by replacing each letter in the plaintext with a letter k positions down the alphabet, where k is the key. For example, if the key is 3, then the letter 'A' would be replaced by the letter 'D', 'B' by 'E', 'C' by 'F', and so on. When we reach the end of the alphabet, we wrap around to the beginning. So, 'X' would be replaced by 'A', 'Y' by 'B', 'Z' by 'C', and so on.

To encrypt a message using the Caesar Cipher, we first choose a key, which is typically a number between 1 and 25. Then, we take the plaintext message and shift each letter in the message by k positions down the alphabet. The resulting message is the ciphertext.

To decrypt a message that has been encrypted using the Caesar Cipher, we simply shift each letter in the ciphertext backwards by k positions to recover the original plaintext message.

The Caesar Cipher is a very weak encryption algorithm and is easily broken by modern cryptographic techniques. However, it is still used today as a basic example of encryption and decryption.

# Substitution Cipher
The Substitution Cipher is a type of encryption algorithm that replaces each letter in the plaintext message with a different letter, according to a predetermined substitution key. The substitution key is a mapping of each letter of the alphabet to another letter, such that no two letters map to the same letter.

The time complexity of the substitution cipher algorithm depends on the length of the message and the size of the key space. Generally, the algorithm has a time complexity of O(n), where n is the length of the message. However, the time complexity can increase if the key space is large, as the algorithm would need to perform more substitution operations. Overall, the time complexity of the substitution cipher algorithm is considered to be relatively low.