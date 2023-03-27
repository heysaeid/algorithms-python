"""
Rabin-Karp
ex 1) rabin_karp("hello world", "world") => output: 6
"""

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    # compute hash value of pattern
    pattern_hash = 0
    x = 31
    for i in range(m):
        pattern_hash = pattern_hash*x + ord(pattern[i])
    # search
    matches = []
    text_hash = 0
    for i in range(n-m+1):
        if i == 0:
            for j in range(m):
                text_hash = text_hash*x + ord(text[i+j])
        else:
            text_hash = x*(text_hash - ord(text[i-1])*x**(m-1)) + ord(text[i+m-1])
        if text_hash == pattern_hash and text[i:i+m] == pattern:
            matches.append(i)
    return matches