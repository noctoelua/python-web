#!/bin/bash

# うざい pycache を削除

sudo find /var/vagrantshare -name __pycache__ | xargs -I{} rm -rf {}
