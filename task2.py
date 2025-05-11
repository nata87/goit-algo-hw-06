import networkx as nx
from collections import deque

G = nx.Graph()

stops = [
    "Центральна Площа",
    "Вокзал",
    "Університет",
    "Торговий центр",
    "Житловий масив",
    "Лікарня",
    "Парк"
]
edges = [
    ("Центральна Площа", "Вокзал"),
    ("Центральна Площа", "Університет"),
    ("Університет", "Торговий центр"),
    ("Торговий центр", "Житловий масив"),
    ("Житловий масив", "Лікарня"),
    ("Лікарня", "Парк"),
    ("Парк", "Центральна Площа")
]

G.add_nodes_from(stops)
G.add_edges_from(edges)

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

print("DFS:")
dfs_recursive(G, "Центральна Площа")
print("\nBFS:")
bfs_recursive(G, deque(["Центральна Площа"]))
