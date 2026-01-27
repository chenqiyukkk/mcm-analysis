# MCM-Analysis AGENTS.md

> **Note for Agents**: This file defines the operational protocols for the mcm-analysis skill. Adhere to these guidelines to ensure consistency with the codebase and project goals.

## 1. Build & Verification Commands

This project is a Python scripts/templates collection without poetry/setuptools. No formal build step required.

### 🧪 Testing & Verification

**Run a Single Script (Primary verification method):**

```bash
# Test init_project.py
python scripts/init_project.py --problem C --year 2026 --team "Test" --path ./temp_output
# Cleanup: Remove-Item -Recurse -Force ./temp_output  (PowerShell) or rm -rf ./temp_output

# Test generate_outline.py  
python scripts/generate_outline.py --problem-type C --output ./temp_outline.md
# Cleanup: rm ./temp_outline.md

# Test humanize_text.py (analyze-only mode - no output file created)
python scripts/humanize_text.py --input README.md --analyze-only

# Test check_format.py (requires pypdf)
python scripts/check_format.py paper.pdf --verbose
```

**Run Visualization Templates (each has `if __name__ == "__main__":` block):**

```bash
python templates/visualization/style_config.py
python templates/visualization/plot_templates/pareto_frontier.py
python templates/visualization/plot_templates/sensitivity_tornado.py
python templates/visualization/plot_templates/multi_panel.py
python templates/visualization/plot_templates/phase_portrait.py
python templates/visualization/plot_templates/network_graph.py
python templates/visualization/plot_templates/heatmap.py
python templates/visualization/plot_templates/time_series.py
```

**Verify Script Help (quick syntax check):**

```bash
python scripts/init_project.py --help
python scripts/generate_outline.py --help
python scripts/humanize_text.py --help
python scripts/check_format.py --help
```

### 📦 Dependencies

**Install all dependencies:**
```bash
pip install -r requirements.txt
```

Core dependencies (managed by `requirements.txt`):
- `matplotlib>=3.7.0` - visualization
- `numpy>=1.24.0` - numerical operations
- `pypdf>=3.0.0` - PDF reading (for check_format.py)

Standard library (no installation needed):
- `pathlib` - path handling
- `argparse` - CLI parsing

### 🧹 Linting & Formatting

No automated linter configured. Follow PEP 8 manually:
- **Indentation**: 4 spaces
- **Line length**: 79-88 chars (soft limit, 100 acceptable for templates)
- **No unused imports**
- **Trailing whitespace**: Remove it

## 2. Code Style Guidelines

### 🐍 Python Conventions

**Type Hints (REQUIRED):**
```python
from typing import List, Tuple, Optional, Union, Dict

def calculate_metric(data: np.ndarray, weight: float = 1.0) -> Tuple[float, float]:
    ...

def process_file(path: Path, options: Optional[Dict[str, str]] = None) -> str:
    ...
```

**Imports (strict ordering):**
```python
# 1. Standard Library
import argparse
import re
from pathlib import Path
from typing import List, Tuple, Optional

# 2. Third-Party
import matplotlib.pyplot as plt
import numpy as np

# 3. Local Application
from ..style_config import use_mcm_style, COLORS, save_figure
```

**Path Handling (ALWAYS use pathlib):**
```python
# CORRECT
from pathlib import Path
filepath = Path(__file__).parent / "data" / "file.csv"

# WRONG - do not use
import os
filepath = os.path.join(os.path.dirname(__file__), "data", "file.csv")
```

**Docstrings (Google Style, REQUIRED for public functions):**
```python
def plot_pareto_frontier(
    x: np.ndarray,
    y: np.ndarray,
    xlabel: str = "Objective 1"
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Creates a Pareto frontier visualization.
    
    Args:
        x: Array of objective 1 values.
        y: Array of objective 2 values.
        xlabel: Label for x-axis.
    
    Returns:
        Tuple of (figure, axes) objects.
    
    Raises:
        ValueError: If x and y have different lengths.
    """
```

**Naming Conventions:**
| Type | Style | Example |
|------|-------|---------|
| Variables/Functions | snake_case | `pareto_mask`, `plot_frontier()` |
| Classes | CamelCase | `TextHumanizer`, `FormatChecker` |
| Constants | UPPER_CASE | `COLORS`, `MAX_PAGES`, `DIMENSIONS` |
| Private members | _prefix | `_add_result()`, `_internal_var` |

### 📊 Visualization Rules (Critical)

For any code in `templates/visualization/`:

1. **ALWAYS apply style first:**
   ```python
   use_mcm_style()  # Call before plt.subplots()
   ```

2. **NEVER use default colors. Use COLORS dict (Okabe-Ito colorblind-safe):**
   ```python
   from ..style_config import COLORS
   ax.plot(x, y, color=COLORS['blue'])       # Primary data
   ax.scatter(x, y, c=COLORS['vermilion'])   # Highlights/warnings
   ax.fill_between(x, y, color=COLORS['gray'], alpha=0.3)  # Background
   ```

3. **Use save_figure() helper, not plt.savefig():**
   ```python
   from ..style_config import save_figure
   save_figure(fig, "pareto_plot", output_dir=Path("./figures"), formats=['png', 'pdf'])
   ```

4. **Standard figure sizes from DIMENSIONS dict:**
   ```python
   from ..style_config import DIMENSIONS
   fig, ax = plt.subplots(figsize=DIMENSIONS['double_column'])  # (7.0, 4.5)
   ```

### 📄 LaTeX & Text Processing

**Raw strings for LaTeX:**
```python
# CORRECT
TEMPLATE = r'''\documentclass{article}
\usepackage{amsmath}
\begin{document}
$x^2 + y^2 = r^2$
\end{document}'''

# WRONG - escape sequences will cause issues
TEMPLATE = "\\documentclass{article}"
```

**Anti-AI writing patterns (for scripts/humanize_text.py):**
- Avoid: "It is important to note that", "Furthermore", "delve into"
- Prefer: Direct statements, varied connectors, specific numbers

### ⚠️ Error Handling

**File I/O with try/except:**
```python
try:
    text = input_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Error: File not found: {input_path}")
    return 1
except Exception as e:
    print(f"Error reading file: {e}")
    return 1
```

**CLI scripts use argparse:**
```python
parser = argparse.ArgumentParser(
    description="Tool description",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Examples:
  python script.py --input file.txt
  python script.py -i file.txt -o output.txt
    """
)
```

## 3. Repository Structure

```
mcm-analysis/
├── AGENTS.md              # This file (agent instructions)
├── SKILL.md               # Skill definition and workflow
├── requirements.txt       # Python dependencies
├── scripts/               # Executable CLI tools
│   ├── init_project.py    # Project scaffolding
│   ├── generate_outline.py
│   ├── humanize_text.py   # Anti-AI text processing
│   ├── check_format.py    # PDF format verification
│   └── auto_evolve.py     # Self-update mechanism
├── templates/
│   ├── visualization/     # Plot templates
│   │   ├── style_config.py    # MCM style + COLORS dict
│   │   ├── mcm_style.mplstyle # Matplotlib stylesheet
│   │   └── plot_templates/    # Individual plot types
│   └── paper_analysis_template.md
└── references/            # Knowledge base markdown files
    ├── models-library.md
    ├── problem-types.md
    ├── paper-structure.md
    └── ...
```

## 4. Agent Operational Protocol

1. **Read Before Edit**: Fully read a script before modifying. Understand argparse logic and imports.

2. **Verify After Modify**: Run `python script.py --help` or use analyze-only flags to check syntax.

3. **Keep Lightweight**: Avoid heavy dependencies (no pandas unless explicitly requested). Core uses only numpy/matplotlib.

4. **Language Policy**:
   - Code comments: English
   - User-facing output: Follow user preference (often Chinese with English technical terms)

5. **Testing Pattern**: After modifying visualization templates, run the `__main__` block to verify plots render.

6. **Version Control**: Use `python scripts/auto_evolve.py` to commit changes after session.

---
*MCM-Analysis Skill v1.2.0 - Agent Guidelines*
