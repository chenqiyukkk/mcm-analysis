# MCM-Analysis Examples

This folder contains comprehensive examples demonstrating how to use the MCM-Analysis skill for Mathematical Contest in Modeling competitions.

## Quick Start

```bash
# Install dependencies first
pip install -r ../requirements.txt

# Run the visualization demo
python 01_visualization_demos/demo_all_plots.py
```

## Contents

### 1. Visualization Demos (`01_visualization_demos/`)

Interactive Python scripts demonstrating all 7 visualization templates:

| Script | Description |
|--------|-------------|
| `demo_all_plots.py` | Generates all plot types in one run |
| `demo_pareto_frontier.py` | Pareto frontier, 3D scatter, parallel coordinates |
| `demo_sensitivity.py` | Tornado, spider, and sensitivity heatmaps |

**Output:** All generated plots are saved to `sample_outputs/`

### 2. Script Usage Examples (`02_script_usage/`)

Step-by-step guides for using the CLI scripts:

| Document | Covers |
|----------|--------|
| `demo_init_project.md` | Project scaffolding with LaTeX templates |
| `demo_generate_outline.md` | Paper outline generation for problem types A-F |
| `demo_humanize_text.md` | Anti-AI text processing with before/after |

### 3. Problem Analysis Examples (`03_problem_analysis/`)

Real-world problem analysis demonstrations:

| Document | Content |
|----------|---------|
| `analysis_type_C_example.md` | Analysis of a Type C problem (2024 Tennis Momentum) |
| `model_selection_guide.md` | Decision tree for choosing the right models |

### 4. Complete Workflow Case (`04_complete_workflow/`)

End-to-end MCM workflow demonstration:

| Document | Content |
|----------|---------|
| `mini_case_study.md` | Simplified case: problem to paper |
| `workflow_diagram.md` | Visual workflow with checkpoints |

## Running the Examples

### Prerequisites

```bash
# Core dependencies
pip install matplotlib numpy

# For all visualization features
pip install scipy networkx seaborn
```

### Visualization Demos

```bash
cd examples/01_visualization_demos

# Run all demos
python demo_all_plots.py

# Run specific demos
python demo_pareto_frontier.py
python demo_sensitivity.py
```

### View Generated Plots

After running the demos, check `sample_outputs/` for the generated PNG files.

## Tips for MCM Teams

1. **Day 1**: Use `03_problem_analysis/` examples to understand how to analyze your problem
2. **Day 2-3**: Reference `01_visualization_demos/` for creating publication-quality figures
3. **Day 4**: Use `02_script_usage/demo_humanize_text.md` to polish your writing
4. **Day 5**: Run `check_format.py` to verify your PDF before submission

## Contributing

Found an issue or have a suggestion? Feel free to open an issue or PR!

---
*MCM-Analysis v1.2.2 Examples*
