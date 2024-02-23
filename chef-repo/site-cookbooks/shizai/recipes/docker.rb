#
# Cookbook Name:: rl9-web
# Recipe:: docker
#

template "/etc/yum.repos.d/docker.repo" do
  source "docker.repo.erb"
  owner "root"
  group "root"
  mode "0644"
end

execute "yum install docker-ce -y" do
  command "yum install --enablerepo=docker-ce-stable docker-ce-23.0.6-1.el7 docker-ce-cli-23.0.6-1.el7 -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep docker"
end

execute "docker daemon reload" do
  command <<'EOS'
  systemctl daemon-reload
EOS
  user "root"
  group "root"
  action :nothing
  notifies :restart, 'service[docker]'
end

execute "copy docker.service" do
  command "cp -p /usr/lib/systemd/system/docker.service /etc/systemd/system/docker.service"
  user "root"
  group "root"
  not_if "ls /etc/systemd/system/ | grep docker.service"
  notifies :run, resources( :execute => "docker daemon reload")
end

# start docker
service "docker" do
  supports [:start, :stop, :restart, :status]
  action [:enable, :start]
end

cookbook_file "/usr/bin/docker-compose" do
  source "docker-compose"
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end
