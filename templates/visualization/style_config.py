"""
Configuration module for MCM Visualization Styles.
Provides constants and helper functions for maintaining consistent
visual identity across all generated charts.
"""

import matplotlib.pyplot as plt
import os

# --- Constants ---

# Okabe-Ito Color Palette (Colorblind Safe)
COLORS = {
    'orange': '#E69F00',
    'sky_blue': '#56B4E9',
    'bluish_green': '#009E73',
    'yellow': '#F0E442',
    'blue': '#0072B2',
    'vermilion': '#D55E00',
    'reddish_purple': '#CC79A7',
    'black': '#000000'
}

# List format for iteration
COLOR_LIST = list(COLORS.values())

# Standard Dimensions (in inches)
DIMENSIONS = {
    'single_column': (3.5, 2.6),  # Aspect ratio ~ 4:3
    'double_column': (7.0, 4.5),  # Aspect ratio ~ 16:10
    'full_page': (7.0, 9.0)
}

# --- Setup Function ---

def use_mcm_style():
    """
    Applies the MCM matplotlib style sheet.
    Call this function before creating any plots.
    """
    style_path = os.path.join(os.path.dirname(__file__), 'mcm_style.mplstyle')
    if os.path.exists(style_path):
        plt.style.use(style_path)
    else:
        # Fallback if style file is missing
        print(f"Warning: Style file not found at {style_path}. Using default.")
        plt.style.use('seaborn-v0_8-whitegrid')
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=COLOR_LIST)

def get_color(name):
    """Returns hex code for a named color from the palette."""
    return COLORS.get(name, '#333333')
