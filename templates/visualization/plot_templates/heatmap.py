"""
Heatmap and Matrix Visualization Template for MCM Papers.
Includes support for:
- Correlation Matrices
- Confusion Matrices (Model Performance)
- Spatial/Grid Heatmaps (2D Data)
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from ..style_config import use_mcm_style, COLORS, DIMENSIONS

def plot_correlation_matrix(
    data,
    features=None,
    title="Correlation Matrix",
    cmap="RdBu_r",
    save_path=None
):
    """
    Generates a professional correlation matrix heatmap.
    
    Args:
        data: DataFrame or correlation matrix (numpy array)
        features: List of feature names (if data is numpy array)
        title: Chart title
        cmap: Colormap (diverging usually best for correlation)
        save_path: Path to save
    """
    use_mcm_style()
    
    # Calculate correlation if passed a DataFrame that isn't already a matrix
    if hasattr(data, 'corr') and data.shape[0] > data.shape[1]: 
        corr = data.corr()
    else:
        corr = data
        
    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column']) # Square-ish often better
    
    # Mask upper triangle for cleaner look (common in academic papers)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    sns.heatmap(
        corr,
        mask=mask,
        cmap=cmap,
        vmax=1, vmin=-1,
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .7},
        annot=True,     # Show numbers
        fmt=".2f",      # 2 decimal places
        annot_kws={"size": 8},
        ax=ax
    )
    
    ax.set_title(title)
    
    if save_path:
        plt.savefig(save_path)
        print(f"Figure saved to {save_path}")
        
    return fig, ax

def plot_confusion_matrix(
    cm,
    classes,
    title='Confusion Matrix',
    cmap='Blues',
    normalize=False,
    save_path=None
):
    """
    Generates a confusion matrix for classification results.
    """
    use_mcm_style()
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fmt = '.2f'
    else:
        fmt = 'd'

    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column'])
    
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax, shrink=0.7)
    
    # Show all ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True Label',
           xlabel='Predicted Label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    
    if save_path:
        plt.savefig(save_path)
    
    return fig, ax

def plot_spatial_heatmap(
    data_grid,
    xlabel="X Coordinate",
    ylabel="Y Coordinate",
    title="Spatial Distribution",
    cmap="viridis",
    save_path=None
):
    """
    Generates a spatial heatmap (e.g., for Type A physics or Type E environment).
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    im = ax.imshow(data_grid, cmap=cmap, origin='lower', aspect='auto')
    cbar = ax.figure.colorbar(im, ax=ax)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Turn off grid for images as it can look messy
    ax.grid(False)
    
    if save_path:
        plt.savefig(save_path)
        
    return fig, ax
