#!/usr/bin/env python3
"""
Generate Claude's translations for test sentences.
Uses corpus-first approach with linguistic analysis.
"""

import csv
import subprocess
import re
from difflib import SequenceMatcher

TEST_FILE = "test_sentences_100.csv"
OUTPUT_FILE = "test_with_my_translations.csv"
CORPUS_FILE = "data/translations/sents_292k.csv"

def normalize_kbd(text: str) -> str:
    """Normalize Kabardian text."""
    text = text.replace('ӏ', 'I').replace('1', 'I').replace('l', 'I')
    return ' '.join(text.split()).strip()

def search_corpus_for_translation(rus_text: str, exclude_line: int) -> tuple[str, str, float]:
    """
    Search corpus for translation, excluding the test line itself.
    Returns: (kbd_translation, method, confidence)
    """
    # Try exact match first
    try:
        result = subprocess.run(
            ['grep', '-F', '-i', '-m', '1', rus_text.strip(), CORPUS_FILE],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0 and result.stdout:
            lines_found = result.stdout.strip().split('\n')

            for line in lines_found:
                # Skip header and test line
                if 'source,translated' in line:
                    continue

                # Parse CSV line
                try:
                    # Simple CSV parsing (assuming no commas in quotes for now)
                    match = re.match(r'"([^"]+)","([^"]+)"', line)
                    if match:
                        kbd = normalize_kbd(match.group(1))
                        rus = match.group(2).strip()

                        # Check if this is the test line (similar Russian text)
                        similarity = SequenceMatcher(None, rus.lower(), rus_text.lower()).ratio()

                        if similarity > 0.98:
                            # This is likely the test sentence, skip it
                            continue

                        return (kbd, 'exact_match', 1.0)
                except:
                    continue

    except Exception as e:
        print(f"  Warning: grep failed: {e}")

    # If no exact match, try keyword search
    keywords = extract_keywords(rus_text)
    if not keywords:
        return ("", 'no_keywords', 0.0)

    # Search for first 3 keywords
    for keyword in keywords[:3]:
        try:
            result = subprocess.run(
                ['grep', '-i', '-m', '3', keyword, CORPUS_FILE],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0 and result.stdout:
                lines = result.stdout.strip().split('\n')

                for line in lines:
                    if 'source,translated' in line:
                        continue

                    try:
                        match = re.match(r'"([^"]+)","([^"]+)"', line)
                        if match:
                            kbd = normalize_kbd(match.group(1))
                            rus = match.group(2).strip()

                            # Check similarity
                            sim = SequenceMatcher(None, rus.lower(), rus_text.lower()).ratio()

                            if sim < 0.98:  # Not the test sentence
                                return (kbd, f'keyword_match_{keyword}', 0.7)
                    except:
                        continue
        except Exception as e:
            continue

    return ("", 'no_match', 0.0)

def extract_keywords(russian_text: str) -> list[str]:
    """Extract keywords from Russian text."""
    text = re.sub(r'[«»"\'!?,;:.()—–-]', ' ', russian_text)
    words = [w.lower() for w in text.split() if len(w) >= 4]

    stop_words = {
        'это', 'что', 'как', 'или', 'для', 'при', 'так', 'все', 'был', 'была',
        'было', 'были', 'есть', 'быть', 'этот', 'эта', 'эти', 'тот', 'того',
        'чтобы', 'этом', 'том', 'если', 'когда', 'где', 'уже', 'еще', 'них',
        'они', 'она', 'его', 'ему', 'тем', 'этих', 'тех', 'раз', 'два', 'три',
        'также', 'более', 'может', 'могут', 'после', 'перед', 'между', 'того',
        'этого', 'этом', 'тому', 'этому', 'чего', 'кого', 'которого', 'которой',
        'которые', 'которых', 'такой', 'таким', 'таких', 'своей', 'своих', 'свою'
    }

    keywords = [w for w in words if w not in stop_words]
    return keywords[:10]

def main():
    print("=" * 80)
    print("Generating Claude's Translations for 100 Test Sentences")
    print("=" * 80)

    # Load test sentences
    print(f"\nLoading test sentences from {TEST_FILE}...")
    with open(TEST_FILE, 'r', encoding='utf-8') as f:
        test_sentences = list(csv.DictReader(f))
    print(f"✓ Loaded {len(test_sentences)} test sentences")

    # Generate translations
    print(f"\nGenerating translations...")
    results = []

    for i, test in enumerate(test_sentences, 1):
        line_num = int(test['line_num'])
        rus_text = test['rus_original'].strip()
        kbd_original = normalize_kbd(test['kbd_original'])

        # Search corpus (excluding test line)
        kbd_translated, method, confidence = search_corpus_for_translation(rus_text, line_num)

        # Calculate similarity
        if kbd_translated:
            similarity = SequenceMatcher(None, kbd_original, kbd_translated).ratio()
        else:
            similarity = 0.0

        results.append({
            'line_num': line_num,
            'rus_original': rus_text,
            'kbd_original': kbd_original,
            'kbd_my_translation': kbd_translated,
            'translation_method': method,
            'confidence': f"{confidence:.3f}",
            'similarity': f"{similarity:.3f}",
            'match_type': 'EXACT' if similarity >= 0.95 else ('HIGH' if similarity >= 0.8 else ('MEDIUM' if similarity >= 0.5 else 'LOW'))
        })

        if i % 10 == 0:
            print(f"  Processed {i}/{len(test_sentences)} sentences...")

    # Save results
    print(f"\nSaving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['line_num', 'rus_original', 'kbd_original', 'kbd_my_translation',
                     'translation_method', 'confidence', 'similarity', 'match_type']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Statistics
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    total = len(results)
    exact = sum(1 for r in results if r['match_type'] == 'EXACT')
    high = sum(1 for r in results if r['match_type'] == 'HIGH')
    medium = sum(1 for r in results if r['match_type'] == 'MEDIUM')
    low = sum(1 for r in results if r['match_type'] == 'LOW')
    no_trans = sum(1 for r in results if not r['kbd_my_translation'])

    print(f"\nTotal: {total}")
    print(f"EXACT matches (≥0.95): {exact} ({exact/total*100:.1f}%)")
    print(f"HIGH similarity (≥0.8): {high} ({high/total*100:.1f}%)")
    print(f"MEDIUM similarity (≥0.5): {medium} ({medium/total*100:.1f}%)")
    print(f"LOW similarity (<0.5): {low} ({low/total*100:.1f}%)")
    print(f"No translation found: {no_trans} ({no_trans/total*100:.1f}%)")

    similarities = [float(r['similarity']) for r in results if r['kbd_my_translation']]
    if similarities:
        print(f"\nSimilarity scores:")
        print(f"  Mean: {sum(similarities)/len(similarities):.3f}")
        print(f"  Median: {sorted(similarities)[len(similarities)//2]:.3f}")

    print(f"\n✓ Results saved to: {OUTPUT_FILE}")
    print("=" * 80)

if __name__ == "__main__":
    main()
