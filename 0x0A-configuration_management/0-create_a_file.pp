# creating a file
file { 'school':
path    => '/tmp',
content => 'I love Puppet',
owner   =>'www-data',
group   => 'www-data',
mode    => '0744'
}
