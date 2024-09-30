import matplotlib
matplotlib.use('TkAgg')  # Set the backend for displaying plots (place this at the top)

import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes (devices) to the graph
G.add_node("Router")
G.add_node("Switch1")
G.add_node("Switch2")
G.add_node("Server1")
G.add_node("Server2")

# Add edges (connections) between the nodes
G.add_edge("Router", "Switch1")
G.add_edge("Router", "Switch2")
G.add_edge("Switch1", "Server1")
G.add_edge("Switch2", "Server2")

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()
