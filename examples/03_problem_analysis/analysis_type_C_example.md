# Problem Analysis Example: 2024-C Tennis Momentum

This example demonstrates how to analyze an MCM Type C (Data Insights) problem using the MCM-Analysis skill workflow.

## Problem Summary

**2024 MCM Problem C: Tennis Momentum**

> Analyze momentum in tennis matches. Is "momentum" real? Can we predict match outcomes based on momentum shifts?

## Phase 1: Problem Type Identification

### Quick Classification

| Aspect | Analysis |
|--------|----------|
| **Type** | C (Data Insights) |
| **Core Task** | Pattern recognition, prediction, causality analysis |
| **Data Format** | Match statistics, point-by-point data |
| **Key Challenge** | Defining and measuring "momentum" |

### Requirements Extraction

From the problem statement, we identify:

1. **Q1**: Define and measure momentum in tennis
2. **Q2**: Test if momentum exists statistically
3. **Q3**: Predict match outcomes using momentum
4. **Q4**: Analyze factors affecting momentum
5. **Q5**: Apply insights to coaching strategy

## Phase 2: Model Selection

Based on Type C characteristics, recommended approaches:

### Primary Models

| Model | Purpose | Why |
|-------|---------|-----|
| **Time Series Analysis** | Detect momentum patterns | Captures temporal dynamics |
| **Statistical Hypothesis Testing** | Validate momentum existence | Runs Test, Ljung-Box Q Test |
| **Machine Learning (Random Forest)** | Predict outcomes | Handles non-linear relationships |
| **Bayesian Networks** | Model psychological factors | Captures latent variables |

### Decision Path

```
Problem involves temporal data?
  └─ YES → Time Series Approach
      ├─ Pattern detection? → ARIMA, Rolling statistics
      └─ Prediction? → ML models (RF, XGBoost)

Need to prove statistical existence?
  └─ YES → Hypothesis Testing
      ├─ Autocorrelation? → Ljung-Box Q Test
      └─ Randomness? → Runs Test, Bootstrap

Hidden/latent variables?
  └─ YES → Bayesian Network
      └─ Model psychological momentum
```

## Phase 3: Momentum Definition Framework

### Option A: Point-Based Momentum

```python
# Rolling window approach
def calculate_momentum(points_won, window=10):
    """Calculate momentum as rolling win rate minus baseline."""
    baseline = 0.5  # Expected 50-50 in balanced play
    rolling_rate = points_won.rolling(window).mean()
    momentum = rolling_rate - baseline
    return momentum
```

### Option B: Game-Level Momentum

```python
# Game-based approach
def game_momentum(games_in_set, recent_n=3):
    """Momentum from recent game outcomes."""
    recent_wins = games_in_set[-recent_n:].sum()
    return (recent_wins / recent_n) - 0.5
```

### Option C: Psychological Momentum (O-Award Approach)

The 2024 O-award papers used **Dual-Temporal Bayesian Networks**:

1. **Short-term momentum**: Last 4-5 points
2. **Long-term momentum**: Set/game level trends
3. **Latent psychological state**: Modeled via EM algorithm

## Phase 4: Statistical Validation

### Runs Test for Randomness

```python
from scipy.stats import mannwhitneyu

def runs_test(sequence):
    """Test if point outcomes are random or show momentum patterns."""
    # If p < 0.05, reject randomness → momentum may exist
    n_runs = count_runs(sequence)
    expected = expected_runs(sequence)
    # Compare observed vs expected runs
    return p_value
```

### Ljung-Box Q Test

```python
from statsmodels.stats.diagnostic import acorr_ljungbox

def test_autocorrelation(point_sequence, lags=10):
    """Test for momentum via autocorrelation."""
    result = acorr_ljungbox(point_sequence, lags=[lags])
    # If p < 0.05, significant autocorrelation → momentum exists
    return result['lb_pvalue'].values[0]
```

## Phase 5: Visualization Recommendations

For this problem, use:

| Visualization | Purpose |
|---------------|---------|
| Time Series Plot | Show momentum over match duration |
| Heatmap | Correlation between momentum and outcomes |
| Confusion Matrix | Prediction model performance |
| Sensitivity Tornado | Key factor importance |

### Example: Momentum Time Series

```python
from templates.visualization.plot_templates import plot_forecast

# Plot momentum evolution with confidence intervals
fig, ax = plot_forecast(
    time_historical=points[:100],
    values_historical=momentum[:100],
    time_forecast=points[100:],
    values_forecast=predicted_momentum,
    ci_lower=ci_lower,
    ci_upper=ci_upper,
    title="Match Momentum Evolution",
    xlabel="Point Number",
    ylabel="Momentum Score"
)
```

## Phase 6: Paper Structure for Type C

| Section | Pages | Content Focus |
|---------|-------|---------------|
| Summary | 1 | Key findings on momentum existence |
| Introduction | 2 | Sports analytics background |
| Assumptions | 1 | What "momentum" means |
| Model 1: Definition | 2 | Mathematical momentum framework |
| Model 2: Testing | 2 | Statistical validation |
| Model 3: Prediction | 3 | ML-based outcome prediction |
| Results | 3 | Key matches analysis |
| Sensitivity | 1.5 | Window size, threshold effects |
| Strengths/Weaknesses | 1 | Model limitations |
| Conclusion | 1.5 | Coaching recommendations |
| References | 1 | |

## Key Takeaways

1. **Define clearly**: Momentum must have a mathematical definition
2. **Validate statistically**: Use hypothesis tests to prove existence
3. **Predict outcomes**: Build predictive models for practical value
4. **Visualize effectively**: Time series and heatmaps are essential
5. **Consider psychology**: Latent variable models add depth

---
*MCM-Analysis v1.2.2 - Type C Analysis Example*
