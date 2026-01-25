# Type E (Sustainability/Environment) Visualization Analysis

## 1. Figure Inventory & Description

### 2020 Problem E: Plastic Waste (Paper 01)
*   **Figure 1:** Schematic of model 1 (System Diagram) - Visualizes the flow of plastic waste (Recycle, Burn, Discard).
*   **Figure 2:** Schematic of model 2 (System Diagram) - Likely an extension of Model 1.
*   **Figure 3:** Reliance and Improvement degrees (Scatter/Line Chart) - Shows relationship between GDP and reliance/improvement capability (U-shape curve mentioned).
*   **Figure 4:** Amount of waste mitigated in three ways (Pie Chart) - Proportion of waste handling methods.
*   **Figure 5:** Impact of plastic in varied fields (Chart) - Likely a Bar or Radar chart showing impact distribution.
*   **Figure 6:** Global PII scores (Map/Bar) - Visualization of the Plastic Impact Index across the globe.
*   **Figure 7:** The impact of plastic in Europe and East-Asia (Comparison Chart).
*   **Figure 8:** Change of PII in Europe and East-Asia (Line Chart) - Time series analysis of index change.
*   **Figure 9:** PII of East-Asia and Europe under policies (Scenario Simulation Chart).
*   **Figure 10:** The index and potential minimum levels (Optimization Result Chart).
*   **Figure 11:** The growing trend of three functions (Line Chart).
*   **Figure 12:** GE matrix diagram (Strategic Matrix) - Classifies countries based on GDP and CICI.
*   **Figure 13:** SDC and change diagram (Scatter Plot) - Shows movement of countries in the matrix over 5 years.
*   **Figure 14:** Sensitivity analysis (Line/Scatter Plot) - Parameter sensitivity verification.

### 2022 Problem E: Forest Management (Paper 01)
*   **Figure 1:** Our work (Flow Chart/Process Diagram) - Overview of the research work.
*   **Figure 2:** The roles of forests and forest products in the global carbon cycle (Cycle Diagram) - Illustrates carbon sequestration and release flows.
*   **Figure 3:** The comparison of various trees (Bar/Line Chart) - Comparative analysis of species.
*   **Figure 4:** Forest carbon sequestration destination (System Diagram) - Carbon flow into wood products vs atmosphere.
*   **Figure 5:** The overall process (Flow Chart) - Detailed modeling process.
*   **Figure 6:** Indicators of forest value (Hierarchy/Structure Diagram).
*   **Figure 7:** The GE matrix (Strategic Matrix) - Balancing carbon value vs social value.
*   **Figure 8:** Relationship between area and ages of trees (Distribution Chart).
*   **Figure 9:** (a) Genetic Algorithm results (Convergence Plot), (b) Optimal plan on GE Matrix.
*   **Figure 10:** The modification of the optimal plan (Dynamic Planning Chart).
*   **Figure 11:** Sensitivity analysis (Line Chart).

### 2023 Problem E: Light Pollution (Paper 01)
*   **Figure 1:** Night View of the Earth (Map/Image) - Visual evidence of light pollution.
*   **Figure 2:** Literature Review Framework (Concept Map) - Classification of research methods.
*   **Figure 3:** Flow Chart of Our Work (Flow Chart) - Algorithm/Logic flow.
*   **Figure 4:** Impact of Light Pollution (Mind Map/Hierarchy) - Classification of impacts (Social, Ecological, Physiological).
*   **Figure 5:** Some Data Visualization (Exploratory Data Analysis Charts).
*   **Figure 6:** Pearson Correlation Coefficient (Heatmap/Scatter) - Correlation between electricity and light pollution.
*   **Figure 7:** (a) Diagram of Risk Assessment Criterion (ALARP Zone Diagram), (b) Cost-Risk Analysis curve.
*   **Figure 8:** (a) Map of selected areas, (b) Normalized data line graph (Model Verification).
*   **Figure 9:** Results of LPA applications (Radar/Bar Chart) - Assessment results for specific sites.
*   **Figure 10:** Starry Sky Conditions (Simulation/Visual Effect) - Impact on visibility.
*   **Figure 11:** Intervention Scores for Rutland (Comparison Bar Chart) - Before vs After strategies.
*   **Figure 12:** Intervention Scores for Westminster (Comparison Bar Chart).
*   **Figure 13:** Changes in EP by Region (Sensitivity Line Chart).

## 2. Chart Type Statistics (Estimated)

| Chart Type | Frequency | Typical Usage |
| :--- | :--- | :--- |
| **System/Flow Diagrams** | High | Describing physical processes (Carbon cycle, Plastic flow) or model logic (Flowcharts). |
| **Line Charts** | High | Time series trends, Sensitivity analysis, Dynamic changes (before/after). |
| **Matrices (GE/Strategy)** | Med-High | Classification of regions/policies (e.g., High Risk-Low Capability). |
| **Maps (Geospatial)** | Medium | Global distribution (PII), Regional sites (Light pollution). |
| **Bar/Comparison Charts**| Medium | Regional comparisons (Europe vs Asia), Scenario comparisons. |
| **Scatter Plots** | Medium | Correlations (GDP vs Pollution), Matrix positioning. |
| **Pie Charts** | Low | Composition of waste/forest types (Less common for complex data). |

## 3. Design Patterns in Type E Papers

### A. The "Process & Cycle" Visuals
Type E problems often deal with *systems* (ecosystems, waste streams).
*   **Pattern:** Use schematic diagrams to show "Stocks and Flows".
    *   *Example:* 2020 Fig 1 (Plastic flow), 2022 Fig 2 (Carbon Cycle).
    *   *Purpose:* Demonstrates understanding of the physical/biological mechanism behind the problem.

### B. The "Strategic Classification" Matrix
Sustainable development problems often require balancing conflicting goals (Economy vs Environment).
*   **Pattern:** The GE Matrix (General Electric Matrix) or 2D Scatter classification.
    *   *Example:* 2020 Fig 12, 2022 Fig 7.
    *   *X-Axis:* Economic/Social capability (GDP, Social Value).
    *   *Y-Axis:* Environmental urgency/Value (Carbon Sequestration, Pollution Index).
    *   *Usage:* Divides regions/strategies into quadrants (e.g., "Prioritize Protection", "Develop Economy") to give tailored policy advice.

### C. The "Before & After" Intervention Comparison
Type E asks for policy impacts.
*   **Pattern:** Comparative Bar/Line charts showing metrics under different scenarios.
    *   *Example:* 2023 Fig 11/12, 2020 Fig 9.
    *   *Design:* Side-by-side bars for "Baseline", "Policy A", "Policy B".

### D. Sensitivity "Fan" Charts
*   **Pattern:** Line charts showing how a key result metric changes as a parameter varies $\pm 5\% - 20\%$.
    *   *Example:* 2020 Fig 14, 2022 Fig 11, 2023 Fig 13.
    *   *Design:* Often multiple lines on one plot or side-by-side subplots for different parameters.

## 4. Type-E Specific Recommendations

1.  **Visualize the Mechanism**: Don't just show data; show the *process*. If it's plastic, draw the lifecycle. If it's forests, draw the carbon exchange. Use tools like Visio, PPT, or Python (Graphviz/NetworkX) to create professional schematic diagrams.
2.  **Use Maps for Context**: Environmental problems are spatial. Even simple colored maps (Choropleth) using Python (Geopandas) or Tableau significantly enhance the "Global" feel of the paper.
3.  **Adopt the GE Matrix**: This is a winning pattern for Type E. It converts complex multi-objective optimization results into actionable, easy-to-understand strategic advice.
4.  **Simulation Results**: Show the *trajectory* of improvement. Not just "Goal reached", but the curve of *how* it is reached over time (e.g., 2020 Fig 11).
