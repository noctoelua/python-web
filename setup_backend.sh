echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log

ps -eo pid,args | grep app_backend | awk '{print$1}' | head -n 1 | xargs -I{} kill {}

sudo rm -rf /var/service/backend
sudo cp -r /var/vagrantshare/service/backend /var/service/backend

sleep 5
echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log


nohup /usr/local/bin/uwsgi --ini /var/service/backend/wsgi/app_backend.ini > /dev/null 2>&1 &
