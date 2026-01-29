# MCM/ICM Literature Review Guide

> **Goal**: Write a professional, academic-style literature review that demonstrates depth of research and justifies your model choice.

---

## 1. Purpose of Literature Review

In an O-Award paper, the literature review serves three critical functions:
1.  **Context**: Shows you understand the broader scientific landscape.
2.  **Justification**: Explains *why* you chose your specific approach over others.
3.  **Gap Identification**: Highlights what previous methods missed, setting the stage for your innovation.

---

## 2. Structure of a Good Review (200-300 words)

### Paragraph 1: Broad Overview
-   Introduce the general field of study.
-   Mention 2-3 standard approaches typically used.
-   *Example*: "In population dynamics, classic approaches include the Malthusian growth model [1] and the Logistic model [2]..."

### Paragraph 2: Critique of Existing Methods
-   Discuss the limitations of standard methods for *this specific problem*.
-   *Example*: "However, these models fail to account for the stochastic nature of [phenomenon] and the [specific constraint] present in this problem..."

### Paragraph 3: Our Contribution
-   Introduce your approach as the solution to these limitations.
-   *Example*: "To address these gaps, we propose a [Your Model Name] that integrates [Technique A] with [Technique B]..."

---

## 3. How to Find References

### Using Perplexity Search (Recommended)
Use the `perplexity-search` skill with queries like:
-   `"[Problem Topic] mathematical modeling review"`
-   `"Approaches for modeling [Key Phenomenon]"`
-   `"Limitations of [Standard Model] in [Context]"`

### Citation Format
-   Use IEEE or numeric style: `[1]`, `[2]`.
-   List full citations in the **References** section at the end.
-   *Format*: `[1] Author(s). "Title of Paper". Journal/Conference, Year.`

---

## 4. Visualization: The Comparison Table

O-Award papers often include a table or chart comparing methods.

| Method | Key Feature | Strengths | Weaknesses |
|--------|-------------|-----------|------------|
| **Method A** | Linear Regression | Simple, interpretable | Cannot model non-linear dynamics |
| **Method B** | Neural Networks | High accuracy | Black-box, requires massive data |
| **Our Model** | Hybrid DE-ML | Physical interpretability + Data-driven | Computationally intensive |

**LaTeX Template:**
```latex
\begin{table}[htbp]
\centering
\caption{Comparison of Existing Approaches}
\label{tab:literature}
\begin{tabular}{lccc}
\toprule
\textbf{Method} & \textbf{Strength} & \textbf{Limitation} & \textbf{Reference} \\
\midrule
Lotka-Volterra & Theoretical basis & Deterministic only & [1] \\
Agent-Based & Individual behavior & Computationally heavy & [2] \\
\textbf{Ours} & \textbf{Hybrid Approach} & \textbf{Balanced trade-off} & - \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 5. Checklist for LLM Generation

When generating the literature review section:
-   [ ] Are there at least 3 distinct references?
-   [ ] Is there a clear logical flow (General -> Specific -> Gap -> Our Solution)?
-   [ ] Is there a comparison (textual or tabular) of methods?
-   [ ] Are the citations properly formatted?
-   [ ] Does it explicitly mention *why* previous methods are insufficient?
