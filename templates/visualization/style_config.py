"""
Configuration module for MCM Visualization Styles.
Provides constants and helper functions for maintaining consistent
visual identity across all generated charts.

v1.2.0 - Added subplot labels, legend optimization, save utilities
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from typing import List, Tuple, Optional, Union

# =============================================================================
# Constants
# =============================================================================

# Okabe-Ito Color Palette (Colorblind Safe)
# Reordered: Blue first (primary), then Orange (secondary), etc.
COLORS = {
    'blue': '#0072B2',
    'orange': '#E69F00',
    'bluish_green': '#009E73',
    'vermilion': '#D55E00',
    'reddish_purple': '#CC79A7',
    'sky_blue': '#56B4E9',
    'yellow': '#F0E442',
    'black': '#000000',
    'gray': '#999999',
}

# List format for iteration (matches axes.prop_cycle order)
COLOR_LIST = [
    '#0072B2',  # Blue
    '#E69F00',  # Orange
    '#009E73',  # Bluish Green
    '#D55E00',  # Vermilion
    '#CC79A7',  # Reddish Purple
    '#56B4E9',  # Sky Blue
    '#F0E442',  # Yellow
]

# Standard Dimensions (in inches)
DIMENSIONS = {
    'single_column': (3.5, 2.8),   # ~4:3 aspect, for 1-column journals
    'double_column': (7.0, 4.5),   # ~16:10 aspect, MCM standard
    'square': (5.0, 5.0),          # For phase portraits, networks
    'full_page': (7.0, 9.0),       # For multi-panel with many rows
}

# Subplot label alphabet
SUBPLOT_LABELS = list('abcdefghijklmnopqrstuvwxyz')


# =============================================================================
# Setup Functions
# =============================================================================

def use_mcm_style():
    """
    Applies the MCM matplotlib style sheet.
    Call this function before creating any plots.
    """
    style_path = Path(__file__).parent / 'mcm_style.mplstyle'
    if style_path.exists():
        plt.style.use(str(style_path))
    else:
        # Fallback if style file is missing
        print(f"Warning: Style file not found at {style_path}. Using defaults.")
        plt.style.use('seaborn-v0_8-whitegrid')
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=COLOR_LIST)


def get_color(name: str) -> str:
    """Returns hex code for a named color from the palette."""
    return COLORS.get(name, '#333333')


def get_colors(n: int) -> List[str]:
    """Returns first n colors from the palette, cycling if needed."""
    return [COLOR_LIST[i % len(COLOR_LIST)] for i in range(n)]


# =============================================================================
# Subplot Labeling
# =============================================================================

def add_subplot_labels(
    axes: Union[np.ndarray, list, plt.Axes],
    style: str = 'parentheses',
    fontsize: int = 12,
    fontweight: str = 'bold',
    loc: str = 'upper_left',
    offset: Tuple[float, float] = (-0.1, 1.05)
):
    """
    Adds automatic labels (a), (b), (c)... to subplot axes.
    
    Args:
        axes: Array of axes objects or single axes
        style: 'parentheses' for (a), 'plain' for a, 'caps' for (A)
        fontsize: Label font size
        fontweight: 'bold' or 'normal'
        loc: Position - 'upper_left', 'upper_right', 'lower_left', 'lower_right'
        offset: (x, y) offset in axes coordinates
    
    Returns:
        List of text objects created
    """
    # Flatten axes if needed
    if isinstance(axes, np.ndarray):
        ax_list = axes.flat
    elif isinstance(axes, list):
        ax_list = axes
    else:
        ax_list = [axes]
    
    # Format function
    def format_label(idx):
        letter = SUBPLOT_LABELS[idx] if idx < len(SUBPLOT_LABELS) else str(idx)
        if style == 'parentheses':
            return f'({letter})'
        elif style == 'caps':
            return f'({letter.upper()})'
        else:
            return letter
    
    # Position mapping
    positions = {
        'upper_left': (-0.1, 1.05),
        'upper_right': (1.05, 1.05),
        'lower_left': (-0.1, -0.1),
        'lower_right': (1.05, -0.1),
    }
    x, y = positions.get(loc, offset)
    
    ha = 'right' if 'left' in loc else 'left'
    va = 'bottom' if 'upper' in loc else 'top'
    
    texts = []
    for i, ax in enumerate(ax_list):
        t = ax.text(
            x, y, format_label(i),
            transform=ax.transAxes,
            fontsize=fontsize,
            fontweight=fontweight,
            ha=ha,
            va=va
        )
        texts.append(t)
    
    return texts


# =============================================================================
# Legend Optimization
# =============================================================================

def optimize_legend_location(
    ax: plt.Axes,
    handles=None,
    labels=None,
    prefer_outside: bool = False,
    **kwargs
) -> plt.legend:
    """
    Places legend in optimal position, avoiding data overlap.
    
    Args:
        ax: Matplotlib axes
        handles: Legend handles (optional, uses ax defaults)
        labels: Legend labels (optional)
        prefer_outside: If True, places legend outside plot area
        **kwargs: Additional legend kwargs
    
    Returns:
        Legend object
    """
    if prefer_outside:
        # Place outside on the right
        legend = ax.legend(
            handles=handles,
            labels=labels,
            loc='center left',
            bbox_to_anchor=(1.02, 0.5),
            frameon=True,
            **kwargs
        )
    else:
        # Use matplotlib's best location algorithm
        legend = ax.legend(
            handles=handles,
            labels=labels,
            loc='best',
            frameon=True,
            **kwargs
        )
    
    return legend


# =============================================================================
# LaTeX Helpers
# =============================================================================

def latex_label(text: str) -> str:
    """
    Wraps text in LaTeX math mode if it contains special characters.
    For use with mathtext (no system LaTeX required).
    
    Examples:
        latex_label("x^2") -> "$x^2$"
        latex_label("Regular text") -> "Regular text"
    """
    math_chars = ['^', '_', '\\', '{', '}', 'frac', 'sqrt', 'sum', 'int']
    if any(char in text for char in math_chars):
        if not text.startswith('$'):
            return f'${text}$'
    return text


def format_scientific(value: float, precision: int = 2) -> str:
    """
    Formats a number in scientific notation for LaTeX labels.
    
    Examples:
        format_scientific(0.00123) -> "$1.23 \\times 10^{-3}$"
    """
    if value == 0:
        return "0"
    
    exp = int(np.floor(np.log10(abs(value))))
    mantissa = value / (10 ** exp)
    
    if exp == 0:
        return f"{value:.{precision}f}"
    else:
        return f"${mantissa:.{precision}f} \\times 10^{{{exp}}}$"


# =============================================================================
# Save Utilities
# =============================================================================

def save_figure(
    fig: plt.Figure,
    name: str,
    output_dir: Optional[Path] = None,
    formats: List[str] = ['png', 'pdf'],
    dpi: int = 300,
    transparent: bool = False
) -> List[Path]:
    """
    Saves figure in multiple formats.
    
    Args:
        fig: Matplotlib figure object
        name: Base filename (without extension)
        output_dir: Directory to save to (default: current directory)
        formats: List of formats ['png', 'pdf', 'svg']
        dpi: Resolution for raster formats
        transparent: Whether background is transparent
    
    Returns:
        List of saved file paths
    """
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    saved_paths = []
    for fmt in formats:
        filepath = output_dir / f"{name}.{fmt}"
        fig.savefig(
            filepath,
            format=fmt,
            dpi=dpi if fmt != 'pdf' else None,
            transparent=transparent,
            bbox_inches='tight',
            pad_inches=0.1
        )
        saved_paths.append(filepath)
        print(f"Saved: {filepath}")
    
    return saved_paths


# =============================================================================
# Quick Setup for Scripts
# =============================================================================

def setup_figure(
    size: str = 'double_column',
    nrows: int = 1,
    ncols: int = 1,
    **kwargs
) -> Tuple[plt.Figure, Union[plt.Axes, np.ndarray]]:
    """
    Convenience function to create a figure with MCM style applied.
    
    Args:
        size: 'single_column', 'double_column', 'square', or 'full_page'
        nrows: Number of subplot rows
        ncols: Number of subplot columns
        **kwargs: Additional plt.subplots kwargs
    
    Returns:
        (fig, axes) tuple
    """
    use_mcm_style()
    
    figsize = DIMENSIONS.get(size, DIMENSIONS['double_column'])
    
    # Adjust height for multiple rows
    if nrows > 1:
        figsize = (figsize[0], figsize[1] * nrows * 0.7)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    
    return fig, axes


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Demo: Create a simple plot with all features
    use_mcm_style()
    
    fig, axes = plt.subplots(1, 2, figsize=DIMENSIONS['double_column'])
    
    # Plot some data
    x = np.linspace(0, 10, 50)
    for i, ax in enumerate(axes):
        for j in range(3):
            ax.plot(x, np.sin(x + j), color=COLOR_LIST[j], label=f'Series {j+1}')
        ax.set_xlabel(latex_label('Time (s)'))
        ax.set_ylabel(latex_label('y = sin(x)'))
        optimize_legend_location(ax)
    
    # Add subplot labels
    add_subplot_labels(axes)
    
    plt.tight_layout()
    plt.show()
