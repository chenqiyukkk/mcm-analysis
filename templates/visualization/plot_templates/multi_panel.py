"""
Multi-panel Layout Template for MCM Papers.
Helps organize multiple plots into a single figure (e.g., 2x2 grid).
Essential for saving space and comparing scenarios.
"""

import matplotlib.pyplot as plt
from ..style_config import use_mcm_style, DIMENSIONS

def create_grid_layout(
    rows=2,
    cols=2,
    figsize=None,
    title="Comparative Analysis",
    save_path=None
):
    """
    Creates a pre-configured grid of subplots.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        figsize: Tuple (width, height). Defaults to double_column standard.
        title: Main figure title (Suptitle)
        save_path: Path to save
        
    Returns:
        fig: Figure object
        axes: Array of axes objects
    """
    use_mcm_style()
    
    if figsize is None:
        # Scale height based on rows, keep width fixed at double column (7")
        height = 3.5 * rows * 0.8  # slightly compressed height
        figsize = (7.0, height)
        
    fig, axes = plt.subplots(rows, cols, figsize=figsize, constrained_layout=True)
    
    fig.suptitle(title, fontsize=14, fontweight='bold')
    
    # Flatten axes array for easy iteration if it's multidimensional
    if rows > 1 and cols > 1:
        ax_flat = axes.flat
    else:
        ax_flat = [axes] if rows==1 and cols==1 else axes
        
    # Label subplots with (a), (b), (c)... standard academic style
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i, ax in enumerate(ax_flat):
        if i < len(letters):
            # Place letter label in top-left corner
            ax.text(-0.1, 1.1, f"({letters[i]})", transform=ax.transAxes, 
                    fontsize=12, fontweight='bold', va='top', ha='right')
            
    if save_path:
        # Note: Saving happens AFTER the user fills the plots
        # This function returns the objects to be filled
        pass
        
    return fig, axes

def save_multi_panel(fig, save_path):
    """
    Helper to save the multi-panel figure after plotting.
    """
    if save_path:
        fig.savefig(save_path)
        print(f"Figure saved to {save_path}")
