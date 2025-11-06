# Список ошибок, найденных в GRAMMAR_REFERENCE_GUIDE.md

## Критические ошибки (требуют немедленного исправления)

### 1. TAM System - Perfect II форма (line 285)
**Текущее:**
```
- Perfect II: с-ы-кIуэ-рт "I had gone" ← remote past -рт
```

**Должно быть:**
```
- Perfect II: с-ы-кIуа-т "I had gone (then)" ← Perfect I + -т marker
- Imperfect: с-ы-кIуэ-т "I was going" ← Imperfect stem + -т
```

**Источник:** chunk_033_pages_161-165.txt, line 51, 167
- сы-кIуэ-рт описывает IMPERFECT, а не Perfect II
- сыкIуат - правильная форма Perfect II

---

### 2. Mood System - Conditional форма (line 299)
**Текущее:**
```
Conditional:    с-ы-кIуэ-н "I would go" (hypothetical)
```

**Должно быть:**
```
Conditional:    с-ы-кIуэ-мэ "if I go" (hypothetical condition)
Conjunctive:    с-ы-кIуэ-нт "I would go" (subjunctive)
```

**Источник:** chunk_034_pages_166-170.txt, lines 226-233, 261
- с-ы-кIуэ-н-щ это FUTURE I, а не conditional
- Conditional использует -мэ суффикс
- Conjunctive/Subjunctive использует -нт суффикс

---

### 3. Mood System - Conjunctive форма (line 301)
**Текущее:**
```
Conjunctive:    с-ы-кIуэ-рэ "I may have gone" (uncertain)
```

**Проблема:** Форма unclear/unverified в источниках

**Рекомендация:** Заменить на проверенную форму с -нт или удалить

---

### 4. Postpositions - Все примеры не найдены (lines 547-564)
**Текущие примеры НЕ НАЙДЕНЫ в chunk_053:**
- гъун "near": унэм гъунэ-р "near the house"
- мыш "over/above": унэм мыш-щ "over the house"
- хьэ "below": унэм хьэ-у "below the house"
- фэ "in/inside": унэм фэ-м "inside the house"

**Должны быть заменены на ПРОВЕРЕННЫЕ послелоги из chunk_053:**
- деж/дей "у, от, около, возле" ("at, from, near")
- щыщ "из" ("from, out of")
- щхьэкIэ "для, ради, из-за" ("for, because of")
- папщIэ "для, ради, о" ("for, about")
- нэгъунэ "до, вплоть до" ("up to")
- пщIондэ "до" ("until")

**Источник:** chunk_053_pages_261-265.txt, lines 232-286

---

### 5. SOV Word Order Example - не найден (lines 636-638)
**Текущее:**
```
Kabardian (SOV): Сэ унэр сыплъ     Subject-Object-Verb
                 I  house see
```

**Проблема:** Этот конкретный пример НЕ НАЙДЕН в syntax chunks

**Проверенные альтернативы из chunk_074:**
```
ЩIалэм тхылъыр иджынущ – «Парень книгу прочтет»
(Boy-the book-the will-read)
```

**Или:**
```
Сэ уэ дыгъуасэ услъэгъуащ – «Я тебя вчера видел»
(I you yesterday saw)
```

**Источник:** chunk_074_pages_366-370.txt, lines 51, 219

---

## Средние ошибки (желательно исправить)

### 6. Adverbs - Temporal adverb "джыри" (line 472)
**Текущее:**
```
- Root adverbs: джыри "now", пщэдей "yesterday", нобэ "today"
```

**Должно быть:**
```
- Root adverbs: иджыри "now/still", пщэдей "yesterday", нобэ "today"
```

**Источник:** chunk_050, chunk_051, chunk_052
- Везде встречается "иджыри" (с префиксом и-), а не "джыри"

---

### 7. Adverbs - Spatial adverbs (lines 477-478)
**Текущее:**
```
- Location: мыдрэ "here", ардрэ "there", дэнэ "where"
```

**Должно быть:**
```
- Location: мыдэ "here/hither", модэ "there/thither", дэнэ "where"
```

**Источник:** chunk_051_pages_251-255.txt, lines 137-138
- "мыдэ «сюда»" (not мыдрэ)
- "модэ «там, туда»" (not ардрэ)

---

## Структурные наблюдения (не ошибки, но важно знать)

### 8. Overlapping chunks (правильно, но стоит отметить)
**chunk_020** существует в двух каталогах:
- adjectives/chunk_020_pages_96-100.txt
- numerals/chunk_020_pages_96-100.txt

**chunk_044** существует в двух каталогах:
- advanced_verbs/chunk_044_pages_216-220.txt
- verbal_derivations/chunk_044_pages_216-220.txt

Это ПРАВИЛЬНО - chunks на границах разделов дублируются для полноты контекста.

---

### 9. Total file count verification
**Документ claims:** 79 files

**Actual count:**
- phonetics: 4 files
- morphology_intro: 2 files
- nouns: 5 files
- adjectives: 4 files
- numerals: 3 files
- verb_morphology: 8 files
- advanced_verbs: 14 files
- verbal_derivations: 6 files
- adverbs: 2 files
- function_words: 4 files
- syntax: 25 files

**Total unique files:** 77 files (не 79!)
- Если учесть 2 overlapping chunks (020, 044), то: 77 + 2 = 79 ✓

---

### 10. Размеры файлов verification
**Документ claims:** ~2.74MB

**Actual size:** 2.8M (du -sh output)

Разница: ~60KB - в пределах нормы (округление, метаданные)

---

## Данные файлы - verification

### Translation corpus (sents_292k.csv)
**Документ claims:** 45MB, ~292,000 pairs
**Actual:** 45M, 292,458 lines ✓ CORRECT

### Rus-Ady dictionary
**Документ claims:** 3.4MB, ~15,989 entries
**Actual:** 3.4M, 15,989 lines ✓ CORRECT

### Ady-Ady dictionary
**Документ claims:** 15MB, ~98,412 entries
**Actual:** 15M, 98,412 lines ✓ CORRECT

### Sentences corpus
**Документ claims:** ~7.3MB
**Actual:** 7.0M ✓ CORRECT (minor rounding)

---

## Рекомендации по исправлению

### Приоритет 1 (CRITICAL - исправить обязательно):
1. ✅ Исправить Perfect II форму (line 285)
2. ✅ Исправить Conditional форму (line 299)
3. ✅ Заменить все примеры послелогов (lines 547-564)
4. ✅ Заменить SOV example (lines 636-638)

### Приоритет 2 (IMPORTANT - исправить желательно):
5. ✅ Исправить "джыри" → "иджыри" (line 472)
6. ✅ Исправить "мыдрэ" → "мыдэ", "ардрэ" → "модэ" (lines 477-478)

### Приоритет 3 (NICE TO HAVE):
7. Добавить примечание об overlapping chunks
8. Добавить ссылки на источники (chunk numbers) для всех примеров

---

## Итоговая статистика проверки

**Проверено разделов:** 11/11 (100%)
**Найдено критических ошибок:** 5
**Найдено средних ошибок:** 2
**Подтверждено правильных данных:** 4 (file sizes, counts)

**Общая оценка точности документа:** ~85%
- Структура: ✓ Правильная
- Размеры файлов: ✓ Правильные
- Примеры глаголов: ⚠ Частично неверные (TAM, mood)
- Примеры послелогов: ✗ Неверные (не найдены)
- Примеры наречий: ⚠ Частично неверные (мелкие опечатки)

---

**Дата проверки:** 2025-11-07
**Проверено агентами:** Explore (sonnet), Human verification
**Методология:** Grep search + Read chunks + cross-reference with source files
