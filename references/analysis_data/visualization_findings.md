# Findings: O-Award Paper Visualization Analysis

## Summary Statistics
Based on the analysis of 30 O-award papers (2020-2024, Types A-F):

- **Average Figures per Paper**: 12-16 (Highest in Type C, Lowest in Type B)
- **Most Critical Visual**: The "Model Framework" Diagram (Figure 1 or 2) is universally present.
- **Color Usage**: Standard academic palettes (Blue/Orange/Grey) dominate. Rainbow colormaps are rare/avoided.

## Patterns by Problem Type

### Type A (Continuous/Physics)
- **Key Charts**: Phase Portraits, 3D Surface Plots, Time Series of State Variables.
- **Specifics**: Often visualize the solution space of differential equations. "Nullclines" and stability regions are common.
- **Template Needs**: `phase_portrait.py` is essential for stability analysis.

### Type B (Discrete/Combinatorial)
- **Key Charts**: Network Graphs, Step-by-Step Algorithm States, Gantt Charts.
- **Specifics**: Showing the *process* of an algorithm (e.g., packing, routing) is more important than just the final result.
- **Template Needs**: `network_graph.py` covers topology. Custom schematics often needed for packing/layout problems.

### Type C (Data Insights)
- **Key Charts**: Time Series Forecasts, Correlation Heatmaps, Residual Plots.
- **Specifics**: "Diagnostic Plots" (ACF/PACF, Residuals) are mandatory to prove statistical rigor.
- **Template Needs**: `time_series.py` (with CI) and `heatmap.py` (correlation) are the workhorses.

### Type D (Operations/Network)
- **Key Charts**: Network Topology, Pareto Frontiers, Sensitivity Curves.
- **Specifics**: Visualizing the trade-off between conflicting objectives (e.g., Cost vs. Efficiency) is standard.
- **Template Needs**: `network_graph.py` for structure, `multi_panel.py` for scenario comparison.

### Type E (Sustainability)
- **Key Charts**: Geo-Maps, Radar Charts, System Dynamics Diagrams.
- **Specifics**: Multi-indicator assessment requires Radar/Spider charts or comprehensive Dashboards.
- **Template Needs**: `heatmap.py` (for grid data) and `multi_panel.py` (for indicators).

### Type F (Policy)
- **Key Charts**: Framework Diagrams, Stakeholder Maps, Logic Trees.
- **Specifics**: Visualizing abstract concepts (Policy A vs Policy B) and their impact on stakeholders.
- **Template Needs**: `network_graph.py` (for hierarchies) and schematic tools.

## Design Best Practices Observed
1.  **Multi-panel Figures**: Almost all O-award papers use (a)(b)(c)(d) subplots to save space and facilitate comparison.
2.  **Dual-Axis**: Frequently used in Type C/A to show relationships between variables with different scales.
3.  **Schematic Integration**: Mathematical results are often overlaid on schematic diagrams (e.g., a graph overlaid on a map).

## Next Steps for Skill Development
1.  **Schematic Generation**: While Python templates handle data plots, "Process Diagrams" (Type B/F) need generative AI support (`scientific-schematics`).
2.  **Geospatial Support**: Type E/D often need map overlays. Future: Integrate `geopandas` or simple image overlay templates.
