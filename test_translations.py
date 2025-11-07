#!/usr/bin/env python3
"""Test Russian→Kabardian translation using corpus-first approach."""

import csv
import re
from pathlib import Path
from difflib import SequenceMatcher

# Configuration
TEST_FILE = "test_sentences_100.csv"
CORPUS_FILE = "data/translations/sents_292k.csv"
OUTPUT_FILE = "test_results_100.csv"

def normalize_text(text: str) -> str:
    """Normalize Kabardian text for comparison."""
    # Standardize glottal stop representations
    text = text.replace('ӏ', 'I')  # U+04CF → Latin I
    text = text.replace('1', 'I')  # Digit 1 → Latin I
    text = text.replace('l', 'I')  # Lowercase l → Latin I
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()

def extract_keywords(russian_text: str) -> list[str]:
    """Extract keywords from Russian text for corpus search."""
    # Remove punctuation and quotes
    text = re.sub(r'[«»"\'!?,;:.()]', ' ', russian_text)
    # Split into words and filter short ones
    words = [w.lower() for w in text.split() if len(w) >= 3]
    # Remove common Russian stop words
    stop_words = {'это', 'что', 'как', 'или', 'для', 'при', 'так', 'все', 'был', 'была',
                  'было', 'были', 'есть', 'быть', 'этот', 'эта', 'эти', 'тот', 'того',
                  'чтобы', 'этом', 'том', 'если', 'когда', 'где', 'уже', 'еще', 'них',
                  'они', 'она', 'его', 'ему', 'тем', 'этих', 'тех', 'раз', 'два'}
    keywords = [w for w in words if w not in stop_words]
    return keywords[:10]  # Limit to top 10 keywords

def search_corpus_exact(russian_text: str, corpus_cache: list[dict]) -> list[dict]:
    """Search for exact matches in corpus."""
    normalized_input = russian_text.lower().strip()
    results = []

    for entry in corpus_cache:
        if entry['rus_lower'] == normalized_input:
            results.append(entry)

    return results

def search_corpus_keywords(keywords: list[str], corpus_cache: list[dict], limit: int = 5) -> list[dict]:
    """Search corpus by keywords with scoring."""
    results = []

    for entry in corpus_cache:
        rus_text = entry['rus_lower']
        # Count keyword matches
        matches = sum(1 for kw in keywords if kw in rus_text)

        if matches > 0:
            score = matches / len(keywords) if keywords else 0
            results.append({
                'entry': entry,
                'score': score,
                'matches': matches
            })

    # Sort by score and matches
    results.sort(key=lambda x: (x['score'], x['matches']), reverse=True)
    return results[:limit]

def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two texts (0-1)."""
    return SequenceMatcher(None, text1, text2).ratio()

def translate_with_corpus(russian_text: str, corpus_cache: list[dict]) -> tuple[str, str, float]:
    """
    Translate Russian→Kabardian using corpus-first approach.
    Returns: (translation, method, confidence)
    """
    # Step 1: Try exact match
    exact_matches = search_corpus_exact(russian_text, corpus_cache)
    if exact_matches:
        return (exact_matches[0]['kbd'], 'exact_match', 1.0)

    # Step 2: Search by keywords
    keywords = extract_keywords(russian_text)
    if not keywords:
        return ("", 'no_keywords', 0.0)

    keyword_results = search_corpus_keywords(keywords, corpus_cache, limit=5)

    if not keyword_results:
        return ("", 'no_matches', 0.0)

    # Use best match
    best = keyword_results[0]
    translation = best['entry']['kbd']
    confidence = best['score']

    return (translation, f'keyword_match_{best["matches"]}', confidence)

def load_corpus_cache(corpus_file: str, max_entries: int = None) -> list[dict]:
    """Load corpus into memory for faster search."""
    print(f"Loading corpus from {corpus_file}...")
    cache = []

    with open(corpus_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            cache.append({
                'kbd': normalize_text(row['source']),
                'rus': row['translated'].strip(),
                'rus_lower': row['translated'].lower().strip()
            })

            if max_entries and i >= max_entries:
                break

            if i % 50000 == 0:
                print(f"  Loaded {i:,} entries...")

    print(f"✓ Loaded {len(cache):,} corpus entries")
    return cache

def main():
    print("=" * 80)
    print("Testing Russian→Kabardian Translation (Corpus-First Approach)")
    print("=" * 80)

    # Load corpus into memory
    corpus_cache = load_corpus_cache(CORPUS_FILE)

    # Load test sentences
    print(f"\nLoading test sentences from {TEST_FILE}...")
    test_sentences = []
    with open(TEST_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        test_sentences = list(reader)
    print(f"✓ Loaded {len(test_sentences)} test sentences")

    # Run translations
    print(f"\nRunning translations...")
    results = []

    for i, test in enumerate(test_sentences, 1):
        rus_text = test['rus_original'].strip()
        kbd_original = normalize_text(test['kbd_original'])

        # Translate using corpus
        kbd_translated, method, confidence = translate_with_corpus(rus_text, corpus_cache)

        # Calculate similarity with original
        similarity = calculate_similarity(kbd_original, kbd_translated) if kbd_translated else 0.0

        # Store result
        result = {
            'line_num': test['line_num'],
            'rus_original': rus_text,
            'kbd_original': kbd_original,
            'kbd_translated': kbd_translated,
            'translation_method': method,
            'confidence': f"{confidence:.3f}",
            'similarity': f"{similarity:.3f}",
            'exact_match': 'YES' if similarity >= 0.95 else 'NO'
        }
        results.append(result)

        # Progress update
        if i % 10 == 0:
            print(f"  Processed {i}/{len(test_sentences)} sentences...")

    # Save results
    print(f"\nSaving results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['line_num', 'rus_original', 'kbd_original', 'kbd_translated',
                     'translation_method', 'confidence', 'similarity', 'exact_match']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Calculate statistics
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)

    total = len(results)
    exact_matches = sum(1 for r in results if r['exact_match'] == 'YES')
    no_translation = sum(1 for r in results if not r['kbd_translated'])

    similarities = [float(r['similarity']) for r in results if r['kbd_translated']]
    confidences = [float(r['confidence']) for r in results]

    # Method distribution
    methods = {}
    for r in results:
        method = r['translation_method']
        methods[method] = methods.get(method, 0) + 1

    print(f"\nTotal test sentences: {total}")
    print(f"Exact matches (similarity ≥ 0.95): {exact_matches} ({exact_matches/total*100:.1f}%)")
    print(f"No translation found: {no_translation} ({no_translation/total*100:.1f}%)")

    if similarities:
        print(f"\nSimilarity scores:")
        print(f"  Mean: {sum(similarities)/len(similarities):.3f}")
        print(f"  Min: {min(similarities):.3f}")
        print(f"  Max: {max(similarities):.3f}")
        print(f"  Median: {sorted(similarities)[len(similarities)//2]:.3f}")

    print(f"\nConfidence scores:")
    print(f"  Mean: {sum(confidences)/len(confidences):.3f}")

    print(f"\nTranslation methods:")
    for method, count in sorted(methods.items(), key=lambda x: -x[1]):
        print(f"  {method}: {count} ({count/total*100:.1f}%)")

    # Show some examples
    print("\n" + "=" * 80)
    print("EXAMPLE TRANSLATIONS (First 3)")
    print("=" * 80)

    for i, r in enumerate(results[:3], 1):
        print(f"\n{i}. Line {r['line_num']} | Method: {r['translation_method']} | Similarity: {r['similarity']}")
        print(f"   RUS: {r['rus_original'][:100]}...")
        print(f"   KBD (original):   {r['kbd_original'][:100]}...")
        print(f"   KBD (translated): {r['kbd_translated'][:100] if r['kbd_translated'] else '(no translation)'}...")

    print("\n" + "=" * 80)
    print(f"✓ Full results saved to: {OUTPUT_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()
