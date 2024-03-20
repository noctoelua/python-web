#!/bin/sh

# すべてのコンテナを更新

# docker 関連
rm -rf /var/service/docker
cp -r /var/vagrantshare/docker /var/service/docker

# backend
cp -r /var/vagrantshare/service/backend /var/service/docker/shizai-backend/
cp -r /var/vagrantshare/service/common /var/service/docker/shizai-backend/

# rest
cp -r /var/vagrantshare/service/rest /var/service/docker/shizai-rest/
cp -r /var/vagrantshare/service/common /var/service/docker/shizai-rest/

# front
cp -r /var/vagrantshare/service/front /var/service/docker/shizai-front/
cp -r /var/vagrantshare/service/common /var/service/docker/shizai-front/

# batch
cp -r /var/vagrantshare/service/batch /var/service/docker/shizai-batch/
cp -r /var/vagrantshare/service/common /var/service/docker/shizai-batch/

cd /var/service/docker
docker compose -f docker-compose-dev.yml down

docker container prune -f
docker image prune -f

docker compose -f docker-compose-dev.yml build --no-cache
docker compose -f docker-compose-dev.yml up -d
