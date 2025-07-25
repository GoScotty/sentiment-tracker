FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/

EXPOSE 8501
CMD ["streamlit", "run", "app/main.py", "--server.port=8501"]
