FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY monitors ./monitors
COPY healing ./healing
COPY orchestrator ./orchestrator

# Set Python path
ENV PYTHONPATH=/app

EXPOSE 5000 8000

CMD ["python", "app/main.py"]
