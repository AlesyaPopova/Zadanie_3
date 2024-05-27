import networkx as nx
G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

G.add_edge(1,4)
G.add_edge(2,4)
G.add_edge(3,4)

print(G)

centrality = nx.eigenvector_centrality_numpy(G)

for n in centrality:
    print("Узел", n, "имеет центральность =", centrality[n])

#Graph with 4 nodes and 3 edges
#Узел 1 имеет центральность = 0.4082482904638631
#Узел 2 имеет центральность = 0.40824829046386313
#Узел 3 имеет центральность = 0.408248290463863
#Узел 4 имеет центральность = 0.7071067811865474
