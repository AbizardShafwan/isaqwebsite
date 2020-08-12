FROM nginx:1.15.8

RUN apt-get update

RUN apt-get install software-properties-common

RUN add-apt-repository universe

RUN add-apt-repository ppa:certbot/certbot

RUN apt-get update

RUN apt-get install certbot python3-certbot-nginx

RUN certbot --nginx

RUN certbot renew --dry-run

RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf

COPY project.conf /etc/nginx/conf.d