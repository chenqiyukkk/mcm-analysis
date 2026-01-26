"""
Pareto Frontier Visualization Template for MCM Papers.
Essential for multi-objective optimization problems (Type B, D, E).

Includes support for:
- Pareto frontier highlighting
- Dominated vs non-dominated points
- Ideal and nadir point annotation
- Trade-off region shading
- Utopia point distance
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Optional, List, Union
from ..style_config import use_mcm_style, COLORS, DIMENSIONS, save_figure


def identify_pareto_front(
    x: np.ndarray,
    y: np.ndarray,
    minimize_x: bool = True,
    minimize_y: bool = True
) -> np.ndarray:
    """
    Identifies Pareto-optimal (non-dominated) points.
    
    Args:
        x: Array of objective 1 values
        y: Array of objective 2 values
        minimize_x: True if objective 1 should be minimized
        minimize_y: True if objective 2 should be minimized
    
    Returns:
        Boolean array where True indicates Pareto-optimal points
    """
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x)
    
    # Adjust signs based on optimization direction
    x_adj = x if minimize_x else -x
    y_adj = y if minimize_y else -y
    
    is_pareto = np.ones(n, dtype=bool)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Check if point j dominates point i
                if (x_adj[j] <= x_adj[i] and y_adj[j] <= y_adj[i] and 
                    (x_adj[j] < x_adj[i] or y_adj[j] < y_adj[i])):
                    is_pareto[i] = False
                    break
    
    return is_pareto


def plot_pareto_frontier(
    x: np.ndarray,
    y: np.ndarray,
    pareto_mask: Optional[np.ndarray] = None,
    minimize_x: bool = True,
    minimize_y: bool = True,
    xlabel: str = "Objective 1",
    ylabel: str = "Objective 2",
    title: str = "Pareto Frontier",
    show_ideal: bool = True,
    show_nadir: bool = True,
    connect_pareto: bool = True,
    labels: Optional[List[str]] = None,
    highlight_indices: Optional[List[int]] = None,
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a Pareto frontier visualization.
    
    Args:
        x: Array of objective 1 values
        y: Array of objective 2 values
        pareto_mask: Boolean array for Pareto points (auto-computed if None)
        minimize_x: True if objective 1 should be minimized
        minimize_y: True if objective 2 should be minimized
        xlabel: X-axis label
        ylabel: Y-axis label
        title: Chart title
        show_ideal: Show ideal point (best of both objectives)
        show_nadir: Show nadir point (worst of Pareto front)
        connect_pareto: Connect Pareto points with line
        labels: Optional labels for each point
        highlight_indices: Indices of points to highlight specially
        save_path: Path to save figure
    
    Returns:
        (fig, ax) tuple
    """
    use_mcm_style()
    
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Auto-compute Pareto front if not provided
    if pareto_mask is None:
        pareto_mask = identify_pareto_front(x, y, minimize_x, minimize_y)
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column'])
    
    # Plot dominated points (gray, smaller)
    dominated_mask = ~pareto_mask
    ax.scatter(
        x[dominated_mask], y[dominated_mask],
        c=COLORS['gray'],
        s=50,
        alpha=0.5,
        edgecolors='white',
        linewidth=0.5,
        label='Dominated Solutions',
        zorder=2
    )
    
    # Plot Pareto points (colored, larger)
    ax.scatter(
        x[pareto_mask], y[pareto_mask],
        c=COLORS['blue'],
        s=100,
        alpha=0.9,
        edgecolors='white',
        linewidth=1,
        label='Pareto-Optimal Solutions',
        zorder=3
    )
    
    # Connect Pareto points
    if connect_pareto and np.sum(pareto_mask) > 1:
        pareto_x = x[pareto_mask]
        pareto_y = y[pareto_mask]
        
        # Sort by x for proper line connection
        sort_idx = np.argsort(pareto_x)
        ax.plot(
            pareto_x[sort_idx], pareto_y[sort_idx],
            color=COLORS['blue'],
            linewidth=2,
            linestyle='-',
            alpha=0.7,
            zorder=2,
            label='_nolegend_'  # Don't add to legend
        )
    
    # Highlight specific points
    if highlight_indices:
        ax.scatter(
            x[highlight_indices], y[highlight_indices],
            c=COLORS['vermilion'],
            s=150,
            marker='*',
            edgecolors='white',
            linewidth=1,
            label='Selected Solutions',
            zorder=4
        )
    
    # Add labels to points
    if labels:
        for i, label in enumerate(labels):
            if label:
                ax.annotate(
                    label,
                    (x[i], y[i]),
                    xytext=(5, 5),
                    textcoords='offset points',
                    fontsize=8,
                    alpha=0.8
                )
    
    # Compute and show ideal point
    if show_ideal:
        ideal_x = x.min() if minimize_x else x.max()
        ideal_y = y.min() if minimize_y else y.max()
        ax.scatter(
            [ideal_x], [ideal_y],
            c=COLORS['bluish_green'],
            s=150,
            marker='D',
            edgecolors='white',
            linewidth=1.5,
            label='Ideal Point',
            zorder=5
        )
        ax.annotate(
            'Ideal',
            (ideal_x, ideal_y),
            xytext=(8, 8),
            textcoords='offset points',
            fontsize=9,
            fontweight='bold',
            color=COLORS['bluish_green']
        )
    
    # Compute and show nadir point
    if show_nadir:
        pareto_x = x[pareto_mask]
        pareto_y = y[pareto_mask]
        nadir_x = pareto_x.max() if minimize_x else pareto_x.min()
        nadir_y = pareto_y.max() if minimize_y else pareto_y.min()
        ax.scatter(
            [nadir_x], [nadir_y],
            c=COLORS['vermilion'],
            s=120,
            marker='s',
            edgecolors='white',
            linewidth=1.5,
            label='Nadir Point',
            zorder=5
        )
        ax.annotate(
            'Nadir',
            (nadir_x, nadir_y),
            xytext=(8, -8),
            textcoords='offset points',
            fontsize=9,
            fontweight='bold',
            color=COLORS['vermilion']
        )
    
    # Labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc='best', fontsize=9)
    
    # Add optimization direction arrows
    arrow_props = dict(arrowstyle='->', color='gray', lw=1.5)
    x_dir = "minimize" if minimize_x else "maximize"
    y_dir = "minimize" if minimize_y else "maximize"
    ax.annotate(
        '', 
        xy=(0.12, 0.02), 
        xytext=(0.02, 0.02),
        xycoords='axes fraction',
        arrowprops=arrow_props
    )
    ax.annotate(
        '', 
        xy=(0.02, 0.12), 
        xytext=(0.02, 0.02),
        xycoords='axes fraction',
        arrowprops=arrow_props
    )
    ax.text(0.07, 0.05, x_dir[:3], transform=ax.transAxes, fontsize=7, ha='center')
    ax.text(0.05, 0.08, y_dir[:3], transform=ax.transAxes, fontsize=7, ha='center', rotation=90)
    
    plt.tight_layout()
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


def plot_pareto_3d(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    title: str = "3D Pareto Surface",
    xlabel: str = "Objective 1",
    ylabel: str = "Objective 2",
    zlabel: str = "Objective 3",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a 3D scatter plot for three-objective optimization.
    Note: For 3+ objectives, use parallel coordinates (see below).
    """
    use_mcm_style()
    
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=DIMENSIONS['square'])
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y, z, c=COLORS['blue'], s=50, alpha=0.7)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


def plot_parallel_coordinates(
    data: np.ndarray,
    objective_names: List[str],
    pareto_mask: Optional[np.ndarray] = None,
    title: str = "Multi-Objective Trade-offs",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a parallel coordinates plot for many objectives.
    Useful when there are more than 3 objectives.
    
    Args:
        data: 2D array (n_solutions x n_objectives)
        objective_names: List of objective names
        pareto_mask: Boolean array for Pareto points
        title: Chart title
        save_path: Path to save
    
    Returns:
        (fig, ax) tuple
    """
    use_mcm_style()
    
    n_solutions, n_objectives = data.shape
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    # Normalize data to [0, 1] for each objective
    data_norm = np.zeros_like(data, dtype=float)
    for j in range(n_objectives):
        col = data[:, j]
        data_norm[:, j] = (col - col.min()) / (col.max() - col.min() + 1e-10)
    
    x_coords = np.arange(n_objectives)
    
    # Plot all solutions
    for i in range(n_solutions):
        if pareto_mask is not None and pareto_mask[i]:
            ax.plot(x_coords, data_norm[i], color=COLORS['blue'], 
                   alpha=0.7, linewidth=2)
        else:
            ax.plot(x_coords, data_norm[i], color=COLORS['gray'], 
                   alpha=0.3, linewidth=1)
    
    # Set x-ticks
    ax.set_xticks(x_coords)
    ax.set_xticklabels(objective_names, rotation=45, ha='right')
    ax.set_ylabel('Normalized Value')
    ax.set_title(title)
    
    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color=COLORS['blue'], linewidth=2, label='Pareto-Optimal'),
        Line2D([0], [0], color=COLORS['gray'], linewidth=1, alpha=0.5, label='Dominated')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Generate sample multi-objective optimization data
    np.random.seed(42)
    n = 50
    
    # Simulated trade-off: as x increases, y tends to decrease
    x = np.random.uniform(0, 10, n)
    y = 10 - x + np.random.normal(0, 1.5, n)
    y = np.clip(y, 0, 12)
    
    # Plot Pareto frontier
    fig, ax = plot_pareto_frontier(
        x, y,
        minimize_x=True,
        minimize_y=True,
        xlabel="Cost ($)",
        ylabel="Environmental Impact",
        title="Cost vs Environmental Impact Trade-off"
    )
    plt.show()
    
    # Multi-objective parallel coordinates example
    data = np.random.rand(30, 5) * 10
    pareto_mask = np.random.random(30) > 0.7
    
    fig2, ax2 = plot_parallel_coordinates(
        data,
        ["Cost", "Time", "Quality", "Risk", "Sustainability"],
        pareto_mask=pareto_mask,
        title="Multi-Objective Analysis"
    )
    plt.show()
