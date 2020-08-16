chmod +x init-letsencrypt.sh

sudo ./init-letsencrypt.sh

echo building docker containers
docker-compose up
