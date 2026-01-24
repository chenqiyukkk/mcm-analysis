# MCM/ICM Problem Types Guide

A comprehensive reference for understanding and approaching each problem type based on 2020-2024 competition patterns.

---

## Problem A: Continuous (MCM)

### Characteristics
- **Core theme**: Physical/biological systems with continuous variables
- **Common domains**: Ecology, physics, environmental science
- **Mathematical focus**: Differential equations, dynamical systems, optimization
- **Data availability**: Usually minimal or no provided data; requires literature research

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Lamprey Sex Ratio Adaptation | Ecosystem dynamics, adaptive mechanisms, stability analysis |
| 2023 | Drought-Stricken Plant Communities | Multi-species competition, environmental stress, biodiversity |
| 2022 | Cyclist Power Profile | Physical dynamics, optimization, fatigue modeling |
| 2021 | Fungal Decomposition | Species interaction, spatial dynamics, environmental sensitivity |
| 2020 | Fish Migration (Moving North) | Climate-driven migration, economic impact, forecasting |

### Recommended Models (Top 5 from O-Award Papers)
1. **Lotka-Volterra Models** - Species interaction, competition, predator-prey dynamics
2. **Differential Equations** - Population dynamics, physical systems, growth models
3. **Cellular Automaton** - Spatial competition, discrete state evolution
4. **Monte Carlo Simulation** - Uncertainty quantification, parameter sensitivity
5. **Simulated Annealing** - Large-scale optimization with constraints

### Success Patterns from O-Award Papers
- **Mechanistic depth**: Go beyond simple equations; explain WHY the model works biologically/physically
- **Multi-scale modeling**: Combine micro (individual/cellular) and macro (population/system) perspectives
- **Stability analysis**: Eigenvalue analysis, resilience vs. resistance metrics
- **Environmental stochasticity**: Include random processes (Poisson, Gaussian noise) for realistic modeling
- **Trade-off identification**: Growth rate vs. tolerance, efficiency vs. robustness

### Key Implementation Notes
- **Parameter estimation**: Fit from literature data or provided figures using regression/SGD
- **Validation**: Use sensitivity analysis and scenario testing
- **Visualization**: Phase portraits, time series plots, spatial heatmaps

### Typical Pitfalls to Avoid
- Ignoring spatial heterogeneity when it matters
- Over-simplified single-species models when multi-species interaction is expected
- Missing stochastic elements in environmental processes

---

## Problem B: Discrete (MCM)

### Characteristics
- **Core theme**: Operations research, discrete decisions, network optimization
- **Common domains**: Resource allocation, logistics, emergency response, facility location
- **Mathematical focus**: Integer programming, graph algorithms, queuing theory
- **Data availability**: Often no provided data; requires GIS/database research

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Submersible Search & Rescue | Trajectory prediction, equipment optimization, search strategy |
| 2023 | Maasai Mara Wildlife Management | Human-wildlife conflict, game theory, policy design |
| 2022 | Colorado River Water Sharing | Multi-stakeholder allocation, drought scenarios |
| 2021 | Australian Wildfire Drone System | Facility location, fleet management, coverage optimization |
| 2020 | Sandcastle Foundation | Physical simulation, shape optimization, erosion modeling |

### Recommended Models (Top 5 from O-Award Papers)
1. **Multi-Objective Programming (MOP)** - Conflicting stakeholder interests
2. **Genetic Algorithm / NSGA-II** - Complex optimization with Pareto fronts
3. **Bayesian Search Theory** - Sequential search with probability updating
4. **Maximum Covering Location Problem (MCLP)** - Facility siting with coverage constraints
5. **Queuing Theory (M/M/s)** - Capacity evaluation, service level analysis

### Success Patterns from O-Award Papers
- **Real-world data integration**: CMEMS, GEBCO, NOAA, USGS data enhances credibility
- **Physical grounding**: Include actual physics (hydrodynamics, aerodynamics, thermodynamics)
- **Multi-layer architecture**: Prediction layer + Optimization layer + Evaluation layer
- **Scenario analysis**: Normal, severe, extreme conditions testing
- **Stakeholder quantification**: Convert qualitative interests to mathematical objective functions

### Key Implementation Notes
- **Discretization**: Grid-based or network representation of continuous space
- **Constraint handling**: Ensure physical feasibility (capacity, distance, time)
- **Solution presentation**: Provide multiple Pareto-optimal solutions for decision-makers

### Typical Pitfalls to Avoid
- Ignoring real-world constraints (regulations, international agreements)
- Over-idealizing equipment capabilities
- Single-objective optimization when multiple stakeholders exist

---

## Problem C: Data Insights (ICM)

### Characteristics
- **Core theme**: Extract insights from provided datasets
- **Common domains**: Sports analytics, e-commerce, gaming, social phenomena
- **Mathematical focus**: Machine learning, statistics, time series, NLP
- **Data availability**: Rich datasets always provided; focus on analysis depth

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Tennis Momentum | Momentum quantification, statistical validation, prediction |
| 2023 | Wordle Predictions | Score distribution prediction, difficulty classification, time series |
| 2022 | Gold/Bitcoin Trading | Price forecasting, trading strategy, portfolio optimization |
| 2021 | Asian Giant Hornet Reports | Multi-modal classification (image+text), spread prediction |
| 2020 | Amazon Product Reviews | Sentiment analysis, success prediction, fake review detection |

### Recommended Models (Top 5 from O-Award Papers)
1. **Random Forest / XGBoost** - Feature-based prediction and importance ranking
2. **Neural Networks (GRU/LSTM/CNN)** - Time series and image classification
3. **Sentiment Analysis (VADER)** - Text mining and opinion extraction
4. **K-Means++ Clustering** - Unsupervised categorization
5. **Bayesian Networks** - Latent variable modeling, causal inference

### Success Patterns from O-Award Papers
- **Feature engineering excellence**: Extract novel features beyond raw data (e.g., word frequency, letter patterns)
- **Residual thinking**: Define phenomena as residuals after removing known effects (e.g., momentum = actual - expected)
- **Statistical rigor**: Hypothesis testing before claiming patterns exist
- **Multi-modal fusion**: Combine text, image, and numerical features
- **External data augmentation**: Google Trends, WordNet, external corpora

### Key Implementation Notes
- **Data preprocessing**: Handle missing values, normalize, encode categoricals
- **Class imbalance**: Use oversampling, weighted loss, or SMOTE
- **Model validation**: k-fold cross-validation, train/test split
- **Interpretability**: Feature importance, SHAP values, decision rules

### Typical Pitfalls to Avoid
- Ignoring provided text data (it's there for a reason!)
- Purely black-box predictions without interpretation
- Missing temporal patterns in time-stamped data
- Not addressing class imbalance in classification tasks

---

## Problem D: Operations Research / Network Science (ICM)

### Characteristics
- **Core theme**: Complex systems, networks, interdependencies
- **Common domains**: Infrastructure, SDGs, music/culture, sports networks
- **Mathematical focus**: Graph theory, network analysis, system dynamics
- **Data availability**: Network/edge data often provided; sometimes requires collection

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Great Lakes Water Management | Multi-stakeholder optimization, control algorithms, environmental modeling |
| 2023 | UN SDG Prioritization | Network construction, priority ranking, crisis simulation |
| 2022 | Data & Analytics Maturity | Maturity assessment, system improvement, protocol design |
| 2021 | Music Influence Network | Influence quantification, similarity metrics, evolution detection |
| 2020 | Football Team Strategies | Passing network analysis, performance metrics, team optimization |

### Recommended Models (Top 5 from O-Award Papers)
1. **PageRank / HITS** - Node importance in influence networks
2. **Network Centrality Measures** - Degree, betweenness, eigenvector centrality
3. **Correlation Networks** - Relationship discovery from time series data
4. **NSGA-II Multi-Objective Optimization** - Stakeholder balancing
5. **System Dynamics** - Feedback loop modeling, policy simulation

### Success Patterns from O-Award Papers
- **Network + Content fusion**: Combine topology with node attributes (e.g., music features + influence links)
- **Temporal dynamics**: Analyze network evolution over time periods
- **Multi-level analysis**: Macro (whole network), meso (communities/motifs), micro (individual nodes)
- **Quantitative definition of abstract concepts**: "Revolution" as feature derivative, "influence" as PageRank
- **Actionable insights**: Translate network metrics to practical recommendations

### Key Implementation Notes
- **Network construction**: Define nodes, edges, and edge weights clearly
- **Visualization**: Force-directed layouts, heatmaps, time-sliced snapshots
- **Validation**: Compare network patterns with random baselines

### Typical Pitfalls to Avoid
- Pure network analysis without connecting to the domain problem
- Ignoring edge weights or directions when they matter
- Static analysis of inherently dynamic networks
- Correlation mistaken for causation

---

## Problem E: Sustainability (ICM)

### Characteristics
- **Core theme**: Environmental sustainability, risk assessment, long-term planning
- **Common domains**: Climate, insurance, pollution, resource management
- **Mathematical focus**: Risk modeling, evaluation frameworks, scenario analysis
- **Data availability**: Requires extensive external data collection

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Property Insurance Sustainability | Risk quantification, insurance pricing, building preservation |
| 2023 | Light Pollution | Risk index construction, intervention strategies, regional comparison |
| 2022 | Forest Carbon Sequestration | Carbon accounting, harvest optimization, social value integration |
| 2021 | Food System Optimization | Efficiency-equity trade-off, sustainability metrics |
| 2020 | Plastic Pollution | Environmental carrying capacity, impact indexing, reduction targets |

### Recommended Models (Top 5 from O-Award Papers)
1. **AHP-EWM Combined Weighting** - Balanced subjective-objective indicator weights
2. **TOPSIS / Comprehensive Evaluation** - Multi-criteria ranking
3. **Risk Assessment Frameworks** - EAL, CAPM, ALARP
4. **Coupling Coordination Analysis** - Subsystem balance evaluation
5. **Logistic Growth / Carbon Models** - Resource accumulation dynamics

### Success Patterns from O-Award Papers
- **Multi-dimensional indexing**: Economic, environmental, social pillars
- **Regional case studies**: Apply abstract models to specific locations (LA vs. Gorontalo, Rutland vs. Westminster)
- **Trade-off visualization**: Pareto frontiers, radar charts, GE matrices
- **Intervention simulation**: Before/after comparison, policy scenarios
- **Stakeholder perspective**: Who benefits, who bears costs

### Key Implementation Notes
- **Data sources**: NOAA, FEMA, World Bank, NASA, IPCC, OECD
- **Index normalization**: Min-max or z-score standardization
- **Weight sensitivity**: Test different weighting schemes

### Typical Pitfalls to Avoid
- Single-dimensional analysis (only economic or only environmental)
- Ignoring implementation feasibility
- Linear assumptions for nonlinear environmental systems
- Overlooking regional differences in applying global models

---

## Problem F: Policy (ICM)

### Characteristics
- **Core theme**: Societal challenges requiring policy interventions
- **Common domains**: International affairs, governance, equity, education
- **Mathematical focus**: Multi-criteria decision making, impact assessment, scenario planning
- **Data availability**: Requires significant external data collection

### Common Themes Across Years (2020-2024)
| Year | Topic | Core Challenge |
|------|-------|----------------|
| 2024 | Illegal Wildlife Trade | Project design, client selection, impact prediction |
| 2023 | Green GDP | Alternative economic indicators, country comparison |
| 2022 | Asteroid Mining Equity | Global equity quantification, scenario impact |
| 2021 | Higher Education Health | System assessment, policy design, reform roadmap |
| 2020 | Environmental Displaced Persons | Population prediction, allocation fairness, cultural preservation |

### Recommended Models (Top 5 from O-Award Papers)
1. **Entropy Weight Method (EWM) + TOPSIS** - Client/country evaluation and selection
2. **Logical Framework Approach (LFA)** - Project design and impact mapping
3. **Grey Relational Analysis (GRA)** - Factor correlation with limited data
4. **System Dynamics** - Policy impact simulation over time
5. **Lotka-Volterra (Cultural)** - Cultural competition and assimilation modeling

### Success Patterns from O-Award Papers
- **Data-driven decision making**: Don't assume; let data guide choices (why this client? why this species?)
- **Project management rigor**: Gantt charts, SMART objectives, logic frameworks
- **Equity considerations**: Include fairness metrics (Gini, climate justice, access)
- **Stakeholder mapping**: Who has power, who needs resources, who is affected
- **Creative extensions**: Apply ecological models to social systems (culture as species)

### Key Implementation Notes
- **Framework adoption**: Use established frameworks (LFA, CAPM, RBM)
- **Scenario comparison**: Present multiple policy options with trade-offs
- **Visualization**: Problem trees, objective trees, stakeholder matrices

### Typical Pitfalls to Avoid
- Designing projects beyond client capabilities/authority
- Ignoring political realities and implementation barriers
- Over-relying on regression with too few data points
- Vague recommendations without quantified targets

---

## Cross-Problem Comparison

### Model Frequency by Problem Type

| Model Category | A | B | C | D | E | F |
|----------------|---|---|---|---|---|---|
| Differential Equations | *** | * | - | - | * | * |
| Optimization (LP/MOP) | * | *** | - | ** | * | - |
| Machine Learning | * | * | *** | * | - | - |
| Network Analysis | - | - | * | *** | - | - |
| Evaluation (AHP/EWM) | - | ** | - | * | *** | *** |
| Simulation (MC/CA) | ** | ** | - | * | * | * |

*Legend: *** = Primary, ** = Secondary, * = Occasional, - = Rare*

### Data Characteristics by Problem Type

| Problem | Data Provided | External Data Needed | Primary Data Type |
|---------|---------------|---------------------|-------------------|
| A | Minimal/None | High | Literature parameters |
| B | None | High | GIS, databases |
| C | Rich | Low-Medium | Tabular, text, images |
| D | Network data | Medium | Edge lists, attributes |
| E | None | High | Environmental databases |
| F | None | High | Economic, social statistics |

### Time Allocation Recommendations (4-day competition)

| Problem Type | Literature Review | Data Collection | Modeling | Writing |
|--------------|-------------------|-----------------|----------|---------|
| A | 20% | 10% | 50% | 20% |
| B | 15% | 20% | 45% | 20% |
| C | 10% | 10% | 55% | 25% |
| D | 15% | 15% | 45% | 25% |
| E | 15% | 25% | 35% | 25% |
| F | 20% | 25% | 30% | 25% |

---

## Universal Success Factors (All Problem Types)

### 1. Problem Decomposition
- Break the problem into 3-5 sub-problems
- Create a clear table mapping sub-problems to models
- Show logical flow between components

### 2. Model Layering
- **Layer 1**: Base model (captures core mechanism)
- **Layer 2**: Advanced model (adds realism, complexity)
- **Layer 3**: Validation/sensitivity analysis

### 3. Data-Driven Rigor
- Cite data sources explicitly
- Use tables to present data characteristics
- Validate models with held-out data or historical records

### 4. Visualization Excellence
- Include 8-12 high-quality figures
- One "signature visualization" that captures the essence
- Label all axes, use consistent color schemes

### 5. Sensitivity Analysis
- Test at least 3 parameters
- Present results in tornado diagrams or tables
- Discuss robustness of conclusions

### 6. Writing Clarity
- Abstract: 250 words, standalone summary
- Clear section headers matching sub-problems
- Conclusions tied back to original questions

---

## Quick Start Checklist by Problem Type

### Problem A Checklist
- [ ] Identify state variables and their dynamics
- [ ] Write differential equations with biological/physical meaning
- [ ] Include environmental stochasticity
- [ ] Perform stability analysis
- [ ] Run Monte Carlo for uncertainty

### Problem B Checklist
- [ ] Define objective function(s) and constraints
- [ ] Collect GIS/database data for the region
- [ ] Discretize space appropriately
- [ ] Compare multiple scenarios (normal, extreme)
- [ ] Present Pareto-optimal solutions

### Problem C Checklist
- [ ] Explore all provided data columns
- [ ] Engineer features beyond raw data
- [ ] Use multiple ML models and compare
- [ ] Validate with statistical tests
- [ ] Provide interpretable insights

### Problem D Checklist
- [ ] Construct network with clear node/edge definitions
- [ ] Calculate network metrics (centrality, motifs)
- [ ] Analyze temporal evolution if applicable
- [ ] Connect network insights to practical recommendations
- [ ] Visualize network structure effectively

### Problem E Checklist
- [ ] Define multi-dimensional indicator system
- [ ] Use combined weighting (AHP + EWM)
- [ ] Apply to 2+ contrasting case studies
- [ ] Simulate intervention scenarios
- [ ] Discuss trade-offs and stakeholder impacts

### Problem F Checklist
- [ ] Use data to justify key choices (client, focus area)
- [ ] Apply professional frameworks (LFA, RBM)
- [ ] Include fairness/equity considerations
- [ ] Provide specific, actionable recommendations
- [ ] Present realistic implementation timeline

---

*Last updated based on MCM/ICM problems and O-award papers 2020-2024*
