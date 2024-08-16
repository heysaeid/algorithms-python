import math

def jump_search(arr, target):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step, n)-1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == target:
        return int(prev)

    return -1

arr = [1, 4, 9, 12, 20, 40]
target = 20

index = jump_search(arr, target)
if index != -1:
    print(f"Found target at index {index}.")
else:
    print("Target is not found.")
