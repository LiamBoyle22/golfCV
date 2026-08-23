FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt \
    && pip uninstall -y opencv-python opencv-python-headless \
    && pip install opencv-python-headless

COPY api/ ./api
COPY workers/ ./workers
COPY db/ ./db

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]