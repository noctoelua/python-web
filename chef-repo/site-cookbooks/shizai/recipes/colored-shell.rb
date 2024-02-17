#
# Cookbook Name:: shizai
# Recipe:: colored-shell
#


node['colored-shell'].each do |user, attrs|
    if user == "root"
        color = attrs.has_key?('color') ? attrs['color'] : "green"
        template "/root/.bash_profile" do
            source "bash_profile.erb"
            owner "root"
            group "root"
            mode "0644"
            variables({
                :color => "#{color}"
            })
        end
    else
        color = attrs.has_key?('color') ? attrs['color'] : "green"
        template "/home/#{user}/.bash_profile" do
            source "bash_profile.erb"
            owner "#{user}"
            group "#{user}"
            mode "0644"
            variables({
                :color => "#{color}"
            })
        end
    end
end
