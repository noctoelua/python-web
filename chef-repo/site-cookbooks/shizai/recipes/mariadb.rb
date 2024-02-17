#
# Cookbook Name:: shizai
# Recipe:: mariadb
#

execute "uninstall mysql" do
  only_if "rpm -qa | grep mysql | grep -v mod_auth_mysql"
  command "yum remove -y mysql-libs mysql"
  user "root"
  group "root"
end

template "/etc/yum.repos.d/MariaDB.repo" do
  source "MariaDB.repo.erb"
  owner "root"
  group "root"
  mode "0644"
end

execute "yum install MariaDB-server -y" do
  command "yum --enablerepo=mariadb install MariaDB-server -y"
  user "root"
  group "root"
  not_if "rpm -qa | grep MariaDB-server"
end

%w{
  /var/log/mysql
}.each do |dir_name|
  directory "#{dir_name}" do
    owner "mysql"
    group "admin"
    mode "0755"
    action :create
  end
end

%w{
  /var/log/mysql/error.log
  /var/log/mysql/query.log
  /var/log/mysql/slow.log
}.each do |filename|
  file "#{filename}" do
    mode "0644"
    owner "mysql"
    group "mysql"
    action :create
  end
end

%w{
  server.cnf
  mysql-clients.cnf
}.each do |conf_name|
  template "/etc/my.cnf.d/#{conf_name}" do
    source "#{conf_name}.erb"
    owner "root"
    group "root"
    mode "0644"
    notifies :restart, 'service[mariadb]'
  end
end

# rootユーザーはとりあえずaliasなし
node['mariadb']['readonly_alias'].each do |user|
  [
    "alias mysql='mysql --safe-updates'",
    "alias mysqlreadonly='mysql -u readonly -preadonly'"
  ].each do |mysql_alias|
    execute "add `#{mysql_alias}` to #{user}" do
      command "echo \"#{mysql_alias}\" >> ~#{user}/.bashrc"
      user "root"
      group "root"
      not_if "grep -q \"^#{mysql_alias}\" ~#{user}/.bashrc"
    end
  end
end

service "mariadb" do
  supports [:start => true, :restart => true, :reload => true, :status => true]
  action [ :enable, :start ]
end

execute "unsocket_pass" do
  command "mysqladmin -u root password #{node['mariadb']['root_password']}"
  user "root"
  group "root"
  # action :nothing
  not_if "echo 'select * from mysql.user where User = \"root\"' | mariadb -u root -p#{node['mariadb']['root_password']} | grep -q root"
end

execute "socket_pass" do
  command "mysqladmin -u root password #{node['mariadb']['root_password']}"
  user "root"
  group "root"
  # action :nothing
  only_if "echo 'select password from mysql.user where User = \"root\"' | mariadb | grep -q invalid"
end

# database作成
node['mariadb']['databases'].each do |db_name, db_config |
  execute "create database" do
    Chef::Log.info('create database #{db_name}')
    command "echo \"CREATE DATABASE IF NOT EXISTS #{db_name};\" | mariadb -u root -p#{node['mariadb']['root_password']}"
    user "root"
    group "root"
    # action :nothing
    subscribes :run, resources( :execute => ["socket_pass", "unsocket_pass"] )
    not_if "echo \"SHOW DATABASES;\" | mariadb -u root -p#{node['mariadb']['root_password']} | grep #{db_name}"
  end
end

# databaseに紐づくユーザー作成
node['mariadb']['databases'].each do |db_name, db_config |
  db_config['users'].each do |name, attrs |
    privileges = attrs.has_key?(:privileges) ? attrs[:privileges].join(', ') : 'ALL'
    password = attrs.has_key?('password') ? attrs['password'] : name
    target = attrs.has_key?('target') ? attrs['target'] : '*'
    hosts = attrs.has_key?(:hosts) ? attrs[:hosts] : ['localhost']
    hosts = [hosts] if !hosts.kind_of?(Array)
    hosts.each do |host|
      execute "create #{name}@#{host} user" do
        Chef::Log.info('Add user: database=#{db_name}, user=#{name}')
        command "echo \"CREATE USER '#{name}'@'#{host}'\" | mariadb -u root -p#{node['mariadb']['root_password']}"
        command "echo \"GRANT #{privileges} ON #{target}.* TO '#{name}'@'#{host}' IDENTIFIED BY '#{password}'; FLUSH PRIVILEGES;\" | mariadb -u root -p#{node['mariadb']['root_password']}"
        user "root"
        group "root"
        not_if "echo 'select * from mysql.user where User = \"#{name}\" and Host = \"#{host}\"' | mariadb -u root -p#{node['mariadb']['root_password']} | grep -q #{name}"
        subscribes :run, resources( :execute => ["socket_pass", "unsocket_pass"] )
      end
    end
  end
end

# readonlyユーザー作成
execute "create readonly user" do
  name = 'readonly'
  privileges = 'SELECT'
  password = 'readonly'
  target = '*'
  host = 'localhost'

  command "echo \"GRANT #{privileges} ON #{target}.* TO '#{name}'@'#{host}' IDENTIFIED BY '#{password}'; FLUSH PRIVILEGES;\" | mariadb -u root -p#{node['mariadb']['root_password']}"
  user "root"
  group "root"
  action :nothing
  not_if "echo 'select * from mysql.user where User = \"#{name}\" and Host = \"#{host}\"' | mariadb -u root -p#{node['mariadb']['root_password']} | grep -q #{name}"
  subscribes :run, resources( :execute => ["socket_pass", "unsocket_pass"] )
end

# クエリ結果色付け用ライブラリ
# execute "yum install grc" do
#   command "yum install grc -y"
#   user "root"
#   group "root"
#   not_if "rpm -qa | grep grc"
# end
