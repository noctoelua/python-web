#
# Cookbook Name:: shizai
# Recipe:: crontab
#

# cronで利用するshellの配置
if node.has_key?("crontab") && node["crontab"].has_key?("template_tools")
    node["crontab"]["template_tools"].each do |tool|
      template "/var/service/tools/#{tool}" do
        source "crontab/#{tool}.erb"
        owner "admin"
        group "admin"
        mode "0755"
      end
    end
end

template "/etc/crontab" do
  source "crontab.erb"
  owner "root"
  group "root"
  mode "0644"
end
