FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
# Upgrade pip and ensure core tooling is present
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install pytest pytest-watch
COPY src/ /app/src

CMD ["ptw", "src"]
