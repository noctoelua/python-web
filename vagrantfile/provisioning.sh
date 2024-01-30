#!/usr/bin/env bash

set -e

echo '---START---'

cp /var/vagrantshare/vagrantfile/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
chmod 644 /etc/yum.repos.d/CentOS-Base.repo
chown root:root /etc/yum.repos.d/CentOS-Base.repo


# install epel repository
# サードパーティリポジトリからインストールできるようにするためのもの
if [[ -z `rpm -qa | grep epel` ]]; then
    echo "--------------------------------------------------"
    echo "  install epel repository"
    echo "--------------------------------------------------"
    yum -y install epel-release
else
    echo "  - allready install epel repository"
fi

# install git
# シェフにはGitが必須なため、Gitを入れる
if [[ -z `rpm -qa | grep -E ^git` ]]; then
    echo "--------------------------------------------------"
    echo "  install git"
    echo "--------------------------------------------------"
    yum install -y git
else
    echo "  - allready install git"
fi

# install ruby
# chefはrubyで書かれるため
# if [[ -z `rpm -qa | grep ruby` ]]; then
#     echo "--------------------------------------------------"
#     echo "  install ruby"
#     echo "--------------------------------------------------"
#     yum install -y ruby
# else
#     echo "  - allready install ruby"
# fi

# install chef
# 本体のインストール. 手元にあるファイルを使用し実行
# if [[ -z `rpm -qa | grep chef` ]]; then
#     echo "--------------------------------------------------"
#     echo "  install chef"
#     echo "--------------------------------------------------"
#     rpm -ivh --nosignature ./chef-14.5.33-1.el7.x86_64.rpm
# else
#     echo "  - allready install chef"
# fi

# user add
if [[ -z `cat /etc/passwd | grep admin` ]]; then
    echo "--------------------------------------------------"
    echo "  user add"
    echo "--------------------------------------------------"
    useradd admin
    useradd ope
else
    echo "  - allready user add"
fi

# set time Asia/Tokyo
if [[ -z `date | grep JST` ]]; then
    echo "--------------------------------------------------"
    echo "  set time zone"
    echo "--------------------------------------------------"
    timedatectl set-timezone Asia/Tokyo
else
    echo "  - allready set time zone"
fi

# install python3
if [[ -z `rpm -qa | grep python3` ]]; then
    echo "--------------------------------------------------"
    echo "  install python3"
    echo "--------------------------------------------------"
    yum install -y python3 python3-pip python3-devel
else
    echo "  - allready install python"
fi

# chef実行
# chef-solo -c ./chef-repo/solo.rb -j ./chef-repo/nodes/`hostname -s`.json
# nmap
# tcpdump

# docker 関連ファイル配置
# echo "--------------------------------------------------"
# echo "  copy docker directry"
# echo "--------------------------------------------------"
# rm -rf /var/service/docker
# cp -r ./docker /var/service/
# echo "  - done"

yum install -y gcc

# python ライブラリのインストール
pip3 install -r /var/vagrantshare/service/requirements.txt

mkdir -p /var/log/shizai/
mkdir -p /var/service
mkdir -p /var/service/run

echo '---END---'
