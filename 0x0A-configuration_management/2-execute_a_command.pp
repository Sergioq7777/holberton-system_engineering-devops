# Kill process puppet
exec {'killp':
  command  => 'pkill killmenow',
  provider => 'shell'
}
