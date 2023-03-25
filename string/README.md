# Brute force
String matching algorithms are used to find patterns within text data. One of the most basic algorithms for string matching is the brute-force algorithm.

The brute-force algorithm checks every possible starting position in the text and compares the substring at that position with the pattern. If the substring matches the pattern, then the algorithm returns the starting position. Otherwise, it moves to the next starting position and tries again. This process continues until a match is found or until every starting position has been checked.

This implementation has a time complexity of O(nm), where n is the length of the text and m is the length of the pattern. For large inputs, this can be very slow. However, it's a good starting point for understanding how string matching algorithms work.

# Naive String Matching Algorithm
The Naive String Matching Algorithm is a simple algorithm for finding occurrences of a pattern string within a larger text string. The algorithm compares the pattern string to each possible substring of the text string, starting at the leftmost position and moving to the right until it either finds a match or reaches the end of the text string.

The time complexity of the Naive String Matching Algorithm is O(n*m), where n is the length of the text string and m is the length of the pattern string. In the worst case, this can be quite slow for large strings or patterns. However, it has the advantage of being simple and easy to implement, making it a good choice for small strings or as a teaching tool for introductory computer science courses.

# Boyer-Moore
The Boyer-Moore Algorithm is a powerful string matching algorithm that is more efficient than the Naive String Matching Algorithm for large patterns. The algorithm is based on two main ideas: the "bad character rule" and the "good suffix rule".

The bad character rule involves looking at the character in the text that doesn't match the corresponding character in the pattern, and using a precomputed table to determine how many positions we can shift the pattern to the right without missing a possible match.

The good suffix rule involves using a precomputed table to determine how many positions we can shift the pattern to the right if we have already matched a suffix of the pattern, but the corresponding prefix doesn't match the text.

The worst-case time complexity of the Boyer-Moore Algorithm is O(nm), where n is the length of the text and m is the length of the pattern. However, in practice, the algorithm is much faster than the naive algorithm and often outperforms other string matching algorithms. The best-case time complexity of the algorithm is O(n/m), which occurs when the pattern occurs at the beginning of the text. The average case time complexity of the algorithm is also sublinear, making it a very efficient algorithm for large patterns.