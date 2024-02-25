#!/bin/bash

# とりあえず全体的に flake

cd /var/vagrantshare/service

flake8 --ignore=E501,E402
