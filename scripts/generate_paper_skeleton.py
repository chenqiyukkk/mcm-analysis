#!/usr/bin/env python3
"""
MCM/ICM Paper Skeleton Generator

Generates complete LaTeX paper skeleton from templates.
Supports two modes:
  - structure: Framework with placeholders (~3 pages)
  - draft: Complete Chinese draft content (~12-15 pages)

Usage:
    python generate_paper_skeleton.py -p C -y 2026 --mode structure
    python generate_paper_skeleton.py -p A -y 2026 --mode draft --team "TeamName"
    python generate_paper_skeleton.py -p D -y 2026  # Interactive mode

Output:
    Generates main.tex and optional sections/ directory
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, List, Tuple


# =============================================================================
# Configuration
# =============================================================================

# Section order for MCM/ICM papers
SECTIONS: List[str] = [
    "summary",
    "introduction",
    "assumptions",
    "model",
    "results",
    "sensitivity",
    "strengths",
    "conclusion"
]

# Valid problem types
VALID_PROBLEMS: List[str] = ["A", "B", "C", "D", "E", "F"]

# Template directory relative to script location
TEMPLATE_DIR: Path = Path(__file__).parent.parent / "templates" / "latex"


# =============================================================================
# Core Functions
# =============================================================================

def get_template_path(section: str, mode: str) -> Path:
    """
    Get template file path for a section.
    
    Args:
        section: Section name (e.g., 'summary', 'introduction')
        mode: Template mode ('structure' or 'draft')
    
    Returns:
        Path to the template file
    
    Raises:
        FileNotFoundError: If template directory doesn't exist
    """
    sections_dir = TEMPLATE_DIR / "sections"
    template_file = f"{section}_{mode}.tex"
    return sections_dir / template_file


def read_template(template_path: Path) -> str:
    """
    Read template file content.
    
    Args:
        template_path: Path to template file
    
    Returns:
        Template content as string
    
    Raises:
        FileNotFoundError: If template file doesn't exist
    """
    try:
        return template_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Template not found: {template_path}")
        raise


def read_preamble() -> str:
    """
    Read the LaTeX preamble template.
    
    Returns:
        Preamble content as string
    """
    preamble_path = TEMPLATE_DIR / "preamble.tex"
    return read_template(preamble_path)


def create_main_tex_header(problem: str, year: int, team: Optional[str]) -> str:
    """
    Create the main.tex header with document class and metadata.
    
    Args:
        problem: Problem letter (A-F)
        year: Competition year
        team: Optional team name
    
    Returns:
        LaTeX header string
    """
    header_lines = [
        r"\documentclass[12pt]{article}",
        r"",
        r"% ============================================================================",
        r"% MCM/ICM Paper",
        f"% Problem: {problem}",
        f"% Year: {year}",
    ]
    
    if team:
        header_lines.append(f"% Team: {team}")
    
    header_lines.extend([
        r"% ============================================================================",
        r"",
        r"% ----- Preamble -----",
        r"\input{preamble}",
        r"",
        r"% ============================================================================",
        r"\begin{document}",
        r"",
    ])
    
    return "\n".join(header_lines)


def create_main_tex_footer() -> str:
    """
    Create the main.tex footer.
    
    Returns:
        LaTeX footer string
    """
    return "\n".join([
        r"",
        r"\end{document}",
        r""
    ])


def interactive_select_mode() -> str:
    """
    Interactive mode to select generation mode.
    
    Returns:
        Selected mode ('structure' or 'draft')
    """
    print("\n" + "=" * 60)
    print("MCM/ICM Paper Skeleton Generator")
    print("=" * 60)
    print("\nSelect generation mode:")
    print("  1. Structure mode - Framework with placeholders (~3 pages)")
    print("     Suitable for: Initial planning, understanding structure")
    print("  2. Draft mode - Complete Chinese draft content (~12-15 pages)")
    print("     Suitable for: Starting with content, then translate to English")
    print("")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            return "structure"
        elif choice == "2":
            return "draft"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def generate_paper(
    problem: str,
    year: int,
    mode: str,
    team: Optional[str] = None,
    output_dir: Optional[Path] = None,
    separate_sections: bool = False
) -> Path:
    """
    Generate complete LaTeX paper skeleton.
    
    Args:
        problem: Problem letter (A-F)
        year: Competition year
        mode: Generation mode ('structure' or 'draft')
        team: Optional team name for metadata
        output_dir: Output directory (default: current directory)
        separate_sections: If True, save sections as separate files
    
    Returns:
        Path to generated main.tex file
    
    Raises:
        ValueError: If problem type or mode is invalid
        FileNotFoundError: If templates are missing
    """
    # Validate inputs
    problem = problem.upper()
    if problem not in VALID_PROBLEMS:
        raise ValueError(f"Invalid problem type: {problem}. Use: {', '.join(VALID_PROBLEMS)}")
    
    if mode not in ["structure", "draft"]:
        raise ValueError(f"Invalid mode: {mode}. Use 'structure' or 'draft'")
    
    # Set output directory
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nGenerating MCM/ICM {year} Problem {problem} paper skeleton...")
    print(f"Mode: {mode}")
    print(f"Output: {output_dir}")
    print("-" * 60)
    
    # Read preamble
    print("Reading preamble...")
    preamble_content = read_preamble()
    
    # Create sections directory if needed
    sections_dir: Optional[Path] = None
    if separate_sections:
        sections_dir = output_dir / "sections"
        sections_dir.mkdir(exist_ok=True)
        print(f"Created sections directory: {sections_dir}")
    
    # Generate main.tex content
    main_content_parts: List[str] = []
    
    # Add header
    main_content_parts.append(create_main_tex_header(problem, year, team))
    
    # Add preamble as separate file or inline
    if separate_sections:
        preamble_path = output_dir / "preamble.tex"
        preamble_path.write_text(preamble_content, encoding="utf-8")
        print(f"  Created: preamble.tex")
    else:
        # Inline preamble
        main_content_parts.append("% ----- Preamble Content -----")
        main_content_parts.append(preamble_content)
        main_content_parts.append("")
    
    # Process each section
    print(f"\nProcessing {len(SECTIONS)} sections...")
    section_contents: List[str] = []
    
    for section in SECTIONS:
        template_path = get_template_path(section, mode)
        
        try:
            section_content = read_template(template_path)
            
            if separate_sections and sections_dir is not None:
                # Write to separate file
                section_file = sections_dir / f"{section}.tex"
                section_file.write_text(section_content, encoding="utf-8")
                print(f"  Created: sections/{section}.tex")
                section_contents.append(f"\\input{{sections/{section}}}")
            else:
                # Inline section
                section_contents.append(f"% ----- {section.upper()} -----")
                section_contents.append(section_content)
                section_contents.append("")
                print(f"  Added: {section}")
                
        except FileNotFoundError:
            print(f"  Warning: Template missing for {section}, skipping...")
            continue
    
    # Add section includes or inline content
    main_content_parts.extend(section_contents)
    
    # Add footer
    main_content_parts.append(create_main_tex_footer())
    
    # Write main.tex
    main_tex_path = output_dir / "main.tex"
    main_tex_content = "\n".join(main_content_parts)
    main_tex_path.write_text(main_tex_content, encoding="utf-8")
    
    print("-" * 60)
    print(f"[OK] Successfully generated: {main_tex_path}")
    
    # Print summary
    line_count = len(main_tex_content.splitlines())
    print(f"\nSummary:")
    print(f"  Total lines: {line_count}")
    print(f"  Sections: {len(SECTIONS)}")
    print(f"  Mode: {mode}")
    
    if mode == "structure":
        print(f"  Expected pages: ~3 pages (framework only)")
    else:
        print(f"  Expected pages: ~12-15 pages (with Chinese draft content)")
    
    print(f"\nNext steps:")
    print(f"  1. cd {output_dir}")
    print(f"  2. Edit main.tex to customize content")
    if mode == "draft":
        print(f"  3. Translate Chinese content to English")
    print(f"  4. Compile with: pdflatex main.tex")
    
    return main_tex_path


def main() -> int:
    """
    Main entry point for the script.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = argparse.ArgumentParser(
        description="Generate MCM/ICM paper skeleton from templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate structure framework
  python generate_paper_skeleton.py -p C -y 2026 --mode structure
  
  # Generate Chinese draft
  python generate_paper_skeleton.py -p A -y 2026 --mode draft --team "MyTeam"
  
  # Interactive mode (will prompt for mode selection)
  python generate_paper_skeleton.py -p D -y 2026
  
  # Output to specific directory
  python generate_paper_skeleton.py -p B -y 2026 --mode draft -o ./my_paper

Problem Types:
  A - Continuous (MCM): Differential equations, optimization
  B - Discrete (MCM): Graph theory, combinatorics
  C - Data Insights (MCM): Data analysis, ML
  D - Operations Research (ICM): Logistics, networks
  E - Sustainability (ICM): Environmental modeling
  F - Policy (ICM): Social systems, policy analysis

Modes:
  structure - Framework with TODO placeholders (~3 pages)
  draft     - Complete Chinese draft content (~12-15 pages)
        """
    )
    
    parser.add_argument(
        "-p", "--problem",
        type=str,
        required=True,
        choices=VALID_PROBLEMS + [p.lower() for p in VALID_PROBLEMS],
        help="Problem letter (A-F)"
    )
    
    parser.add_argument(
        "-y", "--year",
        type=int,
        required=True,
        help="Competition year (e.g., 2026)"
    )
    
    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["structure", "draft"],
        default=None,
        help="Generation mode (default: interactive selection)"
    )
    
    parser.add_argument(
        "-t", "--team",
        type=str,
        default=None,
        help="Team name (optional, for metadata)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output directory (default: current directory)"
    )
    
    parser.add_argument(
        "--separate-sections",
        action="store_true",
        help="Save each section as a separate file in sections/"
    )
    
    args = parser.parse_args()
    
    # Determine mode
    mode = args.mode
    if mode is None:
        mode = interactive_select_mode()
    
    # Parse output directory
    output_dir = Path(args.output) if args.output else None
    
    try:
        generate_paper(
            problem=args.problem.upper(),
            year=args.year,
            mode=mode,
            team=args.team,
            output_dir=output_dir,
            separate_sections=args.separate_sections
        )
        return 0
        
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nMake sure template files exist in templates/latex/")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
