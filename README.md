# Asking yourself
Сервис прохождения тестов/опросов пользователями.

### Запуск проекта в контейнерах

- Клонирование удаленного репозитория
```bash
git clone git@github.com:viator3m/kokoc_polling.git
```
- В директории /infra создайте файл .env, с переменными окружения, используя образец [.env.example](infra/.env.example)
- Сборка и развертывание контейнеров
```bash
docker-compose up -d --build
```

Миграции, создание суперпользователя и наполнение БД автоматизированно для упрощения ознакомления 

Доступ в админку:

`login: admin | password: admin`

### Запуск проекта в dev-режиме

- Клонирование удаленного репозитория
```bash
git clone git@github.com:viator3m/kokoc_polling.git
```
- В директории /infra создайте файл .env, с переменными окружения, используя образец [.env.example](infra/.env.example)
- Создание виртуального окружения и установка зависимостей
```bash
cd kokoc_polling
python -m venv venv
. venv/Scripts/activate (windows)
. venv/bin/activate (linux)
pip install --upgade pip
pip install -r -requirements.txt
```
- в файле [настройках проекта](kokoc_polling/settings.py) замените БД на файловую SQLite
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
- Примените миграции и соберите статику
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```
- Наполнение базы данных тестовыми данными
```bash
python manage.py loaddata polls_db.json
```


- Запуск сервера
```bash
python manage.py runserver 
```