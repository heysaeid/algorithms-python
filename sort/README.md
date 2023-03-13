# Bubble sort(Babel)
The Bubble sort algorithm, also known as the Babel sort algorithm, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

The time complexity of the bubble sort algorithm is O(n^2), where n is the number of elements in the array.

This is because the algorithm uses nested loops to compare and swap adjacent elements. In the worst-case scenario, where the array is already sorted in reverse order, the algorithm would need to make n^2 comparisons and swaps to sort the array.

Additionally, the algorithm always performs n-1 passes over the array, even if the array is already sorted, which makes it inefficient for large arrays.

For small arrays or arrays that are almost sorted, the bubble sort algorithm may perform reasonably well. However, for larger arrays, more efficient sorting algorithms such as quicksort or mergesort are preferred, as they have a better average-case and worst-case time complexity.

# Merge sort
Merge sort is a sorting algorithm that uses a divide-and-conquer strategy to sort an array. It divides the array into two halves, sorts each half recursively, and then merges the two sorted halves back together.

The time complexity of the merge sort algorithm is O(n log n) in the average and worst cases.

The merge sort algorithm divides the input array into two halves recursively until there is only one element in each half, which takes O(log n) time. Then it merges the two sorted halves back together, which takes O(n) time. Since the merge operation is performed on two halves of roughly equal size, the merge operation takes O(n) time.

Therefore, the total time complexity of the merge sort algorithm is O(n log n), as the algorithm splits the array into roughly equal halves log n times, and each of these log n levels requires O(n) time to merge the subarrays.

In the best case, where the input array is already sorted, the time complexity of merge sort is still O(n log n), as the algorithm still needs to divide and merge the array.

Overall, the merge sort algorithm provides a very efficient way of sorting arrays and is widely used in practice due to its stability, scalability, and ability to handle large datasets.