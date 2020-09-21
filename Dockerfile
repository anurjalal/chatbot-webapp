FROM python:3.8-alpine
RUN apk add --no-cache build-base
RUN apk add --no-cache --update python3
RUN apk add --no-cache python3-dev
RUN apk add --no-cache --update py3-pip
COPY . /app
WORKDIR /app
ENV FLASK_ENV development
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install  --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download en
EXPOSE 5000
COPY . .

CMD = ["flask", "run"]
