# Depth-first search (DFS)
Depth-first search (DFS) is a graph traversal algorithm that explores all the vertices of a graph in depth before backtracking. The algorithm starts at a given source vertex, and explores each adjacent vertex in turn, recursively repeating the process until all vertices have been visited.

The time complexity of the Depth-first search (DFS) algorithm depends on the data structure used to represent the graph.

If the graph is represented as an adjacency matrix, where each cell represents an edge between two vertices, then the time complexity of DFS is O(|V|^2), where |V| is the number of vertices in the graph. This is because we need to examine each cell in the matrix to determine if an edge exists between two vertices.

If the graph is represented as an adjacency list, where each vertex has a list of its adjacent vertices, then the time complexity of DFS is O(|V| + |E|), where |V| is the number of vertices in the graph and |E| is the number of edges. This is because we need to visit each vertex and each edge once.

In general, the time complexity of DFS is proportional to the number of vertices and edges in the graph. However, the exact time complexity can vary depending on the specific implementation and the nature of the graph.

# Breath-first search (BFS)
BFS is a graph traversal algorithm that explores all the nodes of a graph in a level-by-level manner. Starting from a source node, it visits all its neighbors before moving on to the next level of nodes. This process continues until all nodes have been visited.

The algorithm uses a queue data structure to keep track of the nodes to be visited. It starts by enqueueing the source node and marking it as visited. Then, it repeatedly dequeues a node, visits it, enqueues its unvisited neighbors, and marks them as visited.

The time complexity of BFS depends on the size of the graph, typically represented by the number of nodes (V) and edges (E). In the worst case, where the graph is densely connected, the time complexity is O(V^2). However, in most cases, when the graph is sparsely connected, the time complexity can be approximated as O(V + E).

To summarize, BFS explores a graph in a breadth-first manner, visiting nodes level by level. It uses a queue to keep track of nodes and has a time complexity of O(V + E) in most cases.