"""
Binary search
Time complexity: O(log n)
ex 1) binary_search([1, 4, 9, 12, 20, 40], 12) => Found target at index 3.
ex 2) binary_search([1, 4, 9, 12, 20, 40], 77) => Target is not found.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 4, 9, 12, 20, 40]
index = binary_search(arr, 12)

if index != -1:
    print(f"Found target at index {index}.")
else:
    print("Target is not found.")