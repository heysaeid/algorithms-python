# Linear search
The linear search algorithm is a simple search algorithm that checks each element of a list or array one by one until it finds the target element.

The time complexity of linear search is O(n), where n is the number of elements in the array. This is because in the worst case, the algorithm will have to check every element in the array before finding the target (or determining that the target is not in the array). Therefore, as the size of the array grows, the time it takes to perform a linear search will also grow linearly.

# Binary search
The binary search algorithm is a more efficient search algorithm than linear search, especially when searching through large sorted arrays. It works by repeatedly dividing the search interval in half until the target value is found.

The time complexity of binary search algorithm is O(log n).

This means that the time it takes to execute the algorithm increases logarithmically with the size of the input array or list. For example, if the input array has 100 elements, binary search will take at most log2(100) = 6.64 iterations to find the target element. As the size of the input array doubles, the number of iterations needed to complete the binary search algorithm only increases by 1.

This makes binary search a very efficient algorithm for searching large sorted arrays. By comparison, linear search has a time complexity of O(n), meaning that the time it takes to execute the algorithm increases linearly with the size of the input array. This can make linear search much slower than binary search for large arrays.