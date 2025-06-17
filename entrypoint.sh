#!/bin/sh

echo "📦 makemigrations..."
python3 manage.py makemigrations

echo "📦 Применяем миграции..."
python3 manage.py migrate

echo "🚀 Запуск сервера..."
python3 manage.py runserver 0.0.0.0:8000
