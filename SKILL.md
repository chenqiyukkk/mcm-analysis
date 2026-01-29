---
name: mcm-analysis
description: Use when analyzing MCM/ICM (Mathematical Contest in Modeling) problems, developing mathematical models, writing competition papers, or preparing for COMAP modeling contests. Triggers on keywords like MCM, ICM, mathematical modeling competition, COMAP, or when user provides a modeling competition problem.
---

# MCM/ICM Analysis Skill v2.0

> **Architecture**: LLM-driven workflow with external skill integration
> **Philosophy**: Scripts handle I/O, LLM handles intelligence

A comprehensive skill for Mathematical Contest in Modeling (MCM) and Interdisciplinary Contest in Modeling (ICM) teams. Designed to help beginner teams produce O-award quality papers.

## Overview

This skill provides end-to-end support for MCM/ICM competition:
- **Problem Analysis**: Identify problem type, extract requirements, recommend models
- **Modeling Guidance**: Match problems with proven modeling approaches
- **Paper Writing**: Generate outlines, provide writing templates, ensure human-like output
- **Quality Assurance**: Format checking, self-evaluation against judging criteria

## Critical: Writing Language Policy

**When generating paper content (outlines, drafts, analysis):**
- Output in **Chinese (中文)** for team review and modification
- Include English technical terms in parentheses: 灵敏度分析 (Sensitivity Analysis)
- Team will handle translation to English separately

**Skill files and templates remain in English for international compatibility.**

---

## External Skill Dependencies

This skill integrates with external skills for specific tasks:

| External Skill | Purpose | When to Use |
|----------------|---------|-------------|
| `pdf` | Extract text from PDF files | User provides problem PDF |
| `markitdown` | Convert documents to Markdown | Alternative PDF extraction |
| `xlsx` | Read and analyze Excel data | Problem includes data files |
| `docx` | Generate Word documents | Create memos, letters |
| `exploratory-data-analysis` | Automatic EDA reports | Analyze provided datasets |
| `statistical-analysis` | Statistical tests and analysis | Validate model results |
| `scientific-visualization` | Generate publication figures | Create charts and plots |

---

## Workflow 1: Problem Analysis

### Trigger Conditions
- User provides MCM/ICM problem PDF or text
- User asks to analyze a modeling problem
- User mentions "这是什么类型的题目" or similar

### Steps

#### Step 1: Extract Problem Text

**If user provides PDF:**
```
Call skill: pdf
Request: Extract all text from [PDF path]
```

**If user provides text directly:**
Use the provided text directly.

#### Step 2: Identify Problem Type

Read the extracted text and analyze against `references/problem-types.md`:

**Type A (Continuous)** - 连续型
- Keywords: differential equation, dynamical system, population, ecology, physics
- Characteristics: Continuous variables, time evolution, physical/biological systems
- Common models: ODE/PDE, Lotka-Volterra, Cellular Automaton

**Type B (Discrete)** - 离散型
- Keywords: discrete, optimization, scheduling, network, graph, facility location
- Characteristics: Discrete decisions, resource allocation, routing
- Common models: Integer Programming, Genetic Algorithm, Network Flow

**Type C (Data Insights)** - 数据洞察型
- Keywords: data, dataset, machine learning, prediction, classification, time series
- Characteristics: Rich datasets provided, pattern recognition, forecasting
- Common models: Random Forest, XGBoost, Neural Networks, Time Series

**Type D (Operations Research/Network)** - 运筹学/网络型
- Keywords: network, graph theory, node, edge, centrality, PageRank
- Characteristics: Complex systems, relationships, interdependencies
- Common models: PageRank, Network Centrality, System Dynamics

**Type E (Sustainability)** - 可持续性型
- Keywords: sustainability, environment, climate, risk, carbon, pollution
- Characteristics: Environmental assessment, long-term planning, policy
- Common models: AHP-EWM, Risk Assessment, Life Cycle Assessment

**Type F (Policy)** - 政策型
- Keywords: policy, social, behavior, stakeholder, game theory, economic
- Characteristics: Social systems, multi-stakeholder, decision making
- Common models: Agent-Based Models, Game Theory, System Dynamics

#### Step 3: Extract Tasks and Requirements

From the problem text, identify:

1. **Main Tasks** (3-6 items)
   - Look for: explicit "Task 1/2/3", bullet points (•, ●, -), numbered lists
   - Extract the actual requirement, not file names
   - Format: "Q1: [task description]"

2. **Data Files**
   - List all provided data files (CSV, Excel, etc.)
   - Note: Don't confuse with task descriptions

3. **Constraints**
   - Page limits (usually 25 pages)
   - Special requirements (memos, letters, etc.)
   - Forbidden elements

4. **Deliverables**
   - Technical paper
   - Summary sheet
   - Additional documents (memos, letters, etc.)

#### Step 4: Recommend Modeling Direction

Based on problem type and tasks, consult `references/models-library.md`:

- Recommend 2-4 suitable models
- Explain why each fits
- Mention O-award precedents from similar years
- Suggest model combination strategy

#### Step 5: Output Structured Analysis

```
## 题目分析报告

**年份**: 2024
**题目类型**: C (Data Insights) - 数据洞察型
**置信度**: High

### 任务分解
1. **Q1**: [Task description in Chinese]
2. **Q2**: [Task description in Chinese]
3. **Q3**: [Task description in Chinese]
...

### 数据文件
- [filename1]: [description]
- [filename2]: [description]

### 约束条件
- [constraint 1]
- [constraint 2]

### 推荐模型
1. **[Model Name]** (中文名)
   - 适用性: [explanation]
   - O奖案例: [year and problem]
   
2. **[Model Name]** (中文名)
   ...

### 相似历年题目
- [Year] Problem [Type]: [brief description]
```

---

## Workflow 2: Data Exploration

### Trigger Conditions
- Problem includes data files (CSV, Excel, etc.)
- User asks to analyze data
- User mentions "数据" or "dataset"

### Steps

#### Step 1: Load Data

**For Excel files:**
```
Call skill: xlsx
Request: Read [file path] and show:
- First 10 rows
- Column names and data types
- Basic statistics (count, mean, std, min, max)
- Missing value counts
```

**For CSV files:**
```
Call skill: exploratory-data-analysis
Request: Generate comprehensive EDA report for [file path]
```

#### Step 2: Analyze Data Characteristics

Based on the output, summarize:

1. **Data Scale**: Number of rows, columns
2. **Key Features**: Most important columns for modeling
3. **Data Quality**: Missing values, outliers, inconsistencies
4. **Feature Types**: Numerical, categorical, text, time series
5. **Relationships**: Correlations between features

#### Step 3: Recommend Preprocessing

Suggest data preprocessing steps:
- Handling missing values
- Feature engineering opportunities
- Normalization/standardization needs
- Train/test split strategy

---

## Workflow 3: Model Selection

### Trigger Conditions
- User asks "用什么模型"
- User requests model recommendations
- After problem analysis, user wants to proceed

### Steps

#### Step 1: Consult Model Library

Read `references/models-library.md` for problem-specific models.

#### Step 2: Select and Justify Models

For each recommended model:

1. **Model Name** (中文名)
2. **Mathematical Basis**: Brief explanation
3. **Why It Fits**: Connection to problem requirements
4. **Implementation**: Python library suggestions
5. **O-Award Precedent**: Similar problems that used this model

#### Step 3: Suggest Model Architecture

Propose how to combine models:

```
建议模型架构:

Layer 1: [Base Model]
- 作用: [purpose]
- 输入: [inputs]
- 输出: [outputs]

Layer 2: [Advanced Model]
- 作用: [purpose]
- 与Layer 1关系: [how they connect]

Validation: [How to validate the combined model]
```

---

## Workflow 4: Paper Writing

### Trigger Conditions
- User asks to write a section
- User requests outline generation
- User wants to draft content

### Steps

#### Step 1: Load Structure Template

Read `references/paper-structure.md` for section guidelines.

#### Step 2: Generate Content

**For each section:**

1. **Introduction (引言)**
   - Background context (Chinese)
   - Problem restatement
   - Paper organization

2. **Assumptions (假设)**
   - List 5-8 key assumptions
   - Justification for each

3. **Model (模型建立)**
   - Mathematical notation
   - Model description
   - Key equations
   - Algorithm pseudocode

4. **Results (结果)**
   - Key findings
   - Figure/table references
   - Interpretation

5. **Sensitivity Analysis (灵敏度分析)**
   - Parameters tested
   - Results summary
   - Robustness conclusions

#### Step 3: Apply Human Writing Style

Reference `references/anti-ai-patterns.md`:

**AVOID:**
- "It is important to note that..."
- Overuse of "Furthermore, moreover, additionally"
- Perfect parallel structure
- All paragraphs same length

**USE:**
- Varied sentence length
- Specific numbers: "23.7% improvement" not "significant improvement"
- Show thinking process: "We initially considered X, but..."
- First-person plural: "We found..." "Our model shows..."

#### Step 4: Output Format

```
## [Section Name in Chinese]

[Content in Chinese with English technical terms in parentheses]

### Key Terms (术语对照)
- [Chinese term]: [English term]
- [Chinese term]: [English term]
```

---

## Workflow 5: Visualization

### Trigger Conditions
- User asks for chart suggestions
- User wants to create figures
- User mentions "画图" or "可视化"

### Steps

#### Step 1: Consult Visualization Guide

Read `references/visualization-guide.md` for problem-type-specific recommendations.

#### Step 2: Recommend Chart Types

Based on data and analysis needs:

| Purpose | Recommended Chart | Template |
|---------|------------------|----------|
| Time series | Line plot with confidence bands | `templates/visualization/plot_templates/time_series.py` |
| Correlations | Heatmap | `templates/visualization/plot_templates/heatmap.py` |
| Optimization | Pareto frontier | `templates/visualization/plot_templates/pareto_frontier.py` |
| Sensitivity | Tornado diagram | `templates/visualization/plot_templates/sensitivity_tornado.py` |
| Network | Network graph | `templates/visualization/plot_templates/network_graph.py` |

#### Step 3: Provide Code Template

Give Python code using templates from `templates/visualization/`:

```python
from templates.visualization.style_config import use_mcm_style, COLORS, save_figure
from templates.visualization.plot_templates.time_series import plot_forecast

# Use MCM style
use_mcm_style()

# Generate plot
fig, ax = plot_forecast(
    time_historical=...,
    values_historical=...,
    time_forecast=...,
    values_forecast=...,
    title="...",
    xlabel="...",
    ylabel="..."
)

# Save
save_figure(fig, "figure_name", output_dir=Path("./figures"))
```

---

## Workflow 6: Quality Check

### Trigger Conditions
- User asks to check paper
- User mentions "格式" or "format"
- Before submission

### Steps

#### Step 1: Format Verification

```bash
python scripts/check_format.py paper.pdf --verbose
```

Check:
- Page count (≤25 pages)
- Font and spacing
- Margin compliance
- Summary sheet presence

#### Step 2: Content Review

Against `references/judging-criteria.md`:

**Completeness Checklist:**
- [ ] Summary Sheet (1 page)
- [ ] Table of Contents
- [ ] Introduction with problem restatement
- [ ] Clear assumptions with justifications
- [ ] Mathematical model with notation
- [ ] Results with figures/tables
- [ ] Sensitivity analysis
- [ ] Strengths and weaknesses
- [ ] Conclusions
- [ ] References
- [ ] AI Use Report (separate, not counted)

#### Step 3: Self-Evaluation

Estimate judging level:

```
自评等级: [Unsuccessful / Successful Participant / Honorable Mention / Meritorious / Finalist]

理由:
- 优点: [strengths]
- 不足: [weaknesses]
- 改进建议: [suggestions]
```

---

## Special Capabilities

### A. Paper Ingest Mode (论文解析模式)

**Trigger**: "解析这篇论文 [PDF路径]"

**Workflow**:
1. **Extract**: Call `pdf` or `markitdown` skill to read PDF
2. **Analyze**: Review against `templates/paper_analysis_template.md`
   - Identify Year, Problem, Title, Type
   - Decompose questions and strategies
   - Extract models, data sources, conclusions
3. **Generate**: Create markdown file `YYYY-Type-paper-XX.md`
4. **Save**: Write to `D:/ICM/解析结果/papers/` or user-specified path

### B. Self-Evolution Mode (自我进化模式)

**Trigger**: "收工" / "进化" / "提交更新"

**Workflow**:
1. **Summarize**: Review session for new insights (models, prompts, code)
2. **Persist**: (Optional) Update `references/models-library.md` if new models discovered
3. **Push**: Execute `python scripts/auto_evolve.py` to commit and push to GitHub

---

## Quick Reference

### Problem Type Quick Reference

| Type | Name | Focus | Key Models |
|------|------|-------|------------|
| A | Continuous | Physics, dynamics, optimization | Differential equations, PDE, optimization |
| B | Discrete | Combinatorics, algorithms | Graph theory, integer programming, simulation |
| C | Data Insights | Data analysis, prediction | ML/DL, time series, statistical analysis |
| D | Operations/Network | Logistics, networks | Network optimization, queueing, scheduling |
| E | Sustainability | Environment, ecology | System dynamics, multi-objective optimization |
| F | Policy | Social systems, policy | Game theory, agent-based modeling, AHP |

### Competition Timeline

| Day | Focus | This Skill Helps With |
|-----|-------|----------------------|
| Day 1 (Thu PM) | Problem analysis, model selection | Workflow 1 + 3 |
| Day 2 (Fri) | Core modeling, initial coding | Model guidance, code templates |
| Day 3 (Sat) | Results, sensitivity analysis | Visualization, validation |
| Day 4 (Sun) | Writing, polishing | Workflow 4 |
| Day 5 (Mon AM) | Final review, submission | Workflow 6 |

### Important Reminders

1. **25 Page Limit**: Includes EVERYTHING (summary, content, references, appendices)
2. **No Identifying Info**: Team number only, no names or school names
3. **AI Disclosure Required**: Must include "Report on Use of AI" section (not counted in 25 pages)
4. **Deadline is HARD**: 9:00 PM EST Monday - no exceptions
5. **Summary is Critical**: Judges weight summary heavily - write it LAST but make it BEST

---

## Reference Files

| File | Purpose |
|------|---------|
| `references/models-library.md` | 50+ models categorized by type |
| `references/problem-types.md` | Historical patterns for A-F problems |
| `references/paper-structure.md` | O-award paper structure templates |
| `references/writing-guide.md` | Academic writing phrases and patterns |
| `references/anti-ai-patterns.md` | Human writing style guide |
| `references/visualization-guide.md` | Chart selection & O-award visualization patterns |
| `references/judging-criteria.md` | COMAP official judging standards |

---

## Workflow 7: Full Paper Generation Pipeline (端到端论文生成)

### Trigger Conditions
- User says: "生成论文", "写完整论文", "一键建模", "从题目到论文"
- User provides: PDF path `[+ data file path]`

### Pipeline Overview

This workflow orchestrates Workflows 1-6 to generate a complete paper draft from problem PDF to LaTeX output.

**Input**: Problem PDF + (optional) data files  
**Output**: Complete LaTeX project ready for Overleaf  
**Mode**: Step-by-step confirmation (user reviews at each phase)

---

### Phase 1: Project Initialization

**Action**: Create project directory structure

```bash
python scripts/init_project.py --problem [X] --year [YYYY] --team [TeamName] --path [output_dir]
```

**Output**: `MCM_YYYY_X_TeamName/` directory with:
- `paper/` - LaTeX template files
- `code/` - Python scaffolding
- `data/` - Data folders

**User Prompt**:
```
📁 项目初始化完成
已创建目录: MCM_2026_C_TeamName/

请确认:
- 题目类型: C (Data Insights)
- 年份: 2026
- 团队名: TeamName

是否正确? (是/否/修改)
```

---

### Phase 2: Problem Analysis (调用 Workflow 1)

**Step 1**: Extract problem text
```
Call skill: pdf
Request: Extract all text from [PDF path]
```

**Step 2**: Analyze problem (参考 Workflow 1)
- Identify problem type (A-F)
- Extract tasks (Q1, Q2, Q3...)
- List data files
- Identify constraints
- Recommend 2-4 models

**Output Format**:
```
## 📊 题目分析报告

**年份**: 2026
**题目类型**: C (Data Insights) - 数据洞察型
**置信度**: High

### 任务分解
1. **Q1**: [Task description]
2. **Q2**: [Task description]
3. **Q3**: [Task description]

### 数据文件
- data.csv: [description]

### 约束条件
- 25页限制
- 需要提交备忘录

### 推荐模型
1. **随机森林 (Random Forest)**
   - 适用性: [explanation]
   - O奖案例: 2024 Problem C

2. **LSTM时间序列**
   - 适用性: [explanation]
   - O奖案例: 2023 Problem A

⏸️ 请确认分析结果是否正确? (是/否/修改)
```

---

### Phase 3: Data Exploration (可选，调用 Workflow 2)

**Condition**: If data files provided

**Step 1**: Load and analyze data
```
Call skill: xlsx (for Excel)
Call skill: exploratory-data-analysis (for CSV)
Request: Generate comprehensive EDA report
```

**Step 2**: Summarize findings
- Data scale (rows, columns)
- Key features
- Data quality issues
- Feature types
- Correlations

**Output Format**:
```
## 📈 数据探索报告

**数据集**: data.csv
**规模**: 1,000行 × 15列

### 关键发现
1. **时间范围**: 2020-2024年
2. **主要变量**: [变量列表]
3. **数据质量**: 缺失值占比2.3%
4. **特征类型**: 数值型12个，类别型3个

### 建模建议
- 适合时间序列分析
- 建议标准化处理
- 特征X与Y高度相关(r=0.85)

⏸️ 请确认数据理解是否正确? (是/否/跳过)
```

---

### Phase 4: Model Selection (调用 Workflow 3)

**Action**: Present recommended models from Phase 2

**User Interaction**:
```
## 🎯 模型选择

基于题目分析，推荐以下模型组合:

1. **随机森林 (Random Forest)** ⭐ 推荐
   - 用于: 特征重要性分析 + 基准预测
   - 优势: 可解释性强，适合作为基准

2. **LSTM神经网络**
   - 用于: 时间序列预测
   - 优势: 捕捉长期依赖关系

3. **XGBoost集成学习**
   - 用于: 最终预测优化
   - 优势: 精度高，处理复杂模式

⏸️ 请选择要使用的模型 (输入序号，如: 1,2 或 all):
```

**Output**: Selected model list → saved to `paper/models_selected.md`

---

### Phase 5: Paper Outline Generation

**Action**: Generate complete outline based on:
- `references/paper-structure.md`
- Problem type and tasks
- Selected models

**Output Format**:
```
## 📝 论文大纲

### 1. Summary (1页)
- 问题重述
- 方法概述
- 主要结果

### 2. Introduction (2-3页)
- 2.1 Problem Background
- 2.2 Restatement of Problems
- 2.3 Our Work

### 3. Assumptions and Notations (1-1.5页)
- 3.1 Assumptions
- 3.2 Notations

### 4. Model Development (12-15页)
- 4.1 Model I: 随机森林
- 4.2 Model II: LSTM
- 4.3 Model III: XGBoost

### 5. Results and Analysis (4-5页)
- 5.1 Task 1 Results
- 5.2 Task 2 Results
- 5.3 Task 3 Results

### 6. Sensitivity Analysis (1-1.5页)

### 7. Strengths and Weaknesses (0.5-1页)

### 8. Conclusions (1-2页)

⏸️ 大纲是否需要调整? (是/否)
```

---

### Phase 6: Content Generation (调用 Workflow 4)

**For each section**, generate content using:
1. `templates/latex/sections/*_draft.tex` as base
2. `references/anti-ai-patterns.md` for human-like writing
3. Problem-specific context from analysis

**Generation Order**:
1. Summary
2. Introduction
3. Assumptions
4. Model Development
5. Results
6. Sensitivity
7. Strengths
8. Conclusion

**Progress Display**:
```
📝 正在生成论文内容...

✅ Summary 完成 (300字)
✅ Introduction 完成 (800字)
✅ Assumptions 完成 (5个假设)
✅ Model Development 完成 (3个模型)
⏳ Results 生成中...
```

**Visualization Code Generation**:
For each figure needed:
```python
# Auto-generated for: [figure description]
from templates.visualization import use_mcm_style, save_figure
from templates.visualization.plot_templates import plot_forecast

# TODO: Replace with actual data
fig, ax = plot_forecast(...)
save_figure(fig, "figure_1", output_dir=Path("./figures"))
```

Save to: `code/auto_generated_figures.py`

---

### Phase 7: LaTeX Assembly

**Action**: Assemble complete `paper/main.tex`

**Structure**:
```latex
\documentclass[12pt]{article}
\input{preamble}  % From templates/latex/preamble.tex

\begin{document}

% Summary
\input{sections/summary}

\newpage
\setcounter{page}{1}

% Main Content
\input{sections/introduction}
\input{sections/assumptions}
\input{sections/model}
\input{sections/results}
\input{sections/sensitivity}
\input{sections/strengths}
\input{sections/conclusion}

\bibliographystyle{plain}
\bibliography{sections/references}

\end{document}
```

**Copy Templates**:
- Copy `templates/latex/sections/*_draft.tex` → `paper/sections/*.tex`
- Fill in generated content
- Add TODO markers for missing data

---

### Phase 8: Final Output

**Generate**:
1. Complete LaTeX project in `MCM_YYYY_X_TeamName/`
2. `OVERLEAF_GUIDE.md` (upload instructions)
3. `paper_progress.md` (status tracking)

**Final Report**:
```
🎉 论文生成完成!

📁 输出目录: MCM_2026_C_TeamName/
   ├── paper/
   │   ├── main.tex (完整论文)
   │   ├── preamble.tex
   │   └── sections/
   │       ├── summary.tex
   │       ├── introduction.tex
   │       ├── assumptions.tex
   │       ├── model.tex
   │       ├── results.tex
   │       ├── sensitivity.tex
   │       ├── strengths.tex
   │       └── conclusion.tex
   ├── code/
   │   ├── auto_generated_figures.py
   │   └── data_preprocessing.py
   ├── data/
   │   ├── raw/
   │   └── processed/
   ├── OVERLEAF_GUIDE.md
   └── paper_progress.md

📊 生成统计:
   - 总页数预估: 18-22页
   - 章节数: 8个
   - 模型数: 3个
   - 图表占位: 6个

⚠️ 注意事项:
   1. 所有[TODO]标记需要补充实际数据
   2. 运行 code/auto_generated_figures.py 生成图表
   3. 按照 OVERLEAF_GUIDE.md 上传到Overleaf
   4. 将中文翻译为英文后提交

下一步: 请查看 OVERLEAF_GUIDE.md 开始上传和编译
```

---

### Special Handling

#### Memo/Letter Requirement
If problem requires memo/letter:
```
检测到题目要求提交备忘录

将在 Conclusion 后添加:
\section*{Memorandum}

请提供:
- 收件人: [organization/person]
- 主题: [subject]
- 关键建议: [bullet points]
```

#### Multiple Data Files
```
检测到多个数据文件:
- data1.csv
- data2.xlsx
- supplementary.pdf

将分别分析并整合到Results章节
```

---

## Reference Files

| Script | Purpose |
|--------|---------|
| `scripts/init_project.py` | Initialize project directory |
| `scripts/check_format.py` | Verify PDF format compliance |
| `scripts/auto_evolve.py` | Git commit and push |

---

*MCM-Analysis Skill v2.0 - LLM-Driven Architecture*
