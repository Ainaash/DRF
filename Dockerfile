# Используем официальный Python-образ (лучше указать версию)
FROM python:3.13-slim

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Открываем порт 8000 для доступа
EXPOSE 8000

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Копируем и даём права на скрипт запуска
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Указываем команду по умолчанию
CMD ["/app/entrypoint.sh"]
