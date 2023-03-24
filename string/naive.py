"""
Naive String Matching Algorithm 
Time complexity: O(n*m)
ex 1) naive_string_matching("hello world", "world") => output: 6
"""

def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            matches.append(i)
    return matches