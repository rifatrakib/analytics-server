FROM python:3.9-slim-buster

WORKDIR /backend

COPY requirements.txt README.md ./secrets /backend/
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY ./server /backend/server

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
