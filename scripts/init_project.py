#!/usr/bin/env python3
"""
MCM/ICM Project Initializer

Creates a complete project directory structure for MCM/ICM competitions
with LaTeX templates, code scaffolding, and organized data folders.

Usage:
    python init_project.py --problem C --year 2026 --team "TeamName"
    python init_project.py -p A -y 2026 -t "Alpha"

Creates:
    MCM_2026_C_TeamName/
    ├── paper/
    │   ├── main.tex          # LaTeX template with proper MCM format
    │   ├── sections/
    │   │   ├── summary.tex
    │   │   ├── introduction.tex
    │   │   ├── assumptions.tex
    │   │   ├── model.tex
    │   │   ├── results.tex
    │   │   ├── sensitivity.tex
    │   │   ├── conclusion.tex
    │   │   └── references.bib
    │   └── figures/
    ├── code/
    │   ├── data_preprocessing.py
    │   ├── visualization.py
    │   └── models/
    ├── data/
    │   ├── raw/
    │   └── processed/
    └── README.md
"""

import argparse
import os
from pathlib import Path
from datetime import datetime


# =============================================================================
# LaTeX Templates
# =============================================================================

MAIN_TEX_TEMPLATE = r'''\documentclass[12pt]{article}

% ============================================================================
% MCM/ICM Paper Template
% Team Control Number: XXXXXXX (Replace with your team number)
% Problem: {problem}
% Year: {year}
% ============================================================================

% ----- Page Layout -----
\usepackage[letterpaper, margin=1in]{geometry}
\usepackage{fancyhdr}

% ----- Math Packages -----
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}

% ----- Graphics and Tables -----
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{subcaption}

% ----- Code and Algorithms -----
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage{listings}

% ----- References and Links -----
\usepackage[hidelinks]{hyperref}
\usepackage{cite}
\usepackage{url}

% ----- Formatting -----
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{xcolor}
\usepackage{lipsum}  % Remove after adding content

% ----- Header/Footer Setup -----
\pagestyle{fancy}
\fancyhf{{}}
\lhead{{Team \# XXXXXXX}}  % Replace XXXXXXX with your team number
\rhead{{Page \thepage\ of \pageref{{LastPage}}}}
\renewcommand{{\headrulewidth}}{{0pt}}

\usepackage{{lastpage}}

% ----- Custom Commands -----
\newcommand{{\teamnum}}{{XXXXXXX}}  % Replace with your team number
\newtheorem{{theorem}}{{Theorem}}
\newtheorem{{lemma}}{{Lemma}}
\newtheorem{{definition}}{{Definition}}

% ============================================================================
\begin{{document}}

% ----- Summary Sheet -----
\input{{sections/summary}}

\newpage
\setcounter{{page}}{{1}}

% ----- Main Content -----
\input{{sections/introduction}}
\input{{sections/assumptions}}
\input{{sections/model}}
\input{{sections/results}}
\input{{sections/sensitivity}}
\input{{sections/conclusion}}

% ----- References -----
\bibliographystyle{{plain}}
\bibliography{{sections/references}}

\end{{document}}
'''

SUMMARY_TEX_TEMPLATE = r'''\begin{center}
\Large\textbf{Summary}
\end{center}

\begin{abstract}
% Your summary goes here (max 1 page)
% Structure:
% 1. Problem restatement (1-2 sentences)
% 2. Approach and methods used (2-3 sentences)
% 3. Key results and findings (2-3 sentences)
% 4. Strengths and limitations (1-2 sentences)
% 5. Conclusions and recommendations (1-2 sentences)

% DELETE THIS PLACEHOLDER TEXT:
\lipsum[1]

\end{abstract}

\vspace{1em}
\noindent\textbf{Keywords:} keyword1, keyword2, keyword3, keyword4, keyword5
'''

INTRODUCTION_TEX_TEMPLATE = r'''\section{Introduction}

\subsection{Problem Background}
% Provide context for the problem
% - Why is this problem important?
% - What are the real-world implications?

\subsection{Problem Restatement}
% Restate the problem in your own words
% - What are we asked to find/optimize/model?
% - What are the key requirements?

\subsection{Our Approach}
% Brief overview of your solution strategy
% - What models will you use?
% - How is the paper organized?
'''

ASSUMPTIONS_TEX_TEMPLATE = r'''\section{Assumptions and Justifications}

We make the following assumptions to simplify the problem while maintaining realism:

\begin{enumerate}[label=\textbf{A\arabic*.}]
    \item \textbf{Assumption 1:} Description here.
    
    \textit{Justification:} Why this assumption is reasonable.
    
    \item \textbf{Assumption 2:} Description here.
    
    \textit{Justification:} Why this assumption is reasonable.
    
    % Add more assumptions as needed
\end{enumerate}

\subsection{Notation}
\begin{table}[H]
\centering
\begin{tabular}{cl}
\toprule
\textbf{Symbol} & \textbf{Description} \\
\midrule
$x$ & Description of $x$ \\
$y$ & Description of $y$ \\
% Add more notation as needed
\bottomrule
\end{tabular}
\caption{Notation used in this paper}
\end{table}
'''

MODEL_TEX_TEMPLATE = r'''\section{Model Development}

\subsection{Model Overview}
% High-level description of your model(s)
% Include a flowchart or diagram if helpful

\subsection{Model 1: [Name]}
% Detailed description of first model
% Include:
% - Mathematical formulation
% - Key equations
% - Algorithm pseudocode if applicable

\subsubsection{Mathematical Formulation}
% Core equations

\subsubsection{Solution Method}
% How you solve the model

\subsection{Model 2: [Name]}
% If you have multiple models, describe additional ones here
'''

RESULTS_TEX_TEMPLATE = r'''\section{Results and Analysis}

\subsection{Data Description}
% Describe your data sources and preprocessing

\subsection{Model Results}
% Present your main findings
% Include:
% - Tables with numerical results
% - Figures showing trends/patterns
% - Statistical measures

\begin{figure}[H]
    \centering
    % \includegraphics[width=0.8\textwidth]{figures/placeholder.png}
    \caption{Description of figure}
    \label{fig:result1}
\end{figure}

\begin{table}[H]
\centering
\begin{tabular}{ccc}
\toprule
\textbf{Parameter} & \textbf{Value} & \textbf{Unit} \\
\midrule
Example & 0.00 & units \\
\bottomrule
\end{tabular}
\caption{Summary of results}
\label{tab:results}
\end{table}

\subsection{Discussion}
% Interpret your results
% - What do the numbers mean?
% - Are results consistent with expectations?
% - Any surprising findings?
'''

SENSITIVITY_TEX_TEMPLATE = r'''\section{Sensitivity Analysis}

\subsection{Parameter Sensitivity}
% Test how your results change with different parameter values
% - Which parameters have the most impact?
% - Is your model robust?

\subsection{Model Validation}
% How do you know your model is correct?
% - Compare to known cases
% - Cross-validation
% - Reasonableness checks

\subsection{Strengths and Weaknesses}

\subsubsection{Strengths}
\begin{itemize}
    \item Strength 1: Description
    \item Strength 2: Description
\end{itemize}

\subsubsection{Weaknesses}
\begin{itemize}
    \item Weakness 1: Description and potential mitigation
    \item Weakness 2: Description and potential mitigation
\end{itemize}
'''

CONCLUSION_TEX_TEMPLATE = r'''\section{Conclusions}

\subsection{Summary of Findings}
% Summarize your main results (3-5 key points)

\subsection{Recommendations}
% Based on your analysis, what do you recommend?

\subsection{Future Work}
% What could be done to extend this work?
% - More data
% - Better models
% - Additional factors to consider
'''

REFERENCES_BIB_TEMPLATE = r'''% References for MCM/ICM Paper
% Add your citations here in BibTeX format

@article{example2024,
    author = {Author, First and Author, Second},
    title = {Example Article Title},
    journal = {Journal Name},
    year = {2024},
    volume = {1},
    number = {1},
    pages = {1--10},
}

@book{examplebook2023,
    author = {Book, Author},
    title = {Example Book Title},
    publisher = {Publisher Name},
    year = {2023},
}

@misc{exampleweb,
    author = {Website Author},
    title = {Website Title},
    howpublished = {\url{https://example.com}},
    year = {2024},
    note = {Accessed: 2024-01-01}
}
'''

# =============================================================================
# Python Code Templates
# =============================================================================

DATA_PREPROCESSING_TEMPLATE = '''#!/usr/bin/env python3
"""
Data Preprocessing Module for MCM/ICM {year} Problem {problem}

This module handles all data loading, cleaning, and transformation tasks.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_RAW = Path(__file__).parent.parent / "data" / "raw"
DATA_PROCESSED = Path(__file__).parent.parent / "data" / "processed"


def load_data(filename: str) -> pd.DataFrame:
    """Load data from the raw data directory."""
    filepath = DATA_RAW / filename
    
    if filepath.suffix == ".csv":
        return pd.read_csv(filepath)
    elif filepath.suffix in [".xlsx", ".xls"]:
        return pd.read_excel(filepath)
    elif filepath.suffix == ".json":
        return pd.read_json(filepath)
    else:
        raise ValueError(f"Unsupported file format: {{filepath.suffix}}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the dataframe."""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    # df = df.dropna()  # or use fillna()
    
    # Add your cleaning logic here
    
    return df


def save_processed(df: pd.DataFrame, filename: str) -> None:
    """Save processed data."""
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    filepath = DATA_PROCESSED / filename
    df.to_csv(filepath, index=False)
    print(f"Saved processed data to {{filepath}}")


if __name__ == "__main__":
    # Example usage
    print("Data preprocessing module ready.")
    print(f"Raw data directory: {{DATA_RAW}}")
    print(f"Processed data directory: {{DATA_PROCESSED}}")
'''

VISUALIZATION_TEMPLATE = '''#!/usr/bin/env python3
"""
Visualization Module for MCM/ICM {year} Problem {problem}

This module provides visualization functions for the analysis.
All figures are saved to the paper/figures directory.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Configure matplotlib for publication-quality figures
plt.rcParams.update({{
    "font.size": 12,
    "font.family": "serif",
    "figure.figsize": (8, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.grid": True,
    "grid.alpha": 0.3,
}}

# Output directory
FIGURES_DIR = Path(__file__).parent.parent / "paper" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(fig, name: str, formats=["png", "pdf"]) -> None:
    """Save figure in multiple formats."""
    for fmt in formats:
        filepath = FIGURES_DIR / f"{{name}}.{{fmt}}"
        fig.savefig(filepath)
        print(f"Saved: {{filepath}}")


def plot_line(x, y, xlabel="x", ylabel="y", title="", filename="line_plot"):
    """Create a simple line plot."""
    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", linewidth=2, markersize=4)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    save_figure(fig, filename)
    plt.close(fig)


def plot_scatter(x, y, xlabel="x", ylabel="y", title="", filename="scatter_plot"):
    """Create a scatter plot."""
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.7, edgecolors="black", linewidth=0.5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    save_figure(fig, filename)
    plt.close(fig)


def plot_heatmap(data, xlabel="x", ylabel="y", title="", filename="heatmap"):
    """Create a heatmap."""
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap="viridis", aspect="auto")
    plt.colorbar(im, ax=ax)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    save_figure(fig, filename)
    plt.close(fig)


if __name__ == "__main__":
    # Example usage
    print("Visualization module ready.")
    print(f"Figures will be saved to: {{FIGURES_DIR}}")
    
    # Create example plot
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    plot_line(x, y, "Time", "Value", "Example Plot", "example_plot")
'''

README_TEMPLATE = '''# MCM/ICM {year} - Problem {problem}

**Team:** {team}  
**Competition Year:** {year}  
**Problem Choice:** {problem}

## Project Structure

```
{project_name}/
├── paper/              # LaTeX paper files
│   ├── main.tex        # Main document (compile this)
│   ├── sections/       # Individual sections
│   └── figures/        # Generated figures
├── code/               # Analysis code
│   ├── data_preprocessing.py
│   ├── visualization.py
│   └── models/         # Model implementations
├── data/               # Data files
│   ├── raw/            # Original data
│   └── processed/      # Cleaned data
└── README.md           # This file
```

## Quick Start

### 1. Data Preparation
Place raw data files in `data/raw/`, then run:
```bash
python code/data_preprocessing.py
```

### 2. Run Analysis
```bash
python code/models/your_model.py
```

### 3. Generate Figures
```bash
python code/visualization.py
```

### 4. Compile Paper
```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Important Reminders

- [ ] Replace `XXXXXXX` with your team control number in `main.tex`
- [ ] Maximum 25 pages (including summary sheet)
- [ ] No team member names or institution names in the paper
- [ ] Include all references in `sections/references.bib`
- [ ] All figures should be high resolution (300 DPI minimum)

## Timeline

| Day | Tasks |
|-----|-------|
| Day 1 | Understand problem, brainstorm approaches, gather data |
| Day 2 | Develop initial model, start coding |
| Day 3 | Refine model, generate results |
| Day 4 | Write paper, create figures |
| Day 5 | Review, revise, format check, submit |

## Notes

_Add your notes here during the competition._

---
Created: {date}
'''


def create_project_structure(problem: str, year: int, team: str, base_path: Path = None):
    """Create the complete MCM project directory structure."""
    
    if base_path is None:
        base_path = Path.cwd()
    
    project_name = f"MCM_{year}_{problem}_{team}"
    project_path = base_path / project_name
    
    # Check if directory already exists
    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists!")
        print("Please choose a different team name or remove the existing directory.")
        return None
    
    print(f"Creating MCM project: {project_name}")
    print("=" * 50)
    
    # Create directory structure
    directories = [
        project_path / "paper" / "sections",
        project_path / "paper" / "figures",
        project_path / "code" / "models",
        project_path / "data" / "raw",
        project_path / "data" / "processed",
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"  Created: {directory.relative_to(base_path)}")
    
    # Create LaTeX files
    latex_files = {
        "paper/main.tex": MAIN_TEX_TEMPLATE.format(problem=problem, year=year),
        "paper/sections/summary.tex": SUMMARY_TEX_TEMPLATE,
        "paper/sections/introduction.tex": INTRODUCTION_TEX_TEMPLATE,
        "paper/sections/assumptions.tex": ASSUMPTIONS_TEX_TEMPLATE,
        "paper/sections/model.tex": MODEL_TEX_TEMPLATE,
        "paper/sections/results.tex": RESULTS_TEX_TEMPLATE,
        "paper/sections/sensitivity.tex": SENSITIVITY_TEX_TEMPLATE,
        "paper/sections/conclusion.tex": CONCLUSION_TEX_TEMPLATE,
        "paper/sections/references.bib": REFERENCES_BIB_TEMPLATE,
    }
    
    for filepath, content in latex_files.items():
        full_path = project_path / filepath
        full_path.write_text(content, encoding="utf-8")
        print(f"  Created: {filepath}")
    
    # Create Python files
    python_files = {
        "code/data_preprocessing.py": DATA_PREPROCESSING_TEMPLATE.format(
            year=year, problem=problem
        ),
        "code/visualization.py": VISUALIZATION_TEMPLATE.format(
            year=year, problem=problem
        ),
    }
    
    for filepath, content in python_files.items():
        full_path = project_path / filepath
        full_path.write_text(content, encoding="utf-8")
        print(f"  Created: {filepath}")
    
    # Create placeholder for models
    models_init = project_path / "code" / "models" / "__init__.py"
    models_init.write_text('"""Model implementations for MCM/ICM analysis."""\n', encoding="utf-8")
    print(f"  Created: code/models/__init__.py")
    
    # Create README
    readme_content = README_TEMPLATE.format(
        year=year,
        problem=problem,
        team=team,
        project_name=project_name,
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    readme_path = project_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"  Created: README.md")
    
    # Create .gitignore
    gitignore_content = """# LaTeX
*.aux
*.log
*.out
*.toc
*.bbl
*.blg
*.synctex.gz
*.fdb_latexmk
*.fls

# Python
__pycache__/
*.pyc
.venv/
venv/

# Data
*.csv
*.xlsx
!data/raw/.gitkeep
!data/processed/.gitkeep

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
"""
    gitignore_path = project_path / ".gitignore"
    gitignore_path.write_text(gitignore_content, encoding="utf-8")
    print(f"  Created: .gitignore")
    
    # Create .gitkeep files
    for folder in ["data/raw", "data/processed", "paper/figures"]:
        gitkeep = project_path / folder / ".gitkeep"
        gitkeep.write_text("", encoding="utf-8")
    
    print("=" * 50)
    print(f"Project created successfully!")
    print(f"\nNext steps:")
    print(f"  1. cd {project_name}")
    print(f"  2. Replace 'XXXXXXX' with your team number in paper/main.tex")
    print(f"  3. Start working on your paper!")
    
    return project_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize an MCM/ICM project directory structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python init_project.py --problem C --year 2026 --team "TeamAlpha"
  python init_project.py -p A -y 2026 -t "MyTeam"
  python init_project.py --problem D --year 2026 --team "Winners" --path ./projects
        """
    )
    
    parser.add_argument(
        "-p", "--problem",
        type=str,
        required=True,
        choices=["A", "B", "C", "D", "E", "F"],
        help="Problem letter (A-F)"
    )
    
    parser.add_argument(
        "-y", "--year",
        type=int,
        required=True,
        help="Competition year (e.g., 2026)"
    )
    
    parser.add_argument(
        "-t", "--team",
        type=str,
        required=True,
        help="Team name (no spaces recommended)"
    )
    
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        help="Base path for project creation (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Validate team name
    team_clean = args.team.replace(" ", "_")
    if team_clean != args.team:
        print(f"Note: Spaces in team name replaced with underscores: {team_clean}")
    
    base_path = Path(args.path) if args.path else None
    
    create_project_structure(
        problem=args.problem.upper(),
        year=args.year,
        team=team_clean,
        base_path=base_path
    )


if __name__ == "__main__":
    main()
