# MCM-Analysis Skill v2.0

> **Architecture**: LLM-Driven Workflow with External Skill Integration  
> **Philosophy**: Scripts handle I/O, LLM handles intelligence

A comprehensive AI skill for Mathematical Contest in Modeling (MCM) and Interdisciplinary Contest in Modeling (ICM) teams. Designed to help beginner teams produce O-award quality papers.

## What's New in v2.0

### Architecture Revolution

| v1.x (Script-Driven) | v2.0 (LLM-Driven) |
|---------------------|-------------------|
| Heavy Python scripts (~800 lines) | Minimal scripts (~200 lines, I/O only) |
| Regex-based parsing (fragile) | LLM semantic understanding (robust) |
| Keywords matching (low accuracy) | Knowledge base references (high accuracy) |
| High maintenance cost | Low maintenance, high flexibility |

### Key Changes

- **Removed Scripts**: `parse_problem.py`, `generate_outline.py`, `humanize_text.py` - now handled by LLM
- **Retained Scripts**: `init_project.py`, `check_format.py`, `auto_evolve.py` (I/O only)
- **Enhanced Knowledge Base**: 7 comprehensive reference documents in `references/`
- **External Skill Integration**: Leverages `pdf`, `xlsx`, `docx`, `exploratory-data-analysis` skills

## Features

- **Problem Analysis**: Identify problem type (A-F), extract requirements, recommend models
- **Model Library**: 50+ models with usage guidance from O-award papers
- **Visualization Engine**: 7 publication-quality templates with Okabe-Ito colorblind-safe palette
- **Paper Writing**: O-award structure templates with human-like writing style
- **Anti-AI Patterns**: Guidelines to make AI-assisted writing appear more natural
- **Format Checking**: Automated compliance verification (25-page limit, headers, etc.)

## Installation

Copy this folder to your OpenCode skills directory:

```bash
# For OpenCode
~/.config/opencode/skills/mcm-analysis/

# For Claude Code
~/.claude/skills/mcm-analysis/
```

### Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies:
- `matplotlib>=3.7.0` - visualization
- `numpy>=1.24.0` - numerical operations
- `pypdf>=3.0.0` - PDF processing
- `scipy>=1.10.0` - ODE solving (phase portraits)
- `networkx>=3.0` - network visualization
- `seaborn>=0.12.0` - statistical visualization

## Quick Start

### Initialize a New Project
```bash
python scripts/init_project.py --problem C --year 2026 --team "YourTeam"
```

### Check Paper Format
```bash
python scripts/check_format.py paper.pdf --verbose
```

### Use Visualization Templates
```python
from templates.visualization import use_mcm_style, COLORS, save_figure

# Apply MCM publication style
use_mcm_style()

# Create plots using templates
from templates.visualization.plot_templates import (
    plot_pareto_frontier,
    plot_tornado,
    create_grid_layout
)

# Example: Pareto frontier
fig, ax = plot_pareto_frontier(cost, risk, title="Cost vs Risk Trade-off")
save_figure(fig, "pareto_plot")
```

## File Structure

```
mcm-analysis/
├── SKILL.md                          # Main skill workflow definitions
├── AGENTS.md                         # Agent operational protocol
│
├── references/                       # Knowledge Base (Core!)
│   ├── models-library.md             # 50+ models categorized
│   ├── problem-types.md              # A-F problem type patterns
│   ├── paper-structure.md            # O-award paper structure
│   ├── writing-guide.md              # Academic writing guide
│   ├── anti-ai-patterns.md           # Human writing patterns
│   ├── visualization-guide.md        # Complete visualization API
│   └── judging-criteria.md           # COMAP judging standards
│
├── templates/
│   ├── visualization/                # 7 plot templates
│   │   ├── style_config.py           # Colors, dimensions, utilities
│   │   ├── mcm_style.mplstyle        # Publication style preset
│   │   └── plot_templates/           # Individual plot types
│   └── latex/                        # LaTeX templates
│       ├── preamble.tex
│       └── sections/
│
├── scripts/                          # Minimal I/O scripts
│   ├── init_project.py               # Project scaffolding
│   ├── check_format.py               # PDF format verification
│   └── auto_evolve.py                # Git commit/push
│
└── examples/                         # 12 example files
    ├── 01_visualization_demos/       # All 7 plot types
    ├── 03_paper_skeleton/            # LaTeX examples
    ├── 03_problem_analysis/          # Analysis examples
    └── 04_complete_workflow/         # End-to-end case study
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

## External Skill Dependencies

v2.0 integrates with external skills for specific tasks:

| External Skill | Purpose | When to Use |
|----------------|---------|-------------|
| `pdf` | Extract text from PDF files | User provides problem PDF |
| `markitdown` | Convert documents to Markdown | Alternative PDF extraction |
| `xlsx` | Read and analyze Excel data | Problem includes data files |
| `docx` | Generate Word documents | Create memos, letters |
| `exploratory-data-analysis` | Automatic EDA reports | Analyze provided datasets |
| `scientific-visualization` | Generate publication figures | Create charts and plots |

## Problem Types Reference

| Type | Name | Focus | Recommended Viz |
|------|------|-------|-----------------|
| A | Continuous | Physics, dynamics, optimization | Phase portraits, time series |
| B | Discrete | Combinatorics, algorithms | Networks, Pareto fronts |
| C | Data Insights | Data analysis, ML, prediction | Heatmaps, time series |
| D | Operations/Network | Logistics, networks, OR | Networks, Pareto, tornado |
| E | Sustainability | Environment, ecology | Spatial heatmaps, sensitivity |
| F | Policy | Social systems, policy modeling | Networks, tornado diagrams |

## Key Design Decisions

1. **LLM-Driven**: Intelligence in LLM, scripts for I/O only
2. **Output Language**: Generated content in **Chinese** for team review
3. **Anti-AI Writing**: Built-in patterns to avoid detectable AI styles
4. **Based on Real Data**: Patterns from 60+ O-award papers (2020-2024)
5. **Colorblind Safe**: All visualizations use Okabe-Ito palette

## Changelog

### v2.0.0 (2026-01-29)
- **Architecture Revolution**: LLM-driven workflow replaces script-driven approach
- Removed heavy scripts: `parse_problem.py`, `generate_outline.py`, `humanize_text.py`
- Enhanced SKILL.md with 6 comprehensive workflow definitions
- Updated AGENTS.md with v2.0 operational protocols
- Retained minimal I/O scripts: `init_project.py`, `check_format.py`, `auto_evolve.py`

### v1.2.2 (2026-01-29)
- Added comprehensive `examples/` folder with 12 example files
- Visualization demos, script usage guides, problem analysis examples

### v1.2.1 (2026-01-28)
- Fixed security issue: removed hardcoded API key
- Updated requirements.txt with missing dependencies

### v1.2.0 (2026-01-27)
- Added Pareto frontier and sensitivity analysis templates
- Enhanced style system with LaTeX support
- Complete rewrite of visualization guide

## License

MIT License - Feel free to use and modify.

## Contributing

Issues and pull requests welcome!
