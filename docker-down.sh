#!/bin/sh

# docker コンテナ全ダウン

cd /var/service/docker
docker compose -f docker-compose-dev.yml down

# いらないからとりあえず削除しておく
docker container prune -f
docker image prune -f
