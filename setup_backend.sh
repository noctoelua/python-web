#!/bin/bash

# backend access lodalhost:6000

# わかりやすいように改行を入れておく
echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log

# ファイルを配置しなおす
sudo rm -rf /var/service/backend
sudo cp -r /var/vagrantshare/service/backend /var/service/backend

# 必要に応じた処理をする
if [[ -z `ps -eo pid,args | grep app_backend | grep -v grep` ]] ; then
    nohup /usr/local/bin/uwsgi --ini /var/service/backend/wsgi/app_backend.ini > /dev/null 2>&1 &
    echo "--- START  ---"
else
    touch /var/service/run/app_backend_greceful.reload
    echo "--- RESTART ---"
fi
