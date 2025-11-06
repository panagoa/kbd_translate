# Agent Skills Best Practices

> Извлечение ключевых практик и принципов от Anthropic из официальной документации, статей и cookbook.

## Что такое Agent Skills

**Skills** — это организованные папки с инструкциями, скриптами и ресурсами, которые агенты могут обнаруживать и загружать динамически для лучшего выполнения конкретных задач.

**Skills расширяют возможности Claude, упаковывая вашу экспертизу в композируемые ресурсы**, превращая универсальные агенты в специализированные агенты, которые соответствуют вашим потребностям.

### Отличие от промптов

- **Промпты** — инструкции уровня разговора для одноразовых задач
- **Skills** — загружаются по требованию и исключают необходимость повторно предоставлять одинаковые указания в разных разговорах

---

## Progressive Disclosure Architecture

**Progressive Disclosure** — основной принцип дизайна, который делает Agent Skills гибкими и масштабируемыми.

Как хорошо организованное руководство, которое начинается с оглавления, затем конкретных глав и, наконец, подробного приложения, skills позволяют Claude загружать информацию только по мере необходимости.

### Три уровня загрузки

| Уровень | Когда загружается | Стоимость токенов | Содержимое |
|---------|-------------------|-------------------|------------|
| **Level 1: Metadata** | Всегда (при старте агента) | ~100 токенов на skill | `name` и `description` из YAML frontmatter |
| **Level 2: Instructions** | Когда skill активируется | <5k токенов | Тело SKILL.md с инструкциями |
| **Level 3+: Resources** | По необходимости | Без лимитов | Дополнительные файлы, код, шаблоны |

### Level 1: Metadata (всегда загружены)

YAML frontmatter предоставляет информацию для обнаружения:

```yaml
---
name: PDF Processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
---
```

Claude загружает эти метаданные при старте и включает их в system prompt. **Облегчённый подход позволяет устанавливать множество skills без штрафа по контексту** — Claude знает только то, что каждый skill существует и когда его использовать.

### Level 2: Instructions (загружаются при активации)

Основное тело SKILL.md содержит процедурные знания: workflow, best practices, guidance:

````markdown
# PDF Processing

## Quick start
Use pdfplumber to extract text from PDFs:

```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced form filling, see [FORMS.md](FORMS.md).
````

Когда запрос соответствует описанию skill, Claude читает SKILL.md из файловой системы. **Только тогда этот контент входит в контекстное окно.**

### Level 3+: Resources and Code (по необходимости)

Skills могут объединять дополнительные материалы:

```
pdf-skill/
├── SKILL.md          # Основные инструкции
├── FORMS.md          # Руководство по заполнению форм
├── REFERENCE.md      # Детальная справка API
└── scripts/
    └── fill_form.py  # Utility скрипт
```

**Типы Level 3+ ресурсов:**

- **Instructions:** Дополнительные markdown файлы со специализированными руководствами
- **Code:** Исполняемые скрипты, которые Claude запускает через bash; код выполняется **без загрузки в контекст**
- **Resources:** Справочные материалы (database schemas, API docs, templates, examples)

Claude получает доступ к этим файлам **только когда на них ссылаются**.

### Преимущества Progressive Disclosure

✅ **On-demand file access:** Claude читает только нужные файлы. Skill может включать десятки справочных файлов, но если задача требует только один — только он и загрузится.

✅ **Эффективное выполнение кода:** Когда Claude запускает скрипт, код никогда не загружается в контекст. Только вывод скрипта потребляет токены.

✅ **Нет практического лимита на контент:** Skills могут включать comprehensive API documentation, большие datasets, extensive examples. Нет штрафа по контексту за неиспользуемый контент.

---

## Структура Skill

### Минимальный skill

Каждый skill требует файл `SKILL.md` с YAML frontmatter:

```yaml
---
name: Your Skill Name
description: Brief description of what this skill does and when to use it
---

# Your Skill Name

## Instructions
[Clear, step-by-step guidance for Claude to follow]

## Examples
[Concrete examples of using this skill]
```

**Обязательные поля:** `name` и `description`

### Ограничения frontmatter

- **name:** максимум 64 символа
- **description:** максимум 1024 символа

### Дополнительные поля

- **allowed-tools:** (опционально) список разрешённых tools для безопасности

```yaml
---
name: kb-bash-expert
description: Expert in running bash commands for KB project...
allowed-tools: Bash, Read, Glob
---
```

---

## Как писать name и description

### Name

✅ **Информативный:** должно быть ясно, что делает skill
✅ **Короткий:** максимум 64 символа
✅ **Уникальный:** отличается от других skills

**Примеры:**
- `pdf-processor` ✅
- `financial-analyzer` ✅
- `skill123` ❌ (неинформативно)

### Description

**Description — самый важный элемент**. Claude использует его при принятии решения о том, активировать ли skill.

**Description должно включать ДВА компонента:**

1. **ЧТО делает skill** (capabilities)
2. **КОГДА Claude должен его использовать** (triggers)

#### ✅ Хороший description

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**Почему хорошо:**
- ✅ Ясно описывает возможности
- ✅ Содержит триггеры ("Use when...")
- ✅ Перечисляет ключевые слова ("PDFs", "forms", "extraction")

#### ❌ Плохой description

```yaml
description: Handles PDF operations.
```

**Почему плохо:**
- ❌ Слишком общо ("operations")
- ❌ Нет триггеров активации
- ❌ Непонятно когда использовать

#### Формула для хорошего description

```
[ЧТО делает]. [Use when | Activates when | Use for] [триггерные сценарии] [or when user mentions] [ключевые слова].
```

**Примеры:**

```yaml
# Translation Processor
description: Process web articles into structured notes with translation and proper frontmatter. Activates when user provides URLs, mentions "translate article", "save article", or wants to create notes from web content.

# KB Bash Expert
description: Expert in running bash commands for Obsidian KB project. Knows project structure and absolute paths. Activates when executing bash commands, running python scripts, or mentions "run script", "execute", "migration".
```

---

## Рекомендации по разработке Skills

### 1. Начните с оценки

**Определите конкретные пробелы в возможностях ваших агентов**, запуская их на репрезентативных задачах и наблюдая, где они испытывают трудности или требуют дополнительного контекста.

❌ Не создавайте skills "на всякий случай"
✅ Создавайте skills для устранения конкретных недостатков

### 2. Структурируйте для масштабирования

**Когда файл SKILL.md становится громоздким:**
- Разделите его содержимое на отдельные файлы
- Ссылайтесь на них из основного SKILL.md

**Если определенные контексты взаимоисключающие:**
- Сохранение путей раздельными уменьшит использование токенов
- Пример: `FORMS.md` отдельно от основного `SKILL.md`

**Код может служить как исполняемыми инструментами, так и документацией:**
- Должно быть ясно, должен ли Claude запускать скрипты напрямую или читать их как справочные материалы
- Используйте комментарии и структуру директорий для ясности

### 3. Думайте с точки зрения Claude

**Отслеживайте, как Claude использует ваш skill в реальных сценариях:**
- Следите за неожиданными траекториями
- Следите за чрезмерной зависимостью от определенных контекстов

**Обратите особое внимание на name и description:**
- Claude будет использовать их при принятии решения о том, активировать ли skill в ответ на текущую задачу

**Пишите инструкции для LLM, а не для людей:**
- Будьте конкретны и однозначны
- Используйте примеры вместо абстрактных описаний
- Структурируйте пошагово

### 4. Итерируйте с Claude

**Когда вы работаете над задачей с Claude:**
- Попросите Claude зафиксировать его успешные подходы в skill
- Попросите Claude документировать распространенные ошибки

**Если Claude сбивается с пути:**
- Попросите его провести саморефлексию о том, что пошло не так
- Этот процесс поможет вам обнаружить, какой контекст на самом деле нужен Claude

❌ Не пытайтесь предугадать нужный контекст заранее
✅ Обнаруживайте нужный контекст через итерации с Claude

---

## Skills и выполнение кода

Skills могут включать код для выполнения Claude в качестве инструментов по его усмотрению.

### Когда использовать код

**LLM превосходны во многих задачах**, но определенные операции лучше подходят для традиционного выполнения кода:

- **Детерминированные операции:** Сортировка, парсинг, валидация
- **Вычисления:** Математические операции, статистика
- **Производительность:** Операции, которые дороги через генерацию токенов

### Преимущества кода в skills

✅ **Детерминированная надежность:** Код обеспечивает последовательное и воспроизводимое поведение
✅ **Эффективность:** Алгоритмы выполняются быстрее и дешевле
✅ **Нет потребления контекста:** Скрипты выполняются без загрузки в контекст

### Пример

```
pdf-skill/
├── SKILL.md
└── scripts/
    └── extract_form_fields.py
```

**В SKILL.md:**

```markdown
## Extracting form fields

To extract all form fields from a PDF, run:

```bash
python scripts/extract_form_fields.py input.pdf
```

This script reads the PDF and outputs JSON with all field names and values.
```

Claude может запустить этот скрипт **без загрузки ни скрипта, ни PDF в контекст**.

---

## Security Considerations

**⚠️ Критически важно:** Используйте skills только из доверенных источников — те, что создали сами или получили от Anthropic.

### Ключевые риски

**Skills предоставляют Claude новые возможности через инструкции и код.** Вредоносный skill может направить Claude на:

- ❌ **Tool misuse:** Вызов tools (file operations, bash) вредоносными способами
- ❌ **Data exposure:** Утечка sensitive данных во внешние системы
- ❌ **Malicious instructions:** Инструкции, заставляющие Claude действовать непредусмотренно

### Рекомендации

✅ **Audit thoroughly:** Проверяйте все файлы в skill перед использованием
✅ **Проверяйте зависимости:** Code dependencies и bundled resources
✅ **Внимание к внешним источникам:** Skills, которые обращаются к внешним URL, особо опасны

### Использование allowed-tools

Ограничьте возможности skill через `allowed-tools`:

```yaml
---
name: safe-reader
description: Reads and analyzes files safely
allowed-tools: Read, Glob
---
```

**Этот skill может:**
- ✅ Читать файлы
- ✅ Искать файлы по паттернам

**Этот skill НЕ может:**
- ❌ Редактировать файлы (нет Edit/Write)
- ❌ Выполнять bash команды (нет Bash)

---

## Performance Tips

### 1. Используйте Progressive Disclosure эффективно

- Держите SKILL.md компактным (основные инструкции)
- Выносите детальную справку в отдельные файлы
- Ссылайтесь на файлы явно когда они нужны

### 2. Разделяйте взаимоисключающие контексты

Если skill обрабатывает несколько сценариев, которые редко используются вместе:

```
skill/
├── SKILL.md              # Общие инструкции
├── scenario_a.md         # Сценарий А
└── scenario_b.md         # Сценарий Б
```

Claude загрузит только нужный сценарий.

### 3. Выносите тяжелые операции в код

Вместо:
```markdown
Generate 100 random numbers, sort them, calculate mean and standard deviation...
```

Лучше:
```markdown
Run: `python scripts/stats.py --samples 100`
```

---

## Где работают Skills

### Claude API
- Поддерживает предустановленные и custom skills
- Custom skills загружаются через Skills API
- Доступны на уровне workspace (organization-wide)

### Claude Code
- Поддерживает только custom skills
- Skills базируются на файловой системе (`.claude/skills/`)
- Персональные или на уровне проекта

### Claude.ai
- Поддерживает предустановленные и custom skills
- Custom skills загружаются как zip файлы
- ⚠️ Индивидуальны для каждого пользователя (не shared)

---

## Ключевые принципы (резюме)

1. **Progressive Disclosure** — основа архитектуры skills
   - Level 1: Metadata (всегда)
   - Level 2: Instructions (при активации)
   - Level 3+: Resources (по необходимости)

2. **Description — самый важный элемент**
   - Включай ЧТО делает + КОГДА активировать
   - Добавляй триггерные фразы

3. **Структурируйте для масштабирования**
   - Разделяйте большие SKILL.md
   - Выносите взаимоисключающие контексты

4. **Думайте с точки зрения Claude**
   - Пишите инструкции для LLM
   - Наблюдайте как Claude использует skill
   - Итерируйте на основе наблюдений

5. **Security First**
   - Используйте только доверенные skills
   - Audit thoroughly перед использованием
   - Используйте allowed-tools для ограничений

6. **Итерируйте с Claude**
   - Не предугадывайте контекст
   - Обнаруживайте через практику
   - Документируйте успешные подходы

---

**Источники:** Anthropic Engineering Blog, Agent Skills Documentation, Claude Cookbooks
