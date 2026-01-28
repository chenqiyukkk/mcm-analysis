"""
MCM/ICM Visualization Templates Package
========================================

A comprehensive collection of publication-quality visualization tools
for Mathematical Contest in Modeling papers.

Quick Start
-----------
>>> from templates.visualization import use_mcm_style, COLORS
>>> use_mcm_style()  # Apply MCM style to all plots

>>> from templates.visualization.plot_templates import (
...     plot_forecast,
...     plot_pareto_frontier,
...     plot_tornado,
...     create_grid_layout,
... )

Available Modules
-----------------
style_config : Core styling and utilities
    - use_mcm_style() : Apply publication style
    - COLORS : Okabe-Ito color palette dict
    - COLOR_LIST : Color palette as list
    - DIMENSIONS : Standard figure sizes
    - add_subplot_labels() : Add (a), (b), (c) labels
    - optimize_legend_location() : Smart legend placement
    - save_figure() : Save in multiple formats

plot_templates.time_series : Time series and forecasts
    - plot_forecast() : Historical + forecast with CI
    - plot_dual_axis() : Two y-axes comparison

plot_templates.heatmap : Heatmaps and matrices
    - plot_correlation_matrix() : Correlation heatmap
    - plot_confusion_matrix() : Classification results
    - plot_spatial_heatmap() : 2D spatial data

plot_templates.multi_panel : Multi-subplot layouts
    - create_grid_layout() : nxm subplot grid
    - create_asymmetric_layout() : Custom GridSpec layout
    - create_comparison_panel() : Pre-titled comparison grid

plot_templates.phase_portrait : Dynamic systems (Type A)
    - plot_phase_portrait() : Streamplot with nullclines

plot_templates.network_graph : Networks (Type B, D, F)
    - plot_network_topology() : Node-link diagrams
    - plot_tree_hierarchy() : Tree/hierarchy layouts

plot_templates.pareto_frontier : Multi-objective optimization
    - plot_pareto_frontier() : 2D Pareto front
    - plot_pareto_3d() : 3D scatter for 3 objectives
    - plot_parallel_coordinates() : Many objectives
    - identify_pareto_front() : Find non-dominated points

plot_templates.sensitivity_tornado : Sensitivity analysis
    - plot_tornado() : Tornado diagram
    - plot_sensitivity_spider() : One-at-a-time curves
    - plot_sensitivity_heatmap() : Two-parameter sensitivity
    - create_sensitivity_summary_table() : Markdown table

Version
-------
v1.2.1 - January 2026
"""

# Version
__version__ = "1.2.1"

# Core exports from style_config
from .style_config import (
    use_mcm_style,
    COLORS,
    COLOR_LIST,
    DIMENSIONS,
    get_color,
    get_colors,
    add_subplot_labels,
    optimize_legend_location,
    latex_label,
    format_scientific,
    save_figure,
    setup_figure,
)

# Convenience re-exports from plot_templates
# These are imported lazily to avoid import errors if dependencies missing

def _lazy_import(module_name, func_name):
    """Lazy import helper to handle missing dependencies gracefully."""
    def wrapper(*args, **kwargs):
        try:
            module = __import__(
                f"templates.visualization.plot_templates.{module_name}",
                fromlist=[func_name]
            )
            func = getattr(module, func_name)
            return func(*args, **kwargs)
        except ImportError as e:
            raise ImportError(
                f"Could not import {func_name} from {module_name}. "
                f"Make sure required dependencies are installed: {e}"
            )
    return wrapper


# All public exports
__all__ = [
    # Version
    "__version__",
    
    # Style config
    "use_mcm_style",
    "COLORS",
    "COLOR_LIST", 
    "DIMENSIONS",
    "get_color",
    "get_colors",
    "add_subplot_labels",
    "optimize_legend_location",
    "latex_label",
    "format_scientific",
    "save_figure",
    "setup_figure",
]
