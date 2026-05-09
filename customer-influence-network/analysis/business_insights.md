# Business Insights — Customer Influence Network

## Project Objective
To identify high-value customer nodes in a co-purchase network using graph analytics,
and translate structural network properties into actionable marketing strategies.

---

## Key Findings

### 1. Top Influencer Nodes
Nodes 4429 and 33 ranked in the top 10 for BOTH degree centrality and PageRank.
This means they are not just widely connected — they are connected to other influential nodes.

**Business implication:**
These are prime candidates for referral marketing programs. Targeting them first
maximizes word-of-mouth reach at lower customer acquisition cost than broad campaigns.

### 2. Degree vs PageRank Gap
Node 14949 had the highest degree centrality but ranked 9th in PageRank.
This means it has many connections, but to less influential customers.

**Business implication:**
Raw connection count alone is a misleading targeting metric. PageRank-based
targeting is more cost-efficient because it accounts for the quality of connections,
not just the quantity.

### 3. Community Segmentation
Label propagation detected distinct organic customer communities formed purely
from co-purchase behaviour — not manually defined demographic segments.

**Business implication:**
Each community likely represents a product interest cluster (e.g. tech buyers,
book readers, home goods). These communities enable personalised campaign messaging
without needing survey data or demographic profiling.

### 4. Triangle Counting as a Loyalty Signal
Nodes with high triangle counts are deeply embedded in tightly-knit clusters,
meaning their neighbours also know each other.

**Business implication:**
High triangle count correlates with customer loyalty and retention. These nodes
are least likely to churn and most likely to respond positively to loyalty rewards.
They also act as trust anchors within their community — their endorsement carries
more weight than that of peripheral nodes.

---

## Strategic Recommendations

| Strategy | Target Nodes | Basis |
|---|---|---|
| Referral campaign | High PageRank nodes | Quality influence reach |
| Loyalty rewards | High triangle count nodes | Embedded trust clusters |
| Cross-sell campaigns | Community bridge nodes | High betweenness centrality |
| Personalised messaging | Community-level targeting | Organic behavioural segments |

---

## Why Graph Analytics Over Traditional Segmentation

Traditional segmentation relies on demographics (age, location, income).
Graph-based segmentation uses actual purchase behaviour and social structure.

The result is segments that are:
- More predictive of future behaviour
- Actionable without expensive survey data
- Dynamically updatable as new purchase data arrives