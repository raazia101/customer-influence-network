import networkx as nx
import pandas as pd
import os
os.makedirs('../outputs', exist_ok=True)

# Load the dataset
G = nx.read_edgelist(
    '../data/amazon0302.txt',
    comments='#',
    create_using=nx.DiGraph()
)

print("Graph loaded. Running centrality analysis...")
print("(This may take 1-2 minutes given the dataset size)\n")

# ── 1. Degree Centrality ──────────────────────────────────────────
# Who directly influences the most people?
degree_centrality = nx.degree_centrality(G)

top_degree = sorted(degree_centrality.items(),
                    key=lambda x: x[1],
                    reverse=True)[:10]

print("Top 10 nodes by Degree Centrality (most direct connections):")
for node, score in top_degree:
    print(f"  Node {node}: {score:.6f}")

# ── 2. PageRank ───────────────────────────────────────────────────
# Who is influential based on WHO they are connected to?
print("\nCalculating PageRank...")
pagerank = nx.pagerank(G, alpha=0.85)

top_pagerank = sorted(pagerank.items(),
                      key=lambda x: x[1],
                      reverse=True)[:10]

print("\nTop 10 nodes by PageRank (most influential overall):")
for node, score in top_pagerank:
    print(f"  Node {node}: {score:.6f}")

# ── 3. Save results to CSV ────────────────────────────────────────
df = pd.DataFrame({
    'node': list(degree_centrality.keys()),
    'degree_centrality': list(degree_centrality.values()),
    'pagerank': [pagerank[n] for n in degree_centrality.keys()]
})

df = df.sort_values('pagerank', ascending=False)
df.to_csv('../outputs/centrality_results.csv', index=False)
print("\nResults saved to outputs/centrality_results.csv")