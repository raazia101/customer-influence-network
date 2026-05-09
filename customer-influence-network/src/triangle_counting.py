import networkx as nx
import pandas as pd
import os

os.makedirs('../outputs', exist_ok=True)

G = nx.read_edgelist(
    '../data/amazon0302.txt',
    comments='#',
    create_using=nx.DiGraph()
)

print("Graph loaded. Converting to undirected...")
G_undirected = G.to_undirected()

print("Counting triangles...\n")

# Triangle counting
triangles = nx.triangles(G_undirected)

total_triangles = sum(triangles.values()) // 3
avg_triangles = sum(triangles.values()) / len(triangles)

print(f"Total triangles in network: {total_triangles}")
print(f"Average triangles per node: {avg_triangles:.4f}")

# Top 10 nodes with most triangles
top_triangle_nodes = sorted(triangles.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 nodes by triangle count (most embedded in tight clusters):")
for node, count in top_triangle_nodes:
    print(f"  Node {node}: {count} triangles")

# Save results
df = pd.DataFrame(list(triangles.items()), columns=['node', 'triangle_count'])
df = df.sort_values('triangle_count', ascending=False)
df.to_csv('../outputs/triangle_results.csv', index=False)
print("\nResults saved to outputs/triangle_results.csv")

print("\n── Business Insight ──────────────────────────────────────────")
print("  Nodes with high triangle counts are deeply embedded in")
print("  tight-knit communities — these represent loyal, trusted")
print("  customers who are least likely to churn and most likely")
print("  to influence others within their cluster.")