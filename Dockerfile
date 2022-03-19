FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

VOLUME upload-dir

CMD flask run --host=0.0.0.0