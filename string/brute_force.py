"""
String matching - brute force
Time complexity: O(nm)
ex 1) brute_force("hello world", "world") => output: 6
"""

def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
        
    return -1

print(brute_force("hello world", "world"))