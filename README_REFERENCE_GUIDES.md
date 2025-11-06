# Reference Guides for kbd_translate

Two comprehensive reference documents have been created to help Claude Skills understand the grammar resources and data files in this project.

## Files Created

### 1. GRAMMAR_REFERENCE_GUIDE.md (47KB, 1318 lines)
**Comprehensive, detailed reference covering ALL grammar and data resources**

Contains:
- Executive summary of resources (2.74MB grammar + 48.4MB data)
- Detailed breakdown of all 11 grammar sections (79 chunks)
- Complete mapping of grammar sections → specific chunks
- Practical grep search patterns for finding topics
- Topic index (find grammar for any topic you need)
- Data files reference (corpus, glossaries, sentence examples)
- Specific recommendations for each Claude Skill

Use when:
- You need detailed information about a specific grammar section
- You want to find which chunks cover a particular topic
- You need grep patterns for searching grammar files
- You're implementing a new skill and need comprehensive reference

**Structure:**
```
Part 1: Grammar Directory Structure (overview table)
Part 2: Detailed Section Breakdown (11 sections analyzed)
  - Each section: Purpose, chunks, pages, use cases, grep patterns
Part 3: Data Files Reference (corpus, glossaries)
Part 4: Topic Index (find grammar for specific topics)
Part 5: Practical Search Patterns & Examples
Part 6: Skill-Specific Recommendations
Part 7: Data Files Summary
```

### 2. REFERENCE_GUIDE_SUMMARY.txt (11KB, 271 lines)
**Quick reference for fast lookup and prioritization**

Contains:
- Quick overview of all resources
- Grammar structure in tree format
- Topic index with chunk numbers
- Priority resources for each skill
- Grep search examples
- Key takeaways and usage notes

Use when:
- You need quick answers without reading detailed text
- You want to prioritize what to read first
- You need fast chunk number lookups
- You want example grep patterns

**Structure:**
```
Overview (sizes, counts)
Grammar Structure (tree view with priorities)
Topic Index (quick lookup)
Data Files (quick reference)
Priority Resources (by skill)
Search Patterns (examples)
Key Takeaways (5 main points)
```

## Quick Start

### For kbd-translator Skill (HIGHEST PRIORITY)
Read in order:
1. `REFERENCE_GUIDE_SUMMARY.txt` sections:
   - Grammar Structure (especially ADVANCED VERBS and SYNTAX)
   - Priority Resources for kbd-translator
   
2. `GRAMMAR_REFERENCE_GUIDE.md` sections:
   - Part 2.7 (Advanced Verbs) - TAM, mood, negation, derivation
   - Part 2.11 (Syntax) - SOV word order (CRITICAL)
   - Part 2.10 (Function Words) - postpositions, conjunctions

3. Then consult:
   - Part 3 (Data Files) for corpus search strategies
   - Part 4 (Topic Index) for specific grammar lookups
   - Part 5 (Search Patterns) for grep examples

### For kbd-morphology Skill (SECONDARY PRIORITY)
Read in order:
1. Part 2.6 (Verb Morphology) - multi-person paradigms
2. Part 2.7 (Advanced Verbs) - TAM and mood suffixes
3. Part 2.8 (Verbal Derivations) - participles and gerunds

### For kbd-glossary Skill (LOWEST PRIORITY)
Use:
1. Part 3.2 (Glossaries) for file structure and usage
2. Part 2.10 (Function Words) for postposition lemmas
3. Part 2.9 (Adverbs) for adverb roots

## Key Numbers

**Grammar Resources:**
- 79 total chunks across 11 sections
- 2.74MB of academic grammar text
- Pages 26-404 of comprehensive grammar
- Covers phonetics → morphology → syntax

**Data Resources:**
- 292,000 translation pairs (45MB corpus)
- 15,989 Russian-Kabardian dictionary entries (3.4MB)
- 98,412 Kabardian explanatory dictionary entries (15MB)
- 100,000+ Kabardian sentence examples (7.3MB)

**Critical Sections:**
- Advanced Verbs (chunks 031-044): TAM, mood, negation
- Function Words (chunks 052-055): Postpositions, conjunctions
- Syntax (chunks 056-080): SOV word order

## File Locations

All references map to files in:
- `/references/grammar/` - All grammar chunks organized by topic
- `/data/` - Data files (corpus, glossaries, sentences)

## How to Use These Guides

1. **Quick lookup:** Use REFERENCE_GUIDE_SUMMARY.txt
2. **Detailed research:** Use GRAMMAR_REFERENCE_GUIDE.md
3. **Topic search:** Use Part 4 (Topic Index) in GRAMMAR_REFERENCE_GUIDE.md
4. **Find chunks:** Use Part 4 or grep patterns in Part 5
5. **Data file search:** See Part 3 for grep examples

## Important Notes

### For Large Files
- sents_292k.csv (45MB): Always use `grep -m N` with limit
- Ady-Ady_AP.csv (15MB): Always use `grep -m 1-2` with limit
- Never use Read tool to open entire CSV files

### Grammar Files
- All chunks are readable text (UTF-8 encoding)
- OCR may have some artifacts but content is accurate
- Tables show inflectional paradigms
- Examples are from Kabardian literature

### Search Patterns
- Use Cyrillic characters for searches
- Case-insensitive searches: `grep -i`
- Exact matches: `grep -F`
- Regex patterns: `grep -E`

## Examples

### Find information about TAM suffixes
```bash
# Quick: Check REFERENCE_GUIDE_SUMMARY.txt "TAM System" section
# Detailed: Read GRAMMAR_REFERENCE_GUIDE.md Part 2.7
# Chunks: 031-033, 161-165 (pages within)
```

### Find postposition rules
```bash
# Quick: Check REFERENCE_GUIDE_SUMMARY.txt "Function Words" section
# Detailed: Read GRAMMAR_REFERENCE_GUIDE.md Part 2.10
# Chunks: 053-054
# Grep: grep -E "гъун|мыш|хьэ|фэ" function_words/chunk_053*.txt
```

### Find verb paradigm examples
```bash
# Quick: REFERENCE_GUIDE_SUMMARY.txt "Verb Morphology" section
# Detailed: Read GRAMMAR_REFERENCE_GUIDE.md Part 2.6-2.7
# Chunks: 023-030 (paradigms), 031-044 (complex forms)
```

### Search translation corpus
```bash
# Never load entire file! Use grep with limit:
grep -i "word" sents_292k.csv | head -10

# Examples in GRAMMAR_REFERENCE_GUIDE.md Part 3.1
```

---

Created: 2025-11-06
Location: /Users/panagoa/PycharmProjects/kbd_translate/
Size: 58KB total (47KB guide + 11KB summary)

For questions about grammar, first check these guides. They contain comprehensive mapping of all resources and practical examples.
