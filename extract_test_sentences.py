#!/usr/bin/env python3
"""Extract 100 random complex sentences from the translation corpus for testing."""

import csv
import random
from pathlib import Path

# Configuration
INPUT_FILE = "data/translations/sents_292k.csv"
OUTPUT_FILE = "test_sentences_100.csv"
MIN_LENGTH = 100  # Minimum length of Russian text
NUM_SENTENCES = 100
RANDOM_SEED = 42  # For reproducibility

def main():
    print(f"Reading {INPUT_FILE}...")

    # Read all sentences and filter by length
    complex_sentences = []

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            kbd_text = row['source']
            rus_text = row['translated']

            # Filter: Russian text should be > MIN_LENGTH characters
            if len(rus_text) > MIN_LENGTH:
                complex_sentences.append({
                    'line_num': i + 1,  # +1 for header
                    'kbd_original': kbd_text,
                    'rus_original': rus_text,
                    'rus_length': len(rus_text)
                })

            if i % 50000 == 0:
                print(f"  Processed {i:,} lines, found {len(complex_sentences):,} complex sentences...")

    print(f"\nFound {len(complex_sentences):,} complex sentences (Russian text > {MIN_LENGTH} chars)")

    # Randomly select NUM_SENTENCES
    random.seed(RANDOM_SEED)
    selected = random.sample(complex_sentences, min(NUM_SENTENCES, len(complex_sentences)))

    # Sort by line number for easier reference
    selected.sort(key=lambda x: x['line_num'])

    # Save to output file
    print(f"\nSaving {len(selected)} test sentences to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['line_num', 'kbd_original', 'rus_original', 'rus_length', 'kbd_translated', 'match_score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(selected)

    # Print statistics
    lengths = [s['rus_length'] for s in selected]
    print(f"\nStatistics of selected sentences:")
    print(f"  Count: {len(selected)}")
    print(f"  Russian text length:")
    print(f"    Min: {min(lengths)}")
    print(f"    Max: {max(lengths)}")
    print(f"    Avg: {sum(lengths) / len(lengths):.1f}")
    print(f"    Median: {sorted(lengths)[len(lengths)//2]}")

    print(f"\n✓ Test file created: {OUTPUT_FILE}")
    print(f"  Use this file to test kbd-translator skill")

if __name__ == "__main__":
    main()
