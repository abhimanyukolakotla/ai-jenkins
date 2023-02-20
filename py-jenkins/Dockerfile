FROM python:slim

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=31004"]