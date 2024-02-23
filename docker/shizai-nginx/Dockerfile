FROM    nginx:1.23.1

# 既存 config ファイル削除
RUN     rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

# 設定ファイル作成用bash
COPY    docker-entrypoint.sh /usr/bin
ENTRYPOINT ["/bin/bash", "/usr/bin/docker-entrypoint.sh"]

# 公開 port 指定
EXPOSE 80
EXPOSE 5000
EXPOSE 6000

# nginx 起動
CMD     ["nginx", "-g", "daemon off;"]
