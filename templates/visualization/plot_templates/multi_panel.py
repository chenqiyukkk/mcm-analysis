"""
Multi-panel Layout Template for MCM Papers.
Helps organize multiple plots into a single figure (e.g., 2x2 grid).
Essential for saving space and comparing scenarios.

v1.2.0 - Enhanced with automatic labeling and flexible layouts
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Union, Optional, List
from ..style_config import (
    use_mcm_style, 
    DIMENSIONS, 
    add_subplot_labels,
    save_figure
)


def create_grid_layout(
    nrows: int = 2,
    ncols: int = 2,
    figsize: Optional[Tuple[float, float]] = None,
    suptitle: str = "",
    sharex: bool = False,
    sharey: bool = False,
    add_labels: bool = True,
    label_style: str = 'parentheses',
    wspace: float = 0.3,
    hspace: float = 0.35,
) -> Tuple[plt.Figure, np.ndarray]:
    """
    Creates a pre-configured grid of subplots with automatic labeling.
    
    Args:
        nrows: Number of rows
        ncols: Number of columns
        figsize: Tuple (width, height). Auto-calculated if None.
        suptitle: Main figure title (optional)
        sharex: Share x-axis across columns
        sharey: Share y-axis across rows
        add_labels: Automatically add (a), (b), (c) labels
        label_style: 'parentheses', 'plain', or 'caps'
        wspace: Width spacing between subplots
        hspace: Height spacing between subplots
        
    Returns:
        fig: Figure object
        axes: 2D array of axes objects (even for 1D layouts)
    """
    use_mcm_style()
    
    if figsize is None:
        # Smart sizing: 3.5" per column, 2.5" per row
        width = min(7.0, 3.5 * ncols)
        height = 2.5 * nrows
        figsize = (width, height)
    
    fig, axes = plt.subplots(
        nrows, ncols, 
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        squeeze=False  # Always return 2D array
    )
    
    # Adjust spacing
    fig.subplots_adjust(wspace=wspace, hspace=hspace)
    
    # Add suptitle if provided
    if suptitle:
        fig.suptitle(suptitle, fontsize=14, fontweight='bold', y=1.02)
    
    # Add subplot labels
    if add_labels:
        add_subplot_labels(axes, style=label_style)
    
    return fig, axes


def create_asymmetric_layout(
    layout: List[List[int]],
    figsize: Optional[Tuple[float, float]] = None,
    suptitle: str = "",
    add_labels: bool = True,
) -> Tuple[plt.Figure, dict]:
    """
    Creates an asymmetric subplot layout using GridSpec.
    
    Args:
        layout: 2D list defining subplot spans.
                Example: [[1, 1, 2],
                          [3, 3, 2]] 
                Creates: (a) top-left half, (b) right column spanning 2 rows,
                         (c) bottom-left half
        figsize: Figure size
        suptitle: Main title
        add_labels: Add (a), (b), (c) labels
    
    Returns:
        fig: Figure object
        axes_dict: Dictionary mapping subplot number to axes
    """
    use_mcm_style()
    
    layout = np.array(layout)
    nrows, ncols = layout.shape
    
    if figsize is None:
        figsize = DIMENSIONS['double_column']
    
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(nrows, ncols, wspace=0.3, hspace=0.35)
    
    axes_dict = {}
    processed = set()
    
    for subplot_num in np.unique(layout):
        if subplot_num in processed:
            continue
        
        # Find extent of this subplot
        rows, cols = np.where(layout == subplot_num)
        row_slice = slice(rows.min(), rows.max() + 1)
        col_slice = slice(cols.min(), cols.max() + 1)
        
        ax = fig.add_subplot(gs[row_slice, col_slice])
        axes_dict[subplot_num] = ax
        processed.add(subplot_num)
    
    # Add suptitle
    if suptitle:
        fig.suptitle(suptitle, fontsize=14, fontweight='bold', y=1.02)
    
    # Add labels
    if add_labels:
        sorted_axes = [axes_dict[k] for k in sorted(axes_dict.keys())]
        add_subplot_labels(sorted_axes)
    
    return fig, axes_dict


def create_comparison_panel(
    titles: List[str],
    ncols: int = 2,
    figsize: Optional[Tuple[float, float]] = None,
    suptitle: str = "Comparative Analysis",
) -> Tuple[plt.Figure, np.ndarray]:
    """
    Creates a comparison panel with pre-set titles for each subplot.
    Useful for comparing scenarios, sensitivity analyses, etc.
    
    Args:
        titles: List of subplot titles
        ncols: Number of columns
        figsize: Figure size
        suptitle: Main figure title
    
    Returns:
        fig: Figure object
        axes: Array of axes objects
    """
    n_plots = len(titles)
    nrows = int(np.ceil(n_plots / ncols))
    
    fig, axes = create_grid_layout(
        nrows=nrows,
        ncols=ncols,
        figsize=figsize,
        suptitle=suptitle,
        add_labels=True
    )
    
    # Set titles and hide unused axes
    axes_flat = axes.flatten()
    for i, ax in enumerate(axes_flat):
        if i < len(titles):
            ax.set_title(titles[i], fontsize=11)
        else:
            ax.set_visible(False)
    
    return fig, axes


def save_multi_panel(
    fig: plt.Figure, 
    name: str,
    output_dir: Optional[str] = None,
    formats: List[str] = ['png', 'pdf']
) -> List[str]:
    """
    Helper to save the multi-panel figure after plotting.
    
    Args:
        fig: Figure object
        name: Base filename
        output_dir: Output directory (default: current)
        formats: List of output formats
    
    Returns:
        List of saved file paths
    """
    return save_figure(fig, name, output_dir, formats)


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    import numpy as np
    
    # Example 1: Standard 2x2 grid
    fig, axes = create_grid_layout(2, 2, suptitle="Model Results Comparison")
    
    x = np.linspace(0, 10, 50)
    
    axes[0, 0].plot(x, np.sin(x))
    axes[0, 0].set_title("Scenario 1")
    
    axes[0, 1].plot(x, np.cos(x))
    axes[0, 1].set_title("Scenario 2")
    
    axes[1, 0].plot(x, np.sin(2*x))
    axes[1, 0].set_title("Scenario 3")
    
    axes[1, 1].plot(x, np.cos(2*x))
    axes[1, 1].set_title("Scenario 4")
    
    plt.tight_layout()
    plt.show()
    
    # Example 2: Asymmetric layout
    layout = [
        [1, 1, 2],
        [3, 4, 2]
    ]
    fig2, axes_dict = create_asymmetric_layout(
        layout, 
        suptitle="Asymmetric Layout Example"
    )
    
    axes_dict[1].set_title("Wide plot")
    axes_dict[2].set_title("Tall plot")
    axes_dict[3].set_title("Small 1")
    axes_dict[4].set_title("Small 2")
    
    plt.tight_layout()
    plt.show()
