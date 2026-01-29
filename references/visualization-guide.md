# MCM Visualization Guide
A comprehensive guide to selecting and designing O-award quality figures for MCM/ICM competitions.

**Version**: 1.2.1 | **Updated**: January 2026

---

## 1. The "Golden Rules" of O-Award Figures

Based on analysis of 2020-2024 Outstanding Papers:

1.  **Start with a Schematic**: The first figure in your paper should almost *always* be a visual flowchart or framework diagram explaining your model logic.
2.  **Verify, Don't Just Display**: Use charts to *prove* your model works (e.g., Residual Plots, Prediction vs. Actual, Sensitivity Analysis).
3.  **Space Efficiency**: Use Multi-panel layouts (2x2 grid) to show multiple scenarios in one figure. Never waste a whole page on a simple line chart.
4.  **Consistency**: Use the same font (Times New Roman), size (11pt), and color palette (Okabe-Ito) throughout the entire paper.

---

## 2. Quick Start

### Install Dependencies
```bash
pip install matplotlib numpy scipy networkx seaborn
```

### Basic Usage
```python
# Step 1: Apply MCM style (do this FIRST, before any plotting)
from templates.visualization import use_mcm_style, COLORS
use_mcm_style()

# Step 2: Import the template you need
from templates.visualization.plot_templates import plot_forecast, create_grid_layout

# Step 3: Create your plot
import numpy as np
x = np.arange(100)
y = np.sin(x * 0.1)
fig, ax = plot_forecast(x, y, title="My Forecast")
```

---

## 3. Recommended Charts by Problem Type

| Problem Type | Core Visualizations | Recommended Templates |
|--------------|---------------------|----------------------|
| **A (Continuous)** | Phase Portraits, Streamplots, Time Series | `phase_portrait.py`, `time_series.py` |
| **B (Discrete)** | Network Graphs, Pareto Frontiers, Sensitivity | `network_graph.py`, `pareto_frontier.py` |
| **C (Data)** | Correlation Heatmaps, Time Series, Confusion Matrices | `heatmap.py`, `time_series.py` |
| **D (Network)** | Topology Maps, Pareto Frontiers, Tornado Diagrams | `network_graph.py`, `pareto_frontier.py` |
| **E (Environment)** | Spatial Heatmaps, Multi-panel, Sensitivity | `heatmap.py`, `sensitivity_tornado.py` |
| **F (Policy)** | Framework Diagrams, Stakeholder Networks, Sensitivity | `network_graph.py`, `sensitivity_tornado.py` |

---

## 4. Available Templates

### 4.1 Time Series (`time_series.py`)
**Best for**: Type A, C, E — Forecasting, trend analysis

```python
from templates.visualization.plot_templates import plot_forecast, plot_dual_axis

# Forecast with confidence interval
fig, ax = plot_forecast(
    dates=date_array,
    y_history=historical_values,
    y_forecast=predicted_values,
    y_ci_lower=lower_bound,
    y_ci_upper=upper_bound,
    title="Gold Price Prediction",
    xlabel="Date",
    ylabel="Price ($)"
)

# Dual-axis comparison (e.g., Price vs Volume)
fig, (ax1, ax2) = plot_dual_axis(
    x=dates,
    y1=prices,
    y2=volumes,
    ylabel1="Price ($)",
    ylabel2="Volume"
)
```

### 4.2 Heatmap (`heatmap.py`)
**Best for**: Type C — Correlation analysis, confusion matrices

```python
from templates.visualization.plot_templates import (
    plot_correlation_matrix, 
    plot_confusion_matrix,
    plot_spatial_heatmap
)

# Correlation matrix (auto-masks upper triangle)
fig, ax = plot_correlation_matrix(
    data=df,  # DataFrame or correlation matrix
    title="Feature Correlation Analysis"
)

# Confusion matrix for classification
fig, ax = plot_confusion_matrix(
    cm=confusion_matrix_array,
    classes=['Class A', 'Class B', 'Class C'],
    normalize=True
)

# Spatial data (e.g., temperature distribution)
fig, ax = plot_spatial_heatmap(
    data_grid=2d_array,
    title="Temperature Distribution"
)
```

### 4.3 Phase Portrait (`phase_portrait.py`)
**Best for**: Type A — Dynamic systems, stability analysis

```python
from templates.visualization.plot_templates import plot_phase_portrait

# Define your system (Lotka-Volterra example)
def dx_dt(x, y, alpha=1.0, beta=0.1):
    return alpha * x - beta * x * y

def dy_dt(x, y, gamma=0.1, delta=0.5):
    return gamma * x * y - delta * y

fig, ax = plot_phase_portrait(
    dxdt_func=dx_dt,
    dydt_func=dy_dt,
    x_range=(0, 20),
    y_range=(0, 20),
    nullclines=True,
    trajectories=[(1, 1), (5, 5), (10, 2)],  # Initial conditions
    title="Predator-Prey Dynamics"
)
```

### 4.4 Network Graph (`network_graph.py`)
**Best for**: Type B, D, F — Network analysis, hierarchies

```python
from templates.visualization.plot_templates import plot_network_topology, plot_tree_hierarchy
import networkx as nx

# Create a network
G = nx.karate_club_graph()

# Plot with automatic degree-based sizing
fig, ax = plot_network_topology(
    G=G,
    layout_algorithm="kamada_kawai",
    title="Social Network Structure"
)

# For hierarchical structures (AHP, decision trees)
tree = nx.balanced_tree(r=2, h=3)
fig, ax = plot_tree_hierarchy(tree, title="AHP Hierarchy")
```

### 4.5 Multi-Panel Layout (`multi_panel.py`)
**Best for**: All types — Scenario comparison, result organization

```python
from templates.visualization.plot_templates import (
    create_grid_layout,
    create_asymmetric_layout,
    create_comparison_panel
)

# Standard 2x2 grid with automatic (a), (b), (c), (d) labels
fig, axes = create_grid_layout(
    nrows=2, ncols=2,
    suptitle="Model Comparison",
    sharex=True  # Share x-axis across columns
)

# Plot on each panel
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Scenario A")
# ... fill other panels

# Asymmetric layout (e.g., one large + two small)
layout = [
    [1, 1, 2],
    [3, 4, 2]
]
fig, axes_dict = create_asymmetric_layout(layout, suptitle="Results")
# axes_dict[1] is the wide plot, axes_dict[2] is the tall plot, etc.
```

### 4.6 Pareto Frontier (`pareto_frontier.py`) ⭐ NEW
**Best for**: Type B, D, E — Multi-objective optimization

```python
from templates.visualization.plot_templates import (
    plot_pareto_frontier,
    plot_parallel_coordinates,
    identify_pareto_front
)

# 2D Pareto front
fig, ax = plot_pareto_frontier(
    x=cost_values,
    y=risk_values,
    minimize_x=True,
    minimize_y=True,
    xlabel="Cost ($)",
    ylabel="Risk Index",
    title="Cost vs Risk Trade-off",
    show_ideal=True,
    show_nadir=True
)

# For 4+ objectives: parallel coordinates
fig, ax = plot_parallel_coordinates(
    data=multi_objective_matrix,  # (n_solutions x n_objectives)
    objective_names=["Cost", "Time", "Quality", "Risk"],
    pareto_mask=is_pareto_optimal,
    title="Multi-Objective Trade-offs"
)
```

### 4.7 Sensitivity Analysis (`sensitivity_tornado.py`) ⭐ NEW
**Best for**: All types — Parameter sensitivity, robustness analysis

```python
from templates.visualization.plot_templates import (
    plot_tornado,
    plot_sensitivity_spider,
    plot_sensitivity_heatmap,
    create_sensitivity_summary_table
)

# Tornado diagram (most common in MCM papers)
fig, ax = plot_tornado(
    param_names=["Growth Rate", "Capacity", "Mortality", "Migration"],
    low_values=[95, 88, 102, 99],   # Output when parameter is -10%
    high_values=[108, 115, 97, 101], # Output when parameter is +10%
    baseline=100,
    xlabel="Impact on Population",
    title="Parameter Sensitivity Analysis"
)

# Generate markdown table for paper
table = create_sensitivity_summary_table(
    param_names, low_values, high_values, baseline
)
print(table)  # Copy to your paper
```

---

## 5. Style Configuration

### Color Palette (Okabe-Ito)
All templates use the colorblind-safe Okabe-Ito palette:

```python
from templates.visualization import COLORS, COLOR_LIST, get_colors

# Named colors
COLORS['blue']          # #0072B2 (primary)
COLORS['orange']        # #E69F00 (secondary)
COLORS['bluish_green']  # #009E73
COLORS['vermilion']     # #D55E00
COLORS['reddish_purple']# #CC79A7
COLORS['sky_blue']      # #56B4E9
COLORS['yellow']        # #F0E442

# Get N colors for plotting
colors = get_colors(5)  # Returns first 5 colors
```

### Figure Dimensions
Standard sizes for MCM papers:

```python
from templates.visualization import DIMENSIONS

DIMENSIONS['single_column']  # (3.5, 2.8) - for small plots
DIMENSIONS['double_column']  # (7.0, 4.5) - standard MCM width
DIMENSIONS['square']         # (5.0, 5.0) - phase portraits, networks
DIMENSIONS['full_page']      # (7.0, 9.0) - multi-panel with many rows
```

### Utility Functions

```python
from templates.visualization import (
    add_subplot_labels,      # Add (a), (b), (c) labels
    optimize_legend_location, # Smart legend placement
    latex_label,             # Handle LaTeX math in labels
    save_figure,             # Save PNG + PDF at once
    setup_figure             # Quick figure setup with style
)

# Quick figure setup
fig, axes = setup_figure(size='double_column', nrows=2, ncols=2)

# Add labels after plotting
add_subplot_labels(axes, style='parentheses')  # (a), (b), (c)...

# Smart legend (avoids data overlap)
optimize_legend_location(ax, prefer_outside=True)

# LaTeX in labels
ax.set_xlabel(latex_label('$x^2 + y^2$'))

# Save in multiple formats
save_figure(fig, 'results', formats=['png', 'pdf'])
```

---

## 6. Design Patterns & Tips

### Caption Style
- Place titles **below** the figure in LaTeX
- Use descriptive captions: "Figure 1: Evolution of the System State. (a) Phase portrait showing stability. (b) Time series of variable X."

### Space Efficiency
- Use 2x2 or 3x2 grids instead of separate figures
- Combine related plots (e.g., prediction + residuals)
- Each figure should have a clear purpose

### LaTeX Integration
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/results.pdf}
    \caption{Model results. (a) Pareto frontier showing cost-risk trade-off. 
             (b) Sensitivity analysis indicating growth rate as most influential.}
    \label{fig:results}
\end{figure}
```

---

## 7. Beyond Python: External Tools

For diagrams that are hard to code (Flowcharts, System Dynamics):
- Use the **`scientific-schematics`** skill
- Prompt: "Generate a system dynamics flowchart for a predator-prey model with delay."
- Use the **`generate-image`** skill for concept illustrations

---

## 8. Complete Example

```python
"""
Complete example: Generate all figures for a Type B problem
"""
from templates.visualization import use_mcm_style, save_figure
from templates.visualization.plot_templates import (
    create_grid_layout,
    plot_pareto_frontier,
    plot_tornado,
    plot_network_topology
)
import numpy as np
import networkx as nx

# Apply style first!
use_mcm_style()

# Figure 1: Model Framework (use scientific-schematics skill)

# Figure 2: Network Analysis
G = nx.random_geometric_graph(50, 0.2)
fig1, ax1 = plot_network_topology(G, title="Resource Distribution Network")
save_figure(fig1, 'fig2_network')

# Figure 3: Optimization Results (2x2 panel)
fig2, axes = create_grid_layout(2, 2, suptitle="Optimization Results")

# (a) Pareto front
x = np.random.uniform(0, 10, 30)
y = 10 - x + np.random.normal(0, 1, 30)
axes[0, 0].scatter(x, y)
axes[0, 0].set_title("Pareto Front")

# (b) Convergence
iters = np.arange(100)
cost = 100 * np.exp(-0.05 * iters) + np.random.normal(0, 2, 100)
axes[0, 1].plot(iters, cost)
axes[0, 1].set_title("Convergence")

# (c) Solution distribution
axes[1, 0].hist(np.random.normal(50, 10, 200), bins=20)
axes[1, 0].set_title("Solution Distribution")

# (d) Sensitivity
params = ['α', 'β', 'γ', 'δ']
impacts = [15, 8, 5, 3]
axes[1, 1].barh(params, impacts)
axes[1, 1].set_title("Parameter Impact")

save_figure(fig2, 'fig3_optimization')

# Figure 4: Sensitivity Analysis
fig3, ax3 = plot_tornado(
    param_names=["Search Radius", "Speed", "Capacity", "Start Time"],
    low_values=[85, 92, 98, 95],
    high_values=[120, 108, 103, 106],
    baseline=100,
    title="Sensitivity Analysis"
)
save_figure(fig3, 'fig4_sensitivity')

print("All figures generated!")
```

---

## 9. Troubleshooting

| Issue | Solution |
|-------|----------|
| Fonts look wrong | Run `use_mcm_style()` before any plotting |
| Colors not matching | Use `COLORS` dict instead of hardcoding |
| Figure too small/large | Use `DIMENSIONS` presets or specify `figsize` |
| Labels overlapping | Use `plt.tight_layout()` or `constrained_layout=True` |
| Legend covers data | Use `optimize_legend_location(ax, prefer_outside=True)` |
| Missing dependencies | `pip install matplotlib numpy scipy networkx seaborn` |

---

## 10. O-Award Mandatory Figure Checklist (NEW)

Based on 2024 O-Award papers, an Outstanding paper MUST contain:

### Type A (Continuous/Physics) Required Figures
1.  **Figure 1**: Problem Background (Real photo or schematic)
2.  **Figure 2**: Literature Review Comparison (Table or Chart)
3.  **Figure 3**: Workflow/Mindmap Diagram (⭐ CRITICAL)
4.  **Figure 4**: Data Distribution/Source Visualization
5.  **Figure 5+**: Model Framework Diagrams (One per model)
6.  **Figure N-2**: Sensitivity Analysis (Tornado/Spider/Heatmap)
7.  **Figure N-1**: Multi-scenario Comparison
8.  **Figure N**: Validation Results (Predicted vs Actual)

### Minimum Quantity Requirements
| Problem Type | Min Figures | Min Pages |
|--------------|-------------|-----------|
| **Type A**   | 15-20       | 22-25     |
| **Type B**   | 12-18       | 20-24     |
| **Type C**   | 18-25       | 22-25     |
| **Type D**   | 15-20       | 22-25     |
| **Type E**   | 15-20       | 20-24     |
| **Type F**   | 12-18       | 20-24     |

### Critical Visual Elements
-   **Schematics**: Don't just show data. Show *how* it works.
-   **Flowcharts**: Visualize your algorithm steps.
-   **Tables**: Use tables for Notations, Parameters, and Results Comparison.
-   **Multi-panel**: Combine related plots (e.g., 2x2 grid) to save space and show relationships.

---

*For more examples, see the `if __name__ == "__main__"` section in each template file.*
