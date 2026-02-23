import networkx as nx 
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices:"))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    G = nx.complete_graph(n)
    nx.draw(G, node_color='green', node_size=1500, with_labels=True)
    plt.show()
7