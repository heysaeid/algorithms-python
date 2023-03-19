"""
Bubble sort(Babel)
Time complexity: O(n^2)
ex 1) bubble_sort([19, 1, 5, 21, 545, 1]) => [1, 1, 5, 19, 21, 545]
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr