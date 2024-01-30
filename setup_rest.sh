echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log

ps -eo pid,args | grep app_front | awk '{print$1}' | head -n 1 | xargs -I{} kill {}

sudo rm -rf /var/service/rest
sudo cp -r /var/vagrantshare/service/rest /var/service/rest

sleep 5
echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log


nohup /usr/local/bin/uwsgi --ini /var/service/rest/wsgi/app_front.ini > /dev/null 2>&1 &
