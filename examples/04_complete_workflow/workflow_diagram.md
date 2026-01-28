# MCM/ICM Complete Workflow Diagram

A visual guide to the entire competition process, from problem release to submission.

## Overall Timeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        MCM/ICM 5-DAY WORKFLOW                           │
├─────────────────────────────────────────────────────────────────────────┤
│ Day 1 │ Day 2 │ Day 3 │ Day 4 │ Day 5 │
│ 8hrs  │ 16hrs │ 16hrs │ 16hrs │ 8hrs  │
│       │       │       │       │       │
│ READ  │ MODEL │ SOLVE │ WRITE │ FINAL │
│ PLAN  │ CODE  │ PLOT  │ EDIT  │ CHECK │
└───────┴───────┴───────┴───────┴───────┘
```

## Detailed Phase Diagram

### Phase 1: Problem Analysis (Day 1, 0-8 hrs)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 1: PROBLEM ANALYSIS                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────────┐         │
│  │ READ     │───▶│ IDENTIFY     │───▶│ CHECK REFERENCES  │         │
│  │ PROBLEM  │    │ TYPE (A-F)   │    │                   │         │
│  └──────────┘    └──────────────┘    │ • problem-types   │         │
│                         │            │ • models-library  │         │
│                         ▼            └───────────────────┘         │
│               ┌──────────────┐              │                      │
│               │ EXTRACT      │              │                      │
│               │ REQUIREMENTS │◀─────────────┘                      │
│               └──────────────┘                                     │
│                         │                                          │
│                         ▼                                          │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ RUN: python scripts/generate_outline.py -p [TYPE]            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  OUTPUT: outline.md with section structure and model suggestions    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase 2: Model Development (Day 2, 8-24 hrs)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 2: MODEL DEVELOPMENT                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────┐    ┌───────────────┐    ┌──────────────┐        │
│  │ SELECT        │───▶│ FORMULATE     │───▶│ IMPLEMENT    │        │
│  │ MODELS        │    │ MATHEMATICS   │    │ IN PYTHON    │        │
│  └───────────────┘    └───────────────┘    └──────────────┘        │
│         │                                          │                │
│         │     ┌────────────────────────────────────┘                │
│         │     ▼                                                     │
│         │   ┌──────────────────────────────────────┐               │
│         │   │ VALIDATION                           │               │
│         │   │ • Unit tests for functions           │               │
│         │   │ • Known case comparison              │               │
│         │   │ • Sanity checks on outputs           │               │
│         │   └──────────────────────────────────────┘               │
│         │                                                          │
│         ▼                                                          │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Reference: models-library.md for implementation hints       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase 3: Results & Visualization (Day 3, 24-40 hrs)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 3: RESULTS & VISUALIZATION                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐    ┌───────────────┐    ┌────────────────┐           │
│  │ RUN      │───▶│ COLLECT       │───▶│ GENERATE       │           │
│  │ MODEL    │    │ RESULTS       │    │ FIGURES        │           │
│  └──────────┘    └───────────────┘    └────────────────┘           │
│                                              │                      │
│                                              ▼                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ USE VISUALIZATION TEMPLATES:                                  │  │
│  │                                                               │  │
│  │  from templates.visualization import use_mcm_style            │  │
│  │  from templates.visualization.plot_templates import (         │  │
│  │      plot_pareto_frontier,  # For optimization                │  │
│  │      plot_tornado,          # For sensitivity                 │  │
│  │      plot_forecast,         # For time series                 │  │
│  │      create_grid_layout     # For multi-panel                 │  │
│  │  )                                                            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  OUTPUT: figures/*.png, figures/*.pdf                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase 4: Writing & Polish (Day 4, 40-56 hrs)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PHASE 4: WRITING & POLISH                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ SECTION ORDER (based on paper-structure.md):                  │  │
│  │                                                               │  │
│  │  1. Introduction      ─┐                                      │  │
│  │  2. Assumptions       ─┤                                      │  │
│  │  3. Model Development ─┼─▶ Write these FIRST                  │  │
│  │  4. Results           ─┤                                      │  │
│  │  5. Sensitivity       ─┤                                      │  │
│  │  6. Strengths/Weak    ─┤                                      │  │
│  │  7. Conclusion        ─┘                                      │  │
│  │                                                               │  │
│  │  8. Summary           ────▶ Write this LAST (most important!) │  │
│  │  9. References                                                │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ HUMANIZE TEXT:                                                │  │
│  │                                                               │  │
│  │   python scripts/humanize_text.py -i draft.md -o final.md    │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase 5: Final Check (Day 5, 56-72+ hrs)

```
┌─────────────────────────────────────────────────────────────────────┐
│                      PHASE 5: FINAL CHECK                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ FORMAT CHECK:                                                 │  │
│  │                                                               │  │
│  │   python scripts/check_format.py paper.pdf --verbose          │  │
│  │                                                               │  │
│  │ Verifies:                                                     │  │
│  │   ✓ Page count ≤ 25                                          │  │
│  │   ✓ Team number in header                                    │  │
│  │   ✓ No identifying information                               │  │
│  │   ✓ Summary section present                                  │  │
│  │   ✓ References section present                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ FINAL CHECKLIST:                                              │  │
│  │                                                               │  │
│  │   □ All problem requirements addressed                       │  │
│  │   □ All figures referenced in text                           │  │
│  │   □ All equations numbered                                   │  │
│  │   □ Citations complete                                       │  │
│  │   □ AI usage report included (if required)                   │  │
│  │   □ PDF renders correctly                                    │  │
│  │   □ File named correctly                                     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ SUBMIT before 9:00 PM EST Monday                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Tool Usage Summary

| Phase | Tool | Command |
|-------|------|---------|
| 1 | Outline Generator | `python scripts/generate_outline.py -p [TYPE]` |
| 2 | Models Library | Read `references/models-library.md` |
| 3 | Visualization | `from templates.visualization.plot_templates import ...` |
| 4 | Text Humanizer | `python scripts/humanize_text.py -i draft.md -o final.md` |
| 5 | Format Checker | `python scripts/check_format.py paper.pdf` |

## Emergency Timeline

If behind schedule:

```
Day 4 Night (no sleep):
├── Hour 1-2: Finish all figures
├── Hour 3-4: Write Results section
├── Hour 5-6: Write Model section
├── Hour 7-8: Write Introduction + Conclusion
├── Hour 9: Write Summary (CRITICAL)
└── Hour 10: Format check + Submit

Minimum viable paper:
- Summary: 1 page (required)
- Introduction: 1 page
- Model: 3-4 pages (core content)
- Results: 2-3 pages (with figures)
- Conclusion: 0.5 page
- References: 0.5 page
Total: 8-10 pages (acceptable but not competitive)
```

---
*MCM-Analysis v1.2.2 - Workflow Diagram*
