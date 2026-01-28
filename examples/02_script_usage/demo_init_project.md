# Demo: init_project.py Usage Guide

The `init_project.py` script creates a complete MCM/ICM project directory with LaTeX templates and Python scaffolding.

## Basic Usage

```bash
python scripts/init_project.py --problem C --year 2026 --team "Alpha"
```

This creates:

```
MCM_2026_C_Alpha/
├── paper/
│   ├── main.tex              # Main LaTeX document
│   ├── sections/
│   │   ├── summary.tex       # Summary template
│   │   ├── introduction.tex  # Introduction template
│   │   ├── assumptions.tex   # Assumptions template
│   │   ├── model.tex         # Model development template
│   │   ├── results.tex       # Results template
│   │   ├── sensitivity.tex   # Sensitivity analysis template
│   │   ├── conclusion.tex    # Conclusion template
│   │   └── references.bib    # Bibliography file
│   └── figures/
├── code/
│   ├── data_preprocessing.py
│   ├── visualization.py
│   └── models/
├── data/
│   ├── raw/
│   └── processed/
└── README.md
```

## Command Line Options

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--problem` | `-p` | Yes | Problem letter (A-F) |
| `--year` | `-y` | Yes | Competition year (e.g., 2026) |
| `--team` | `-t` | Yes | Team name (no spaces recommended) |
| `--path` | | No | Base directory (default: current) |

## Examples

### Example 1: Type A Problem

```bash
python scripts/init_project.py -p A -y 2026 -t "PhysicsTeam"
```

### Example 2: ICM Problem (Type D)

```bash
python scripts/init_project.py --problem D --year 2026 --team "NetworkOptimizers"
```

### Example 3: Custom Directory

```bash
python scripts/init_project.py -p E -y 2026 -t "EcoModelers" --path ./projects
```

## After Running

1. **Navigate to project:**
   ```bash
   cd MCM_2026_C_Alpha
   ```

2. **Replace team number:**
   Open `paper/main.tex` and replace `XXXXXXX` with your actual team control number.

3. **Start working:**
   - Add raw data to `data/raw/`
   - Write code in `code/`
   - Edit LaTeX sections in `paper/sections/`

## LaTeX Compilation

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or use a LaTeX editor like Overleaf, TeXstudio, or VSCode with LaTeX Workshop.

## Directory Purpose

| Directory | Purpose |
|-----------|---------|
| `paper/` | All LaTeX files and figures |
| `paper/sections/` | Individual paper sections (edit these) |
| `paper/figures/` | Generated visualization outputs |
| `code/` | Python analysis and modeling code |
| `code/models/` | Model implementation files |
| `data/raw/` | Original, unmodified data |
| `data/processed/` | Cleaned and transformed data |

---
*MCM-Analysis v1.2.2*
