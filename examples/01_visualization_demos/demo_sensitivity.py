#!/usr/bin/env python3
"""
MCM Visualization Demo: Sensitivity Analysis
=============================================

Demonstrates sensitivity analysis visualizations:
- Tornado diagram (one-at-a-time sensitivity)
- Spider plot (parameter variation curves)
- Sensitivity heatmap (two-parameter interaction)

Usage:
    python demo_sensitivity.py
"""

import sys
from pathlib import Path

skill_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(skill_root))

import numpy as np
import matplotlib.pyplot as plt

from templates.visualization import use_mcm_style, COLORS, save_figure
from templates.visualization.plot_templates import (
    plot_tornado,
    plot_sensitivity_spider,
    plot_sensitivity_heatmap,
    create_sensitivity_summary_table,
)

OUTPUT_DIR = Path(__file__).parent / "sample_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def demo_tornado():
    """Tornado diagram showing parameter importance."""
    print("Generating: Tornado Diagram...")
    use_mcm_style()
    
    # Economic model sensitivity parameters
    parameters = [
        "Discount Rate",
        "Initial Investment",
        "Operating Cost",
        "Revenue Growth",
        "Tax Rate",
        "Salvage Value",
        "Inflation Rate",
        "Market Share"
    ]
    
    baseline = 1500  # Baseline NPV in $1000
    
    # Impact at -20% and +20% parameter variation
    low_values = [1250, 1320, 1380, 1420, 1450, 1480, 1485, 1490]
    high_values = [1820, 1700, 1650, 1600, 1560, 1530, 1520, 1515]
    
    fig, ax = plot_tornado(
        parameters=parameters,
        low_values=low_values,
        high_values=high_values,
        baseline=baseline,
        title="NPV Sensitivity Analysis (±20% Parameter Variation)",
        xlabel="Net Present Value ($1000)",
        variation_label="±20% change"
    )
    
    save_figure(fig, "sensitivity_tornado", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: sensitivity_tornado.png/pdf")


def demo_spider():
    """Spider plot showing sensitivity curves."""
    print("Generating: Spider Plot...")
    use_mcm_style()
    
    # Define parameter variation range
    variation_pct = np.linspace(-30, 30, 13)  # -30% to +30%
    
    # Parameter responses (percentage change in output)
    parameters = {
        "Interest Rate": -0.8 * variation_pct,  # High negative sensitivity
        "Material Cost": -0.5 * variation_pct,
        "Labor Cost": -0.3 * variation_pct,
        "Demand": 0.6 * variation_pct,  # Positive sensitivity
        "Price": 0.9 * variation_pct,  # Highest positive sensitivity
    }
    
    fig, ax = plot_sensitivity_spider(
        variation_range=variation_pct,
        parameter_responses=parameters,
        title="One-at-a-Time Sensitivity Analysis",
        xlabel="Parameter Change (%)",
        ylabel="Output Change (%)"
    )
    
    save_figure(fig, "sensitivity_spider", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: sensitivity_spider.png/pdf")


def demo_heatmap():
    """Sensitivity heatmap for two-parameter interaction."""
    print("Generating: Sensitivity Heatmap...")
    use_mcm_style()
    
    # Two parameters: Interest Rate and Demand Growth
    interest_rates = np.linspace(0.02, 0.10, 9)  # 2% to 10%
    demand_growth = np.linspace(-0.05, 0.15, 11)  # -5% to 15%
    
    # Create output matrix (NPV in $M)
    IR, DG = np.meshgrid(interest_rates, demand_growth)
    # NPV decreases with interest rate, increases with demand
    NPV = 10 - 50 * IR + 30 * DG + 5 * np.random.randn(*IR.shape) * 0.1
    
    fig, ax = plot_sensitivity_heatmap(
        x_values=interest_rates * 100,  # Convert to percentage
        y_values=demand_growth * 100,
        z_values=NPV,
        xlabel="Interest Rate (%)",
        ylabel="Demand Growth (%)",
        title="NPV Response to Parameter Combinations",
        colorbar_label="NPV ($M)"
    )
    
    save_figure(fig, "sensitivity_heatmap", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: sensitivity_heatmap.png/pdf")


def demo_summary_table():
    """Generate markdown summary table."""
    print("Generating: Summary Table...")
    
    parameters = ["Interest Rate", "Material Cost", "Labor Cost", "Demand", "Price"]
    baseline_values = [0.05, 100, 50, 1000, 25]
    sensitivities = [-0.8, -0.5, -0.3, 0.6, 0.9]
    
    table = create_sensitivity_summary_table(
        parameters=parameters,
        baseline_values=baseline_values,
        sensitivities=sensitivities,
        units=["fraction", "$", "$", "units", "$"]
    )
    
    # Save as markdown file
    table_path = OUTPUT_DIR / "sensitivity_summary_table.md"
    table_path.write_text(table, encoding="utf-8")
    print(f"  Saved: {table_path}")


def main():
    print("=" * 60)
    print("MCM Visualization Demo: Sensitivity Analysis")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    demo_tornado()
    demo_spider()
    demo_heatmap()
    demo_summary_table()
    
    print()
    print("Done! Check sample_outputs/ for generated figures.")


if __name__ == "__main__":
    main()
