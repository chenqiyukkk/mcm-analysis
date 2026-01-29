"""
MCM/ICM Flowchart Generator
Creates O-Award quality workflow diagrams and model frameworks using NetworkX and Matplotlib.
No external binary dependencies (like Graphviz) required.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Union

# Try to import style_config, but fallback if not found (for standalone testing)
try:
    from ..style_config import use_mcm_style, COLORS, save_figure
except ImportError:
    # Minimal fallback style
    COLORS = {
        'blue': '#0072B2',
        'orange': '#E69F00',
        'green': '#009E73',
        'gray': '#999999',
        'black': '#000000',
        'white': '#FFFFFF'
    }
    def use_mcm_style():
        plt.style.use('seaborn-v0_8-whitegrid')
    def save_figure(fig, name, output_dir=Path('.')):
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / f"{name}.png", dpi=300, bbox_inches='tight')
        print(f"Saved to {output_dir}/{name}.png")

def plot_workflow(
    steps: List[str],
    title: str = "Our Work Framework",
    output_name: str = "workflow"
) -> plt.Figure:
    """
    Creates a linear vertical flowchart for the overall methodology.
    
    Args:
        steps: List of strings describing each major step
        title: Figure title
        output_name: Filename for saving
        
    Returns:
        Matplotlib figure object
    """
    use_mcm_style()
    
    n_steps = len(steps)
    fig, ax = plt.subplots(figsize=(8, n_steps * 1.5))
    
    # Coordinate system: x in [0, 1], y in [0, n_steps]
    # Top step at y = n_steps - 0.5, Bottom at y = 0.5
    
    box_width = 0.6
    box_height = 0.8
    
    for i, step in enumerate(steps):
        # Calculate center y (from top to bottom)
        y = n_steps - 1 - i
        
        # Draw box
        # FancyBboxPatch for rounded corners
        box = patches.FancyBboxPatch(
            (0.5 - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.1",
            ec=COLORS['blue'],
            fc='white',
            linewidth=2,
            zorder=2
        )
        ax.add_patch(box)
        
        # Add text
        ax.text(
            0.5, y, step,
            ha='center', va='center',
            fontsize=12,
            fontweight='bold' if i == 0 else 'normal',
            wrap=True,
            zorder=3
        )
        
        # Draw arrow to next step (except for last one)
        if i < n_steps - 1:
            arrow = patches.FancyArrowPatch(
                (0.5, y - box_height/2),
                (0.5, y - 1 + box_height/2),
                arrowstyle='->',
                mutation_scale=20,
                color=COLORS['gray'],
                linewidth=2,
                zorder=1
            )
            ax.add_patch(arrow)
            
    # Set plot limits and clean up
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, n_steps - 0.5)
    ax.axis('off')
    ax.set_title(title, fontsize=14, pad=20)
    
    return fig

def plot_model_framework(
    inputs: List[str],
    process: str,
    outputs: List[str],
    title: str = "Model Framework"
) -> plt.Figure:
    """
    Creates a Input -> Process -> Output diagram for a specific model.
    
    Args:
        inputs: List of input variables/data
        process: Description of the core model/algorithm
        outputs: List of output variables/results
        
    Returns:
        Matplotlib figure object
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Layout: Inputs (Left) -> Process (Center) -> Outputs (Right)
    
    # Draw Process (Central Box)
    process_box = patches.FancyBboxPatch(
        (0.35, 0.3), 0.3, 0.4,
        boxstyle="round,pad=0.05",
        ec=COLORS['blue'],
        fc='#E6F3FF',  # Light blue
        linewidth=2
    )
    ax.add_patch(process_box)
    ax.text(0.5, 0.5, process, ha='center', va='center', fontsize=12, fontweight='bold', wrap=True)
    
    # Draw Inputs (Left Nodes)
    for i, inp in enumerate(inputs):
        y = 0.8 - i * (0.6 / max(1, len(inputs) - 1)) if len(inputs) > 1 else 0.5
        
        # Box
        box = patches.FancyBboxPatch(
            (0.05, y - 0.05), 0.2, 0.1,
            boxstyle="square,pad=0.02",
            ec=COLORS['green'],
            fc='white',
            linewidth=1.5
        )
        ax.add_patch(box)
        ax.text(0.15, y, inp, ha='center', va='center', fontsize=10)
        
        # Arrow
        arrow = patches.FancyArrowPatch(
            (0.25, y), (0.35, 0.5),  # To center box edge? Simplify: to box edge
            posA=(0,0), posB=(0,0),
            path=None,
            arrowstyle='->',
            connectionstyle="arc3,rad=0.1",
            color=COLORS['gray']
        )
        # Simple straight line for now, fancy arrows are tricky without connectionstyle tuning
        ax.annotate("",
            xy=(0.35, 0.5), xycoords='data',
            xytext=(0.25, y), textcoords='data',
            arrowprops=dict(arrowstyle="->", color=COLORS['gray'], lw=1.5)
        )

    # Draw Outputs (Right Nodes)
    for i, out in enumerate(outputs):
        y = 0.8 - i * (0.6 / max(1, len(outputs) - 1)) if len(outputs) > 1 else 0.5
        
        # Box
        box = patches.FancyBboxPatch(
            (0.75, y - 0.05), 0.2, 0.1,
            boxstyle="square,pad=0.02",
            ec=COLORS['orange'],
            fc='white',
            linewidth=1.5
        )
        ax.add_patch(box)
        ax.text(0.85, y, out, ha='center', va='center', fontsize=10)
        
        # Arrow from Process
        ax.annotate("",
            xy=(0.75, y), xycoords='data',
            xytext=(0.65, 0.5), textcoords='data',
            arrowprops=dict(arrowstyle="->", color=COLORS['gray'], lw=1.5)
        )
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title(title, fontsize=14)
    
    return fig

def plot_complex_flowchart(
    nodes: Dict[str, Tuple[float, float]],
    edges: List[Tuple[str, str]],
    node_labels: Optional[Dict[str, str]] = None,
    title: str = "Complex Flow"
) -> plt.Figure:
    """
    General purpose flowchart using NetworkX for layout.
    """
    use_mcm_style()
    
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node)
    G.add_edges_from(edges)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw nodes
    for node, (x, y) in nodes.items():
        label = node_labels.get(node, node) if node_labels else node
        
        box = patches.FancyBboxPatch(
            (x - 0.1, y - 0.05), 0.2, 0.1,
            boxstyle="round,pad=0.02",
            ec=COLORS['blue'],
            fc='white',
            linewidth=1.5
        )
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=10, wrap=True)
        
    # Draw edges
    for u, v in edges:
        start = nodes[u]
        end = nodes[v]
        
        ax.annotate("",
            xy=end, xycoords='data',
            xytext=start, textcoords='data',
            arrowprops=dict(arrowstyle="->", color='black', lw=1.5, shrinkA=15, shrinkB=15)
        )
        
    ax.set_xlim(min(x for x, y in nodes.values()) - 0.2, max(x for x, y in nodes.values()) + 0.2)
    ax.set_ylim(min(y for x, y in nodes.values()) - 0.2, max(y for x, y in nodes.values()) + 0.2)
    ax.axis('off')
    ax.set_title(title)
    
    return fig

if __name__ == "__main__":
    # Demo 1: Linear Workflow
    steps = [
        "Problem Analysis & Data Preprocessing",
        "Model I: Time Series Forecasting",
        "Model II: Optimization Algorithm",
        "Sensitivity Analysis",
        "Policy Recommendations"
    ]
    fig1 = plot_workflow(steps)
    save_figure(fig1, "demo_workflow")
    
    # Demo 2: Model Framework
    inputs = ["Historical Data", "Weather Params", "Economic Index"]
    outputs = ["Future Demand", "Confidence Interval"]
    fig2 = plot_model_framework(inputs, "LSTM Neural Network", outputs)
    save_figure(fig2, "demo_model_framework")
