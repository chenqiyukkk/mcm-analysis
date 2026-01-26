"""
MCM Visualization Plot Templates Package
=========================================

Import all plot templates from here for convenience:

>>> from templates.visualization.plot_templates import (
...     plot_forecast,
...     plot_pareto_frontier,
...     create_grid_layout,
... )

Or import specific modules:

>>> from templates.visualization.plot_templates import time_series
>>> fig, ax = time_series.plot_forecast(...)
"""

# Time Series
from .time_series import (
    plot_forecast,
    plot_dual_axis,
)

# Heatmaps
from .heatmap import (
    plot_correlation_matrix,
    plot_confusion_matrix,
    plot_spatial_heatmap,
)

# Multi-panel layouts
from .multi_panel import (
    create_grid_layout,
    create_asymmetric_layout,
    create_comparison_panel,
    save_multi_panel,
)

# Phase portraits (Type A)
from .phase_portrait import (
    plot_phase_portrait,
)

# Network graphs (Type B, D, F)
from .network_graph import (
    plot_network_topology,
    plot_tree_hierarchy,
)

# Pareto frontier (Multi-objective)
from .pareto_frontier import (
    plot_pareto_frontier,
    plot_pareto_3d,
    plot_parallel_coordinates,
    identify_pareto_front,
)

# Sensitivity analysis
from .sensitivity_tornado import (
    plot_tornado,
    plot_sensitivity_spider,
    plot_sensitivity_heatmap,
    create_sensitivity_summary_table,
)


__all__ = [
    # Time Series
    "plot_forecast",
    "plot_dual_axis",
    
    # Heatmaps
    "plot_correlation_matrix",
    "plot_confusion_matrix",
    "plot_spatial_heatmap",
    
    # Multi-panel
    "create_grid_layout",
    "create_asymmetric_layout",
    "create_comparison_panel",
    "save_multi_panel",
    
    # Phase portrait
    "plot_phase_portrait",
    
    # Network
    "plot_network_topology",
    "plot_tree_hierarchy",
    
    # Pareto
    "plot_pareto_frontier",
    "plot_pareto_3d",
    "plot_parallel_coordinates",
    "identify_pareto_front",
    
    # Sensitivity
    "plot_tornado",
    "plot_sensitivity_spider",
    "plot_sensitivity_heatmap",
    "create_sensitivity_summary_table",
]
