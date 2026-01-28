# Demo: generate_outline.py Usage Guide

The `generate_outline.py` script creates a structured paper outline based on problem type, with recommended models, page allocation, and timeline.

## Basic Usage

```bash
python scripts/generate_outline.py --problem-type C
```

This generates an `outline.md` file in the current directory.

## Command Line Options

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--problem-type` | `-p` | Yes | Problem type (A-F) |
| `--requirements` | `-r` | No | Comma-separated requirements |
| `--title` | `-t` | No | Problem title |
| `--output` | `-o` | No | Output file path |

## Examples by Problem Type

### Type A: Continuous

```bash
python scripts/generate_outline.py -p A -t "Heat Transfer Optimization"
```

Output includes:
- Differential Equations (ODEs/PDEs)
- Linear/Nonlinear Programming
- Monte Carlo Simulation
- Sensitivity Analysis

### Type B: Discrete

```bash
python scripts/generate_outline.py -p B -t "Network Routing Problem"
```

Output includes:
- Graph Theory / Network Models
- Integer Programming
- Dynamic Programming
- Game-theoretic analysis

### Type C: Data Insights

```bash
python scripts/generate_outline.py -p C -t "Customer Behavior Prediction"
```

Output includes:
- Regression Models
- Machine Learning (Random Forest, SVM)
- Time Series (ARIMA, Prophet)
- Clustering (K-means, DBSCAN)

### Type D: Operations Research

```bash
python scripts/generate_outline.py -p D -t "Supply Chain Optimization"
```

### Type E: Sustainability

```bash
python scripts/generate_outline.py -p E -t "Renewable Energy Policy"
```

### Type F: Policy

```bash
python scripts/generate_outline.py -p F -t "Healthcare Resource Allocation"
```

## Adding Requirements

```bash
python scripts/generate_outline.py -p C \
    -r "predict customer churn,identify key factors,recommend interventions" \
    -t "Customer Retention Analysis"
```

This adds a "Specific Requirements" section to the outline.

## Sample Output Structure

The generated `outline.md` includes:

1. **Problem Type Overview**
   - Description
   - Typical topics
   - Recommended models
   - Key techniques

2. **Page Budget**
   - Section-by-section allocation
   - Cumulative page count
   - Buffer for expansion

3. **Detailed Section Outline**
   - Summary (1 page)
   - Introduction (1.5-2 pages)
   - Assumptions (1-1.5 pages)
   - Model Development (5-8 pages)
   - Results (4-6 pages)
   - Sensitivity Analysis (2-3 pages)
   - Strengths/Weaknesses (1-1.5 pages)
   - Conclusions (1-1.5 pages)
   - References (0.5-1 page)

4. **Model Development Strategy**
   - Problem-specific approach

5. **Suggested Timeline**
   - Day 1-5 breakdown

6. **Pre-Submission Checklist**
   - Format requirements
   - Content verification

## Custom Output Path

```bash
python scripts/generate_outline.py -p C -o ./paper/my_outline.md
```

## Workflow Integration

1. Read the problem statement
2. Run `generate_outline.py` with your problem type
3. Customize the generated outline for your specific problem
4. Use as a guide throughout the competition

---
*MCM-Analysis v1.2.2*
