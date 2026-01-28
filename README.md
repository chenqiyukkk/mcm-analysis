# MCM-Analysis Skill (v1.2.1)

A comprehensive AI skill for Mathematical Contest in Modeling (MCM) and Interdisciplinary Contest in Modeling (ICM) teams. Designed to help beginner teams produce O-award quality papers.

## What's New in v1.2.0

- **Pareto Frontier Visualization**: 2D/3D Pareto fronts, parallel coordinates for multi-objective optimization
- **Sensitivity Analysis Tools**: Tornado diagrams, spider plots, parameter impact heatmaps
- **Enhanced Style System**: Auto subplot labels (a)(b)(c), smart legend placement, LaTeX math support
- **Multi-format Export**: Save figures as PNG + PDF simultaneously
- **Asymmetric Layouts**: Flexible GridSpec-based multi-panel figures
- **Complete Documentation**: Comprehensive visualization guide with examples

## Features

- **Problem Analysis**: Identify problem type (A-F), extract requirements, recommend models
- **Model Library**: 50+ models with usage guidance from O-award papers
- **Visualization Engine**: 7 publication-quality templates with Okabe-Ito colorblind-safe palette
- **Paper Writing**: O-award structure templates with human-like writing style
- **Anti-AI Patterns**: Guidelines to make AI-assisted writing appear more natural
- **Format Checking**: Automated compliance verification (25-page limit, headers, etc.)
- **Python Scripts**: Project initialization, outline generation, format checking

## Installation

Copy this folder to your OpenCode skills directory:

```bash
# For OpenCode
~/.config/opencode/skills/mcm-analysis/

# For Claude Code
~/.claude/skills/mcm-analysis/
```

### Dependencies (for visualization)
```bash
pip install matplotlib numpy scipy networkx seaborn
```

## Quick Start

### Initialize a New Project
```bash
python scripts/init_project.py --problem C --year 2026 --team "YourTeam"
```

### Use Visualization Templates
```python
from templates.visualization import use_mcm_style, COLORS
use_mcm_style()

from templates.visualization.plot_templates import (
    plot_pareto_frontier,
    plot_tornado,
    create_grid_layout
)

# Create Pareto frontier
fig, ax = plot_pareto_frontier(cost, risk, title="Cost vs Risk Trade-off")

# Create sensitivity tornado diagram
fig, ax = plot_tornado(params, low_vals, high_vals, baseline=100)
```

### Generate Paper Outline
```bash
python scripts/generate_outline.py --problem-type C
```

### Humanize AI-Generated Text
```bash
python scripts/humanize_text.py --input draft.md --output humanized.md
```

## File Structure

```
mcm-analysis/
├── SKILL.md                          # Main skill instructions
├── references/
│   ├── models-library.md             # 50+ models categorized
│   ├── problem-types.md              # A-F problem type patterns
│   ├── paper-structure.md            # O-award paper structure
│   ├── writing-guide.md              # Academic writing guide
│   ├── anti-ai-patterns.md           # Human writing patterns
│   ├── visualization-guide.md        # Complete visualization API docs
│   └── judging-criteria.md           # COMAP judging standards
├── templates/
│   └── visualization/
│       ├── __init__.py               # Package exports
│       ├── mcm_style.mplstyle        # Publication style preset
│       ├── style_config.py           # Colors, dimensions, utilities
│       └── plot_templates/
│           ├── __init__.py           # Template exports
│           ├── time_series.py        # Forecasts with confidence intervals
│           ├── heatmap.py            # Correlation/confusion matrices
│           ├── phase_portrait.py     # Dynamic systems (Type A)
│           ├── network_graph.py      # Networks & hierarchies
│           ├── multi_panel.py        # Multi-subplot layouts
│           ├── pareto_frontier.py    # Multi-objective optimization (NEW)
│           └── sensitivity_tornado.py # Sensitivity analysis (NEW)
└── scripts/
    ├── init_project.py               # Project initializer with LaTeX
    ├── generate_outline.py           # Outline generator
    ├── check_format.py               # Format compliance checker
    └── humanize_text.py              # AI pattern reducer
```

## Visualization Templates

| Template | Best For | Key Functions |
|----------|----------|---------------|
| `time_series.py` | Type A, C, E | `plot_forecast()`, `plot_dual_axis()` |
| `heatmap.py` | Type C | `plot_correlation_matrix()`, `plot_confusion_matrix()` |
| `phase_portrait.py` | Type A | `plot_phase_portrait()` with nullclines |
| `network_graph.py` | Type B, D, F | `plot_network_topology()`, `plot_tree_hierarchy()` |
| `multi_panel.py` | All types | `create_grid_layout()`, `create_asymmetric_layout()` |
| `pareto_frontier.py` | Type B, D, E | `plot_pareto_frontier()`, `plot_parallel_coordinates()` |
| `sensitivity_tornado.py` | All types | `plot_tornado()`, `plot_sensitivity_heatmap()` |

## Key Design Decisions

1. **Output Language**: Generated content is in **Chinese** for team review; translation handled separately
2. **Anti-AI Writing**: Built-in patterns to avoid detectable AI writing styles
3. **Based on Real Data**: Patterns extracted from 60+ O-award papers (2020-2024)
4. **Colorblind Safe**: All visualizations use Okabe-Ito palette
5. **Beginner Friendly**: Complete templates, scripts, and checklists

## Problem Types Reference

| Type | Name | Focus | Recommended Viz |
|------|------|-------|-----------------|
| A | Continuous | Physics, dynamics, optimization | Phase portraits, time series |
| B | Discrete | Combinatorics, algorithms | Networks, Pareto fronts |
| C | Data Insights | Data analysis, ML, prediction | Heatmaps, time series |
| D | Operations/Network | Logistics, networks, OR | Networks, Pareto, tornado |
| E | Sustainability | Environment, ecology | Spatial heatmaps, sensitivity |
| F | Policy | Social systems, policy modeling | Networks, tornado diagrams |

## License

MIT License - Feel free to use and modify.

## Contributing

Issues and pull requests welcome!

## Changelog

### v1.2.1 (2026-01-28)
- Fixed security issue: removed hardcoded API key from release_script.py
- Updated requirements.txt with missing dependencies (scipy, networkx, seaborn)
- Fixed models module: removed false declarations of unimplemented modules
- Unified version numbers across all files

### v1.2.0 (2026-01-27)
- Added `pareto_frontier.py` with Pareto front, 3D scatter, parallel coordinates
- Added `sensitivity_tornado.py` with tornado diagram, spider plot, heatmap
- Enhanced `style_config.py` with subplot labels, legend optimization, LaTeX support
- Enhanced `multi_panel.py` with asymmetric layouts
- Updated `mcm_style.mplstyle` with LaTeX math support and refined defaults
- Complete rewrite of `visualization-guide.md` with API documentation

### v1.1.1 (2026-01-26)
- Added self-evolution and paper ingest modes
- Added 10+ new models from 2022-2023 O-award papers

### v1.1.0 (2026-01-26)
- Initial public release
