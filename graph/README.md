# Depth-first search (DFS)
Depth-first search (DFS) is a graph traversal algorithm that explores all the vertices of a graph in depth before backtracking. The algorithm starts at a given source vertex, and explores each adjacent vertex in turn, recursively repeating the process until all vertices have been visited.

The time complexity of the Depth-first search (DFS) algorithm depends on the data structure used to represent the graph.

If the graph is represented as an adjacency matrix, where each cell represents an edge between two vertices, then the time complexity of DFS is O(|V|^2), where |V| is the number of vertices in the graph. This is because we need to examine each cell in the matrix to determine if an edge exists between two vertices.

If the graph is represented as an adjacency list, where each vertex has a list of its adjacent vertices, then the time complexity of DFS is O(|V| + |E|), where |V| is the number of vertices in the graph and |E| is the number of edges. This is because we need to visit each vertex and each edge once.

In general, the time complexity of DFS is proportional to the number of vertices and edges in the graph. However, the exact time complexity can vary depending on the specific implementation and the nature of the graph.