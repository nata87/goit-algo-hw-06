import networkx as nx
import matplotlib.pyplot as plt

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
G.add_nodes_from(stops)

edges = [
    ("Центральна Площа", "Вокзал"),
    ("Центральна Площа", "Університет"),
    ("Університет", "Торговий центр"),
    ("Торговий центр", "Житловий масив"),
    ("Житловий масив", "Лікарня"),
    ("Лікарня", "Парк"),
    ("Парк", "Центральна Площа")
]
G.add_edges_from(edges)

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь кожної вершини:", dict(G.degree()))


plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()