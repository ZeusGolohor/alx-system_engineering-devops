# Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow_process_killer':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
