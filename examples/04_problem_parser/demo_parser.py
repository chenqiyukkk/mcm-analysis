#!/usr/bin/env python3
"""
Demo script for Phase 2: Problem Parser
Tests the parse_problem functionality with sample text
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from parse_problem import ProblemParser, generate_markdown_report

def main():
    print("=" * 70)
    print("PHASE 2 DEMONSTRATION: Problem Parser")
    print("=" * 70)
    print()
    
    # Read sample problem text
    sample_file = Path(__file__).parent / "sample_problem_2026_C.txt"
    
    if not sample_file.exists():
        print(f"Error: Sample file not found: {sample_file}")
        return 1
    
    sample_text = sample_file.read_text(encoding="utf-8")
    
    print("Sample Problem Loaded:")
    print(f"  File: {sample_file.name}")
    print(f"  Length: {len(sample_text)} characters")
    print()
    
    # Create parser and manually set the text
    parser = ProblemParser()
    parser.analysis.raw_text = sample_text
    
    # Extract metadata from filename
    parser._extract_metadata_from_filename("2026_MCM_Problem_C.txt")
    
    print("-" * 70)
    print("STEP 1: Identifying Problem Type...")
    print("-" * 70)
    parser._identify_problem_type(sample_text)
    print(f"  Problem Type: {parser.analysis.problem_type}")
    print(f"  Confidence: {parser.analysis.type_confidence:.0%}")
    print(f"  Domain: {parser.analysis.background_domain}")
    print()
    
    print("-" * 70)
    print("STEP 2: Extracting Subproblems...")
    print("-" * 70)
    parser._extract_subproblems(sample_text)
    print(f"  Found {len(parser.analysis.subproblems)} subproblems:")
    for sp in parser.analysis.subproblems:
        print(f"    - {sp.id}: {sp.title[:80]}...")
    print()
    
    print("-" * 70)
    print("STEP 3: Identifying Data Files...")
    print("-" * 70)
    parser._extract_data_files(sample_text)
    print(f"  Found {len(parser.analysis.data_files)} data files:")
    for df in parser.analysis.data_files:
        print(f"    - {df}")
    print()
    
    print("-" * 70)
    print("STEP 4: Extracting Constraints...")
    print("-" * 70)
    parser._extract_constraints(sample_text)
    print(f"  Found {len(parser.analysis.constraints)} constraints:")
    for i, constraint in enumerate(parser.analysis.constraints[:5], 1):
        print(f"    {i}. {constraint[:100]}...")
    print()
    
    # Generate output
    output_dir = Path(__file__).parent / "demo_output"
    output_dir.mkdir(exist_ok=True)
    
    print("-" * 70)
    print("STEP 5: Generating Reports...")
    print("-" * 70)
    
    # JSON output
    import json
    json_path = output_dir / "demo_analysis.json"
    json_path.write_text(
        json.dumps(parser.analysis.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"  [OK] JSON report: {json_path}")
    
    # Markdown output
    md_path = output_dir / "demo_analysis.md"
    generate_markdown_report(parser.analysis, md_path)
    print(f"  [OK] Markdown report: {md_path}")
    print()
    
    print("=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)
    print()
    print("Generated files:")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    print()
    print("You can view these files to see the full analysis output.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
