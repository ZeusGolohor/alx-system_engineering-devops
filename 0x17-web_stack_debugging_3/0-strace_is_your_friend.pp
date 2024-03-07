# A puppet file to find out why Apache is returning a 500 error

exec {'WordPress Server FIx',
  command => 'bash -c "sudo sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
  /var/www/html/wp-settings.php; sudo service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'l
}
