# Mini Case Study: Water Resource Optimization

A simplified end-to-end MCM workflow demonstration using a water allocation problem.

## Problem Statement (Simplified)

> Three states share a river system. Each state has different water needs (agriculture, industry, municipal). Design an optimal allocation strategy that balances economic benefit, environmental sustainability, and equity.

**Problem Type**: D/E hybrid (Operations + Sustainability)

## Day 1: Problem Analysis (Hours 0-8)

### Step 1: Read and Understand

**Key Requirements Identified:**

1. Model water supply and demand for 3 states
2. Optimize allocation for multiple objectives
3. Consider environmental flow requirements
4. Ensure fairness among states

### Step 2: Generate Outline

```bash
python scripts/generate_outline.py -p D -t "Water Resource Allocation" \
    -r "model supply/demand,multi-objective optimization,environmental constraints,equity"
```

### Step 3: Model Selection

Using the decision tree:

```
Optimization problem? → YES
Multiple objectives? → YES
  ├── Economic benefit
  ├── Environmental sustainability
  └── Equity among states

Selected: NSGA-II + AHP for objective weighting
Validation: Monte Carlo for uncertainty
```

## Day 2: Model Development (Hours 8-24)

### Step 4: Mathematical Formulation

**Decision Variables:**
- $x_i$ = water allocation to state $i$ (million m³)

**Objective Functions:**
1. Maximize economic benefit: $\max Z_1 = \sum_i b_i \cdot x_i$
2. Minimize environmental impact: $\min Z_2 = f_{env}(x)$
3. Maximize equity (minimize variance): $\min Z_3 = \text{Var}(x_i / d_i)$

**Constraints:**
- Total allocation ≤ available supply: $\sum_i x_i \leq S$
- Minimum allocation: $x_i \geq x_i^{min}$
- Environmental flow: $S - \sum_i x_i \geq E_{min}$

### Step 5: Implementation

```python
# Simplified NSGA-II implementation
import numpy as np

def evaluate_allocation(x):
    """Evaluate three objectives for allocation x."""
    # x = [x1, x2, x3] allocations to 3 states
    
    # Objective 1: Economic benefit (maximize → minimize negative)
    benefits = [2.5, 3.0, 2.0]  # benefit per unit water
    z1 = -np.dot(benefits, x)
    
    # Objective 2: Environmental impact (minimize)
    total_use = np.sum(x)
    z2 = total_use / 100  # Simplified: more use = more impact
    
    # Objective 3: Equity (minimize variance in satisfaction ratio)
    demands = [30, 40, 25]  # demands for 3 states
    satisfaction = x / demands
    z3 = np.var(satisfaction)
    
    return [z1, z2, z3]

# Constraints
def constraints(x):
    supply = 70  # Total available
    env_flow = 10  # Minimum environmental
    min_alloc = [10, 15, 8]  # Minimum per state
    
    c1 = supply - np.sum(x) - env_flow  # >= 0
    c2 = x - min_alloc  # >= 0 for all
    return c1, c2
```

## Day 3: Results and Visualization (Hours 24-48)

### Step 6: Generate Pareto Front

```python
from templates.visualization.plot_templates import plot_pareto_frontier

# After running NSGA-II, visualize trade-offs
fig, ax = plot_pareto_frontier(
    x=economic_benefit,
    y=environmental_impact,
    xlabel="Economic Benefit ($M)",
    ylabel="Environmental Impact Score",
    title="Water Allocation Trade-offs",
    highlight_pareto=True
)
```

### Step 7: Sensitivity Analysis

```python
from templates.visualization.plot_templates import plot_tornado

parameters = ["Supply Level", "State 1 Demand", "State 2 Demand", 
              "Env. Flow Req.", "Benefit Rate"]
              
fig, ax = plot_tornado(
    parameters=parameters,
    low_values=[...],
    high_values=[...],
    baseline=optimal_value,
    title="Optimal Allocation Sensitivity"
)
```

## Day 4: Writing (Hours 48-72)

### Step 8: Structure Based on Outline

| Section | Key Content |
|---------|-------------|
| Summary | 3-objective NSGA-II, Pareto solutions, recommendations |
| Introduction | Water scarcity context, problem importance |
| Assumptions | Linear benefits, known demands, steady supply |
| Model | NSGA-II formulation, AHP weighting |
| Results | Pareto front, 3 recommended solutions |
| Sensitivity | Supply level is most critical parameter |
| Conclusion | Balanced allocation achieves 85% of max benefit |

### Step 9: Humanize Text

```bash
python scripts/humanize_text.py -i draft.md -o final.md --report changes.txt
```

## Day 5: Final Check (Hours 72-80)

### Step 10: Format Verification

```bash
python scripts/check_format.py paper.pdf --verbose
```

Expected output:
```
[PASS] Page count: 22/25
[PASS] Team number header found
[PASS] Summary section detected
[PASS] References section detected
[WARN] Possible school names detected (check manually)
```

## Final Deliverables

```
project/
├── paper/
│   ├── main.pdf              # Final submission
│   └── figures/
│       ├── pareto_frontier.png
│       ├── sensitivity_tornado.png
│       └── allocation_map.png
│
├── code/
│   ├── nsga2_optimizer.py    # Main optimization
│   ├── ahp_weights.py        # Objective weighting
│   └── visualization.py      # All plots
│
└── data/
    ├── raw/water_data.csv
    └── processed/results.csv
```

## Lessons Learned

1. **Start with simple model**: Linear approximations first, add complexity later
2. **Visualize early**: Pareto front helped understand trade-offs
3. **Sensitivity matters**: Shows which data to trust
4. **Humanize at end**: Don't over-process draft versions

---
*MCM-Analysis v1.2.2 - Mini Case Study*
