#
# Cookbook Name:: shizai
# Recipe:: iptables
#

service "firewalld" do
  supports [:start => true, :restart => true, :reload => true, :status => true, :stop => true, :disable => true]
  action [ :disable, :stop ]
end

execute "yum install iptables-services -y" do
  command "yum install iptables-services -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep iptables-services"
end

service "iptables" do
  supports [:start => true, :restart => true, :reload => true, :status => true]
  action [ :enable, :start ]
end
