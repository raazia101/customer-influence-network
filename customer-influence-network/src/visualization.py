import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import os

os.makedirs('../outputs', exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

G = nx.read_edgelist(
    '../data/amazon0302.txt',
    comments='#',
    create_using=nx.DiGraph()
)

print("Graph loaded. Building clean visualizations...")

centrality_df = pd.read_csv('../outputs/centrality_results.csv')
triangle_df   = pd.read_csv('../outputs/triangle_results.csv')

centrality_df['node'] = centrality_df['node'].astype(str)
triangle_df['node']   = triangle_df['node'].astype(str)

# ── Plot 1: Top 10 Nodes — Horizontal Bar Chart ───────────────────
# Instead of a messy network diagram, show the top 10 nodes clearly
# as a ranked bar chart. Clean, readable, and immediately interpretable.

print("Generating Plot 1: Top 10 Influencer Rankings...")

top10 = centrality_df.head(10).copy()
top10 = top10.sort_values('pagerank', ascending=True)  # ascending for horizontal bar
top10['node_label'] = 'Node ' + top10['node']

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Top 10 Most Influential Customer Nodes', 
             fontsize=16, fontweight='bold', y=1.02)

# Left: PageRank
colors_pr = ['#1a5276' if i >= 8 else '#2e86c1' if i >= 5 else '#85c1e9' 
             for i in range(len(top10))]
bars1 = axes[0].barh(top10['node_label'], top10['pagerank'], color=colors_pr, height=0.6)
axes[0].set_xlabel('PageRank Score', fontsize=12)
axes[0].set_title('By PageRank\n(influence quality — who your connections are)', 
                  fontsize=11, pad=10)
axes[0].set_xlim(0, top10['pagerank'].max() * 1.25)

for bar, val in zip(bars1, top10['pagerank']):
    axes[0].text(bar.get_width() + top10['pagerank'].max() * 0.02,
                 bar.get_y() + bar.get_height() / 2,
                 f'{val:.5f}', va='center', fontsize=9, color='#2c3e50')

# Right: Degree Centrality
top10_deg = centrality_df.sort_values('degree_centrality', ascending=False).head(10).copy()
top10_deg = top10_deg.sort_values('degree_centrality', ascending=True)
top10_deg['node_label'] = 'Node ' + top10_deg['node']

colors_deg = ['#1e8449' if i >= 8 else '#27ae60' if i >= 5 else '#82e0aa' 
              for i in range(len(top10_deg))]
bars2 = axes[1].barh(top10_deg['node_label'], top10_deg['degree_centrality'], 
                     color=colors_deg, height=0.6)
axes[1].set_xlabel('Degree Centrality Score', fontsize=12)
axes[1].set_title('By Degree Centrality\n(influence reach — how many you connect to directly)', 
                  fontsize=11, pad=10)
axes[1].set_xlim(0, top10_deg['degree_centrality'].max() * 1.25)

for bar, val in zip(bars2, top10_deg['degree_centrality']):
    axes[1].text(bar.get_width() + top10_deg['degree_centrality'].max() * 0.02,
                 bar.get_y() + bar.get_height() / 2,
                 f'{val:.5f}', va='center', fontsize=9, color='#2c3e50')

plt.tight_layout()
plt.savefig('../outputs/top10_influencers.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: top10_influencers.png")


# ── Plot 2: Degree vs PageRank — Cleaned Scatter ──────────────────
print("Generating Plot 2: Degree vs PageRank scatter...")

fig, ax = plt.subplots(figsize=(12, 7))

# Sample 5000 points so it's not overcrowded
sample = centrality_df.sample(n=min(5000, len(centrality_df)), random_state=42)
top10_full = centrality_df.head(10)

ax.scatter(sample['degree_centrality'], sample['pagerank'],
           alpha=0.15, s=8, color='#2e86c1', label='All nodes')

ax.scatter(top10_full['degree_centrality'], top10_full['pagerank'],
           alpha=1.0, s=120, color='#e74c3c', zorder=5, label='Top 10 target nodes')

# Label only the top 10
for _, row in top10_full.iterrows():
    ax.annotate(
        f"Node {row['node']}",
        (row['degree_centrality'], row['pagerank']),
        fontsize=8.5,
        fontweight='bold',
        color='#922b21',
        xytext=(8, 6),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='-', color='#e74c3c', lw=0.8)
    )

ax.set_xlabel('Degree Centrality  (breadth of direct connections)', fontsize=12)
ax.set_ylabel('PageRank Score  (quality of influence)', fontsize=12)
ax.set_title('Degree Centrality vs PageRank\n'
             'Nodes in the top-right are high priority: broadly connected AND influential',
             fontsize=13, fontweight='bold', pad=15)

ax.legend(fontsize=10, framealpha=0.9)

# Add quadrant annotations
x_mid = sample['degree_centrality'].median()
y_mid = sample['pagerank'].median()

ax.axvline(x_mid, color='gray', linestyle='--', alpha=0.4, lw=1)
ax.axhline(y_mid, color='gray', linestyle='--', alpha=0.4, lw=1)

ax.text(x_mid * 1.05, ax.get_ylim()[1] * 0.95,
        'High reach\nHigh quality\n→ Prime targets', fontsize=8,
        color='#1a5276', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d6eaf8', alpha=0.7))

ax.text(ax.get_xlim()[0], ax.get_ylim()[1] * 0.95,
        'Low reach\nHigh quality\n→ Hidden connectors', fontsize=8,
        color='#1e8449', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d5f5e3', alpha=0.7))

plt.tight_layout()
plt.savefig('../outputs/degree_vs_pagerank.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: degree_vs_pagerank.png")


# ── Plot 3: Triangle Distribution — Clean Histogram ───────────────
print("Generating Plot 3: Triangle distribution...")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Triangle Count Distribution — Measuring Customer Loyalty Embeddedness',
             fontsize=14, fontweight='bold', y=1.02)

tri_nonzero = triangle_df[triangle_df['triangle_count'] > 0]['triangle_count']

# Left: log scale histogram
axes[0].hist(tri_nonzero, bins=60, color='#8e44ad', edgecolor='white', 
             linewidth=0.5, log=True)
axes[0].set_xlabel('Triangle Count per Node', fontsize=12)
axes[0].set_ylabel('Number of Nodes (log scale)', fontsize=12)
axes[0].set_title('Full Distribution (log scale)\nMost nodes have few triangles — '
                  'loyalty is concentrated', fontsize=11, pad=10)

axes[0].axvline(tri_nonzero.mean(), color='#e74c3c', linestyle='--', lw=1.5,
                label=f'Mean: {tri_nonzero.mean():.1f}')
axes[0].axvline(tri_nonzero.median(), color='#f39c12', linestyle='--', lw=1.5,
                label=f'Median: {tri_nonzero.median():.1f}')
axes[0].legend(fontsize=9)

# Right: top 15 nodes by triangle count as bar chart
top15_tri = triangle_df.sort_values('triangle_count', ascending=False).head(15).copy()
top15_tri = top15_tri.sort_values('triangle_count', ascending=True)
top15_tri['node_label'] = 'Node ' + top15_tri['node']

colors_tri = ['#6c3483' if i >= 12 else '#8e44ad' if i >= 8 else '#bb8fce'
              for i in range(len(top15_tri))]
bars = axes[1].barh(top15_tri['node_label'], top15_tri['triangle_count'],
                    color=colors_tri, height=0.6)
axes[1].set_xlabel('Number of Triangles', fontsize=12)
axes[1].set_title('Top 15 Nodes by Triangle Count\n'
                  'These are your most loyal, trust-embedded customers', fontsize=11, pad=10)

for bar, val in zip(bars, top15_tri['triangle_count']):
    axes[1].text(bar.get_width() + top15_tri['triangle_count'].max() * 0.01,
                 bar.get_y() + bar.get_height() / 2,
                 f'{int(val):,}', va='center', fontsize=9, color='#4a235a')

plt.tight_layout()
plt.savefig('../outputs/triangle_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: triangle_analysis.png")


# ── Plot 4: Small clean network — top 15 nodes only ───────────────
print("Generating Plot 4: Clean influencer network map...")

top15_nodes = centrality_df.head(15)['node'].tolist()
subgraph = G.subgraph(top15_nodes)

pagerank_map = dict(zip(centrality_df['node'], centrality_df['pagerank']))
node_sizes   = [pagerank_map.get(n, 0.0001) * 120000 for n in subgraph.nodes()]
node_colors  = [pagerank_map.get(n, 0.0001) for n in subgraph.nodes()]

fig, ax = plt.subplots(figsize=(13, 9))
pos = nx.spring_layout(subgraph, seed=7, k=2.5)

nodes = nx.draw_networkx_nodes(subgraph, pos,
                               node_size=node_sizes,
                               node_color=node_colors,
                               cmap=plt.cm.Blues,
                               ax=ax)

nx.draw_networkx_edges(subgraph, pos,
                       edge_color='#aab7b8',
                       arrows=True,
                       arrowsize=15,
                       width=1.5,
                       alpha=0.7,
                       ax=ax)

# Clean labels with background box
for node, (x, y) in pos.items():
    ax.text(x, y, f'Node\n{node}',
            fontsize=8, fontweight='bold',
            ha='center', va='center',
            color='white' if pagerank_map.get(node, 0) > 0.0003 else '#1a252f',
            bbox=dict(boxstyle='round,pad=0.2', 
                      facecolor='none', 
                      edgecolor='none'))

sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues,
                            norm=plt.Normalize(vmin=min(node_colors), 
                                               vmax=max(node_colors)))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.6, pad=0.02)
cbar.set_label('PageRank Score', fontsize=10)

ax.set_title('Top 15 Customer Influencer Network\n'
             'Node size and colour intensity = PageRank score  |  '
             'Arrows show co-purchase direction',
             fontsize=13, fontweight='bold', pad=15)
ax.axis('off')

plt.tight_layout()
plt.savefig('../outputs/influencer_network.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: influencer_network.png")

print("\nAll 4 visualizations saved cleanly to outputs/")
print("\nFiles generated:")
print("  top10_influencers.png    — ranked bar charts for PageRank and Degree")
print("  degree_vs_pagerank.png   — scatter with quadrant labels")
print("  triangle_analysis.png    — distribution + top 15 loyalty nodes")
print("  influencer_network.png   — clean network map, top 15 only")