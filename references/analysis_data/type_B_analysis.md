# MCM/ICM Problem B (Discrete/Combinatorial) Visualization Analysis

## 1. Figure Inventory & Analysis

### 2020: Sandcastle Foundation (Discrete Simulation / CA)
*   **Visualizations:**
    *   **CA State Snapshots (Grid):** 2D/3D grid visualizations of the sandcastle foundation at $t=0$, $t=middle$, and $t=end$. Shows "erosion" process pixel by pixel.
    *   **Geometric Shapes:** 3D renderings of the 5 candidate shapes (Triangular Frustum, Square Frustum, etc.).
    *   **Algorithm Flowcharts:** Step-by-step logic for the Cellular Automaton rules and the Water-Sand ratio optimization.
    *   **Fitting Curves:** Polynomial fitting of "Duration ($t$)" vs "Water-Sand Ratio".
*   **Key Feature:** **Process Visualization**. Showing the *evolution* of a discrete system over time steps.

### 2021: Bushfire Response (Discrete Optimization / Network)
*   **Visualizations:**
    *   **GIS Risk Maps:** Heatmaps overlaid on Victoria state map showing fire risk predictions (from SSA-LSSVM).
    *   **Coverage Diagrams:** Circles/Polygons on a map representing drone coverage radii (MCLP output).
    *   **Pareto Frontiers:** Trade-off plots between "Number of Drones/Cost" and "Response Time/Coverage".
    *   **Queuing System Diagrams:** Schematic of the M/M/s/k queue (Arrival rate $\lambda$, Service rate $\mu$).
*   **Key Feature:** **Geospatial Allocation**. Discrete facility location (drones) on a continuous map.

### 2022: Water Scarcity (Network Flow / Multi-objective)
*   **Visualizations:**
    *   **System Topology:** Node-link diagram representing Dams (Nodes) and River segments (Edges).
    *   **Fitting Curves:** Scatter plots with fitted lines for "Water Level" vs "Storage Volume" for Lake Powell/Mead.
    *   **Geographic Map:** Colorado River basin map highlighting 5 states and 2 dams.
    *   **Allocation Charts:** Stacked bar charts or Sankey diagrams showing water distribution to Industry/Agriculture/Residents under different scenarios.
*   **Key Feature:** **Network Flow**. Visualizing resources moving through a constrained graph.

### 2023: Maasai Mara (Game Theory / Policy)
*   **Visualizations:**
    *   **Phase Plane Plots:** Trajectories of Lion ($x$) vs Wildebeest ($y$) populations (Limit cycles from Lotka-Volterra).
    *   **Payoff Matrices:** Tables or 3D bar charts showing utilities for Government/Locals/Tourists.
    *   **Evolutionary Dynamics:** Line charts showing the proportion of "Cooperators" vs "Poachers" over time.
    *   **Policy Impact:** Bar charts comparing "Status Quo" vs "New Policy" metrics (Income, Animal Counts).
*   **Key Feature:** **Interaction Dynamics**. Visualizing stability points and strategy evolution.

### 2024: Deep-Sea Rescue (Search Theory / 3D Dynamics)
*   **Visualizations:**
    *   **3D Trajectory Plots:** $x,y,z$ plot of the submersible drifting under ocean currents.
    *   **Search Probability Heatmaps:** Grid-based heatmap showing $P(\text{Found})$ decreasing/updating over search blocks.
    *   **Pareto Optimization:** 2D scatter plot of "Cost" vs "Success Probability" for equipment packages.
    *   **Drift Vector Fields:** Quiver plots showing ocean current directions.
*   **Key Feature:** **Search Space**. Visualizing probability distributions over a discrete search grid.

## 2. Chart Type Statistics (Type B Focus)

| Category | Chart Type | Frequency | Typical Usage in Type B |
| :--- | :--- | :--- | :--- |
| **Discrete Structures** | **Grid/Matrix** | High | CA states, Search grids, Payoff matrices. |
| | **Network/Graph** | Med | Transportation nodes, Infrastructure layout. |
| **Process/Logic** | **Flowchart** | Very High | Visualizing complex discrete algorithms (CA rules, Heuristic search). |
| | **State Diagram** | Med | Finite state machines, Queue states. |
| **Spatial** | **GIS/Map Overlay** | High | Facility location, Drone coverage, Resource distribution. |
| **Data/Analysis** | **Fitting/Regression** | High | Parameter estimation (Level-Volume, Stability-Ratio). |
| | **Pareto Frontier** | High | Multi-objective discrete optimization results. |

## 3. Design Patterns for Type B

### Pattern 1: The "Discrete Evolution" Strip
*   **Description:** A sequence of 3+ images showing the state of the system at different time steps ($T_0, T_{opt}, T_{end}$).
*   **Use Case:** Cellular Automata (Sandcastle), Simulation steps, Dynamic search processes.
*   **Why:** Discrete problems often involve step-by-step changes that are hard to describe with just equations.

### Pattern 2: The "Map + Nodes" Overlay
*   **Description:** A realistic background map (satellite or political) overlaid with abstract mathematical nodes (depots, dams, drones) and coverage radii.
*   **Use Case:** Facility location (MCLP), Resource allocation.
*   **Why:** Grounds abstract discrete optimization in the real-world context of the problem.

### Pattern 3: The "Trade-off" Scatter
*   **Description:** A scatter plot where each point is a discrete solution configuration. The "Pareto Front" is highlighted to show optimal trade-offs (e.g., Cost vs. Safety).
*   **Use Case:** Equipment selection, Portfolio optimization.
*   **Why:** Discrete problems often have finite but vast solution spaces; this visualization proves the "best" subset was chosen.

## 4. Type B Specifics & Recommendations

### Visualizing Algorithms
Unlike Continuous problems (Type A) which rely heavily on equation derivation, Type B relies on **Algorithms**.
*   **Recommendation:** Always include a high-quality, professional flowchart (e.g., Visio/Mermaid style) for your heuristic algorithms (Genetic Algorithm, Simulated Annealing, CA rules).
*   **Detail:** Don't just show boxes; show the *logic* (diamond decision shapes, loops for iterations).

### Visualizing Discrete Configurations
*   **Recommendation:** Use **Schematic Diagrams** to represent specific solution instances.
    *   *Example:* If you optimized a drone fleet, show ONE example configuration: "Here is Drone A at location X covering area Y".
    *   *Example:* If you optimized a packing/layout, show the 3D render of the optimal packing.

### Visualizing Sensitivity in Discrete Space
*   **Recommendation:** Use **Heatmaps** or **3D Bar Charts** to show how the objective function changes as you vary discrete parameters (e.g., Grid size, Number of servers). Continuous line charts are sometimes misleading for discrete parameters.
