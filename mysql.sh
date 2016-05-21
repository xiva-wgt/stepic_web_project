#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djdb;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'qwertypass';"
mysql -uroot -e "GRANT ALL ON djdb.* TO 'django@localhost';"
mysql -uroot -e "GRANT USAGE ON *.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"