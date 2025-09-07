FROM python:3.12-slim

WORKDIR /app

# Instala só o essencial
RUN apt-get update && apt-get install -y \
    build-essential \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

EXPOSE 54321

CMD ["flask", "run", "--host=0.0.0.0", "--port=54321"]
