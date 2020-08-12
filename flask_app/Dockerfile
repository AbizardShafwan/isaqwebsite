FROM python:3.8

LABEL "maintainer"="abizardshafwan_rudylie"

# Create user home directory
RUN mkdir -p /home/isaq

# create the appropriate directories
ENV HOME=/home/isaq
ENV APP_HOME=/home/isaq/flask_app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip

# install https from chatbot
RUN sudo apt-get update
RUN sudo apt-get install software-properties-common
RUN sudo add-apt-repository universe
RUN sudo add-apt-repository ppa:certbot/certbot
RUN sudo apt-get update
RUN sudo apt-get install certbot python3-certbot-nginx
RUN sudo certbot --nginx
RUN sudo certbot renew --dry-run

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy flask_app directory to APP_HOME directory
COPY . .

