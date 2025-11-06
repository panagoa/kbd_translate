# Kabardian Grammar References

This directory contains excerpts from academic grammar resources for Kabardian language. These materials were copied from the deprecated `zbze_blog` project to serve as local references for translation and morphological analysis.

## Source

**Кабардино-Черкесский язык** (Kabardino-Cherkess Language)
Large academic grammar reference (~5MB, 560 chunks total)

Original location: `/Users/panagoa/PycharmProjects/zbze_blog/data/external/pdf/Kabardino-Cherkesskiy_chunks/`

## Directory Structure

### `verb_morphology/` (Chunks 23-30, Pages 111-150)

The most critical section for understanding Kabardian verb structure:

- **chunk_023** (pages 111-115): Introduction to verb morphology
- **chunk_024** (pages 116-120): Verb structure foundations
- **chunk_025** (pages 121-125): Polipersonalizm (multi-person verbs)
- **chunk_026** (pages 126-130): Verb paradigms (1-person verbs)
- **chunk_027** (pages 131-135): Two-person verb paradigms
- **chunk_028** (pages 136-140): Three-person verb paradigms
- **chunk_029** (pages 141-145): Four-person verb paradigms
- **chunk_030** (pages 146-150): Complex verb forms

**Key Sections:**
- 8.1. Общая характеристика полисинтетизма глагола (Verb polysynthesis)
- 8.5. Категория лица (Person category)
- 8.5.1. Формы проявления полиперсонализма (Polipersonalism forms)
- 8.6. Глагольные парадигмы (Verb paradigms)

### `phonetics/` (Chunks 6-9, Pages 26-45)

Phonetic system and sound patterns:

- **chunk_006** (pages 26-30): Phoneme inventory
- **chunk_007** (pages 31-35): Consonant system
- **chunk_008** (pages 36-40): Vowel system
- **chunk_009** (pages 41-45): Phonological processes

**Key Topics:**
- Consonant phonemes (including ejectives)
- Vowel system (reduced inventory)
- Assimilation rules
- Morphophonological changes

### `nouns/` (Chunks 12-16, Pages 61-83)

Noun morphology and word formation:

- **chunk_012** (pages 56-60): Basic noun characteristics
- **chunk_013** (pages 61-65): Definiteness/indefiniteness category (-р marker)
- **chunk_014** (pages 66-70): Case system (ergative, postpositional, oblique)
- **chunk_015** (pages 71-75): Number category (-хэ, -хэр plurals) and possessiveness
- **chunk_016** (pages 76-80): Conjunction category and compound formation

**Key Sections:**
- 3.1. Основные особенности (Basic features)
- 3.2. Категория определённости (Definiteness)
- 3.3. Категория падежа (Case system)
- 3.4. Категория числа (Number)
- 3.5. Категория притяжательности (Possessiveness)
- 3.7. Словообразование существительных (Noun derivation)

### `verbal_derivations/` (Chunks 44-49, Pages 222-247)

Deverbal formations (participles, gerunds, infinitives):

- **chunk_044** (pages 216-220): Ablaut in verb derivation
- **chunk_045** (pages 221-225): Participle types and formation
- **chunk_046** (pages 226-230): Subject/object participles
- **chunk_047** (pages 231-235): Adverbial and instrumental participles
- **chunk_048** (pages 236-240): Participle inflection and case
- **chunk_049** (pages 241-245): Gerunds (деепричастия) and infinitives

**Key Sections:**
- 9.1. Причастие (Participles: subjective, objective, adverbial, instrumental)
- 9.2. Деепричастие (Gerunds with -у/-уэ and -рэ suffixes)
- 9.3. Инфинитив (Infinitive forms)
- 9.4. Масдар (Masdar/verbal noun)

### `syntax/` (Chunks 56-80, Pages 282-404) ⭐ CRITICAL

Sentence structure and word order - **essential for translation**:

- **chunks_056-057** (pages 276-285): Introduction and phrase structure
- **chunks_058-061** (pages 286-305): Simple sentences and sentence types
- **chunks_062-065** (pages 306-325): Predicate and subject structures
- **chunks_066-073** (pages 326-365): Complements, attributes, circumstances
- **chunks_074-075** (pages 366-375): **WORD ORDER RULES (SOV)** ⭐
- **chunks_076-080** (pages 376-404): Complex sentences and subordination

**Key Sections (Critical for Translation):**
- 3. Простое предложение (Simple sentence structure)
- 3.5. Сказуемое (Predicate types)
- 3.6. Подлежащее (Subject forms)
- 3.8. Дополнение (Complements in different cases)
- 3.9. Определение (Attributes and modifiers)
- **4. Словопорядок в простом предложении (Word order)** ⭐⭐⭐
  - 4.1. Базисный словопорядок (Basic SOV order)
  - 4.2. Изменение базового порядка (Order variations)
  - 4.3. Роль маркеров (Role of case markers)
  - 4.5. Словопорядок в вопросах (Question word order)
- 5. Сложное предложение (Complex sentences)

**Why This Section is Critical:**
This section contains the fundamental rules for SOV word order that are the foundation of the kbd-translator skill. Understanding these rules is essential for producing grammatically correct Kabardian translations.

### Reference Files

- **table_of_content.txt**: Complete table of contents with page numbers (555+ entries)
- **table_of_content_to_index.txt**: Mapping from page numbers to chunk files

## Usage

These references are intended for:

1. **kbd-morphology skill**: Understanding verb structure templates `[PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD]`
2. **kbd-translator skill**: Verifying grammar rules for SOV word order and morphological transformations
3. **Manual consultation**: Detailed examples of polipersonal verb forms (1-5 participants)

## File Format

Each chunk file contains:
- 5 pages of OCR-extracted text from the original grammar PDF
- Cyrillic text with special characters (Ӏ, хь, къ, etc.)
- Section headers, tables, and examples
- Some OCR artifacts may be present

## Notes

- These materials supplement the simplified references in `.claude/skills/kbd-morphology/reference_morphology.md`
- For quick reference, use the skill references first
- Use these detailed academic sections for complex cases or ambiguities
- The complete grammar covers pages 1-555; only key sections are copied here

---

**Copied on:** 2025-11-06
**Source project:** zbze_blog (deprecated)
