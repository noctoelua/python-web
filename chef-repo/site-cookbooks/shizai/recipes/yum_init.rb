#
# Cookbook Name:: shizai
# Recipe:: yum_init
#

execute "yum update -y openssl" do
    user "root"
    group "root"
end
