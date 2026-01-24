---
name: mcm-analysis
description: Use when analyzing MCM/ICM (Mathematical Contest in Modeling) problems, developing mathematical models, writing competition papers, or preparing for COMAP modeling contests. Triggers on keywords like MCM, ICM, mathematical modeling competition, COMAP, or when user provides a modeling competition problem.
---

# MCM/ICM Analysis Skill

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

## Workflow

```
User provides problem (PDF/text)
         │
         ▼
┌─────────────────────────────────────┐
│ PHASE 1: Problem Analysis           │
│                                     │
│ 1. Identify problem type (A-F)      │
│ 2. Extract key requirements         │
│ 3. Identify hidden requirements     │
│ 4. Recommend modeling directions    │
│                                     │
│ Reference: problem-types.md         │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ PHASE 2: Model Selection            │
│                                     │
│ 1. Match problem with models        │
│ 2. Review O-award approaches        │
│ 3. Provide implementation guidance  │
│ 4. Suggest Python code frameworks   │
│                                     │
│ Reference: models-library.md        │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ PHASE 3: Paper Writing              │
│                                     │
│ 1. Generate paper outline           │
│ 2. Apply O-award structure patterns │
│ 3. Use human writing style          │
│ 4. Avoid AI-detectable patterns     │
│                                     │
│ Reference: paper-structure.md       │
│            writing-guide.md         │
│            anti-ai-patterns.md      │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ PHASE 4: Quality Check              │
│                                     │
│ 1. Format compliance (25 pages)     │
│ 2. Section completeness             │
│ 3. Self-evaluation vs criteria      │
│ 4. Citation verification            │
│                                     │
│ Reference: judging-criteria.md      │
│ Script: check_format.py             │
└─────────────────────────────────────┘
```

## Quick Start Commands

### Initialize New Project
```bash
python scripts/init_project.py --problem C --year 2026 --team "YourTeamName"
```

### Generate Paper Outline
```bash
python scripts/generate_outline.py --problem-type C
```

### Check Paper Format
```bash
python scripts/check_format.py paper.pdf
```

### Humanize Draft Text
```bash
python scripts/humanize_text.py --input draft.md --output humanized.md
```

## Problem Type Quick Reference

| Type | Name | Focus | Key Models |
|------|------|-------|------------|
| A | Continuous | Physics, dynamics, optimization | Differential equations, PDE, optimization |
| B | Discrete | Combinatorics, algorithms | Graph theory, integer programming, simulation |
| C | Data Insights | Data analysis, prediction | ML/DL, time series, statistical analysis |
| D | Operations/Network | Logistics, networks | Network optimization, queueing, scheduling |
| E | Sustainability | Environment, ecology | System dynamics, multi-objective optimization |
| F | Policy | Social systems, policy | Game theory, agent-based modeling, AHP |

## Anti-AI Writing Guidelines

### Patterns to AVOID (AI tells)

| AI Pattern | Human Alternative |
|------------|-------------------|
| "It is important to note that..." | State directly |
| "Furthermore, moreover, additionally" (overuse) | Vary connectors or omit |
| "In conclusion, we have demonstrated..." | Specific conclusion statement |
| Perfect parallel structure always | Natural variation |
| All paragraphs same length | Varied paragraph sizes |
| "This paper presents..." | "We analyze..." / "This model..." |

### Patterns to USE (Human tells)

1. **Vary sentence length**: Mix short (under 15 words) with longer complex sentences
2. **Show thinking process**: "We initially considered X, but found Y more suitable because..."
3. **Acknowledge limitations honestly**: "Due to time constraints..." / "Data limitations prevented..."
4. **Use specific numbers**: "23.7% improvement" not "significant improvement"
5. **Domain terminology**: Use field-specific jargon appropriately
6. **First-person plural**: "We found..." "Our model shows..."

## Integrated Skills

This skill automatically integrates with:

| Skill | Integration |
|-------|-------------|
| `pdf` | Read problem PDFs, generate final papers |
| `research-lookup` | Search for relevant literature and data |
| `scientific-writing` | Academic writing patterns |
| `scientific-visualization` | Professional figure generation |
| `planning-with-files` | Task tracking during competition |

## Reference Files

| File | Purpose |
|------|---------|
| `references/models-library.md` | 50+ models categorized by type |
| `references/problem-types.md` | Historical patterns for A-F problems |
| `references/paper-structure.md` | O-award paper structure templates |
| `references/writing-guide.md` | Academic writing phrases and patterns |
| `references/anti-ai-patterns.md` | Human writing style guide |
| `references/judging-criteria.md` | COMAP official judging standards |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/init_project.py` | Initialize project directory with LaTeX template |
| `scripts/generate_outline.py` | Generate problem-specific outline |
| `scripts/check_format.py` | Verify PDF format compliance |
| `scripts/humanize_text.py` | Reduce AI patterns in text |

## Usage Examples

### Example 1: Analyze a New Problem

**User**: 这是2026年MCM的C题，请帮我分析 [provides problem text]

**Response Pattern**:
1. 识别题型和核心要求（用中文）
2. 分解子问题
3. 识别隐含要求
4. 推荐建模方向
5. 提供类似历年题目参考

### Example 2: Model Selection Guidance

**User**: C题应该用什么模型？

**Response Pattern**:
1. 根据题目特点推荐 3-5 个适合的模型
2. 每个模型说明：适用场景、优缺点、O奖案例
3. 提供 Python 代码框架
4. 建议模型组合策略

### Example 3: Writing Assistance

**User**: 帮我写Introduction部分

**Response Pattern**:
1. 用中文生成草稿
2. 遵循 paper-structure.md 的结构
3. 应用 anti-ai-patterns.md 的人性化技巧
4. 标注英文术语
5. 提供修改建议

## Competition Timeline Guidance

| Day | Focus | This Skill Helps With |
|-----|-------|----------------------|
| Day 1 (Thu PM) | Problem analysis, model selection | Phase 1 + Phase 2 |
| Day 2 (Fri) | Core modeling, initial coding | Model guidance, code templates |
| Day 3 (Sat) | Results, sensitivity analysis | Visualization, validation |
| Day 4 (Sun) | Writing, polishing | Phase 3 + Phase 4 |
| Day 5 (Mon AM) | Final review, submission | Format check, quality review |

## Important Reminders

1. **25 Page Limit**: Includes EVERYTHING (summary, content, references, appendices)
2. **No Identifying Info**: Team number only, no names or school names
3. **AI Disclosure Required**: Must include "Report on Use of AI" section (not counted in 25 pages)
4. **Deadline is HARD**: 9:00 PM EST Monday - no exceptions
5. **Summary is Critical**: Judges weight summary heavily - write it LAST but make it BEST

## Judging Levels (Lowest to Highest)

1. **Unsuccessful** - Did not address requirements
2. **Successful Participant** - Made effort but has deficiencies  
3. **Honorable Mention** - Above average, sound processes
4. **Meritorious** - Excellent in many aspects
5. **Finalist** - Exemplary, reached final judging round
6. **Outstanding Winner** - Best of the best
