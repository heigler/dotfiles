#!/usr/bin/python
import sys 
import os
from django.conf import settings
try:
    import settings # Assumed to be in the same directory.
    sys.path.insert(0, os.path.join(settings.PROJECT_ROOT, "apps"))
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)
bind = '127.0.0.1:9000'
workers = 3 
worker_connections = 2048
worker_class = 'egg:gunicorn#sync'
logfile = '/tmp/gunicorn_djangoproject.log'
timeout = 3600
