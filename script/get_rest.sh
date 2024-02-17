sudo bash -c 'echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log'


# curl \
# -H "LOG_UNIQ_KEY:12345678" \
# -H "LOG_COUNT:10" \
# http://localhost:5000/v1/status

curl http://localhost:5000/v2/call
