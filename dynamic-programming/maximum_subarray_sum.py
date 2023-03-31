"""
Maximum Subarray Sum
Time complexity: O(n)
ex 1) max_subarray_sum([10, -3, 1, 4, -7, 1, 4]) => 12
"""

def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far