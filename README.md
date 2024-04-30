[![Build Status](http://192.168.1.231:8080/api/badges/common/python-web/status.svg)](http://192.168.1.231:8080/common/python-web)

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
