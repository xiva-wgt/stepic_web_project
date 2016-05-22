#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djdb;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'qwertypass123';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON djdb.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"