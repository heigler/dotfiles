#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import os

APT_PACKAGES = [
    'build-essential',
    'python-dev',
    'python-setuptools',
    'libjpeg-dev',
    'zlib1g-dev',
    'libxslt1-dev',
    'libxslt1.1',
    'libxml2-dev',
    'libxml2',
    'libssl-dev',
    'libffi-dev',
    'libmysqlclient-dev',
    'nodejs',
    'npm',
    'git',
]
PIP_PACKAGES = [
    'virtualenv',
    'virtualenvwrapper',
    'bpython',
    'fabric',
]


def system_packages_install():
    apt_data = ' '.join(APT_PACKAGES)
    os.system('sudo apt-get update')
    os.system('sudo apt-get install {0} -y'.format(apt_data))


def system_packages_configure():
    os.system('sudo -H npm install -g bower')
    os.system('sudo easy_install pip')


def python_global_packages_install():
    pip_data = ' '.join(PIP_PACKAGES)
    os.system('sudo pip install {0}'.format(pip_data))


def python_global_packages_configure():
    with open(os.path.expanduser('~/.bashrc'), 'r') as buff:
        bashrc = buff.read()
        if 'WORKON_HOME' in bashrc:
            return None

    os.system('echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc')
    os.system('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc')


if __name__ == '__main__':
    system_packages_install()
    system_packages_configure()
    python_global_packages_install()
    python_global_packages_configure()
