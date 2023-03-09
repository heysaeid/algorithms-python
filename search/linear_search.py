"""
    Linear search
    Time complexity: O(n)
"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 4, 9, 12, 20, 40]
index = linear_search(arr, 12)

if index != -1:
    print(f"Found target at index {index}.")
else:
    print("Target is not found.")