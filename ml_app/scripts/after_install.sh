#!/bin/bash
cd /home/ubuntu/ml_app   # change to the directory where the docker-compose.yml file is located

docker-compose stop;   # stop the running containers
docker-compose rm -f;  # remove the containers
docker-compose pull;   # pull the latest images
docker-compose up -d;  # start the containers in the background

