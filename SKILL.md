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

## Scripts (Minimal)

| Script | Purpose |
|--------|---------|
| `scripts/init_project.py` | Initialize project directory |
| `scripts/check_format.py` | Verify PDF format compliance |
| `scripts/auto_evolve.py` | Git commit and push |

---

*MCM-Analysis Skill v2.0 - LLM-Driven Architecture*
