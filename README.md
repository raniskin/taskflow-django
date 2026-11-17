# TaskFlow — Django Task Manager

Сервис управления личными задачами: регистрация, вход, создание/изменение/удаление задач, поиск, фильтры и статусы. Пользователь видит **только свои** задачи.

## Стек
Python 3.10+, Django 5, SQLite, HTML/CSS (Django templates).

## Запуск
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Откройте http://127.0.0.1:8000/register/ и создайте аккаунт.

Тесты: `python manage.py test`.

## Демонстрация
Регистрация → создание 2 задач → фильтр по статусу → редактирование → удаление. Покажите, что чужие задачи недоступны.

## Безопасность и ограничения
Используются стандартные CSRF-защита, хеширование паролей и permissions по владельцу. `DEBUG=1` и локальный `SECRET_KEY` предназначены **только для разработки**. Перед публичным деплоем настройте `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS`, HTTPS и резервное копирование БД. SQLite подходит для демонстрации, но не для высоконагруженного продакшена.
