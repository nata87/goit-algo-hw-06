import heapq

graph = {
    "Центральна Площа": [("Вокзал", 5), ("Університет", 3), ("Парк", 8)],
    "Вокзал": [("Центральна Площа", 5)],
    "Університет": [("Центральна Площа", 3), ("Торговий центр", 4)],
    "Торговий центр": [("Університет", 4), ("Житловий масив", 6)],
    "Житловий масив": [("Торговий центр", 6), ("Лікарня", 7)],
    "Лікарня": [("Житловий масив", 7), ("Парк", 5)],
    "Парк": [("Лікарня", 5), ("Центральна Площа", 8)],
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

start_node = "Центральна Площа"
shortest_paths = dijkstra(graph, start_node)

print(f"\nНайкоротші відстані від '{start_node}':")
for node, distance in shortest_paths.items():
    print(f"До {node}: {distance}")
