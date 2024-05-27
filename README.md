# python-web
## 概要
本リポジトリは python の web サーバーを構築する際に1から作成せずに済むよう、
基本的なモジュール作成を行うものです.

## ディレクトリ
### .vscode
* vscode の設定

### chef-repo
* chef関連を配置

### docker
* docker に利用する設定ファイル等々

### migration
* migration 関連を配置

### script
* テスト用の curl をまとめたものを配置

### service
* サービス利用するコードを配置.
* docker 化の際はこのファイル配下を COPY して利用する

### vagrantfile
* ローカル環境作成する際の vagrant 関連ファイルを配置

### その他のshell
* コンテナ更新や uwsgi 更新等の開発用 shell

## ログフォーマット
```console
container_name:/shizai-rest     log:2024-03-17 05:52:14,296 [INFO   ] [15088319:1] [REQUEST] GET: endpoint=http://5000_pass/status, access=172.16.10.10 [/var/service/common/libs/RestABRequest.py 41 in before_request]
container_name:/shizai-rest     log:2024-03-17 05:52:14,296 [INFO   ] [15088319:3] TEST2 [/var/service/rest/wsgi/www_rest.py 35 in hello_world]
container_name:/shizai-rest     log:2024-03-17 05:52:14,296 [WARNING] [15088319:4] TEST3 [/var/service/rest/wsgi/www_rest.py 36 in hello_world]
container_name:/shizai-rest     log:2024-03-17 05:52:14,296 [ERROR  ] [15088319:5] TEST4 [/var/service/rest/wsgi/www_rest.py 37 in hello_world]
container_name:/shizai-rest     log:2024-03-17 05:52:14,296 [INFO   ] [15088319:6] time: 0.613 ms   - done [/var/service/common/libs/RestABRequest.py 55 in after_request]
```
