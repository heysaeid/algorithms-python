def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0  # F(n-2)
    fib1 = 1  # F(n-1)
    fib = fib1 + fib2  # F(n)

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

arr = [1, 4, 9, 12, 20, 40]
target = 20

index = fibonacci_search(arr, target)
if index != -1:
    print(f"Found target at index {index}.")
else:
    print("Target is not found.")