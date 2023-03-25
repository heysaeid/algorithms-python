"""
Boyer-Moore
ex 1) boyer_moore("hello world", "world") => output: 6
"""

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    # preprocess bad character rule
    last_occurrence = {}
    for i in range(m):
        last_occurrence[pattern[i]] = i
    # search
    matches = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1
        if j == -1:
            matches.append(i)
            i += 1
        else:
            bad_char_shift = j - last_occurrence.get(text[i+j], -1)
            if bad_char_shift > 0:
                i += bad_char_shift
            else:
                i += 1
    return matches