#!/bin/sh
# this script install commons packages for a debian based distro
# should be run as superuser

apt-get install python-setuptools python-dev libjpeg-dev zlib1g-dev -y 
apt-get install g++ make mysql-server postgresql libpq-dev -y

apt-get build-dep python-mysqldb
