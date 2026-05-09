# Customer Influence Network — Graph Analytics Project

A graph analytics project that models Amazon co-purchase data as a customer
influence network to identify high-value nodes and inform targeted marketing strategy.

---

## Business Problem
Which customers should a business target first to maximise word-of-mouth growth
at the lowest acquisition cost?

Traditional approaches use demographics. This project uses network structure —
treating customer relationships as a graph and letting the data reveal influence organically.

---

## Dataset
- **Source:** Stanford SNAP — Amazon Co-Purchase Network
- **Nodes:** 262,111 (products/customers)
- **Edges:** 1,234,877 (co-purchase relationships)
- **Link:** https://snap.stanford.edu/data/amazon0302.html

---

## Methods

| Method | Purpose | Business Use |
|---|---|---|
| Degree Centrality | Direct connection count | Reach estimation |
| PageRank | Quality-weighted influence | Target prioritisation |
| Label Propagation | Community detection | Customer segmentation |
| Triangle Counting | Cluster embeddedness | Loyalty signal |

---

## Key Findings
- Nodes 4429 and 33 rank in the top 10 for both degree centrality and PageRank — 
  ideal first targets for referral campaigns
- Degree centrality alone is a misleading targeting metric — PageRank reveals 
  connection quality, not just quantity
- Community detection identified distinct behavioural segments without any 
  demographic data
- High triangle count nodes represent loyal, trust-embedded customers with 
  lowest churn risk

## Visualisations

### Influencer Network
![Influencer Network](outputs/influencer_network.png)

### Degree vs PageRank
![Degree vs PageRank](outputs/degree_vs_pagerank.png)

### Triangle Distribution
![Triangle Distribution](outputs/triangle_distribution.png)

---

## Project Structure