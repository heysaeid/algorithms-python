"""
Fibonacci sequence
Time complexity: O(n)
ex 1) fibonacci(10) => 55
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b