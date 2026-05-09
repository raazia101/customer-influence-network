import networkx as nx

# Load the dataset
G = nx.read_edgelist(
    '../data/amazon0302.txt',
    comments='#',
    create_using=nx.DiGraph()
)

# Basic stats
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is directed: {nx.is_directed(G)}")

# Quick sanity check - see first 5 edges
edges = list(G.edges())
print(f"\nSample edges: {edges[:5]}")