
#Line 137 on file, useless
exec { 'increment fd limit':
path     => '/usr/bin:/usr/sbin:/bin',
provider => 'shell',
command  => 'sed -i "/ULIMIT=/c\ULIMIT=\"-n 3000\"" /etc/default/nginx; sudo service nginx restart',
}
