"""
Depth-first search (DFS)
"""

def dfs_recursive(graph, start, visited=None): 
    if visited is None: 
        visited = set()
    visited.add(start) 
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

visited = dfs_recursive(graph, 'A')
print(visited)