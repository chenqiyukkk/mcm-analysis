#!/usr/bin/env python3
"""
MCM Visualization Demo: All Plot Types
=======================================

This script demonstrates all 7 visualization templates available in the
MCM-Analysis skill. Run this to generate sample figures.

Usage:
    python demo_all_plots.py

Output:
    All figures saved to ./sample_outputs/
"""

import sys
from pathlib import Path

# Add parent directories to path for imports
skill_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(skill_root))

import numpy as np
import matplotlib.pyplot as plt

# Import MCM visualization tools
from templates.visualization import (
    use_mcm_style,
    COLORS,
    COLOR_LIST,
    DIMENSIONS,
    save_figure,
    add_subplot_labels,
)

from templates.visualization.plot_templates import (
    # Time series
    plot_forecast,
    plot_dual_axis,
    # Heatmaps
    plot_correlation_matrix,
    plot_confusion_matrix,
    # Multi-panel
    create_grid_layout,
    # Phase portrait
    plot_phase_portrait,
    # Network
    plot_network_topology,
    # Pareto
    plot_pareto_frontier,
    # Sensitivity
    plot_tornado,
)

# Output directory
OUTPUT_DIR = Path(__file__).parent / "sample_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def demo_time_series():
    """Demo 1: Time Series Forecast Plot"""
    print("Generating: Time Series Forecast...")
    
    use_mcm_style()
    
    # Generate sample data
    np.random.seed(42)
    n_historical = 50
    n_forecast = 20
    
    # Create full date range
    dates = np.arange(n_historical + n_forecast)
    
    # Historical data
    y_history = 100 + np.cumsum(np.random.randn(n_historical) * 2)
    
    # Forecast data
    y_forecast = np.cumsum(np.random.randn(n_forecast) * 2)
    y_ci_lower = y_forecast - np.linspace(5, 15, n_forecast)
    y_ci_upper = y_forecast + np.linspace(5, 15, n_forecast)
    
    fig, ax = plot_forecast(
        dates=dates,
        y_history=y_history,
        y_forecast=y_forecast,
        y_ci_lower=y_ci_lower,
        y_ci_upper=y_ci_upper,
        title="Stock Price Prediction",
        xlabel="Trading Days",
        ylabel="Price ($)"
    )
    
    save_figure(fig, "01_time_series_forecast", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 01_time_series_forecast.png/pdf")


def demo_heatmap():
    """Demo 2: Correlation Heatmap"""
    print("Generating: Correlation Heatmap...")
    
    use_mcm_style()
    
    # Generate sample correlation matrix
    np.random.seed(42)
    n_vars = 8
    data = np.random.randn(100, n_vars)
    # Add some correlations
    data[:, 1] = data[:, 0] * 0.8 + np.random.randn(100) * 0.4
    data[:, 3] = data[:, 2] * -0.6 + np.random.randn(100) * 0.5
    
    corr_matrix = np.corrcoef(data.T)
    labels = [f"Var_{i+1}" for i in range(n_vars)]
    
    fig, ax = plot_correlation_matrix(
        data=corr_matrix,
        features=labels,
        title="Variable Correlation Analysis"
    )
    
    save_figure(fig, "02_correlation_heatmap", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 02_correlation_heatmap.png/pdf")


def demo_phase_portrait():
    """Demo 3: Phase Portrait for Dynamic Systems"""
    print("Generating: Phase Portrait...")
    
    use_mcm_style()
    
    # Lotka-Volterra predator-prey model
    # dx/dt = alpha*x - beta*x*y
    # dy/dt = delta*x*y - gamma*y
    alpha, beta, delta, gamma = 1.1, 0.4, 0.1, 0.4
    
    def dxdt(x, y):
        return alpha * x - beta * x * y
    
    def dydt(x, y):
        return delta * x * y - gamma * y
    
    fig, ax = plot_phase_portrait(
        dxdt_func=dxdt,
        dydt_func=dydt,
        x_range=(0, 5),
        y_range=(0, 5),
        title="Predator-Prey Dynamics",
        xlabel="Prey Population",
        ylabel="Predator Population",
        density=1.5
    )
    
    save_figure(fig, "03_phase_portrait", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 03_phase_portrait.png/pdf")


def demo_network():
    """Demo 4: Network Topology"""
    print("Generating: Network Graph...")
    
    use_mcm_style()
    
    # Create sample network
    import networkx as nx
    
    G = nx.karate_club_graph()
    
    fig, ax = plot_network_topology(
        G=G,
        title="Social Network Structure",
        layout_algorithm='spring'
    )
    
    save_figure(fig, "04_network_graph", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 04_network_graph.png/pdf")


def demo_pareto():
    """Demo 5: Pareto Frontier"""
    print("Generating: Pareto Frontier...")
    
    use_mcm_style()
    
    # Generate sample multi-objective data
    np.random.seed(42)
    n_points = 50
    
    # Create Pareto-like distribution
    cost = np.random.uniform(10, 100, n_points)
    # Risk inversely related to cost with noise
    risk = 100 - 0.7 * cost + np.random.randn(n_points) * 10
    risk = np.clip(risk, 5, 95)
    
    fig, ax = plot_pareto_frontier(
        x=cost,
        y=risk,
        xlabel="Cost ($1000)",
        ylabel="Risk Score",
        title="Cost vs Risk Trade-off Analysis",
        minimize_x=True,
        minimize_y=True
    )
    
    save_figure(fig, "05_pareto_frontier", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 05_pareto_frontier.png/pdf")


def demo_tornado():
    """Demo 6: Sensitivity Tornado Diagram"""
    print("Generating: Tornado Diagram...")
    
    use_mcm_style()
    
    # Sample sensitivity data
    param_names = [
        "Interest Rate",
        "Material Cost",
        "Labor Cost",
        "Energy Price",
        "Demand Growth",
        "Tax Rate"
    ]
    
    baseline = 100  # Baseline NPV
    low_values = np.array([85, 88, 92, 95, 97, 98])   # NPV at -10% parameter
    high_values = np.array([118, 115, 110, 106, 103, 102])  # NPV at +10% parameter
    
    fig, ax = plot_tornado(
        param_names=param_names,
        low_values=low_values,
        high_values=high_values,
        baseline=baseline,
        title="NPV Sensitivity Analysis",
        xlabel="Net Present Value ($M)"
    )
    
    save_figure(fig, "06_tornado_diagram", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 06_tornado_diagram.png/pdf")


def demo_multi_panel():
    """Demo 7: Multi-Panel Layout"""
    print("Generating: Multi-Panel Figure...")
    
    use_mcm_style()
    
    # Create 2x2 grid layout
    fig, axes = create_grid_layout(
        nrows=2,
        ncols=2,
        suptitle="Data Analysis Pipeline"
    )
    
    # Plot sample data in each panel
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    
    # Panel (a): Raw data
    y_raw = np.sin(x) + np.random.randn(100) * 0.3
    axes[0, 0].scatter(x, y_raw, alpha=0.5, c=COLORS['blue'], s=10)
    axes[0, 0].set_xlabel("Time")
    axes[0, 0].set_ylabel("Signal")
    axes[0, 0].set_title("Raw Data")
    
    # Panel (b): Smoothed
    from scipy.ndimage import gaussian_filter1d
    y_smooth = gaussian_filter1d(y_raw, sigma=3)
    axes[0, 1].plot(x, y_smooth, color=COLORS['orange'], linewidth=2)
    axes[0, 1].set_xlabel("Time")
    axes[0, 1].set_ylabel("Smoothed Signal")
    axes[0, 1].set_title("Processed")
    
    # Panel (c): Model fit
    axes[1, 0].scatter(x, y_raw, alpha=0.3, c=COLORS['gray'], s=10, label='Data')
    axes[1, 0].plot(x, np.sin(x), color=COLORS['vermilion'], linewidth=2, label='Model')
    axes[1, 0].set_xlabel("Time")
    axes[1, 0].set_ylabel("Signal")
    axes[1, 0].set_title("Model Fit")
    axes[1, 0].legend()
    
    # Panel (d): Residuals
    residuals = y_raw - np.sin(x)
    axes[1, 1].hist(residuals, bins=20, color=COLORS['bluish_green'], edgecolor='white')
    axes[1, 1].axvline(0, color='black', linestyle='--', alpha=0.5)
    axes[1, 1].set_xlabel("Residual")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].set_title("Residuals")
    
    plt.tight_layout()
    save_figure(fig, "07_multi_panel", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: 07_multi_panel.png/pdf")


def main():
    """Run all demos."""
    print("=" * 60)
    print("MCM Visualization Demo: Generating All Plot Types")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    demos = [
        demo_time_series,
        demo_heatmap,
        demo_phase_portrait,
        demo_network,
        demo_pareto,
        demo_tornado,
        demo_multi_panel,
    ]
    
    success_count = 0
    for demo_func in demos:
        try:
            demo_func()
            success_count += 1
        except Exception as e:
            print(f"  Error in {demo_func.__name__}: {e}")
    
    print()
    print("=" * 60)
    print(f"Completed: {success_count}/{len(demos)} demos successful")
    print(f"Check {OUTPUT_DIR} for outputs.")
    print("=" * 60)


if __name__ == "__main__":
    main()
