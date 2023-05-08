import heapq
#I am using Dijkstra's algorithm
class ShortestPath:
    def __init__(self, graph):
        self.graph = graph

    #algorith
    def dijkstra(self, start):
        distances = {node:float('inf') for node in self.graph}
        distances[start] = 0
        heap = [(0,start)]
        while heap:
            (current_distance, current_node) = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node].items():
                dist = current_distance + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (dist,neighbor))
        return distances
    
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 3},
    'C': {'D': 1, 'E': 6},
    'D': {'E': 4},
    'E': {}
}
'''
# with the starting vertex 'A' to get the shortest distances from 'A' to all other vertices in the graph
sp = ShortestPath(graph)
distances_from_A = sp.dijkstra('A')
print(distances_from_A)
'''