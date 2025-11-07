#!/usr/bin/env python3
"""
Test Russian→Kabardian translation using LLM-augmented corpus approach.
This simulates the kbd-translator skill logic but without actual LLM.
"""

import csv
import re
from collections import Counter
from difflib import SequenceMatcher

# Configuration
TEST_FILE = "test_sentences_100.csv"
CORPUS_FILE = "data/translations/sents_292k.csv"
OUTPUT_FILE = "test_llm_results_100.csv"

def normalize_kbd(text: str) -> str:
    """Normalize Kabardian text."""
    text = text.replace('ӏ', 'I').replace('1', 'I').replace('l', 'I')
    return ' '.join(text.split()).strip()

def extract_keywords(russian_text: str, min_length: int = 3) -> list[str]:
    """Extract keywords from Russian text."""
    text = re.sub(r'[«»"\'!?,;:.()—–-]', ' ', russian_text)
    words = [w.lower() for w in text.split() if len(w) >= min_length]

    # Remove common stop words
    stop_words = {
        'это', 'что', 'как', 'или', 'для', 'при', 'так', 'все', 'был', 'была',
        'было', 'были', 'есть', 'быть', 'этот', 'эта', 'эти', 'тот', 'того',
        'чтобы', 'этом', 'том', 'если', 'когда', 'где', 'уже', 'еще', 'них',
        'они', 'она', 'его', 'ему', 'тем', 'этих', 'тех', 'раз', 'два', 'три',
        'также', 'более', 'может', 'могут', 'после', 'перед', 'между'
    }

    keywords = [w for w in words if w not in stop_words]

    # Count frequency and prioritize important words
    word_counts = Counter(keywords)

    # Return unique keywords sorted by frequency
    return list(dict.fromkeys(keywords))

def calculate_match_score(keywords: list[str], text: str) -> float:
    """Calculate how well keywords match a text."""
    text_lower = text.lower()
    matches = sum(1 for kw in keywords if kw in text_lower)
    if not keywords:
        return 0.0
    return matches / len(keywords)

def calculate_similarity(s1: str, s2: str) -> float:
    """Calculate string similarity."""
    return SequenceMatcher(None, s1, s2).ratio()

def search_corpus_smart(russian_text: str, corpus_cache: list[dict], top_k: int = 10) -> list[dict]:
    """
    Smart corpus search using keyword matching and scoring.
    Returns top_k best matches with their scores.
    """
    keywords = extract_keywords(russian_text)

    if not keywords:
        return []

    # Score all corpus entries
    matches = []
    for entry in corpus_cache:
        score = calculate_match_score(keywords, entry['rus'])
        if score > 0:
            matches.append({
                'kbd': entry['kbd'],
                'rus': entry['rus'],
                'score': score,
                'keyword_count': sum(1 for kw in keywords if kw in entry['rus'].lower())
            })

    # Sort by score and keyword count
    matches.sort(key=lambda x: (x['score'], x['keyword_count']), reverse=True)

    return matches[:top_k]

def analyze_translation_patterns(matches: list[dict], keywords: list[str]) -> dict:
    """
    Analyze patterns from corpus matches to inform translation.
    This simulates LLM pattern analysis.
    """
    if not matches:
        return {'confidence': 0.0, 'method': 'no_matches'}

    best_match = matches[0]

    # Calculate confidence based on match quality
    confidence = best_match['score']

    # Determine translation method
    if confidence >= 0.8:
        method = 'high_confidence_pattern'
    elif confidence >= 0.5:
        method = 'medium_confidence_pattern'
    elif confidence >= 0.3:
        method = 'low_confidence_pattern'
    else:
        method = 'weak_pattern'

    return {
        'confidence': confidence,
        'method': method,
        'best_match_rus': best_match['rus'],
        'best_match_kbd': best_match['kbd'],
        'num_good_matches': sum(1 for m in matches if m['score'] >= 0.3)
    }

def translate_with_llm_approach(russian_text: str, corpus_cache: list[dict],
                                exclude_line: int = None) -> dict:
    """
    Translate using LLM-augmented corpus approach.
    Excludes the test sentence itself from corpus if exclude_line is provided.
    """
    # Filter out test sentence from corpus
    if exclude_line:
        corpus_cache = [e for e in corpus_cache if e.get('line_num') != exclude_line]

    # Step 1: Search corpus for similar examples
    matches = search_corpus_smart(russian_text, corpus_cache, top_k=10)

    if not matches:
        return {
            'translation': '',
            'confidence': 0.0,
            'method': 'no_matches',
            'matches_found': 0
        }

    # Step 2: Analyze patterns
    keywords = extract_keywords(russian_text)
    analysis = analyze_translation_patterns(matches, keywords)

    # Step 3: Select best translation
    # In real LLM approach, this would involve pattern adaptation
    # Here we use the best match as baseline
    best_translation = analysis['best_match_kbd']

    return {
        'translation': best_translation,
        'confidence': analysis['confidence'],
        'method': analysis['method'],
        'matches_found': len(matches),
        'best_match_similarity': calculate_similarity(russian_text.lower(),
                                                       analysis['best_match_rus'].lower())
    }

def load_corpus(corpus_file: str) -> list[dict]:
    """Load corpus with line numbers."""
    print(f"Loading corpus from {corpus_file}...")
    corpus = []

    with open(corpus_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            corpus.append({
                'line_num': i + 1,  # +1 for header
                'kbd': normalize_kbd(row['source']),
                'rus': row['translated'].strip()
            })

            if i % 50000 == 0:
                print(f"  Loaded {i:,} entries...")

    print(f"✓ Loaded {len(corpus):,} corpus entries")
    return corpus

def main():
    print("=" * 80)
    print("Testing Russian→Kabardian Translation")
    print("LLM-Augmented Corpus Approach (Excluding Test Sentences)")
    print("=" * 80)

    # Load corpus
    corpus = load_corpus(CORPUS_FILE)

    # Load test sentences
    print(f"\nLoading test sentences from {TEST_FILE}...")
    with open(TEST_FILE, 'r', encoding='utf-8') as f:
        test_sentences = list(csv.DictReader(f))
    print(f"✓ Loaded {len(test_sentences)} test sentences")

    # Run translations
    print(f"\nTranslating (excluding test sentences from corpus)...")
    results = []

    for i, test in enumerate(test_sentences, 1):
        line_num = int(test['line_num'])
        rus_text = test['rus_original'].strip()
        kbd_original = normalize_kbd(test['kbd_original'])

        # Translate using LLM approach (exclude test sentence from corpus)
        result = translate_with_llm_approach(rus_text, corpus, exclude_line=line_num)

        kbd_translated = normalize_kbd(result['translation']) if result['translation'] else ''

        # Calculate similarity with original
        similarity = calculate_similarity(kbd_original, kbd_translated) if kbd_translated else 0.0

        # Store result
        results.append({
            'line_num': line_num,
            'rus_original': rus_text,
            'kbd_original': kbd_original,
            'kbd_translated': kbd_translated,
            'translation_method': result['method'],
            'confidence': f"{result['confidence']:.3f}",
            'similarity': f"{similarity:.3f}",
            'matches_found': result['matches_found'],
            'exact_match': 'YES' if similarity >= 0.95 else 'NO'
        })

        if i % 10 == 0:
            print(f"  Processed {i}/{len(test_sentences)} sentences...")

    # Save results
    print(f"\nSaving results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['line_num', 'rus_original', 'kbd_original', 'kbd_translated',
                     'translation_method', 'confidence', 'similarity', 'matches_found', 'exact_match']
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
    methods = Counter(r['translation_method'] for r in results)

    print(f"\nTotal test sentences: {total}")
    print(f"Exact matches (similarity ≥ 0.95): {exact_matches} ({exact_matches/total*100:.1f}%)")
    print(f"No translation found: {no_translation} ({no_translation/total*100:.1f}%)")

    if similarities:
        print(f"\nSimilarity scores (with original):")
        print(f"  Mean: {sum(similarities)/len(similarities):.3f}")
        print(f"  Min: {min(similarities):.3f}")
        print(f"  Max: {max(similarities):.3f}")
        print(f"  Median: {sorted(similarities)[len(similarities)//2]:.3f}")

        # Buckets
        high_sim = sum(1 for s in similarities if s >= 0.8)
        medium_sim = sum(1 for s in similarities if 0.5 <= s < 0.8)
        low_sim = sum(1 for s in similarities if s < 0.5)

        print(f"\nSimilarity distribution:")
        print(f"  High (≥0.8): {high_sim} ({high_sim/total*100:.1f}%)")
        print(f"  Medium (0.5-0.8): {medium_sim} ({medium_sim/total*100:.1f}%)")
        print(f"  Low (<0.5): {low_sim} ({low_sim/total*100:.1f}%)")

    print(f"\nConfidence scores:")
    print(f"  Mean: {sum(confidences)/len(confidences):.3f}")

    print(f"\nTranslation methods:")
    for method, count in methods.most_common():
        print(f"  {method}: {count} ({count/total*100:.1f}%)")

    # Show examples
    print("\n" + "=" * 80)
    print("EXAMPLE TRANSLATIONS")
    print("=" * 80)

    # Show best, worst, and medium examples
    results_sorted = sorted([r for r in results if r['kbd_translated']],
                           key=lambda x: float(x['similarity']))

    if results_sorted:
        print("\n=== WORST MATCH ===")
        worst = results_sorted[0]
        print(f"Line {worst['line_num']} | Similarity: {worst['similarity']} | Method: {worst['translation_method']}")
        print(f"RUS: {worst['rus_original'][:120]}...")
        print(f"KBD (expected): {worst['kbd_original'][:120]}...")
        print(f"KBD (got):      {worst['kbd_translated'][:120]}...")

        if len(results_sorted) > 1:
            print("\n=== MEDIUM MATCH ===")
            medium = results_sorted[len(results_sorted)//2]
            print(f"Line {medium['line_num']} | Similarity: {medium['similarity']} | Method: {medium['translation_method']}")
            print(f"RUS: {medium['rus_original'][:120]}...")
            print(f"KBD (expected): {medium['kbd_original'][:120]}...")
            print(f"KBD (got):      {medium['kbd_translated'][:120]}...")

        print("\n=== BEST MATCH ===")
        best = results_sorted[-1]
        print(f"Line {best['line_num']} | Similarity: {best['similarity']} | Method: {best['translation_method']}")
        print(f"RUS: {best['rus_original'][:120]}...")
        print(f"KBD (expected): {best['kbd_original'][:120]}...")
        print(f"KBD (got):      {best['kbd_translated'][:120]}...")

    print("\n" + "=" * 80)
    print(f"✓ Full results saved to: {OUTPUT_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()
