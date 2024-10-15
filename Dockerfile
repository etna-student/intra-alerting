FROM python:alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY app/main.py app/

CMD ["python","main.py"]

