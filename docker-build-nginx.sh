#!/bin/sh

# nginx コンテナを更新

# docker 関連
rm -rf /var/service/docker
cp -r /var/vagrantshare/docker /var/service/docker

cd /var/service/docker

docker container prune -f
docker image prune -f

docker compose -f docker-compose-dev.yml rm -fsv shizai-nginx
docker-compose -f docker-compose-dev.yml up -d --no-deps --build shizai-nginx
