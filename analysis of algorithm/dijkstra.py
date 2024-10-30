import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to keep track of nodes to visit
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the computed distance, skip
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    for _ in range(num_vertices):
        node = input("Enter vertex: ")
        edges = {}
        num_edges = int(input(f"Enter the number of edges for vertex {node}: "))
        for _ in range(num_edges):
            neighbor, weight = input("Enter neighbor and weight separated by space: ").split()
            edges[neighbor] = int(weight)
        graph[node] = edges
    
    start_node = input("Enter the start node: ")
    distances = dijkstra(graph, start_node)
    print("Shortest distances from", start_node, "to other nodes:")
    for node, distance in distances.items():
        print("Node:", node, "Distance:", distance)

if __name__ == "__main__":
    main()
