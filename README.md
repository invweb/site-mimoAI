# MiMo AI — Тестовый сайт / MiMo AI — Test Site

Динамический сайт на Python Flask, созданный с помощью AI-ассистента MiMo.
A dynamic website built with Python Flask using MiMo AI assistant.

**Сайт вживую / Live site:** https://site-invweb.fly.dev/

---

## Описание / Description

### Русский
Сайт демонстрирует возможности AI-помощника в разработке. Включает два основных раздела с подробной информацией об аниме.

### English
The site demonstrates AI assistant capabilities in development. Features two main sections with detailed anime information.

---

## Разделы сайта / Site Sections

### Главная страница (`/`) / Home Page (`/`)
- Приветствие и навигация по разделам / Welcome and navigation

### About (`/about`)
- Информация о проекте MiMo AI / MiMo AI project information
- Описание того, как ИИ помогает программистам / How AI helps developers

---

### Гайвер (`/guyver`) / Guyver (`/guyver`)

Раздел, посвящённый аниме-франшизе «Гайвер» (Guyver) — персонажу манги, аниме и фильмов Ёсики Такая.
Dedicated to the Guyver anime franchise — manga, anime and film character by Yoshiki Takaya.

#### Подразделы / Subsections:

**Хронология** (`/guyver/chronology`) / **Chronology** (`/guyver/chronology`)
- Интерактивная лента: манга → OVA → сериал → фильмы / Interactive timeline: manga → OVA → series → movies
- Фильтрация по типу / Filter by type
- Рекомендации «с чего начать» / «Where to start» recommendations

**Сравнение версий** (`/guyver/comparison`) / **Version Comparison** (`/guyver/comparison`)
- Таблица: манга vs аниме 2005 vs фильмы / Table: manga vs anime 2005 vs films
- 9 аспектов сравнения / 9 comparison aspects

**Карта лора** (`/guyver/lore`) / **Lore Map** (`/guyver/lore`)
- Визуальная карта связей / Visual connection map
- Иерархия сил / Power hierarchy

**Галерея трансформаций** (`/guyver/gallery`) / **Transformation Gallery** (`/guyver/gallery`)
- 9 форм брони / 9 armor forms
- Фильтрация по стадии / Filter by stage

**Какой ты зоаноид?** (`/guyver/quiz`) / **What Zoanoid Are You?** (`/guyver/quiz`)
- Квиз из 7 вопросов / 7-question quiz
- 4 результата / 4 results

**Где смотреть** (`/guyver/legal`) / **Where to Watch** (`/guyver/legal`)
- Платформы по странам / Platforms by country
- Таблица цен / Price table

---

### Мой сосед Тоторо (`/totoro`) / My Neighbor Totoro (`/totoro`)

Раздел, посвящённый аниме-фильму Studio Ghibli «Мой сосед Тоторо» (1988).
Dedicated to Studio Ghibli's «My Neighbor Totoro» (1988).

- **Обзор / Overview**: жанр, студия, режиссёр / genre, studio, director
- **Сюжет / Plot**: полное описание истории / full story description
- **Персонажи / Characters**: 8 карточек / 8 character cards
- **О Тоторо / About Totoro**: три вида / three types
- **Факты / Facts**: астероид, вид перипатуса / asteroid, peripatus species
- **Саундтрек / Soundtrack**: Дзё Хисаиси / Joe Hisaishi
- **Где посмотреть / Where to Watch**: Crunchyroll, Disney+, Amazon

---

## Технологии / Tech Stack

- **Backend**: Python 3.12, Flask
- **Frontend**: HTML5, CSS3, vanilla JavaScript
- **Деплой / Deploy**: Fly.io (Docker)
- **Контроль версий / VCS**: Git + GitHub

---

## Структура проекта / Project Structure

```
site/
├── app.py                    # Flask-приложение / Flask app
├── requirements.txt          # Зависимости / Dependencies
├── runtime.txt               # Версия Python / Python version
├── Procfile                  # Конфигурация для Render / Render config
├── Dockerfile                # Docker-образ / Docker image
├── fly.toml                  # Конфигурация Fly.io / Fly.io config
├── README.md
├── .gitignore
├── static/
│   ├── style.css             # Стили / Styles
│   ├── guyver.jpg            # Картинка Гайвера / Guyver image
│   └── totoro_main.svg       # SVG-иллюстрация / SVG illustration
└── templates/
    ├── index.html            # Главная / Home
    ├── about.html            # О проекте / About
    ├── guyver.html           # Хаб Гайвера / Guyver hub
    ├── guyver_chronology.html
    ├── guyver_comparison.html
    ├── guyver_lore.html
    ├── guyver_gallery.html
    ├── guyver_quiz.html
    ├── guyver_legal.html
    └── totoro.html
```

---

## Запуск локально / Local Setup

```bash
cd ~/Projects/site
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Откроется на / Opens at: `http://127.0.0.1:3000`

---

## Деплой / Deploy

```bash
fly deploy --yes
```

Публичный сайт / Live site: https://site-invweb.fly.dev/

---

## Создано с помощью / Built with

MiMo AI — AI-ассистент, интегрированный в VS Code.
MiMo AI — AI assistant integrated into VS Code.
