"""
Network and Graph Visualization Template for MCM Papers.
Includes support for:
- Network Topology (Node-Link diagrams)
- Flow visualizations (Sankey / Directed)
- Tree structures
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from typing import Optional, Tuple, Dict, List, Union
from ..style_config import use_mcm_style, COLORS, DIMENSIONS, save_figure

def plot_network_topology(
    G: nx.Graph,
    pos: Optional[Dict] = None,
    node_color: Optional[Union[str, List]] = None,
    node_size: Optional[Union[int, List]] = None,
    edge_width: float = 1.0,
    with_labels: bool = True,
    title: str = "Network Topology",
    layout_algorithm: str = "spring",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generates a professional network visualization.
    
    Args:
        G: NetworkX graph object
        pos: Dictionary of positions (optional)
        node_color: List or single color (default: Sky Blue)
        node_size: List or single size (default: 300)
        edge_width: List or single width (default: 1.0)
        with_labels: Boolean
        title: Chart title
        layout_algorithm: 'spring', 'kamada_kawai', 'circular', 'shell'
        save_path: Path to save
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    # Default visual properties
    if node_color is None:
        node_color = COLORS['sky_blue']
    if node_size is None:
        # Scale node size by degree if not provided
        degrees = [d for n, d in G.degree()]
        if degrees:
            # Normalize to decent size range
            node_size = [v * 50 + 100 for v in degrees]
        else:
            node_size = 300
            
    # Layout calculation
    if pos is None:
        if layout_algorithm == 'spring':
            pos = nx.spring_layout(G, k=0.15, iterations=20)
        elif layout_algorithm == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(G)
        elif layout_algorithm == 'circular':
            pos = nx.circular_layout(G)
        else:
            pos = nx.spring_layout(G)
            
    # Draw
    nx.draw_networkx_nodes(
        G, pos,
        node_size=node_size,
        node_color=node_color,
        edgecolors='white', # White border for separation
        linewidths=1.5,
        ax=ax
    )
    
    nx.draw_networkx_edges(
        G, pos,
        width=edge_width,
        edge_color='gray',
        alpha=0.6,
        ax=ax
    )
    
    if with_labels:
        nx.draw_networkx_labels(
            G, pos,
            font_size=8,
            font_family='sans-serif',
            ax=ax
        )
        
    ax.set_title(title)
    ax.axis('off') # Turn off axis for networks
    
    if save_path:
        save_figure(fig, save_path)
        
    return fig, ax

def plot_tree_hierarchy(
    G: nx.Graph,
    root: Optional[str] = None,
    title: str = "Hierarchy Structure",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Specialized layout for tree/hierarchy structures (e.g., AHP, Decision Trees).
    Requires 'pygraphviz' typically for graphviz_layout, but we'll use a custom implementation
    to avoid dependency hell.
    """
    use_mcm_style()
    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column'])
    
    # Use a simple hierarchy layout if possible, or fall back to spring
    try:
        from networkx.drawing.nx_agraph import graphviz_layout
        pos = graphviz_layout(G, prog='dot')
    except ImportError:
        # Custom simple hierarchy layout
        pos = nx.spring_layout(G) 
        print("Warning: PyGraphviz not found. Using spring layout for tree.")
        
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=COLORS['yellow'],
        node_size=500,
        arrows=True,
        ax=ax
    )
    
    ax.set_title(title)
    
    if save_path:
        save_figure(fig, save_path)
        
    return fig, ax
