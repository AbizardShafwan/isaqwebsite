FROM python:3.6

LABEL "maintainer"="abizardshafwan_rudylie"

WORKDIR /usr/src/flask_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
