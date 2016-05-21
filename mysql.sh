#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djdb;"
mysql -uroot -e "CREATE USER 'django@%' IDENTIFIED BY 'qwertypass';"
mysql -uroot -e "GRANT ALL ON djdb.* TO 'django@%';"
mysql -uroot -e "GRANT USAGE ON *.* TO 'django@%';"
mysql -uroot -e "FLUSH PRIVILEGES;"

GRANT ALL PRIVILEGES ON *.* TO 'UserName'@'%' IDENTIFIED BY 'UnencriptedPa55w0RdHeRe' WITH GRANT OPTION;
FLUSH PRIVILEGES;