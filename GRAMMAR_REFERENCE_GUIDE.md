# Comprehensive Reference Guide for kbd_translate Grammar & Data

## Executive Summary

This guide maps the complete grammar resources and data files in the `kbd_translate` project, designed to support three Claude Skills: `kbd-translator`, `kbd-morphology`, and `kbd-glossary`. The project contains ~2.74MB of academic grammar materials (79 files) and ~48.4MB of working data.

**Total Structure:**
- 11 grammar sections with 79 chunks (pages 26-404 from academic grammar)
- 292k translation pairs (45MB corpus)
- 2 large glossaries (18.4MB total)
- 100k+ sentence examples

---

## Part 1: Grammar References Directory Structure

### Overview of `/references/grammar/`

| Section | Chunks | Pages | Size | Key Focus |
|---------|--------|-------|------|-----------|
| **phonetics/** | 4 | 26-45 | 136K | Sound system, consonants, vowels, phonological processes |
| **morphology_intro/** | 2 | 46-56 | 72K | Theoretical foundations, stem types, morphological structure |
| **nouns/** | 5 | 56-80 | 180K | Definiteness, cases, number, possessiveness, noun derivation |
| **adjectives/** | 4 | 81-100 | 128K | Comparative/superlative forms, qualitative vs relative |
| **numerals/** | 3 | 101-115 | 96K | Vigesimal system, cardinal/ordinal, distributive numerals |
| **verb_morphology/** | 8 | 111-150 | 244K | Polypersonalism, person marking, verb paradigms (1-4 person) |
| **advanced_verbs/** | 14 | 151-222 | 492K | TAM markers, moods, negation, derivation, preverbs **CRITICAL** |
| **verbal_derivations/** | 6 | 223-247 | 220K | Participles, gerunds, infinitives, verbal nouns |
| **adverbs/** | 2 | 246-256 | 72K | Adverb formation, temporal/spatial/manner adverbs |
| **function_words/** | 4 | 256-282 | 152K | Postpositions, conjunctions, particles **CRITICAL** |
| **syntax/** | 25 | 282-404 | 932K | Simple & complex sentences, word order (SOV) **CRITICAL** |

**Total:** 79 files, ~2.74MB, covering comprehensive Kabardian morphosyntax

---

## Part 2: Detailed Section Breakdown

### 2.1 PHONETICS (chunks_006-009, pages 26-45, 136KB)

**Purpose:** Foundation for understanding sound patterns, morphophonological processes, and character handling.

| Chunk | Pages | Topics | Use Cases |
|-------|-------|--------|-----------|
| chunk_006 | 26-30 | Phoneme inventory, consonant classification, ejectives | Recognizing special characters (Ӏ, хь, къ, etc.) |
| chunk_007 | 31-35 | Consonant system details, palatal consonants, affricates | Understanding consonant assimilation in verb forms |
| chunk_008 | 36-40 | Vowel system, reduced vowels, stress patterns | Handling vowel alternations in morphology |
| chunk_009 | 41-45 | Morphophonological processes, borrowing patterns, assimilation | Understanding loanword adaptation, ablaut patterns |

**Key Grep Patterns:**
```bash
# Find consonant system details
grep -i "согласн\|consonant" chunks_006-009

# Find ejective marking (Ӏ)
grep "Ӏ\|глоттальн\|eject" chunks_006-009

# Find vowel alternation patterns
grep "чередова\|альтерна" chunks_008-009
```

**Critical for Skills:**
- `kbd-translator`: Character normalization (ӏ→I, 1→I)
- `kbd-morphology`: Ablaut patterns (ы:э alternation)

---

### 2.2 MORPHOLOGY INTRO (chunks_010-011, pages 46-56, 72KB)

**Purpose:** Theoretical framework for all morphological structures.

| Chunk | Pages | Topics | Content |
|-------|-------|--------|---------|
| chunk_010 | 46-50 | Morphology chapter intro, stem structure foundations | "Общая характеристика морфологической системы" |
| chunk_011 | 51-55 | Stem types classification, nominal vs verbal stems | Memberability (членимые/нечленимые), productivity (производные/непроизводные) |

**Key Classifications:**
```
Stem Types:
├─ Segmentable (членимые) vs Non-segmentable (нечленимые)
├─ Derived (производные) vs Underived (непроизводные)
├─ Continuous vs Discontinuous (прерывистые)
├─ Neutral vs Non-neutral
└─ Free vs Bound stems
```

**Critical for Skills:**
- `kbd-morphology`: Understanding [PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD] template structure
- `kbd-translator`: Stem identification before applying affixes

---

### 2.3 NOUNS (chunks_012-016, pages 56-80, 180KB)

**Purpose:** Complete noun morphology including case, number, possessiveness.

| Chunk | Pages | Topics | Key Features |
|-------|-------|--------|--------------|
| chunk_012 | 56-60 | Basic noun characteristics, types of nouns | Morphological properties |
| chunk_013 | 61-65 | **Definiteness category** (-р suffix) | "определённость/неопределённость" marking |
| chunk_014 | 66-70 | **Case system (CRITICAL for translation)** | Ergative, postpositional, oblique cases |
| chunk_015 | 71-75 | Number category (-хэ, -хэр), possessiveness | Plurality marking and possession |
| chunk_016 | 76-80 | Conjunction category, compound formation | Word formation, derivation patterns |

**Case System (from chunk_014):**
```
Cases in Kabardian:
- Absolutive (nominative) - unmarked
- Ergative (абсолютив-эргатив) 
- Postpositional (послеложный)
- Oblique cases with various postpositions
```

**Key Grep Patterns:**
```bash
# Find case system details
grep -i "падеж\|case" chunks_012-016

# Find definiteness (-р) marker
grep -E "определён|\-р\b" chunks_013

# Find noun derivation suffixes (-гъэ, -агъ, -кIэ)
grep -E "\-гъэ|\-агъ|\-кIэ" chunks_012
```

**Critical for Skills:**
- `kbd-translator`: Case marking determines word function and postposition selection
- `kbd-morphology`: Noun stem morphology, suffix identification

---

### 2.4 ADJECTIVES (chunks_017-020, pages 81-100, 128KB)

**Purpose:** Adjective morphology including comparison and evaluation forms.

| Chunk | Pages | Topics | Content |
|-------|-------|--------|---------|
| chunk_017 | 81-85 | Adjectives as part of speech, types | Qualitative vs relative adjectives |
| chunk_018 | 86-90 | Qualitative adjectives, comparative degree | Formation of -рэ comparatives |
| chunk_019 | 91-95 | Superlative degree, evaluative forms | Augmentative (-шхуэ), diminutive (-кIэ) |
| chunk_020 | 96-100 | Relative adjectives, declension patterns | Adjective agreement with nouns |

**Degree Comparison:**
```
дахэ "beautiful"
├─ дахэрэ "more beautiful" (comparative with -рэ)
├─ дахэ фI "most beautiful" (superlative)
└─ дахэу "beautifully" (adverbial form)
```

**Key Grep Patterns:**
```bash
# Find comparative formation (-рэ)
grep -E "\-рэ\b|сравнител" chunks_018

# Find superlative patterns
grep -i "превосход" chunks_019

# Find evaluative suffixes (-шхуэ for augmentative)
grep -E "\-шхуэ|\-кIэ" chunks_019
```

**Critical for Skills:**
- `kbd-translator`: Translating Russian comparative/superlative forms to Kabardian
- `kbd-morphology`: Adjective suffix identification

---

### 2.5 NUMERALS (chunks_020-022, pages 101-115, 96KB)

**Purpose:** Understanding Kabardian vigesimal number system and numeral formation.

| Chunk | Pages | Topics | System |
|-------|-------|--------|--------|
| chunk_020 | 101-105 | Vigesimal counting system (base-20) | зы, тIу, щ, плI, тIощI "1,2,3,4,20" |
| chunk_021 | 106-110 | Cardinal numeral formation | Quantitative numbers (количественные) |
| chunk_022 | 111-115 | Ordinal, distributive, collective numerals | 11-20 compounds, complex number formation |

**Vigesimal System Structure:**
```
1-20:        зы(1), тIу(2), щ(3), плI(4), тху(5)...пщI(10)...тIощI(20)
21-40:       пщIы+зы, пщIы+тIу... (20+1, 20+2...)
100+:        щ-и-тI "two hundred" (2×100), плIы-щI "40" (2×20)

Morphophonological processes:
- Vowel truncation in compounds (second component)
- Connection element -ры-
- Alternation ы:э in numeral families
```

**Key Grep Patterns:**
```bash
# Find base numerals
grep -E "зы|тIу|щы|плI" chunks_020-022

# Find compound numeral rules
grep -i "сложн\|compound" chunks_021-022

# Find distributive numerals (по одному, по два)
grep -E "разделител" chunks_022
```

**Critical for Skills:**
- `kbd-translator`: Recognizing and translating numerals, understanding compounds
- `kbd-morphology`: Numeral morpheme identification and combining patterns

---

### 2.6 VERB MORPHOLOGY (chunks_023-030, pages 111-150, 244KB)

**Purpose:** Foundation of verb structure, polypersonalism, person marking, paradigms.

| Chunk | Pages | Topics | Key Paradigms |
|-------|-------|--------|----------------|
| chunk_023 | 111-115 | Introduction to verb morphology, dynamic vs static verbs | "Полисинтетизм глагола" |
| chunk_024 | 116-120 | Verb structure foundations, present tense paradigms | Basic 1-person verb forms |
| chunk_025 | 121-125 | Polypersonalism (multi-person verbs) | How verbs mark multiple participants |
| chunk_026 | 126-130 | 1-person verb paradigms | Simple transitive/intransitive verbs |
| chunk_027 | 131-135 | 2-person verb paradigms | Two-participant verbs with complements |
| chunk_028 | 136-140 | 3-person verb paradigms | Three-participant verbs (agent, theme, recipient) |
| chunk_029 | 141-145 | 4-person verb paradigms | Four-participant complex verbs |
| chunk_030 | 146-150 | Verb homonymy, complex forms | Form disambiguation through context |

**Multi-Person Verb Structure:**
```
Basic Template: [PERSON]-[OBJECT]-[VERB_STEM]

1-person:     с-кIуэ        "I go"
2-person:     с-абы-р-узо   "I (agent) him (recipient) give it (theme)"
3-person:     къы-зэ-дэ-уо   "you (agent) me (recipient) him (theme) give"
4-person:     (complex combinations with multiple arguments)

Prefix positions encode:
- S (subject) first position
- A (agent/indirect object) second
- D (direct object) third
```

**Key Grep Patterns:**
```bash
# Find polypersonalism explanation
grep -i "полипер\|multi-person" chunks_023-025

# Find verb paradigm tables
grep -E "Ед\.ч\.|Мн\.ч\.|singular|plural" chunks_026-029

# Find prefix positions for arguments
grep -E "прямой объект|косвен\|prefix" chunks_024-027
```

**Critical for Skills:**
- `kbd-translator`: Essential for handling multi-argument verbs in translation
- `kbd-morphology`: Core of [PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD] template

---

### 2.7 ADVANCED VERBS (chunks_031-044, pages 151-222, 492KB) ⭐ CRITICAL

**Purpose:** TAM markers, moods, negation, derivational categories, directional preverbs - most complex verb morphology.

| Chunk Range | Pages | Topics | Critical Content |
|-------------|-------|--------|------------------|
| 031-033 | 151-165 | **Tense (Category of Time)** | Present, future, perfect, imperfect, pluperfect, aorist suffixes |
| 033-034 | 161-170 | **Mood (Category of Mood)** | Indicative, conditional, conjunctive, optative, imperative |
| 034-036 | 171-180 | **Negation** (-къым suffix) | Negative verb forms, imperative negation |
| 036 | 181-185 | **Question Forms** | Interrogative particles, question word order |
| 037-038 | 186-195 | **Verb Derivation I** | Prefixation, suffixation, morpheme ordering principles |
| 038-039 | 191-199 | **Derivational Categories I** | Factitive (гъэ-), causative patterns, conjunction |
| 039-040 | 200-205 | **Derivational Categories II** | Comitative (дэ-), reciprocal (зэ-), version (хуэ-, фIэ-) |
| 040-042 | 206-215 | **Directional Preverbs** | къэ-, къы-, щы-, дэ-, те-, щIэ- locative meanings |
| 042-044 | 216-222 | **Ablaut in Derivation** | Vowel alternations (ы:э) in derived forms |

**CRITICAL TAM System (from chunks_031-033):**

Present Tenses:
```
- Present 1 (immediateness): с-о-кIуэ "I go" → active continuous
- Present 2 (habituality): с-о-кIуэ-р (variant with -р)
- Present 3 (stative): с-ыщы-т "I stand"
```

Perfect/Aorist System:
```
- Perfect I: с-ы-кIуа-щ "I went (recently)" ← perfective aspect marker -щ
- Perfect II: с-ы-кIуа-т "I had gone (then)" ← Perfect I + -т marker (limited time)
- Imperfect: с-ы-кIуэ-т "I was going" ← Imperfect stem + -т
- Aorist: с-ы-кIуэ-гъа "I (generally) go" ← gnomic aspect
```

Future:
```
- Future I: с-ы-кIуэ-ну "I will go"
- Future II: с-ы-кIуэ-г(ъ)ащ "I will go (by then)"
```

**CRITICAL Mood System (from chunks_033-034):**

```
Indicative:     с-ы-кIуащ      "I went" (factual)
Conditional:    с-ы-кIуэ-мэ    "if I go" (hypothetical condition)
Conjunctive:    с-ы-кIуэ-нт    "I would go" (subjunctive)
Optative:       с-ы-кIуа-рэт   "Let me go" (wish/desire)
Imperative:     кIуэ           "Go!" (command)
```

**CRITICAL Negation (from chunks_034-036):**

```
Basic negation with -къым:
- Negative present: с-ы-кIуэ-къым       "I don't go"
- Negative past:    с-ы-кIуащ-къым      "I didn't go"
- Negative future:  с-ы-кIуэ-ну-къым    "I won't go"

Special negative imperative:
- Positive: кIуэ "Go!"
- Negative: кIуэ-къым "Don't go!"
```

**Derivational Categories (chunks_038-040):**

```
CAUSATIVE (гъэ-): Convert intransitive to transitive
- лэжьэн "work" → гъэлэжьэ-н "make work"
- кIуэн "go" → гъэкIуэ-н "send"

RECIPROCAL (зэ-): Mutual action
- уащын "hit" → зэуащ-ын "hit each other"

COMITATIVE (дэ-): With/together action
- мышлэн "go" → дэмышлэ-н "go along"
- хъун "be" → дэхъ-ун "be together"

VERSION (хуэ-/фIэ-): Directional nuance
- кIуэн "go" → хуэкIуэ-н "go in certain direction"

POTENTIAL (хуэ-): Capability
- тхын "write" → хуэтхы-н "be able to write"
```

**Directional Preverbs (chunks_040-042):**

```
DIRECTIONAL (movement toward/away):
- къэ-: direction away from speaker (къэкIуэ "go away")
- къы-: direction toward something (къыкIуэ "go to")
- щы-: direction upward/inward (щыкIуэ "go up")
- дэ-: direction downward (дэкIуэ "go down")
- те-: direction along surface (теплъэ "slide")

LOCATIVE (location/position):
- Combination with -хь suffix for spatial location
- Complex preverbs like щI-э-, фIэ- for specific regions
```

**Key Grep Patterns for Advanced Verbs:**

```bash
# Find TAM suffix inventory
grep -E "суффикс\s+\-|временной\s+суффикс" chunks_031-033

# Find mood distinctions
grep -i "наклонени\|mood" chunks_033-035

# Find negation rules
grep -E "\-къым|\-ощ" chunks_034-036

# Find causative formation (гъэ-)
grep -E "гъэ\-|гъэ\s|фактити" chunks_038-039

# Find preverb meanings
grep -E "щы\-|къэ\-|къы\-|дэ\-|те\-" chunks_040-042

# Find ablaut patterns (ы:э)
grep -i "чередова\|ablaut" chunks_044
```

**Critical for Skills:**
- `kbd-translator`: **ESSENTIAL** - Without understanding TAM system, cannot produce correct verb forms
  - Translating Russian past/present/future requires matching Kabardian TAM markers
  - Mood distinctions affect meaning (conditional vs factual)
  - Negation placement is critical for SVO→SOV transformation
  
- `kbd-morphology`: **ESSENTIAL** - Core of [PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD] template
  - [TAM] position: -щ (perfect I), -рт (perfect II), -ну (future), -гъа (aorist), etc.
  - [SUBORD] position: -н (conditional), -рэ (conjunctive), -рэт (optative)

---

### 2.8 VERBAL DERIVATIONS (chunks_044-049, pages 216-247, 220KB)

**Purpose:** Deverbal formations (participles, gerunds, infinitives).

| Chunk | Pages | Topics | Forms |
|-------|-------|--------|-------|
| chunk_044 | 216-220 | Ablaut in verb derivation | ы:э patterns in -кI, -хь derivatives |
| chunk_045 | 221-225 | Participle types and basic formation | Subject vs object participles |
| chunk_046 | 226-230 | Subject/object participle details | "причастие" (pričastie) structures |
| chunk_047 | 231-235 | Adverbial and instrumental participles | -уэ, -рэ suffixed participles |
| chunk_048 | 236-240 | Participle inflection, case marking | Participial phrases |
| chunk_049 | 241-245 | Gerunds (деепричастия) and infinitives | Infinitive forms, masdar (verbal noun) |

**Participle System:**

```
SUBJECT PARTICIPLE (субъектное причастие):
- кIуа "went (subject who went)"
- кIуэ-ри "going (subject going)" ← present tense

OBJECT PARTICIPLE (объектное причастие):
- кIуэ-ни "someone going" (affects object of main verb)

ADVERBIAL PARTICIPLE (деепричастие):
- кIуэ-у "going, while going"
- кIуэ-рэ "having gone"

INSTRUMENTAL PARTICIPLE:
- кIуэ-шхуэ "by means of going"
```

**Infinitive Forms:**

```
Three infinitive variants in Kabardian:

1. -н suffix form: кIуэ-н "to go"
   - Used with volitional predicates (хуэй "want")
   - "Сэ кIуэн хуэйщ" = "I want to go"

2. -ну suffix form: кIуэ-ну "to go"
   - Used with phase predicates (щIэддзэ "begin")
   - "Дэ щIэддзэнущ кIуэну" = "We began to go"

3. Bare stem: кIуэ "to go"
   - Used with perception predicates
   - "Сэ абы кIуэ сыплъагъущ" = "I see him going"
```

**Key Grep Patterns:**

```bash
# Find participle types
grep -i "причастие|participle" chunks_045-048

# Find gerund formation (-у, -рэ suffixes)
grep -E "\-уэ|\-рэ" chunks_047-049

# Find infinitive forms
grep -E "\-н\b|\-ну\b|инфинитив" chunks_049
```

**Critical for Skills:**
- `kbd-translator`: Participles and gerunds are used in relative clauses and temporal expressions
  - "The running boy" → "кIуэ-ри цIыху"
  - "Having seen the house" → "унэ елъагъу"
  
- `kbd-morphology`: Understanding -у, -рэ, -уэ suffixes and their participial roots

---

### 2.9 ADVERBS (chunks_050-051, pages 246-256, 72KB)

**Purpose:** Adverb formation and classification - essential for circumstantial expressions.

| Chunk | Pages | Topics | Content |
|-------|-------|--------|---------|
| chunk_050 | 246-250 | End of verbal derivations + adverb introduction | Masdar, infinitive review, adverb types |
| chunk_051 | 251-255 | Adverb formation and production | Derived vs root adverbs |

**Adverb Categories:**

```
TEMPORAL ADVERBS (время):
- Root adverbs: иджыри "now/still", пщэдей "yesterday", нобэ "today"
- Derived: мыгувэу "soon", хэкIуэтауэ "late"
- Duration: зэпымыууэ "continuously"

SPATIAL ADVERBS (место):
- Location: мыдэ "here/hither", модэ "there/thither", дэнэ "where"
- Direction: модэкIэ "there" (direction), ипщэкIэ "upward"
- Distance: жыжьэу "far away"

MANNER ADVERBS (образ действия):
- From adjectives: дахэу "beautifully" (from дахэ "beautiful")
- With -у, -кIэ suffixes
- Reduplication: щ-щэ "quickly" (from щэ "fast")

QUANTITATIVE ADVERBS:
- мыр "much", кIын "little", жыIэ "many"
```

**Adverb Formation Patterns:**

```
FROM ADJECTIVES (-у suffix):
дахэ "beautiful" → дахэу "beautifully"
лъагэ "big" → лъагэу "greatly"

FROM NOUNS + -кIэ:
нобэ "today" → нобэкIэ "on today (specific date)"

FROM NUMBERS + -у:
тIу "two" → тIуу "twice" (with palatalization)

REDUPLICATION:
щ-щэхыу "rapidly"
нобэ-ныжэбэ "sometimes today, sometimes at night"
```

**Key Grep Patterns:**

```bash
# Find adverb formation rules
grep -i "наречи\|adverb" chunks_050-051

# Find temporal adverbs (иджыри, пщэдей)
grep -E "иджыри|пщэдей|нобэ|время" chunks_051

# Find spatial adverbs (мыдэ, модэ)
grep -E "мыдэ|модэ|место" chunks_051

# Find manner adverbs (-у suffix)
grep -E "\-у\b|\-кIэ\b" chunks_050-051
```

**Critical for Skills:**
- `kbd-translator`: Adverbs are crucial for translating Russian temporal/spatial/manner expressions
  - "Yesterday" → пщэдей, "now/still" → иджыри, "here" → мыдэ, "there" → модэ

- `kbd-morphology`: Identifying adverbial suffixes and formation patterns

---

### 2.10 FUNCTION WORDS (chunks_052-055, pages 256-282, 152KB) ⭐ CRITICAL

**Purpose:** Postpositions, conjunctions, particles - essential for sentence structure and connections.

| Chunk | Pages | Topics | Critical Content |
|-------|-------|--------|------------------|
| chunk_052 | 256-260 | Adverbs (final sections) + postposition intro | Continuation from adverbs section |
| chunk_053 | 261-265 | **Postpositions (Morphology)** | Structure, agreement, government |
| chunk_054 | 266-270 | **Postposition Functions** + Conjunction types | Semantic functions, coordinating vs subordinating |
| chunk_055 | 271-275 | **Subordinating Conjunctions** + Particles | Clause-linking words, particle meanings |

**Postposition System (chunks_053-054) - CRITICAL:**

Kabardian postpositions function like Russian prepositions but appear AFTER nouns:

```
LOCATIVE POSTPOSITIONS:
- деж/дей "у, от, около, возле" (at, from, near, by): унэм деж "near the house"
- щыщ "из" (from, out of): унэм щыщ "from the house"
- щхьэкIэ "для, ради, из-за" (for, because of): унэм щхьэкIэ "for the house"

TEMPORAL POSTPOSITIONS:
- пщIондэ "до" (until, up to): нобэ пщIондэ "until today"
- лъандэрэ "с" (with, since): нобэ лъандэрэ "since today"
- иджыри къэс "до сих пор" (until now): иджыри къэс "until now"

CAUSAL/PURPOSIVE POSTPOSITIONS:
- папщIэ/папщIэкIэ "для, ради, о" (for, about): абы папщIэ "about him/for him"
- щхьэкIэ "для, ради, из-за" (for, because of): сэ щхьэкIэ "because of me"

LIMITATIVE POSTPOSITIONS:
- нэгъунэ "до, вплоть до" (up to, as far as): къалэм нэгъунэ "up to the city"
```

**Conjunction System (chunks_054-055) - CRITICAL:**

```
COORDINATING CONJUNCTIONS (сочинительные союзы):
- и "and": "лыр и лъыкъу" = "father and mother"
- ауэ "and/but": "щыIащ ауэ си нэтхьэу" = "he was there but I didn't see him"
- е "or": "пlэ е хьэ" = "above or below"

SUBORDINATING CONJUNCTIONS (подчинительные союзы):
- фэ "that" (introduces noun clauses): "жиIащ фэ ар кIуащ" = "he said that he went"
- зэрыIуэу "if/when": "зэрыIуэу щыIащ" = "when he was there"
- гъуэм "because": "гъуэм ущыпlэ" = "because you went"
- кIасэ "while": "сэ лэжьэнущ кIасэ" = "while I was working"

PARTICLES (частицы):
- гущэ "even": "ауи гущэ" = "even though"
- аркъудей "only": "аркъудей щыIащ" = "only then was he there"
- иIэ "let's, let me": "иIэ кIуэ" = "let's go"
```

**Key Grep Patterns:**

```bash
# Find postposition system
grep -E "послелог\|postposition" chunks_053-054

# Find postposition examples with -р, -м, -у suffixes (possessive marking)
grep -E "гъун|мыш|хьэ|фэ" chunks_053

# Find conjunction inventory
grep -E "союз\|conjunction" chunks_054-055

# Find specific conjunctions (и, ауэ, е, фэ)
grep -E "\bи\b|\bауэ\b|\bе\b|\bфэ\b" chunks_054-055

# Find particle meanings
grep -i "частица\|particle" chunks_055
```

**Critical for Skills:**
- `kbd-translator`: **ESSENTIAL** - Postpositions are critical for expressing spatial/temporal relationships
  - Russian prepositions (в, на, перед, после) → Kabardian postpositions with possessive markers
  - Conjunction selection affects sentence semantics (и vs ауэ changes meaning)
  - Particle placement modifies focus and emphasis
  
- `kbd-glossary`: Finding postposition entries in dictionaries (they appear as separate lemmas)

---

### 2.11 SYNTAX (chunks_056-080, pages 282-404, 932KB) ⭐⭐⭐ CRITICAL

**Purpose:** Sentence structure and **critical SOV word order rules** - foundation of translation.

| Chunk Range | Pages | Topics | Critical Content |
|-------------|-------|--------|------------------|
| 056-057 | 276-285 | Introduction, phrase structure, sentence types | Basic sentence structure framework |
| 058-061 | 286-305 | Simple sentences, declarative/interrogative/imperative | Sentence type distinctions |
| 062-065 | 306-325 | Predicate types, subject morphology | Core grammatical functions |
| 066-073 | 326-365 | Complements, attributes, circumstantials | Modifier functions and positions |
| **074-075** | **366-375** | **WORD ORDER RULES (SOV BASE ORDER)** | **⭐ MOST CRITICAL FOR TRANSLATION** |
| 076-080 | 376-404 | Complex sentences, subordination, embedding | Multi-clause structures |

**CRITICAL WORD ORDER (from chunks_074-075):**

Kabardian follows strict Subject-Object-Verb (SOV) order:

```
BASIC SOV STRUCTURE (verified example from chunk_074):

Russian (SVO): Парень книгу прочтет    Subject-Verb-Object
               Boy    book   will-read

Kabardian (SOV): ЩIалэм тхылъыр иджынущ  Subject-Object-Verb
                 Boy-the book-the will-read

EXPANSION WITH MODIFIERS (SOV, verified from chunk_074):

Russian:     Я тебя вчера видел
             I you yesterday saw

Kabardian:   Сэ уэ дыгъуасэ услъэгъуащ
             I you yesterday saw

Order rules:
1. Subject (with definite marker -р if definite)
2. Temporal/spatial circumstantials
3. Agent/indirect objects (if present)
4. Adjectives/modifiers of object
5. Direct object (with definite marker -р)
6. Adverbials of manner
7. VERB + TAM/MOOD markers

CASE MARKING INTERACTS WITH WORD ORDER:

The -р definite marker on nouns helps signal:
- Subject reference (агент): абы-р = "the one/he" 
- Object reference (темa): унэ-р = "the house"
- Theme in multi-person verbs

WITHOUT case/definiteness markers, word position becomes critical:
- First noun = likely subject
- Noun before verb = object
- Verb-final position mandatory
```

**Complement Positions (from chunks_066-073):**

```
TYPES OF COMPLEMENTS (дополнения):

1. DIRECT OBJECT (прямое дополнение):
   - Marks theme of action
   - Can be definite (-р) or indefinite
   - Position: immediately before verb
   - Example: "сэ унэр сыплъ" = "I house (DEF) see"

2. INDIRECT OBJECT (косвенное дополнение):
   - Marks recipient/beneficiary/maleficiary
   - Appears in complex multi-person verbs
   - Position: between subject and direct object
   - Example: "сэ абы-р ар изоты" = "I him (DEF) it give"

3. OBLIQUE COMPLEMENTS (обстоятельственные дополнения):
   - With postpositions and case markers
   - Position: after subject, before object
   - Example: "сэ унэм гъунэ-р сыплъ" = "I near-house see"

WORD ORDER WITHIN COMPLEMENTS:
- Case-marked nouns can move more freely
- Postpositional phrases: noun + postposition + possessive suffix
```

**Attributes and Modifiers (from chunks_066-073):**

```
MODIFIER POSITION (BEFORE HEAD NOUN - Attributive Order):

Kabardian uses PRENOMINAL modifiers:

Article/Possessive + Adjective + Quantifier + Noun + Definite Marker
Example: а  дахэ  зы  унэ  р
         THE beautiful ONE house DEF
         = "the one beautiful house"

RELATIVE CLAUSE POSITION:
- Relative clauses come BEFORE the head noun
- Use participle + relative particle
- Example: "кIуэ-ри лым" = "going (one)" = "the one going"
```

**Complex Sentences (chunks_076-080):**

```
SUBORDINATION PATTERNS:

1. NOUN CLAUSE (with фэ "that"):
   "жиIащ фэ ар кIуащ" = "he-said that he went"
   Structure: Main Clause + фэ + Subordinate Clause

2. ADVERBIAL CLAUSE (with subordinating conjunctions):
   "зэрыIуэу щыIащ" = "when he was there"
   With: зэрыIуэу (temporal), гъуэм (causal), кIасэ (temporal)

3. RELATIVE CLAUSE (with participles):
   "кIуэ-ри цIыху" = "the-going person" = "the person who goes"
   Uses subject/object participles + relative particles

WORD ORDER IN COMPLEX SENTENCES:
- Main clause precedes subordinate in most cases
- Subordinate clause maintains own SOV order
- Conjunction/particle marks relationship
```

**Key Grep Patterns for Syntax:**

```bash
# Find basic SOV word order rules
grep -i "словопорядок\|word.order" chunks_074-075

# Find subject and predicate description
grep -i "подлежащее\|сказуемое" chunks_062-065

# Find complement types
grep -i "дополнение\|complement" chunks_066-073

# Find attribute/modifier rules
grep -i "определение\|modifier" chunks_066-073

# Find relative clause formation
grep -i "относител\|relative" chunks_076-080

# Find subordination patterns
grep -i "подчинител\|subordinat" chunks_076-080
```

**Critical for Skills:**

- `kbd-translator`: **ABSOLUTELY ESSENTIAL** - Core of the translation algorithm
  - Russian SVO → Kabardian SOV transformation requires understanding these rules
  - Word position determines grammatical function when case markers are ambiguous
  - Modifier order affects meaning and grammaticality
  - Complex sentences require clause reordering
  
- `kbd-morphology`: Understanding how word order interacts with morphology (case, agreement)

---

## Part 3: Data Files Reference

### 3.1 Translation Corpus

**File:** `/Users/panagoa/PycharmProjects/kbd_translate/data/translations/sents_292k.csv`

**Size:** 45MB (~292,000 translation pairs)

**Format:**
```csv
source,translated
"кабардинский текст","русский перевод"
```

**Structure:**
- Column 1 (source): Kabardian text (original)
- Column 2 (translated): Russian translation
- CSV format with quoted fields
- UTF-8 encoding

**Example:**
```
"Америкэ псом зыхуигъазэу жиIат пщащэм.","Америка, ко всем обращаясь, сказала девушка."
"Дапщэ?","Сколько?"
```

**Usage:**
```bash
# ✅ CORRECT: Search with limit
grep -i "унэ" /path/to/sents_292k.csv | head -10

# ✅ CORRECT: Search for Russian word (to find Kabardian equivalent)
grep "видел" /path/to/sents_292k.csv | head -5

# ❌ WRONG: Never load entire 45MB file in memory
# Don't use Read tool to open full file
```

**For kbd-translator skill:**
- **3-level search strategy:**
  1. Exact match on full sentence
  2. Partial match on key words
  3. Pattern match on grammatical structures
- Returns high-quality verified translations
- Essential corpus for CORPUS-FIRST approach

**Search Grep Patterns:**

```bash
# Find examples with specific Kabardian word
grep -i "лэжьэ" sents_292k.csv | head -5

# Find examples with Russian verb
grep -i "видеть\|видел\|видим" sents_292k.csv | head -5

# Find examples with multi-person verb patterns
grep -E "[аеиоуу]-[а-я]+-[а-я]+" sents_292k.csv | head -10

# Find examples with specific postposition
grep "гъунэ\|фэм\|мыш" sents_292k.csv | head -5

# Count examples with word (in quotes to preserve structure)
grep -c "\"[^\"]*унэ[^\"]*\"" sents_292k.csv
```

---

### 3.2 Glossaries

#### 3.2.1 Rus-Ady_UASP.csv (Russian-Kabardian)

**File:** `/Users/panagoa/PycharmProjects/kbd_translate/data/glossary/Rus-Ady_UASP.csv`

**Size:** 3.4MB (~15,989 entries)

**Format:**
```csv
"русское_слово","<div>HTML содержимое с кабардинским переводом</div>"
```

**Structure:**
- Column 1: Russian word (lookup key)
- Column 2: HTML-formatted content with:
  - Kabardian translations
  - Word class labels
  - Example sentences
  - Grammatical information

**Example Entry Structure:**
```html
<div style="...">
  <span class="translation">кабардинское слово</span>
  <span class="pos">[существительное/глагол/...]</span>
  <span class="examples">Примеры использования...</span>
</div>
```

**Usage:**
```bash
# ✅ CORRECT: Use grep to find Russian word
grep -F "\"видеть\"" Rus-Ady_UASP.csv

# ✅ CORRECT: Case-insensitive search with limit
grep -i -m 1 "\"работ" Rus-Ady_UASP.csv

# ❌ WRONG: Don't load entire 3.4MB file
# Never use Read tool for full file
```

**For kbd-translator skill:**
- **FALLBACK source** (not primary - corpus is primary)
- Useful for finding base word translations
- HTML parsing required to extract Kabardian
- Search strategy: word-by-word for verbs/nouns

**Search Grep Patterns:**

```bash
# Find Russian verb translation
grep -i "\"писать\"" Rus-Ady_UASP.csv

# Find noun with quotes (to ensure exact word match)
grep -F "\"дом\"" Rus-Ady_UASP.csv

# Find words starting with prefix
grep "\"работ" Rus-Ady_UASP.csv | head -3

# Count entries
wc -l Rus-Ady_UASP.csv
```

---

#### 3.2.2 Ady-Ady_AP.csv (Kabardian Explanatory Dictionary)

**File:** `/Users/panagoa/PycharmProjects/kbd_translate/data/glossary/Ady-Ady_AP.csv`

**Size:** 15MB (~98,412 entries)

**Format:**
```csv
"КАБАРДИНСКОЕ_СЛОВО","<div>HTML определение на кабардинском</div>"
```

**Structure:**
- Column 1: Kabardian word (lookup key, often UPPERCASE)
- Column 2: HTML-formatted explanatory definition in Kabardian
- Extensive dictionary with morphological variants

**Usage:**
```bash
# ✅ CORRECT: Case-insensitive search with limit
grep -i -m 2 "ЛЭЖЬЭ" Ady-Ady_AP.csv

# ✅ CORRECT: Search for Kabardian root
grep -i "ТХЫ" Ady-Ady_AP.csv | head -3

# ❌ WRONG: Don't load entire 15MB file
# Never use Read tool for full file
```

**For kbd-glossary skill:**
- **Primary Kabardian resource** for word meaning verification
- Definitions in Kabardian help with semantic understanding
- Large entry count covers morphological variants
- Essential for disambiguating polysemy

**Search Grep Patterns:**

```bash
# Find Kabardian word definition
grep -i "\"ТХЫ\"" Ady-Ady_AP.csv

# Find words by root (search uppercase)
grep "УНЭ" Ady-Ady_AP.csv | head -5

# Find derivations of verb
grep -i "лэжьэ" Ady-Ady_AP.csv | head -5

# Case-insensitive exact match
grep -F -i "\"КIУЭ\"" Ady-Ady_AP.csv
```

---

### 3.3 Sentence Corpus

**File:** `/Users/panagoa/PycharmProjects/kbd_translate/data/00_kbd_sentences.csv`

**Size:** ~7.3MB (~100,000+ sentences)

**Format:**
```csv
sent
"кабардинское предложение"
```

**Structure:**
- Single column named "sent"
- Complete Kabardian sentences
- Used for examples and pattern extraction

**Usage:**
```bash
# Find sentences with specific word
grep "унэ" 00_kbd_sentences.csv | head -10

# Find multi-person verb examples
grep -E "[аеиоу]\_[а-я]+\_[а-я]+" 00_kbd_sentences.csv | head -5
```

**For kbd-translator/morphology skills:**
- Source for example sentences
- Pattern recognition for grammar rules
- Verification of sentence structures

---

## Part 4: Topic Index - Find Grammar For Specific Topics

Use this table to locate specific grammatical topics in the chunks:

### 4.1 Verb Grammar

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Verb polypersonalism** | 023-025 | 111-125 | Multi-argument verbs (1-5 participants) |
| **Verb paradigms (1-person)** | 026 | 126-130 | Basic transitive/intransitive |
| **Verb paradigms (2-person)** | 027 | 131-135 | Two-argument verbs, agent-theme |
| **Verb paradigms (3-person)** | 028 | 136-140 | Three-argument verbs, recipient |
| **Verb paradigms (4-person)** | 029 | 141-145 | Four-argument complex verbs |
| **Dynamic vs static verbs** | 024 | 116-120 | Copula vs action verbs |
| **TAM system (Present)** | 031 | 151-155 | Present tenses (1, 2, continuous) |
| **TAM system (Past/Aorist)** | 031-033 | 151-165 | Perfect I, Perfect II, Aorist |
| **TAM system (Future)** | 033 | 161-165 | Future I, Future II |
| **Mood (Indicative)** | 033 | 161-165 | Factual statements |
| **Mood (Conditional/Subjunctive)** | 033-034 | 166-170 | Hypothetical (-н suffix) |
| **Mood (Optative/Wish)** | 034-035 | 171-175 | Desire forms (-рэт suffix) |
| **Mood (Imperative)** | 035 | 175+ | Commands (Appendix) |
| **Negation (-къым)** | 034-036 | 171-185 | Negative forms of all tenses |
| **Causative (гъэ-)** | 038-039 | 191-199 | Make/cause actions |
| **Reciprocal (зэ-)** | 039-040 | 200-205 | Mutual actions |
| **Comitative (дэ-)** | 039-040 | 200-205 | With/together actions |
| **Version (хуэ-/фIэ-)** | 039-040 | 200-205 | Directional nuance |
| **Potential (хуэ-)** | 040 | 205+ | Ability/capability |
| **Directional preverb (къэ-)** | 040-042 | 206-215 | Away from |
| **Directional preverb (къы-)** | 040-042 | 206-215 | Toward |
| **Directional preverb (щы-)** | 040-042 | 206-215 | Upward |
| **Directional preverb (дэ-)** | 040-042 | 206-215 | Downward |
| **Directional preverb (те-)** | 040-042 | 206-215 | Along surface |
| **Ablaut in derivation** | 044 | 216-220 | ы:э patterns in -кI, -хь forms |

### 4.2 Noun Grammar

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Definiteness (-р marker)** | 013 | 61-65 | Definite vs indefinite marking |
| **Case system overview** | 014 | 66-70 | Ergative, postpositional, oblique |
| **Number (-хэ plural)** | 015 | 71-75 | Singular/plural marking |
| **Possessive marking** | 015 | 71-75 | -м, -й possessive suffixes |
| **Noun derivation (-гъэ)** | 012, 016 | 56-80 | Abstract noun formation |
| **Noun derivation (-агъ)** | 012 | 56-60 | Quality/property nouns |
| **Compound nouns** | 016 | 76-80 | Noun + noun compounds |

### 4.3 Adjective Grammar

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Comparative degree (-рэ)** | 018 | 86-90 | More beautiful, stronger |
| **Superlative degree** | 019 | 91-95 | Most beautiful, strongest |
| **Augmentative (-шхуэ)** | 019 | 91-95 | Very big, large |
| **Diminutive (-кIэ)** | 019 | 91-95 | Small, little |
| **Relative adjectives** | 020 | 96-100 | Denominative adj (из wood), etc. |

### 4.4 Numeral Grammar

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Vigesimal system (1-10)** | 020 | 101-105 | зы, тIу, щ, плI, тху... пщI |
| **Vigesimal system (11-20)** | 021 | 106-110 | Compound formation rules |
| **Vigesimal system (100+)** | 021-022 | 106-115 | Hundreds, complex compounds |
| **Ordinal numerals** | 022 | 111-115 | First, second, third (е-з-анэ) |
| **Distributive numerals** | 022 | 111-115 | "по одному" (one each) |
| **Collective numerals** | 022 | 111-115 | Grouped quantities |

### 4.5 Adverb Grammar

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Temporal adverbs (time)** | 051 | 251-255 | иджыри "now/still", пщэдей "yesterday" |
| **Spatial adverbs (place)** | 051 | 251-255 | мыдэ "here/hither", модэ "there/thither" |
| **Manner adverbs (-у suffix)** | 050-051 | 246-256 | How things are done |
| **Adverb derivation from adj** | 051 | 251-255 | дахэ → дахэу "beautifully" |

### 4.6 Function Words

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Postpositions (spatial)** | 053 | 261-265 | гъун "near", мыш "over", хьэ "below" |
| **Postpositions (temporal)** | 053 | 261-265 | мыхьэнэ "after", дыдей "before" |
| **Postpositions (causal)** | 053 | 261-265 | зэ "because of" |
| **Postposition agreement** | 053 | 261-265 | -р, -м, -у possessive marking |
| **Coordinating conjunctions** | 054 | 266-270 | и "and", ауэ "but", е "or" |
| **Subordinating conjunctions** | 055 | 271-275 | фэ "that", зэрыIуэу "if/when" |
| **Particles** | 055 | 271-275 | гущэ "even", аркъудей "only" |

### 4.7 Deverbal Forms

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Subject participles** | 045 | 221-225 | "going person" (кIуэ-ри) |
| **Object participles** | 046 | 226-230 | Object-oriented participles |
| **Gerunds (-у/-уэ)** | 047-049 | 231-245 | "while going", contemporaneous |
| **Gerunds (-рэ)** | 047-049 | 231-245 | "having gone", perfective |
| **Infinitives (-н form)** | 049 | 241-245 | Used with desire verbs |
| **Infinitives (-ну form)** | 049 | 241-245 | Used with phase verbs |
| **Masdar (verbal noun)** | 049 | 241-245 | Nominalized verb actions |

### 4.8 Syntax

| Topic | Chunks | Pages | Key Content |
|-------|--------|-------|-------------|
| **Basic SOV word order** | 074-075 | 366-375 | Subject-Object-Verb base structure |
| **Word order with modifiers** | 074-075 | 366-375 | Adjectives, adverbs placement |
| **Word order with postpositions** | 074-075 | 366-375 | Postpositional phrase position |
| **Subject marking and agreement** | 062-065 | 306-325 | How subjects are marked |
| **Object marking (-р for definite)** | 066-073 | 326-365 | Direct/indirect object marking |
| **Relative clauses** | 076-080 | 376-404 | Participle-based relative structures |
| **Complex sentences (coordination)** | 076-080 | 376-404 | Multi-clause structures with и, ауэ |
| **Complex sentences (subordination)** | 076-080 | 376-404 | Clauses with фэ, зэрыIуэу, etc. |
| **Question formation** | 036, 074-075 | 181-185, 366-375 | Word order in questions |

---

## Part 5: Practical Search Patterns & Examples

### 5.1 Finding TAM Information

**Goal:** Understand how to mark "I went" vs "I will go"

```bash
# Search for past tense forms
grep -i "прошедш\|past" advanced_verbs/chunk_031*.txt | head -20

# Search for specific TAM suffix examples
grep "щ\|рт\|ну" advanced_verbs/chunk_033*.txt

# Search for perfect forms
grep -i "перфект" advanced_verbs/chunk_031-033*.txt
```

**Expected Finding:** Chunk_031-033 will show:
- Perfect I: с-ы-кIуащ (with -щ suffix indicating recent past)
- Perfect II: с-ы-кIуэрт (with -рт suffix indicating remote past)
- Future: с-ы-кIуэну (with -ну suffix)

---

### 5.2 Finding Negation Rules

**Goal:** How to negate a verb (Russian "не" → Kabardian "-къым")

```bash
# Search for negation chapter
grep -i "отрицани\|negation" advanced_verbs/chunk_034*.txt

# Search for -къым suffix
grep -E "\-къым" advanced_verbs/chunk_034-036*.txt

# Search for negative imperative
grep -i "отрицательн.*повелител" advanced_verbs/chunk_036*.txt
```

**Expected Finding:** Chunk_034-036 will show:
- Negative forms attach -къым to any tense
- Negative imperative: кIуэ-къым "Don't go!"
- Negative participles: кIуэ-къы "non-going"

---

### 5.3 Finding Postposition Rules

**Goal:** How to express "in the house", "near the house"

```bash
# Search for postposition introduction
grep -i "послелог" function_words/chunk_053*.txt

# Search for specific postpositions
grep -E "гъун|мыш|хьэ|фэ" function_words/chunk_053*.txt

# Search for possessive marking on postpositions
grep -E "\-р|\-м|\-у" function_words/chunk_053*.txt
```

**Expected Finding:** Chunk_053 will show:
- унэм фэм = "in the house" (noun + postposition + possessive suffix)
- унэм гъунэр = "near the house"
- Rule: postpositions take possessive affixes (-м, -р, -у) from the noun

---

### 5.4 Finding Multi-Person Verb Paradigms

**Goal:** Understand 3-person verbs (agent-theme-recipient)

```bash
# Search for 3-person verb explanation
grep -i "трёхличн\|три-person\|three-argument" verb_morphology/chunk_028*.txt

# Search for paradigm tables
grep -E "Ед\.ч\.|единствен" verb_morphology/chunk_028*.txt

# Search for examples with 3 arguments
grep -E "дать|отдать" verb_morphology/chunk_028*.txt
```

**Expected Finding:** Chunk_028 will show:
- Tables with prefixes for: Subject (с-, у-, е-)
- Indirect object (different prefix combinations)
- Direct object (implicit or marked)

---

### 5.5 Finding Relative Clause Patterns

**Goal:** How to translate "the person who goes", "the house that I built"

```bash
# Search for participle types in verbal_derivations
grep -i "причастие\|participle" verbal_derivations/chunk_045*.txt

# Search for subject vs object participles
grep -E "субъектн\|объектн" verbal_derivations/chunk_045-046*.txt

# Search for relative clause examples
grep -i "относител\|relative" syntax/chunk_076*.txt
```

**Expected Finding:**
- Chunk_045: Subject participles кIуэ-ри (the one going)
- Chunk_046: Object participles
- Chunk_076-080: Relative clause syntax with participles

---

## Part 6: For Each Claude Skill - Specific Recommendations

### 6.1 For kbd-translator Skill

**Most Critical Sections (in priority order):**

1. **advanced_verbs/ (chunks 031-044)** - 492KB, Pages 151-222
   - TAM system (chunks 031-033): How to convert Russian tense to Kabardian
   - Mood system (chunks 033-034): Distinguishing indicative vs conditional
   - Negation (chunks 034-036): -къым suffix and negative forms
   - Derivational categories (chunks 038-040): Causative, reciprocal, version
   - Directional preverbs (chunks 040-042): Movement preverbs (къэ-, къы-, дэ-, те-)

2. **syntax/ (chunks 056-080)** - 932KB, Pages 282-404
   - **Chunks 074-075 (CRITICAL)**: SOV word order rules
   - Chunks 062-065: Subject/object marking
   - Chunks 066-073: Complement and modifier positions
   - Chunks 076-080: Complex sentence structures

3. **function_words/ (chunks 052-055)** - 152KB, Pages 256-282
   - Chunks 053-054: Postposition system and agreement
   - Chunks 054-055: Conjunction inventory and usage

4. **verb_morphology/ (chunks 023-030)** - 244KB, Pages 111-150
   - Chunks 025-029: Multi-person verb paradigms

### 6.2 For kbd-morphology Skill

**Most Critical Sections:**

1. **advanced_verbs/ (chunks 031-044)** - TAM and mood suffixes
   - For [TAM] position in [PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD]

2. **verb_morphology/ (chunks 023-030)** - Paradigm reference
   - For [PRAGM], [GEOM], [ARGS] prefixes

3. **verbal_derivations/ (chunks 044-049)** - Participle forms
   - For derivational morphology

4. **nouns/, adjectives/, numerals/** - Word class morphology

### 6.3 For kbd-glossary Skill

**Most Useful Sections:**

1. **function_words/chunk_053** - Postposition lemmas
   - Helps identify postposition entries in glossaries

2. **adverbs/chunks_050-051** - Adverb roots
   - Temporal (иджыри, пщэдей), spatial (мыдэ, модэ)

3. **All sections** - For semantic understanding
   - Use grammar to understand context of dictionary entries

---

## Part 7: Data Files Summary

### Quick Reference Table

| File | Size | Format | Entries | Purpose | Search Tool |
|------|------|--------|---------|---------|------------|
| sents_292k.csv | 45MB | CSV | 292k pairs | Translation corpus | Grep (with limit) |
| Rus-Ady_UASP.csv | 3.4MB | CSV+HTML | 15,989 | Rus→Kbd dictionary | Grep (with -m 1) |
| Ady-Ady_AP.csv | 15MB | CSV+HTML | 98,412 | Kbd explanatory | Grep (with -m 1-2) |
| 00_kbd_sentences.csv | 7.3MB | CSV | 100k+ | Sentence corpus | Grep |

**Key Rules:**
- Always use Grep with `-m N` (limit) on large files
- Never use Read tool to open entire CSV files
- CSV files preserve quotes around fields
- HTML content may need parsing/stripping

---

## Summary: Key Takeaways for Skills Implementation

1. **kbd-translator** needs:
   - Chunks 074-075 (SOV word order) - CRITICAL
   - Chunks 031-044 (verb TAM, mood, negation, derivation) - CRITICAL
   - Chunks 053-055 (postpositions, conjunctions) - CRITICAL
   - sents_292k.csv corpus for CORPUS-FIRST approach

2. **kbd-morphology** needs:
   - Chunks 023-030 (multi-person verb paradigms)
   - Chunks 031-044 (TAM, mood, derivation)
   - Chunks 044-049 (participles, gerunds)
   - Understanding of [PRAGM]-[GEOM]-[ARGS]-[STEM]-[TAM]-[SUBORD] structure

3. **kbd-glossary** needs:
   - Ady-Ady_AP.csv for Kabardian word meanings
   - Rus-Ady_UASP.csv for Russian→Kabardian lookup
   - Understanding of postpositions (chunks 053-054)

4. **General Patterns:**
   - Use Grep, never load 45MB+ files entirely
   - Chunks are organized logically: phonetics→morphology→syntax
   - Tables in chunks show inflectional paradigms
   - Examples in chunks show real usage

