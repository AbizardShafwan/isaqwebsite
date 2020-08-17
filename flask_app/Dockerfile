# Flask app Dockerfile
FROM python:3.8

# create directory for the app user
RUN mkdir -p /home/isaq

# create the appropriate directories
ENV HOME=/home/isaq
ENV APP_HOME=/home/isaq/flask_app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


