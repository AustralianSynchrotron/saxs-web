#wsgi_handler.py

import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'saxs_deployment_apache.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
