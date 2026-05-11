FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

COPY pyproject.toml .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root

COPY app.py .
COPY templates ./templates

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
