#!/bin/bash


# ファイルを配置しなおす
sudo rm -rf /var/service/rest
sudo cp -r /var/vagrantshare/service/rest /var/service/rest

sudo rm -rf /var/service/common
sudo cp -r /var/vagrantshare/service/common /var/service/common

sudo rm -rf /var/service/front
sudo cp -r /var/vagrantshare/service/front /var/service/front

sudo rm -rf /var/service/backend
sudo cp -r /var/vagrantshare/service/backend /var/service/backend
