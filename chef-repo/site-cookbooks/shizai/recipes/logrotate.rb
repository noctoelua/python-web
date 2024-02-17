#
# Cookbook Name:: shizai
# Recipe:: logrotate
#

template "/etc/logrotate.conf" do
  source "logrotate.conf.erb"
  owner "root"
  group "root"
  mode "0644"
end

if node.has_key?("logrotate") && node["logrotate"].has_key?("services")
    node["logrotate"]["services"].each do |conf|
      template "/etc/logrotate.d/#{conf}" do
        source "logrotate.d/#{conf}.erb"
        owner "root"
        group "root"
        mode "0644"
      end
    end
end
