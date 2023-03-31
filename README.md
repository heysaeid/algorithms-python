# What Is An Algorithm
An algorithm is a step-by-step set of instructions that a computer or a human can follow to solve a problem or complete a task. It's like a recipe that you follow to cook a meal.

Just like how a recipe tells you what ingredients you need, the algorithm tells you what data you need to input. Then, it gives you a set of instructions to follow to manipulate that data until you get the desired output.

For example, let's say you want to find the largest number in a set of numbers. The algorithm for this would be:

Start with the first number in the set.
Compare it with the next number in the set.
If the next number is larger, remember it as the new largest number.
Repeat step 2 and 3 for each number in the set until you have compared all of them.
The last number you remembered as the largest number is the answer.

This algorithm works for any set of numbers, no matter how large or small, and will always give you the correct answer.

# What is Time Complexity
Time complexity is a measure of the amount of time it takes for an algorithm to complete its task as the input size increases. It's a way to compare the efficiency of different algorithms for the same task.

Time complexity is usually expressed in big O notation, which represents the upper bound on the amount of time an algorithm takes to run, as a function of the input size.

For example, an algorithm that has a time complexity of O(n) means that the time it takes to run the algorithm will increase linearly with the input size n. This means that if you double the input size, the algorithm will take roughly twice as long to run.

Some common time complexity classes and their corresponding algorithms are:

+ O(1) - constant time complexity: This means that the algorithm takes a constant amount of time to run, regardless of the input size. Examples of such algorithms are accessing an element in an array or performing a simple arithmetic operation.

+ O(log n) - logarithmic time complexity: This means that the time it takes to run the algorithm increases logarithmically with the input size. Binary search and some sorting algorithms, such as quicksort and mergesort, have a logarithmic time complexity.

+ O(n) - linear time complexity: This means that the time it takes to run the algorithm increases linearly with the input size. Traversing an array or a linked list have a linear time complexity.

+ O(n log n) - linearithmic time complexity: This means that the time it takes to run the algorithm increases by n times the logarithm of the input size. Examples of such algorithms are some sorting algorithms, like heapsort and some implementations of mergesort.

+ O(n^2) - quadratic time complexity: This means that the time it takes to run the algorithm increases by the square of the input size. Examples of such algorithms are bubble sort and insertion sort.

These are just a few examples of common time complexity classes and their corresponding algorithms. The choice of algorithm depends on the specific problem being solved and the requirements for performance and scalability.

# Do we need to know a set of algorithms?
It is important to have a good understanding of a set of algorithms as they form the foundation of computer science and are used in various applications, such as data analysis, machine learning, artificial intelligence, and many more. Understanding algorithms can help you design efficient and effective solutions to problems.

Knowing a set of algorithms helps you to choose the best algorithm for a given problem based on its time and space complexity, and also helps you to optimize the algorithm if necessary. Understanding algorithms also helps you to communicate with other developers and computer scientists about solutions to problems

Some common algorithms that are useful to know include sorting algorithms (such as bubble sort, insertion sort, quicksort, and mergesort), searching algorithms (such as linear search and binary search), graph algorithms (such as Dijkstra's algorithm and Bellman-Ford algorithm), and dynamic programming algorithms (such as the Fibonacci sequence algorithm and the Knapsack problem).

In summary, while you may not need to know every single algorithm, having a good understanding of a set of commonly used algorithms can be very beneficial in the field of computer science.

# List of Algorithms
Search:
- Binary Search
- Linear Search

Sort:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Selection Sort
- Merge Sort

Graph:
- Depth-first search (DFS)

String:
- Brute Force
- Boyer Moore
- Rabin-Karp
- Naive

Dynamic Programming:
- Fibonacci Sequence
- Maximum Subarray Sum