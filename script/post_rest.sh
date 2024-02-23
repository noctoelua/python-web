sudo bash -c 'echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log'

curl \
-X POST \
-H "LOG-UNIQ-KEY:12345678" \
-H "LOG-COUNT:10" \
-H "content-type: application/json" \
-d '{"test": "test"}' \
http://localhost:6000/status
