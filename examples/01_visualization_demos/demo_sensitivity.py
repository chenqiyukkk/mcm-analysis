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
    param_names = [
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
    low_values = np.array([1250, 1320, 1380, 1420, 1450, 1480, 1485, 1490])
    high_values = np.array([1820, 1700, 1650, 1600, 1560, 1530, 1520, 1515])
    
    # Use actual function signature:
    # plot_tornado(param_names, low_values, high_values, baseline=0.0,
    #              xlabel, title, show_values=True, sort_by_impact=True,
    #              perturbation_label="±10%", save_path=None)
    fig, ax = plot_tornado(
        param_names=param_names,
        low_values=low_values,
        high_values=high_values,
        baseline=baseline,
        title="NPV Sensitivity Analysis (±20% Parameter Variation)",
        xlabel="Net Present Value ($1000)",
        perturbation_label="±20%"
    )
    
    save_figure(fig, "sensitivity_tornado", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: sensitivity_tornado.png/pdf")


def demo_spider():
    """Spider plot showing sensitivity curves."""
    print("Generating: Spider Plot...")
    use_mcm_style()
    
    # Define parameter names
    param_names = ["Interest Rate", "Material Cost", "Labor Cost", "Demand", "Price"]
    
    # Baseline values for each parameter
    baseline_params = np.array([0.05, 100, 50, 1000, 25])
    baseline_output = 500  # Baseline profit
    
    # Define test ranges for each parameter (80% to 120% of baseline)
    param_values = []
    output_values = []
    
    # Sensitivities (output change per unit param change)
    sensitivities = [-0.8, -0.5, -0.3, 0.6, 0.9]
    
    for i, (base_val, sens) in enumerate(zip(baseline_params, sensitivities)):
        # Test from 80% to 120% of baseline
        test_vals = np.linspace(base_val * 0.8, base_val * 1.2, 9)
        # Calculate output: baseline + sensitivity * (param_change_fraction * 100)
        param_change_pct = (test_vals - base_val) / base_val * 100
        outputs = baseline_output + sens * param_change_pct * 5  # Scale factor
        
        param_values.append(test_vals)
        output_values.append(outputs)
    
    # Use actual function signature:
    # plot_sensitivity_spider(param_names, param_values, output_values,
    #                         baseline_params, baseline_output,
    #                         xlabel, ylabel, title, save_path=None)
    fig, ax = plot_sensitivity_spider(
        param_names=param_names,
        param_values=param_values,
        output_values=output_values,
        baseline_params=baseline_params,
        baseline_output=baseline_output,
        title="One-at-a-Time Sensitivity Analysis",
        xlabel="Parameter Value (% of baseline)",
        ylabel="Profit ($1000)"
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
    np.random.seed(42)
    NPV = 10 - 50 * IR + 30 * DG + 0.5 * np.random.randn(*IR.shape)
    
    # Use actual function signature:
    # plot_sensitivity_heatmap(param1_name, param2_name, param1_values, param2_values,
    #                          output_matrix, title, output_label, save_path=None)
    fig, ax = plot_sensitivity_heatmap(
        param1_name="Interest Rate (%)",
        param2_name="Demand Growth (%)",
        param1_values=interest_rates * 100,  # Convert to percentage
        param2_values=demand_growth * 100,
        output_matrix=NPV,
        title="NPV Response to Parameter Combinations",
        output_label="NPV ($M)"
    )
    
    save_figure(fig, "sensitivity_heatmap", OUTPUT_DIR)
    plt.close(fig)
    print("  Saved: sensitivity_heatmap.png/pdf")


def demo_summary_table():
    """Generate markdown summary table."""
    print("Generating: Summary Table...")
    
    param_names = ["Interest Rate", "Material Cost", "Labor Cost", "Demand", "Price"]
    baseline = 1500
    
    # Low and high output values when parameters varied ±10%
    low_values = np.array([1380, 1420, 1450, 1550, 1620])
    high_values = np.array([1620, 1580, 1550, 1450, 1380])
    
    # Use actual function signature:
    # create_sensitivity_summary_table(param_names, low_values, high_values,
    #                                   baseline, perturbation="±10%")
    table = create_sensitivity_summary_table(
        param_names=param_names,
        low_values=low_values,
        high_values=high_values,
        baseline=baseline,
        perturbation="±10%"
    )
    
    # Save as markdown file
    table_path = OUTPUT_DIR / "sensitivity_summary_table.md"
    table_path.write_text(table, encoding="utf-8")
    print(f"  Saved: {table_path.name}")


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
