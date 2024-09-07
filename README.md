# Структура проекта
```
python-service-project
    |— data
       |— data.json # Создастся при старте скрипта
       |— result.json # Создастся при старте скрипта
    |— src
       |— __init__.py
       |— bot.py
       |— google_api_auth.py
       |— json_handler.py
       |— main.py
       |— parser.py
       |— services.py
       |— settings.py
       |— telegram_api_handler.py
       |— validators.py
    |— .env.sample
    |— .flake8
    |— .gitignore
    |— credentials.json
    |— LICENSE
    |— poetry.lock
    |— pyproject.toml
    |— README.md
    |— requirements.txt
```

# Инструкция для работы

## 1) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/python-service-project.git
```

## 2) Добавьте файл .env для переменных окружения
Чтобы запустить проект, понадобятся переменные окружения, которые необходимо добавить в созданный Вами .env файл.

Пример переменных окружения необходимо взять из файла .env.sample.

## 3) Добавьте файл credentials.json для Google API
Чтобы Вы могли взаимодействовать с Google API, необходимо скачать файл credentials.json из Google Cloud Console (Service Accounts) 

## 4) Запустите проект

### Запуск бота
```
python -m src.bot
```

### Пример команды для получения данных
```
python -m src.main --options_json '100_cctv'
```

P.S. Данные пользователя сохраняются в словарь, который создаётся при запуске бота и удаляется при его остановке. В случае неудобства, можете реализовать добавление данных в json-файл или в базу данных (на Ваше усмотрение).
