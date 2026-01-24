# MCM/ICM O-Award Paper Structure Reference

This guide synthesizes structural patterns from 6 Outstanding papers (2024 MCM/ICM Problems A-F).

---

## 1. Overall Page Allocation

| Section | Percentage | Typical Pages |
|---------|------------|---------------|
| Summary/Abstract | 4% | 1 page (strictly) |
| Introduction | 8-10% | 2-3 pages |
| Assumptions & Notations | 4-6% | 1-1.5 pages |
| Model Development | 50-60% | 12-15 pages |
| Results & Analysis | 15-20% | 4-5 pages |
| Sensitivity Analysis | 4-6% | 1-1.5 pages |
| Strengths & Weaknesses | 2-4% | 0.5-1 page |
| Conclusion/Memo | 4-6% | 1-2 pages |
| References | 2-4% | 0.5-1 page |

---

## 2. Summary Sheet Patterns

### Word Count
- Target: 300-450 words
- Maximum: One full page (including keywords)

### Structure Template
```
[Title: Descriptive, often includes colon]

Summary

[Opening hook - 1-2 sentences describing problem importance]

For Task 1, we [verb: developed/established/constructed] a [Model Name]. 
[Brief methodology]. [Key result or insight].

For Task 2, we [verb: applied/used/extended] [approach]. 
[What was achieved]. [Specific quantitative result if applicable].

For Task 3, we [verb: analyzed/evaluated/assessed] [aspect].
[Methodology]. [Key finding with numbers].

[Continue for remaining tasks...]

[Final synthesis paragraph - 2-3 sentences]

Keywords: [4-6 comma-separated terms]
```

### Observed Patterns
1. **Task-by-task structure**: Each task gets 2-4 sentences
2. **Quantitative results**: Include specific numbers (percentages, dollar values, time periods)
3. **Model naming**: Papers consistently NAME their models (e.g., "Discrete Population Dynamics Model", "DBMI", "GSRF Swing Predictor Model")
4. **Keywords format**: 4-6 keywords, semicolon or comma separated, includes main techniques

### Example Keywords
- "Discrete Population Dynamics Modeling; Lampreys Sex Ratio; Ecosystem Stability"
- "Dynamics Model, Monte Carlo Simulation, Ant Colony Algorithm, Cost-Benefit Analysis based on EWM, Bayesian Detection"
- "Monte Carlo Simulation, Runs Test, GSRF, Factor Analysis"

---

## 3. Contents/Table of Contents Structure

### Standard Section Numbering
```
1 Introduction
   1.1 Problem Background
   1.2 Restatement of the Problems
   1.3 Our Work

2 Assumptions and Notations
   2.1 Assumptions
   2.2 Notations

3 [Main Model Name]
   3.1 Model Preparation / Foundation
   3.2 [Core Model Component]
   3.3 [Additional Components]
   3.4 Model Overview

4 Task 1: [Descriptive Title]
   4.1 [Analysis Approach]
   4.2 [Results]

5 Task 2: [Descriptive Title]
...

N Sensitivity Analysis
N+1 Strengths and Weaknesses
References
[Optional: Memo/Letter]
[Optional: AI Usage Report]
```

---

## 4. Introduction Patterns

### 4.1 Problem Background (1-1.5 pages)
**Structure:**
1. Broad context (1 paragraph)
2. Specific problem domain (1-2 paragraphs)
3. Why this matters / challenges (1 paragraph)

**Example openers:**
- "In nature, the sex ratio of different species is different..."
- "With the development of diving technology, deep-sea diving has gradually found its way into..."
- "Tennis matches are exciting and ever-changing..."
- "The Great Lakes, spanning the United States and Canada, constitute the world's largest..."

### 4.2 Restatement of Problems (0.5-1 page)
**Format:** Bullet points, one per task

**Template:**
```
For the problem of [domain], we develop plausible mathematical models 
that provide insights into [outcome] and answer the following questions:

• [Task 1 rephrased in own words]
• [Task 2 rephrased in own words]
• [Continue for all tasks]
```

### 4.3 Our Work (0.5-1 page)
- Often includes a **workflow diagram/flowchart**
- Brief overview connecting tasks
- Explains paper organization

---

## 5. Assumptions Section Patterns

### Format
Each assumption follows this structure:
```
• Assumption [N]: [Clear statement of what is assumed]
  Justification: [Why this assumption is reasonable - 1-3 sentences]
```

### Common Assumption Types
1. **Simplification**: "We assume that X follows a simplified pattern..."
2. **Boundary conditions**: "We consider the average X as the initial value..."
3. **Scope limitation**: "We do not consider X because..."
4. **Behavioral**: "Players/Actors are assumed to behave rationally..."
5. **Data reliability**: "The data we use is true and reliable..."

### Typical Count
- 3-5 major assumptions per paper
- Each with explicit justification

---

## 6. Notations Table Pattern

### Standard Format
| Symbol/Notation | Definition | Unit (if applicable) |
|-----------------|------------|---------------------|
| M_t | Proportion of females at time t | - |
| β_m | Natural mortality rate | 1/year |
| Q_out(i) | Outflow of the ith lake | m³/s |

### Placement
- Immediately after assumptions
- Note at bottom: "Note: Some variables not listed will be discussed in detail in each section."

---

## 7. Methodology Section Organization

### Layered Approach (Common Pattern)
```
3 [Model Name]
   3.1 Model Preparation
       3.1.1 [Foundational concept/grouping]
       3.1.2 [System/relationship definition]
   
   3.2 [Core Mathematical Model]
       3.2.1 [Component A modeling]
       3.2.2 [Component B modeling]
       3.2.3 [External factors/interventions]
   
   3.3 Model Overview
       [Summary equation or diagram]
       [Parameter tables]
```

### Equation Presentation
1. Present equation with number
2. Explain each variable
3. Provide physical/logical interpretation
4. Show derivation if non-trivial

---

## 8. Results Presentation Patterns

### Figure Captions
- Descriptive: "Figure X: [Description of what is shown]"
- Always referenced in text before appearing
- Subfigures labeled (a), (b), (c) with individual descriptions

### Table Patterns
- Clear headers
- Units specified
- Source noted if external data

### Quantitative Results Format
- Present specific numbers: "The accuracy reaches 94%..."
- Compare to baselines: "Compared with 2017 data, our model shows..."
- Include confidence intervals or ranges where applicable

---

## 9. Sensitivity Analysis Structure

### Standard Approach
1. **Parameter selection**: Identify key parameters to test
2. **Perturbation**: Apply ±5%, ±10% changes
3. **Visualization**: Show impact graphs
4. **Conclusion**: State whether model is robust

**Example statement:**
"We perturbed each parameter in the model by ±5% to analyze [output variable]. The results show that changes in [parameter] cause the fluctuations to reach X%, while the fluctuations caused by other parameters were within Y%."

---

## 10. Strengths and Weaknesses Section

### Format
```
Strengths:
• [Strength 1 with brief explanation]
• [Strength 2 with brief explanation]
• [2-4 total]

Weaknesses:
• [Weakness 1 with acknowledgment]
• [Weakness 2 with potential improvement]
• [1-3 total]
```

### Common Strengths Mentioned
- Comprehensive consideration of factors
- Scientific validity (literature-backed)
- Robust to parameter changes
- Practical applicability

### Common Weaknesses Acknowledged
- Simplified assumptions
- Data limitations
- Computational complexity
- Scope limitations

---

## 11. Memo/Letter Patterns

### Length: 1-2 pages

### Structure
```
To: [Recipient Organization/Person]
From: Team #[Number]
Date: [Competition Date]
Subject: [Brief descriptive title]

Dear [Appropriate salutation],

[Opening - 1 paragraph introducing purpose]

[Body - 2-4 paragraphs covering:
 - Problem overview
 - Key findings
 - Recommendations
 - Supporting data/tables if brief]

[Closing - appreciation and offer for further discussion]

Yours Sincerely,
Team #[Number]
```

---

## 12. Reference Patterns

### Count: 7-15 references typical

### Format
- Numbered list [1], [2], etc.
- Academic citation style
- Mix of:
  - Academic papers
  - Official reports/databases
  - Authoritative websites (Wikipedia acceptable for background)

### In-text Citations
- "[X]" format immediately after claim
- Multiple sources: "[X][Y]" or "[X,Y]"

---

## 13. AI Usage Report (When Required)

### Format
```
Report on Use of AI

1. [AI Tool Name]
Query [N]: <exact query submitted>
Output: <summarized or quoted response>

2. [AI Tool Name]
Query [N]: <query>
Output: <response>
```

### Observed Uses
- Background research queries
- Definition/explanation requests
- Writing polish/rewriting requests
- Technical concept clarification
