#!/usr/bin/env python3
"""
MCM/ICM Paper Outline Generator

Generates a structured paper outline based on problem type and requirements,
with suggested section structure, page allocation, and recommended models.

Usage:
    python generate_outline.py --problem-type C
    python generate_outline.py --problem-type A --requirements "optimize,constraints,real-world"
    python generate_outline.py -p D --title "Network Analysis Problem"

Output: outline.md in current directory
"""

import argparse
from pathlib import Path
from datetime import datetime


# =============================================================================
# Problem Type Configurations
# =============================================================================

PROBLEM_TYPES = {
    "A": {
        "name": "Continuous (MCM)",
        "description": "Continuous mathematical modeling, often involving differential equations, optimization, or physical systems",
        "typical_topics": [
            "Physical systems modeling",
            "Optimization problems",
            "Resource allocation",
            "Environmental modeling",
            "Engineering design"
        ],
        "recommended_models": [
            "Differential Equations (ODEs/PDEs)",
            "Linear/Nonlinear Programming",
            "Simulation (Monte Carlo)",
            "Sensitivity Analysis",
            "Multi-objective Optimization"
        ],
        "key_techniques": [
            "Calculus and analysis",
            "Numerical methods",
            "Optimization algorithms",
            "Physical modeling",
            "Parameter estimation"
        ]
    },
    "B": {
        "name": "Discrete (MCM)",
        "description": "Discrete mathematical modeling, often involving combinatorics, graph theory, or discrete optimization",
        "typical_topics": [
            "Scheduling problems",
            "Network flow",
            "Combinatorial optimization",
            "Game theory",
            "Resource allocation (discrete)"
        ],
        "recommended_models": [
            "Graph Theory / Network Models",
            "Integer Programming",
            "Dynamic Programming",
            "Queuing Theory",
            "Markov Chains"
        ],
        "key_techniques": [
            "Graph algorithms",
            "Combinatorial analysis",
            "Heuristic methods (GA, SA)",
            "Game-theoretic analysis",
            "Discrete simulation"
        ]
    },
    "C": {
        "name": "Data Insights (MCM)",
        "description": "Data-driven modeling requiring analysis of provided datasets",
        "typical_topics": [
            "Pattern recognition",
            "Predictive modeling",
            "Classification/clustering",
            "Time series analysis",
            "Data-driven decision making"
        ],
        "recommended_models": [
            "Regression Models (Linear, Logistic)",
            "Machine Learning (Random Forest, SVM)",
            "Time Series (ARIMA, Prophet)",
            "Clustering (K-means, DBSCAN)",
            "Neural Networks (if appropriate)"
        ],
        "key_techniques": [
            "Exploratory data analysis",
            "Feature engineering",
            "Cross-validation",
            "Statistical testing",
            "Visualization"
        ]
    },
    "D": {
        "name": "Operations Research (ICM)",
        "description": "Operations research and management science problems",
        "typical_topics": [
            "Supply chain optimization",
            "Network design",
            "Logistics and routing",
            "Resource management",
            "Policy optimization"
        ],
        "recommended_models": [
            "Linear/Integer Programming",
            "Network Flow Models",
            "Simulation Models",
            "Multi-criteria Decision Analysis",
            "Stochastic Programming"
        ],
        "key_techniques": [
            "OR modeling techniques",
            "Cost-benefit analysis",
            "Scenario analysis",
            "Sensitivity analysis",
            "Implementation planning"
        ]
    },
    "E": {
        "name": "Sustainability (ICM)",
        "description": "Environmental science and sustainability problems",
        "typical_topics": [
            "Climate modeling",
            "Resource sustainability",
            "Ecosystem analysis",
            "Environmental policy",
            "Renewable energy"
        ],
        "recommended_models": [
            "System Dynamics",
            "Agent-Based Models",
            "Ecological Models",
            "Life Cycle Assessment",
            "Scenario Planning"
        ],
        "key_techniques": [
            "Environmental data analysis",
            "Long-term forecasting",
            "Uncertainty quantification",
            "Stakeholder analysis",
            "Policy impact assessment"
        ]
    },
    "F": {
        "name": "Policy (ICM)",
        "description": "Policy modeling and social science problems",
        "typical_topics": [
            "Social systems modeling",
            "Policy impact analysis",
            "Public health",
            "Economic modeling",
            "Behavioral modeling"
        ],
        "recommended_models": [
            "Agent-Based Models",
            "System Dynamics",
            "Epidemiological Models (SIR)",
            "Game Theory",
            "Econometric Models"
        ],
        "key_techniques": [
            "Stakeholder analysis",
            "Scenario analysis",
            "Social network analysis",
            "Behavioral modeling",
            "Policy simulation"
        ]
    }
}

# Standard MCM/ICM section structure with page allocations
BASE_OUTLINE = {
    "Summary": {
        "pages": "1",
        "content": [
            "Problem restatement (1-2 sentences)",
            "Approach overview and key methods",
            "Main results and findings",
            "Key insights and recommendations",
            "Strengths and limitations (brief)",
        ],
        "tips": [
            "Write this LAST, after completing the paper",
            "Must be exactly 1 page",
            "Include 4-6 keywords at the end",
            "This is what judges read first - make it count!"
        ]
    },
    "Introduction": {
        "pages": "1.5-2",
        "content": [
            "Problem background and context",
            "Problem restatement in your own words",
            "Key requirements and objectives",
            "Overview of your approach",
            "Paper organization"
        ],
        "tips": [
            "Show you understand WHY this problem matters",
            "Clearly state what you will deliver",
            "Don't include detailed methods here"
        ]
    },
    "Assumptions": {
        "pages": "1-1.5",
        "content": [
            "List all assumptions clearly (numbered)",
            "Provide justification for each assumption",
            "Explain how assumptions simplify the problem",
            "Discuss impact of key assumptions",
            "Define notation table"
        ],
        "tips": [
            "5-10 well-justified assumptions is typical",
            "Assumptions should be reasonable and defensible",
            "Include a notation/symbol table"
        ]
    },
    "Model Development": {
        "pages": "5-8",
        "content": [
            "Model overview and framework",
            "Detailed model formulation",
            "Mathematical equations and derivations",
            "Algorithm or solution method",
            "Implementation details"
        ],
        "tips": [
            "This is the core of your paper",
            "Explain WHY you chose this approach",
            "Include diagrams and flowcharts",
            "Show the mathematics clearly"
        ]
    },
    "Results": {
        "pages": "4-6",
        "content": [
            "Data description and sources",
            "Model calibration/parameter fitting",
            "Main results with visualizations",
            "Quantitative analysis",
            "Interpretation of results"
        ],
        "tips": [
            "Use high-quality figures and tables",
            "Every figure must be referenced in text",
            "Explain what results MEAN, not just what they ARE"
        ]
    },
    "Sensitivity Analysis": {
        "pages": "2-3",
        "content": [
            "Parameter sensitivity testing",
            "Model robustness analysis",
            "Validation against known cases",
            "Error/uncertainty analysis"
        ],
        "tips": [
            "Test 2-4 key parameters",
            "Show your model isn't cherry-picked",
            "Discuss what happens when assumptions change"
        ]
    },
    "Strengths and Weaknesses": {
        "pages": "1-1.5",
        "content": [
            "Model strengths (3-5 points)",
            "Model weaknesses (3-5 points)",
            "Comparison with alternative approaches",
            "Potential improvements"
        ],
        "tips": [
            "Be honest about limitations",
            "For each weakness, suggest mitigation",
            "Judges appreciate self-awareness"
        ]
    },
    "Conclusions": {
        "pages": "1-1.5",
        "content": [
            "Summary of key findings",
            "Recommendations based on analysis",
            "Answers to specific problem questions",
            "Future work suggestions"
        ],
        "tips": [
            "Directly answer all problem requirements",
            "Make recommendations actionable",
            "End strong!"
        ]
    },
    "References": {
        "pages": "0.5-1",
        "content": [
            "All cited sources",
            "Proper citation format",
            "10-20 references is typical"
        ],
        "tips": [
            "Use academic sources when possible",
            "Cite datasets and tools used",
            "Include URLs for web sources"
        ]
    }
}


def generate_outline(
    problem_type: str,
    requirements: list = None,
    title: str = None,
    output_path: Path = None
) -> str:
    """Generate a structured outline for MCM/ICM paper."""
    
    problem_info = PROBLEM_TYPES.get(problem_type.upper())
    if not problem_info:
        raise ValueError(f"Unknown problem type: {problem_type}. Use A, B, C, D, E, or F.")
    
    lines = []
    
    # Header
    lines.append(f"# MCM/ICM Paper Outline")
    lines.append("")
    lines.append(f"**Problem Type:** {problem_type.upper()} - {problem_info['name']}")
    if title:
        lines.append(f"**Problem Title:** {title}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    
    # Problem Type Overview
    lines.append("---")
    lines.append("")
    lines.append("## Problem Type Overview")
    lines.append("")
    lines.append(f"> {problem_info['description']}")
    lines.append("")
    
    lines.append("### Typical Topics for Problem " + problem_type.upper())
    for topic in problem_info["typical_topics"]:
        lines.append(f"- {topic}")
    lines.append("")
    
    # Recommended Models
    lines.append("### Recommended Models/Approaches")
    for model in problem_info["recommended_models"]:
        lines.append(f"- {model}")
    lines.append("")
    
    lines.append("### Key Techniques")
    for technique in problem_info["key_techniques"]:
        lines.append(f"- {technique}")
    lines.append("")
    
    # Requirements (if provided)
    if requirements:
        lines.append("---")
        lines.append("")
        lines.append("## Specific Requirements")
        lines.append("")
        for i, req in enumerate(requirements, 1):
            lines.append(f"{i}. {req.strip()}")
        lines.append("")
    
    # Page Budget
    lines.append("---")
    lines.append("")
    lines.append("## Page Budget (25 pages max)")
    lines.append("")
    lines.append("| Section | Pages | Cumulative |")
    lines.append("|---------|-------|------------|")
    
    total_min = 0
    total_max = 0
    for section, info in BASE_OUTLINE.items():
        pages = info["pages"]
        if "-" in pages:
            min_p, max_p = map(float, pages.split("-"))
        else:
            min_p = max_p = float(pages)
        total_min += min_p
        total_max += max_p
        lines.append(f"| {section} | {pages} | {total_min:.1f}-{total_max:.1f} |")
    
    lines.append(f"| **Total** | **{total_min:.1f}-{total_max:.1f}** | |")
    lines.append("")
    lines.append(f"> Remaining buffer: {25-total_max:.1f}-{25-total_min:.1f} pages for appendices or expansion")
    lines.append("")
    
    # Detailed Outline
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Section Outline")
    lines.append("")
    
    for section, info in BASE_OUTLINE.items():
        lines.append(f"### {section}")
        lines.append(f"**Target: {info['pages']} page(s)**")
        lines.append("")
        
        lines.append("**Key Content:**")
        for item in info["content"]:
            lines.append(f"- [ ] {item}")
        lines.append("")
        
        lines.append("**Tips:**")
        for tip in info["tips"]:
            lines.append(f"- {tip}")
        lines.append("")
    
    # Model Development Specifics
    lines.append("---")
    lines.append("")
    lines.append("## Model Development Strategy")
    lines.append("")
    lines.append(f"For Problem {problem_type.upper()}, consider this approach:")
    lines.append("")
    
    # Problem-specific model suggestions
    if problem_type.upper() in ["A", "B"]:
        lines.append("### Suggested Model Structure")
        lines.append("1. **Primary Model**: Main mathematical model addressing core problem")
        lines.append("2. **Optimization Layer**: How you find optimal solutions")
        lines.append("3. **Validation**: How you verify model correctness")
        lines.append("")
    elif problem_type.upper() == "C":
        lines.append("### Suggested Model Structure")
        lines.append("1. **Data Pipeline**: Preprocessing, cleaning, feature engineering")
        lines.append("2. **Exploratory Analysis**: Initial patterns and insights")
        lines.append("3. **Predictive Model**: ML/statistical models for predictions")
        lines.append("4. **Interpretation**: What the results mean for stakeholders")
        lines.append("")
    elif problem_type.upper() in ["D", "E", "F"]:
        lines.append("### Suggested Model Structure")
        lines.append("1. **System Model**: How the system/environment works")
        lines.append("2. **Intervention Model**: How policies/changes affect outcomes")
        lines.append("3. **Scenario Analysis**: Different futures/conditions")
        lines.append("4. **Recommendations**: Actionable policy suggestions")
        lines.append("")
    
    # Timeline
    lines.append("---")
    lines.append("")
    lines.append("## Suggested Timeline")
    lines.append("")
    lines.append("| Time | Task |")
    lines.append("|------|------|")
    lines.append("| Day 1 (0-8 hrs) | Read problem, brainstorm, research, gather data |")
    lines.append("| Day 1-2 (8-20 hrs) | Develop initial model, start implementation |")
    lines.append("| Day 2-3 (20-36 hrs) | Refine model, generate results, create figures |")
    lines.append("| Day 3-4 (36-52 hrs) | Write paper sections, iterate on analysis |")
    lines.append("| Day 4 (52-60 hrs) | Complete draft, internal review |")
    lines.append("| Day 5 (60-72 hrs) | Final revisions, format check, proofread |")
    lines.append("| Final hours | Format check, PDF export, submission |")
    lines.append("")
    
    # Checklist
    lines.append("---")
    lines.append("")
    lines.append("## Pre-Submission Checklist")
    lines.append("")
    lines.append("- [ ] Team control number in header (Team # XXXXXXX)")
    lines.append("- [ ] Page numbers present (Page X of Y)")
    lines.append("- [ ] No team member names in paper")
    lines.append("- [ ] No school/institution names in paper")
    lines.append("- [ ] Summary is exactly 1 page with keywords")
    lines.append("- [ ] All figures referenced in text")
    lines.append("- [ ] All tables referenced in text")
    lines.append("- [ ] References section complete")
    lines.append("- [ ] Page count <= 25 pages")
    lines.append("- [ ] All problem requirements addressed")
    lines.append("- [ ] PDF renders correctly")
    lines.append("- [ ] Spell check complete")
    lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append("*Good luck with your MCM/ICM paper!*")
    
    content = "\n".join(lines)
    
    # Save to file
    if output_path is None:
        output_path = Path.cwd() / "outline.md"
    
    output_path.write_text(content, encoding="utf-8")
    
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate MCM/ICM paper outline based on problem type",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_outline.py --problem-type C
  python generate_outline.py -p A --requirements "minimize cost,satisfy constraints"
  python generate_outline.py --problem-type E --title "Climate Change Model"
  python generate_outline.py -p B -o my_outline.md

Problem Types:
  A - Continuous (MCM): Differential equations, optimization
  B - Discrete (MCM): Graph theory, combinatorics
  C - Data Insights (MCM): Data analysis, ML
  D - Operations Research (ICM): Logistics, networks
  E - Sustainability (ICM): Environmental modeling
  F - Policy (ICM): Social systems, policy analysis
        """
    )
    
    parser.add_argument(
        "-p", "--problem-type",
        type=str,
        required=True,
        choices=["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"],
        help="MCM/ICM problem type (A-F)"
    )
    
    parser.add_argument(
        "-r", "--requirements",
        type=str,
        default=None,
        help="Comma-separated list of specific requirements"
    )
    
    parser.add_argument(
        "-t", "--title",
        type=str,
        default=None,
        help="Problem title or brief description"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output file path (default: outline.md in current directory)"
    )
    
    args = parser.parse_args()
    
    # Parse requirements
    requirements = None
    if args.requirements:
        requirements = [r.strip() for r in args.requirements.split(",")]
    
    # Output path
    output_path = Path(args.output) if args.output else None
    
    # Generate outline
    try:
        result_path = generate_outline(
            problem_type=args.problem_type.upper(),
            requirements=requirements,
            title=args.title,
            output_path=output_path
        )
        
        print(f"Outline generated successfully!")
        print(f"Output: {result_path}")
        print("")
        print("Next steps:")
        print("  1. Review the outline and customize for your specific problem")
        print("  2. Start with the Introduction while ideas are fresh")
        print("  3. Develop your model in parallel with writing")
        print("  4. Write the Summary LAST")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
