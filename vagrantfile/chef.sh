#!/usr/bin/env bash

set -e

echo '---START---'

# chef実行
chef-solo -c /var/vagrantshare/chef-repo/solo.rb -j /var/vagrantshare/chef-repo/nodes/`hostname -s`.json

echo '---END---'
