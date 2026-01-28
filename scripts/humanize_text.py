#!/usr/bin/env python3
"""
Text Humanizer for MCM/ICM Papers

Detects and suggests replacements for common AI writing patterns,
making academic text sound more natural while maintaining professionalism.

Usage:
    python humanize_text.py --input draft.md --output humanized.md
    python humanize_text.py -i draft.md -o humanized.md --report changes.txt
    python humanize_text.py -i draft.md  # prints to stdout

Detects:
    - Overused transition phrases
    - Overly formal constructions
    - Perfect parallel structures
    - Repetitive sentence patterns
"""

import argparse
import re
import random
from pathlib import Path
from collections import Counter
from typing import List, Tuple, Dict


# =============================================================================
# Pattern Definitions
# =============================================================================

# Phrase replacements: pattern -> list of alternatives
PHRASE_REPLACEMENTS = {
    # Wordy/formal openings
    r"It is important to note that": [
        "Notably,",
        "We note that",
        "An important point is that",
        "",  # Often can be removed entirely
    ],
    r"It is worth noting that": [
        "Notably,",
        "We observe that",
        "Interestingly,",
        "",
    ],
    r"It should be noted that": [
        "Note that",
        "Notably,",
        "We emphasize that",
        "",
    ],
    r"It is crucial to": [
        "We must",
        "Crucially,",
        "Essential here is to",
    ],
    r"It is essential to": [
        "We need to",
        "Essential is",
        "Critically,",
    ],
    
    # Overused transitions
    r"\bFurthermore\b": [
        "Additionally,",
        "Also,",
        "Beyond this,",
        "In addition,",
    ],
    r"\bMoreover\b": [
        "Also,",
        "Additionally,",
        "Further,",
        "What's more,",
    ],
    r"\bAdditionally\b": [
        "Also,",
        "Further,",
        "In addition,",
        "Beyond this,",
    ],
    r"\bConsequently\b": [
        "As a result,",
        "Thus,",
        "Therefore,",
        "This leads to",
    ],
    r"\bNevertheless\b": [
        "However,",
        "Still,",
        "Yet,",
        "Even so,",
    ],
    r"\bNonetheless\b": [
        "However,",
        "Still,",
        "Yet,",
        "Even so,",
    ],
    r"\bSubsequently\b": [
        "Then,",
        "After this,",
        "Next,",
        "Following this,",
    ],
    
    # Overly formal phrases
    r"In order to": [
        "To",
    ],
    r"Due to the fact that": [
        "Because",
        "Since",
        "As",
    ],
    r"In light of": [
        "Given",
        "Considering",
        "Because of",
    ],
    r"With respect to": [
        "Regarding",
        "For",
        "About",
    ],
    r"In the context of": [
        "In",
        "For",
        "Regarding",
    ],
    r"Prior to": [
        "Before",
    ],
    r"Subsequent to": [
        "After",
    ],
    r"In conjunction with": [
        "With",
        "Along with",
    ],
    r"A significant amount of": [
        "Much",
        "Significant",
        "Considerable",
    ],
    r"A large number of": [
        "Many",
        "Numerous",
    ],
    r"The vast majority of": [
        "Most",
        "Nearly all",
    ],
    
    # AI-typical phrases
    r"delve into": [
        "examine",
        "explore",
        "investigate",
        "analyze",
    ],
    r"delve deeper": [
        "examine further",
        "explore more",
        "look more closely",
    ],
    r"it is evident that": [
        "clearly,",
        "evidently,",
        "",
    ],
    r"it becomes apparent": [
        "we see",
        "this shows",
        "evidently",
    ],
    r"plays a crucial role": [
        "is important",
        "is key",
        "matters significantly",
    ],
    r"a myriad of": [
        "many",
        "various",
        "numerous",
    ],
    r"in today's world": [
        "currently",
        "now",
        "today",
    ],
    r"at the end of the day": [
        "ultimately",
        "finally",
        "in the end",
    ],
    r"a testament to": [
        "evidence of",
        "proof of",
        "demonstrates",
    ],
    r"taking into account": [
        "considering",
        "given",
        "accounting for",
    ],
}

# Check for repeated words/patterns
REPETITION_WINDOW = 100  # characters to look back for repetition


class TextHumanizer:
    """Analyzes and humanizes text by detecting AI writing patterns."""
    
    def __init__(self, text: str):
        self.original_text = text
        self.text = text
        self.changes: List[Dict] = []
        self.warnings: List[str] = []
        self.stats = Counter()
    
    def analyze_phrase_patterns(self) -> None:
        """Find and record overused phrases."""
        for pattern, alternatives in PHRASE_REPLACEMENTS.items():
            matches = list(re.finditer(pattern, self.text, re.IGNORECASE))
            if matches:
                self.stats[pattern] += len(matches)
                for match in matches:
                    self.changes.append({
                        "type": "phrase",
                        "original": match.group(),
                        "position": match.start(),
                        "alternatives": alternatives,
                        "applied": False
                    })
    
    def analyze_sentence_starters(self) -> None:
        """Check for repetitive sentence starters."""
        sentences = re.split(r'(?<=[.!?])\s+', self.text)
        starter_counts = Counter()
        
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 5:
                continue
            
            # Get first word
            first_word = sentence.split()[0] if sentence.split() else ""
            starter_counts[first_word] += 1
        
        # Warn about overused starters
        total_sentences = len([s for s in sentences if len(s.strip()) > 5])
        for starter, count in starter_counts.most_common(5):
            if count > 3 and count / max(total_sentences, 1) > 0.15:
                self.warnings.append(
                    f"Repetitive starter: '{starter}' begins {count}/{total_sentences} sentences ({count/total_sentences*100:.0f}%)"
                )
    
    def analyze_word_repetition(self) -> None:
        """Check for repeated significant words within proximity."""
        words = re.findall(r'\b[a-zA-Z]{5,}\b', self.text.lower())
        word_positions = {}
        
        for i, word in enumerate(words):
            if word in word_positions:
                # Check if too close
                if i - word_positions[word] < 15:  # Within 15 words
                    self.warnings.append(
                        f"Word repetition: '{word}' appears twice within ~15 words"
                    )
            word_positions[word] = i
    
    def analyze_transition_density(self) -> None:
        """Check if transitions are overused."""
        transition_words = [
            "however", "therefore", "thus", "hence", "furthermore",
            "moreover", "additionally", "consequently", "nevertheless"
        ]
        
        words = self.text.lower().split()
        transitions_found = [w for w in words if w.rstrip(",.:;") in transition_words]
        
        density = len(transitions_found) / max(len(words), 1) * 100
        if density > 2:
            self.warnings.append(
                f"High transition word density: {len(transitions_found)} transitions in {len(words)} words ({density:.1f}%)"
            )
    
    def apply_replacements(self, randomize: bool = True) -> str:
        """Apply phrase replacements to the text."""
        result = self.text
        offset = 0
        
        # Sort changes by position
        phrase_changes = sorted(
            [c for c in self.changes if c["type"] == "phrase"],
            key=lambda x: x["position"]
        )
        
        for change in phrase_changes:
            if not change["alternatives"]:
                continue
            
            # Choose replacement
            if randomize:
                replacement = random.choice(change["alternatives"])
            else:
                replacement = change["alternatives"][0]
            
            # Apply replacement
            pos = change["position"] + offset
            original = change["original"]
            
            # Find and replace
            before = result[:pos]
            after = result[pos + len(original):]
            
            # Handle case matching
            if original[0].isupper() and replacement:
                replacement = replacement[0].upper() + replacement[1:]
            
            result = before + replacement + after
            offset += len(replacement) - len(original)
            change["applied"] = True
            change["replacement"] = replacement
        
        return result
    
    def run_analysis(self) -> None:
        """Run all analysis methods."""
        self.analyze_phrase_patterns()
        self.analyze_sentence_starters()
        self.analyze_word_repetition()
        self.analyze_transition_density()
    
    def get_humanized_text(self, randomize: bool = True) -> str:
        """Get the humanized version of the text."""
        return self.apply_replacements(randomize=randomize)
    
    def generate_report(self) -> str:
        """Generate a detailed change report."""
        lines = []
        lines.append("=" * 60)
        lines.append("TEXT HUMANIZATION REPORT")
        lines.append("=" * 60)
        lines.append("")
        
        # Statistics
        total_chars = len(self.original_text)
        total_words = len(self.original_text.split())
        
        lines.append(f"Document Statistics:")
        lines.append(f"  - Characters: {total_chars:,}")
        lines.append(f"  - Words: {total_words:,}")
        lines.append("")
        
        # Phrase patterns found
        lines.append("Phrase Patterns Found:")
        lines.append("-" * 40)
        
        if self.stats:
            for pattern, count in sorted(self.stats.items(), key=lambda x: -x[1]):
                # Clean up pattern for display
                display_pattern = pattern.replace(r"\b", "").replace("^", "")
                lines.append(f"  [{count}x] {display_pattern}")
        else:
            lines.append("  No common AI patterns detected.")
        lines.append("")
        
        # Warnings
        lines.append("Style Warnings:")
        lines.append("-" * 40)
        
        if self.warnings:
            for warning in self.warnings:
                lines.append(f"  [!] {warning}")
        else:
            lines.append("  No style warnings.")
        lines.append("")
        
        # Applied changes
        applied_changes = [c for c in self.changes if c.get("applied")]
        if applied_changes:
            lines.append("Applied Changes:")
            lines.append("-" * 40)
            for change in applied_changes[:20]:  # Limit to first 20
                orig = change["original"][:30]
                repl = change.get("replacement", "")[:30]
                if repl:
                    lines.append(f'  "{orig}" -> "{repl}"')
                else:
                    lines.append(f'  "{orig}" -> (removed)')
            
            if len(applied_changes) > 20:
                lines.append(f"  ... and {len(applied_changes) - 20} more changes")
        lines.append("")
        
        # Summary
        lines.append("=" * 60)
        lines.append("SUMMARY")
        lines.append("=" * 60)
        lines.append(f"  Patterns found: {sum(self.stats.values())}")
        lines.append(f"  Changes applied: {len(applied_changes)}")
        lines.append(f"  Warnings: {len(self.warnings)}")
        lines.append("")
        
        # Recommendations
        lines.append("Recommendations:")
        lines.append("-" * 40)
        
        if len(self.warnings) > 0:
            lines.append("  1. Review style warnings and consider manual adjustments")
        if sum(self.stats.values()) > 10:
            lines.append("  2. High number of AI patterns detected - review carefully")
        
        lines.append("  3. Read the output aloud to check for natural flow")
        lines.append("  4. Have a teammate review for consistency")
        lines.append("  5. Ensure technical accuracy wasn't lost in changes")
        lines.append("")
        
        return "\n".join(lines)


# =============================================================================
# CLI Functions
# =============================================================================

def humanize_file(
    input_path: Path,
    output_path: Path = None,
    report_path: Path = None,
    randomize: bool = True
) -> Tuple[str, str]:
    """Process a file and return humanized text and report."""
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Read input
    text = input_path.read_text(encoding="utf-8")
    
    # Process
    humanizer = TextHumanizer(text)
    humanizer.run_analysis()
    
    humanized_text = humanizer.get_humanized_text(randomize=randomize)
    report = humanizer.generate_report()
    
    # Write output
    if output_path:
        output_path.write_text(humanized_text, encoding="utf-8")
    
    if report_path:
        report_path.write_text(report, encoding="utf-8")
    
    return humanized_text, report


def main():
    parser = argparse.ArgumentParser(
        description="Humanize text by reducing AI writing patterns",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python humanize_text.py --input draft.md --output humanized.md
  python humanize_text.py -i draft.md -o final.md --report changes.txt
  python humanize_text.py -i draft.md  # prints to stdout
  python humanize_text.py -i draft.md --analyze-only  # just show report

What it detects:
  - Overused phrases: "It is important to note that", "Furthermore", etc.
  - Wordy constructions: "In order to" -> "To"
  - AI-typical phrases: "delve into", "plays a crucial role"
  - Repetitive sentence starters
  - High transition word density

Note: This tool makes suggestions but cannot guarantee the output sounds
natural. Always review changes for technical accuracy and readability.
        """
    )
    
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Input file path (markdown, txt, or tex)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output file path (default: print to stdout)"
    )
    
    parser.add_argument(
        "-r", "--report",
        type=str,
        default=None,
        help="Save change report to file"
    )
    
    parser.add_argument(
        "--analyze-only",
        action="store_true",
        help="Only analyze and show report, don't modify text"
    )
    
    parser.add_argument(
        "--no-randomize",
        action="store_true",
        help="Always use first alternative instead of random"
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None
    report_path = Path(args.report) if args.report else None
    
    try:
        if args.analyze_only:
            # Just analyze
            text = input_path.read_text(encoding="utf-8")
            humanizer = TextHumanizer(text)
            humanizer.run_analysis()
            print(humanizer.generate_report())
        else:
            # Full processing
            humanized_text, report = humanize_file(
                input_path=input_path,
                output_path=output_path,
                report_path=report_path,
                randomize=not args.no_randomize
            )
            
            # Print report
            print(report)
            
            if output_path:
                print(f"\nHumanized text saved to: {output_path}")
            else:
                print("\n" + "=" * 60)
                print("HUMANIZED TEXT:")
                print("=" * 60)
                print(humanized_text)
            
            if report_path:
                print(f"Report saved to: {report_path}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error processing file: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
