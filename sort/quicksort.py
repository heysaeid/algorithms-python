"""
Quicksort
Time complexity: O(n log n) or O(n^2)
ex 1) quicksort([19, 1, 5, 21, 545, 1]) => [1, 1, 5, 19, 21, 545]
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)