#!/usr/bin/env python3
"""
MCM Visualization Demo: Pareto Frontier
========================================

Detailed demonstration of multi-objective optimization visualizations:
- 2D Pareto frontier
- 3D scatter for 3 objectives
- Parallel coordinates for many objectives

Usage:
    python demo_pareto_frontier.py
"""

import sys
from pathlib import Path

skill_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(skill_root))

import numpy as np
import matplotlib.pyplot as plt

from templates.visualization import use_mcm_style, COLORS, save_figure
from templates.visualization.plot_templates import (
    plot_pareto_frontier,
    plot_pareto_3d,
    plot_parallel_coordinates,
    identify_pareto_front,
)

OUTPUT_DIR = Path(__file__).parent / "sample_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def demo_2d_pareto():
    """2D Pareto Frontier with dominated and non-dominated points."""
    print("Generating: 2D Pareto Frontier...")
    use_mcm_style()
    
    np.random.seed(123)
    n = 100
    
    # Generate points: cost vs delivery time trade-off
    cost = np.random.uniform(50, 200, n)
    # Inverse relationship with noise
    time = 300 / cost + np.random.randn(n) * 3
    time = np.clip(time, 1, 10)
    
    # Use actual function signature:
    # plot_pareto_frontier(x, y, pareto_mask=None, minimize_x=True, minimize_y=True,
    #                      xlabel, ylabel, title, show_ideal=True, show_nadir=True,
    #                      connect_pareto=True, labels=None, highlight_indices=None, save_path=None)
    fig, ax = plot_pareto_frontier(
        x=cost,
        y=time,
        xlabel="Cost ($)",
        ylabel="Delivery Time (days)",
        title="Supply Chain Optimization: Cost vs Time",
        minimize_x=True,
        minimize_y=True,
        show_ideal=True,
        show_nadir=True,
        connect_pareto=True
    )
    
    save_figure(fig, "pareto_2d_cost_time", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: pareto_2d_cost_time.png/pdf")


def demo_3d_pareto():
    """3D Pareto visualization for 3 objectives."""
    print("Generating: 3D Pareto Scatter...")
    use_mcm_style()
    
    np.random.seed(456)
    n = 200
    
    # Three objectives: cost, risk, time
    cost = np.random.uniform(10, 100, n)
    risk = 50 - 0.3 * cost + np.random.randn(n) * 10
    time = 20 + 0.1 * cost - 0.2 * risk + np.random.randn(n) * 3
    
    risk = np.clip(risk, 5, 60)
    time = np.clip(time, 5, 30)
    
    # Use actual function signature:
    # plot_pareto_3d(x, y, z, title, xlabel, ylabel, zlabel, save_path=None)
    fig, ax = plot_pareto_3d(
        x=cost,
        y=risk,
        z=time,
        xlabel="Cost ($1000)",
        ylabel="Risk Score",
        zlabel="Time (weeks)",
        title="3-Objective Optimization"
    )
    
    save_figure(fig, "pareto_3d_scatter", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: pareto_3d_scatter.png/pdf")


def demo_parallel_coordinates():
    """Parallel coordinates for multi-dimensional Pareto analysis."""
    print("Generating: Parallel Coordinates...")
    use_mcm_style()
    
    np.random.seed(789)
    n = 50
    
    # 5 objectives
    data = np.random.rand(n, 5)
    # Add some structure
    data[:, 1] = 1 - data[:, 0] + np.random.randn(n) * 0.1  # Inverse
    data[:, 2] = data[:, 0] * 0.5 + np.random.randn(n) * 0.1  # Correlated
    data = np.clip(data, 0, 1)
    
    # Note: identify_pareto_front only works for 2D, so we manually create a mask
    # For demo purposes, mark top 20% performers (lowest sum across all objectives) as Pareto
    total_scores = data.sum(axis=1)
    threshold = np.percentile(total_scores, 20)
    pareto_mask = total_scores <= threshold
    
    objective_names = ["Cost", "Quality", "Speed", "Safety", "Sustainability"]
    
    # Use actual function signature:
    # plot_parallel_coordinates(data, objective_names, pareto_mask=None, title, save_path=None)
    fig, ax = plot_parallel_coordinates(
        data=data,
        objective_names=objective_names,
        pareto_mask=pareto_mask,
        title="Multi-Objective Comparison"
    )
    
    save_figure(fig, "pareto_parallel_coords", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: pareto_parallel_coords.png/pdf")


def main():
    print("=" * 60)
    print("MCM Visualization Demo: Pareto Frontier")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    demo_2d_pareto()
    demo_3d_pareto()
    demo_parallel_coordinates()
    
    print()
    print("Done! Check sample_outputs/ for generated figures.")


if __name__ == "__main__":
    main()
