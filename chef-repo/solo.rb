base = File.expand_path('..', __FILE__)

nodes_path                File.join(base, 'nodes')
ssl_verify_mode           :verify_peer

log_level                 :auto

cookbook_path []
cookbook_path << File.join(base, 'cookbooks')
cookbook_path << File.join(base, 'site-cookbooks')
