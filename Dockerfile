# Используем образ с Python
FROM python:3

# Устанавливаем рабочую директорию
WORKDIR /app 

# Копируем исходный код в контейнер 
COPY calc.py /app/calc.py

# Запускаем приложение при старте контейнера
CMD ["python", "/app/calc.py"]