import networkx as nx
from task1 import G

weighted_edges = [
    ("Центральна Площа", "Вокзал", 5),
    ("Центральна Площа", "Університет", 3),
    ("Університет", "Торговий центр", 4),
    ("Торговий центр", "Житловий масив", 6),
    ("Житловий масив", "Лікарня", 7),
    ("Лікарня", "Парк", 5),
    ("Парк", "Центральна Площа", 8)
]

WG = nx.Graph()
WG.add_weighted_edges_from(weighted_edges)

print("\nНайкоротші шляхи від Центральна Площа (алгоритм Дейкстри):")
for target in WG.nodes:
    path = nx.dijkstra_path(WG, source="Центральна Площа", target=target)
    length = nx.dijkstra_path_length(WG, source="Центральна Площа", target=target)
    print(f"До {target}: шлях {path}, довжина {length}")
