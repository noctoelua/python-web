echo -e "\n\n\n\n\n\n\n\n\n\n" >> /var/log/shizai/web_log.log


# curl \
# -H "LOG-UNIQ-KEY:12345678" \
# -H "LOG-COUNT:10" \
# http://localhost:5000/v1/status

curl http://localhost:6000/status
