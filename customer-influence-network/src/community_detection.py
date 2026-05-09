import networkx as nx
import pandas as pd
import os
from collections import defaultdict

os.makedirs('../outputs', exist_ok=True)

# Load dataset
G = nx.read_edgelist(
    '../data/amazon0302.txt',
    comments='#',
    create_using=nx.DiGraph()
)

print("Graph loaded. Converting to undirected...")
G_undirected = G.to_undirected()

print("Running community detection (Label Propagation)...")
print("(This should finish in under a minute)\n")

# ── Label Propagation (much faster) ──────────────────────────────
communities = list(nx.algorithms.community.label_propagation_communities(G_undirected))

# Sort by size largest first
communities = sorted(communities, key=len, reverse=True)

print(f"Total communities found: {len(communities)}")
print(f"Largest community size:  {len(communities[0])}")
print(f"Smallest community size: {len(communities[-1])}")

# ── Top 10 communities ────────────────────────────────────────────
print("\nTop 10 communities by size:")
community_data = []

for i, community in enumerate(communities[:10]):
    print(f"  Community {i+1}: {len(community)} members")
    community_data.append({
        'community_id': i + 1,
        'size': len(community),
        'sample_members': str(list(community)[:5])
    })

# ── Save results ──────────────────────────────────────────────────
df = pd.DataFrame(community_data)
df.to_csv('../outputs/community_results.csv', index=False)
print("\nResults saved to outputs/community_results.csv")

# ── Business Insight ──────────────────────────────────────────────
print("\n── Business Insight ──────────────────────────────────────────")
print(f"  {len(communities)} distinct customer segments identified")
print(f"  Largest segment contains {len(communities[0])} customers")
print(f"  Segments represent organic purchase behaviour clusters")
print(f"  Each community can receive targeted marketing messaging")