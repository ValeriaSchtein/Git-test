# NeiroBot — простой Telegram-бот на aiogram

Простой учебный проект: Telegram-бот на Python с библиотекой **aiogram 3** и загрузкой настроек через **python-dotenv**.  
Бот умеет:

- отвечать на команду **`/start`**
- показывать справку по команде **`/help`**
- повторять (эхо) любое текстовое сообщение

---

## Структура проекта

```text
.
├─ README.md          # эта инструкция
├─ requirements.txt   # список зависимостей (библиотек)
├─ .env               # реальные секреты (токен бота) — не в Git
├─ .env.example       # пример .env (без секретов)
├─ src/
│  └─ bot/
│     ├─ __init__.py
│     ├─ __main__.py  # запуск: python -m src.bot
│     ├─ main.py      # точка входа бота
│     ├─ config.py    # загрузка настроек из .env
│     ├─ routers/     # обработчики команд и сообщений
│     │  ├─ __init__.py
│     │  ├─ start.py  # команда /start
│     │  ├─ help.py   # команда /help
│     │  └─ echo.py   # эхо-сообщения
│     ├─ services/    # бизнес-логика (без aiogram)
│     │  └─ text.py
│     └─ keyboards/   # клавиатуры (кнопки)
│        ├─ __init__.py
│        └─ common.py
└─ venv/              # виртуальное окружение (в Git игнорируется)
```

Ключевая идея: **логика бота отделена от Telegram‑обвязки**.  
Например, тексты сообщений лежат в `services/text.py`, а обработчики Telegram‑команд — в `routers/`.

---

## Подготовка токена бота

1. Открой Telegram и найди бота **`@BotFather`**.
2. Создай нового бота командой `/newbot` и следуй инструкциям.
3. В конце BotFather пришлёт тебе **токен** вида:

   ```text
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

4. В корне проекта создай файл `.env` (или скопируй `.env.example` в `.env`) и добавь строку:

   ```text
   BOT_TOKEN=твой_токен_от_BotFather
   ```

   Этот файл **нельзя коммитить в Git** — он уже добавлен в `.gitignore`.

---

## Установка и запуск на Windows

### 1. Создать и активировать виртуальное окружение

```powershell
cd c:\NeiroBot\Git-test
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Если PowerShell ругается на выполнение скриптов, разреши их для текущего пользователя:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Потом снова активируй окружение:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Установить зависимости

```powershell
pip install -r requirements.txt
```

### 3. Запустить бота

```powershell
python -m src.bot
```

Пока эта команда работает и терминал «живой», бот запущен.  
Открой в Telegram своего бота и отправь команды:

- `/start` — приветствие и краткое описание
- `/help` — список команд
- любой текст — бот повторит его (эхо)

---

## Установка и запуск на macOS / Linux

### 1. Создать и активировать виртуальное окружение

```bash
cd /путь/к/NeiroBot-Git-test
python3 -m venv venv
source venv/bin/activate
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Запустить бота

```bash
python -m src.bot
```

Дальше взаимодействие с ботом такое же, как на Windows.

---

## Как устроен код (понятно для начинающих)

- **`config.py`** — читает настройки из `.env`.  
  Здесь мы берём `BOT_TOKEN` и, если его нет, бросаем понятную ошибку.

- **`routers/*.py`** — файлы, которые решают, *что делать при конкретном сообщении*:
  - `start.py` — что ответить на `/start`
  - `help.py` — что ответить на `/help`
  - `echo.py` — как обрабатывать обычный текст

- **`services/text.py`** — *чистые функции*, которые строят текст ответа.  
  Здесь нет Telegram‑объектов, только строки. Это удобно для тестов и дальнейшей логики.

- **`keyboards/common.py`** — создание клавиатуры с кнопками `/start` и `/help`.  
  Клавиатура передаётся в обработчик `/start`, чтобы пользователю было удобно нажимать команды.

---

## Полезные команды для разработки

Активировать виртуальное окружение (Windows, PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Обновить `pip` (по желанию, но рекомендуется):

```powershell
python -m pip install --upgrade pip
```

Запустить бота:

```powershell
python -m src.bot
```

Остановить бота — просто нажать `Ctrl + C` в терминале, где он запущен.

