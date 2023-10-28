import networkx as nx
import math
from math import radians, sin, cos, sqrt, atan2
import matplotlib.pyplot as plt

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

G = nx.Graph()
data = [
    (23.749249, 90.369372, 14),
    (23.749249, 90.374405, 6),
    (23.749249, 90.379438, 5),
    (23.749249, 90.384471, 22),
    (23.749249, 90.389504, 25),
    (23.749249, 90.394537, 18),
    (23.749249, 90.39957, 1),
    (23.745657, 90.369372, 4),
    (23.745657, 90.374405, 10),
    (23.745657, 90.379438, 26),
    (23.745657, 90.384471, 18),
    (23.745657, 90.389504, 8),
    (23.745657, 90.394537, 1),
    (23.745657, 90.39957, 1),
    (23.742065, 90.369372, 5),
    (23.742065, 90.374405, 15),
    (23.742065, 90.379438, 30),
    (23.742065, 90.384471, 1),
    (23.742065, 90.389504, 25),
    (23.742065, 90.394537, 15),
    (23.742065, 90.39957, 21),
    (23.738473, 90.369372, 12),
    (23.738473, 90.374405, 11),
    (23.738473, 90.379438, 20),
    (23.738473, 90.384471, 29),
    (23.738473, 90.389504, 8),
    (23.738473, 90.394537, 8),
    (23.738473, 90.39957, 5),
    (23.73488, 90.369372, 8),
    (23.73488, 90.374405, 7),
    (23.73488, 90.379438, 27),
    (23.73488, 90.384471, 21),
    (23.73488, 90.389504, 13),
    (23.73488, 90.394537, 23),
    (23.73488, 90.39957, 25),
    (23.731288, 90.369372, 19),
    (23.731288, 90.374405, 10),
    (23.731288, 90.379438, 20),
    (23.731288, 90.384471, 5),
    (23.731288, 90.389504, 9),
    (23.731288, 90.394537, 25),
    (23.731288, 90.39957, 7),
    (23.727696, 90.369372, 17),
    (23.727696, 90.374405, 7),
    (23.727696, 90.379438, 10),
    (23.727696, 90.384471, 2),
    (23.727696, 90.389504, 17),
    (23.727696, 90.394537, 29),
    (23.727696, 90.39957, 17)
]

deadZones = [item for item in data if item[2] <= 15]

for zone in deadZones:
    G.add_node(zone)

for i in range(len(deadZones)):
    for j in range(i+1, len(deadZones)):
        lat1, lon1, _ = deadZones[i]
        lat2, lon2, _ = deadZones[j]
        dist = calculate_distance(lat1, lon1, lat2, lon2)
        print("Distance:", dist, "km")
        G.add_edge(i, j, weight=dist)
print(G.edges)
edge_labels = nx.get_edge_attributes(G, 'distance')
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.savefig("weighted_graph.png")
plt.show()

# Apply Dijkstra’s Algorithm: use networkx's shortest_path function

# Cover Nodes
# covered_nodes = set()
# circles = []
# for node in nx.dfs_preorder_nodes(G):
#     if node not in covered_nodes:
#         # add a new circle covering this node
#         circles.append(node)
#         # update covered_nodes
#         pass

