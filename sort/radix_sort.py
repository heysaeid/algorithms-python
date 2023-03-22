"""
ًRadix Sort
"""

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    # Do counting sort for every digit, starting from least significant digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    # Change count[i] so that it contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    # Copy the output array to arr[]
    for i in range(n):
        arr[i] = output[i]
