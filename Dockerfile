FROM python:3.10

RUN pip install --upgrade pip

WORKDIR /API

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
