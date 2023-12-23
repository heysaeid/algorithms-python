"""
Breath-first search (BFS)
"""

from collections import deque


def bfs(graph: dict, start: str):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current_node = queue.popleft()
        print(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

bfs(graph, 'A')