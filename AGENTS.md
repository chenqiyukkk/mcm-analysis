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

**Run Example Demos (v1.2.2+):**

```bash
# Run all visualization demos (generates sample_outputs/)
python examples/01_visualization_demos/demo_all_plots.py
python examples/01_visualization_demos/demo_pareto_frontier.py
python examples/01_visualization_demos/demo_sensitivity.py

# Test humanize_text with sample file
python scripts/humanize_text.py --input examples/02_script_usage/sample_input/sample_draft.md --analyze-only
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

## 5. Development Roadmap: 论文自动化生成引擎

> **目标**: 将 MCM-Analysis 从可视化工具进化为端到端论文自动生成引擎
> **预计版本**: v1.3.0 → v2.0.0

### Phase 1: 论文框架自动化生成 ✅ COMPLETED (v1.3.0)

**目标**: 根据题型自动生成完整的 LaTeX 论文骨架

**实现内容**:
- [x] 新增 `scripts/generate_paper_skeleton.py` - 核心脚本
- [x] 新增 `templates/latex/` - LaTeX 模板目录
  - [x] `preamble.tex` - LaTeX 前言/宏包配置
  - [x] `sections/` - 结构级和初稿级章节模板 (16个文件)
- [x] 支持两种模式:
  - **结构级 (structure)**: 标题 + 提纲 + 图表位置标注 (~3页)
  - **初稿级 (draft)**: 完整中文初稿内容 (~12-15页)
- [x] 交互式询问用户选择模式

**验证命令**:
```bash
python scripts/generate_paper_skeleton.py --help
python scripts/generate_paper_skeleton.py -p C -y 2026 --mode structure
python scripts/generate_paper_skeleton.py -p C -y 2026 --mode draft
```

---

### Phase 2: 题目智能解析 ⏳ PENDING

**目标**: 自动读取题目 PDF，提取关键信息

**计划内容**:
- [ ] 新增 `scripts/parse_problem.py` - 题目解析脚本
- [ ] 集成用户已有的 `pdf` skill 进行 PDF 读取
- [ ] 功能:
  - 识别问题类型 (A-F)
  - 提取子问题 (Q1, Q2, Q3...)
  - 识别数据文件引用
  - 提取关键约束条件
- [ ] 输出: 结构化的 `problem_analysis.json`

**预计版本**: v1.4.0

---

### Phase 3: 模型代码自动生成 ⏳ PENDING

**目标**: 根据问题分析结果，自动生成模型代码框架

**计划内容**:
- [ ] 新增 `templates/models/` - 模型代码模板库
  - 优化类: 线性规划、整数规划、遗传算法
  - 预测类: ARIMA、LSTM、XGBoost
  - 网络类: 最短路径、最大流、PageRank
  - 动态系统: ODE求解、系统动力学
- [ ] 新增 `scripts/generate_model_code.py` - 代码生成脚本
- [ ] 根据题目分析自动匹配并生成代码框架

**预计版本**: v1.5.0

---

### Phase 4: 数据处理自动化 ⏳ PENDING

**目标**: 自动识别和预处理题目数据

**计划内容**:
- [ ] 新增 `scripts/process_data.py` - 数据处理脚本
- [ ] 功能:
  - 读取 CSV/Excel 数据文件
  - 自动生成数据探索报告 (EDA)
  - 数据清洗代码生成
  - 特征工程建议

**预计版本**: v1.6.0

---

### Phase 5: 论文内容自动生成 ⏳ PENDING

**目标**: 自动生成各章节的初稿内容

**计划内容**:
- [ ] 新增 `scripts/generate_section.py` - 章节生成脚本
- [ ] 每个章节使用专门的 prompt 模板:
  - Introduction: 背景 + 问题重述 + 贡献
  - Assumptions: 假设列表 + 合理性论证
  - Model: 模型描述 + 公式 + 伪代码
  - Results: 结果描述 + 图表引用
  - Sensitivity: 灵敏度分析模板
  - Conclusion: 总结 + 局限性 + 未来工作
- [ ] 自动应用 `anti-ai-patterns.md` 人性化处理

**预计版本**: v1.7.0

---

### Phase 6: 一键论文生成引擎 ⏳ PENDING

**目标**: 整合所有组件，实现端到端自动化

**计划内容**:
- [ ] 新增 `scripts/generate_paper.py` - 主控脚本
- [ ] 完整流程:
  ```
  题目PDF → 解析 → 模型选择 → 代码生成 → 运行分析 → 
  生成图表 → 写作各章节 → 人性化处理 → 格式检查 → LaTeX编译 → PDF
  ```
- [ ] 支持中间步骤人工干预/修改
- [ ] 支持增量生成 (只重新生成修改的部分)

**预计版本**: v2.0.0

---

### 开发进度总览

| Phase | 名称 | 状态 | 版本 |
|-------|------|------|------|
| 1 | 论文框架自动化生成 | ✅ COMPLETED | v1.3.0 |
| 2 | 题目智能解析 | ⏳ PENDING | v1.4.0 |
| 3 | 模型代码自动生成 | ⏳ PENDING | v1.5.0 |
| 4 | 数据处理自动化 | ⏳ PENDING | v1.6.0 |
| 5 | 论文内容自动生成 | ⏳ PENDING | v1.7.0 |
| 6 | 一键论文生成引擎 | ⏳ PENDING | v2.0.0 |

---
*MCM-Analysis Skill v1.3.0 - Agent Guidelines*
