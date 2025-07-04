# Используем официальный Python-образ
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /app/

# Указываем переменную окружения для Python
ENV PYTHONUNBUFFERED 1

# Открываем порт
EXPOSE 8000

# Команда для запуска Django

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
