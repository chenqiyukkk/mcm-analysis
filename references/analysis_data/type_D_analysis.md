# Visualization Analysis: MCM/ICM Problem D (Operations Research / Network Science)

## 1. Overview
Problem D typically focuses on **Operations Research (OR)** and **Network Science**. The core tasks often involve analyzing complex systems, optimizing resources, or understanding connectivity. Consequently, visualizations heavily rely on **Graph Theory** (networks, trees, flows) and **System Dynamics**.

**Analyzed Papers:**
- **2020 (Soccer):** Social Network Analysis (SNA) of passing networks.
- **2021 (Music):** Influence networks and evolutionary feature spaces.
- **2022 (Data Maturity):** System Dynamics (SD) and Hierarchical Evaluation (AHP).
- **2023 (SDGs):** Complex network of goals (Synergy/Trade-off).
- **2024 (Great Lakes):** Network flow (Hydrology) and Multi-objective optimization (Pareto).

## 2. Figure Inventory & Statistics

Based on the analysis of recent O-award papers, the following visualization types are dominant in Type D:

### A. Network & Topology Graphs (High Frequency)
*Used in: 2020, 2021, 2023, 2024*
*   **Purpose:** To visualize the structure of the system (Who connects to whom? Where does the flow go?).
*   **Common Variants:**
    *   **Force-Directed Graphs:** For displaying social networks (players, musicians) or abstract connections (SDG correlations). Nodes often sized by Centrality (Degree, PageRank).
    *   **Geospatial Networks:** For physical systems like water networks (2024 Great Lakes), where nodes are pinned to map coordinates.
    *   **Motif/Sub-graph Visualization:** Highlighting specific structures (e.g., Triangles in soccer passing).
    *   **Hierarchical Trees:** For decomposition of problems (e.g., AHP hierarchy in 2022).

### B. Dynamic & Evolutionary Plots
*Used in: 2020, 2021, 2022, 2023*
*   **Purpose:** To show how the system changes over time.
*   **Common Variants:**
    *   **Time Series Line Charts:** Basic trend analysis (e.g., 2020 Game Timeline, 2023 SDG forecasts).
    *   **Stock-and-Flow Diagrams:** Specific to System Dynamics (2022), showing accumulation and rates.
    *   **Evolutionary Trajectories:** 2D scatter paths showing how an entity (e.g., a music genre) moves in feature space over time (2021).

### C. Optimization & Trade-off Visualizations
*Used in: 2024, 2023*
*   **Purpose:** To present results of decision-making models.
*   **Common Variants:**
    *   **Pareto Frontiers:** 2D/3D scatter plots showing the trade-off between conflicting objectives (e.g., Cost vs. Reliability, Lake A Level vs. Lake B Level).
    *   **Control Rule Curves:** Function plots showing input-output relationships for controllers (e.g., Water Inflow -> Outflow decision).
    *   **Sensitivity Analysis Plots:** Tornado diagrams or line charts showing how robust the solution is to parameter changes.

### D. Statistical & Correlation Plots
*Used in: 2020, 2021, 2023*
*   **Purpose:** To justify model assumptions or validate data.
*   **Common Variants:**
    *   **Heatmaps:** Correlation matrices (e.g., SDG vs SDG, Audio Feature vs Audio Feature).
    *   **Regression Diagnostic Plots:** Residual plots, Scatter plots with fitted lines (2020).
    *   **Distributions:** Histograms of node degrees or feature values.

## 3. Design Patterns & Best Practices

### Pattern 1: "The Network is the Model"
In Type D, the network diagram often serves as the "System Diagram".
*   **Best Practice:** Don't just show a hairball of nodes. Use **color** to denote communities/clusters and **node size** to denote importance (Centrality). Use **edge thickness** for weights (flow/influence).

### Pattern 2: Algorithmic Flowcharts
Since Type D involves complex algorithms (PageRank, NSGA-II, AHP), papers frequently use flowcharts to explain the *methodology* itself.
*   **Structure:** Data Input -> Network Construction -> Metric Calculation -> Optimization -> Output.

### Pattern 3: Macro to Micro
Visualizations often follow a zoom-in pattern:
1.  **Macro:** Whole network view (Global topology).
2.  **Meso:** Community detection or Motif analysis (Sub-groups).
3.  **Micro:** Individual node metrics or specific link analysis (Case studies).

## 4. Specific Recommendations for Type D

1.  **If using Graph Theory:**
    *   Explicitly visualize the **Adjacency Matrix** (as a Heatmap) or the **Graph Topology**.
    *   If the graph is dense, use **filtering** (show only strong edges) or **backbone extraction** to avoid visual clutter.

2.  **If using System Dynamics:**
    *   Include a clear **Causal Loop Diagram (CLD)** or **Stock-and-Flow Diagram**. These are standard visual languages in this domain.

3.  **If using Optimization:**
    *   Always show the **Pareto Frontier** if multi-objective.
    *   Visualize the **"Before vs. After"**: Comparison of system state under current rules vs. optimized rules (e.g., Water levels in 2017 historical vs. optimized).

## 5. Summary Table

| Year | Problem Topic | Key Visualization | Type |
|------|---------------|-------------------|------|
| 2020 | Soccer Team | Passing Network, Motifs | Network / SNA |
| 2021 | Music Evolution | Influence Graph, Genre Centroids | Network / PCA |
| 2022 | Data Maturity | Stock-and-Flow, AHP Tree | System Dynamics |
| 2023 | SDGs | Correlation Network, Synergy Heatmap | Complex Network |
| 2024 | Great Lakes | Hydraulic Flow, Pareto Frontier | Optimization / Flow |
