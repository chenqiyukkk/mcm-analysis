#!/usr/bin/env python3
"""
MCM/ICM Problem Parser

Automatically extracts key information from MCM/ICM problem PDFs.

Usage:
    python parse_problem.py 2026_MCM_Problem_C.pdf
    python parse_problem.py problem.pdf -o ./analysis/
    python parse_problem.py --batch ./problems/*.pdf

Output:
    Generates structured JSON and Markdown reports
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Any


# Configuration - Enhanced with references/problem-types.md
VALID_PROBLEMS = ["A", "B", "C", "D", "E", "F"]

# Enhanced keywords based on references/problem-types.md analysis
PROBLEM_TYPE_PROFILES = {
    "A": {
        "name": "Continuous (MCM)",
        "keywords": [
            "differential equation", "dynamical system", "population", "ecology",
            "physics", "continuous", "growth", "decay", "diffusion", "flow",
            "rate", "derivative", "ODE", "PDE", "stability", "equilibrium",
            "species", "organism", "environment", "climate", "temperature",
            "Lotka-Volterra", "predator-prey", "competition", "cellular automaton"
        ],
        "domains": ["ecology", "physics", "environmental science", "biology"],
        "models": ["Differential Equations", "Lotka-Volterra", "Cellular Automaton", "Monte Carlo"]
    },
    "B": {
        "name": "Discrete (MCM)",
        "keywords": [
            "discrete", "combinatorial", "optimization", "scheduling", "routing",
            "network", "graph", "algorithm", "integer programming", "allocation",
            "facility location", "covering", "packing", "assignment", "sequence",
            "timetable", "planning", "discrete event", "queue", "logistics",
            "multi-objective", "genetic algorithm", "NSGA-II", "Bayesian search"
        ],
        "domains": ["logistics", "operations research", "emergency response"],
        "models": ["Integer Programming", "Genetic Algorithm", "Queuing Theory", "MCLP"]
    },
    "C": {
        "name": "Data Insights (MCM)",
        "keywords": [
            "data", "dataset", "machine learning", "ML", "prediction", "forecast",
            "classification", "clustering", "regression", "time series", "pattern",
            "trend", "analysis", "insight", "feature", "model training", "test set",
            "validation", "accuracy", "correlation", "statistics", "CSV", "Excel",
            "random forest", "XGBoost", "neural network", "LSTM", "sentiment"
        ],
        "domains": ["sports analytics", "e-commerce", "gaming", "social phenomena"],
        "models": ["Random Forest", "XGBoost", "Neural Networks", "Time Series", "Clustering"]
    },
    "D": {
        "name": "Operations Research/Network (ICM)",
        "keywords": [
            "network", "graph theory", "node", "edge", "centrality", "PageRank",
            "connectivity", "path", "flow", "influence", "relationship", "link",
            "topology", "community", "cluster", "system", "interconnection",
            "dependency", "structure", "organization", "HITS", "betweenness"
        ],
        "domains": ["infrastructure", "SDGs", "music", "culture", "sports networks"],
        "models": ["PageRank", "Network Centrality", "Correlation Networks", "System Dynamics"]
    },
    "E": {
        "name": "Sustainability (ICM)",
        "keywords": [
            "sustainability", "environment", "climate", "risk", "assessment",
            "policy", "impact", "evaluation", "index", "indicator", "green",
            "carbon", "pollution", "resource", "conservation", "protection",
            "ecosystem service", "biodiversity", "renewable", "energy",
            "AHP", "EWM", "life cycle assessment"
        ],
        "domains": ["climate", "insurance", "pollution", "resource management"],
        "models": ["AHP-EWM", "Risk Assessment", "Life Cycle Assessment", "Scenario Planning"]
    },
    "F": {
        "name": "Policy (ICM)",
        "keywords": [
            "policy", "social", "behavior", "stakeholder", "decision", "strategy",
            "game theory", "incentive", "public", "government", "regulation",
            "economic", "market", "agent", "simulation", "opinion", "consensus",
            "cooperation", "conflict", "negotiation", "agent-based model"
        ],
        "domains": ["social systems", "public health", "economic modeling"],
        "models": ["Agent-Based Models", "Game Theory", "System Dynamics", "Epidemiological"]
    }
}


@dataclass
class SubProblem:
    id: str
    title: str
    description: str = ""


@dataclass
class ProblemAnalysis:
    year: Optional[int] = None
    problem_type: Optional[str] = None
    problem_letter: Optional[str] = None
    problem_title: str = ""
    parsed_at: str = field(default_factory=lambda: datetime.now().isoformat())
    type_confidence: float = 0.0
    background_domain: str = ""
    subproblems: List[SubProblem] = field(default_factory=list)
    data_files: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    key_terms: List[str] = field(default_factory=list)
    raw_text: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ProblemParser:
    def __init__(self):
        self.analysis = ProblemAnalysis()
    
    def parse_pdf(self, pdf_path: Path) -> ProblemAnalysis:
        pdf_path = Path(pdf_path)
        
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        print(f"Parsing: {pdf_path.name}")
        print("-" * 60)
        
        self._extract_metadata_from_filename(pdf_path.name)
        raw_text = self._extract_text_from_pdf(pdf_path)
        self.analysis.raw_text = raw_text
        
        print("Analyzing problem type...")
        self._identify_problem_type(raw_text)
        
        print("Extracting subproblems...")
        self._extract_subproblems(raw_text)
        
        print("Identifying data files...")
        self._extract_data_files(raw_text)
        
        print("Extracting constraints...")
        self._extract_constraints(raw_text)
        
        print("-" * 60)
        print("[OK] Analysis complete!")
        
        return self.analysis
    
    def _extract_metadata_from_filename(self, filename: str) -> None:
        year_match = re.search(r'20\d{2}', filename)
        if year_match:
            self.analysis.year = int(year_match.group())
        
        problem_match = re.search(r'[ _][ABCDEF][ _]', filename, re.IGNORECASE)
        if problem_match:
            self.analysis.problem_letter = problem_match.group().strip(' _').upper()
    
    def _extract_text_from_pdf(self, pdf_path: Path) -> str:
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(pdf_path))
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except ImportError:
            print("Warning: pypdf not installed. Trying pdfplumber...")
            try:
                import pdfplumber
                with pdfplumber.open(pdf_path) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text() or ""
                        text += "\n"
                    return text
            except ImportError:
                raise ImportError("Please install pypdf or pdfplumber: pip install pypdf")
    
    def _identify_problem_type(self, text: str) -> None:
        text_lower = text.lower()
        scores = {}
        
        for problem_type, profile in PROBLEM_TYPE_PROFILES.items():
            keywords = profile["keywords"]
            score = sum(1 for keyword in keywords if keyword.lower() in text_lower)
            scores[problem_type] = score
        
        if scores:
            best_match = max(scores.items(), key=lambda x: x[1])[0]
            max_score = scores[best_match]
            total_keywords = len(PROBLEM_TYPE_PROFILES[best_match]["keywords"])
            confidence = min(max_score / total_keywords * 3, 1.0)
            
            self.analysis.problem_type = best_match
            self.analysis.type_confidence = round(confidence, 2)
            self.analysis.background_domain = PROBLEM_TYPE_PROFILES[best_match]["domains"][0]
    
    def _extract_subproblems(self, text: str) -> None:
        patterns = [
            r'(?:Task|Question|Problem|Q)\s*(\d+)[\s:.)]+([^\n]+)',
            r'(?:^|\n)\s*(\d+)\.\s+([^\n]+)',
        ]
        
        found = set()
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                num = match.group(1)
                title = match.group(2).strip()
                if len(title) > 10 and num not in found:
                    found.add(num)
                    subproblem = SubProblem(
                        id=f"Q{num}",
                        title=title[:200]
                    )
                    self.analysis.subproblems.append(subproblem)
    
    def _extract_data_files(self, text: str) -> None:
        patterns = [
            r'\b([\w_]+\.(?:csv|xlsx?|txt|json|xml|dat))\b',
            r'(?:file|dataset|data)\s+[\"\']?([\w_]+\.(?:csv|xlsx?|txt))[\"\']?',
        ]
        
        found = set()
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                filename = match.group(1)
                if filename.lower() not in found:
                    found.add(filename.lower())
                    self.analysis.data_files.append(filename)
    
    def _extract_constraints(self, text: str) -> None:
        constraint_keywords = [
            "must", "should", "required", "constraint", "limit", "maximum", "minimum",
            "at most", "at least", "cannot", "must not", "assume", "given"
        ]
        
        sentences = re.split(r'[.!?]\s+', text)
        for sentence in sentences:
            sentence = sentence.strip()
            if any(kw in sentence.lower() for kw in constraint_keywords):
                if 20 < len(sentence) < 200:
                    self.analysis.constraints.append(sentence)


def generate_markdown_report(analysis: ProblemAnalysis, output_path: Path) -> None:
    lines = []
    lines.append("# MCM/ICM Problem Analysis Report")
    lines.append("")
    lines.append(f"**Generated:** {analysis.parsed_at}")
    lines.append("")
    
    if analysis.year:
        lines.append(f"**Year:** {analysis.year}")
    if analysis.problem_type:
        lines.append(f"**Problem Type:** {analysis.problem_type}")
        lines.append(f"**Confidence:** {analysis.type_confidence:.0%}")
    lines.append("")
    
    lines.append("## Subproblems")
    for sp in analysis.subproblems:
        lines.append(f"- **{sp.id}:** {sp.title}")
    lines.append("")
    
    lines.append("## Data Files")
    if analysis.data_files:
        for df in analysis.data_files:
            lines.append(f"- {df}")
    else:
        lines.append("- No data files identified")
    lines.append("")
    
    lines.append("## Constraints")
    for i, constraint in enumerate(analysis.constraints[:10], 1):
        lines.append(f"{i}. {constraint}")
    lines.append("")
    
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Parse MCM/ICM problem PDFs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python parse_problem.py 2026_MCM_Problem_C.pdf
  python parse_problem.py problem.pdf -o ./analysis/
  python parse_problem.py --batch ./problems/*.pdf
        """
    )
    
    parser.add_argument("pdf", nargs="?", help="PDF file to parse")
    parser.add_argument("-o", "--output", help="Output directory")
    parser.add_argument("--batch", action="store_true", help="Batch mode")
    parser.add_argument("--format", choices=["json", "markdown", "both"], default="both")
    
    args = parser.parse_args()
    
    if not args.pdf and not args.batch:
        parser.print_help()
        return 1
    
    output_dir = Path(args.output) if args.output else Path.cwd()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = [Path(args.pdf)] if args.pdf else list(Path.cwd().glob("*.pdf"))
    
    for pdf_file in pdf_files:
        try:
            problem_parser = ProblemParser()
            analysis = problem_parser.parse_pdf(pdf_file)
            
            base_name = pdf_file.stem
            
            if args.format in ["json", "both"]:
                json_path = output_dir / f"{base_name}_analysis.json"
                json_path.write_text(
                    json.dumps(analysis.to_dict(), indent=2, ensure_ascii=False),
                    encoding="utf-8"
                )
                print(f"Saved JSON: {json_path}")
            
            if args.format in ["markdown", "both"]:
                md_path = output_dir / f"{base_name}_analysis.md"
                generate_markdown_report(analysis, md_path)
                print(f"Saved Markdown: {md_path}")
            
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
            continue
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
