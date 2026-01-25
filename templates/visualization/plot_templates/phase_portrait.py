"""
Phase Portrait Visualization Template for MCM Papers (Type A).
Essential for visualizing systems of differential equations (ODEs).

Includes support for:
- Streamplots (Flow fields)
- Quiver plots (Vector fields)
- Trajectories from initial conditions
- Nullclines (Steady state analysis)
"""

import matplotlib.pyplot as plt
import numpy as np
from ..style_config import use_mcm_style, COLORS, DIMENSIONS

def plot_phase_portrait(
    dxdt_func,
    dydt_func,
    x_range,
    y_range,
    args=(),
    density=1.5,
    title="Phase Portrait",
    xlabel="State Variable X",
    ylabel="State Variable Y",
    nullclines=True,
    trajectories=None,
    save_path=None
):
    """
    Generates a professional phase portrait for a 2D system.
    
    Args:
        dxdt_func: Function f(x, y, *args) returning dx/dt
        dydt_func: Function g(x, y, *args) returning dy/dt
        x_range: Tuple (min, max) for x-axis
        y_range: Tuple (min, max) for y-axis
        args: Extra arguments to pass to the differential functions
        density: Density of stream lines
        title: Chart title
        nullclines: Boolean, whether to compute and plot nullclines (approximate)
        trajectories: List of (x0, y0) tuples for sample trajectories
        save_path: Path to save
    """
    use_mcm_style()
    
    fig, ax = plt.subplots(figsize=DIMENSIONS['single_column']) # Phase portraits often look good square-ish
    
    # Create grid
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    
    # Compute derivatives
    DX = np.zeros_like(X)
    DY = np.zeros_like(Y)
    
    # We iterate because functions might not be vectorized
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            DX[i, j] = dxdt_func(X[i, j], Y[i, j], *args)
            DY[i, j] = dydt_func(X[i, j], Y[i, j], *args)
            
    # Normalize for color mapping (speed)
    speed = np.sqrt(DX**2 + DY**2)
    lw = 1.0 # Constant linewidth usually looks cleaner for print
    
    # Plot Streamplot
    strm = ax.streamplot(
        X, Y, DX, DY,
        color=speed,
        cmap='viridis',
        linewidth=lw,
        density=density,
        arrowsize=1.0
    )
    
    # Plot Nullclines (Approximate contours where derivative is zero)
    if nullclines:
        ax.contour(X, Y, DX, levels=[0], colors=COLORS['vermilion'], linewidths=1.5, linestyles='--')
        ax.contour(X, Y, DY, levels=[0], colors=COLORS['sky_blue'], linewidths=1.5, linestyles='--')
        
    # Plot Trajectories
    if trajectories:
        from scipy.integrate import odeint
        
        def system(state, t, *p):
            x, y = state
            return [dxdt_func(x, y, *p), dydt_func(x, y, *p)]
            
        t = np.linspace(0, 50, 500) # Time horizon
        
        for p0 in trajectories:
            sol = odeint(system, p0, t, args=args)
            ax.plot(sol[:, 0], sol[:, 1], color=COLORS['black'], linewidth=1.5)
            # Mark start
            ax.plot(p0[0], p0[1], 'o', color=COLORS['black'], markersize=4)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    
    if save_path:
        plt.savefig(save_path)
        
    return fig, ax
