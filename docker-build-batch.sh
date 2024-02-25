#!/bin/sh

# batch コンテナを更新

# docker 関連
rm -rf /var/service/docker
cp -r /var/vagrantshare/docker /var/service/docker

# batch
cp -r /var/vagrantshare/service/batch /var/service/docker/shizai-batch/
cp -r /var/vagrantshare/service/common /var/service/docker/shizai-batch/

cd /var/service/docker

docker container prune -f
docker image prune -f

docker compose -f docker-compose-dev.yml rm -fsv shizai-batch
docker compose -f docker-compose-dev.yml up -d --no-deps --build shizai-batch
