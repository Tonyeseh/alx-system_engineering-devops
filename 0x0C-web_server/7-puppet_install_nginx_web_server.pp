# Configure Nginx server with pouppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'add block server':
  path    => '/usr/bin',
  command => 'echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}" | sudo tee /etc/nginx/sites-available/default'
}

exec {'restarting nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart'
}
