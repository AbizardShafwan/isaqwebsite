# Flask app Dockerfile
FROM python:3.8

# create directory for the app user
RUN mkdir -p /home/flask_app

# create the appropriate directories
ENV HOME=/home/flask_app
ENV APP_HOME=/home/flask_app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


