# Customer Influence Network — Business Insights

## Dataset
- Source: Amazon Co-Purchase Network (SNAP Stanford)
- Nodes: 262,111 (customers/products)
- Edges: 1,234,877 (co-purchase relationships)

---

## Key Findings

### 1. Top Influencer Nodes
Nodes 4429 and 33 appeared in the top 10 of BOTH degree 
centrality and PageRank rankings.

**Business Implication:**
These nodes are not just highly connected — they are connected 
to other influential nodes. In a real marketing context, 
targeting these customers first with referral incentives would 
produce the highest network-wide impact at the lowest cost.

This is significantly more efficient than broad-based marketing 
because influence spreads organically through existing 
connections.

---

### 2. Customer Segmentation
- Total organic segments detected: 24,717
- Largest segment size: 1,180 customers
- Top 10 segments range from 386 to 1,180 members

**Business Implication:**
These segments formed purely from purchase behaviour — not 
demographics or manual labelling. Each community likely 
represents a distinct product interest cluster (e.g. tech 
buyers, book readers, home goods).

A business can assign a different marketing message to each 
community, improving conversion rates compared to one-size-
fits-all campaigns.

---

### 3. Triangle Counting and Customer Loyalty
- Total triangles in network: 717,719
- Average triangles per node: 8.21
- Node 14949 leads with 520 triangles
- Node 4429 follows with 446 triangles

**Business Implication:**
The network contains 717,719 closed triangular relationships,
with an average of 8.21 triangles per node — indicating a
highly trust-embedded customer base overall.

Nodes with the highest triangle counts are deeply embedded
in tight peer clusters where purchase decisions mutually
reinforce each other. These are not just influential customers
— they are loyal ones.

Most critically, Node 4429 appears in the top 10 of ALL
three metrics — degree centrality, PageRank, and triangle
count. This makes it the single highest priority node across
every dimension of influence. It has wide reach, high quality
connections, AND deep community embeddedness simultaneously.

Node 14949 tells a different story — it ranks 1st in degree
centrality and 1st in triangle count, but only 9th in
PageRank. This means it has massive reach and is deeply
embedded locally, but its connections
---

### 4. PageRank vs Degree Centrality — Strategic Distinction

| Node  | Degree Centrality | PageRank | Strategy |
|-------|-------------------|----------|----------|
| 14949 | Highest           | 9th      | High reach, lower quality connections |
| 4429  | 2nd               | 1st      | Prime target — high reach + high influence |
| 33    | 3rd               | 2nd      | Prime target — consistent across both metrics |

**Business Implication:**
Not all highly connected customers are equal. PageRank 
identifies customers whose connections are themselves 
influential — these are the ones whose recommendations 
carry the most weight in their network.

---

## Strategic Recommendations

1. **Prioritise nodes 4429 and 33** for referral and 
   ambassador programs — highest combined influence score.

2. **Segment marketing campaigns** by community — each of 
   the top 10 communities represents a distinct customer 
   interest cluster requiring a tailored message.

3. **Use triangle density as a loyalty proxy** — high 
   triangle count nodes are deeply embedded in peer groups 
   and respond better to retention offers than acquisition 
   campaigns.

4. **Combine PageRank + degree centrality** for targeting 
   decisions — neither metric alone is sufficient. Nodes 
   ranking highly on both are the most valuable marketing 
   targets.

---

## Conclusion
Graph-based customer analysis reveals structural insights 
that traditional demographic segmentation cannot capture. 
By treating purchase behaviour as a network, businesses can 
identify influence pathways, organic segments, and loyalty 
clusters — enabling more precise, cost-effective marketing 
strategies.
