# Flask app Dockerfile
FROM python:3.6-alpine

# Install needed dependencies for our app to run.
RUN apk update
RUN apk add --no-cache gcc
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache musl-dev
RUN apk add --no-cache libjpeg
RUN apk add --no-cache zlib
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow

WORKDIR /opt/app

# App non-root user
ENV GROUP=app
ENV USER=flask
ENV UID=12345
ENV GID=23456
RUN addgroup --gid "$GID" "$GROUP" \
  && adduser --uid "$UID" \
    --disabled-password \
    --gecos "" \
    --ingroup "$GROUP" \
    "$USER"

# Switch to the non-root user
USER "$USER"
ENV PATH="/home/$USER/.local/bin:${PATH}"

# Copy requirements file to our container, install, and remove
# files to we don't need to reduce the container size
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app to container (with privileges to non-root user)
COPY --chown=$USER:$GROUP . .

# Gunicorn is run from the docker-compose file
