#
# Cookbook Name:: shizai
# Recipe:: default
#

%w{
  log
  service/tools
  service/dbbackup
}.each do |dir|
  directory "/var/#{dir}" do
    owner "admin"
    group "admin"
    mode "0755"
    action :create
    recursive true
  end
end

execute "yum install nmap -y" do
  command "yum install nmap -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep nmap"
end

execute "yum install tcpdump -y" do
  command "yum install tcpdump -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep tcpdump"
end

execute "yum install rsync -y" do
  command "yum install rsync -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep rsync"
end

execute "yum install bzip2 -y" do
  command "yum install bzip2 -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep bzip2"
end

execute "yum install bind-utils -y" do
  command "yum install bind-utils -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep bind-utils"
end
