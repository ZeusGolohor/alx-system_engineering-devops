# A puppet file to fix the issue of nginx request limit

exec {'restetLim':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['nginxRestart'],
}

exec {'nginxRestart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
