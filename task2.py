import networkx as nx
from task1 import G  


dfs_edges = list(nx.dfs_edges(G, source="Центральна Площа"))
print("\nDFS шлях від Центральна Площа:")
print(dfs_edges)

bfs_edges = list(nx.bfs_edges(G, source="Центральна Площа"))
print("\nBFS шлях від Центральна Площа:")
print(bfs_edges)