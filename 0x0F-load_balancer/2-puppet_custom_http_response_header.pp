# create a custom HTTP header response

exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}

file_line { 'locate':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'error_page 404 /custom.html;',
    require => Package['nginx'],
}

file_line { 'redirect':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require => Package['nginx'],
}

file_line { 'header':
    ensure  => 'present',
    path    => '/etc/nginx/nginx.conf',
    after   => 'http {',
    line    => 'add_header X-Served-By "$HOSTNAME";',
    require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World',
  require => Package['nginx'],
}

file { '/var/www/html/custom.html':
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}


service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
