"""
Insertion Sort
ex 1) insertion_sort([19, 1, 5, 21, 545, 1]) => [1, 1, 5, 19, 21, 545]
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr