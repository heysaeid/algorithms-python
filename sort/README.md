# Bubble sort(Babel)
The Bubble sort algorithm, also known as the Babel sort algorithm, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

The time complexity of the bubble sort algorithm is O(n^2), where n is the number of elements in the array.

This is because the algorithm uses nested loops to compare and swap adjacent elements. In the worst-case scenario, where the array is already sorted in reverse order, the algorithm would need to make n^2 comparisons and swaps to sort the array.

Additionally, the algorithm always performs n-1 passes over the array, even if the array is already sorted, which makes it inefficient for large arrays.

For small arrays or arrays that are almost sorted, the bubble sort algorithm may perform reasonably well. However, for larger arrays, more efficient sorting algorithms such as quicksort or mergesort are preferred, as they have a better average-case and worst-case time complexity.