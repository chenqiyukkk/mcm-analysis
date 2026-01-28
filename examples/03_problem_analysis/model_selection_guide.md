# Model Selection Guide

A decision tree approach to choosing the right models for your MCM/ICM problem.

## Quick Selection by Problem Type

| Type | First Choice | Alternative | Visualization |
|------|--------------|-------------|---------------|
| A | Differential Equations | Monte Carlo, SA | Phase Portrait |
| B | Graph Theory, Integer Programming | Queuing, GA | Network Graph |
| C | ML (Random Forest, XGBoost) | Time Series | Heatmap, Time Series |
| D | Network Flow, NSGA-II | PageRank | Network, Pareto |
| E | System Dynamics, AHP-EWM | TOPSIS, FCE | Sensitivity Tornado |
| F | Game Theory, Agent-Based | LFA, RBM | Network, Tornado |

## Decision Tree

```
START
  │
  ├── Is it a PREDICTION problem?
  │     ├── Time series data?
  │     │     ├── Linear trends → ARIMA
  │     │     ├── Seasonality → Prophet, SARIMA
  │     │     └── Complex patterns → GRU, LSTM
  │     │
  │     └── Classification/Regression?
  │           ├── Tabular data → Random Forest, XGBoost
  │           ├── Image data → CNN
  │           └── Text data → TF-IDF + SVM, LDA
  │
  ├── Is it an OPTIMIZATION problem?
  │     ├── Single objective?
  │     │     ├── Linear constraints → Linear Programming
  │     │     ├── Discrete decisions → Integer Programming
  │     │     └── Non-convex → Genetic Algorithm, SA
  │     │
  │     └── Multiple objectives?
  │           ├── Conflicting goals → NSGA-II
  │           ├── Weighted sum → AHP + LP
  │           └── Visualize trade-offs → Pareto Frontier
  │
  ├── Is it an EVALUATION/RANKING problem?
  │     ├── Subjective criteria → AHP
  │     ├── Data-driven weights → Entropy Weight Method
  │     ├── Distance to ideal → TOPSIS
  │     └── Uncertain assessments → Fuzzy Comprehensive Evaluation
  │
  ├── Is it a DYNAMIC SYSTEM?
  │     ├── Population/ecology → Lotka-Volterra
  │     ├── Growth with limits → Logistic Model
  │     ├── Spatial evolution → Cellular Automaton
  │     └── Policy feedback → System Dynamics (Vensim)
  │
  ├── Is it a NETWORK problem?
  │     ├── Node importance → PageRank, Centrality
  │     ├── Community structure → Louvain Algorithm
  │     ├── Resource flow → Max Flow, Min Cost Flow
  │     └── Local patterns → Network Motifs
  │
  └── Need UNCERTAINTY quantification?
        ├── Parameter uncertainty → Monte Carlo Simulation
        ├── Sequential decisions → Bayesian Updating
        └── Confidence intervals → Bootstrap
```

## Detailed Selection Criteria

### For Prediction Tasks

| Criterion | Model | When to Use |
|-----------|-------|-------------|
| Small data (<100 samples) | Linear Regression | Simple relationships |
| Medium data + interpretability | Random Forest | Feature importance needed |
| Large data + accuracy | XGBoost, LightGBM | Kaggle-style competitions |
| Sequence data | ARIMA, GRU | Time-dependent patterns |
| Limited data points (4-10) | Grey GM(1,1) | Exponential trends |

### For Optimization Tasks

| Criterion | Model | When to Use |
|-----------|-------|-------------|
| Linear + continuous | LP (scipy.optimize.linprog) | Resource allocation |
| Yes/No decisions | Integer Programming | Facility location |
| 2-3 objectives | NSGA-II | Trade-off analysis |
| Large search space | Genetic Algorithm | Complex constraints |
| Physical systems | Simulated Annealing | Continuous + constraints |

### For Evaluation Tasks

| Criterion | Model | When to Use |
|-----------|-------|-------------|
| Expert judgment available | AHP | Subjective weighting |
| Data dispersion matters | Entropy Weight Method | Objective weighting |
| Need ranking | TOPSIS | Distance-based comparison |
| Multiple dimensions | Fuzzy Evaluation | Linguistic variables |
| Combine subjective + objective | AHP-EWM Combination | Best of both |

## Model Combination Strategies

### Strategy 1: Hierarchical

```
Problem
  ├── Layer 1: Data Preprocessing
  │     └── PCA for dimensionality reduction
  │
  ├── Layer 2: Core Model
  │     └── NSGA-II for optimization
  │
  └── Layer 3: Validation
        └── Monte Carlo for uncertainty
```

### Strategy 2: Ensemble

```
Multiple Models → Voting/Averaging → Final Result

Example:
  Random Forest     ─┐
  XGBoost           ─┼→ Weighted Average → Prediction
  Neural Network    ─┘
```

### Strategy 3: Pipeline

```
Data → Clustering → Per-Cluster Model → Integration

Example:
  K-Means → Cluster 1 → ARIMA
         → Cluster 2 → Prophet
         → Cluster 3 → Linear Regression
```

## Common Model Pairs

| Problem Type | Model 1 + Model 2 |
|--------------|-------------------|
| Type A | Lotka-Volterra + Monte Carlo |
| Type B | Network Flow + Genetic Algorithm |
| Type C | Random Forest + ARIMA |
| Type D | NSGA-II + PageRank |
| Type E | AHP-EWM + TOPSIS |
| Type F | Game Theory + System Dynamics |

## Model Selection Checklist

- [ ] Does the model fit the problem structure?
- [ ] Do you have enough data for the model?
- [ ] Can you interpret and explain the results?
- [ ] Is there precedent from O-award papers?
- [ ] Can you implement it in the time available?
- [ ] Does it produce visualizable outputs?

## References

See `references/models-library.md` for detailed descriptions of each model with O-award examples.

---
*MCM-Analysis v1.2.2 - Model Selection Guide*
