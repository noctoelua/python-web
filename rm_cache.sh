sudo find /var/vagrantshare -name __pycache__ | xargs -I{} rm -rf {}
