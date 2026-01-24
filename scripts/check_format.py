#!/usr/bin/env python3
"""
MCM/ICM Paper Format Checker

Checks PDF papers for MCM/ICM format compliance including page count,
headers, identifying information, and structural requirements.

Usage:
    python check_format.py paper.pdf
    python check_format.py paper.pdf --verbose
    python check_format.py paper.pdf --output report.txt

Requirements:
    pip install pypdf
"""

import argparse
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("Error: Please install pypdf or PyPDF2")
        print("  pip install pypdf")
        print("  or")
        print("  pip install PyPDF2")
        sys.exit(1)


# =============================================================================
# Check Functions
# =============================================================================

class FormatChecker:
    """MCM/ICM paper format checker."""
    
    MAX_PAGES = 25
    TEAM_NUMBER_PATTERN = r"Team\s*#?\s*\d{7}"
    PAGE_HEADER_PATTERN = r"Page\s+\d+\s+of\s+\d+"
    
    # Common university/school name patterns
    SCHOOL_PATTERNS = [
        r"university",
        r"college",
        r"institute",
        r"school\s+of",
        r"department\s+of",
        r"faculty\s+of",
        r"MIT\b",
        r"UCLA",
        r"Stanford",
        r"Harvard",
        r"Berkeley",
        r"Tsinghua",
        r"Peking\s+University",
        r"PKU\b",
    ]
    
    # Common name patterns (very basic check)
    NAME_INDICATORS = [
        r"submitted\s+by",
        r"authors?:",
        r"prepared\s+by",
        r"team\s+members?:",
        r"written\s+by",
    ]
    
    def __init__(self, pdf_path: str, verbose: bool = False):
        self.pdf_path = Path(pdf_path)
        self.verbose = verbose
        self.results = []
        self.text_content = []
        self.reader = None
        
    def load_pdf(self) -> bool:
        """Load the PDF file."""
        if not self.pdf_path.exists():
            self._add_result("ERROR", "FILE", f"File not found: {self.pdf_path}")
            return False
        
        if not self.pdf_path.suffix.lower() == ".pdf":
            self._add_result("ERROR", "FILE", "File is not a PDF")
            return False
        
        try:
            self.reader = PdfReader(str(self.pdf_path))
            
            # Extract text from all pages
            for page in self.reader.pages:
                text = page.extract_text() or ""
                self.text_content.append(text)
            
            self._add_result("PASS", "FILE", f"Successfully loaded: {self.pdf_path.name}")
            return True
            
        except Exception as e:
            self._add_result("ERROR", "FILE", f"Failed to read PDF: {str(e)}")
            return False
    
    def _add_result(self, status: str, category: str, message: str, details: str = None):
        """Add a check result."""
        self.results.append({
            "status": status,
            "category": category,
            "message": message,
            "details": details
        })
    
    def check_page_count(self):
        """Check if page count is within limit."""
        page_count = len(self.reader.pages)
        
        if page_count <= self.MAX_PAGES:
            self._add_result(
                "PASS", 
                "PAGES", 
                f"Page count: {page_count}/{self.MAX_PAGES}",
                f"{self.MAX_PAGES - page_count} pages remaining"
            )
        else:
            self._add_result(
                "FAIL",
                "PAGES",
                f"Page count: {page_count}/{self.MAX_PAGES}",
                f"OVER LIMIT by {page_count - self.MAX_PAGES} pages!"
            )
    
    def check_team_number_header(self):
        """Check for team number in headers."""
        team_found = False
        team_pages = []
        
        for i, text in enumerate(self.text_content, 1):
            if re.search(self.TEAM_NUMBER_PATTERN, text, re.IGNORECASE):
                team_found = True
                team_pages.append(i)
        
        if team_found:
            if len(team_pages) == len(self.text_content):
                self._add_result(
                    "PASS",
                    "HEADER",
                    "Team number header found on all pages"
                )
            else:
                self._add_result(
                    "WARN",
                    "HEADER",
                    f"Team number found on {len(team_pages)}/{len(self.text_content)} pages",
                    f"Found on pages: {team_pages[:5]}{'...' if len(team_pages) > 5 else ''}"
                )
        else:
            self._add_result(
                "FAIL",
                "HEADER",
                "No team number header found (Team # XXXXXXX)",
                "Ensure 'Team # XXXXXXX' appears in header with your 7-digit number"
            )
    
    def check_page_number_header(self):
        """Check for page number headers."""
        page_header_found = False
        pages_with_header = []
        
        for i, text in enumerate(self.text_content, 1):
            if re.search(self.PAGE_HEADER_PATTERN, text, re.IGNORECASE):
                page_header_found = True
                pages_with_header.append(i)
        
        if page_header_found:
            coverage = len(pages_with_header) / len(self.text_content)
            if coverage >= 0.8:
                self._add_result(
                    "PASS",
                    "HEADER",
                    f"Page headers present (Page X of Y)"
                )
            else:
                self._add_result(
                    "WARN",
                    "HEADER",
                    f"Page headers found on {len(pages_with_header)}/{len(self.text_content)} pages"
                )
        else:
            self._add_result(
                "WARN",
                "HEADER",
                "Page number headers not detected (Page X of Y)",
                "Consider adding 'Page X of Y' headers"
            )
    
    def check_identifying_info(self):
        """Check for potentially identifying information."""
        full_text = " ".join(self.text_content).lower()
        
        # Check for school/university names
        school_matches = []
        for pattern in self.SCHOOL_PATTERNS:
            if re.search(pattern, full_text, re.IGNORECASE):
                school_matches.append(pattern)
        
        if school_matches:
            self._add_result(
                "WARN",
                "ANONYMOUS",
                "Possible school/institution names detected",
                f"Patterns found: {', '.join(school_matches[:3])}"
            )
        else:
            self._add_result(
                "PASS",
                "ANONYMOUS",
                "No obvious school/institution names detected"
            )
        
        # Check for name indicators
        name_matches = []
        for pattern in self.NAME_INDICATORS:
            if re.search(pattern, full_text, re.IGNORECASE):
                name_matches.append(pattern)
        
        if name_matches:
            self._add_result(
                "FAIL",
                "ANONYMOUS",
                "Possible author name indicators found",
                f"Patterns: {', '.join(name_matches)}"
            )
        else:
            self._add_result(
                "PASS",
                "ANONYMOUS",
                "No obvious author name indicators detected"
            )
    
    def check_references(self):
        """Check for references section."""
        full_text = " ".join(self.text_content)
        
        ref_patterns = [
            r"\bReferences\b",
            r"\bBibliography\b",
            r"\bWorks\s+Cited\b",
        ]
        
        ref_found = False
        for pattern in ref_patterns:
            if re.search(pattern, full_text, re.IGNORECASE):
                ref_found = True
                break
        
        if ref_found:
            self._add_result(
                "PASS",
                "STRUCTURE",
                "References section detected"
            )
        else:
            self._add_result(
                "WARN",
                "STRUCTURE",
                "No References section detected",
                "Ensure you have a clearly labeled References section"
            )
    
    def check_summary(self):
        """Check for summary/abstract section."""
        # Check first 2 pages for summary
        first_pages = " ".join(self.text_content[:2]) if len(self.text_content) >= 2 else self.text_content[0]
        
        summary_patterns = [
            r"\bSummary\b",
            r"\bAbstract\b",
            r"\bExecutive\s+Summary\b",
        ]
        
        summary_found = False
        for pattern in summary_patterns:
            if re.search(pattern, first_pages, re.IGNORECASE):
                summary_found = True
                break
        
        if summary_found:
            self._add_result(
                "PASS",
                "STRUCTURE",
                "Summary/Abstract section detected"
            )
        else:
            self._add_result(
                "WARN",
                "STRUCTURE",
                "No Summary section detected on first pages",
                "MCM requires a 1-page summary at the beginning"
            )
    
    def check_keywords(self):
        """Check for keywords."""
        first_pages = " ".join(self.text_content[:2]) if len(self.text_content) >= 2 else self.text_content[0]
        
        if re.search(r"\bKeywords?\s*:", first_pages, re.IGNORECASE):
            self._add_result(
                "PASS",
                "STRUCTURE",
                "Keywords detected"
            )
        else:
            self._add_result(
                "WARN",
                "STRUCTURE",
                "No Keywords section detected",
                "Consider adding keywords after your summary"
            )
    
    def run_all_checks(self):
        """Run all format checks."""
        if not self.load_pdf():
            return
        
        self.check_page_count()
        self.check_team_number_header()
        self.check_page_number_header()
        self.check_identifying_info()
        self.check_summary()
        self.check_references()
        self.check_keywords()
    
    def generate_report(self) -> str:
        """Generate formatted report."""
        lines = []
        lines.append("=" * 60)
        lines.append("MCM/ICM FORMAT CHECK REPORT")
        lines.append("=" * 60)
        lines.append(f"File: {self.pdf_path.name}")
        lines.append(f"Pages: {len(self.reader.pages) if self.reader else 'N/A'}")
        lines.append("=" * 60)
        lines.append("")
        
        # Group results by category
        categories = {}
        for result in self.results:
            cat = result["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(result)
        
        # Status indicators
        status_icons = {
            "PASS": "[PASS]",
            "FAIL": "[FAIL]",
            "WARN": "[WARN]",
            "ERROR": "[ERR!]",
        }
        
        # Summary counts
        counts = {"PASS": 0, "FAIL": 0, "WARN": 0, "ERROR": 0}
        
        for category, results in categories.items():
            lines.append(f"[{category}]")
            lines.append("-" * 40)
            
            for result in results:
                status = result["status"]
                icon = status_icons.get(status, "[????]")
                counts[status] = counts.get(status, 0) + 1
                
                lines.append(f"  {icon} {result['message']}")
                
                if result.get("details") and self.verbose:
                    lines.append(f"         -> {result['details']}")
            
            lines.append("")
        
        # Summary
        lines.append("=" * 60)
        lines.append("SUMMARY")
        lines.append("=" * 60)
        lines.append(f"  [PASS]: {counts['PASS']}")
        lines.append(f"  [WARN]: {counts['WARN']}")
        lines.append(f"  [FAIL]: {counts['FAIL']}")
        lines.append(f"  [ERR!]: {counts['ERROR']}")
        lines.append("")
        
        # Overall status
        if counts["FAIL"] > 0 or counts["ERROR"] > 0:
            lines.append("STATUS: ISSUES FOUND - Please review and fix before submission")
        elif counts["WARN"] > 0:
            lines.append("STATUS: WARNINGS - Review recommended before submission")
        else:
            lines.append("STATUS: PASSED - Paper appears to meet format requirements")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Check MCM/ICM paper format compliance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python check_format.py paper.pdf
  python check_format.py paper.pdf --verbose
  python check_format.py paper.pdf --output report.txt

Checks performed:
  - Page count (max 25 pages)
  - Team number header (Team # XXXXXXX)
  - Page number headers (Page X of Y)
  - No identifying information (names, school names)
  - Summary/Abstract section present
  - References section present
  - Keywords present

Note: This is an automated check and may not catch all issues.
      Always manually review your paper before submission.
        """
    )
    
    parser.add_argument(
        "pdf_file",
        type=str,
        help="Path to the PDF file to check"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed information for each check"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Save report to file (default: print to console)"
    )
    
    args = parser.parse_args()
    
    # Run checks
    checker = FormatChecker(args.pdf_file, verbose=args.verbose)
    checker.run_all_checks()
    
    # Generate report
    report = checker.generate_report()
    
    # Output
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding="utf-8")
        print(f"Report saved to: {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
