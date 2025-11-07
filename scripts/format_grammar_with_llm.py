#!/usr/bin/env python3
"""
LLM-powered grammar documentation formatter.
Uses Claude API to intelligently reformat poorly formatted text extracts.
"""

import os
import re
import time
from pathlib import Path
from typing import Optional

import anthropic


# Formatting prompt for Claude
FORMATTING_PROMPT = """Ты эксперт по форматированию академических текстов. Тебе дан плохо отформатированный фрагмент из грамматики кабардинского языка.

ТВОЯ ЗАДАЧА:
1. Убрать артефакты извлечения:
   - Номера строк со стрелками (1→, 2→, 100→ и т.д.)
   - Номера страниц, вставленные в текст
   - Лишние пробелы и разрывы

2. Добавить структуру Markdown:
   - Заголовки разделов (##, ###, ####)
   - Разделы типа "8. Глагол" → ## 8. Глагол
   - Подразделы "8.1. Подраздел" → ### 8.1. Подраздел

3. Форматировать таблицы:
   - Обрамить в ```
   - Сохранить структуру и выравнивание как можно лучше
   - Если таблица сломана - постарайся восстановить

4. Сохранить специальные элементы:
   - Кабардинские символы (Ӏ, I, ъ, ь и др.) - оставь БЕЗ изменений
   - Морфемные разборы (префикс+корень+суффикс)
   - Все примеры на кабардинском и русском
   - Лингвистические термины и обозначения

5. Улучшить читаемость:
   - Добавить пустые строки между абзацами
   - Выделить примеры если нужно
   - Списки оформить через дефисы или цифры

ВАЖНО:
- НЕ изменяй содержание, только форматирование
- НЕ переводи и не исправляй язык
- СОХРАНИ все кабардинские примеры точно как есть
- Если что-то непонятно - оставь как есть, не выдумывай

Верни ТОЛЬКО отформатированный текст в Markdown, без дополнительных комментариев.
"""


def extract_metadata(filename: str) -> tuple[str, str]:
    """Extract chunk number and page range from filename."""
    match = re.search(r'chunk_(\d+)_pages_(\d+-\d+)', filename)
    if match:
        return match.group(1), match.group(2)
    return "", ""


def format_with_claude(
    content: str,
    client: anthropic.Anthropic,
    chunk_num: str,
    pages: str,
    max_retries: int = 3
) -> Optional[str]:
    """Format content using Claude API with retries."""

    for attempt in range(max_retries):
        try:
            message = client.messages.create(
                model="claude-sonnet-4-20250514",  # Using latest Sonnet
                max_tokens=16000,
                temperature=0,  # Deterministic for formatting
                messages=[
                    {
                        "role": "user",
                        "content": f"{FORMATTING_PROMPT}\n\n---\n\nФРАГМЕНТ (Chunk {chunk_num}, Pages {pages}):\n\n{content}"
                    }
                ]
            )

            formatted_text = message.content[0].text

            # Add metadata header
            header = f"""# Chunk {chunk_num}: Pages {pages}

*Source: Kabardian-Circassian Grammar Reference*
*Formatted with Claude AI*

---

"""
            return header + formatted_text

        except anthropic.RateLimitError:
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"    Rate limit hit, waiting {wait_time}s...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"    Error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                return None

    return None


def process_file(
    input_path: Path,
    output_path: Path,
    client: anthropic.Anthropic,
    dry_run: bool = False
) -> bool:
    """Process a single grammar file."""

    # Extract metadata
    chunk_num, pages = extract_metadata(input_path.name)

    # Read original content
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check size
    size_kb = len(content.encode('utf-8')) / 1024
    print(f"  Chunk {chunk_num} (pages {pages}) - {size_kb:.1f} KB")

    if dry_run:
        print(f"    [DRY RUN] Would format and save to {output_path.name}")
        return True

    # Format with Claude
    formatted = format_with_claude(content, client, chunk_num, pages)

    if formatted:
        # Write formatted content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        print(f"    ✓ Saved to {output_path.name}")
        return True
    else:
        print(f"    ✗ Failed to format")
        return False


def main():
    """Main function to process all grammar files."""

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export ANTHROPIC_API_KEY='your-api-key'")
        return

    # Initialize client
    client = anthropic.Anthropic(api_key=api_key)

    # Define paths
    grammar_dir = Path(__file__).parent.parent / "references" / "grammar"

    # Find all txt files in subdirectories
    txt_files = sorted(grammar_dir.glob("*/chunk_*.txt"))

    if not txt_files:
        print("No files found to process!")
        return

    print(f"🔍 Found {len(txt_files)} files to process\n")

    # Ask for confirmation
    print("This will:")
    print(f"  - Process {len(txt_files)} files using Claude API")
    print(f"  - Estimated cost: ~${len(txt_files) * 0.05:.2f} (rough estimate)")
    print(f"  - Estimated time: ~{len(txt_files) * 5 / 60:.0f} minutes")
    print()

    response = input("Continue? [y/N/test]: ").strip().lower()

    if response == 'test':
        # Test mode - process first 3 files
        txt_files = txt_files[:3]
        print(f"\n🧪 TEST MODE: Processing first {len(txt_files)} files\n")
    elif response != 'y':
        print("Cancelled.")
        return

    # Process each file
    success_count = 0
    failed_files = []

    print("\n" + "="*60)
    print("Starting processing...")
    print("="*60 + "\n")

    for i, txt_file in enumerate(txt_files, 1):
        print(f"[{i}/{len(txt_files)}] {txt_file.parent.name}/{txt_file.name}")

        # Create output path (change .txt to .md)
        output_file = txt_file.with_suffix('.md')

        try:
            if process_file(txt_file, output_file, client):
                success_count += 1
            else:
                failed_files.append(txt_file.name)

            # Rate limiting: wait between requests
            if i < len(txt_files):
                time.sleep(1)  # 1 second between files

        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            break
        except Exception as e:
            print(f"    ✗ Unexpected error: {e}")
            failed_files.append(txt_file.name)

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✓ Successfully processed: {success_count}/{len(txt_files)}")

    if failed_files:
        print(f"✗ Failed: {len(failed_files)}")
        print("\nFailed files:")
        for fname in failed_files:
            print(f"  - {fname}")

    print("\n💡 Next steps:")
    print("1. Review the generated .md files")
    print("2. Check a few files manually for quality")
    print("3. If satisfied, you can remove .txt files")
    print("4. Update README.md to reflect new format")


if __name__ == "__main__":
    main()
