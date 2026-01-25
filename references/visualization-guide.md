# MCM Visualization Guide

A comprehensive guide to selecting and designing O-award quality figures for MCM/ICM competitions.

## 1. The "Golden Rules" of O-Award Figures

Based on analysis of 2020-2024 Outstanding Papers:

1.  **Start with a Schematic**: The first figure in your paper should almost *always* be a visual flowchart or framework diagram explaining your model logic.
2.  **Verify, Don't Just Display**: Use charts to *prove* your model works (e.g., Residual Plots, Prediction vs. Actual, Sensitivity Analysis).
3.  **Space Efficiency**: Use Multi-panel layouts (2x2 grid) to show multiple scenarios in one figure. Never waste a whole page on a simple line chart.
4.  **Consistency**: Use the same font (Arial/Helvetica), size (10pt), and color palette (Okabe-Ito) throughout the entire paper.

## 2. Recommended Charts by Problem Type

| Problem Type | Core Visualizations | Recommended Template |
|--------------|---------------------|----------------------|
| **A (Continuous)** | **Phase Portraits**, Streamplots, 3D Surfaces, Time Series | `phase_portrait.py`, `time_series.py` |
| **B (Discrete)** | **Network Graphs**, State Transition Diagrams, Algorithm Flowcharts | `network_graph.py`, `heatmap.py` (grid states) |
| **C (Data)** | **Correlation Heatmaps**, Time Series Forecasts, Residual Plots, Confusion Matrices | `heatmap.py`, `time_series.py` |
| **D (Network)** | **Topology Maps**, Flow Diagrams, Pareto Frontiers, Sensitivity Curves | `network_graph.py` |
| **E (Environment)** | **Geo-Maps**, Radar Charts, System Dynamics (Stock-Flow), Sensitivity Fans | `heatmap.py` (spatial), `multi_panel.py` |
| **F (Policy)** | **Framework Diagrams**, Gantt Charts, Stakeholder Maps (Radar), Logic Trees | `multi_panel.py`, `network_graph.py` (trees) |

## 3. Visualization Toolkit Usage

### Step 1: Setup Style
Always import the MCM style configuration at the start of your code.
```python
from templates.visualization.style_config import use_mcm_style
use_mcm_style()
```

### Step 2: Choose Your Template

#### For Time Series & Forecasts (Type A, C, E)
Use `plot_templates/time_series.py`.
- **Features**: Confidence intervals (shaded bands), Dual-axis support.
- **When to use**: Predicting future trends, comparing model output to history.

#### For Dynamic Systems (Type A)
Use `plot_templates/phase_portrait.py`.
- **Features**: Streamlines, nullclines, trajectory simulation.
- **When to use**: Analyzing stability of differential equations (e.g., Predator-Prey, Infectious Disease models).

#### For Correlations & Matrices (Type C)
Use `plot_templates/heatmap.py`.
- **Features**: Annotated correlation matrices, Confusion matrices.
- **When to use**: Exploratory Data Analysis (EDA), Model performance evaluation.

#### For Networks & Hierarchies (Type B, D, F)
Use `plot_templates/network_graph.py`.
- **Features**: Node-link diagrams, Tree layouts.
- **When to use**: Visualizing logistics networks, decision trees, AHP hierarchies.

#### For Comparisons (All Types)
Use `plot_templates/multi_panel.py`.
- **Features**: Pre-configured 2x2 or 3x2 grids with (a), (b) labeling.
- **When to use**: Comparing 4 different scenarios, showing model results alongside residuals.

## 4. Design Patterns & Tips

### Color Palette (Okabe-Ito)
Safe for colorblindness and print-friendly.
- **Primary Data**: Blue (`#0072B2`) or Orange (`#E69F00`)
- **Secondary/Compare**: Sky Blue (`#56B4E9`) or Vermilion (`#D55E00`)
- **Highlight**: Yellow (`#F0E442`)

### Layout
- **Single Column**: Width 3.5 inches. Use for simple scatter plots or confusion matrices.
- **Double Column**: Width 7.0 inches. Use for time series, large networks, or multi-panel grids.

### Captions
- Place titles **below** the figure (in LaTeX), but you can include a top title in the chart for drafting.
- Use descriptive captions: "Figure 1: Evolution of the System State. (a) Phase portrait showing stability. (b) Time series of variable X."

## 5. Beyond Python: External Tools
For diagrams that are hard to code (Flowcharts, System Dynamics):
- Use the **`scientific-schematics`** skill.
- Prompt: "Generate a system dynamics flowchart for a predator-prey model with delay."
