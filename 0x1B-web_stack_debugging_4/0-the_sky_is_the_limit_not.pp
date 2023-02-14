# Increases the amount of traffic an Nginx server can handle

# Increase the Ulimit for the default file
exec { 'ulimit-incre':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'restart_restart':
  command     => 'service nginx restart',
  path        => '/usr/bin/:/bin/'
  refreshonly => true
}
