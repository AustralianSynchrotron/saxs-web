#!/usr/bin/env python
import os
from distutils.core import setup

setup(
    name='saxs-deployment-apache',
    version='0.0.1',
    packages=['saxs_deployment_apache'],
    data_files = [
        ('/etc/saxs', ['config/saxs-deployment-apache.ini']),
        ('/etc/httpd/conf.d', ['apache/saxs-media.conf', 'apache/saxs-root.conf']),
        ('/usr/share/saxs/deployment/apache', ['apache/saxs.wsgi','manage.py']),
    ],
)
