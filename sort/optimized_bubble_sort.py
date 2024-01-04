"""
Bubble sort(Babel)
Time complexity: O(n^2)
ex 1) optimized_bubble_sort([19, 1, 5, 21, 545, 1]) => [1, 1, 5, 19, 21, 545]
"""


def optimized_bubble_sort(arr: list[int]) -> list[int]:
    length = len(arr)
    
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
        
    return arr