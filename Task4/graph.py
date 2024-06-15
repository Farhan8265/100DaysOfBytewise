# Exercise: Graph Traversal (BFS and DFS)
from collections import deque
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)           
    return visited

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = []
    visited.append(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

print("Enter the graph as Adjacency List (e.g. '0 1 2, 1 2, 2 0 3, 3 3'):")
graph_input = input().split(", ")
graph = {}
for edge in graph_input:
    nodes = list(map(int, edge.split()))
    graph[nodes[0]] = nodes[1:]

start_node = int(input("Enter the Starting Node: "))

bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print("BFS: ", bfs_result)
print("DFS: ", dfs_result)
