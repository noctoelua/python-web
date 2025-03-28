#!/bin/bash

# rest access lodalhost:5000
# process kill command : ps -eo pid,args | grep app_rest | awk '{print$1}' | head -n 1 | xargs -I{} kill {}

# わかりやすいように改行を入れておく
echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log

# ファイルを配置しなおす
sudo rm -rf /var/service/rest
sudo cp -r /var/vagrantshare/service/rest /var/service/rest

# commonも
sudo rm -rf /var/service/common
sudo cp -r /var/vagrantshare/service/common /var/service/common

# 必要に応じた処理をする
if [[ -z `ps -eo pid,args | grep app_rest | grep -v grep` ]] ; then
    nohup /usr/local/bin/uwsgi --ini /var/service/rest/wsgi/app_rest.ini > /dev/null 2>&1 &
    echo "--- START  ---"
else
    touch /var/service/run/app_rest_greceful.reload
    echo "--- RESTART ---"
fi
