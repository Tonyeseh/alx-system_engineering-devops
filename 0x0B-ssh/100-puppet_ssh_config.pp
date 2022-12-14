# making changes to our ssh configuration file using puppet

file_line {'Passwd auth off':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => 'PasswordAuthentication yes'
}

file_line {'Add identity file':
  ensure => 'present'
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
