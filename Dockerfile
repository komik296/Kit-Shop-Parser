FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
# установка зависимостей
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]