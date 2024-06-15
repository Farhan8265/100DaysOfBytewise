# Exercise: Dijkstra's Algorithm
import heapq
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def input_graph():
    graph = {}
    print("Enter the graph as adjacency list (e.g., 'A B 1 C 4, B C 2 D 5, C D 1, D'):")
    graph_input = input().split(", ")
    for edge in graph_input:
        nodes = edge.split()
        node = nodes[0]
        edges = {}
        for i in range(1, len(nodes) - 1, 2):
            neighbor = nodes[i]
            weight = int(nodes[i + 1])
            edges[neighbor] = weight
        graph[node] = edges
    return graph

graph = input_graph()
start_node = input("Enter the starting node: ")
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node", start_node, ":", shortest_paths)
