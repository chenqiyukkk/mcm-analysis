# MCM/ICM Problem Type F (Policy/Social) Visualization Analysis

## 1. Overview
Type F problems focus on policy making, social stability, and sustainable development. Unlike engineering or physical modeling problems, Type F papers rely heavily on **conceptual frameworks**, **stakeholder analysis**, and **scenario comparisons**. Visualizations serve to bridge the gap between abstract policy concepts and quantitative model outputs.

## 2. Figure Inventory & Statistics

Based on the analysis of O-award papers (2020-2024), the following visualization types are most prevalent:

| Category | Chart Type | Frequency | Typical Usage |
|----------|------------|-----------|---------------|
| **Framework** | Flowcharts / Process Diagrams | High | Illustrating the "Work Flow" or problem solving logic. |
| | Logic Trees / Mindmaps | Med | Decomposing complex concepts (e.g., "Global Equity", "EDP"). |
| | Concept Diagrams | Med | Visualizing novel concepts (e.g., "Three Swords" strategy, "Cone Island"). |
| **Evaluation** | Radar Charts / Spider Charts | High | Comparing multi-dimensional indicators (e.g., NGO vs Gov vs Enterprise). |
| | Bar / Stacked Bar Charts | High | Ranking countries or policies by score. |
| | 3D Scatter / Vector Plots | Low | Visualizing clustering of countries or entities. |
| **Dynamics** | Line Charts (Time Series) | High | Predicting trends (e.g., GDP, population, sea level). |
| | Phase Plane Plots | Low | Showing dynamic equilibrium (e.g., Lotka-Volterra culture competition). |
| | Stock-Flow Diagrams | Med | System Dynamics models for policy simulation (2021). |
| **Statistical** | Scatter Plots | Med | Correlation analysis (e.g., Trade volume vs Factors). |
| | Residual / P-P Plots | Low | Validating regression models. |
| | Sensitivity Analysis Plots | High | Showing model robustness under parameter changes. |

## 3. Design Patterns by Year

### 2024: Roaring Silence (Illegal Wildlife Trade)
*   **Radar Charts:** Used extensively to profile clients (Power, Resources, Interests). This is a classic pattern for "Selection/Evaluation" tasks in Type F.
*   **Process Flowcharts:** "Our Work" diagrams clearly map the inputs (Data), Models (EWM, TOPSIS, Regression), and Outputs (Policy).
*   **Statistical Validation:** Explicit inclusion of Residual Histograms and P-P plots to justify the rigor of the regression model.
*   **Concept Art:** "Three Swords" diagram to metaphorically represent the multi-pronged approach (Governments, Enterprises, NGOs).

### 2022: Global Equity (Asteroid Mining)
*   **Logic Trees (McKinsey Style):** Used to break down the abstract "Global Equity" into measurable indicators. This suggests a "Top-Down" modeling approach often favored in policy papers.
*   **Clustering Visuals:** Visualizing the "Global South" vs "Global North" divide using K-Means results.
*   **Scenario Comparison:** Visualizing the divergence of "Global Equity Index" under different future scenarios (Private vs Public mining).

### 2020: Wandering Homeland (Environmentally Displaced Persons)
*   **Geometric/Physical Models:** The "Cone Island" model visualizes a physical simplification of a complex geographic problem.
*   **Cultural Dynamics:** Using phase portraits (from Lotka-Volterra equations) to show the *trajectory* of culture survival, rather than just static numbers.
*   **Fitting Curves:** Linear fitting of sea-level data to establish the baseline urgency.

## 4. Type-F Specific Visualization Strategies

### A. The "Abstract to Concrete" Pipeline
Type F problems often start with vague terms like "Health", "Equity", or "Sustainability".
*   **Pattern:** Use **Logic Trees** or **Mindmaps** early in the paper (Section 2 or 3) to visually demonstrate how these abstract concepts are broken down into quantifiable variables ($x_1, x_2, ...$).

### B. Stakeholder & Multi-Criteria Evaluation
Policy problems involve multiple actors with conflicting goals.
*   **Pattern:** **Radar Charts** are the gold standard here. They allow for instant visual comparison of the "shape" of different stakeholders (e.g., one is rich but weak in policy, another is strong in policy but poor).

### C. Policy Impact "What-If" Visuals
The core of Type F is predicting the future under a new policy.
*   **Pattern:** **Diverging Line Charts** or **Scenario Fan Charts**. Show the baseline trajectory (Status Quo) vs. the trajectory under the proposed policy.
*   **Pattern:** **Sensitivity Analysis** is crucial. It shows that the policy is robust even if political/economic parameters fluctuate.

### D. System Dynamics (Stock-Flow)
For complex systems (Education, Migration, Trade), static equations aren't enough.
*   **Pattern:** **Stock-Flow Diagrams** (boxes and arrows with valves) illustrate the feedback loops. This is particularly effective for arguing about "long-term stability" or "vicious cycles".

## 5. Recommendations for Future Type F Papers
1.  **Visual Project Management:** Include a Gantt chart or Logframe matrix if the problem asks for a "Plan" or "Project". (See 2024).
2.  **Profile Your Subjects:** If comparing countries or organizations, use Radar Charts instead of simple tables.
3.  **Metaphorical Diagrams:** Don't be afraid to create a simple schematic to explain your core philosophy (e.g., the "Three Swords" or "Cone Island"). It makes the paper memorable.
4.  **Validate Visually:** Always include a visual proof of your model's validity (Residuals, Sensitivity, or Historical Back-testing).
