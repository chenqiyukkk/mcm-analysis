# Phase 2: Problem Parser - Usage Guide

## Overview

The `parse_problem.py` script automatically extracts key information from MCM/ICM problem PDFs.

## Features

- **Problem Type Identification**: Automatically classifies problems as A, B, C, D, E, or F
- **Subproblem Extraction**: Identifies Task 1, Task 2, Q1, Q2, etc.
- **Data File Detection**: Finds references to CSV, Excel, and other data files
- **Constraint Extraction**: Identifies requirements and limitations
- **Dual Output**: Generates both JSON (structured) and Markdown (readable) reports

## Installation

```bash
pip install pypdf
# or
pip install pdfplumber
```

## Usage Examples

### 1. Parse a Single PDF

```bash
python scripts/parse_problem.py 2026_MCM_Problem_C.pdf
```

Output:
- `2026_MCM_Problem_C_analysis.json`
- `2026_MCM_Problem_C_analysis.md`

### 2. Specify Output Directory

```bash
python scripts/parse_problem.py problem.pdf -o ./analysis/
```

### 3. Batch Processing

```bash
python scripts/parse_problem.py --batch ./problems/*.pdf
```

### 4. Choose Output Format

```bash
# JSON only
python scripts/parse_problem.py problem.pdf --format json

# Markdown only
python scripts/parse_problem.py problem.pdf --format markdown

# Both (default)
python scripts/parse_problem.py problem.pdf --format both
```

## Output Format

### JSON Output Structure

```json
{
  "year": 2026,
  "problem_type": "C",
  "problem_letter": "C",
  "type_confidence": 0.85,
  "background_domain": "Sports Analytics",
  "subproblems": [
    {
      "id": "Q1",
      "title": "Develop a model to quantify momentum...",
      "description": ""
    }
  ],
  "data_files": [
    "match_data.csv",
    "player_stats.xlsx"
  ],
  "constraints": [
    "Your model must be validated using cross-validation",
    "The maximum length of your paper is 25 pages"
  ],
  "key_terms": [],
  "parsed_at": "2026-01-29T10:00:00",
  "raw_text": "..."
}
```

### Markdown Report

```markdown
# MCM/ICM Problem Analysis Report

**Generated:** 2026-01-29T10:00:00

**Year:** 2026
**Problem Type:** C
**Confidence:** 85%

## Subproblems
- **Q1:** Develop a model to quantify momentum...
- **Q2:** Use your model to predict match outcomes...

## Data Files
- match_data.csv
- player_stats.xlsx

## Constraints
1. Your model must be validated using cross-validation
2. The maximum length of your paper is 25 pages
```

## Integration with Phase 1

After parsing a problem, you can use the analysis to generate a paper skeleton:

```bash
# 1. Parse the problem
python scripts/parse_problem.py 2026_C.pdf -o ./analysis/

# 2. Generate paper skeleton based on analysis
python scripts/generate_paper_skeleton.py \
  --problem C \
  --year 2026 \
  --mode draft \
  -o ./my_paper/
```

## Problem Type Keywords

The parser uses keyword matching to identify problem types:

| Type | Keywords |
|------|----------|
| A | differential equation, dynamical system, population, ecology, physics |
| B | discrete, combinatorial, optimization, scheduling, network, graph |
| C | data, dataset, machine learning, prediction, classification, time series |
| D | network, graph theory, node, edge, centrality, PageRank |
| E | sustainability, environment, climate, risk, carbon, pollution |
| F | policy, social, behavior, stakeholder, game theory, economic |

## Testing

Test with the provided sample:

```bash
# The test sample is in examples/04_problem_parser/test_sample.txt
# To test with a real PDF, download any MCM/ICM problem from the official website
```

## Limitations

- Requires clean PDF text (scanned PDFs may need OCR)
- Problem type classification is heuristic-based
- Subproblem extraction may miss unconventional formatting

## Future Enhancements

- [ ] Support for scanned PDFs (OCR)
- [ ] More sophisticated NLP for constraint extraction
- [ ] Integration with external data sources
- [ ] Automatic model recommendation based on problem type

---

*Phase 2 Complete - MCM-Analysis Skill v1.4.0*
