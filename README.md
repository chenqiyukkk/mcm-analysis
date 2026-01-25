# MCM-Analysis Skill

A comprehensive AI skill for Mathematical Contest in Modeling (MCM) and Interdisciplinary Contest in Modeling (ICM) teams. Designed to help beginner teams produce O-award quality papers.

## Features

- **Problem Analysis**: Identify problem type (A-F), extract requirements, recommend models
- **Model Library**: 50+ models with usage guidance from O-award papers
- **Visualization Engine**: Publication-quality matplotlib templates (A-F specific) based on O-award styles
- **Paper Writing**: O-award structure templates with human-like writing style
- **Anti-AI Patterns**: Guidelines to make AI-assisted writing appear more natural
- **Format Checking**: Automated compliance verification (25-page limit, headers, etc.)
- **Python Scripts**: Project initialization, outline generation, format checking

## Installation

Copy this folder to your OpenCode skills directory:

```bash
# For OpenCode
~/.config/opencode/skills/mcm-analysis/

# For Claude Code
~/.claude/skills/mcm-analysis/
```

## Quick Start

### Initialize a New Project
```bash
python scripts/init_project.py --problem C --year 2026 --team "YourTeam"
```

### Generate Paper Outline
```bash
python scripts/generate_outline.py --problem-type C
```

### Check Paper Format
```bash
python scripts/check_format.py paper.pdf
```

### Humanize AI-Generated Text
```bash
python scripts/humanize_text.py --input draft.md --output humanized.md
```

## File Structure

```
mcm-analysis/
├── SKILL.md                          # Main skill instructions
├── references/
│   ├── models-library.md             # 50+ models categorized
│   ├── problem-types.md              # A-F problem type patterns
│   ├── paper-structure.md            # O-award paper structure
│   ├── writing-guide.md              # Academic writing guide
│   ├── anti-ai-patterns.md           # Human writing patterns
│   ├── visualization-guide.md        # Chart selection & design guide
│   └── judging-criteria.md           # COMAP judging standards
├── templates/
│   └── visualization/                # Plotting templates & styles
│       ├── mcm_style.mplstyle        # Publication style preset
│       ├── style_config.py           # Color palettes & helpers
│       └── plot_templates/           # Core chart templates (time_series, etc.)
└── scripts/
    ├── init_project.py               # Project initializer with LaTeX
    ├── generate_outline.py           # Outline generator
    ├── check_format.py               # Format compliance checker
    └── humanize_text.py              # AI pattern reducer
```

## Key Design Decisions

1. **Output Language**: Generated content is in **Chinese** for team review; translation handled separately
2. **Anti-AI Writing**: Built-in patterns to avoid detectable AI writing styles
3. **Based on Real Data**: Patterns extracted from 60+ O-award papers (2020-2024)
4. **Beginner Friendly**: Complete templates, scripts, and checklists

## Problem Types Reference

| Type | Name | Focus |
|------|------|-------|
| A | Continuous | Physics, dynamics, optimization |
| B | Discrete | Combinatorics, algorithms |
| C | Data Insights | Data analysis, ML, prediction |
| D | Operations/Network | Logistics, networks, OR |
| E | Sustainability | Environment, ecology |
| F | Policy | Social systems, policy modeling |

## License

MIT License - Feel free to use and modify.

## Contributing

Issues and pull requests welcome!
