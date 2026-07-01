# MiMo AI — Тестовый сайт / MiMo AI — Test Site

Динамический сайт на Python Flask, созданный с помощью AI-ассистента MiMo.
A dynamic website built with Python Flask using MiMo AI assistant.

**Сайт вживую / Live site:** https://site-invweb.fly.dev/

---

## Описание / Description

### Русский
Сайт демонстрирует возможности AI-помощника в разработке. Включает разделы с подробной информацией об аниме: Гайвер, Тоторо, Блич, One Piece, Studio Ghibli и Наруто.

### English
The site demonstrates AI assistant capabilities in development. Features sections with detailed anime information: Guyver, Totoro, Bleach, One Piece, Studio Ghibli and Naruto.

---

## Разделы сайта / Site Sections

### Главная страница (`/`) / Home Page (`/`)
- Приветствие и навигация по разделам / Welcome and navigation

### About (`/about`)
- Информация о проекте MiMo AI / MiMo AI project information

---

### Гайвер (`/guyver`) / Guyver (`/guyver`)
Аниме-франшиза Ёсики Такая / Anime franchise by Yoshaki Takaya

- **Хронология** (`/guyver/chronology`) — Интерактивная лента / Interactive timeline
- **Сравнение версий** (`/guyver/comparison`) — Таблица сравнения / Comparison table
- **Карта лора** (`/guyver/lore`) — Визуальная карта связей / Visual map
- **Галерея трансформаций** (`/guyver/gallery`) — 9 форм брони / 9 armor forms
- **Какой ты зоаноид?** (`/guyver/quiz`) — Квиз / Quiz
- **Где смотреть** (`/guyver/legal`) — Платформы / Platforms

---

### Мой сосед Тоторо (`/totoro`) / My Neighbor Totoro (`/totoro`)
Фильм Studio Ghibli (1988) / Studio Ghibli film (1988)

- Обзор, сюжет, персонажи, факты / Overview, plot, characters, facts

---

### Блич (`/bleach`) / Bleach (`/bleach`)
Манга Тайто Кубо / Manga by Tite Kubo

- Обзор, сюжет (5 арк), персонажи, мир / Overview, plot (5 arcs), characters, world

---

### One Piece (`/onepiece`) / One Piece (`/onepiece`)
Самая продаваемая манга в мире / Best-selling manga in the world

- Обзор, сюжет, команда Луффи, система сил, мир, рекорды / Overview, plot, Luffy's crew, power system, world, records

---

### Studio Ghibli (`/ghibli`) / Studio Ghibli (`/ghibli`)
Легендарная анимационная студия / Legendary animation studio

- История, основатели, фильмы, достижения / History, founders, films, achievements

---

### Наруто (`/naruto`) / Naruto (`/naruto`)
Манга Масаши Кисимото / Manga by Masashi Kishimoto

- Обзор, сюжет, персонажи, система сил, мир / Overview, plot, characters, power system, world

---

## SVG-иллюстрации / SVG Illustrations

Сайт использует собственные SVG-иллюстрации вместо фотографий:
The site uses custom SVG illustrations instead of photos:

| Файл / File | Раздел / Section |
|---|---|
| `guyver_hero.svg` | Гайвер / Guyver |
| `guyver_main.svg` | Тоторо / Totoro |
| `totoro_hero2.svg` | Тоторо / Totoro |
| `bleach_hero.svg` | Блич / Bleach |
| `onepiece_hero.svg` | One Piece |
| `ghibli_hero.svg` | Studio Ghibli |
| `naruto_hero.svg` | Наруто / Naruto |
| `naruto_portrait.svg` | Наруто / Naruto |
| `narutoSharingan.svg` | Шаринган / Sharingan |
| `naruto_rasengan.svg` | Расенган / Rasengan |
| `naruto_kurama.svg` | Кьюби / Kurama |
| `naruto_konoha.svg` | Коноха / Konoha |

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
│   ├── guyver_hero.svg       # Hero-картинка / Hero image
│   ├── totoro_main.svg       # SVG Тоторо / Totoro SVG
│   ├── totoro_hero2.svg      # SVG Тоторо / Totoro SVG
│   ├── bleach_hero.svg       # Hero Блича / Bleach hero
│   ├── onepiece_hero.svg     # Hero One Piece
│   ├── ghibli_hero.svg       # Hero Ghibli
│   ├── naruto_hero.svg       # Hero Наруто / Naruto hero
│   ├── naruto_portrait.svg   # Портрет Наруто / Naruto portrait
│   ├── narutoSharingan.svg   # Шаринган / Sharingan
│   ├── naruto_rasengan.svg   # Расенган / Rasengan
│   ├── naruto_kurama.svg     # Кьюби / Kurama
│   └── naruto_konoha.svg     # Коноха / Konoha
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
    ├── totoro.html           # Мой сосед Тоторо / My Neighbor Totoro
    ├── bleach.html           # Блич / Bleach
    ├── onepiece.html         # One Piece
    ├── ghibli.html           # Studio Ghibli
    └── naruto.html           # Наруто / Naruto
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
