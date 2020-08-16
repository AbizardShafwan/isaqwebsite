chmod +x init-letsencrypt.sh

sudo ./init-letsencrypt.sh

echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d
