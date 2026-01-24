# MCM/ICM Models Library

A comprehensive reference of mathematical models used in O-award winning papers from 2020-2024.

---

## 1. Optimization Models

### 1.1 Linear Programming (LP)
- **When to use**: Resource allocation, transportation problems, capacity constraints
- **Problem types**: B, D, E
- **Example applications**:
  - Water resource allocation in Colorado River (2022-B)
  - Forest harvesting optimization under carbon constraints (2022-E)
  - Food system optimization with nutrient requirements (2021-E)
- **Key considerations**:
  - Define clear objective function and constraints
  - Ensure linearity; use relaxation for integer variables
  - Consider sensitivity analysis on coefficients

### 1.2 Integer Programming / Mixed-Integer Programming
- **When to use**: Discrete decisions (yes/no), facility location, equipment selection
- **Problem types**: B, D
- **Example applications**:
  - Drone base station location selection (2021-B)
  - Equipment configuration for submersible rescue (2024-B)
- **Key considerations**:
  - Use branch-and-bound or heuristics for large problems
  - Binary variables for selection decisions

### 1.3 Multi-Objective Programming (MOP)
- **When to use**: Conflicting objectives, stakeholder trade-offs
- **Problem types**: B, D, E
- **Example applications**:
  - Water-hydroelectric power sharing among 5 states (2022-B)
  - Great Lakes water level management with 6 stakeholders (2024-D)
  - Food system balancing efficiency, equity, and sustainability (2021-E)
- **Key considerations**:
  - Use Pareto frontier visualization
  - Weight methods (AHP, entropy) for objective aggregation
  - Present multiple solutions for decision-makers

### 1.4 NSGA-II (Non-dominated Sorting Genetic Algorithm)
- **When to use**: Complex multi-objective problems with non-convex Pareto fronts
- **Problem types**: B, D, E
- **Example applications**:
  - Great Lakes optimal water level determination (2024-D)
  - Forest carbon sequestration vs. economic value (2022-E)
  - Equipment configuration optimization (2024-B)
- **Key considerations**:
  - Population size typically 100-500
  - Terminate after 200-500 generations
  - Crowding distance for diversity preservation

### 1.5 Simulated Annealing (SA)
- **When to use**: Large search space, continuous optimization with constraints
- **Problem types**: A
- **Example applications**:
  - Cyclist power distribution across 1164 track segments (2022-A)
- **Key considerations**:
  - Careful temperature schedule design
  - Good for non-convex problems
  - Escape local optima through probabilistic acceptance

### 1.6 Genetic Algorithm (GA)
- **When to use**: Complex optimization, combinatorial problems
- **Problem types**: B, D, E
- **Example applications**:
  - Submersible search equipment selection (2024-B)
  - Forest management harvesting schedule (2022-E)
- **Key considerations**:
  - Crossover and mutation rate tuning
  - Representation design is critical
  - Combine with local search for refinement

---

## 2. Statistical Models

### 2.1 Regression Analysis

#### Linear Regression / Multiple Linear Regression
- **When to use**: Relationship quantification, prediction, variable importance
- **Problem types**: C, D, F
- **Example applications**:
  - Football team performance indicators vs. goal difference (2020-D)
  - Word attributes vs. Wordle difficulty score (2023-C)
- **Key considerations**:
  - Check multicollinearity (VIF)
  - Verify residual assumptions

#### Ridge Regression
- **When to use**: Multicollinearity issues, regularization needed
- **Problem types**: B, F
- **Example applications**:
  - Ocean current field fitting from discrete data (2024-B)
  - Project impact on illegal wildlife trade (2024-F)
- **Key considerations**:
  - Lambda parameter tuning via cross-validation
  - Handles correlated predictors well

### 2.2 Time Series Models

#### ARIMA (AutoRegressive Integrated Moving Average)
- **When to use**: Trend and seasonality in time series, forecasting
- **Problem types**: A, C, D
- **Example applications**:
  - Sea surface temperature prediction for fish migration (2020-A)
  - Ocean current velocity forecasting (2024-B)
  - SDG indicator trend prediction (2023-D)
- **Key considerations**:
  - Stationarity test (ADF test) before modeling
  - ACF/PACF for parameter selection
  - Differencing for non-stationary series

#### Prophet / X-Prophet
- **When to use**: Time series with strong seasonality, holiday effects
- **Problem types**: C
- **Example applications**:
  - Gold and Bitcoin price prediction with XGBoost residual modeling (2022-C)
- **Key considerations**:
  - Handles missing data well
  - Add external regressors for enhanced accuracy
  - Sliding window for volatile markets

#### Grey Prediction Model GM(1,1)
- **When to use**: Limited data points, exponential trends
- **Problem types**: F
- **Example applications**:
  - GGS index future trajectory prediction (2023-F)
- **Key considerations**:
  - Works well with 4-10 data points
  - Assumes exponential underlying pattern

### 2.3 Hypothesis Testing
- **Ljung-Box Q Test**: Autocorrelation detection (2024-C tennis momentum)
- **Runs Test**: Randomness verification (2024-C)
- **t-Test**: Group comparison (2021-D music similarity)
- **Key considerations**:
  - State null hypothesis clearly
  - Report p-values and effect sizes

### 2.4 Bootstrap Simulation
- **When to use**: Uncertainty quantification, confidence intervals
- **Problem types**: A
- **Example applications**:
  - Fish migration path uncertainty with 10000 simulations (2020-A)
- **Key considerations**:
  - Minimum 1000 iterations recommended
  - Generate percentile-based confidence intervals

---

## 3. Machine Learning Models

### 3.1 Classification Models

#### Random Forest / GSRF (Grid-Search Random Forest)
- **When to use**: Non-linear classification/regression, feature importance
- **Problem types**: C
- **Example applications**:
  - Wordle score distribution prediction from word attributes (2023-C)
  - Report classification credibility scoring (2021-C)
- **Key considerations**:
  - Grid search for hyperparameter optimization
  - Feature importance for interpretation
  - Handle class imbalance with class weights

#### Support Vector Machine (SVM) / LSSVM
- **When to use**: Classification with clear margins, small-medium datasets
- **Problem types**: B, C
- **Example applications**:
  - Fire risk prediction SSA-LSSVM (2021-B)
  - Text-based report classification (2021-C)
- **Key considerations**:
  - Kernel selection (RBF, linear)
  - Parameter optimization critical (C, gamma)

#### XGBoost / Gradient Boosting
- **When to use**: Tabular data prediction, feature engineering
- **Problem types**: C
- **Example applications**:
  - Residual modeling in X-Prophet price prediction (2022-C)
- **Key considerations**:
  - Early stopping for overfitting prevention
  - SHAP values for interpretability

### 3.2 Deep Learning Models

#### CNN (Convolutional Neural Network)
- **When to use**: Image classification, visual pattern recognition
- **Problem types**: C
- **Example applications**:
  - Hornet species identification from uploaded photos (2021-C)
- **Key considerations**:
  - Data augmentation for small datasets
  - Transfer learning with pre-trained models (ResNet50)
  - Weighted loss for imbalanced classes

#### GRU (Gated Recurrent Unit)
- **When to use**: Sequence prediction, time series with memory
- **Problem types**: C
- **Example applications**:
  - Daily Wordle report count prediction (2023-C)
- **Key considerations**:
  - Faster than LSTM with similar performance
  - Good for medium-length sequences

#### LSTM (Long Short-Term Memory)
- **When to use**: Long sequence dependencies
- **Problem types**: C
- **Example applications**:
  - Price trend prediction (2022-C alternative)
- **Key considerations**:
  - Handles vanishing gradient problem
  - Bidirectional for enhanced context

### 3.3 Clustering Models

#### K-Means / K-Means++
- **When to use**: Grouping similar items, risk stratification
- **Problem types**: B, C, E, F
- **Example applications**:
  - Fire risk zone division in Victoria (2021-B)
  - Word difficulty classification (2023-C)
  - Country development level clustering (2022-F)
- **Key considerations**:
  - K-Means++ for better initialization
  - Elbow method or silhouette score for K selection
  - Normalize features before clustering

### 3.4 Dimensionality Reduction

#### PCA (Principal Component Analysis)
- **When to use**: Feature reduction, multicollinearity handling
- **Problem types**: D, F
- **Example applications**:
  - GGS index construction from 12 indicators (2023-F)
  - Football team performance factor extraction (2020-D)
- **Key considerations**:
  - Retain components explaining 80-90% variance
  - Interpret principal components meaningfully

---

## 4. Simulation Models

### 4.1 Monte Carlo Simulation
- **When to use**: Uncertainty propagation, risk assessment
- **Problem types**: A, B, E
- **Example applications**:
  - Submersible trajectory uncertainty (2.39% average error) (2024-B)
  - Fish migration path probability distribution (2020-A)
- **Key considerations**:
  - Minimum 1000-10000 iterations
  - Use Latin Hypercube Sampling for efficiency
  - Report confidence intervals

### 4.2 Cellular Automaton (CA)
- **When to use**: Spatial competition, discrete state evolution
- **Problem types**: A, B
- **Example applications**:
  - Fungal decomposition and spatial competition (2021-A)
  - Sandcastle erosion simulation (2020-B)
- **Key considerations**:
  - Define clear state transition rules
  - Grid resolution affects accuracy
  - Computationally efficient vs. PDE approaches

### 4.3 System Dynamics (SD)
- **When to use**: Feedback loops, long-term policy simulation
- **Problem types**: D, E, F
- **Example applications**:
  - Data maturity improvement ROI (2022-D)
  - Higher education policy simulation (2021-F)
  - Plastic waste stock-flow modeling (2020-E)
- **Key considerations**:
  - Use Vensim or STELLA software
  - Stock-flow diagrams for clarity
  - Capture feedback loops and delays

### 4.4 Discrete Event Simulation (DES)
- **When to use**: Queue systems, resource capacity evaluation
- **Problem types**: B
- **Example applications**:
  - Drone fleet response capacity (2021-B)
- **Key considerations**:
  - Define arrival rates and service times
  - Analyze waiting times and utilization

---

## 5. Network Models

### 5.1 Complex Network Analysis

#### PageRank
- **When to use**: Node importance in directed networks
- **Problem types**: D
- **Example applications**:
  - SDG priority ranking based on interconnections (2023-D)
  - Music artist influence ranking (2021-D)
- **Key considerations**:
  - Damping factor typically 0.85
  - Interpretable importance scores

#### Centrality Measures
- **Degree Centrality**: Direct connections
- **Betweenness Centrality**: Bridge nodes
- **Eigenvector Centrality**: Connection quality
- **Problem types**: D
- **Example applications**:
  - Football passing network analysis (2020-D)
  - SDG network hub identification (2023-D)

#### Network Motifs
- **When to use**: Local structural patterns
- **Problem types**: D
- **Example applications**:
  - Triangular passing configurations in football (2020-D)
- **Key considerations**:
  - Compare with random network baseline
  - Statistical significance testing

### 5.2 Correlation Networks
- **When to use**: Relationship mapping between variables
- **Problem types**: A, D
- **Example applications**:
  - Lamprey ecosystem species interaction network (2024-A)
  - SDG synergy and trade-off network (2023-D)
- **Key considerations**:
  - Pearson for linear, Spearman for monotonic
  - Set correlation threshold for edge creation

### 5.3 Network Flow Models
- **When to use**: Resource flow, transportation optimization
- **Problem types**: B, D
- **Example applications**:
  - Great Lakes water cascade network (2024-D)
  - Water-power distribution network (2022-B)
- **Key considerations**:
  - Conservation at each node
  - Capacity constraints on arcs

---

## 6. Differential Equation Models

### 6.1 Ordinary Differential Equations (ODE)

#### Lotka-Volterra Model
- **When to use**: Population dynamics, competition, predator-prey
- **Problem types**: A, B, F
- **Example applications**:
  - Lamprey-host-parasite ecosystem dynamics (2024-A)
  - Maasai-wildlife-livestock interaction (2023-B)
  - Cultural competition EDP assimilation (2020-F)
- **Key considerations**:
  - Parameter sensitivity analysis essential
  - Stability analysis via eigenvalues
  - Consider stochastic extensions

#### Logistic Growth Model
- **When to use**: Bounded growth, carrying capacity
- **Problem types**: A, C, E
- **Example applications**:
  - Forest biomass accumulation (2022-E)
  - Product reputation evolution (2020-C)
  - Plant community succession (2023-A)
- **Key considerations**:
  - Estimate carrying capacity K
  - S-curve interpretation

### 6.2 Partial Differential Equations (PDE)

#### Advection-Diffusion Equation
- **When to use**: Species migration, pollutant transport
- **Problem types**: A
- **Example applications**:
  - Fish migration driven by temperature gradients (2020-A)
- **Key considerations**:
  - Numerical methods (finite difference)
  - Boundary conditions critical

### 6.3 Dynamics Models

#### Newton's Laws / Force Balance
- **When to use**: Physical motion, trajectory prediction
- **Problem types**: A, B
- **Example applications**:
  - Submersible drift trajectory (2024-B)
  - Cyclist power-velocity relationship (2022-A)
- **Key considerations**:
  - Include all relevant forces
  - Validate with physical intuition

#### W' Balance Model (Skiba)
- **When to use**: Athlete fatigue and recovery
- **Problem types**: A
- **Example applications**:
  - Cyclist energy depletion tracking (2022-A)
- **Key considerations**:
  - Critical power threshold
  - Exponential recovery during sub-threshold effort

---

## 7. Evaluation Models

### 7.1 AHP (Analytic Hierarchy Process)
- **When to use**: Subjective weighting, pairwise comparison
- **Problem types**: B, D, E, F
- **Example applications**:
  - Water allocation stakeholder priority (2022-B)
  - Building preservation value assessment (2024-E)
  - Higher education health dimensions (2021-F)
- **Key considerations**:
  - Consistency ratio < 0.1
  - Combine with objective methods (EWM)
  - 9-point scale for comparisons

### 7.2 Entropy Weight Method (EWM)
- **When to use**: Objective weighting based on data dispersion
- **Problem types**: E, F
- **Example applications**:
  - Light pollution risk indicators (2023-E)
  - Global equity index construction (2022-F)
  - Client selection for IWT project (2024-F)
- **Key considerations**:
  - More dispersion = higher weight
  - Combine with AHP for balance

### 7.3 TOPSIS (Technique for Order Preference)
- **When to use**: Multi-criteria ranking, distance to ideal
- **Problem types**: D, E, F
- **Example applications**:
  - Country food system ranking (2021-E)
  - Client organization selection (2024-F)
- **Key considerations**:
  - Normalize data first
  - Define positive and negative ideals
  - Euclidean distance calculation

### 7.4 Fuzzy Comprehensive Evaluation (FCE)
- **When to use**: Uncertain assessments, linguistic variables
- **Problem types**: F
- **Example applications**:
  - Asteroid mining impact assessment (2022-F)
  - State fragility evaluation (2020-F)
- **Key considerations**:
  - Define membership functions
  - Multiple evaluation levels

### 7.5 GE Matrix (General Electric Matrix)
- **When to use**: Strategic positioning, two-dimensional classification
- **Problem types**: E
- **Example applications**:
  - Forest management strategic positioning (2022-E)
  - Plastic impact regional classification (2020-E)
- **Key considerations**:
  - 9-cell matrix (3x3)
  - Industry attractiveness vs. business strength

### 7.6 Coupling Coordination Analysis
- **When to use**: Subsystem balance assessment
- **Problem types**: E
- **Example applications**:
  - Human-society-ecology coordination after light pollution intervention (2023-E)
- **Key considerations**:
  - Coupling degree (interaction strength)
  - Coordination degree (development balance)

### 7.7 Spearman-CRITIC Combination
- **When to use**: Hybrid objective weighting
- **Problem types**: E
- **Example applications**:
  - Building preservation indicator weighting (2024-E)
- **Key considerations**:
  - CRITIC captures conflict and contrast
  - Spearman handles correlation

---

## 8. Probabilistic & Bayesian Models

### 8.1 Bayesian Networks
- **When to use**: Causal inference, latent variables
- **Problem types**: C
- **Example applications**:
  - Dual-temporal tennis momentum prediction with latent psychological variables (2024-C)
- **Key considerations**:
  - Structure learning or expert-defined
  - EM algorithm for latent variables

### 8.2 Bayesian Search Theory
- **When to use**: Sequential search optimization, probability updating
- **Problem types**: B
- **Example applications**:
  - Grid probability search for submersible (2024-B)
- **Key considerations**:
  - Prior probability from prediction
  - Posterior update after each search
  - Parallel sweep patterns

### 8.3 Poisson Process
- **When to use**: Random event occurrence, arrival modeling
- **Problem types**: A, B
- **Example applications**:
  - Drought occurrence timing (2023-A)
  - Fire event arrival rate (2021-B)
- **Key considerations**:
  - Exponential inter-arrival times
  - Rate parameter estimation

### 8.4 SEIR Model (Epidemic Dynamics)
- **When to use**: Information spread, rumor propagation
- **Problem types**: C
- **Example applications**:
  - False hornet report spread modeling (2021-C)
- **Key considerations**:
  - Time-varying transmission rate
  - Link to media exposure (Google Trends)

---

## 9. Ecological Models

### 9.1 MaxEnt (Maximum Entropy)
- **When to use**: Species distribution prediction, presence-only data
- **Problem types**: C
- **Example applications**:
  - Asian Giant Hornet potential habitat prediction (2021-C)
- **Key considerations**:
  - Environmental variable selection
  - AUC for model validation
  - Threshold selection for binary prediction

### 9.2 Niche Models
- **When to use**: Species habitat requirements, competition
- **Problem types**: A
- **Example applications**:
  - Plant community drought survival based on niche width (2023-A)
- **Key considerations**:
  - Niche overlap calculation
  - Resource partitioning

### 9.3 BDS Evaluation Model
- **When to use**: Ecosystem health assessment
- **Problem types**: A
- **Example applications**:
  - Lamprey ecosystem impact: Biomass, Diversity, Stability (2024-A)
- **Key considerations**:
  - Shannon-Wiener Index for diversity
  - Variance-based stability measures

---

## 10. Financial & Risk Models

### 10.1 CAPM (Capital Asset Pricing Model)
- **When to use**: Risk-adjusted pricing, insurance premium
- **Problem types**: E
- **Example applications**:
  - Risk-incorporated insurance premium calculation (2024-E)
- **Key considerations**:
  - Beta coefficient for risk
  - Risk-free rate assumption
  - Bankruptcy probability threshold

### 10.2 Expected Annual Loss (EAL)
- **When to use**: Risk quantification, insurance underwriting
- **Problem types**: E
- **Example applications**:
  - Property insurance sustainability assessment (2024-E)
- **Key considerations**:
  - EAL = Exposure × Frequency × Loss Ratio
  - Historical loss data required

### 10.3 Cost-Benefit Analysis (CBA)
- **When to use**: Policy evaluation, investment decisions
- **Problem types**: B, E, F
- **Example applications**:
  - Drone system economic viability (2021-B)
  - Food system transformation ROI (2021-E)
- **Key considerations**:
  - Discount rate selection
  - Monetize intangible benefits
  - Sensitivity to assumptions

---

## 11. Natural Language Processing (NLP)

### 11.1 Sentiment Analysis

#### VADER (Valence Aware Dictionary)
- **When to use**: Social media text, short reviews
- **Problem types**: C
- **Example applications**:
  - Amazon review sentiment scoring (2020-C)
- **Key considerations**:
  - Handles emojis and slang
  - Pre-built lexicon

#### TF-IDF + Classification
- **When to use**: Keyword extraction, document classification
- **Problem types**: C
- **Example applications**:
  - Hornet report text classification (2021-C)
- **Key considerations**:
  - Combine with SVM or Random Forest
  - Remove stop words

### 11.2 Topic Modeling (LDA)
- **When to use**: Theme extraction from text corpus
- **Problem types**: C
- **Example applications**:
  - Amazon review theme identification (2020-C alternative)
- **Key considerations**:
  - Number of topics selection
  - Coherence score for validation

---

## 12. Project Management Models

### 12.1 Logical Framework Approach (LFA)
- **When to use**: Project design, impact evaluation
- **Problem types**: F
- **Example applications**:
  - STSEA illegal wildlife trade project design (2024-F)
- **Key considerations**:
  - Problem tree and objective tree
  - Logframe matrix with indicators
  - Assumptions and risks

### 12.2 Results-Based Management (RBM)
- **When to use**: Outcome-focused project planning
- **Problem types**: F
- **Example applications**:
  - 5-year IWT reduction project (2024-F)
- **Key considerations**:
  - SMART objectives
  - Theory of change
  - Gantt chart timeline

---

## Quick Reference: Models by Problem Type

| Problem Type | Top Models |
|--------------|------------|
| **A (Continuous)** | Lotka-Volterra, Differential Equations, Monte Carlo, Cellular Automaton, Simulated Annealing |
| **B (Discrete)** | MCLP, Genetic Algorithm, Queuing Theory, Bayesian Search, Multi-objective Programming |
| **C (Data Insights)** | Random Forest, CNN, GRU/LSTM, Sentiment Analysis, K-Means, Time Series (ARIMA/Prophet) |
| **D (Networks/OR)** | PageRank, Network Flow, NSGA-II, System Dynamics, Correlation Networks |
| **E (Sustainability)** | AHP-EWM, TOPSIS, Coupling Coordination, GE Matrix, Risk Models (CAPM, EAL) |
| **F (Policy)** | Entropy Weight Method, Fuzzy Evaluation, LFA/RBM, Game Theory, Lotka-Volterra (cultural) |

---

## Model Selection Decision Tree

```
Is the problem about...

PREDICTION/FORECASTING?
├─ Time series data → ARIMA, Prophet, GRU
├─ Classification → Random Forest, SVM, CNN
└─ Spatial distribution → MaxEnt, Advection-Diffusion

OPTIMIZATION?
├─ Single objective, linear → Linear Programming
├─ Multiple objectives → NSGA-II, MOP
├─ Discrete decisions → Integer Programming, GA
└─ Large search space → Simulated Annealing

EVALUATION/RANKING?
├─ Subjective weights → AHP
├─ Objective weights → Entropy Weight Method
├─ Combined ranking → TOPSIS
└─ Uncertain assessment → Fuzzy Comprehensive Evaluation

DYNAMIC SYSTEMS?
├─ Population/competition → Lotka-Volterra
├─ Growth → Logistic Model
├─ Policy feedback → System Dynamics
└─ Spatial evolution → Cellular Automaton

NETWORKS?
├─ Node importance → PageRank, Centrality
├─ Local patterns → Network Motifs
└─ Resource flow → Network Flow Model

UNCERTAINTY?
├─ Parameter uncertainty → Monte Carlo
├─ Sequential decisions → Bayesian Updating
└─ Confidence intervals → Bootstrap
```

---

*Last updated based on MCM/ICM O-award papers 2020-2024*
