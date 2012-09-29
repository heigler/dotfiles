#!/usr/bin/env python 
import sys 
import os
import multiprocessing
from django.conf import settings
import settings

logdir = os.path.join(settings.PROJECT_ROOT, '..', 'deploy')
if not os.path.exists(logdir):
    os.makedirs(logdir)

bind = '127.0.0.1:9000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1000
worker_class = 'egg:gunicorn#gevent'
logfile = os.path.join(logdir, 'gunicorn.log')
timeout = 60
keepalive = 2
limit_request_line = 2040
limit_request_fields = 100
debug = False
pidfile = os.path.join(logdir, 'pidfile.pid')
loglevel = 'error'

# for development stage, you can import this file and change anything you
# want like in settings.py
