---
name: mcm-analysis
description: Use when analyzing MCM/ICM (Mathematical Contest in Modeling) problems, developing mathematical models, writing competition papers, or preparing for COMAP modeling contests. Triggers on keywords like MCM, ICM, mathematical modeling competition, COMAP, or when user provides a modeling competition problem.
---

# MCM/ICM Analysis Skill v2.1

> **Architecture**: LLM-driven workflow with external skill integration
> **Philosophy**: Scripts handle I/O, LLM handles intelligence
> **Version 2.1 Update**: Visual-First Workflow & Deep Content Templates

A comprehensive skill for Mathematical Contest in Modeling (MCM) and Interdisciplinary Contest in Modeling (ICM) teams. Designed to help beginner teams produce O-award quality papers.

## Overview

This skill provides end-to-end support for MCM/ICM competition:
- **Problem Analysis**: Identify problem type, extract requirements, recommend models
- **Modeling Guidance**: Match problems with proven modeling approaches
- **Visual Planning**: Force-planning of O-award mandatory figures
- **Paper Writing**: Generate outlines, provide *deep* writing templates, ensure human-like output
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
| `perplexity-search` | Find literature and data | Literature review, data sourcing |

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

Read `references/paper-structure.md` and `templates/latex/sections_deep/` for detailed guidelines.

#### Step 2: Generate Content (Deep Mode)

**For each section, use the new Deep Templates:**

1. **Introduction (引言)**
   - Use `templates/latex/sections_deep/introduction_deep.tex`
   - MUST include: Problem Background (with data), Literature Review (with table), Restatement, Our Work (with Flowchart).

2. **Assumptions (假设)**
   - Use `templates/latex/sections_deep/model_deep.tex`
   - 4-6 Assumptions, each with Justification.

3. **Model (模型建立)**
   - Use `templates/latex/sections_deep/model_deep.tex`
   - MUST include: Mindmap for each model, Formula derivation, Algorithm pseudocode.

4. **Results (结果)**
   - Use `templates/latex/sections_deep/results_deep.tex`
   - Separate subsections for each Task.
   - MUST include: Visual results, quantitative analysis.

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

Read `references/visualization-guide.md` for problem-type-specific recommendations and O-Award Checklist.

#### Step 2: Recommend Chart Types

Based on data and analysis needs:

| Purpose | Recommended Chart | Template |
|---------|------------------|----------|
| **Flowchart** | Workflow Diagram | `templates/visualization/plot_templates/flowchart.py` |
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
fig, ax = plot_forecast(...)

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

Against `references/o-award-checklist.md`:

**Completeness Checklist:**
- [ ] Summary Sheet (1 page)
- [ ] **Figure 3: Workflow Diagram** (Critical!)
- [ ] **Figure 2: Literature Review Table**
- [ ] **Figure 5+: Model Framework Diagrams**
- [ ] Algorithm Pseudocode
- [ ] Sensitivity Analysis (Tornado/Heatmap)
- [ ] References (7-15 citations)

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

## Workflow 7: Full Paper Generation Pipeline (v2.1 Visual-First)

### Trigger Conditions
- User says: "生成论文", "写完整论文", "一键建模", "从题目到论文"
- User provides: PDF path `[+ data file path]`

### Pipeline Overview

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

---

### Phase 2: Problem Analysis (调用 Workflow 1)

**Step 1**: Extract problem text (skill: `pdf`)
**Step 2**: Analyze problem (Type, Tasks, Constraints)
**Step 3**: Recommend Models

**Output Format**: (Structured Analysis Report)

---

### Phase 2.5: Visual Planning (NEW - Critical) ⭐

**Action**: Before writing a single word, plan the figures!

**Steps**:
1. Read `references/visualization-guide.md`.
2. Generate a **Figure List** for the paper.
3. **MUST INCLUDE**:
   - Figure 1: Problem Background
   - Figure 2: Literature Review Table
   - Figure 3: Workflow Diagram (using `flowchart.py`)
   - Figure 4: Data Visualization
   - Figure 5+: Model Frameworks

**User Prompt**:
```
📊 视觉规划完成
规划图表: 15张
1. [ ] Figure 1: ...
2. [ ] Figure 2: ...
3. [ ] Figure 3: Workflow Diagram (代码已准备)
...
⏸️ 请确认视觉规划? (是/否/调整)
```

---

### Phase 3: Data Exploration (Optional)

**Condition**: If data files provided
**Action**: Load, Analyze, Visualize (Workflow 2)

---

### Phase 3.5: Literature Search (NEW) ⭐

**Action**: Search for real academic references.

**Steps**:
1. Call `perplexity-search` skill.
2. Query: "[Problem Topic] mathematical modeling review".
3. Save 3-5 key references to `references.bib`.
4. Generate comparison table content for Literature Review.

---

### Phase 4: Model Selection & Architecture

**Action**: Present recommended models and how they connect.

---

### Phase 5: Paper Outline Generation

**Action**: Generate outline using **Deep Templates**.

**Structure**:
- 1. Introduction (Background, Lit Review, Restatement, Our Work)
- 2. Model Preparation (Assumptions, Notations, Data)
- 3. Model Establishment (Model I, Model II, Algorithm)
- 4. Results (Task 1, Task 2, Task 3, Validation)
- 5. Evaluation (Sensitivity, Strengths, Weaknesses)
- 6. Conclusion

---

### Phase 6: Content Generation (Deep Mode)

**For each section**, generate content using:
1. `templates/latex/sections_deep/*.tex` as base.
2. `references/literature-review-guide.md` for Intro.
3. `references/validation-patterns.md` for Results.
4. `references/anti-ai-patterns.md` for style.

**Generation Order**:
1. Introduction (fill deep subsections)
2. Model Preparation
3. Model Establishment (fill deep subsections)
4. Results (fill per Task)
5. Sensitivity
6. Strengths/Conclusion
7. **Summary Sheet (Write LAST)**

**Visualization Code Generation**:
For the mandatory figures planned in Phase 2.5, generate Python code.

---

### Phase 6.5: Thickness Check (NEW) ⭐

**Action**: Verify word counts.

**Targets**:
- Introduction: >800 words
- Model: >2500 words
- Results: >1000 words
- **Total**: >6000 words (approx 20 pages)

---

### Phase 7: LaTeX Assembly

**Action**: Assemble complete `paper/main.tex`.

---

### Phase 8: Final Output

**Generate**:
1. Complete LaTeX project
2. `OVERLEAF_GUIDE.md`
3. `paper_progress.md`

**Final Report**:
```
🎉 论文生成完成!

📊 质量自评:
   - 总页数预估: 22页 (O奖标准)
   - 图表数量: 16张
   - 引用数量: 12条
   - 必需元素: Workflow(✅), Lit Review(✅), Pseudocode(✅)

下一步: 请查看 OVERLEAF_GUIDE.md 开始上传和编译
```

---

## Reference Files

| File | Purpose |
|------|---------|
| `references/models-library.md` | 50+ models categorized by type |
| `references/visualization-guide.md` | **Mandatory Figure Checklist** & Templates |
| `references/literature-review-guide.md` | How to write academic reviews |
| `references/validation-patterns.md` | How to validate models quantitatively |
| `references/o-award-checklist.md` | **Final Quality Control Checklist** |
| `references/paper-structure.md` | Structure templates |
| `references/writing-guide.md` | Academic writing phrases |
| `references/anti-ai-patterns.md` | Human writing style guide |

---

*MCM-Analysis Skill v2.1 - Visual-First & Deep Content*

---

### ⚠️ Flow Integrity Check

**Before claiming paper is ready, verify ALL phases are completed:**

| Phase | Status Check |
|-------|-------------|
| Phase 1 | `paper/` directory exists |
| Phase 2 | `paper_progress.md` shows "Problem Analysis: ✅" |
| Phase 2.5 | At least 10 figures in `paper/figures/` |
| Phase 6 | Each .tex file has >100 lines of actual content |
| Phase 6.5 | Total word count >6000 |

**If any check fails, the paper generation is INCOMPLETE.**
