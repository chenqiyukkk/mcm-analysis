"""
Time Series Visualization Template for MCM Papers.
Includes support for:
- Historical data + Forecasts
- Confidence intervals
- Residual analysis (optional subplot)
- Dual-axis (e.g., Price vs Volume)
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Optional, Tuple, Union, List
from ..style_config import use_mcm_style, COLORS, DIMENSIONS, save_figure

def plot_forecast(
    dates: Union[List, np.ndarray],
    y_history: Union[List, np.ndarray],
    y_forecast: Optional[Union[List, np.ndarray]] = None,
    y_ci_lower: Optional[Union[List, np.ndarray]] = None,
    y_ci_upper: Optional[Union[List, np.ndarray]] = None,
    title: str = "Time Series Forecast",
    xlabel: str = "Time",
    ylabel: str = "Value",
    label_history: str = "Historical Data",
    label_forecast: str = "Forecast",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generates a standard MCM forecast plot with confidence intervals.
    
    Args:
        dates: Array-like of datetime objects or x-axis values
        y_history: Array-like of historical values (aligned with start of dates)
        y_forecast: Array-like of forecast values (aligned with end of dates)
        y_ci_lower: Array-like, lower bound of confidence interval
        y_ci_upper: Array-like, upper bound of confidence interval
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label
        save_path: If provided, saves the figure to this path
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    # Plot History
    # Assuming dates covers the whole range, we split based on lengths
    len_hist = len(y_history)
    dates_hist = dates[:len_hist]
    
    ax.plot(dates_hist, y_history, label=label_history, 
            color=COLORS['black'], linestyle='-', marker='o', markersize=3, alpha=0.7)
            
    # Plot Forecast
    if y_forecast is not None:
        dates_forecast = dates[len_hist-1:] # Overlap one point to connect lines
        # Prepend last history point to forecast to make it continuous
        y_forecast_plot = np.concatenate(([y_history[-1]], y_forecast))
        
        ax.plot(dates_forecast, y_forecast_plot, label=label_forecast,
                color=COLORS['vermilion'], linestyle='--', linewidth=2)
                
        # Plot Confidence Interval
        if y_ci_lower is not None and y_ci_upper is not None:
            # Adjust CI lengths to match forecast dates (excluding the connecting point)
            # This logic assumes CIs are provided just for the forecast part
            ax.fill_between(dates[len_hist:], y_ci_lower, y_ci_upper,
                            color=COLORS['vermilion'], alpha=0.2, label='95% Confidence Interval')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    
    if save_path:
        save_figure(fig, save_path)
        
    return fig, ax

def plot_dual_axis(
    x: Union[List, np.ndarray],
    y1: Union[List, np.ndarray],
    y2: Union[List, np.ndarray],
    label1: str = "Metric 1",
    label2: str = "Metric 2",
    title: str = "Dual Axis Analysis",
    xlabel: str = "Time",
    ylabel1: str = "Value 1",
    ylabel2: str = "Value 2",
    save_path: Optional[str] = None
) -> Tuple[plt.Figure, Tuple[plt.Axes, plt.Axes]]:
    """
    Generates a dual-axis time series plot.
    Useful for showing correlation between two scales (e.g., Price vs Volume).
    """
    use_mcm_style()
    
    fig, ax1 = plt.subplots(figsize=DIMENSIONS['double_column'])
    
    color1 = COLORS['blue']
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1, color=color1)
    ax1.plot(x, y1, color=color1, label=label1)
    ax1.tick_params(axis='y', labelcolor=color1)
    
    ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
    
    color2 = COLORS['orange']
    ax2.set_ylabel(ylabel2, color=color2)
    ax2.plot(x, y2, color=color2, linestyle='--', label=label2)
    ax2.tick_params(axis='y', labelcolor=color2)
    
    ax1.set_title(title)
    
    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    if save_path:
        save_figure(fig, save_path)
        
    return fig, (ax1, ax2)
