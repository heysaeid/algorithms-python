"""
Selection Sort
Time complexity: O(n^2)
ex 1) selection_sort([19, 1, 5, 21, 545, 1]) => [1, 1, 5, 19, 21, 545]
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr