"""
Sensitivity Analysis Tornado Diagram Template for MCM Papers.
Essential for presenting parameter sensitivity results (All problem types).

Includes support for:
- Horizontal tornado charts (parameter impact)
- Symmetric/asymmetric impact visualization
- Automatic parameter ranking by impact
- Baseline reference line
- Percentage annotations
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Optional, List, Union
from ..style_config import use_mcm_style, COLORS, DIMENSIONS, save_figure


def plot_tornado(
    param_names: List[str],
    low_values: np.ndarray,
    high_values: np.ndarray,
    baseline: float = 0.0,
    xlabel: str = "Impact on Output",
    title: str = "Sensitivity Analysis - Tornado Diagram",
    show_values: bool = True,
    sort_by_impact: bool = True,
    perturbation_label: str = "±10%",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a tornado diagram for sensitivity analysis.
    
    Args:
        param_names: List of parameter names
        low_values: Output values when parameters are at low end
        high_values: Output values when parameters are at high end
        baseline: Baseline/reference output value
        xlabel: X-axis label
        title: Chart title
        show_values: Show numeric values on bars
        sort_by_impact: Sort parameters by total impact
        perturbation_label: Label describing the perturbation (e.g., "±10%")
        save_path: Path to save figure
    
    Returns:
        (fig, ax) tuple
    """
    use_mcm_style()
    
    param_names = list(param_names)
    low_values = np.asarray(low_values)
    high_values = np.asarray(high_values)
    
    # Calculate impacts relative to baseline
    low_impact = low_values - baseline
    high_impact = high_values - baseline
    
    # Total impact for sorting
    total_impact = np.abs(low_impact) + np.abs(high_impact)
    
    # Sort by total impact if requested
    if sort_by_impact:
        sort_idx = np.argsort(total_impact)[::-1]  # Descending
        param_names = [param_names[i] for i in sort_idx]
        low_impact = low_impact[sort_idx]
        high_impact = high_impact[sort_idx]
        total_impact = total_impact[sort_idx]
    
    n_params = len(param_names)
    y_pos = np.arange(n_params)
    
    # Figure sizing
    height = max(4, n_params * 0.5)
    fig, ax = plt.subplots(figsize=(7, height))
    
    # Plot bars
    # Low impact bars (extend left if negative)
    bars_low = ax.barh(
        y_pos, low_impact,
        height=0.4,
        left=0,
        color=COLORS['sky_blue'],
        alpha=0.85,
        edgecolor='white',
        linewidth=1,
        label=f'Low ({perturbation_label.split("±")[0]}−)'
    )
    
    # High impact bars (extend right if positive)
    bars_high = ax.barh(
        y_pos, high_impact,
        height=0.4,
        left=0,
        color=COLORS['vermilion'],
        alpha=0.85,
        edgecolor='white',
        linewidth=1,
        label=f'High ({perturbation_label.split("±")[0]}+)'
    )
    
    # Add value annotations
    if show_values:
        for i, (low, high) in enumerate(zip(low_impact, high_impact)):
            # Low value annotation
            if abs(low) > 0.001:
                x_pos = low - 0.02 * np.sign(low) * ax.get_xlim()[1]
                ha = 'right' if low < 0 else 'left'
                ax.text(
                    low, i, f'{low:+.2f}',
                    ha=ha, va='center', fontsize=8,
                    color='white' if abs(low) > total_impact.max() * 0.3 else 'black'
                )
            
            # High value annotation
            if abs(high) > 0.001:
                x_pos = high + 0.02 * np.sign(high) * ax.get_xlim()[1]
                ha = 'left' if high > 0 else 'right'
                ax.text(
                    high, i, f'{high:+.2f}',
                    ha=ha, va='center', fontsize=8,
                    color='white' if abs(high) > total_impact.max() * 0.3 else 'black'
                )
    
    # Baseline reference line
    ax.axvline(x=0, color='black', linewidth=1.5, linestyle='-', zorder=1)
    
    # Y-axis labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(param_names)
    
    # Labels and title
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    
    # Legend
    ax.legend(loc='lower right', fontsize=9)
    
    # Invert y-axis so most impactful is on top
    ax.invert_yaxis()
    
    # Grid for x-axis only
    ax.xaxis.grid(True, alpha=0.3)
    ax.yaxis.grid(False)
    
    plt.tight_layout()
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


def plot_sensitivity_spider(
    param_names: List[str],
    param_values: List[np.ndarray],
    output_values: List[np.ndarray],
    baseline_params: np.ndarray,
    baseline_output: float,
    xlabel: str = "Parameter Value (% of baseline)",
    ylabel: str = "Output Value",
    title: str = "One-at-a-Time Sensitivity Analysis",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a spider/web plot showing how output changes as each parameter varies.
    
    Args:
        param_names: List of parameter names
        param_values: List of arrays, each containing test values for one parameter
        output_values: List of arrays, each containing output values for parameter tests
        baseline_params: Array of baseline parameter values
        baseline_output: Baseline output value
        xlabel: X-axis label
        ylabel: Y-axis label
        title: Chart title
        save_path: Path to save figure
    
    Returns:
        (fig, ax) tuple
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    colors = [COLORS['blue'], COLORS['orange'], COLORS['bluish_green'],
              COLORS['vermilion'], COLORS['reddish_purple'], COLORS['sky_blue']]
    
    for i, (name, pvals, ovals) in enumerate(zip(param_names, param_values, output_values)):
        # Normalize parameter values to percentage of baseline
        baseline_val = baseline_params[i] if hasattr(baseline_params, '__len__') else baseline_params
        if baseline_val != 0:
            pvals_norm = (pvals / baseline_val) * 100
        else:
            pvals_norm = pvals * 100
        
        color = colors[i % len(colors)]
        ax.plot(pvals_norm, ovals, color=color, linewidth=2, 
               marker='o', markersize=5, label=name)
    
    # Baseline reference lines
    ax.axhline(y=baseline_output, color='gray', linestyle='--', 
               linewidth=1, alpha=0.7, label='Baseline Output')
    ax.axvline(x=100, color='gray', linestyle='--', 
               linewidth=1, alpha=0.7)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc='best', fontsize=9)
    
    plt.tight_layout()
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


def plot_sensitivity_heatmap(
    param1_name: str,
    param2_name: str,
    param1_values: np.ndarray,
    param2_values: np.ndarray,
    output_matrix: np.ndarray,
    title: str = "Two-Parameter Sensitivity",
    output_label: str = "Output Value",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a heatmap showing sensitivity to two parameters simultaneously.
    
    Args:
        param1_name: Name of parameter 1 (x-axis)
        param2_name: Name of parameter 2 (y-axis)
        param1_values: Array of parameter 1 test values
        param2_values: Array of parameter 2 test values
        output_matrix: 2D array of output values (rows=param2, cols=param1)
        title: Chart title
        output_label: Colorbar label
        save_path: Path to save figure
    
    Returns:
        (fig, ax) tuple
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column'])
    
    im = ax.imshow(
        output_matrix, 
        cmap='RdYlBu_r', 
        aspect='auto',
        origin='lower'
    )
    
    # Set tick labels
    n1, n2 = len(param1_values), len(param2_values)
    ax.set_xticks(np.linspace(0, n1-1, min(5, n1)).astype(int))
    ax.set_yticks(np.linspace(0, n2-1, min(5, n2)).astype(int))
    ax.set_xticklabels([f'{param1_values[i]:.2g}' for i in np.linspace(0, n1-1, min(5, n1)).astype(int)])
    ax.set_yticklabels([f'{param2_values[i]:.2g}' for i in np.linspace(0, n2-1, min(5, n2)).astype(int)])
    
    ax.set_xlabel(param1_name)
    ax.set_ylabel(param2_name)
    ax.set_title(title)
    
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label(output_label)
    
    plt.tight_layout()
    
    if save_path:
        save_figure(fig, save_path.replace('.png', '').replace('.pdf', ''))
    
    return fig, ax


def create_sensitivity_summary_table(
    param_names: List[str],
    low_values: np.ndarray,
    high_values: np.ndarray,
    baseline: float,
    perturbation: str = "±10%"
) -> str:
    """
    Creates a formatted summary table for sensitivity analysis results.
    Useful for including in papers or reports.
    
    Returns:
        Markdown-formatted table string
    """
    low_impact = np.asarray(low_values) - baseline
    high_impact = np.asarray(high_values) - baseline
    total_impact = np.abs(low_impact) + np.abs(high_impact)
    
    # Sort by total impact
    sort_idx = np.argsort(total_impact)[::-1]
    
    lines = [
        f"| Parameter | Low Impact | High Impact | Total Range | Sensitivity Rank |",
        f"|-----------|------------|-------------|-------------|------------------|"
    ]
    
    for rank, i in enumerate(sort_idx, 1):
        lines.append(
            f"| {param_names[i]} | {low_impact[i]:+.3f} | {high_impact[i]:+.3f} | "
            f"{total_impact[i]:.3f} | {rank} |"
        )
    
    return "\n".join(lines)


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Example: Tornado diagram
    params = [
        "Growth Rate (r)",
        "Carrying Capacity (K)", 
        "Initial Population",
        "Mortality Rate",
        "Migration Rate",
        "Reproduction Rate"
    ]
    
    # Simulated sensitivity results (output values at ±10% perturbation)
    baseline = 100
    np.random.seed(42)
    
    # Low values (parameter decreased by 10%)
    low = baseline + np.random.uniform(-20, -2, len(params))
    # High values (parameter increased by 10%)  
    high = baseline + np.random.uniform(2, 25, len(params))
    
    fig, ax = plot_tornado(
        params, low, high,
        baseline=baseline,
        xlabel="Population Change (%)",
        title="Sensitivity Analysis: Population Model"
    )
    plt.show()
    
    # Print summary table
    table = create_sensitivity_summary_table(params, low, high, baseline)
    print("\nSensitivity Summary:")
    print(table)
