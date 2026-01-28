# Demo: humanize_text.py Usage Guide

The `humanize_text.py` script detects and replaces common AI writing patterns to make your text sound more natural.

## Why Use This?

AI-generated text often has telltale patterns:
- Overused transitions ("Furthermore", "Moreover")
- Wordy phrases ("It is important to note that")
- Perfect parallel structure
- Formal constructions ("In order to")

This tool identifies these patterns and suggests alternatives.

## Basic Usage

### Analyze Only (No Changes)

```bash
python scripts/humanize_text.py --input draft.md --analyze-only
```

This shows a report without modifying the text.

### Full Processing

```bash
python scripts/humanize_text.py --input draft.md --output humanized.md
```

This creates a new file with replacements applied.

## Command Line Options

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--input` | `-i` | Yes | Input file path |
| `--output` | `-o` | No | Output file path |
| `--report` | `-r` | No | Save report to file |
| `--analyze-only` | | No | Only analyze, don't modify |
| `--no-randomize` | | No | Use first alternative always |

## Example Session

### Input Text (draft.md)

```markdown
It is important to note that our model achieves high accuracy. 
Furthermore, we observe significant improvement in performance.
Moreover, the results demonstrate the effectiveness of our approach.
In order to validate the model, we conducted extensive experiments.
Additionally, we performed sensitivity analysis on key parameters.
```

### Command

```bash
python scripts/humanize_text.py -i draft.md -o humanized.md
```

### Output Text (humanized.md)

```markdown
Notably, our model achieves high accuracy.
Also, we observe significant improvement in performance.
Further, the results demonstrate the effectiveness of our approach.
To validate the model, we conducted extensive experiments.
Beyond this, we performed sensitivity analysis on key parameters.
```

### Report Output

```
============================================================
TEXT HUMANIZATION REPORT
============================================================

Document Statistics:
  - Characters: 412
  - Words: 58

Phrase Patterns Found:
----------------------------------------
  [1x] It is important to note that
  [1x] Furthermore
  [1x] Moreover
  [1x] In order to
  [1x] Additionally

Style Warnings:
----------------------------------------
  No style warnings.

Applied Changes:
----------------------------------------
  "It is important to note that" -> "Notably,"
  "Furthermore" -> "Also,"
  "Moreover" -> "Further,"
  "In order to" -> "To"
  "Additionally" -> "Beyond this,"

============================================================
SUMMARY
============================================================
  Patterns found: 5
  Changes applied: 5
  Warnings: 0

Recommendations:
----------------------------------------
  3. Read the output aloud to check for natural flow
  4. Have a teammate review for consistency
  5. Ensure technical accuracy wasn't lost in changes
```

## Patterns Detected

### Wordy Phrases (Replaced)

| AI Pattern | Replacement Options |
|------------|---------------------|
| "It is important to note that" | "Notably,", "We note that", (remove) |
| "Due to the fact that" | "Because", "Since", "As" |
| "In order to" | "To" |
| "A significant amount of" | "Much", "Significant" |
| "The vast majority of" | "Most", "Nearly all" |

### Overused Transitions (Varied)

| AI Pattern | Alternatives |
|------------|--------------|
| "Furthermore" | "Additionally,", "Also,", "Beyond this," |
| "Moreover" | "Also,", "Further,", "What's more," |
| "Consequently" | "As a result,", "Thus,", "Therefore," |
| "Nevertheless" | "However,", "Still,", "Yet," |

### AI-Typical Phrases (Replaced)

| AI Pattern | Alternatives |
|------------|--------------|
| "delve into" | "examine", "explore", "analyze" |
| "plays a crucial role" | "is important", "is key" |
| "a myriad of" | "many", "various", "numerous" |

## Style Warnings

The tool also warns about:

1. **Repetitive sentence starters**: Same word begins >15% of sentences
2. **Word repetition**: Same significant word appears twice within 15 words
3. **High transition density**: >2% of words are transition words

## Tips for Best Results

1. **Run analyze-only first** to see what will change
2. **Review changes manually** - automatic replacements may not always fit context
3. **Use with technical sections** - math and model descriptions need less humanization
4. **Keep domain terminology** - don't replace technical terms

## Sample Input File

A sample input file is provided at:
```
examples/02_script_usage/sample_input/sample_draft.md
```

Try running:
```bash
python scripts/humanize_text.py -i examples/02_script_usage/sample_input/sample_draft.md --analyze-only
```

---
*MCM-Analysis v1.2.2*
