# Используем официальный Python-образ (лучше указать версию)
FROM python:3.13-slim

# Отключаем буферизацию вывода
ENV PYTHONUNBUFFERED=1

# Обновляем pip и устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
