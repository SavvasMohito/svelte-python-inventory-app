FROM python:3.12.3-slim-bookworm

WORKDIR /app

ADD src .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/src

CMD uvicorn app:app --host 0.0.0.0 --port 8000