# Brute force
String matching algorithms are used to find patterns within text data. One of the most basic algorithms for string matching is the brute-force algorithm.

The brute-force algorithm checks every possible starting position in the text and compares the substring at that position with the pattern. If the substring matches the pattern, then the algorithm returns the starting position. Otherwise, it moves to the next starting position and tries again. This process continues until a match is found or until every starting position has been checked.

This implementation has a time complexity of O(nm), where n is the length of the text and m is the length of the pattern. For large inputs, this can be very slow. However, it's a good starting point for understanding how string matching algorithms work.

# Naive String Matching Algorithm
The Naive String Matching Algorithm is a simple algorithm for finding occurrences of a pattern string within a larger text string. The algorithm compares the pattern string to each possible substring of the text string, starting at the leftmost position and moving to the right until it either finds a match or reaches the end of the text string.

The time complexity of the Naive String Matching Algorithm is O(n*m), where n is the length of the text string and m is the length of the pattern string. In the worst case, this can be quite slow for large strings or patterns. However, it has the advantage of being simple and easy to implement, making it a good choice for small strings or as a teaching tool for introductory computer science courses.